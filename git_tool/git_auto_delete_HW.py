# os를 조작하는 방법
# 서브프로세스를 실행하는 방법

# 과목
# 종류
# 세트번호

# 범위 1~6까지 혹은 a, b, c
# 를 반복해서
    # git clone 을 받도록하는
    # base_url = 'htttp~~// {subject}_{seperator}_{stage}/

# 현재 위치를 기준으로,
# 최상위 폴더를 제외한 모든 폴더를 순회하며 (모든 폴더는 아마 list)
    # 폴더 이름이 ".git"인 경우를 모두 삭제 -> `rm -f``

import os
import shutil
import stat

# .git 으로 끝나는 파일/디렉토리 삭제

def force_remove(path):
    def on_rm_error(func, path, exc_info):
        # 삭제 권한이 없으면 실행되는 함수
        # 숨김 파일 삭제 권한 부여
        # chmod : 권한 부여 명령어
        os.chmod(path, stat.S_IWRITE)
        func(path)

    # 디렉토리 내부에 있는 모든 파일에 대해 삭제 수행
    shutil.rmtree(path, onerror=on_rm_error)

def remove_git_dirs():
    
    # 현재 있는 폴더로 경로 설정
    base_path = os.getcwd()
    first = True

    # 하위 디렉토리 순환
    for root, dirs, files in os.walk(base_path, topdown=True):
        # 최상위 폴더면 삭제 X
        if first:
            first = False
            continue
        
        # 만약 .git으로 끝나면 해당 폴더/파일 force_remove 실행
        if '.git' in dirs:
            git_path = os.path.join(root, '.git')
            print(f"삭제 중: {git_path}")
            force_remove(git_path)

if __name__ == "__main__":
    # 메인 함수
    remove_git_dirs()