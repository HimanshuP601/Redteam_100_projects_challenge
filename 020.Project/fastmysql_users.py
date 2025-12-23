import mysql.connector
from mysql.connector import errorcode

# ===== CONFIG =====
MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = 3306
TIMEOUT = 5
DUMMY_PASSWORD = "invalid_password"
# ==================

def check_user(username):
    try:
        mysql.connector.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=username,
            password=DUMMY_PASSWORD,
            connection_timeout=TIMEOUT
        )
        return "VALID USER (unexpected login)"
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            return "VALID USER (password incorrect)"
        elif err.errno == errorcode.ER_HOST_NOT_PRIVILEGED:
            return "USER EXISTS BUT HOST NOT ALLOWED"
        elif err.errno == errorcode.ER_DBACCESS_DENIED_ERROR:
            return "VALID USER (db access denied)"
        else:
            return f"UNKNOWN RESPONSE ({err.errno})"

def main():
    print(f"[+] MySQL User Footprinting on {MYSQL_HOST}:{MYSQL_PORT}\n")

    with open("users.txt") as f:
        for user in f:
            user = user.strip()
            if not user:
                continue
            result = check_user(user)
            print(f"{user}: {result}")

if __name__ == "__main__":
    main()
