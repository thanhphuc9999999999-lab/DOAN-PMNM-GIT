def check_user_format(data):
    return len(str(data)) > 0

def validate_admin_input(data):
    return data is not None

def process_data(data):
    # Ham xu ly chinh
    return check_user_format(data)
