stack = []  # В Python стек реализован через список

status = not stack  # Список пуст
# True
stack.append(1)  # [1]
stack.append(2)  # [1, 2]
stack.append(3)  # [1, 2, 3]
status = not stack  # Список не пустой
# False
status = stack
# [1, 2, 3]
stack.pop()  # В стеке [1, 2]
# 3
stack.pop()  # В стеке [1]
# 2
stack.pop()  # В стеке пусто
# 1
status = not stack
# True