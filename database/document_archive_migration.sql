-- ============================================================================
-- document_archive 테이블 생성 및 RLS 설정
-- Supabase 대시보드 → SQL Editor에서 실행하세요
-- ============================================================================

-- 1. document_archive 테이블 생성
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

-- 2. 인덱스 생성 (검색 성능)
CREATE INDEX IF NOT EXISTS idx_document_archive_tenant ON public.document_archive(tenant_id);
CREATE INDEX IF NOT EXISTS idx_document_archive_project ON public.document_archive(tenant_id, project_name);
CREATE INDEX IF NOT EXISTS idx_document_archive_type ON public.document_archive(document_type);
CREATE INDEX IF NOT EXISTS idx_document_archive_created ON public.document_archive(created_at DESC);

-- 3. 테이블 설명
COMMENT ON TABLE public.document_archive IS '생성된 문서 보관소 (견적서, 발주서, 내역서)';
COMMENT ON COLUMN public.document_archive.id IS 'UUID 고유 ID';
COMMENT ON COLUMN public.document_archive.tenant_id IS '고객사 ID (dooho, kukje 등)';
COMMENT ON COLUMN public.document_archive.project_id IS '현장 ID';
COMMENT ON COLUMN public.document_archive.project_name IS '현장명 (샘플초등학교 등)';
COMMENT ON COLUMN public.document_archive.document_type IS '문서 타입 (quotation=견적서, po=발주서, bom=내역서)';
COMMENT ON COLUMN public.document_archive.storage_path IS 'Supabase Storage 경로';
COMMENT ON COLUMN public.document_archive.filename IS '원본 파일명 (한글 가능)';
COMMENT ON COLUMN public.document_archive.file_size IS '파일 크기 (바이트)';
COMMENT ON COLUMN public.document_archive.created_by IS '작성자 ID';

-- 4. RLS 활성화
ALTER TABLE public.document_archive ENABLE ROW LEVEL SECURITY;

-- 5. RLS 정책 설정

-- 5-1. SELECT (읽기) 정책 - tenant_id 기반 필터링
CREATE POLICY "allow_select_document_archive" ON public.document_archive
    FOR SELECT
    TO authenticated
    USING (true);  -- 먼저 모든 인증된 사용자 허용 (나중에 tenant_id로 제한 가능)

-- 5-2. INSERT (작성) 정책 - 모든 인증된 사용자 허용
CREATE POLICY "allow_insert_document_archive" ON public.document_archive
    FOR INSERT
    TO authenticated
    WITH CHECK (true);

-- 5-3. DELETE (삭제) 정책 - 모든 인증된 사용자 허용
CREATE POLICY "allow_delete_document_archive" ON public.document_archive
    FOR DELETE
    TO authenticated
    USING (true);

-- ============================================================================
-- Storage 버킷 RLS 설정 (수동으로 대시보드에서 설정 필요)
-- ============================================================================
--
-- Supabase 대시보드 → Storage → ptop-files 버킷 → Policies 에서:
--
-- 1. 업로드 정책:
--    CREATE POLICY "Allow uploads"
--    ON storage.objects FOR INSERT
--    TO authenticated
--    WITH CHECK (bucket_id = 'ptop-files');
--
-- 2. 다운로드 정책:
--    CREATE POLICY "Allow downloads"
--    ON storage.objects FOR SELECT
--    TO authenticated
--    USING (bucket_id = 'ptop-files');
--
-- 3. 삭제 정책:
--    CREATE POLICY "Allow deletes"
--    ON storage.objects FOR DELETE
--    TO authenticated
--    USING (bucket_id = 'ptop-files');

-- ============================================================================
-- 완료
-- ============================================================================
-- 이 스크립트를 실행한 후, 위의 Storage RLS 정책도 설정하세요.
