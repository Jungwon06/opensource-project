# opensource-project

# 실행 방법

1. 필요한 라이브러리 설치
pip install torch torchvision pillow pandas
2. 프로그램 실행
python main.py <알약이미지1> <알약이미지2>
예시
python main.py pill1.png pill2.png

# 시스템 동작 순서

1. 사용자가 두 개의 알약 이미지를 입력
2. inference.py가 ResNet50 모델을 이용하여 약물명을 예측
3. danger_check.py가 interaction_db.csv를 조회하여 상호작용 여부를 확인
4. 최종 판정 결과(위험/주의/안전)와 사유를 출력

# 의약품 상호작용 검사 모듈 (Interaction Checker)
담당: 허선우(2412674)

## 개요
입력된 두 가지 약물 성분을 비교하여, 함께 복용했을 때의 위험도와 주의 사항(상호작용)을 판별하는 핵심 데이터 처리 모듈

## 파일 설명
### 1. `danger_check.py` (검사 로직)
두 약물의 이름을 전달받아 데이터베이스에서 상호작용 여부를 검색하는 스크립트
* **스마트 검색:** 약물 이름에 섞인 대소문자나 공백을 내부적으로 자동 정제하여 검색의 정확도를 높임
* **순서 교차 검증:** 입력된 약물의 순서(A+B 또는 B+A)에 상관없이 완벽하게 데이터 매칭이 가능함

### 2. `interaction_db.csv` (데이터베이스)
약물 간 상호작용 결과가 저장된 정형화된 CSV 파일
* **데이터 구성:** `성분1`, `성분2`, `판정`(위험/주의/안전), `이유` 4개의 열(Column)로 구성
* 데이터 검색 오류를 방지하기 위해 모든 성분명은 특수문자가 제거된 영문 소문자로 정제됨

## 동작 원리
1. 외부 스크립트에서 `danger_check.py`로 두 개의 약물 이름을 전달
2. 코드가 `interaction_db.csv`를 순회하며 해당 약물 조합의 매칭 여부를 확인
3. 조합이 존재할 경우 **판정 결과**와 **사유**를 반환하며, 데이터가 없을 경우 안전한 처리를 위해 '정보 없음'을 반환

### 3. 'main.py'(메인 스크립트)
CLI(Command Line Interface) 환경에서 두 개의 알약 이미지 경로를 인자로 전달받아, 전체 분석 프로세스(초기화 → 이미지 분석 → 상호작용 분석 → 결과 출력)를 제어하는 실행 파일
* **End-to-End 파이프라인:** 약물 이미지 인식부터 상호작용 분석까지 전 과정을 통합해 결과를 한 번에 출력
* **안정성 및 예외 처리:** 모델 파일(best_pill_model.pth)과 입력 이미지의 경로를 사전 검증하여 불필요한 연산 오류를 방지
* **직관적인 CLI:** 터미널 명령어 한 줄(python main.py <이미지1> <이미지2>)로 간편하게 시스템을 실행

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

## 추가 작업

- Google Colab 환경에서 학습 코드를 실행하여 최종 모델 가중치(best_pill_model.pth) 생성
- 추론 모듈(inference.py) 구현
- 메인 시스템(main.py)과 연동하여 시스템 통합 테스트 및 시연 수행

## 파일 설명

- rename_files.py : 이미지 파일명 자동 변경
- count_images.py : 클래스별 이미지 개수 확인
- preprocess.py : 데이터 전처리 및 증강 수행
- inference.py : 학습된 모델을 이용하여 입력된 알약 이미지를 분류
- best_pill_model.pth : 학습 완료 후 생성된 최종 모델 가중치 파일

## 결과 데이터 구조
processed_dataset/
├── train/
├── val/
└── test/

# 알약 인식 전이학습 모델(ResNet50) 구현 및 검증
## 담당
2411495 손정원

## 작업 내용
### 1. 사전학습 모델 활용
- ImageNet으로 대규모 사전학습된 ResNet50 모델을 로드하여 이미지 특징 추출기로 활용
- 최종 분류 레이어를 13개의 알약 클래스에 맞게 수정 및 Fine-tuning 진행

### 2. 성능 검증
- 학습 완료 후 Loss Curve 및 Accuracy Curve 시각화 완료
- 학습에 사용되지 않은 test 데이터셋을 활용해 최종 성능 측정 및 혼동 행렬 도출 완료
