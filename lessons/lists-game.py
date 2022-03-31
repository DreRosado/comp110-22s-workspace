"""Examples of using lists in a simple 'game'."""


from random import randint

rolls: list[int] = list()

while len(rolls) == 0 or rolls [len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))

print (rolls) 
rolls.pop(len(rolls)//2)
print(rolls)

# rolls.append(randint(1, 6))
# rolls.append(randint(1,6))
# print(rolls)
# print(rolls[0])

# print(len(rolls))

# print(rolls[len(rolls) - 1 ])