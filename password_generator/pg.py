import random

alphabets = []
numbers = []
symbols=['!','#','$','%','&','(',')','*','+']

for char in range(ord('a'),ord('z')+1):
  alphabets.append(chr(char))
  
for num in range(ord('0'),ord('9')+1):
  numbers.append(chr(num))

print("\nWellcome to the Secured Password Generator!\n")

nr_letters = int(input("How many letters do you want in your password?\n"))
nr_numbers = int(input("How many numbers do you want in your password?\n"))
nr_symbols = int(input("How many symbols do you want in your password?\n"))

generate_characters = []
generate_numbers = []
generate_symbols = []
 
#random.choics(list)

for i in range(1,nr_letters+1):
  random_index = random.randint(0,len(alphabets)-1)
  random_style = random.randint(0,101)
  if random_style%2==0 :
    generate_characters.append(alphabets[random_index].upper())
  else:
    generate_characters.append(alphabets[random_index])
    
  
for i in range(1,nr_numbers+1):
  random_index = random.randint(0,len(numbers)-1)
  generate_numbers.append(numbers[random_index])
  
for i in range(1,nr_symbols+1):
  random_index = random.randint(0,len(symbols)-1)
  generate_symbols.append(symbols[random_index])

password = []
password.extend(generate_characters)
password.extend(generate_numbers)
password.extend(generate_symbols)

normal_password = ""
hard_password = ""

for passd in password:
  normal_password+=passd
  
#random.shuffle(x)

for i in range(0,len(password)):
  ran_i = random.randint(0,len(password)-1)
  hard_password+=password[ran_i]
  password.remove(password[ran_i])

print(normal_password)
print(hard_password)




