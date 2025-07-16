# Git (분산 버전 관리 시스템)
- 컴퓨터 내 파일 변화의 기록과 추적을 자동화해주는 시스템
- 코드의 '변경 이력'을 기록하고 '협업'을 원활하게 하는 도구
- ex) [Google Docs](https://www.google.com/intl/ko_KR/docs/about/)
- ex) [GitHub](https://github.com/) (public. 포트폴리오)
- ex) [GitLab](https://about.gitlab.com/) (private. SSAFY)

|`증앙 집중식`|`분산식`|
|------|-----|
|버전은 중앙 서버에 저장되고 중앙 서버에서 파일을 가져와 다시 중앙에 업로드|버전을 여러 개의 복제된 저장소에 저장 및 관리|
|-> 같은 파일의 같은 내용을 다른 사람이 고치는 경우 충돌 일어남|-> 같은 파일의 같은 내용을 다른 사람이 고치는 경우 다른 버전으로 기록되어 겹치는 부분만 수정 가능|
- 중앙 서버에 의존하지 않고도 동시에 다양한 작업을 수행하여 개발자들 간의 작업충돌을 줄여주고 개발 생산성을 향상
- 중앙 서버의 장애나 손실에 대비하여 백업과 복구가 용이
- 변경 이력과 코드를 로컬 저장소에 기록하고, 나중에 중앙 서버와 동기화하기 때문에 인터넷에 연결되지 않은 환경에서도 작업을 계속할 수 있음
---
## Git의 3가지 영역
### Working Directory
- 실제 작업 중인 파일들이 위치하는 영역
```
Desktop/lecture/00_startcamp
ㄴ 01_git
ㄴ 02_git_advanced
```

### Staging Area
- Working Directory에서 변경된 파일 중, 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역
- Repository에 commit후 파일들이 삭제됨
```
Desktop/lecture/00_startcamp/01_git
```

### Repository
- 버전 이력과 파일들이 영구적으로 저장되는 영역
- 모든 버전과 변경 이력이 기록됨
```
Desktop/lecture/00_startcamp/01_git
```

### Commit
- 변경된 파일들을 저장하는 행위이며, 마치 사진을 찍듯이 기록한다 하여 'snapshot' 이라고도 함
---

## git의 동작
- git init: 로컬 저장소 설정(초기화)
- git add: 변경사항이 있는 파일을 staging area에 추가
- git commit: staging area에 있는 파일들을 저장소에 기록
- git status: 현재 로컬 저장소의 파일 상태 보기
- git log: commit history 보기
- git log --oneline: commit 목록 한 줄로 보기
- git config --global -l: git global 설정 정보 보기
---
- 로컬 저장소 초기화
    - git 로컬 저장소 내에 또다른 git 로컬 저장소를 만들지 말 것
    - git 저장소 안에 git 저장소가 있을 경우 가장 바깥 쪽의 git 저장소가 안쪽의 git 저장소의 변경사항을 추적할 수 없기 때문
```
~/Desktop/lectures
$ git init

~/Desktop/lectures (master)
$ ls -a
./  ../ .git/ 00_startcamp/
```
- 파일을 staging area에 추가
```
~/Desktop/lectures (master)
$ git add 00_startcamp/01_git/markdown.md
```
- 로컬 저장소의 파일 상태 확인
```
~/Desktop/lectures (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   00_startcamp/01_git/markdown.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        00_startcamp/01_git/CLI.md
```
- commit 생성하기 (commit을 생성하기 위해서는 commit 작성자 정보가 필요)
```
~/Desktop/lectures (master)
$ git commit -m "마크다운 연습"
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'SSAFY@DESKTOP-763H707.(none)')
```
- 작성자 정보 설정
    - global 설정 후 앞으로 재입력하지 않음
```
~/Desktop/lectures (master)
$ git config --global user.email "eunsue1222@gmail.com"

~/Desktop/lectures (master)
$ git config --global user.name "김은수"
```
- 작성자 정보 확인
```
~/Desktop/lectures (master)
$ git config --global --list
user.email=eunsue1222@gmail.com
user.name=김은수
```
- 작성자 정보 변경
```
~/Desktop/lectures (master)
$ code ~/.gitconfig
```
- Commit 생성하기 재시도
```
~/Desktop/lectures (master)
$ git commit -m "마크다운 연습"
[master (root-commit) 9fb7612] 마크다운 연습
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 00_startcamp/01_git/markdown.md
 ```
- Commit 목록 확인
 ```
 ~/Desktop/lectures (master)
$ git log
commit 9fb76129f11e249b378d3ff0751b1d40f531ee77 (HEAD -> master)
Author: 김은수 <eunsue1222@gmail.com>
Date:   Wed Jul 16 15:50:47 2025 +0900

    마크다운 연습
```
---
## 저장소
### 로컬 저장소
- 현재 사용자가 직접 접속하고 있는 기기 또는 시스템
- 개인 컴퓨터, 노트북, 테블릿 등 사용자가 직접 조작하는 환경경
### 원격 저장소
- 코드와 버전 관리 이력을 온라인 상의 특정 위치에 저장하여 여러 개발자가 협업하고 코드를 공유할 수 있는 저장 공간
<br>

- 새로운 레퍼지토리 생성
```
$ echo "# TIL" >> README.md
$ git init
$ git add README.md
$ git commit -m "first commit"
$ git branch -M master
$ git remote add origin https://github.com/eunsue1222/TIL.git
$ git push -u origin master
```
- 로컬 저장소에 원격 저장소 추가
- 별칭을 사용해 로컬 저장소 한 개에 여러 원격 저장소를 추가할 수 있음
    - origin: 추가하는 원격 저장소 별칭
    - https://github.com/eunsue1222/TIL.git: 추가하는 원격 저장소의 URL
```
~/Desktop/lectures (master)
$ git remote add origin https://github.com/eunsue1222/TIL.git
```
- 등록된 원격 저장소 목록 확인
```
~/Desktop/lectures (master)
$ git remote -v
origin  https://github.com/eunsue1222/TIL.git (fetch)
origin  https://github.com/eunsue1222/TIL.git (push)
```
- 원격 저장소에 commit 목록을 업로드
    - "git아, origin이라는 이름의 원격 저장소에 master 라는 이름의 브랜치를 push해줘"
```
~/Desktop/lectures (master)
$ git push -u origin master
info: please complete authentication in your browser...
Enumerating objects: 13, done.
Counting objects: 100% (13/13), done.
Delta compression using up to 28 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (13/13), 924 bytes | 462.00 KiB/s, done.
Total 13 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/eunsue1222/TIL.git
 * [new branch]      master -> master
branch 'master' set up to track 'origin/master'.
```

```
~/Desktop/lectures (master)
$ git add .

~/Desktop/lectures (master)
$ git commit -m "원격 저장소 활용 연습"
[master 08514d7] 원격 저장소 활용 연습
 1 file changed, 262 insertions(+)

nothing to commit, working tree clean

~/Desktop/lectures (master)
$ git push
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 28 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (5/5), 3.14 KiB | 3.14 MiB/s, done.
Total 5 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/eunsue1222/TIL.git
   9c2aae4..08514d7  master -> master
```
- 원격 저장소 전체를 복제 (다운로드)
```
$ git clone https://github.com/eunsue1222/TIL.git
```
- 변경사항 작업 후 commit 생성
```
$ git commit -m "커밋 연습"
```
- commit을 원격 저장소에 push
```
$ git push origin master
```
- 업데이트된 변경사항 받기
```
$ git pull
```