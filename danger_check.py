import pandas as pd

class InteractionChecker:
    def __init__(self, csv_path='interaction_db.csv'):
        # 한글 깨짐 방지를 위해 인코딩(utf-8-sig) 추가
        self.db = pd.read_csv(csv_path, encoding='utf-8-sig')
            
        # 검색을 빠르게 하기 위해 문자열 정규화
        self.db['성분1'] = self.db['성분1'].str.strip().str.lower()
        self.db['성분2'] = self.db['성분2'].str.strip().str.lower()

    def check_risk(self, pill1, pill2):
        p1_norm = pill1.strip().lower()
        p2_norm = pill2.strip().lower()

        # 양방향 검색 (A-B 또는 B-A)
        condition = (
            ((self.db['성분1'] == p1_norm) & (self.db['성분2'] == p2_norm)) |
            ((self.db['성분1'] == p2_norm) & (self.db['성분2'] == p1_norm))
        )
        
        result_df = self.db[condition]

        if not result_df.empty:
            return {
                "status": result_df.iloc[0]['판정'], 
                "reason": result_df.iloc[0]['이유']
            }
        return {"status": "정보 없음", "reason": "등록된 상호작용 정보가 없습니다."}