# Dahan, Regine Fae M. (BSCPE 1-5) DECRYPTION

# ask the user for input
user_input = input (' Type your string >>> ')
the_output = ''

# user's input to be decrypt through...
for i in range (len(user_input)):

#   if *, substitute it to 
    if user_input[i] == '*':
        the_output += 'a'
    else:
        the_output += user_input[i]

#   if &, substitute it to e
#   if #, substitute it to i
#   if +, substitute it to o
#   if !, substitute it to u

# display the output
print ('The string\'s decryption is >>>',the_output)
