# opensource-project
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
