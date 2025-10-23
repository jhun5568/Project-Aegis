-- ============================================================================
-- Ptop (Produce-to-Pay) Supabase 스키마
-- 견적/발주/내역서 관리 시스템
-- Multi-tenant 지원 (tenant_id 기반 데이터 격리)
-- ============================================================================

-- 스키마 생성
CREATE SCHEMA IF NOT EXISTS ptop;

-- ============================================================================
-- 1. models 테이블 (모델 마스터)
-- ============================================================================
CREATE TABLE IF NOT EXISTS ptop.models (
    id BIGSERIAL PRIMARY KEY,
    tenant_id TEXT NOT NULL DEFAULT 'dooho',
    model_id TEXT NOT NULL,
    model_name TEXT NOT NULL,
    category TEXT,
    model_standard TEXT,
    quote_number TEXT,
    description TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    CONSTRAINT unique_tenant_model UNIQUE (tenant_id, model_id)
);

CREATE INDEX idx_models_tenant ON ptop.models(tenant_id);
CREATE INDEX idx_models_name ON ptop.models(model_name);
CREATE INDEX idx_models_category ON ptop.models(category);

COMMENT ON TABLE ptop.models IS '모델 마스터 테이블';
COMMENT ON COLUMN ptop.models.tenant_id IS '고객사 ID (dooho, kukje 등)';
COMMENT ON COLUMN ptop.models.model_id IS '모델 고유 ID (DH001, KJ001 등)';
COMMENT ON COLUMN ptop.models.model_name IS '모델명 (DAL01-2012 등)';

-- ============================================================================
-- 2. bom 테이블 (BOM - Bill of Materials)
-- ============================================================================
CREATE TABLE IF NOT EXISTS ptop.bom (
    id BIGSERIAL PRIMARY KEY,
    tenant_id TEXT NOT NULL DEFAULT 'dooho',
    model_id TEXT NOT NULL,
    model_name TEXT,
    material_id TEXT,
    material_name TEXT NOT NULL,
    standard TEXT,
    quantity NUMERIC(10,3) DEFAULT 0,
    unit TEXT DEFAULT 'EA',
    category TEXT,
    material_type TEXT,
    notes TEXT,
    unit_price NUMERIC(12,2),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    CONSTRAINT fk_bom_model FOREIGN KEY (tenant_id, model_id)
        REFERENCES ptop.models(tenant_id, model_id) ON DELETE CASCADE
);

CREATE INDEX idx_bom_tenant ON ptop.bom(tenant_id);
CREATE INDEX idx_bom_model ON ptop.bom(tenant_id, model_id);
CREATE INDEX idx_bom_material ON ptop.bom(material_name);
CREATE INDEX idx_bom_category ON ptop.bom(category);

COMMENT ON TABLE ptop.bom IS 'BOM (Bill of Materials) - 모델별 자재 구성';
COMMENT ON COLUMN ptop.bom.quantity IS '경간당 수량';
COMMENT ON COLUMN ptop.bom.category IS '자재 카테고리 (HGI PIPE, AL CASTING 등)';

-- ============================================================================
-- 3. pricing 테이블 (모델 가격)
-- ============================================================================
CREATE TABLE IF NOT EXISTS ptop.pricing (
    id BIGSERIAL PRIMARY KEY,
    tenant_id TEXT NOT NULL DEFAULT 'dooho',
    no INTEGER,
    product_type TEXT,
    model_name TEXT NOT NULL,
    standard TEXT,
    unit TEXT DEFAULT 'm',
    unit_price NUMERIC(12,2),
    quote_number TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    CONSTRAINT unique_tenant_pricing UNIQUE (tenant_id, model_name)
);

CREATE INDEX idx_pricing_tenant ON ptop.pricing(tenant_id);
CREATE INDEX idx_pricing_model ON ptop.pricing(model_name);

COMMENT ON TABLE ptop.pricing IS '모델별 판매 단가';

-- ============================================================================
-- 4. main_materials 테이블 (주자재 마스터)
-- ============================================================================
CREATE TABLE IF NOT EXISTS ptop.main_materials (
    id BIGSERIAL PRIMARY KEY,
    tenant_id TEXT NOT NULL DEFAULT 'dooho',
    product_name TEXT NOT NULL,
    standard TEXT NOT NULL,
    unit_length_m NUMERIC(10,3),
    unit_price NUMERIC(12,2),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    CONSTRAINT unique_tenant_main_material UNIQUE (tenant_id, product_name, standard)
);

CREATE INDEX idx_main_materials_tenant ON ptop.main_materials(tenant_id);
CREATE INDEX idx_main_materials_product ON ptop.main_materials(product_name);

COMMENT ON TABLE ptop.main_materials IS '주자재 마스터 (PIPE, SHEET 등)';
COMMENT ON COLUMN ptop.main_materials.unit_length_m IS '단위 길이 (미터)';

-- ============================================================================
-- 5. sub_materials 테이블 (부자재 마스터)
-- ============================================================================
CREATE TABLE IF NOT EXISTS ptop.sub_materials (
    id BIGSERIAL PRIMARY KEY,
    tenant_id TEXT NOT NULL DEFAULT 'dooho',
    product_name TEXT NOT NULL,
    standard TEXT,
    unit TEXT DEFAULT 'EA',
    unit_price NUMERIC(12,2),
    notes TEXT,
    supplier TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    CONSTRAINT unique_tenant_sub_material UNIQUE (tenant_id, product_name, standard)
);

CREATE INDEX idx_sub_materials_tenant ON ptop.sub_materials(tenant_id);
CREATE INDEX idx_sub_materials_product ON ptop.sub_materials(product_name);

COMMENT ON TABLE ptop.sub_materials IS '부자재 마스터 (볼트, 너트 등)';

-- ============================================================================
-- 6. inventory 테이블 (재고 관리)
-- ============================================================================
CREATE TABLE IF NOT EXISTS ptop.inventory (
    id BIGSERIAL PRIMARY KEY,
    tenant_id TEXT NOT NULL DEFAULT 'dooho',
    item_id TEXT NOT NULL,
    product_name TEXT,
    standard TEXT,
    thickness TEXT,
    unit_length_m NUMERIC(10,3),
    unit_price NUMERIC(12,2),
    current_quantity NUMERIC(10,2) DEFAULT 0,
    unit TEXT DEFAULT 'EA',
    supplier TEXT,
    notes TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    CONSTRAINT unique_tenant_inventory UNIQUE (tenant_id, item_id)
);

CREATE INDEX idx_inventory_tenant ON ptop.inventory(tenant_id);
CREATE INDEX idx_inventory_item ON ptop.inventory(item_id);
CREATE INDEX idx_inventory_product ON ptop.inventory(product_name);

COMMENT ON TABLE ptop.inventory IS '재고 관리';
COMMENT ON COLUMN ptop.inventory.current_quantity IS '현재 재고 수량';

-- ============================================================================
-- Row Level Security (RLS) 설정
-- ============================================================================

-- RLS 활성화
ALTER TABLE ptop.models ENABLE ROW LEVEL SECURITY;
ALTER TABLE ptop.bom ENABLE ROW LEVEL SECURITY;
ALTER TABLE ptop.pricing ENABLE ROW LEVEL SECURITY;
ALTER TABLE ptop.main_materials ENABLE ROW LEVEL SECURITY;
ALTER TABLE ptop.sub_materials ENABLE ROW LEVEL SECURITY;
ALTER TABLE ptop.inventory ENABLE ROW LEVEL SECURITY;

-- 정책: tenant_id 기반 필터링 (읽기)
-- 주의: app.current_tenant 설정을 앱에서 해야 함
-- 예: SET LOCAL app.current_tenant = 'dooho';

CREATE POLICY "tenant_isolation_select_models" ON ptop.models
    FOR SELECT
    USING (
        tenant_id = COALESCE(
            current_setting('app.current_tenant', true),
            'dooho'
        )
    );

CREATE POLICY "tenant_isolation_select_bom" ON ptop.bom
    FOR SELECT
    USING (
        tenant_id = COALESCE(
            current_setting('app.current_tenant', true),
            'dooho'
        )
    );

CREATE POLICY "tenant_isolation_select_pricing" ON ptop.pricing
    FOR SELECT
    USING (
        tenant_id = COALESCE(
            current_setting('app.current_tenant', true),
            'dooho'
        )
    );

CREATE POLICY "tenant_isolation_select_main_materials" ON ptop.main_materials
    FOR SELECT
    USING (
        tenant_id = COALESCE(
            current_setting('app.current_tenant', true),
            'dooho'
        )
    );

CREATE POLICY "tenant_isolation_select_sub_materials" ON ptop.sub_materials
    FOR SELECT
    USING (
        tenant_id = COALESCE(
            current_setting('app.current_tenant', true),
            'dooho'
        )
    );

CREATE POLICY "tenant_isolation_select_inventory" ON ptop.inventory
    FOR SELECT
    USING (
        tenant_id = COALESCE(
            current_setting('app.current_tenant', true),
            'dooho'
        )
    );

-- 정책: INSERT/UPDATE/DELETE (서비스 역할만 허용, 나중에 필요시 수정)
CREATE POLICY "service_role_insert_models" ON ptop.models
    FOR INSERT
    WITH CHECK (true);

CREATE POLICY "service_role_update_models" ON ptop.models
    FOR UPDATE
    USING (true);

CREATE POLICY "service_role_delete_models" ON ptop.models
    FOR DELETE
    USING (true);

-- BOM, Pricing, Materials, Inventory도 동일하게 적용
-- (간결성을 위해 생략, 필요시 models 패턴 복사)

-- ============================================================================
-- 트리거: updated_at 자동 갱신
-- ============================================================================

CREATE OR REPLACE FUNCTION ptop.update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_models_updated_at BEFORE UPDATE ON ptop.models
    FOR EACH ROW EXECUTE FUNCTION ptop.update_updated_at_column();

CREATE TRIGGER update_bom_updated_at BEFORE UPDATE ON ptop.bom
    FOR EACH ROW EXECUTE FUNCTION ptop.update_updated_at_column();

CREATE TRIGGER update_pricing_updated_at BEFORE UPDATE ON ptop.pricing
    FOR EACH ROW EXECUTE FUNCTION ptop.update_updated_at_column();

CREATE TRIGGER update_main_materials_updated_at BEFORE UPDATE ON ptop.main_materials
    FOR EACH ROW EXECUTE FUNCTION ptop.update_updated_at_column();

CREATE TRIGGER update_sub_materials_updated_at BEFORE UPDATE ON ptop.sub_materials
    FOR EACH ROW EXECUTE FUNCTION ptop.update_updated_at_column();

CREATE TRIGGER update_inventory_updated_at BEFORE UPDATE ON ptop.inventory
    FOR EACH ROW EXECUTE FUNCTION ptop.update_updated_at_column();

-- ============================================================================
-- 7. document_archive 테이블 (문서 보관소) - public 스키마
-- ============================================================================
CREATE TABLE IF NOT EXISTS public.document_archive (
    id TEXT PRIMARY KEY,
    tenant_id TEXT NOT NULL,
    project_id TEXT NOT NULL,
    project_name TEXT NOT NULL,
    document_type TEXT NOT NULL,
    storage_path TEXT NOT NULL,
    filename TEXT NOT NULL,
    file_size BIGINT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    created_by TEXT,
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_document_archive_tenant ON public.document_archive(tenant_id);
CREATE INDEX idx_document_archive_project ON public.document_archive(tenant_id, project_name);
CREATE INDEX idx_document_archive_type ON public.document_archive(document_type);
CREATE INDEX idx_document_archive_created ON public.document_archive(created_at DESC);

COMMENT ON TABLE public.document_archive IS '생성된 문서 보관소 (견적서, 발주서, 내역서)';
COMMENT ON COLUMN public.document_archive.tenant_id IS '고객사 ID (dooho, kukje 등)';
COMMENT ON COLUMN public.document_archive.project_name IS '현장명 (샘플초등학교 등)';
COMMENT ON COLUMN public.document_archive.document_type IS '문서 타입 (quotation, po, bom)';
COMMENT ON COLUMN public.document_archive.storage_path IS 'Supabase Storage 경로';
COMMENT ON COLUMN public.document_archive.filename IS '원본 파일명 (한글 가능)';

-- RLS 활성화
ALTER TABLE public.document_archive ENABLE ROW LEVEL SECURITY;

-- 정책: tenant_id 기반 SELECT (읽기)
CREATE POLICY "tenant_isolation_select_document_archive" ON public.document_archive
    FOR SELECT
    USING (
        tenant_id = COALESCE(
            current_setting('app.current_tenant', true),
            'dooho'
        )
    );

-- 정책: INSERT (모든 인증된 사용자 허용)
CREATE POLICY "allow_insert_document_archive" ON public.document_archive
    FOR INSERT
    WITH CHECK (true);

-- 정책: DELETE (모든 인증된 사용자 허용)
CREATE POLICY "allow_delete_document_archive" ON public.document_archive
    FOR DELETE
    USING (true);

-- ============================================================================
-- 완료
-- ============================================================================

-- 스키마 확인 쿼리
-- SELECT table_name FROM information_schema.tables WHERE table_schema = 'ptop';
