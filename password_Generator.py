import random
letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
symbol=['!','#','$','%','&','*','(',')','+']
number=['0','1','2','3','4','5','6','7','8','9']

nr_letter=int(input("How many letters do you want in your password: \n"))
nr_symbol=int(input("How many symbols do you want in your password: \n"))
nr_number=int(input("How many numbers do you want in your password: \n"))


#easy level

# password=""
# for char in range(1, nr_letter + 1):
#     password += random.choice(letter)
#
# for sym in range(1, nr_symbol +1):
#     password += random.choice(symbol)
#
# for num in range(1, nr_number +1):
#     password += random.choice(number)
#
# print(password)

#hard level
password_list=[]
for char in range(1, nr_letter + 1):
    password_list += random.choice(letter)

for sym in range(1, nr_symbol +1):
    password_list += random.choice(symbol)

for num in range(1, nr_number +1):
    password_list += random.choice(number)

print(password_list)
random.shuffle(password_list)
print(password_list)

password=""
for char in password_list:
    password+=char

print(f"Your password is :  {password}")






