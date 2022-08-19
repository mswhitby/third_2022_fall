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
  
  # Below we made a "list" of punctuation marks
  punctuation =  [
    ".", "!", "?", ";", ",", "-",":","—","[","]",
    "(",")","{","}","'",'"',"..."
    ]
  
  for char in password:
   
    if char in punctuation:
      print(char)
      has_punctuation = True
      break
  
  print(f"password has punctuation: {has_punctuation}")
  
def check_prime(password):
  has_prime = False
  for char in password:
    if char.isdigit():
      char = int(char)
      half_char = char // 2
      
      for val in range(2, half_char):
        if char % val == 0:
          has_prime = True
          break
        print(val)

# password = user_input_password()
# rule_1 = check_punctuation(password)
# rule_2 = check_prime(password)
