# Shopping_Market

## This is a program about the shopping market.

To make this program, here are some points we should figure out:

### 1. How to list the products to choose

​		In fact, there are many ways to list the products to let the user choose one he or she want. Without Web, we can use the **print()** function to make a beautiful panel which just like this:

```python
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

```

​	As you can see, we make a simple but elegant products menu to let user choose. Here is a interesting point we should notice:

```python
products_price = {"pens": 3, "notebook": 10, "desk_light": 25}

products_color = ["black", "green", "yellow", "blue"]
```

​	we use a dictionary to deposit(store) the three products(of cause we can make more) and list their price and use a list to store the colors of these products.



### 2. using  function  package  to  make  code  elegant

​	we all know that using function to package our code can make our program elegant. That is why I using many self-define functions to package my code. In fact, I used self-define functions such as **product_choose()**, **color_choose()**, **post_address()** and **pay_page()**, some of them return value and other return nothing. there is no doubt that using self-define functions we can easily view the code blocks of our program.

### 3. using  global  variables  to  connect  our  functions

​	sometimes we have to use the variable with value of one function in another function, but we don't have method to make it other than using global variables. global variables are useful, they help us connect our self-define functions with each other.  In this program, we should make the **products**, **color** and **money**(you should pay) as global variables because we may use them in more than one functions. details just like this:

```python
global product

def color_choose(products):
	global product
	....
	....
	product = products
```

```python
global color

num = product_choose()

if num == 1:

    color = color_choose("pen")
    .....
```

```python
global address

def post_address():
	address = input("Please input the address...")
	....
	....
	return address
	....
	....
return address
```

```python
global money

def pay_page():
	money = 0
	
	while money < products_price[product]		# in this, the 'product' is 											 # global variable too
	....
	....
```

### 4. another little trick:  time.sleep(sec)

​	another trick is that in this program, I use a little trick to make the program more real (make a time waiting like jumping to another web page), of cause we have to **import time** first. then we can use the time method like this :

```python
import time 
....
....
time.sleep(3)			# wait for 3 seconds 
```


