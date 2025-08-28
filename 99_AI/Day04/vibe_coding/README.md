# SSAFY AI Chatbot

## 프로젝트 실행 방법

### Backend Server

1.  **서버 디렉토리로 이동**

    ```bash
    cd vibe_coding/server
    ```

2.  **필요한 패키지 설치**

    ```bash
    npm install
    ```

3.  **.env 파일 설정**

    `.env_example` 파일명을 `.env` 로 수정
    `.env` 파일을 열고, `OPENAI_API_KEY`에 본인의 OpenAI API 키를 입력합니다.

    ```
    # server/.env
    PORT=3001
    OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    CORS_ORIGIN=http://localhost:5173
    ```

4.  **서버 실행**

    ```bash
    npm run dev
    ```

### Frontend Client

1.  **클라이언트 디렉토리로 이동**

    ```bash
    cd vibe_coding/client
    ```

2.  **필요한 패키지 설치**

    ```bash
    npm install
    ```

3.  **.env 파일 설정**

    `.env_example` 파일명을 `.env` 로 수정


4.  **클라이언트 실행**

    ```bash
    npm run dev
    ```
