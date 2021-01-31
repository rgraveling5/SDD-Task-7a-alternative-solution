attempts = 0

file = open('input_data.txt','r')

line = file.read()

file.close()


#Writing File

password_enter = input('Please enter your password: ')

file = open('output_data.txt','w')

file.write(password_enter)

file.close()

while not line == password_enter and attempts <4:
  print('Access denied. try again')
  password_enter = input('Please enter your password: ')
  
  attempts = attempts + 1

  if attempts == 4 and not line == password_enter:
    print('Too many attempts bye:() ')

if line == password_enter and attempts <=4 :
  print('Access granted')

file = open('output_data.txt','w')

file.write(password_enter)

file.close()


