-- ============================================================================
-- 라이선스 관리 시스템 (Tenants 테이블)
-- ============================================================================
-- 용도: 회사별 라이선스 활성화/비활성화 중앙 관리
-- 작성일: 2025.10.11
-- ============================================================================

-- tenants 테이블 생성
CREATE TABLE IF NOT EXISTS ptop.tenants (
    tenant_id TEXT PRIMARY KEY,
    company_name TEXT NOT NULL,
    is_active BOOLEAN DEFAULT true,
    license_expires_at TIMESTAMPTZ,
    max_users INT DEFAULT 10,
    contact_email TEXT,
    contact_phone TEXT,
    notes TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 코멘트 추가
COMMENT ON TABLE ptop.tenants IS '회사별 라이선스 관리 테이블';
COMMENT ON COLUMN ptop.tenants.tenant_id IS '회사 식별자 (예: dooho, kukje)';
COMMENT ON COLUMN ptop.tenants.company_name IS '회사명 (예: 두호, 국제)';
COMMENT ON COLUMN ptop.tenants.is_active IS '활성화 여부 (false = 서비스 중지)';
COMMENT ON COLUMN ptop.tenants.license_expires_at IS '라이선스 만료일';
COMMENT ON COLUMN ptop.tenants.max_users IS '최대 사용자 수';
COMMENT ON COLUMN ptop.tenants.contact_email IS '담당자 이메일';
COMMENT ON COLUMN ptop.tenants.contact_phone IS '담당자 연락처';
COMMENT ON COLUMN ptop.tenants.notes IS '메모';

-- 초기 데이터 삽입 (두호, 국제)
INSERT INTO ptop.tenants (tenant_id, company_name, is_active, license_expires_at, max_users, contact_email, notes)
VALUES
    ('dooho', '두호', true, '2026-12-31 23:59:59+09', 10, 'admin@dooho.com', '초기 고객 - 무제한 라이선스'),
    ('kukje', '국제', true, '2026-12-31 23:59:59+09', 10, 'admin@kukje.com', '초기 고객 - 무제한 라이선스')
ON CONFLICT (tenant_id) DO NOTHING;

-- Row Level Security (RLS) 활성화
ALTER TABLE ptop.tenants ENABLE ROW LEVEL SECURITY;

-- 정책: 모든 사용자가 자신의 tenant 정보만 조회 가능
CREATE POLICY tenant_select_policy ON ptop.tenants
    FOR SELECT
    USING (true);  -- 일단 모든 사용자가 조회 가능 (추후 제한 가능)

-- 정책: 관리자만 수정 가능 (추후 구현)
-- CREATE POLICY tenant_update_policy ON ptop.tenants
--     FOR UPDATE
--     USING (auth.jwt() ->> 'role' = 'admin');

-- ============================================================================
-- 사용 예시
-- ============================================================================

-- 1. 라이선스 확인
-- SELECT * FROM ptop.tenants WHERE tenant_id = 'dooho';

-- 2. 서비스 중지 (결제 거부 시)
-- UPDATE ptop.tenants SET is_active = false WHERE tenant_id = 'kukje';

-- 3. 서비스 재개
-- UPDATE ptop.tenants SET is_active = true WHERE tenant_id = 'kukje';

-- 4. 만료일 연장
-- UPDATE ptop.tenants
-- SET license_expires_at = '2027-12-31 23:59:59+09'
-- WHERE tenant_id = 'dooho';

-- 5. 새 고객사 추가
-- INSERT INTO ptop.tenants (tenant_id, company_name, is_active, license_expires_at, max_users)
-- VALUES ('samsung', '삼성', true, '2026-12-31 23:59:59+09', 20);

-- ============================================================================
