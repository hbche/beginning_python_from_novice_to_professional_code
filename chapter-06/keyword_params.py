# def hello_1(greeting, name):
#     return "{}, {}".format(greeting, name)

# def hello_2(name, greeting):
#     return "{}, {}!".format(name, greeting)

# print(hello_1('Hello', 'world'))
# print(hello_2('Hello', 'world'))

# print(hello_2('world', 'Hello'))

# # 使用关键字参数给传参指定名称
# print(hello_2(name="world", greeting="Hello")) # world, Hello!

# def hello_3(greeting='Hello', name='world'):
#     return "{}, {}!".format(greeting, name)

# print(hello_3()) # Hello, world!
# print(hello_3('Greetings')) # Greetings, world!
# print(hello_3('Greetings', 'universe')) # Greetings, universe!
# print(hello_3(name="robin")) # Hello, robin!

# # 收集参数
# def in_the_middle(first, *middle, last):
#     print(first, middle, last)
    
# # in_the_middle(1, 2, 3, 4, 5) # TypeError: in_the_middle() missing 1 required keyword-only argument: 'last'
# # 最后一个参数必须得使用关键字参数指定，否则会报错
# in_the_middle(1, 2, 3, 4, last=5) # 1 (2, 3, 4) 5

# def print_params_1(*params):
#     print(params)

# print_params_1('Testing') # ('Testing',)
# print_params_1(1, 2, 3) # (1, 2, 3)

# def print_params_2(title, *params):
#     print(title)
#     print(params)
    
# print_params_2('Params', 1, 2, 3)
# # Params
# # (1, 2, 3)
# print_params_2('Params')
# # Params
# # ()
# print_params_2('Params', something=(1, 2, 3))
# # Traceback (most recent call last):
# #   File "F:\beginning_python_from_novice_to_professional_code\chapter-06\keyword_params.py", line 41, in <module>
# #     print_params_2('Params', something=(1, 2, 3))
# #     ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# # TypeError: print_params_2() got an unexpected keyword argument 'something'

# def print_params_3(**params):
#     print(params)
    
# print_params_3(first='Anne', middle="Lie", last="Hetland") # {'first': 'Anne', 'middle': 'Lie', 'last': 'Hetland'}

def print_params_4(x, y, z=3, *position_params, **key_parmas):
    print(x, y, z)
    print(position_params)
    print(key_parmas)

print_params_4(1, 2, 3, 4, 5, 6, 7, foo="boo", bar="bar")

# 1 2 3
# (4, 5, 6, 7)
# {'foo': 'boo', 'bar': 'bar'}