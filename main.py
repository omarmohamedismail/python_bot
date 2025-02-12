from password_generator import generate_password, generate_special_password
from personal_dictonary_assistant import memorize_with_files
from shopping_assistant import calculate_discounts, get_shopping_list




print("hello, I am Jarvis, your personal assistant bot")
print("how can I help you?")
user_name = input("What is your name?")
print("hallo " + user_name + "! I am your personal mathematical assistant bot")
print("how can I help you?")
command = [
      "_i can be your math assistant", "_add_add two numbers",
      "_subtract_subtract two numbers", "_multiply_multiply two numbers",
      "_divide_divide two numbers", "_power_power two numbers",
      "_modelas_modelas two numbers", "_primeter_primeter of rectangle",
      "_primeter2_primeter of square", "_primeter3_primeter of triangle",
      "_i can be your shopping assistant",
      "_(sh)opping_memorize your shopping list",
      "_(dis)count_calculate discounts",
      "_I can memorize (ischool) journey too!",
      "_(gen)rate_generate a password",
      "_(s.gen)generate_generate a special password",
  ]
for commanditem in command:
      print(commanditem)
command = input("what do you need me to do?")
if command == "add":
      print("lets add your numbers")
      num1 = input("please give me number1:=")
      num2 = input("please give me number2:=")
      number1 = int(num1)
      number2 = int(num2)
      res_sum = number1 + number2
      addition_result = str(res_sum)
      print("the result is:=" + addition_result)
elif command == "subtract":
      print("lets subtract your numbers")
      num1 = input("please give me number1:=")
      num2 = input("please give me number2:=")
      number1 = int(num1)
      number2 = int(num2)
      res_sum = number1 - number2
      subtraction_result = str(res_sum)
      print("the result is:=" + subtraction_result)
elif command == "multiply":
      print("lets multiply your numbers")
      num1 = input("please give me number1:=")
      num2 = input("please give me number2:=")
      number1 = int(num1)
      number2 = int(num2)
      res_sum = number1 * number2
      multiply_result = str(res_sum)
      print("the result is:=" + multiply_result)
elif command == "divide":
      print("lets divide your numbers")
      num1 = input("please give me number1:=")
      num2 = input("please give me number2:=")
      number1 = int(num1)
      number2 = int(num2)
      res_sum = number1 / number2
      divide_result = str(res_sum)
      print("the result is:=" + divide_result)
elif command == "power":
      print("lets power your numbers")
      num1 = input("please give me number1:=")
      num2 = input("please give me number2:=")
      number1 = int(num1)
      number2 = int(num2)
      res_sum = number1 ** number2
      power_result = str(res_sum)
      print("the result is:=" + power_result)
elif command == "modelas":
      print("lets power your numbers")
      num1 = input("please give me number1:=")
      num2 = input("please give me number2:=")
      number1 = int(num1)
      number2 = int(num2)
      res_sum = number1 % number2
      modelas_result = str(res_sum)
      print("the result is:=" + modelas_result)
elif command == "primeter":
      print("lets calculate area of reactangle")
      num1 = input("please give me a:=")
      num2 = input("please give me b:=")
      a = int(num1)
      b = int(num2)
      res_primeter = 2 * (a + b)
      primeter_result = str(res_primeter)
      print("the result is:=" + primeter_result)
elif command == "primeter2":
      print("lets calculate area of sqaure")
      num1 = input("please give me a:=")
      a = int(num1)
      res_primeter = 4 * a
      primeter2_result = str(res_primeter)
      print("the result is:=" + primeter2_result)
elif command == "primeter3":
      print("lets calculate area of triangle")
      num1 = input("please give me a:=")
      num2 = input("please give me b:=")
      num3 = input("please give me c:=")
      a = int(num1)
      b = int(num2)
      c = int(num3)
      resprimeter3 = a + b + c
      primeter3_result = str(resprimeter3)
      print("the result is:=" + primeter3_result)
elif command == "shopping":
      get_shopping_list()
elif command == "discount":
      calculate_discounts()
elif command == "memorize":
  memorize_with_files()

elif command=="password":
  password=generate_password(10)
  print("your password is:=" + password)
elif command=="s.password":
  password=generate_special_password()
  print("your special password is:= " + password)
