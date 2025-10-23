-- Users 테이블 스키마 (향후 로그인 시스템용)
-- 작성일: 2025-10-13

-- 사용자 테이블 생성
CREATE TABLE IF NOT EXISTS ptop.users (
    id BIGSERIAL PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    tenant_id TEXT NOT NULL,
    first_name TEXT,
    last_name TEXT,
    is_active BOOLEAN DEFAULT true,
    is_admin BOOLEAN DEFAULT false,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    last_login_at TIMESTAMP WITH TIME ZONE
);

-- 인덱스 생성
CREATE INDEX IF NOT EXISTS idx_users_email ON ptop.users(email);
CREATE INDEX IF NOT EXISTS idx_users_tenant_id ON ptop.users(tenant_id);
CREATE INDEX IF NOT EXISTS idx_users_is_active ON ptop.users(is_active);
CREATE INDEX IF NOT EXISTS idx_users_created_at ON ptop.users(created_at);

-- Row Level Security (RLS) 정책 활성화
ALTER TABLE ptop.users ENABLE ROW LEVEL SECURITY;

-- 사용자는 자신의 정보만 조회/수정 가능
CREATE POLICY "Users can view own profile" ON ptop.users
    FOR SELECT USING (
        auth.uid()::text = email
    );

CREATE POLICY "Users can update own profile" ON ptop.users
    FOR UPDATE USING (
        auth.uid()::text = email
    );

-- 관리자는 모든 사용자 정보 조회/수정 가능 (향후 구현)
-- CREATE POLICY "Admins can view all users" ON ptop.users
--     FOR SELECT USING (
--         EXISTS (
--             SELECT 1 FROM ptop.users 
--             WHERE auth.uid()::text = email 
--             AND is_admin = true
--         )
--     );

-- 테넌트별 관리자 정책 (향후 구현)
-- CREATE POLICY "Tenant admins can manage their users" ON ptop.users
--     FOR ALL USING (
--         auth.uid()::text IN (
--             SELECT email FROM ptop.users 
--             WHERE tenant_id = current_setting('app.current_tenant')
--             AND is_admin = true
--         )
--     );

-- 샘플 사용자 데이터 (테스트용)
-- INSERT INTO ptop.users (email, password_hash, tenant_id, first_name, last_name, is_admin) VALUES
-- ('admin@dooho.com', 'hashed_password_here', 'dooho', '관리자', '두호', true),
-- ('user1@dooho.com', 'hashed_password_here', 'dooho', '사용자', '일', false),
-- ('admin@kukje.com', 'hashed_password_here', 'kukje', '관리자', '국제', true),
-- ('user1@kukje.com', 'hashed_password_here', 'kukje', '사용자', '일', false);

-- 테이블 정보 확인
SELECT 
    'users 테이블 생성 완료' as status,
    NOW() as created_at;
