import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'zl존코드'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909


# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

# --- 메인 소켓 통신부 ---
sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))
send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')

while True:
    recv_data = (sock.recv(1024)).decode()
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx]); idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        continue

    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    angle = 0.0
    power = 0.0

    # ############################
    # --- 전략 코드 시작 ---
    # ############################

    # --- 1. 환경 설정 및 공 분류 ---
    Ball_R = 5.73
    HOLE_OFFSET = 3.0 
    
    EFFECTIVE_HOLES = [
        (0 - HOLE_OFFSET, 0 - HOLE_OFFSET), (127, 0 - HOLE_OFFSET), (254 + HOLE_OFFSET, 0 - HOLE_OFFSET),
        (0 - HOLE_OFFSET, 127 + HOLE_OFFSET), (127, 127 + HOLE_OFFSET), (254 + HOLE_OFFSET, 127 + HOLE_OFFSET)
    ]
    
    myball = (balls[0][0], balls[0][1])
    obj_balls = []
    enemy_balls = []
    black_ball = None

    my_primary_targets_indices = [1, 3] if order == 1 else [2, 4]
    is_8ball_turn = all(balls[i][0] < 0 for i in my_primary_targets_indices)

    for i in range(1, 6):
        if balls[i][0] < 0: continue
        ball_pos = (balls[i][0], balls[i][1])
        if i == 5:
            black_ball = ball_pos
            if is_8ball_turn: obj_balls.append(ball_pos)
        elif i in my_primary_targets_indices:
            obj_balls.append(ball_pos)
        else:
            enemy_balls.append(ball_pos)
    
    all_obstacles_for_pathing = enemy_balls
    if not is_8ball_turn and black_ball:
        all_obstacles_for_pathing.append(black_ball)
    
    all_balls_with_type = [(b, 'obj') for b in obj_balls] + [(b, 'enemy') for b in enemy_balls]

    # --- 2. 기본 삼각함수 기반 보조 함수 ---
    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def path_is_clear(p1, p2, obstacles, clearance):
        p1_x, p1_y = p1; p2_x, p2_y = p2
        line_dist = distance(p1, p2)
        if line_dist < 1e-6: return False
        for obs in obstacles:
            if obs == p1 or obs == p2: continue
            obs_x, obs_y = obs
            dot_product = (p2_x - p1_x) * (obs_x - p1_x) + (p2_y - p1_y) * (obs_y - p1_y)
            if dot_product < 0 or dot_product > line_dist**2: continue
            perp_dist = abs((p2_x - p1_x)*(p1_y - obs_y) - (p1_x - obs_x)*(p2_y - p1_y)) / line_dist
            if perp_dist < clearance: return False
        return True

    def find_first_hit(start, direction_rad, balls_to_check):
        dir_x, dir_y = math.cos(direction_rad), math.sin(direction_rad)
        closest_dist = float('inf'); first_hit_type = None
        for ball_pos, ball_type in balls_to_check:
            oc_x, oc_y = ball_pos[0] - start[0], ball_pos[1] - start[1]
            proj_dist = oc_x * dir_x + oc_y * dir_y
            if proj_dist <= 0: continue
            perp_dist_sq = (oc_x**2 + oc_y**2) - proj_dist**2
            if perp_dist_sq > Ball_R**2: continue
            hit_dist = proj_dist - math.sqrt(Ball_R**2 - perp_dist_sq)
            if hit_dist < closest_dist:
                closest_dist = hit_dist; first_hit_type = ball_type
        return first_hit_type

    def predict_and_check_scratch(myball_pos, aim_point_pos, holes):
        dist_myball_aim = distance(myball_pos, aim_point_pos)
        if dist_myball_aim < 1: return True
        dx = aim_point_pos[0] - myball_pos[0]; dy = aim_point_pos[1] - myball_pos[1]
        tangent_vec = (-dy, dx)
        p1 = aim_point_pos; p2 = (p1[0] + tangent_vec[0], p1[1] + tangent_vec[1])
        if distance(p1, p2) < 1: return False
        for hole in holes:
            dist_to_line = abs((p2[0]-p1[0])*(p1[1]-hole[1]) - (p1[0]-hole[0])*(p2[1]-p1[1])) / distance(p1,p2)
            if dist_to_line < Ball_R: return True
        return False
    
    # --- 3. 샷 후보 생성 및 다차원 평가 ---
    candidate_shots = []

    for obj in obj_balls:
        for hole in EFFECTIVE_HOLES:
            angle_hole_to_obj = math.atan2(obj[1] - hole[1], obj[0] - hole[0])
            aim_point = (obj[0] + Ball_R * math.cos(angle_hole_to_obj), obj[1] + Ball_R * math.sin(angle_hole_to_obj))
            
            # ★★★ 차세대 충돌 회피 시스템 ★★★
            # 모든 장애물에 대해 더욱 엄격한 안전거리(공 2개 너비) 적용하여 2차 충돌 방지
            clearance_all = Ball_R * 2.0 
            
            obstacles_for_check = [b for b in (obj_balls + enemy_balls) if b != obj]
            if not is_8ball_turn and black_ball:
                # 8번 공은 훨씬 더 넓게 회피 (공 3개 너비)
                if not path_is_clear(myball, aim_point, [black_ball], Ball_R * 3.0): continue
                if not path_is_clear(obj, hole, [black_ball], Ball_R * 3.0): continue
                obstacles_for_check.append(black_ball)
            
            if not path_is_clear(myball, aim_point, obstacles_for_check, clearance_all): continue
            if not path_is_clear(obj, hole, obstacles_for_check, clearance_all): continue
            
            angle_myball_to_aim = math.atan2(aim_point[1] - myball[1], aim_point[0] - myball[0])
            if find_first_hit(myball, angle_myball_to_aim, all_balls_with_type) != 'obj': continue
            if predict_and_check_scratch(myball, aim_point, EFFECTIVE_HOLES): continue

            angle_obj_to_hole_rad = math.atan2(hole[1] - obj[1], hole[0] - obj[0])
            angle_myball_to_obj_rad = math.atan2(obj[1] - myball[1], obj[0] - myball[0])
            vec1 = (math.cos(angle_obj_to_hole_rad), math.sin(angle_obj_to_hole_rad))
            vec2 = (math.cos(angle_myball_to_obj_rad), math.sin(angle_myball_to_obj_rad))
            success_score = vec1[0]*vec2[0] + vec1[1]*vec2[1]

            if success_score < 0.6: continue

            dist_myball_to_aim = distance(myball, aim_point)
            dist_obj_to_hole = distance(obj, hole)
            total_dist = dist_myball_to_aim + dist_obj_to_hole
            efficiency_score = 600 / total_dist

            mue = 5.5
            v1h = (55 + 2 * mue * dist_obj_to_hole)
            v01 = (v1h + 2 * mue * dist_myball_to_aim)**(1 / 2)
            power_norm = v01 / (success_score**(1/2))

            # ★★★ 승리를 위한 공격적 최적화: 점수 가중치 변경 ★★★
            # 최단 경로(효율성)의 가중치를 대폭 상향하여 더 공격적이고 빠른 플레이 스타일 추구
            final_score = (success_score * 1.0) + (efficiency_score * 1.5)
            
            final_angle_deg = ((90 - math.degrees(angle_myball_to_aim)) + 360) % 360
            final_power = min(100, power_norm * 0.42 + 20)
            
            candidate_shots.append({'score': final_score, 'angle': final_angle_deg, 'power': final_power})

    # --- 4. 최종 샷 결정 ---
    if candidate_shots:
        best_shot = max(candidate_shots, key=lambda s: s['score'])
        angle = best_shot['angle']
        power = best_shot['power']
    else:
        # ★★★ 지능형 스누커(Snooker) 수비 전략 ★★★
        best_defense_score = -float('inf')
        defense_shot = None

        # 상대방의 시야를 나의 목적구로 가리는 최적의 수비 위치 탐색
        for obj in obj_balls:
            # 가장 가까운 상대방 공 찾기
            if not enemy_balls: continue
            closest_enemy = min(enemy_balls, key=lambda e: distance(e, obj))

            # 목적구 너머로, 상대 공을 등지고 숨을 위치 계산
            vec_enemy_to_obj = (obj[0] - closest_enemy[0], obj[1] - closest_enemy[1])
            dist_e_o = distance(obj, closest_enemy)
            if dist_e_o < 1: continue
            
            # 목적구 뒤, 상대 공 반대편에 흰 공을 숨기는 것이 목표
            hide_spot = (obj[0] + vec_enemy_to_obj[0]/dist_e_o * Ball_R, 
                         obj[1] + vec_enemy_to_obj[1]/dist_e_o * Ball_R)
            
            # 목적구를 쳐서 흰 공을 hide_spot으로 보내기 위한 조준점 계산
            angle_obj_to_hide = math.atan2(hide_spot[1] - obj[1], hide_spot[0] - obj[0])
            aim_point = (obj[0] - Ball_R * math.cos(angle_obj_to_hide),
                         obj[1] - Ball_R * math.sin(angle_obj_to_hide))

            if not path_is_clear(myball, aim_point, all_obstacles_for_pathing, Ball_R): continue
            
            angle_myball_to_aim = math.atan2(aim_point[1] - myball[1], aim_point[0] - myball[0])
            if find_first_hit(myball, angle_myball_to_aim, all_balls_with_type) == 'obj':
                score = distance(myball, closest_enemy) # 상대 공과 멀어지는 것을 점수로
                if score > best_defense_score:
                    best_defense_score = score
                    angle = ((90 - math.degrees(angle_myball_to_aim)) + 360) % 360
                    power = 45 # 위치 제어를 위해 약간 더 강한 힘

    if power == 0.0 and obj_balls:
        # 최후의 수단: 모든 공격/수비가 막혔을 때 멈춤 방지
        closest_obj = min(obj_balls, key=lambda b: distance(myball, b))
        angle_rad = math.atan2(closest_obj[1] - myball[1], closest_obj[0] - myball[0])
        angle = ((90 - math.degrees(angle_rad)) + 360) % 360
        power = 30 
    
    print(f'Angle: {angle}, Power: {power}')
    # ############################
    # --- 전략 코드 종료 ---
    # ############################
    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')