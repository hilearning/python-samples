# 简单的单词计数器
def count_words(text):
    return len(text.split())

text = "Python is an amazing programming language"
word_count = count_words(text)
print(f"The text has {word_count} words.")
