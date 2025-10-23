-- 1. 기존 업체 process_types를 한글로 변경
UPDATE vendors SET process_types = '절단/절곡' WHERE process_types = 'CUT';
UPDATE vendors SET process_types = 'P레이저' WHERE process_types = 'PLASER';
UPDATE vendors SET process_types = '레이저(판재)' WHERE process_types = 'LASER_PANEL';
UPDATE vendors SET process_types = '벤딩' WHERE process_types = 'BAND';
UPDATE vendors SET process_types = '페인트' WHERE process_types = 'PAINT';

-- NONE(작업없음)은 모든 공정을 담당하므로
UPDATE vendors 
SET process_types = '절단/절곡,P레이저,레이저(판재),벤딩,페인트,스티커,입고' 
WHERE vendor_id = 'NONE';

-- 2. 스티커, 입고 업체 추가
INSERT INTO vendors (vendor_id, vendor_name, contact, process_types, memo) VALUES
('STICKER', '이노텍', '010-2120-7375', '스티커', '스티커 제작'),
('RECEIVING', '준비완료', '', '입고', '제품 준비 완료');