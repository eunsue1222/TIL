# CLI (Command Line Interface)
|`CLI (Command Line Interface)`|`GUI (Graphic User Interface)`|
|------|-----|
|명령어를 통해 사용자와 컴퓨터가 상호 작용하는 방식|그래픽을 통해 사용자와 컴퓨터가 상호 작용하는 방식|
- CLI는 키보드만으로 모든 작업을 수행할 수 있으며 메모리와 CPU 사용량이 적어 저사양 시스템에서도 효율적으로 동작
- 특정 프로그램이나 시스템의 세부 설정을 보다 정밀하게 제어할 수 있음
- CLI 명령어는 대부분의 Unix 운영체제 기반 시스템에서 동일하게 작동하여 여러 환경에서 적용할 수 있음
---
## 기초 문법
- tab: 자동완성

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
$ rm some file_name.txt
$ rm -r folder_name
```
---
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
---