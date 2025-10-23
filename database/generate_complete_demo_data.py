#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aegis-Demo 테넌트용 완전한 샘플 데이터 생성
models, bom, pricing, main_materials, sub_materials, inventory 테이블 포함
"""

# 모델 데이터
models_data = {
    '디자인형울타리': [
        ('DESIGN_FENCE_001', '디자인형울타리-기본형 1000H', '1000x2000mm', 'DF-001', 'QT-2025-DF001'),
        ('DESIGN_FENCE_002', '디자인형울타리-라운드톱 1200H', '1200x2000mm', 'DF-002', 'QT-2025-DF002'),
        ('DESIGN_FENCE_003', '디자인형울타리-모던형 1000H', '1000x2000mm', 'DF-003', 'QT-2025-DF003'),
        ('DESIGN_FENCE_004', '디자인형울타리-곡선형 1100H', '1100x2000mm', 'DF-004', 'QT-2025-DF004'),
        ('DESIGN_FENCE_005', '디자인형울타리-기하학형 1050H', '1050x2000mm', 'DF-005', 'QT-2025-DF005'),
        ('DESIGN_FENCE_006', '디자인형울타리-스트라이프 1000H', '1000x2000mm', 'DF-006', 'QT-2025-DF006'),
        ('DESIGN_FENCE_007', '디자인형울타리-대각선 1150H', '1150x2000mm', 'DF-007', 'QT-2025-DF007'),
        ('DESIGN_FENCE_008', '디자인형울타리-프레임형 1000H', '1000x2000mm', 'DF-008', 'QT-2025-DF008'),
        ('DESIGN_FENCE_009', '디자인형울타리-나무결 1200H', '1200x2000mm', 'DF-009', 'QT-2025-DF009'),
        ('DESIGN_FENCE_010', '디자인형울타리-미니멀 900H', '900x2000mm', 'DF-010', 'QT-2025-DF010'),
    ],
    '금속재기타울타리': [
        ('METAL_FENCE_001', '금속재기타울타리-앵글형 1000H', '1000x2000mm', 'MF-001', 'QT-2025-MF001'),
        ('METAL_FENCE_002', '금속재기타울타리-파이프형 1200H', '1200x2000mm', 'MF-002', 'QT-2025-MF002'),
        ('METAL_FENCE_003', '금속재기타울타리-체인링크 1000H', '1000x2000mm', 'MF-003', 'QT-2025-MF003'),
        ('METAL_FENCE_004', '금속재기타울타리-메쉬형 1100H', '1100x2000mm', 'MF-004', 'QT-2025-MF004'),
        ('METAL_FENCE_005', '금속재기타울타리-박스빔 1150H', '1150x2000mm', 'MF-005', 'QT-2025-MF005'),
        ('METAL_FENCE_006', '금속재기타울타리-철봉격자 1050H', '1050x2000mm', 'MF-006', 'QT-2025-MF006'),
        ('METAL_FENCE_007', '금속재기타울타리-스틸플레이트 1000H', '1000x2000mm', 'MF-007', 'QT-2025-MF007'),
        ('METAL_FENCE_008', '금속재기타울타리-구조강재 1200H', '1200x2000mm', 'MF-008', 'QT-2025-MF008'),
        ('METAL_FENCE_009', '금속재기타울타리-갈바강판 1100H', '1100x2000mm', 'MF-009', 'QT-2025-MF009'),
        ('METAL_FENCE_010', '금속재기타울타리-알루미늄 900H', '900x2000mm', 'MF-010', 'QT-2025-MF010'),
    ],
    '창살형울타리': [
        ('SPINDLE_FENCE_001', '창살형울타리-수직창살 1000H', '1000x2000mm', 'SF-001', 'QT-2025-SF001'),
        ('SPINDLE_FENCE_002', '창살형울타리-x자형 1200H', '1200x2000mm', 'SF-002', 'QT-2025-SF002'),
        ('SPINDLE_FENCE_003', '창살형울타리-다이아몬드 1000H', '1000x2000mm', 'SF-003', 'QT-2025-SF003'),
        ('SPINDLE_FENCE_004', '창살형울타리-원형봉 1100H', '1100x2000mm', 'SF-004', 'QT-2025-SF004'),
        ('SPINDLE_FENCE_005', '창살형울타리-각형봉 1050H', '1050x2000mm', 'SF-005', 'QT-2025-SF005'),
        ('SPINDLE_FENCE_006', '창살형울타리-경사창살 1000H', '1000x2000mm', 'SF-006', 'QT-2025-SF006'),
        ('SPINDLE_FENCE_007', '창살형울타리-조밀창살 1150H', '1150x2000mm', 'SF-007', 'QT-2025-SF007'),
        ('SPINDLE_FENCE_008', '창살형울타리-성글창살 1000H', '1000x2000mm', 'SF-008', 'QT-2025-SF008'),
        ('SPINDLE_FENCE_009', '창살형울타리-계단형 1200H', '1200x2000mm', 'SF-009', 'QT-2025-SF009'),
        ('SPINDLE_FENCE_010', '창살형울타리-물결형 900H', '900x2000mm', 'SF-010', 'QT-2025-SF010'),
    ],
    '차양': [
        ('AWNING_001', '차양-수동 알루미늄 2000W', '2000x1500mm', 'AW-001', 'QT-2025-AW001'),
        ('AWNING_002', '차양-반자동 스틸 2500W', '2500x1500mm', 'AW-002', 'QT-2025-AW002'),
        ('AWNING_003', '차양-전동 프리미엄 3000W', '3000x1500mm', 'AW-003', 'QT-2025-AW003'),
        ('AWNING_004', '차양-카세트형 2000W', '2000x1200mm', 'AW-004', 'QT-2025-AW004'),
        ('AWNING_005', '차양-반투명캔버스 2200W', '2200x1500mm', 'AW-005', 'QT-2025-AW005'),
        ('AWNING_006', '차양-방수천 2400W', '2400x1500mm', 'AW-006', 'QT-2025-AW006'),
        ('AWNING_007', '차양-방풍형 2000W', '2000x1500mm', 'AW-007', 'QT-2025-AW007'),
        ('AWNING_008', '차양-LED조명 2500W', '2500x1500mm', 'AW-008', 'QT-2025-AW008'),
        ('AWNING_009', '차양-태양광 3000W', '3000x1500mm', 'AW-009', 'QT-2025-AW009'),
        ('AWNING_010', '차양-리모콘식 2200W', '2200x1500mm', 'AW-010', 'QT-2025-AW010'),
    ],
    '자전거보관대': [
        ('BIKE_RACK_001', '자전거보관대-벽부착형 2대용', '600x400x200mm', 'BR-001', 'QT-2025-BR001'),
        ('BIKE_RACK_002', '자전거보관대-스탠드형 4대용', '1200x400x400mm', 'BR-002', 'QT-2025-BR002'),
        ('BIKE_RACK_003', '자전거보관대-수평거치 3대용', '900x400x300mm', 'BR-003', 'QT-2025-BR003'),
        ('BIKE_RACK_004', '자전거보관대-라운드형 6대용', '1500x500x500mm', 'BR-004', 'QT-2025-BR004'),
        ('BIKE_RACK_005', '자전거보관대-접이식 2대용', '500x300x150mm', 'BR-005', 'QT-2025-BR005'),
        ('BIKE_RACK_006', '자전거보관대-타워형 8대용', '1200x600x800mm', 'BR-006', 'QT-2025-BR006'),
        ('BIKE_RACK_007', '자전거보관대-잠금함일체형 2대', '700x400x250mm', 'BR-007', 'QT-2025-BR007'),
        ('BIKE_RACK_008', '자전거보관대-슬랫형 5대용', '1000x300x400mm', 'BR-008', 'QT-2025-BR008'),
        ('BIKE_RACK_009', '자전거보관대-개별칸막이 4대', '800x400x450mm', 'BR-009', 'QT-2025-BR009'),
        ('BIKE_RACK_010', '자전거보관대-우산겸용 3대용', '900x400x250mm', 'BR-010', 'QT-2025-BR010'),
    ],
}

# 주요 자재 (Main Materials)
main_materials = [
    ('MM-PIPE-50', 'HGI PIPE 50mm', '50x50x1.6', '6.0', 45000),
    ('MM-PIPE-75', 'HGI PIPE 75mm', '75x75x2.3', '6.0', 68000),
    ('MM-ANGLE-50', 'ANGLE STEEL 50mm', '50x50x5', '6.0', 52000),
    ('MM-PLATE-10', 'STEEL PLATE 10mm', '1000x2000x10', '1.0', 85000),
    ('MM-AL-PROF', 'AL PROFILE', '40x40x2', '6.0', 38000),
    ('MM-BOLT-M16', 'BOLT M16', 'M16x50', '1.0', 2500),
]

# 보조 자재 (Sub Materials)
sub_materials = [
    ('SM-WELD', '용접', 'EA', 5000),
    ('SM-PAINT', '페인트', 'L', 15000),
    ('SM-NUT', '너트 M16', 'EA', 800),
    ('SM-WASHER', '와셔', 'EA', 500),
    ('SM-CONCRETE', '콘크리트 기초', 'EA', 25000),
]

def escape_sql(text):
    """SQL 문자열 이스케이프"""
    if text is None:
        return 'null'
    return "'" + str(text).replace("'", "''") + "'"

sql_lines = []
sql_lines.append("-- Aegis-Demo 테넌트 완전한 샘플 데이터")
sql_lines.append("-- models, bom, pricing, main_materials, sub_materials, inventory")
sql_lines.append("")

# 1. MAIN_MATERIALS 삽입
sql_lines.append("-- 1. 주요 자재 (Main Materials) 삽입")
for material_id, name, standard, length, price in main_materials:
    sql_lines.append(
        f"INSERT INTO ptop.main_materials (tenant_id, product_name, standard, unit_length_m, unit_price) "
        f"VALUES ('demo', {escape_sql(name)}, {escape_sql(standard)}, {escape_sql(length)}, {price});"
    )
sql_lines.append("")

# 2. SUB_MATERIALS 삽입
sql_lines.append("-- 2. 보조 자재 (Sub Materials) 삽입")
for material_id, name, unit, price in sub_materials:
    sql_lines.append(
        f"INSERT INTO ptop.sub_materials (tenant_id, product_name, unit, unit_price) "
        f"VALUES ('demo', {escape_sql(name)}, {escape_sql(unit)}, {price});"
    )
sql_lines.append("")

# 3. INVENTORY 삽입 (재고 초기화)
sql_lines.append("-- 3. 재고 (Inventory) 초기화")
for material_id, name, standard, length, _ in main_materials:
    sql_lines.append(
        f"INSERT INTO ptop.inventory (tenant_id, item_id, product_name, standard, unit_price, current_quantity, unit) "
        f"VALUES ('demo', {escape_sql(material_id)}, {escape_sql(name)}, {escape_sql(standard)}, 45000, 100, 'EA');"
    )
sql_lines.append("")

# 4. MODELS 삽입
sql_lines.append("-- 4. 모델 (Models) 삽입")
for category, models in models_data.items():
    sql_lines.append(f"-- {category} 모델")
    for model_id, model_name, standard, identifier, quote_num in models:
        sql_lines.append(
            f"INSERT INTO ptop.models (tenant_id, model_id, model_name, category, model_standard, "
            f"quote_number, description) "
            f"VALUES ('demo', {escape_sql(model_id)}, {escape_sql(model_name)}, {escape_sql(category)}, "
            f"{escape_sql(standard)}, {escape_sql(quote_num)}, {escape_sql(model_name + ' 시리즈')});"
        )
    sql_lines.append("")

# 5. BOM 삽입 (각 모델별 자재 구성)
sql_lines.append("-- 5. BOM (Bill of Materials) 삽입")
bom_idx = 1
for category, models in models_data.items():
    for model_id, model_name, _, _, _ in models:
        # 각 모델마다 주요 자재 2개, 보조 자재 2개 할당
        for i, (mat_id, mat_name, mat_std, _, mat_price) in enumerate(main_materials[:2]):
            qty = 2 + (i % 3)
            sql_lines.append(
                f"INSERT INTO ptop.bom (tenant_id, model_id, model_name, material_id, material_name, "
                f"standard, quantity, unit, unit_price) "
                f"VALUES ('demo', {escape_sql(model_id)}, {escape_sql(model_name)}, {escape_sql(mat_id)}, "
                f"{escape_sql(mat_name)}, {escape_sql(mat_std)}, {qty}, 'EA', {mat_price});"
            )
        for sub_id, sub_name, sub_unit, sub_price in sub_materials[:2]:
            qty = 1 + (bom_idx % 2)
            sql_lines.append(
                f"INSERT INTO ptop.bom (tenant_id, model_id, model_name, material_name, "
                f"quantity, unit, unit_price) "
                f"VALUES ('demo', {escape_sql(model_id)}, {escape_sql(model_name)}, {escape_sql(sub_name)}, "
                f"{qty}, {escape_sql(sub_unit)}, {sub_price});"
            )
        bom_idx += 1
sql_lines.append("")

# 6. PRICING 삽입
sql_lines.append("-- 6. 가격 책정 (Pricing) 삽입")
pricing_no = 1
for category, models in models_data.items():
    for model_id, model_name, standard, _, quote_num in models:
        base_price = 500000 + (pricing_no * 50000)
        sql_lines.append(
            f"INSERT INTO ptop.pricing (tenant_id, no, product_type, model_name, standard, unit, "
            f"unit_price, quote_number) "
            f"VALUES ('demo', {pricing_no}, {escape_sql(category)}, {escape_sql(model_name)}, "
            f"{escape_sql(standard)}, 'm', {base_price}, {escape_sql(quote_num)});"
        )
        pricing_no += 1
sql_lines.append("")

sql_content = "\n".join(sql_lines)

# 파일에 저장
output_file = r"c:\Users\JUN\Desktop\Auto-CVS-Project\database\demo_complete_sample_data.sql"
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(sql_content)

print(f"[OK] 완전한 샘플 데이터 SQL 생성 완료")
print(f"[OK] 파일: {output_file}")
print(f"[OK] 포함 항목:")
print(f"     - main_materials: {len(main_materials)}개")
print(f"     - sub_materials: {len(sub_materials)}개")
print(f"     - models: 50개 (5 카테고리 x 10개)")
print(f"     - bom: {50 * 4}개 (모델당 4개 자재)")
print(f"     - pricing: 50개")
print(f"     - inventory: {len(main_materials)}개")
