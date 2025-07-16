# Command Line Interface
- tab: 자동완성

## 기초 문법
```
Desktop/lecture/00_startcamp/01_git
ㄴ A.txt
ㄴ B.txt
```
### '.'
- .: 현재 디렉토리
- ..: 현재의 상위 디렉토리 (부모 폴더)
- ~: 루트 디렉토리

```
$ .
Desktop/lecture/00_startcamp/01_git

$ ..
Desktop/lecture/00_startcamp
```

### 'touch'
- 파일 생성 (파일명: 공백 금지)
```
$ touch file_name.txt
```

### 'mkdir'
- 새 디렉토리 생성
```
$ mkdir folder_name
```

### 'ls'
- 현재 작업 중인 디렉토리 내부의 폴더/파일 목록을 출력
- 숨김 파일 보기 가능
```
$ ls
$ ls -a
$ ls -al
```
### 'cd'
- 현재 작업 중인 디렉토리를 변경 (위치 이동)
```
~/Desktop/lecture/00_startcamp/01_git
$ cd ..

~/Desktop/lecture/00_startcamp
$ mkdir 02_git_advanced
$ ls
01_git/   02_git_advanced/
```

### 'start'
- 폴더/파일을 열기 (Mac에서는 open을 사용)
```
$ start .
```

### 'rm'
- 파일 삭제 (휴지통에 남지 않음)
- 디렉토리 삭제는 -r 옵션을 추가 사용
```
$ rm some some_file.txt
$ rm -r folder_name
```

## 경로
- /: Windows
- \\: Unix
### 절대경로
- Root 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것
```
C:/Users/ssafy/Desktop
```
### 상대경로
- 현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치를 작성한 것
```
현재 디렉토리: C:/Users
윈도우 바탕 화면으로의 상대 경로: ssafy/Desktop
```
# Git (분산 버전 관리 시스템)
- 컴퓨터 내 파일의 변화의 기록과 추적을 자동화해주는 시스템
- 코드의 '변경 이력'을 기록하고 '협업'을 원활하게 하는 도구

|`증앙 집중식`|`분산식`|
|------|-----|
|버전은 중앙 서버에 저장되고 중앙 서버에서 파일을 가져와 다시 중앙에 업로드|버전을 여러 개의 복제된 저장소에 저장 및 관리|
|-> 같은 파일의 같은 내용을 다른 사람이 고치는 경우 충돌 일어남|-> 같은 파일의 같은 내용을 다른 사람이 고치는 경우 다른 버전으로 기록되어 겹치는 부분만 수정 가능|

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


## git의 동작
- git init: 로컬 저장소 설정(초기화)
- git add: 변경사항이 있는 파일을 staging area에 추가
- git commit: staging area에 있는 파일들을 저장소에 기록
---
- 로컬 저장소 초기화
```
~/Desktop/lectures
$ git init

~/Desktop/lectures (master)
$ ls -a
./  ../ .git/ 00_startcamp/
```
- staging area에 추가
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
- commit 생성하기 실패 (commit을 생성하기 위해서는 commit 작성자 정보가 필요)
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
## 로컬 저장소
## 원격 저장소
- 코드와 버전 관리 이력을 온라인 상의 특정 위치에 저장하여 여러 개발자가 협업하고 코드를 공유할 수 있는 저장 공간
- ex) GitLab(private. SSAFY), GitHub(public. 포트폴리오), Bitbucket 등
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
- 
```
~/Desktop/lectures (master)
$ git remote add origin https://github.com/eunsue1222/TIL.git

~/Desktop/lectures (master)
$ git remote -v
origin  https://github.com/eunsue1222/TIL.git (fetch)
origin  https://github.com/eunsue1222/TIL.git (push)

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
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean

~/Desktop/lectures (master)
$ git push
Everything up-to-date
```