USER_ACCESS = "admin"
USER_PASSWORD = "admin123"

def access_protection(func):
    def wrapper(*args, **kwargs):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == USER_ACCESS and password == USER_PASSWORD:
            return func(*args, **kwargs)
        return "Access Denied"
    return wrapper

@access_protection
def protected_function():
    return "Access Granted"

print(protected_function())