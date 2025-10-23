-- 1. 기존의 외래 키 규칙을 먼저 삭제합니다.
ALTER TABLE public.orders
DROP CONSTRAINT orders_project_id_fkey;

-- 2. ON DELETE CASCADE 옵션을 포함하여 새로운 규칙을 추가합니다.
ALTER TABLE public.orders
ADD CONSTRAINT orders_project_id_fkey
FOREIGN KEY (project_id)
REFERENCES public.projects (project_idid)
ON DELETE CASCADE;