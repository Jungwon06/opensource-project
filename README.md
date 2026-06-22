# opensource-project
# 의약품 상호작용 검사 모듈 (Interaction Checker)
담당: 허선우(2412674)

## 개요
입력된 두 가지 약물 성분을 비교하여, 함께 복용했을 때의 위험도와 주의 사항(상호작용)을 판별하는 핵심 데이터 처리 모듈입니다.

## 파일 설명
### 1. `danger_check.py` (검사 로직)
두 약물의 이름을 전달받아 데이터베이스에서 상호작용 여부를 검색하는 스크립트입니다.
* **스마트 검색:** 약물 이름에 섞인 대소문자나 공백을 내부적으로 자동 정제하여 검색의 정확도를 높였습니다.
* **순서 교차 검증:** 입력된 약물의 순서(A+B 또는 B+A)에 상관없이 완벽하게 데이터 매칭이 가능하도록 설계되었습니다.

### 2. `interaction_db.csv` (데이터베이스)
약물 간 상호작용 결과가 저장된 정형화된 CSV 파일입니다.
* **데이터 구성:** `성분1`, `성분2`, `판정`(위험/주의/안전), `이유` 4개의 열(Column)로 구성되어 있습니다.
* 데이터 검색 오류를 방지하기 위해 모든 성분명은 특수문자가 제거된 영문 소문자로 정제되어 있습니다.

## 동작 원리
1. 외부 스크립트에서 `danger_check.py`로 두 개의 약물 이름을 전달합니다.
2. 코드가 `interaction_db.csv`를 순회하며 해당 약물 조합의 매칭 여부를 확인합니다.
3. 조합이 존재할 경우 **판정 결과**와 **사유**를 반환하며, 데이터가 없을 경우 안전한 처리를 위해 '정보 없음'을 반환합니다.
# Pill Risk Detection Project - Data Branch

## 담당
2410639 김안나

## 데이터셋 구성

사용 약물 종류 및 이미지 수(13종)

- Acetaminophen: 16장
- Aspirin: 20장
- Ciprofloxacin: 10장
- Dexibuprofen: 20장
- Famotidine: 19장
- Ibuprofen: 18장
- Itraconazole: 9장
- Lamotrigine: 12장
- Loperamide: 11장
- MagnesiumHydroxide: 50장
- Naproxen: 22장
- Nizatidine: 13장
- Warfarin: 17장

## 데이터 전처리

- 이미지 파일명 통일
- 이미지 크기 224x224 통일
- RGB 변환
- Train / Validation / Test 분할 (70:15:15)
- 데이터 증강 적용
  - Rotation
  - Brightness Adjustment
  - Zoom

## 파일 설명

- `rename_files.py` : 이미지 파일명 자동 변경
- `count_images.py` : 클래스별 이미지 개수 확인
- `preprocess.py` : 데이터 전처리 및 증강 수행

## 결과 데이터 구조
processed_dataset/
├── train/
├── val/
└── test/
