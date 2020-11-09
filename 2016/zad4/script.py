import random

for i in range(10000):
    with open('punkty.txt', 'a') as f:
        f.write(str(random.randrange(0, 400)) + ' ' + str(random.randrange(0, 400)) + '\n')