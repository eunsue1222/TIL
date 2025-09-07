'''
베이비진 게임이란게 뭐냐?
6개의 숫자를 가지고, triple 혹은 run 이 각각 2번 나오거나, 혹은 한번씩 번갈아 나오면 베이비진
triple -> 동일한 숫자가 6번
run -> 숫자 3개가 차례로 증가하는 형태

0~9 중에 6개를 중복 포함해서 뽑는다.
'667767' -> 666 777 : 트리플이 2번 베이비진
'123123' -> 123 123 : 런이 2번 베이비진
'111456' -> 111 456 : 트리플, 런이 한번씩 베이비진
'111156' -> 111: 트리플 한번은 만들 수 있지만 남은수 156 으로는 트리플도 런도 안되므로 베이비 진 아님.

그리디 한 방식으로 해결해 본다면?
'''
# 함수를 통해서 얻고자 하는바가 무엇인가?
# 어떤 지엽적인 문제를 해결해 나가면서 큰 문제를 모두 해결 가능한가.
# 어떤 아주 특이한 케이스 하나만을 위한 if문을 작성하는데에는 신중한 고민 끝에 결론을 내야한다. (검증)
def baby_gin(numbers):
    '''
    numbers: 정수 6개가 문자열로 주어짐.
    숫자 3개씩 끊어서, 트리플인지 보기, 런인지 보기 2번 나오면 베이비진
    일단 정렬을 해.
    667767 -> 666777: 트리플이 2번임. 3씩 끊어서 보면
    111456 -> 111456: 트리플 1번, 런 1번
    123123 -> 112233: 트리플...? 런...? 어떻게 확인하지?
    641352 -> 123456: 런 2번임.
    '''
    digits = [int(char) for char in numbers]

    count = 0   # 트리플 or 런이 나온 횟수 만큼 1씩 증가 하도록 할 것.
    # 조사는 총 몇번 해야 할까?
    for _ in range(2):  # 이번 회차에 숫자 3개 끊어서 트리플인지 런인지 볼거임.
        digits.sort()
        # if 트리플이니?
        #     count += 1
        # 트리플인지 먼저 확인
        # 앞에서부터 연속된 3개가 같은 숫자인지 확인
        for i in range(len(digits) - 2):  # 0 1 2 3
            # 이 경우, 트리플
            if digits[i] == digits[i+1] == digits[i+2]:
                tiple_val = digits[i]
                digits.remove(tiple_val)
                digits.remove(tiple_val)
                digits.remove(tiple_val)
                # digits.remove(i)    # 이렇게 직접적으로 digits 제거 해버리면...곤란할지도..?
                count += 1
                break
        # if 런이니?
        #     count += 1
        for i in range(len(digits) - 2):
            # 내 값보다 1큰 값과, 내 값보다 2 큰값이 배열안에 있는지 확인
            # if digits[i] + 1 == digits[i+1]
            if digits[i] + 1 in digits and digits[i] + 2 in digits:
                run_val = digits[i]
                digits.remove(run_val)
                digits.remove(run_val+1)
                digits.remove(run_val+2)
                count += 1
                break
    if count == 2:
        return True

cases = ['667767', '123123', '111456', '111156']
for tc in cases:
    if baby_gin(tc):
        print('베이비 진')
    else:
        print('베이비 진 아님!')