# 将句子中每个单词的首字母大写
def capitalize_words(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

sentence = "hello world! this is python."
capitalized_sentence = capitalize_words(sentence)
print(capitalized_sentence)
