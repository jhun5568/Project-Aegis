-- Phase 3 RLS policies (DEV-friendly)
-- Copy/paste into Supabase SQL Editor AFTER creating the Phase 3 tables (08/09 migrations).
-- This enables RLS and adds permissive DEV policies (anon can SELECT/INSERT/UPDATE/DELETE).
-- For production, remove anon write policies and switch to authenticated + tenant-isolated rules.

-- Helper: apply RLS + DEV policies only if the table exists
-- Usage: call apply_policies('<table_name>');
CREATE OR REPLACE FUNCTION apply_policies(tbl text) RETURNS void AS $$
DECLARE
  q text;
BEGIN
  IF to_regclass('public.'||tbl) IS NULL THEN
    RAISE NOTICE 'Skip %, table not found', tbl;
    RETURN;
  END IF;

  -- Enable RLS
  EXECUTE format('ALTER TABLE %I ENABLE ROW LEVEL SECURITY;', tbl);

  -- Drop existing DEV policies (idempotent)
  FOR q IN SELECT
      format('DROP POLICY IF EXISTS %I ON %I;', 'dev_anon_select_'||tbl, tbl) UNION ALL
      SELECT format('DROP POLICY IF EXISTS %I ON %I;', 'dev_anon_insert_'||tbl, tbl) UNION ALL
      SELECT format('DROP POLICY IF EXISTS %I ON %I;', 'dev_anon_update_'||tbl, tbl) UNION ALL
      SELECT format('DROP POLICY IF EXISTS %I ON %I;', 'dev_anon_delete_'||tbl, tbl)
  LOOP
    EXECUTE q;
  END LOOP;

  -- DEV policies: allow anon read/write (adjust before production)
  EXECUTE format('CREATE POLICY %I ON %I FOR SELECT TO anon USING (true);', 'dev_anon_select_'||tbl, tbl);
  EXECUTE format('CREATE POLICY %I ON %I FOR INSERT TO anon WITH CHECK (true);', 'dev_anon_insert_'||tbl, tbl);
  EXECUTE format('CREATE POLICY %I ON %I FOR UPDATE TO anon USING (true) WITH CHECK (true);', 'dev_anon_update_'||tbl, tbl);
  EXECUTE format('CREATE POLICY %I ON %I FOR DELETE TO anon USING (true);', 'dev_anon_delete_'||tbl, tbl);

  RAISE NOTICE 'Applied DEV RLS policies to %', tbl;
END;
$$ LANGUAGE plpgsql;

-- Apply to Phase 3 tables
SELECT apply_policies('quotations');
SELECT apply_policies('quotation_items');
SELECT apply_policies('purchase_orders');
SELECT apply_policies('po_items');
SELECT apply_policies('inventory');
SELECT apply_policies('inventory_txns');
SELECT apply_policies('bom_snapshots');

-- Optional: drop helper when done
-- DROP FUNCTION IF EXISTS apply_policies(text);

-- Notes for production hardening:
-- 1) Remove anon INSERT/UPDATE/DELETE policies (and possibly anon SELECT).
-- 2) Add authenticated policies with tenant isolation, for example:
--    CREATE POLICY tenant_select_quotations ON quotations FOR SELECT TO authenticated
--    USING (EXISTS (SELECT 1 FROM user_tenant_permissions p
--                   WHERE p.user_id = auth.uid() AND p.tenant_id = quotations.tenant_id));
--    CREATE POLICY tenant_write_quotations ON quotations FOR INSERT TO authenticated
--    WITH CHECK (EXISTS (SELECT 1 FROM user_tenant_permissions p
--                        WHERE p.user_id = auth.uid() AND p.tenant_id = quotations.tenant_id));
--    -- Repeat similarly for UPDATE/DELETE and the other Phase 3 tables.

