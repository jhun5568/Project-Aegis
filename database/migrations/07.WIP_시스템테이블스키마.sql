-- ============================================================================
-- WIP 시스템 v0.6 - Supabase 테이블 생성
-- SQLite → PostgreSQL 전환
-- ============================================================================

-- 1. 고객사 테이블
CREATE TABLE IF NOT EXISTS customers (
    customer_id TEXT PRIMARY KEY,
    customer_name TEXT NOT NULL,
    contact TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 2. 업체 마스터 테이블
CREATE TABLE IF NOT EXISTS vendors (
    vendor_id TEXT PRIMARY KEY,
    vendor_name TEXT NOT NULL,
    contact TEXT,
    process_types TEXT,
    memo TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 3. 프로젝트 테이블
CREATE TABLE IF NOT EXISTS projects (
    project_id TEXT PRIMARY KEY,
    project_name TEXT NOT NULL,
    customer_id TEXT REFERENCES customers(customer_id),
    final_due_date DATE NOT NULL,
    contract_type TEXT DEFAULT '관급',
    contract_amount INTEGER DEFAULT 0,
    installation_completed_date DATE,
    installation_staff_count INTEGER,
    installation_days INTEGER,
    tax_invoice_issued BOOLEAN DEFAULT FALSE,
    trade_statement_issued BOOLEAN DEFAULT FALSE,
    status TEXT DEFAULT '진행중',
    memo TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 4. 발주 테이블
CREATE TABLE IF NOT EXISTS orders (
    order_id TEXT PRIMARY KEY,
    customer_id TEXT REFERENCES customers(customer_id),
    project_id TEXT REFERENCES projects(project_id),
    project TEXT NOT NULL,
    vendor TEXT NOT NULL,
    order_date DATE,
    due_date DATE,
    status TEXT DEFAULT '진행중',
    memo TEXT,
    current_stage TEXT DEFAULT '미시작',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 5. 발주 품목 테이블
CREATE TABLE IF NOT EXISTS order_items (
    item_id SERIAL PRIMARY KEY,
    order_id TEXT NOT NULL REFERENCES orders(order_id) ON DELETE CASCADE,
    item_name TEXT NOT NULL,
    spec TEXT,
    quantity TEXT DEFAULT '1식'
);

-- 6. 공정 진행 이벤트 테이블
CREATE TABLE IF NOT EXISTS process_events (
    event_id SERIAL PRIMARY KEY,
    order_id TEXT NOT NULL REFERENCES orders(order_id) ON DELETE CASCADE,
    stage TEXT NOT NULL,
    progress INTEGER DEFAULT 0,
    planned_date DATE,
    done_date DATE,
    vendor TEXT,
    note TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    created_by TEXT DEFAULT 'USER'
);

-- ============================================================================
-- 인덱스 생성 (성능 최적화)
-- ============================================================================

CREATE INDEX IF NOT EXISTS idx_orders_customer ON orders(customer_id);
CREATE INDEX IF NOT EXISTS idx_orders_project ON orders(project_id);
CREATE INDEX IF NOT EXISTS idx_events_order ON process_events(order_id);
CREATE INDEX IF NOT EXISTS idx_projects_customer ON projects(customer_id);
CREATE INDEX IF NOT EXISTS idx_projects_status ON projects(status);
CREATE INDEX IF NOT EXISTS idx_projects_due_date ON projects(final_due_date);

-- ============================================================================
-- RLS (Row Level Security) 비활성화 - v0.6에서는 로그인 없이 사용
-- ============================================================================

ALTER TABLE customers DISABLE ROW LEVEL SECURITY;
ALTER TABLE vendors DISABLE ROW LEVEL SECURITY;
ALTER TABLE projects DISABLE ROW LEVEL SECURITY;
ALTER TABLE orders DISABLE ROW LEVEL SECURITY;
ALTER TABLE order_items DISABLE ROW LEVEL SECURITY;
ALTER TABLE process_events DISABLE ROW LEVEL SECURITY;

-- ============================================================================
-- 기본 업체 데이터 입력
-- ============================================================================

INSERT INTO vendors (vendor_id, vendor_name, contact, process_types) VALUES
    ('NONE', '작업없음', '', 'CUT,LASER_PIPE,LASER_SHEET,BAND,PAINT,STICKER,RECEIVING'),
    ('OSEONG', '오성벤딩', '', 'BAND'),
    ('HWASEONG', '화성공장', '', 'LASER_PIPE'),
    ('HYUNDAI', '현대도장', '', 'PAINT'),
    ('DUSON', '두손레이저', '', 'LASER_SHEET'),
    ('HYOSUNG', '효성', '', 'CUT')
ON CONFLICT (vendor_id) DO NOTHING;

-- 완료!