import random
import array
maximum_len=12

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
locase_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
  
upcase_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
           '*', '(', ')', '<']                     
combined_list = digits + upcase_characters + locase_characters + symbols
rand_digit = random.choice(digits)
rand_upper = random.choice(upcase_characters)
rand_lower = random.choice(locase_characters)
rand_symbol = random.choice(symbols)

temp_password = rand_digit + rand_upper + rand_lower + rand_symbol
for a in range(maximum_len - 4):
    temp_password = temp_password + random.choice(combined_list)

    temp_password_list = array.array('u', temp_password)
    random.shuffle(temp_password_list)

    password = ""
for a in temp_password_list:
        password = password + a
        
print(password)
