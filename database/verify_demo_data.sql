-- Demo 테넌트 데이터 검증 쿼리
-- Supabase SQL 콘솔에서 실행하세요

-- 1. Demo 테넌트의 모델 개수 확인
SELECT COUNT(*) as model_count, tenant_id
FROM ptop.models
WHERE tenant_id = 'demo'
GROUP BY tenant_id;

-- 2. 테넌트별 모델 수 비교
SELECT tenant_id, COUNT(*) as model_count
FROM ptop.models
GROUP BY tenant_id
ORDER BY model_count DESC;

-- 3. Demo 테넌트의 모든 모델 확인 (최근 20개)
SELECT id, tenant_id, model_id, model_name, category, model_standard
FROM ptop.models
WHERE tenant_id = 'demo'
ORDER BY created_at DESC
LIMIT 20;

-- 4. Demo 테넌트의 카테고리별 모델 수
SELECT category, COUNT(*) as count
FROM ptop.models
WHERE tenant_id = 'demo'
GROUP BY category
ORDER BY category;

-- 5. Demo 테넌트의 BOM 데이터 개수
SELECT COUNT(*) as bom_count
FROM ptop.bom
WHERE tenant_id = 'demo';

-- 6. Demo 테넌트의 주요 자재 확인
SELECT COUNT(*) as material_count
FROM ptop.main_materials
WHERE tenant_id = 'demo';
