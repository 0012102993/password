#password yaaayy
import time
import random
print("hello monkeyyys!!! type smth so that I can generate a random password 4 u lil' monkeyy!!!")

allowedkeys =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
q1 = int(input("hey lil' monkey, what's the password length going to be??"))
psswrd = ""
for x in range(q1):
    psswrd += random.choice(allowedkeys)

time.sleep(2)
print("loading....")
time.sleep(3)
print("done!!")
time.sleep(2)
print(psswrd)