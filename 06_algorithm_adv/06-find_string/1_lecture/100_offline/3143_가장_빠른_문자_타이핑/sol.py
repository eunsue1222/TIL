import sys

sys.stdin = open('input.txt')

# 브루트 포스(Brute Force) 방식으로 문자열을 탐색하는 함수
def brute_force(pattern, target):
    result = 0  # 치환 횟수를 저장할 변수
    pattern_index = 0  # 패턴 문자열의 인덱스
    target_index = 0  # 대상 문자열의 인덱스

    while target_index < len(target):  # 대상 문자열을 끝까지 탐색
        if pattern[pattern_index] != target[target_index]:  
            # 일치하지 않는 경우, 새로운 위치에서 다시 탐색 시작
            result += 1
            pattern_index = -1  # 패턴의 첫 번째 문자로 초기화

        pattern_index += 1  # 패턴의 다음 문자로 이동
        target_index += 1  # 대상 문자열의 다음 문자로 이동

        if pattern_index == len(pattern):  
            # 패턴을 끝까지 찾은 경우
            pattern_index = 0  # 패턴의 처음으로 되돌리기
            result += 1  # 치환 횟수 증가

    return result

# KMP (Knuth-Morris-Pratt) 알고리즘을 이용한 문자열 탐색 함수
def KMP(pattern, target):
    def make_lps():
        """ LPS(Longest Prefix Suffix) 배열을 생성하는 함수 """
        lps = [0] * len(pattern)  # LPS 배열 초기화
        for i in range(1, len(pattern)):  
            # 현재 위치의 접두사와 접미사가 일치하는지 확인
            if pattern[lps[i - 1]] == pattern[i]:  
                lps[i] = lps[i - 1] + 1  # 일치하는 경우 길이를 증가
        lps[0] = -1  # LPS의 첫 번째 값은 -1로 설정
        return lps

    lps = make_lps()  # LPS 배열 생성
    result = 0  # 치환 횟수를 저장할 변수
    target_index = 0  # 대상 문자열의 인덱스
    pattern_index = 0  # 패턴 문자열의 인덱스

    while target_index < len(target):  # 대상 문자열을 끝까지 탐색
        if target[target_index] != pattern[pattern_index]:  
            # 일치하지 않는 경우, LPS를 이용하여 패턴 인덱스 이동
            pattern_index = lps[pattern_index]
            result += 1  # 치환 횟수 증가

        target_index += 1  # 대상 문자열의 다음 문자로 이동
        pattern_index += 1  # 패턴의 다음 문자로 이동

        if pattern_index == len(pattern):  
            # 패턴을 찾은 경우
            result += 1  # 치환 횟수 증가
            pattern_index = 0  # 패턴의 처음으로 되돌리기

    return result

# 보이어-무어(Boyer-Moore) 알고리즘을 이용한 문자열 탐색 함수
def boyer_moore(pattern, target):
    # Bad Character Heuristic을 기반으로 이동 테이블(lps) 생성
    lps = {pattern[i]: len(pattern) - i - 1 for i in range(len(pattern))}

    result = 0  # 치환 횟수를 저장할 변수
    pattern_index = len(pattern)  # 패턴 문자열의 길이
    target_index = 0  # 대상 문자열의 탐색 위치

    while target_index <= len(target) - pattern_index:  # 대상 문자열을 탐색할 범위 내에서 진행
        for p_idx in range(pattern_index - 1, -1, -1):  
            # 패턴의 끝에서부터 비교
            if target[target_index + p_idx] != pattern[p_idx]:  
                # 일치하지 않는 경우, Bad Character 테이블을 이용하여 건너뛰기
                skip_cancle_range = lps.get(target[target_index + p_idx], len(pattern))
                target_index += skip_cancle_range  # 패턴 이동
                result += 1  # 치환 횟수 증가
                break
        else:
            # 패턴이 완전히 일치하는 경우
            target_index += 1  # 탐색 위치를 1칸 이동
            result += 1  # 치환 횟수 증가

    return result

T = int(input())

for tc in range(1, T + 1):
    A, B = input().split()  # 대상 문자열 A와 찾을 패턴 B 입력

    # 단순히 패턴의 개수를 세어 치환하는 방식
    result = len(A) - (A.count(B) * len(B)) + A.count(B)

    # 브루트 포스 방법을 사용하여 패턴을 찾음
    result = brute_force(B, A)

    # KMP 알고리즘을 사용하여 패턴을 찾음
    result = KMP(B, A)

    # 보이어 무어 알고리즘을 사용하여 패턴을 찾음
    result = boyer_moore(B, A)

    # 결과 출력
    print(f'#{tc} {result}')
