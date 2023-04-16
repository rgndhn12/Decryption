# Dahan, Regine Fae M. (BSCPE 1-5) DECRYPTION

#introduction
import pyfiglet
import time

the_intro ='Starting...'
print(pyfiglet.figlet_format(the_intro,font="digital"))
time.sleep(3)
print('Hello! This program is entitled DECRYPTION! It will accept a\nstring as encrypted text, then the program will decrypt it.')
time.sleep(2)

now_begin ='Let\'s start'
print(pyfiglet.figlet_format(now_begin,font="bubble"))
time.sleep (2)

# ask the user for input
user_input = input (' Type your string >>> ')
the_output = ''

# user's input to be decrypt through...
for i in range (len(user_input)):

#   if *, substitute it to 
    if user_input[i] == '*':
        the_output += 'a'
    
#   if &, substitute it to e
    elif user_input[i] == '&':
        the_output += 'e'

#   if #, substitute it to i
    elif user_input[i] == '#':
        the_output += 'i'

#   if +, substitute it to o
    elif user_input[i] == '+':
        the_output += 'o'
        
#   if !, substitute it to u
    elif user_input[i] == '!':
        the_output += 'u'
    
    else:
        the_output += user_input[i]

# display the output
time.sleep(1)
the_decryption = ' Decrypting the string...'
print(pyfiglet.figlet_format(the_decryption,font="digital"))
time.sleep(2)
print ('The string\'s decryption is >>>',the_output)
