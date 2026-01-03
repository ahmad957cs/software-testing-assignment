def login(username, password):
    if not username or not password:
        return False

    if username == "admin" and password == "admin123":
        return True

    return False
