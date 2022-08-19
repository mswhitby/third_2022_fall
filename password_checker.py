# 1. Must have at least one punctuation mark
# 2. Must have at least one prime number
# 3. Must have the name of a planet
# 4. Must have a favorite food???
# 5. Must have the name of a continent
# 6. Must have exactly 22 digits

def user_input_password():
  password = input(
    """
    1. Must have at least one punctuation mark
    2. Must have at least one prime number
    3. Must have the name of a planet
    4. Must have a favorite food???
    5. Must have the name of a continent
    6. Must have exactly 22 digits
  
    """
    
    "Please create a password that meets the conditions above: "
  )
  
  return password


def check_punctuation(password):
  has_punctuation = False
  punctuation =  [".", "!", "?", ";", ",", "-"]
  
  for char in password:
    print(char)

    if char in punctuation:
      has_punctuation = True
  
  print(has_punctuation)


password = user_input_password()
rule_1 = check_punctuation(password)
      
