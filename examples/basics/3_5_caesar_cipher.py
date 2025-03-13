# 使用凯撒密码加密文件内容
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

text = "Hello, World!"
shift = 3
encrypted_text = caesar_cipher(text, shift)
print(f"Encrypted: {encrypted_text}")
