

password = input('Please, create your password: ')

has_lower_char = False 
has_upper_char = False 
has_special_char = False 
has_space = False

for char in password: 
    if char.islower(): 
        has_lower_char = True 
    elif char.isupper(): 
        has_upper_char = True 
    elif char.isspace(): 
        has_space = True 
    elif not char.isdigit(): 
        has_special_char= True

min_lenght = len(password) >= 8

password_ok = ( has_lower_char 
               and has_upper_char 
               and has_special_char 
               and min_lenght 
               and not has_space )

if password_ok == True: 
    print('Your password is correct.') 
else: 
    if not has_lower_char: print('Your password does not have a lower character.') 
    if not has_upper_char: print('Your password does not have an upper character.') 
    if not has_special_char: print('Your password does not have a special character.') 
    if has_space: print('Your password should not have a space.') 
    if not min_lenght: print('Your password does not have a required lenght.')