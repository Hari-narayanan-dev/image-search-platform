#encrypting password and verifying it

# from app.config.security import hash_password, verify_password

# password = "admin123"

# hashed = hash_password(password)

# print(hashed)

# print(verify_password(password, hashed))

#creating access token
from app.config.security import create_access_token

token = create_access_token(
    {
        "sub": "hari@gmail.com"
    }
)

print(token)