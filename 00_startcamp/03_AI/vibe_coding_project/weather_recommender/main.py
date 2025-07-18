
"""
Weather-Based Clothing Recommendation System
프로젝트 진입점 (main)
"""

import argparse
import sys

def main():
    """
    진입점 함수. 실행 옵션에 따라 GUI, 웹, CLI를 실행할 수 있음.
    """
    parser = argparse.ArgumentParser(description="날씨 기반 옷차림 추천 시스템")
    parser.add_argument('--gui', action='store_true', help='tkinter GUI 실행')
    parser.add_argument('--web', action='store_true', help='FastAPI 웹서비스 실행')
    parser.add_argument('--cli', action='store_true', help='CLI 모드(미구현)')
    args = parser.parse_args()

    if args.gui:
        try:
            from weather_recommender.interface.gui_app import run_gui
            run_gui()
        except ImportError as e:
            print("[오류] GUI 모듈을 불러올 수 없습니다:", e)
            print("PYTHONPATH 또는 실행 위치를 확인하세요.")
    elif args.web:
        print("FastAPI 웹서비스는 다음 명령어로 실행하세요:")
        print("uvicorn weather_recommender.interface.web_app:app --reload")
    elif args.cli:
        print("CLI 모드는 추후 구현 예정입니다.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
