# 일종의 기획서 작성 (aka. 알고리즘 수도코드)

- 기술스택
1. django, djangorestframework


- 기본적인 게시글 서비스
1. 회원가입이 가능해야 하며, 회원만 접근할 수 있는 기능이 있어야 한다.
2. 게시글을 작성할 수 있어야 하고, 각 게시글들마다 댓글을 달 수 있어야 한다.
3. 게시글은 유저만 작성할 수 있다.
4. 유저는 다른 유저가 작성한 게시글을 찜하거나 추천할 수 있어야 한다.
5. extra. 유저 활동 기반 추천 알고리즘을 만든다. (하이라키컬, 가우시안 믹스쳐)  

- 모델 정의
1. User Model
    - django가 기본 제공하는 User Model 사용 예정
    - User Model 커스터마이징 가능성

    |User|유저 정보 저장||
    |---|---|---|
    |id|고유값|PK|
    |age|나이|INT|
    |phone|핸드폰번호|TEXT|

2. Article Model
    - User Model과 관계
    1. 1:N 관계 (게시글 작성자 정보를 저장 해야함)
    2. M:N 관계 (여러명의 유저가 여러개의 게시글을 '좋아요' 할 수 있어야 함)

    |Article|게시글 정보 저장||
    |---|---|---|
    |title|제목|CHAR(100)|
    |content|내용|TEXT|
    |created_at|작성일|DATE? DATETIME?|
    |user_id|작성자|FK|

3. Comment Model
4. User-Article M:N 관계 테이블

    |like|좋아요 정보를 저장|
    |---|---|
    |user_id|좋아요를 누른 유저|FK|
    |article_id|위의 user가 좋아요를 누른 게시글|FK|
    |created_at|좋아요를 누른 시간|DATETIME|


- 기능 정리
1. 회원가입 요청 방법 -> 응답 방식
2. 로그인 요청 방법 -> 응답 방식
3. 프로필 요청 방법 -> 응답 방식
4. 게시글 작성 요청 방법 -> 응답 방식
5. 게시글 전체 조회 요청 방법 -> 응답 방식
6. 게시글 수정, 삭제, 상세 조회 요청 방법 -> 응답 방식
7. 댓글 -> 응답 방식

# 요청과 응답
- django 처리 순서
1. 식별 (Client가 요청을 보낼 위치)
2. 행위
3. 표현

- base domain - 'http://127.0.0.1:8000/
- 기획 단계에서는 노션 등으로 공유해서 작성
    - 

|기능설명|행위|식별|표현|응답방식|
|---|---|---|---|---|
|회원가입|POST|account/signup/|dj-rest-auth|Token|

1. accounts 관련 기능 모음
    1. 회원 가입
        - 요청 방식 `POST accounts/signup/`
        - 응답 데이터
        ```JSON
        {
            "token": "dj-rest-auth가 반환한 토큰값"
        }
        ```
        - 구현 방식: `dj-rest-auth[with-social]` 활용한 registration
2. articles 관련 기능 모음
    1. 게시글 작성
      - 요청 방식 `POST articles/`
      - 응답 방식
      ```JSON
        {
            "title": "문자열",
            "content": "문자열",
            "created_at": "날짜, 시간",
            "createdAt": "날짜, 시간",
        }
        ```
    
    - 요청 방식 `GET articles/{article_id}/`
    - 응답 방식
    ```JSON
        {
            "title"
            "content"
            "created_at"
            "comments": [
                {
                    "id",
                    "user_name",
                    "content",
                }
            ]
        }
    ```
