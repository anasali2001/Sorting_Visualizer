from random import randint
#GENERATE THREE FILES
print("Generating Files.....")

f1 = open("small.txt", "w")
for i in range(10):
            i = randint(1, 100)
            i = str(i)
            f1.write(i + "\n")
f1.close()

f1 = open("medium.txt", "w")
for i in range(1000):
            i = randint(100, 999)
            i = str(i)
            f1.write(i + "\n")
f1.close()

f1 = open("high.txt", "w")
for i in range(1000000):
            i = randint(100000, 999999)
            i = str(i)
            f1.write(i + "\n")
f1.close()