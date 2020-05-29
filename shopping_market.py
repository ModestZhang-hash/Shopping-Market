import time

print("shopping Market\n")
print("*******************************")
print("Welcome to the shopping Market!\n")

products_price = {"pens": 3, "notebook": 10, "desk_light": 25}

products_color = ["black", "green", "yellow", "blue"]

print("Here are the products in the shopping market:\n"
      "1. pen\n"
      "2. notebook\n"
      "3. desk_light\n")
print("*******************************")
'''
product_choose = input("Please input the product you choose: ")


if product_choose == "1":
    print("you choose a pen.")
    
elif product_choose == "2":
    print("you choose a notebook.")

elif product_choose == "3":
    print("you choose a desk_light.")
'''


def product_choose():
    n = input("please input the product you choose: ")
    if n == "1":
        print(f"you choose a pen, it costs {products_price['pens']} dollars.")
        return 1

    elif n == "2":
        print(f"you choose a notebook, it costs {products_price['notebook']} dollars.")
        return 2

    elif n == "3":
        print(f"you choose a desk_light, it costs {products_price['desk_light']} dollars.")
        return 3

    return

global product

def color_choose(products):

    global product

    color = input(f"Please input the color of {products} you want: \n"
                  f"1.black\n"
                  f"2.green\n"
                  f"3.yellow\n"
                  f"4.blue\n")

    if color == '1':

        print(f"You choose the {products} with color {products_color[0]}.")
        color = products_color[0]
        product = products

    elif color == '2':

        print(f"You choose the {products} with color {products_color[1]}.")
        color = products_color[1]
        product = products

    elif color == '3':

        print(f"You choose the {products} with color {products_color[2]}.")
        color = products_color[2]
        product = products

    elif color == '4':

        print(f"You choose the {products} with color {products_color[3]}.")
        color = products_color[3]
        product = products

    return color


'''
def choose_pen():

    color = input("Please input the color of pen you want: \n"
                  "1. black\n"
                  "2. green\n"
                  "3. yellow\n"
                  "4. blue\n")

    if color == '1':

        print(f"You choose the {pens_color[0]} pen.")

    elif color == '2':

        print(f"You choose the {pens_color[1]} pen.")

    elif color == '3':

        print(f"You choose the {pens_color[2]} pen.")

    elif color == '4':

        print(f"You choose the {pens_color[3]} pen.")

    return


def choose_notebook():

    color = input("Please input the color of notebook you want: \n"
                  "1. black"
                  "2. green"
                  "3. yellow"
                  "4. blue")

    if color == '1':

        print(f"You choose the {notebook_color[0]} notebook.")

    elif color == '2':

        print(f"You choose the {notebook_color[1]} notebook.")

    elif color == '3':

        print(f"You choose the {notebook_color[2]} notebook.")

    elif color == '4':

        print(f"You choose the {notebook_color[3]} notebook.")

    return
..........
..........
..........(too long and Duplicated code fragment[重复代码段])
'''

global color

num = product_choose()

if num == 1:

    color = color_choose("pen")

elif num == 2:

    color = color_choose("notebook")

elif num == 3:

    color = color_choose("desk_light")


print("You have chosen the product and its color you want, wait jumping to the pay page....")

time.sleep(3)

print("the details of the order form:\n")

print(f"You have chosen the {product} with color {color}, it costs {products_price[product]} dollars.\n")

global address

def post_address():

    address = input("Please input the address where we will post your product to: ")

    judge = input(f"check it, your address is {address}, is it? Y/N")

    if judge.upper() == "Y":
        return address

    elif judge.upper() == "N":
        post_address()

    return address



post_address = post_address()


global money

def pay_page():

    money = 0

    print(f"You have chosen the {product} with color {color}, it costs {products_price[product]} dollars.\n")
    print(f"the address you want to post product to is {post_address}.\n")

    print("Now pay it: \n")



    while money < products_price[product]:

        print("Your money is not enough to pay for your product you want.")

        if_charge = input("Are you want to recharge your money? Y/N")

        if if_charge.upper() == "Y":

            print("You choose to charge your money.\n")

            charge = eval(input("Please input the money you want to charge: "))

            code = '0'

            while code == '0':

                code = input("Please input your pay code: ")

                if code == "5292":

                    money += charge
                    print("you charge successfully.\n")
                    break

                else:
                    print("Your input pay code is wrong! charge failed.")
                    continue

        elif if_charge.upper() == "N":

            print("because you want to charge money, you can't buy the product you want.\n")
            print("Wait for exit the pay page....")

            time.sleep(3)

            return




    if_pay = input("Are you sure to pay for product you want? Y/N")

    if if_pay.upper() == "Y":

        money -= products_price[product]

        print(f"You pay for product you want successfully, current money you have is {money}.\n")

    elif if_pay.upper() == "N":

        print(f"You choose not to pay for product you want, current money you have is {money}.\n")
        print("Wait for exit pay page....")

        time.sleep(3)

        return

    print(f"now check the order form:\n"
          f"product: {product}\n"
          f"product color: {color}\n"
          f"product_price: {products_price[product]}\n"
          f"address: {post_address}\n")

    print("trade successfully, wait to exit pay page.....")

    time.sleep(5)

    return

pay_page()



























