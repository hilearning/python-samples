# 生成随机密码
import random
import string

def generate_random_string(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

password = generate_random_string(12)
print(f"Generated Password: {password}")
