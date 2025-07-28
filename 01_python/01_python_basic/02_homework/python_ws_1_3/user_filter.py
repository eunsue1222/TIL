def filter_over18(users):
    return [user for user in users if user['age'] >= 18]

def filter_isactive(users):
    return [user for user in users if user['is_active'] == True]

def filter_over18_and_isactive(users):
    return [user for user in users if user['age'] >= 18 and user['is_active'] == True]