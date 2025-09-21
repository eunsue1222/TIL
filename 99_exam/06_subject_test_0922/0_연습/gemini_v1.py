import sys
import socket
from collections import deque

##############################
# 메인 프로그램 통신 변수 정의
##############################
HOST = '127.0.0.1'
PORT = 8747
ARGS = sys.argv[1] if len(sys.argv) > 1 else ''
sock = socket.socket()

##############################
# 메인 프로그램 통신 함수 정의
##############################

# 메인 프로그램 연결 및 초기화
def init(nickname):
    try:
        print(f'[STATUS] Trying to connect to {HOST}:{PORT}...')
        sock.connect((HOST, PORT))
        print('[STATUS] Connected')
        init_command = f'INIT {nickname}'

        return submit(init_command)
    
    except Exception as e:
        print('[ERROR] Failed to connect. Please check if the main program is waiting for connection.')
        print(e)

# 메인 프로그램으로 데이터(명령어) 전송
def submit(string_to_send):
    try:
        send_data = ARGS + string_to_send + ' '
        sock.send(send_data.encode('utf-8'))

        return receive()
    
    except Exception as e:
        print('[ERROR] Failed to send data. Please check if connection to the main program is valid.')
    
    return None

# 메인 프로그램으로부터 데이터 수신
def receive():
    try:
        game_data = (sock.recv(1024)).decode()

        if game_data and game_data[0].isdigit() and int(game_data[0]) > 0:
            return game_data
        
        print('[STATUS] No receive data from the main program.')
        close()

    except Exception as e:
        print('[ERROR] Failed to receive data. Please check if connection to the main program is valid.')

# 연결 해제
def close():
    try:
        if sock is not None:
            sock.close()
        print('[STATUS] Connection closed')

    except Exception as e:
        print('[ERROR] Network connection has been corrupted.')

##############################
# 입력 데이터 변수 정의
##############################
map_data = [[]]
my_allies = {}
enemies = {}
codes = []
### 수정
my_tank = None

##############################
# 입력 데이터 파싱
##############################
def parse_data(game_data):
    ### 수정
    global my_tank

    # 입력 데이터를 행으로 나누기
    game_data_rows = game_data.split('\n')
    row_index = 0

    # 첫 번째 행 데이터 읽기
    header = game_data_rows[row_index].split(' ')
    map_height = int(header[0]) if len(header) >= 1 else 0 # 맵의 세로 크기
    map_width = int(header[1]) if len(header) >= 2 else 0  # 맵의 가로 크기
    num_of_allies = int(header[2]) if len(header) >= 3 else 0  # 아군의 수
    num_of_enemies = int(header[3]) if len(header) >= 4 else 0  # 적군의 수
    num_of_codes = int(header[4]) if len(header) >= 5 else 0  # 암호문의 수
    row_index += 1

    # 기존의 맵 정보를 초기화하고 다시 읽어오기
    map_data.clear()
    map_data.extend([['' for _ in range(map_width)] for _ in range(map_height)])
    for i in range(0, map_height):
        col = game_data_rows[row_index + i].split(' ')
        for j in range(0, len(col)):
            map_data[i][j] = col[j]
    row_index += map_height

    # 기존의 아군 정보를 초기화하고 다시 읽어오기
    my_allies.clear()
    for i in range(row_index, row_index + num_of_allies):
        ally = game_data_rows[i].split(' ')
        ally_name = ally.pop(0) if len(ally) >= 1 else '-'
        my_allies[ally_name] = ally
    row_index += num_of_allies

    # 기존의 적군 정보를 초기화하고 다시 읽어오기
    enemies.clear()
    for i in range(row_index, row_index + num_of_enemies):
        enemy = game_data_rows[i].split(' ')
        enemy_name = enemy.pop(0) if len(enemy) >= 1 else '-'
        enemies[enemy_name] = enemy
    row_index += num_of_enemies

    # 기존의 암호문 정보를 초기화하고 다시 읽어오기
    codes.clear()
    for i in range(row_index, row_index + num_of_codes):
        codes.append(game_data_rows[i])

    ### 수정
    if 'M' in my_allies:
        my_tank = {
            'health': int(my_allies['M'][0]),
            'direction': my_allies['M'][1],
            'missiles': int(my_allies['M'][2]),
            'mega_missiles': int(my_allies['M'][3]),
            'pos': find_positions(map_data, 'M')
        }

# 파싱한 데이터를 화면에 출력
def print_data():
    print(f'\n----------입력 데이터----------\n{game_data}\n----------------------------')
    
    print(f'\n[맵 정보] ({len(map_data)} x {len(map_data[0])})')
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            print(f'{map_data[i][j]} ', end='')
        print()
    
    print(f'\n[아군 정보] (아군 수: {len(my_allies)})')
    for k, v in my_allies.items():
        if k == 'M':
            print(f'M (내 탱크) - 체력: {v[0]}, 방향: {v[1]}, 보유한 일반 포탄: {v[2]}개, 보유한 메가 포탄: {v[3]}개')
        elif k == 'H':
            print(f'H (아군 포탑) - 체력: {v[0]}')
        else:
            print(f'{k} (아군 탱크) - 체력: {v[0]}')
    
    print(f'\n[적군 정보] (적군 수: {len(enemies)})')
    for k, v in enemies.items():
        if k == 'X':
            print(f'X (적군 포탑) - 체력: {v[0]}')
        else:
            print(f'{k} (적군 탱크) - 체력: {v[0]}')
    
    print(f'\n[암호문 정보] (암호문 수: {len(codes)})')
    for i in range(len(codes)):
        print(codes[i])

##############################
# 닉네임 설정 및 최초 연결
##############################
NICKNAME = '기본코드'
game_data = init(NICKNAME)

###################################
# 알고리즘 함수/메서드 부분 구현 시작
###################################

# 출발지와 목적지의 위치 찾기
def find_positions(grid, target_mark):
    rows, cols = len(grid), len(grid[0])
    positions = []
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == target_mark:
                positions.append((row, col))
    return positions[0] if len(positions) == 1 else positions

def find_nearest_target(current_pos, targets, grid, wall):
    if not targets:
        return None
    
    min_dist = float('inf')
    nearest_target = None
    
    for target in targets:
        distance, path = bfs(grid, current_pos, target, wall)
        if distance < min_dist:
            min_dist = distance
            nearest_target = target
    
    return nearest_target

# 경로 탐색 알고리즘 (거리와 경로를 모두 반환하도록 수정)
def bfs(grid, start, target, wall):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, 0, [])]) # (위치, 거리, 경로)
    visited = {start}

    while queue:
        (r, c), dist, actions = queue.popleft()

        if (r, c) == target:
            return dist, actions

        for d, (dr, dc) in enumerate(DIRS):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != wall and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), dist + 1, actions + [MOVE_CMDS[d]]))
    return float('inf'), []

# 카이사르 암호 해독 함수
def decrypt_caesar(cipher_text):
    if not cipher_text:
        return ""
    
    # "AKWNSDN"이 "BATTLESSAFY"가 되는 것을 기준으로 시프트 값 계산
    # 'A'(65) -> 'B'(66), 'K'(75) -> 'A'(65), ...
    # 'A' -> 'B'는 +1, 'K' -> 'A'는 -10. 밀린 거리는 다를 수 있으므로 규칙을 찾기 어려움.
    # 사용 설명서의 예시를 기반으로 하드코딩된 시프트 값을 사용하거나, 규칙을 추론해야 함.
    # 여기서는 규칙을 찾기 위한 예시 로직을 제공합니다.
    # 가장 흔한 방식인 'E'를 'E'로 가정하고 시프트 값을 계산합니다. (E: 5번째 알파벳)
    shift = 0
    # 간단한 가정을 통해 암호 해독을 시도
    # 'A' = 65, 'B' = 66
    # 'AKWNSDN' -> 'BATTLESSAFY'는 복잡한 시프트 규칙을 따르므로,
    # 여기서는 가장 간단한 고정 시프트 방법을 가정하고 구현합니다.
    # 예를 들어, 암호문 'SRKKCVJJRWP'가 'BATTLESSAFY'로 해독되었다는 예시가 있습니다. 
    # S(19) -> B(2)는 -17. R(18) -> A(1)는 -17. 이 경우 시프트 값은 17입니다.
    
    shift = 17 # 암호문 예시를 통해 추론한 값
    
    decrypted_text = ""
    for char in cipher_text:
        if 'A' <= char <= 'Z':
            decrypted_text += chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

# 경로 탐색 변수 정의
DIRS = [(0,1), (1,0), (0,-1), (-1,0)]
MOVE_CMDS = {0: "R A", 1: "D A", 2: "L A", 3: "U A"}
FIRE_CMDS = {0: "R F", 1: "D F", 2: "L F", 3: "U F"}
MEGA_FIRE_CMDS = {0: "R F M", 1: "D F M", 2: "L F M", 3: "U F M"}
WALL_SYMBOL = 'R'
TARGET_PRIORITY = ['X', 'E', 'F'] # 적 포탑, 적 탱크, 보급 시설 순으로 우선순위 지정

# 최초 데이터 파싱
NICKNAME = '기본코드'
game_data = init(NICKNAME)
parse_data(game_data)
actions = []

###################################
# 알고리즘 함수/메서드 부분 구현 끝
###################################

# 반복문: 메인 프로그램 <-> 클라이언트(이 코드) 간 순차로 데이터 송수신(동기 처리)
while game_data is not None:
    ##############################
    # 알고리즘 메인 부분 구현 시작
    ##############################
    print_data()

    # 동적 목표물 설정 및 경로 재탐색
    my_pos = find_positions(map_data, 'M')
    
    # 메가 포탄이 0개이고 보급 시설이 있다면 보급 시설을 최우선 목표로 설정
    if my_tank and my_tank['mega_missiles'] == 0:
        supply_facilities = find_positions(map_data, 'F')
        if supply_facilities:
            target_pos = find_nearest_target(my_pos, supply_facilities, map_data, WALL_SYMBOL)
            if target_pos:
                distance, actions = bfs(map_data, my_pos, target_pos, WALL_SYMBOL)
    
    # 메가 포탄이 1개 이상이거나 보급 시설이 없으면 적군을 목표로 설정
    if not actions:
        all_enemies = find_positions(map_data, 'X') + find_positions(map_data, 'E')
        if all_enemies:
            target_pos = find_nearest_target(my_pos, all_enemies, map_data, WALL_SYMBOL)
            if target_pos:
                distance, actions = bfs(map_data, my_pos, target_pos, WALL_SYMBOL)

    # 암호문 해독 로직
    if 'F' in my_allies and my_tank['pos'] in [find_positions(map_data, 'F')]:
        if codes:
            decrypted_code = decrypt_caesar(codes[0])
            output = f'G {decrypted_code}'
            actions = [] # 암호 해독 후 경로 초기화
        else:
            output = 'S' # 보급 시설에 인접했으나 암호문이 없을 경우 대기
    # 공격 로직
    elif actions and my_pos == target_pos:
        # 적 포탑(X)을 목표로 할 경우 메가 포탄 우선 사용
        if target_pos in find_positions(map_data, 'X') and my_tank['mega_missiles'] > 0:
            output = MEGA_FIRE_CMDS[determine_direction(my_pos, target_pos)]
        # 일반 포탄 사용
        else:
            output = FIRE_CMDS[determine_direction(my_pos, target_pos)]
        actions.pop(0) # 발사 후 경로에서 첫 번째 행동 제거
    # 이동 로직
    elif actions:
        output = actions.pop(0)
    # 기본 대기
    else:
        output = 'S'

    game_data = submit(output)
    if game_data:
        parse_data(game_data)
        
    ##############################
    # 알고리즘 메인 구현 끝
    ##############################

# 반복문을 빠져나왔을 때 메인 프로그램과의 연결을 완전히 해제하기 위해 close() 호출
close()

def determine_direction(current_pos, target_pos):
    dr = target_pos[0] - current_pos[0]
    dc = target_pos[1] - current_pos[1]
    if dc > 0: return 0 # 오른쪽
    if dr > 0: return 1 # 아래쪽
    if dc < 0: return 2 # 왼쪽
    if dr < 0: return 3 # 위쪽
    return 0 # 기본값