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
        return None

def submit(string_to_send):
    try:
        send_data = ARGS + string_to_send + ' '
        sock.send(send_data.encode('utf-8'))
        return receive()
    except Exception as e:
        print('[ERROR] Failed to send data. Please check if connection to the main program is valid.')
    return None

def receive():
    try:
        game_data = (sock.recv(1024)).decode()
        if game_data and game_data[0].isdigit() and int(game_data[0]) > 0:
            return game_data
        print('[STATUS] No receive data from the main program.')
        close()
    except Exception as e:
        print('[ERROR] Failed to receive data. Please check if connection to the main program is valid.')
    return None

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
my_tank = None

##############################
# 입력 데이터 파싱
##############################
def parse_data(game_data):
    global my_tank
    game_data_rows = game_data.split('\n')
    row_index = 0
    header = game_data_rows[row_index].split(' ')
    map_height = int(header[0]) if len(header) >= 1 else 0
    map_width = int(header[1]) if len(header) >= 2 else 0
    num_of_allies = int(header[2]) if len(header) >= 3 else 0
    num_of_enemies = int(header[3]) if len(header) >= 4 else 0
    num_of_codes = int(header[4]) if len(header) >= 5 else 0
    row_index += 1

    map_data.clear()
    map_data.extend([['' for _ in range(map_width)] for _ in range(map_height)])
    for i in range(0, map_height):
        col = game_data_rows[row_index + i].split(' ')
        for j in range(0, len(col)):
            map_data[i][j] = col[j]
    row_index += map_height

    my_allies.clear()
    for i in range(row_index, row_index + num_of_allies):
        ally = game_data_rows[i].split(' ')
        ally_name = ally.pop(0) if len(ally) >= 1 else '-'
        my_allies[ally_name] = ally
    row_index += num_of_allies

    enemies.clear()
    for i in range(row_index, row_index + num_of_enemies):
        enemy = game_data_rows[i].split(' ')
        enemy_name = enemy.pop(0) if len(enemy) >= 1 else '-'
        enemies[enemy_name] = enemy
    row_index += num_of_enemies

    codes.clear()
    for i in range(row_index, row_index + num_of_codes):
        codes.append(game_data_rows[i])

    if 'M' in my_allies:
        my_tank = {
            'health': int(my_allies['M'][0]),
            'direction': my_allies['M'][1],
            'missiles': int(my_allies['M'][2]),
            'mega_missiles': int(my_allies['M'][3]),
            'pos': find_position(map_data, 'M')
        }

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

###################################
# 알고리즘 함수/메서드 부분 구현 시작
###################################
def find_position(grid, target_mark):
    rows, cols = len(grid), len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == target_mark:
                return (row, col)
    return None

def find_targets(grid, target_marks):
    rows, cols = len(grid), len(grid[0])
    positions = {}
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] in target_marks:
                mark = grid[row][col]
                if mark not in positions:
                    positions[mark] = []
                positions[mark].append((row, col))
    return positions

def find_nearest_target(current_pos, targets, grid, obstacles):
    if not targets:
        return None
    
    min_dist = float('inf')
    nearest_target = None
    
    for target in targets:
        distance, path = bfs(grid, current_pos, target, obstacles)
        if distance < min_dist:
            min_dist = distance
            nearest_target = target
    
    return nearest_target

def bfs(grid, start, target, obstacles):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, 0, [])])
    visited = {start}
    
    while queue:
        (r, c), dist, actions = queue.popleft()

        if (r, c) == target:
            return dist, actions

        for d, (dr, dc) in enumerate(DIRS):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in obstacles and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), dist + 1, actions + [MOVE_CMDS[d]]))
    return float('inf'), []

def decrypt_caesar(cipher_text):
    if not cipher_text:
        return ""
    shift = 17
    decrypted_text = ""
    for char in cipher_text:
        if 'A' <= char <= 'Z':
            decrypted_text += chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

def get_movement_command(current_dir, target_dir):
    if current_dir == 'U' and target_dir == 'U': return 'U A'
    if current_dir == 'D' and target_dir == 'D': return 'D A'
    if current_dir == 'L' and target_dir == 'L': return 'L A'
    if current_dir == 'R' and target_dir == 'R': return 'R A'
    
    if current_dir == 'U':
        if target_dir == 'R': return 'R A'
        if target_dir == 'L': return 'L A'
        if target_dir == 'D': return 'U R R' # 방향을 두 번 바꿔야 함
    if current_dir == 'D':
        if target_dir == 'R': return 'R A'
        if target_dir == 'L': return 'L A'
        if target_dir == 'U': return 'D R R'
    if current_dir == 'L':
        if target_dir == 'U': return 'U A'
        if target_dir == 'D': return 'D A'
        if target_dir == 'R': return 'L R R'
    if current_dir == 'R':
        if target_dir == 'U': return 'U A'
        if target_dir == 'D': return 'D A'
        if target_dir == 'L': return 'R R R'

def determine_fire_direction(current_pos, target_pos):
    if not current_pos or not target_pos:
        return 'S' # 예외 처리
    
    if current_pos[1] < target_pos[1]: return 'R' # 오른쪽
    if current_pos[1] > target_pos[1]: return 'L' # 왼쪽
    if current_pos[0] < target_pos[0]: return 'D' # 아래쪽
    if current_pos[0] > target_pos[0]: return 'U' # 위쪽
    return my_tank['direction'] # 같은 위치에 있을 경우 현재 방향 유지

# 경로 탐색 변수 정의
DIRS = [(0,1), (1,0), (0,-1), (-1,0)] # R, D, L, U
MOVE_CMDS = {0: "R A", 1: "D A", 2: "L A", 3: "U A"}
FIRE_CMDS = {'U': 'U F', 'D': 'D F', 'L': 'L F', 'R': 'R F'}
MEGA_FIRE_CMDS = {'U': 'U F M', 'D': 'D F M', 'L': 'L F M', 'R': 'R F M'}
WALL_SYMBOL = 'R'
TARGET_PRIORITY = {'X': 1, 'E': 2, 'F': 3} # 적 포탑, 적 탱크, 보급 시설

# 최초 데이터 파싱
NICKNAME = '개선코드'
game_data = init(NICKNAME)
actions = []
if game_data:
    parse_data(game_data)

###################################
# 알고리즘 함수/메서드 부분 구현 끝
###################################
while game_data is not None:
    ##############################
    # 알고리즘 메인 부분 구현 시작
    ##############################
    print_data()

    my_pos = my_tank['pos'] if my_tank else None
    
    # 장애물 위치 업데이트
    obstacles = set()
    for row in range(len(map_data)):
        for col in range(len(map_data[0])):
            if map_data[row][col] in ['R', 'X', 'E', 'A', 'H']: # 벽, 적 탱크, 적 포탑, 아군 탱크, 아군 포탑을 장애물로 간주
                obstacles.add((row, col))
    
    if my_pos in obstacles:
        obstacles.remove(my_pos)
    
    # 동적 목표물 설정 및 경로 재탐색
    target_pos = None
    
    # 1. 메가 포탄이 부족하고 보급 시설이 있다면 보급 시설을 최우선 목표로
    if my_tank and my_tank['mega_missiles'] == 0:
        supply_facilities = find_targets(map_data, ['F'])
        if 'F' in supply_facilities:
            target_pos = find_nearest_target(my_pos, supply_facilities['F'], map_data, obstacles)
    
    # 2. 보급 시설이 없거나 메가 포탄이 충분하면 적군 공격 목표 설정
    if not target_pos:
        enemy_targets = []
        for name, data in enemies.items():
            if name in ['X', 'E']:
                pos = find_position(map_data, name)
                if pos:
                    enemy_targets.append({'pos': pos, 'health': int(data[0])})

        # 체력이 가장 낮은 적군 우선 공격
        if enemy_targets:
            sorted_enemies = sorted(enemy_targets, key=lambda x: x['health'])
            target_pos = sorted_enemies[0]['pos']

    # 경로 재탐색
    if target_pos:
        distance, actions = bfs(map_data, my_pos, target_pos, obstacles)

    # 암호문 해독 로직
    if my_tank and map_data[my_pos[0]][my_pos[1]] == 'F' and codes:
        decrypted_code = decrypt_caesar(codes[0])
        output = f'G {decrypted_code}'
        actions = [] # 암호 해독 후 경로 초기화
    # 공격 로직
    elif actions and my_pos == target_pos:
        fire_dir = determine_fire_direction(my_pos, target_pos)
        if my_tank['mega_missiles'] > 0 and (map_data[target_pos[0]][target_pos[1]] == 'X' or map_data[target_pos[0]][target_pos[1]] == 'E'):
            output = MEGA_FIRE_CMDS[fire_dir]
        else:
            output = FIRE_CMDS[fire_dir]
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
close()