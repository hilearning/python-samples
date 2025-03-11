# 检查字符串是否为回文
def is_palindrome(s):
    return s == s[::-1]

text = "racecar"
if is_palindrome(text):
    print(f"'{text}' is a palindrome.")
else:
    print(f"'{text}' is not a palindrome.")
