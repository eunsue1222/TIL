# open AI API를 활용하여서 대화를 생성하는 기능
import openai

def generate_response(prompt):
    openai.api_key = 'your-api-key-here'
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 모델 선택
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

# 예시 사용
if __name__ == "__main__":
    user_input = "안녕하세요! 오늘 날씨는 어떤가요?"
    response = generate_response(user_input)
    print("AI 응답:", response)