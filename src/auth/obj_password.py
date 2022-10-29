from flask_bcrypt import generate_password_hash, check_password_hash

class Password():

    def create_password(self, user_password_plain:str):
        return generate_password_hash(user_password_plain.encode(),10)

    def match_password(self, user_password_DB:str, user_password_plain:str):
        return check_password_hash(user_password_DB.encode(), user_password_plain.encode())
