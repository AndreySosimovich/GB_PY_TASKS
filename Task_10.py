# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

coins = [1, 1, 1, 1, 0, 1]
orel = 0
reshka = 0
for i in range(len(coins)):
    if coins[i] == 1:
        orel += 1
    if coins[i] == 0:
        reshka += 1
if orel < reshka:
    count = orel
else:
    count = reshka
print(count)

# coins = [1, 1, 1, 1, 0, 1]
# print(coins.count(0) if coins.count(0) < coins.count(1) else coins.count(1))
