# opensource-project
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
