import random
from string import digits
from string import punctuation
from string import ascii_letters

jk_Char=ascii_letters + digits + punctuation
jk_random=random.SystemRandom()
new_password="".join(jk_random.choice(jk_Char)for i in range(20))
print("You Password is",   new_password)  