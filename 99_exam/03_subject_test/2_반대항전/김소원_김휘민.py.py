import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = '소원휘민피스'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'
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
BALL_DIAMETER = 5.73

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')


def is_path_clear(start_pos, end_pos, all_balls, balls_to_ignore_indices):
    path_vector = (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
    path_length_sq = path_vector[0]**2 + path_vector[1]**2
    if path_length_sq == 0: return True

    for i, ball_pos in enumerate(all_balls):
        if i in balls_to_ignore_indices or ball_pos[0] < 0:
            continue

        start_to_obstacle = (ball_pos[0] - start_pos[0], ball_pos[1] - start_pos[1])
        dot_product = start_to_obstacle[0] * path_vector[0] + start_to_obstacle[1] * path_vector[1]
        projection = dot_product / path_length_sq

        if 0 < projection < 1:
            closest_point_x = start_pos[0] + projection * path_vector[0]
            closest_point_y = start_pos[1] + projection * path_vector[1]
            dist_sq = (ball_pos[0] - closest_point_x)**2 + (ball_pos[1] - closest_point_y)**2
            
            if dist_sq < (BALL_DIAMETER)**2:
                return False
    return True

while True:
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    split_data = recv_data.split('/')
    idx = 0
    # [수정] 데이터 파싱 루프를 완벽하게 수정했습니다.
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except Exception as e:
        # 정상적인 게임 종료 또는 플레이어 순서 신호가 아닐 때만 오류 메시지를 출력합니다.
        if split_data and not (split_data[0] == str(SIGNAL_ORDER) or split_data[0] == str(SIGNAL_CLOSE)):
            print(f"Data parsing error: {e}. Resend Requested.")
            send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
            sock.send(send_data.encode('utf-8'))
        continue

    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    ##############################
    # 그랜드 마스터 알고리즘 (이 부분은 수정되지 않았습니다)

    # 물리계 및 전략 파라미터
    COR = 0.95
    FRICTION = 10.0
    POWER_SCALING_FACTOR = 150.0
    
    white_ball_pos = balls[0]
    
    my_ball_indices_seq = [1, 3, 5] if order == 1 else [2, 4, 5]
    
    on_table_seq = [i for i in my_ball_indices_seq if balls[i][0] >= 0]
    
    current_targets = []
    next_target_idx = -1
    if on_table_seq:
        first_target = on_table_seq[0]
        if first_target != 5:
            current_targets = [i for i in my_ball_indices_seq if i != 5 and balls[i][0] >= 0]
            next_target_idx = on_table_seq[1] if len(on_table_seq) > 1 else 5
        else:
            current_targets = [5]

    best_shot_overall = {'score': -float('inf')}

    for target_idx in current_targets:
        target_pos = balls[target_idx]
        for hole in HOLES:
            v_th = (hole[0] - target_pos[0], hole[1] - target_pos[1])
            dist_th = math.hypot(*v_th)
            if dist_th == 0: continue
            
            unit_v_th = (v_th[0] / dist_th, v_th[1] / dist_th)
            ghost_pos = (target_pos[0] - unit_v_th[0] * BALL_DIAMETER, target_pos[1] - unit_v_th[1] * BALL_DIAMETER)

            if not is_path_clear(target_pos, hole, balls, [0, target_idx]) or \
               not is_path_clear(white_ball_pos, ghost_pos, balls, [0, target_idx]):
                continue

            v_wg = (ghost_pos[0] - white_ball_pos[0], ghost_pos[1] - white_ball_pos[1])
            dist_wg = math.hypot(*v_wg)
            if dist_wg == 0: continue

            dot_product = v_wg[0]*v_th[0] + v_wg[1]*v_th[1]
            cos_theta = max(-1.0, min(1.0, dot_product / (dist_wg * dist_th)))
            cut_angle_deg = math.degrees(math.acos(cos_theta))
            potting_score = (90 - cut_angle_deg) - (dist_wg + dist_th) * 0.1

            positioning_score = 0
            if next_target_idx != -1:
                next_target_pos = balls[next_target_idx]
                ideal_line_dist = float('inf')
                for next_hole in HOLES:
                    v_next_th = (next_hole[0] - next_target_pos[0], next_hole[1] - next_target_pos[1])
                    dist_next_th = math.hypot(*v_next_th)
                    if dist_next_th == 0: continue
                    unit_v_next = (v_next_th[0] / dist_next_th, v_next_th[1] / dist_next_th)
                    vec_to_next_target = (next_target_pos[0] - ghost_pos[0], next_target_pos[1] - ghost_pos[1])
                    cross_product = vec_to_next_target[0] * unit_v_next[1] - vec_to_next_target[1] * unit_v_next[0]
                    dist_to_line = abs(cross_product)
                    ideal_line_dist = min(ideal_line_dist, dist_to_line)
                positioning_score = 50 / (ideal_line_dist + 10)

            scratch_risk = 0
            for h in HOLES:
                if not is_path_clear(ghost_pos, h, balls, [0, target_idx, next_target_idx if next_target_idx != -1 else -1]):
                    pass
                else:
                    scratch_risk += 300 / (math.hypot(ghost_pos[0] - h[0], ghost_pos[1] - h[1]) + 10)

            total_score = potting_score + positioning_score - scratch_risk
            
            if total_score > best_shot_overall['score']:
                best_shot_overall = {
                    'score': total_score, 'angle': math.degrees(math.atan2(v_wg[0], v_wg[1])),
                    'power_params': {'d_cue': dist_wg, 'd_target': dist_th, 'cos_theta': cos_theta}
                }

    if best_shot_overall['score'] > -float('inf'):
        shot = best_shot_overall
        angle = shot['angle']
        if angle < 0: angle += 360
        
        p = shot['power_params']
        efficiency = (COR**2) * (abs(p['cos_theta'])**1.2)
        if efficiency < 0.05: efficiency = 0.05
        
        energy = (FRICTION * p['d_target']) / efficiency + (FRICTION * p['d_cue'])
        power = math.sqrt(energy) * POWER_SCALING_FACTOR
        if power > 100: power = 100
    else:
        if on_table_seq:
            target_pos = balls[on_table_seq[0]]
            v_wt = (target_pos[0] - white_ball_pos[0], target_pos[1] - white_ball_pos[1])
            angle = math.degrees(math.atan2(v_wt[0], v_wt[1]))
            if angle < 0: angle += 360
            power = 25

    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')