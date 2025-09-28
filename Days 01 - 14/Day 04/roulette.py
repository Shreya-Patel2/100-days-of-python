import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(random.choice(friends))

# if result == 0:
#     print(friends[0])
# elif result == 1:
#     print(friends[1])
# elif result == 2:
#     print(friends[2])
# elif result == 3:
#     print(friends[3])
# else:
#     print(friends[4])

result = random.randint(0,4)
print(friends[result])