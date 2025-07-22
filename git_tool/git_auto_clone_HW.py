import os
import requests
import subprocess
from datetime import datetime, timedelta, timezone
from dateutil import parser


# GitLab 설정
GITLAB_API = "https://lab.ssafy.com/api/v4"
USERNAME = ""  # 본인 GitLab id
PRIVATE_TOKEN = "" # 본인 GitLab token

# clone 받을 경로 설정
CLONE_DIR = "" # 경로 입력
clone_path = CLONE_DIR if CLONE_DIR else os.getcwd() # 미입력 시 현재 터미널 경로로 clone


# 시간 설정 6시간 이내
# 변경을 원할 시 timedelta() 내부값 변경, hours, minutes, seconds, days로 설정 가능
# ex) timedelta(days=1) : 하루 이내(24시간)
since = datetime.utcnow().replace(tzinfo=timezone.utc) - timedelta(hours=6)


# 프로젝트 목록 불러오기
response = requests.get(
    f"{GITLAB_API}/users/{USERNAME}/projects",
    headers={"PRIVATE-TOKEN": PRIVATE_TOKEN},
    params={"visibility": "private", "order_by": "last_activity_at", "sort": "desc", "per_page": 100}
)

projects = response.json()


# 불러온 프로젝트에 대해 6시간 이내 업데이트 프로젝트만 clone
for project in projects:
    last_activity = project['last_activity_at']
    last_activity_dt = parser.isoparse(last_activity)
    
    if last_activity_dt >= since:
        print(f"클론할 프로젝트: {project['name']} / 업데이트 시간: {last_activity_dt}")
        clone_url = project['http_url_to_repo']
        target_dir = os.path.join(clone_path, project['name'])
        
        subprocess.run(["git", "clone", clone_url, target_dir])