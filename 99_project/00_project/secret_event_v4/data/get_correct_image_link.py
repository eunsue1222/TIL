import pandas as pd
import re

# --- 1. 사용자 설정 ---
# 이 부분을 자신의 환경에 맞게 수정해주세요.

# 변환할 원본 CSV 파일 이름
INPUT_CSV_FILE = "rolling_paper_v8.csv"

# 결과물을 저장할 새 CSV 파일 이름
OUTPUT_CSV_FILE = "rolling_paper_v9.csv"

# Google Drive 링크가 들어있는 컬럼의 이름
# ★ 요청하신 대로, 이 컬럼을 읽어서 변환한 뒤 다시 같은 이름으로 저장합니다.
COLUMN_TO_CONVERT = "image_link"
# -------------------------


def extract_gdrive_file_id(url):
    """
    다양한 형태의 Google Drive URL에서 파일 ID를 추출합니다.
    예: https://drive.google.com/file/d/FILE_ID/view?usp=sharing
        https://drive.google.com/open?id=FILE_ID
    """
    if not isinstance(url, str):
        return None
    
    # --- [수정] ---
    # 다양한 URL 형식을 처리하기 위해 여러 정규 표현식 패턴을 시도합니다.
    patterns = [
        r"/d/([a-zA-Z0-9_-]{25,})",       # e.g., /d/FILE_ID
        r"id=([a-zA-Z0-9_-]{25,})"        # e.g., ?id=FILE_ID
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1) # 첫 번째로 일치하는 파일 ID 반환
            
    return None

def convert_to_direct_link(file_id):
    """
    추출된 파일 ID를 웹사이트에 직접 삽입 가능한 URL 형식으로 변환합니다.
    """
    if file_id:
        return f"https://lh3.googleusercontent.com/d/{file_id}"
    return ""

def main():
    """
    메인 실행 함수: CSV 파일을 읽고, 링크를 변환하여, 새 파일로 저장합니다.
    """
    print(f"'{INPUT_CSV_FILE}' 파일 처리를 시작합니다...")

    # CSV 파일 읽기
    try:
        df = pd.read_csv(INPUT_CSV_FILE)
        print("파일을 성공적으로 읽었습니다.")
    except FileNotFoundError:
        print(f"오류: '{INPUT_CSV_FILE}' 파일을 찾을 수 없습니다. 파일 이름과 경로를 확인해주세요.")
        return

    # 지정된 컬럼이 파일에 있는지 확인
    if COLUMN_TO_CONVERT not in df.columns:
        print(f"오류: '{COLUMN_TO_CONVERT}' 컬럼을 찾을 수 없습니다. 컬럼 이름을 확인해주세요.")
        return

    print(f"'{COLUMN_TO_CONVERT}' 컬럼의 링크를 변환합니다...")
    
    # 각 링크를 변환하는 함수를 컬럼 전체에 적용
    def process_link(url):
        file_id = extract_gdrive_file_id(url)
        if file_id:
            return convert_to_direct_link(file_id)
        # 변환할 수 없는 링크는 원본을 그대로 유지하거나 비워둘 수 있습니다.
        # 여기서는 원본을 유지하도록 설정했습니다.
        return url

    # ★ 'image_link' 컬럼의 내용을 변환한 결과로 'image_link' 컬럼을 덮어씁니다.
    # 따라서 컬럼 이름은 변경되지 않습니다.
    df[COLUMN_TO_CONVERT] = df[COLUMN_TO_CONVERT].apply(process_link)

    # 변환된 데이터를 새 CSV 파일로 저장
    try:
        df.to_csv(OUTPUT_CSV_FILE, index=False, encoding='utf-8-sig')
        print("\n🎉 모든 작업이 완료되었습니다!")
        print(f"결과가 '{OUTPUT_CSV_FILE}' 파일에 저장되었습니다.")
    except Exception as e:
        print(f"\n오류: 파일을 저장하는 중에 문제가 발생했습니다. - {e}")


if __name__ == "__main__":
    main()

