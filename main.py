import argparse
import os
from inference import load_model, predict_image, DEVICE, CLASS_NAMES
from danger_check import InteractionChecker

MODEL_PATH = 'best_pill_model.pth'

def run_system(img_path1, img_path2):
    print("시스템 초기화 중...")
    
    if not os.path.exists(MODEL_PATH):
        print(f"오류: 모델 가중치 파일({MODEL_PATH})을 찾을 수 없습니다.")
        return

    # 모델과 진짜 CSV 파일 로드
    model = load_model(MODEL_PATH)
    checker = InteractionChecker('interaction_db.csv') 
    
    print("이미지 분석 중...")
    try:
        pill1_name = predict_image(model, img_path1)
        pill2_name = predict_image(model, img_path2)
        print(f"인식 결과: 약물1=[{pill1_name}], 약물2=[{pill2_name}]")
    except Exception as e:
        print(f"이미지 처리 오류: {e}")
        return

    print("상호작용 분석 중...")
    risk_info = checker.check_risk(pill1_name, pill2_name)

    print("\n--- 분석 결과 ---")
    print(f"조합: {pill1_name} + {pill2_name}")
    print(f"판정: {risk_info['status']}")
    print(f"사유: {risk_info['reason']}")
    print("-----------------")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="의약품 상호작용 분석 시스템")
    
    parser.add_argument("img1", help="첫 번째 알약 이미지 경로")
    parser.add_argument("img2", help="두 번째 알약 이미지 경로")
    
    args = parser.parse_args()
    
    run_system(args.img1, args.img2)