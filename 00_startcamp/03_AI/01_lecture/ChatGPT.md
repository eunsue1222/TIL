# ChatGPT (Generative / Pre-trained / Transformer)
- 생성 모델 / 사전 훈련 / 트랜스포머 AI 모델 -> GPT 모델을 기반으로 한 대화형 AI

## Generative AI
- 기존 패턴을 기반으로 오디오, 비디오, 이미지, 텍스트, 코드, 시뮬레이션 등의 새로운 코텐츠를 생성하는 인공지능 모델

## Pre-trained
- 거대 언어 모델 + 추가 학습 데이터 + 추가 강화 학습

## Transformer (Neural Network Architecture) 
  - 문장 속의 단어 간 관계를 추적해 맥락과 의미를 학습
  - 인간처럼 일관되고 연관성이 높은 언어를 구사하여 대화형 작업에 강점
  - `Self-Attention 메커니즘`: 입력 데이터 간의 관계와 중요도를 계산
  - `병렬 처리 기능`: RNN과 달리 순차 처리가 필요 없어 속도가 빠름
  - `스케일링 가능`: 대규모 데이터 및 파라미터로 확장 가능

---

# Interface
- 서로 다른 두 개의 시스템 (기기, 소프트웨어 등)이 정보를 교환할 때, 그 사이에 존재하는 접점
- 사용자가 기기를 쉽게 동작 시키거나, 기계와 기계가 통신할 때 필요한 '약속된 방식'

## 클라이언트와 서버
- CLIENT (request) <-> (responses) SERVER 

### 클라이언트 (Client)
- 서비스를 요청하는 쪽
- ex) 사용자의 웹 브라우저, 모바일 앱

### 서버 (Server)
- 요청을 받아서 처리하고, 결과를 응답해주는 쪽
- ex) 웹 서버, 데이터베이스 서버

## API (Application Programming Interface)
- 두 소프트웨어 (또는 시스템)가 서로 통신할 수 있게 하는 메커니즘
- '약속된 방식의 인터페이스'로, 특정 규칙에 따라 데이터를 요청하고 응답하는 규칙을 제공
- [OpenAI API Documentation](https://platform.openai.com/docs/overview)
- [OpenAI Tokenizer](https://platform.openai.com/tokenizer)