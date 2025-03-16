from google_play_scraper import reviews_all, Sort
import pandas as pd
import os

# 실제 패키지 이름 사용
result = reviews_all(
    'com.superbin',
    lang='ko',  # language
    country='kr',  # country
    sort=Sort.NEWEST,  # sorting by newest
)

# DataFrame으로 변환
df = pd.DataFrame(result)

# 사용자 홈 디렉토리에 파일 저장
home_dir = os.path.expanduser('~')
file_path = os.path.join(home_dir, 'SuperBin_recent_reviews.xlsx')

df.to_excel(file_path, index=False)

print(f"리뷰 수집 및 엑셀 파일 저장이 완료되었습니다. 파일 경로: {file_path}")
