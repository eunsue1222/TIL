import csv

def load_clothes_rules(csv_path):
    """
    clothes_rules.csv 파일을 파싱하여 룰 리스트 반환
    """
    rules = []
    with open(csv_path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # min_temp, max_temp는 float, rain은 bool/any로 변환
            row['min_temp'] = float(row['min_temp'])
            row['max_temp'] = float(row['max_temp'])
            if row['rain'].lower() == 'any':
                row['rain'] = 'any'
            else:
                row['rain'] = row['rain'].lower() == 'true'
            rules.append(row)
    return rules
