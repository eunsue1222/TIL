# Markdown
- 일반 텍스트로 문서를 작성하는 간단한 방법
- 주로 개발자들이 텍스트와 코드를 작성해 문서화하기 위해 사용
- 작성된 Markdown 문서는 다른 프로그램에 의해 변환되어 출력됨
---
- [Markdown Guide](https://www.markdownguide.org/basic-syntax/)
- [Typora](https://typora.io/) (유료)
- [MarkText](https://github.com/marktext/marktext#download-and-installation) (무료)
- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) (VSCode 확장프로그램)
---
## Heading
- 문서의 단계별 제목으로 사용
- '#'의 개수에 따라 제목의 수준을 구별
```
# 제목1
## 제목2
### 제목3
#### 제목4
##### 제목5
###### 제목6
```
# 제목1
## 제목2
### 제목3
#### 제목4
##### 제목5
###### 제목6
---
## List
- 목록을 표시하기 위해 사용
- 순서가 있는 리스트와 순서가 없는 리스트 제공
```
1. 순서가
   1. 있는
2. 리스트

- 순서가
    - 없는
- 리스트
```
1. 순서가
   1. 있는
2. 리스트

- 순서가
    - 없는
- 리스트
---
## Code block & Inline code block
- 일반 텍스트와 달리 해당 프로그래밍 언어에 맞춰서 텍스트 스타일을 변환
- 개발에서 마크다운을 사용하는 가장 큰 이유

```python
print('hello')
```
```bash
$ mkdir test
```
```javascript
cosole.log('test')
```
---
## Link & Image
- 특정 주소를 사용해 다른 페이지로 이동하는 링크 혹은 이미지 출력
- 이미지의 너비와 높이는 마크다운으로 조절할 수 없음 (HTML 사용 필요)
- 해당 경로에 있는 이미지도 경로까지 유지한 상태로 공유
```
[Naver](www.naver.com)   
![Image](image.png)
```
[Naver](www.naver.com)    
![Image](image.png)  

---
## Text
```
**굵게**
*기울임*
~~취소선~~
<u>밑줄</u>
```
**굵게**  
*기울임*  
~~취소선~~  
<u>밑줄</u>  
<br>

---
## 수평선
- 단락을 구분할 때 사용하는 수평선
- '-' (hypen)을 3개 이상 적으면 작동
```
---
```
---