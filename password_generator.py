import random

def generate_password(length):
    chars= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    length=input("Enter the length of the password: ")
    length = int(length)
    password = ""
    for c in range (length):
        password += random.choice(chars)
    return password

def generate_special_password():
  small_chars='abcdefghijklmnopqrstuvwxyz'
  capital_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  special_chars='!@#$%^&*()_+'
  digital_chars='123456789'
  print("answer the following questions to generate a password")
  is_there_small_chars=input("Do you want small chars? ): ")
  is_there_capital_chars=input("Do you want capital chars? ): ")
  is_there_special_chars=input("Do you want special chars? ): ")
  is_there_digital_chars=input("Do you want digital chars? ): ")
  length=input("now, Enter the length of the password: ")
  length=int(length)
  password=''
  temporary_chars = ''
  for c in range(length):
      if is_there_small_chars == 'yes':
          temporary_chars += random.choice(small_chars)
      if is_there_capital_chars == 'yes':
          temporary_chars += random.choice(capital_chars)
      if is_there_special_chars == 'yes':
          temporary_chars += random.choice(special_chars)
      if is_there_digital_chars == 'yes':
          temporary_chars += random.choice(digital_chars)
      password += random.choice(temporary_chars)
  return password
