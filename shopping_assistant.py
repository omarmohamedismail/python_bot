shopping = []

def get_shopping_list():
    count = 0
    how_many = int(input("how many items of shopping do you want to add? "))
    for item_number in range(how_many):
        item = input("what is the item number " + str(item_number) + "? ")
        shopping.append(item)
        count = count + 1
    print("here is your list")
    for item in shopping:
        print(item)

def get_item_from_shopping_list(item_number):
    return shopping[item_number]

def calculate_discounts():
    input1 = input("what is the total amount? ")
    amount = int(input1)
    input2 = input("what is the discount amount? ")
    discount_amount = int(input2)
    percentage_after_discount = 100 - discount_amount
    percentage = percentage_after_discount / 100
    result = amount * percentage
    output = str(result)
    print("amount after discount is = " + output + "L.E")
