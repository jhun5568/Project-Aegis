#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aegis-Demo 테넌트용 샘플 데이터 생성 스크립트
ptop.models 테이블에 5개 카테고리별 10개 모델씩 INSERT 쿼리 생성
"""

categories_data = {
    '디자인형울타리': [
        ('DESIGN_FENCE_001', '디자인형울타리-기본형 1000H', '1000x2000mm'),
        ('DESIGN_FENCE_002', '디자인형울타리-라운드톱 1200H', '1200x2000mm'),
        ('DESIGN_FENCE_003', '디자인형울타리-모던형 1000H', '1000x2000mm'),
        ('DESIGN_FENCE_004', '디자인형울타리-곡선형 1100H', '1100x2000mm'),
        ('DESIGN_FENCE_005', '디자인형울타리-기하학형 1050H', '1050x2000mm'),
        ('DESIGN_FENCE_006', '디자인형울타리-스트라이프 1000H', '1000x2000mm'),
        ('DESIGN_FENCE_007', '디자인형울타리-대각선 1150H', '1150x2000mm'),
        ('DESIGN_FENCE_008', '디자인형울타리-프레임형 1000H', '1000x2000mm'),
        ('DESIGN_FENCE_009', '디자인형울타리-나무결 1200H', '1200x2000mm'),
        ('DESIGN_FENCE_010', '디자인형울타리-미니멀 900H', '900x2000mm'),
    ],
    '금속재기타울타리': [
        ('METAL_FENCE_001', '금속재기타울타리-앵글형 1000H', '1000x2000mm'),
        ('METAL_FENCE_002', '금속재기타울타리-파이프형 1200H', '1200x2000mm'),
        ('METAL_FENCE_003', '금속재기타울타리-체인링크 1000H', '1000x2000mm'),
        ('METAL_FENCE_004', '금속재기타울타리-메쉬형 1100H', '1100x2000mm'),
        ('METAL_FENCE_005', '금속재기타울타리-박스빔 1150H', '1150x2000mm'),
        ('METAL_FENCE_006', '금속재기타울타리-철봉격자 1050H', '1050x2000mm'),
        ('METAL_FENCE_007', '금속재기타울타리-스틸플레이트 1000H', '1000x2000mm'),
        ('METAL_FENCE_008', '금속재기타울타리-구조강재 1200H', '1200x2000mm'),
        ('METAL_FENCE_009', '금속재기타울타리-갈바강판 1100H', '1100x2000mm'),
        ('METAL_FENCE_010', '금속재기타울타리-알루미늄 900H', '900x2000mm'),
    ],
    '창살형울타리': [
        ('SPINDLE_FENCE_001', '창살형울타리-수직창살 1000H', '1000x2000mm'),
        ('SPINDLE_FENCE_002', '창살형울타리-x자형 1200H', '1200x2000mm'),
        ('SPINDLE_FENCE_003', '창살형울타리-다이아몬드 1000H', '1000x2000mm'),
        ('SPINDLE_FENCE_004', '창살형울타리-원형봉 1100H', '1100x2000mm'),
        ('SPINDLE_FENCE_005', '창살형울타리-각형봉 1050H', '1050x2000mm'),
        ('SPINDLE_FENCE_006', '창살형울타리-경사창살 1000H', '1000x2000mm'),
        ('SPINDLE_FENCE_007', '창살형울타리-조밀창살 1150H', '1150x2000mm'),
        ('SPINDLE_FENCE_008', '창살형울타리-성글창살 1000H', '1000x2000mm'),
        ('SPINDLE_FENCE_009', '창살형울타리-계단형 1200H', '1200x2000mm'),
        ('SPINDLE_FENCE_010', '창살형울타리-물결형 900H', '900x2000mm'),
    ],
    '차양': [
        ('AWNING_001', '차양-수동 알루미늄 2000W', '2000x1500mm'),
        ('AWNING_002', '차양-반자동 스틸 2500W', '2500x1500mm'),
        ('AWNING_003', '차양-전동 프리미엄 3000W', '3000x1500mm'),
        ('AWNING_004', '차양-카세트형 2000W', '2000x1200mm'),
        ('AWNING_005', '차양-반투명캔버스 2200W', '2200x1500mm'),
        ('AWNING_006', '차양-방수천 2400W', '2400x1500mm'),
        ('AWNING_007', '차양-방풍형 2000W', '2000x1500mm'),
        ('AWNING_008', '차양-LED조명 2500W', '2500x1500mm'),
        ('AWNING_009', '차양-태양광 3000W', '3000x1500mm'),
        ('AWNING_010', '차양-리모콘식 2200W', '2200x1500mm'),
    ],
    '자전거보관대': [
        ('BIKE_RACK_001', '자전거보관대-벽부착형 2대용', '600x400x200mm'),
        ('BIKE_RACK_002', '자전거보관대-스탠드형 4대용', '1200x400x400mm'),
        ('BIKE_RACK_003', '자전거보관대-수평거치 3대용', '900x400x300mm'),
        ('BIKE_RACK_004', '자전거보관대-라운드형 6대용', '1500x500x500mm'),
        ('BIKE_RACK_005', '자전거보관대-접이식 2대용', '500x300x150mm'),
        ('BIKE_RACK_006', '자전거보관대-타워형 8대용', '1200x600x800mm'),
        ('BIKE_RACK_007', '자전거보관대-잠금함일체형 2대', '700x400x250mm'),
        ('BIKE_RACK_008', '자전거보관대-슬랫형 5대용', '1000x300x400mm'),
        ('BIKE_RACK_009', '자전거보관대-개별칸막이 4대', '800x400x450mm'),
        ('BIKE_RACK_010', '자전거보관대-우산겸용 3대용', '900x400x250mm'),
    ],
}

category_codes = {
    '디자인형울타리': 'DF',
    '금속재기타울타리': 'MF',
    '창살형울타리': 'SF',
    '차양': 'AW',
    '자전거보관대': 'BR',
}

def escape_sql(text):
    """SQL 문자열 이스케이프"""
    return text.replace("'", "''")

# SQL 생성
sql_lines = []
sql_lines.append("-- Aegis-Demo 테넌트용 샘플 데이터")
sql_lines.append("-- ptop.models 테이블에 5개 카테고리별 10개 모델씩 생성 (총 50개)")
sql_lines.append("")

for category, models in categories_data.items():
    sql_lines.append(f"-- {category} ({len(models)}개)")

    values = []
    for idx, (model_id, model_name, standard) in enumerate(models, 1):
        code = category_codes[category]
        identifier = f"{code}-{idx:03d}"
        quote_num = f"QT-2025-{code}{idx:03d}"
        description = f"{model_name} 시리즈"

        # VALUES 절 구성
        values.append(
            f"  ('demo', '{escape_sql(model_id)}', '{escape_sql(model_name)}', "
            f"'{escape_sql(category)}', '{escape_sql(standard)}', '{escape_sql(quote_num)}', "
            f"'{escape_sql(description)}', '{escape_sql(identifier)}')"
        )

    sql_lines.append("INSERT INTO ptop.models (tenant_id, model_id, model_name, category, model_standard, quote_number, description, identifier_number) VALUES")
    sql_lines.append(",\n".join(values) + ";")
    sql_lines.append("")

sql_content = "\n".join(sql_lines)

# 파일에 저장
output_file = r"c:\Users\JUN\Desktop\Auto-CVS-Project\database\demo_sample_data_fixed.sql"
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(sql_content)

print(f"[OK] SQL 파일 생성 완료: {output_file}")
print(f"[OK] 총 50개 INSERT 문 생성됨")
print("\n첫 30줄:")
print("\n".join(sql_lines[:30]))
