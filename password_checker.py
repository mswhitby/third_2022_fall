# password = input()
password = "2manyRULES#"

punctuation =  [".", "!", "?", ";", ",", "-"]

for char in password:
  has_punctuation = False
  print(char)
  if char in punctuation:
    has_punctuation = True
    
    
print(has_punctuation)
    
