import pandas as pd
from googleapiclient.discovery import build
import re

# 1. ------------------ (사용자 설정) ------------------
# 여기에 자신의 YouTube Data API v3 키를 입력하세요.
API_KEY = "AIzaSyBsBexIr6dSw5c934nYxa5xn2zxnrQa5pk" 

# 처리할 원본 CSV 파일 이름
input_csv_file = "rolling_paper_v6.csv" 
# 결과물을 저장할 CSV 파일 이름
output_csv_file = "rolling_paper_v7.csv"
# ----------------------------------------------------


def clean_music_title(title):
    """'<', '>' 문자를 제거하고 '-' 좌우 공백을 제거하는 함수"""
    if not isinstance(title, str):
        return ""
    # '<' 또는 '>' 제거
    cleaned_title = title.replace('<', '').replace('>', '')
    # ' - ' 또는 ' -' 또는 '- '를 '-'로 변경
    cleaned_title = re.sub(r'\s*-\s*', '-', cleaned_title)
    return cleaned_title

def search_youtube_video(service, query):
    """YouTube에서 검색 쿼리로 동영상을 검색하고 첫 번째 결과의 링크를 반환하는 함수"""
    if not query:
        return "Query is empty"
    try:
        search_response = service.search().list(
            q=query,
            part="snippet",
            maxResults=1,
            type="video"
        ).execute()

        # 검색 결과가 있으면 videoId를 추출하여 링크 생성
        if search_response.get("items"):
            video_id = search_response["items"][0]["id"]["videoId"]
            return f"https://www.youtube.com/watch?v={video_id}"
        else:
            return "Not Found"
    except Exception as e:
        print(f"An error occurred while searching for '{query}': {e}")
        return "API Error"

def main():
    """메인 실행 함수"""
    print("CSV 처리를 시작합니다...")

    try:
        # CSV 파일 읽기
        df = pd.read_csv(input_csv_file)
        print(f"'{input_csv_file}' 파일을 성공적으로 읽었습니다.")
    except FileNotFoundError:
        print(f"오류: '{input_csv_file}' 파일을 찾을 수 없습니다. 파일 이름과 경로를 확인해주세요.")
        return

    # 1. 'music' 컬럼의 값을 정리합니다.
    df['music'] = df['music'].apply(clean_music_title)
    print("'music' 컬럼 정리 완료.")

    # YouTube API 서비스 객체 생성
    try:
        youtube = build('youtube', 'v3', developerKey=API_KEY)
        print("YouTube API 서비스에 연결되었습니다.")
    except Exception as e:
        print(f"YouTube API 연결에 실패했습니다. API 키를 확인해주세요. 오류: {e}")
        return
        
    # 2. 정리된 음악 제목으로 YouTube를 검색하여 링크를 가져옵니다.
    music_links = []
    total_songs = len(df)
    for i, title in enumerate(df['music']):
        print(f"[{i+1}/{total_songs}] '{title}' 검색 중...")
        link = search_youtube_video(youtube, title)
        music_links.append(link)

    # 'music_link' 라는 새 컬럼에 결과 추가
    df['music_link'] = music_links
    print("모든 음악에 대한 링크 추가 완료.")

    # 변경된 DataFrame을 새 CSV 파일로 저장
    df.to_csv(output_csv_file, index=False, encoding='utf-8-sig')
    print(f"모든 작업이 완료되었습니다. 결과가 '{output_csv_file}' 파일에 저장되었습니다.")


if __name__ == "__main__":
    main()