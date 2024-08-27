import random
pw = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
save = ''
for i in range(10):
    save = save + random.choice(pw)
print(save)
