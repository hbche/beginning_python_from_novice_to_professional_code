# 在屏幕中央打印一个句子
sentence = input("Sentence: ")

# 假设控制台屏幕宽度为80
screen_width = 80
sentence_width = len(sentence)
box_width = sentence_width + 6
margin_left = (screen_width - box_width) // 2

print()
print(' ' * margin_left + '+' + '-' * box_width + '+')
print(' ' * margin_left + '|' + ' ' * box_width + '|')
print(' ' * margin_left + '|' + ' ' * 3 + sentence + ' ' * 3 + '|')
print(' ' * margin_left + '|' + ' ' * box_width + '|')
print(' ' * margin_left + '+' + '-' * box_width + '+')