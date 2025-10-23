-- 사용자별 테넌트 접근 권한 테이블
-- 한 명의 사용자가 여러 테넌트에 접근할 수 있도록 다대다 관계를 정의합니다.
-- 작성일: 2025-10-13

CREATE TABLE IF NOT EXISTS ptop.user_tenant_permissions (
    id BIGSERIAL PRIMARY KEY,
    user_email TEXT NOT NULL,
    tenant_id TEXT NOT NULL,
    role TEXT DEFAULT 'member', -- 'admin', 'member', 'viewer' 등 역할 확장 가능
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    UNIQUE(user_email, tenant_id) -- 중복 권한 방지
);

-- 인덱스 생성
CREATE INDEX IF NOT EXISTS idx_user_tenant_permissions_user_email ON ptop.user_tenant_permissions(user_email);
CREATE INDEX IF NOT EXISTS idx_user_tenant_permissions_tenant_id ON ptop.user_tenant_permissions(tenant_id);

-- 샘플 데이터 (사장님 계정 예시)
-- 이메일 'boss@example.com' 사용자는 'dooho'와 'kukje' 테넌트 모두에 접근 권한을 가집니다.
-- INSERT INTO ptop.user_tenant_permissions (user_email, tenant_id, role) VALUES
-- ('boss@example.com', 'dooho', 'admin'),
-- ('boss@example.com', 'kukje', 'admin');

-- 일반 사용자 예시
-- INSERT INTO ptop.user_tenant_permissions (user_email, tenant_id, role) VALUES
-- ('user1@dooho.com', 'dooho', 'member');

SELECT 'user_tenant_permissions 테이블 스키마 생성 완료' as status;
