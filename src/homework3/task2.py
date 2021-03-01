# List practice
import copy as copy
# 1. Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']
lst = [i + j for i in 'ab' for j in 'bcd']

# 2. Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
lst_ = lst[0::2]

# 3. Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
ls = [i + j for i in '1234' for j in 'a']

# 4.Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
print(lst.pop(1))

# 5. Скопируйте список и добавьте в него элемент '2a'
# так чтобы в исходном списке этого элемента не было.
lsst = copy.copy(lst)
lsst.insert(1, '2a')
print(lsst)
print(lst)
