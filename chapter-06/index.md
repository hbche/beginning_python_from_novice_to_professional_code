# 第 6 章 抽象

## 6.1 懒惰是一种美德

实现生成含有 10 个元素的斐波那契数列：

```python
# 声明最小阶数的斐波那契数列
fibs = [0, 1]

for i in range(8):
    fibs.append(fibs[-2] + fibs[-1])

print(fibs)
```

如果需要生成指定个数的斐波那契数列呢？

## 6.2 抽象和结构

抽象是程序能够被人理解的关键所在，我们也可以采用抽象的方式组织计算机程序。

以下这个代码就是结构化和抽象的案例，下载网页、统计网页、打印每个词的使用频率

```python
page = download_page()
freqs = compute_frequencies(page)
for word, freq in freqs:
    print(word, freq)
```

## 6.3 自定义函数

使用 def 关键字定义函数，使用冒号定义函数体开始，使用缩进定义函数体，退出缩进标
志着函数定义结束，使用 return 语句返回函数的结果：

```python
# 函数注释
def function_name(args1, args2, ...):
    """说明函数的作用"""

    do_something...
```

动态计算斐波那契数列：

```python
def fibs(num):
    """计算 num 对应的斐波那契数列"""
    results = [0, 1]
    for i in range(num-2):
        results.append(results[-2] + results[-1])
    return results

# 将用户输入的 字符串 转换成数值，否则函数 fibs 内部使用 range 生成列表时将会报错，因为未转换的输入参数默认是字符串类型
num = int(input("Please input number of fibs:"))
print(fibs(num))
```

> 注意：一般而言要判断某个对象是否可调用，可使用 Python 内置的 callable 函数调用
> 检查

检查某个对象是否是函数，是否具有可调用性：

```python
import math

# 测试 math 模块是否具有可调用性
print(callable(math)) # False
# 测试 math 模块下的 sqrt 函数是否有可调用性
print(callable(math.sqrt)) # True
```

### 6.3.1 给函数加文档

我们可以通过注释给函数加文档。放在函数体开头的字符串称为**文档字符串**。

```python
def square(x):
    "Calculates squares of the number x."
    return x * x

# 打印函数文档
print(square.__doc__) # Calculates squares of the number x.
```

> 注意：`__doc__` 是一个属性，其中双下划线表示该属性是一个特殊属性。

内置的 help 函数也很有用：

```python
def square(x):
    "Calculates squares of the number x."
    return x * x

# 内置的 help 函数
print(help(square))

# >>>
# Help on function square in module __main__:

# square(x)
#     Calculates squares of the number x.

# None
```

### 6.3.2 不是函数的函数

数学意义上的函数是根据给定参数返回计算结果。在 Python 中有些函数没有返回值。

## 6.4 参数魔法

### 6.4.1 值从哪里来

函数声明时需要指定形参，函数调用时需要根据声明时的形参传入实参进行调用。即使实参
和形参同名也没关系，形参是只在函数内部作用域有效的临时变量；

### 6.4.2 能修改参数吗

参数不过是变量而已，和我们平时的赋值修改没有什么区别；

```python
def try_to_change(n):
    n = "Mrs. Gumby"

name = "Mr. Gumby"
try_to_change(name)
print(name)
```

与变量赋值类似：

```python
name = "Mr. Gumby"
n = name
n = 'Mrs. Gumby'
print(name)
```

变量 n 变了，变量 name 没有变。

字符串(元组、数值类型)是不可变的。因此函数也没法修改这些。下面给函数传递可变的数
据结构(列表)，我们看看结果：

```python
def try_to_change(n):
    n[0] = 'Mr. Gumby'

name = ['Mrs. Entity', 'Mrs. Thing']
try_to_change(name)
print(name) # ['Mr. Gumby', 'Mrs. Thing']
```

对应的变量赋值逻辑如下：

```python
name = ['Mrs. Entity', 'Mrs. Thing']
n = name
n[0] = 'Mr. Gumby'
print(name) # ['Mr. Gumby', 'Mrs. Thing']
```

显而易见，name[0] 会被修改，因为 name 和 n 指向的是同一个列表。如果我们不希望函
数修改列表数据，我们可以使用切片生成列表的副本，这样就不会修改传入的实参了

```python
def try_to_change(n):
    n[0] = 'Mr. Gumby'

name = ['Mrs. Entity', 'Mrs. Thing']
try_to_change(name[:])
print(name) # ['Mrs. Entity', 'Mrs. Thing']
```

不会修改实参数据。

下面我们编写一个存储用户姓名，并查找用户姓名的程序：

```python
storage = {}
storage['first'] = {}
storage['middle'] = {}
storage['last'] = {}

my_name = 'Magnus Lie Hetland'
my_sister = 'Anne Lie Hetland'

storage['first'].setdefault('Magnus', []).append(my_name)
storage['first'].setdefault('Anne', []).append(my_sister)
storage['middle'].setdefault('Lie', []).append(my_name)
storage['middle'].setdefault('Lie', []).append(my_sister)
storage['last'].setdefault('Hetland', []).append(my_name)
storage['last'].setdefault('Hetland', []).append(my_sister)

print(storage['first']['Magnus'])
print(storage['middle']['Lie'])
```

上述代码没有抽象，我们无法复用，下面我们来完成逻辑抽象

```python
def init_storage():
    """初始化存储结构"""
    storage = {}
    storage['first'] = {}
    storage['middle'] = {}
    storage['last'] = {}
    return storage

def look_name(data, label, name):
    """在存储中查找姓名中指定部分符合指定值的姓名列表"""
    return data[label].get(name)

def add_name(data, full_name):
    """新增姓名存储"""
    names = full_name.split(' ')
    if len(names) == 2:
        names.insert(1, '')
    labels = 'first', 'middle', 'last'
    for label, name in zip(labels, names):
        person = look_name(data, label, name)
        if person:
            person.append(full_name)
        else:
            data[label][name] = [full_name]

my_name = 'Magnus Lie Hetland'
my_sister = 'Anne Lie Hetland'
customer_1 = 'Robin Hood'
customer_2 = 'Robin Locksley'
storage = init_storage()
add_name(storage, my_name)
add_name(storage, my_sister)
add_name(storage, customer_1)
add_name(storage, customer_2)
print(look_name(storage, 'first', 'Anne'))
print(look_name(storage, 'middle', 'Lie'))
print(look_name(storage, 'last', 'Hetland'))
print(look_name(storage, 'first', 'Roin')) # None
print(look_name(storage, 'first', 'Robin'))
```

### 6.4.3 关键字参数和默认值

前面使用的参数都是**位置参数**。接下来有一类参数，不依赖位置进行传参，依赖参数名
称进行传参，这一类参数称为**关键字参数**。

```python
def hello_1(greeting, name):
    return "{}, {}".format(greeting, name)

def hello_2(name, greeting):
    return "{}, {}!".format(name, greeting)

print(hello_1('Hello', 'world'))
print(hello_2('Hello', 'world'))
```

上述两个函数实现的功能一样，唯一的区别是参数声明顺序，如果我们在调用的时候错传了
参数位置，将无法获取预期结果；

```python
print(hello_2('world', 'Hello')) # world, Hello!
```

为了简化调用过程，我们可以指定参数的名称：

```python
# 使用关键字参数给传参指定名称
print(hello_2(name="world", greeting="Hello")) # world, Hello!
```

像这样使用名称指定的参数称为**关键字参数** ，主要优点是有助于澄清各个参数的作用
。

而关键字最大的优点在于可以指定参数的默认值：

```python
def hello_3(greeting='Hello', name='world'):
    return "{}, {}!".format(greeting, name)

print(hello_3()) # Hello, world!
print(hello_3('Greetings')) # Greetings, world!
print(hello_3('Greetings', 'universe')) # Greetings, universe!
```

如果我们需要给指定参数传入值，我们需要指定参数名称

```python
print(hello_3(name="robin")) # Hello, robin!
```

### 6.4.4 收集参数

有时候，允许用户提供任意数量的参数很有用。

例如，如果一次性存储多个用户名：

```python
store_name(data, name1, name2, name3, ...)
```

为此，函数提供了一种参数声明语法，用于收集剩余参数:

```python
def print_params_1(*params):
    print(params)

print_params_1('Testing') # ('Testing',)
print_params_1(1, 2, 3) # (1, 2, 3)
```

参数前面的星号将提供的所有值都放在一个元组中，也就是将这些值收集起来。下面再编写
一种收集参数的使用形式：

```python
def print_params_2(title, *params):
    print(title)
    print(params)

print_params_2('Params', 1, 2, 3)
# Params
# (1, 2, 3)
print_params_2('Params')
# Params
# ()
```

与赋值时一样，带星号的参数也可放在其他位置（而不是最后）​，但不同的是，在这种情
况下你需要做些额外的工作：**使用名称来指定后续参数**。

```python
# 收集参数
def in_the_middle(first, *middle, last):
    print(first, middle, last)

# in_the_middle(1, 2, 3, 4, 5) # TypeError: in_the_middle() missing 1 required keyword-only argument: 'last'
# 最后一个参数必须得使用关键字参数指定，否则会报错
in_the_middle(1, 2, 3, 4, last=5) # 1 (2, 3, 4) 5
```

> 注意：\* 号不会收集关键字参数

要收集关键字参数，可使用**两个星号**。

```python
def print_params_3(**params):
    print(params)

print_params_3(first='Anne', middle="Lie", last="Hetland") # {'first': 'Anne', 'middle': 'Lie', 'last': 'Hetland'}
```

这样得到的是一个**字典**而不是元组。

可结合这三种使用形式：

```python
def print_params_4(x, y, z=3, *position_params, **key_parmas):
    print(x, y, z)
    print(position_params)
    print(key_parmas)

print_params_4(1, 2, 3, 4, 5, 6, 7, foo="boo", bar="bar")

# 1 2 3
# (4, 5, 6, 7)
# {'foo': 'boo', 'bar': 'bar'}
```

以下是使用**收集参数**改写后的案例：

```python
# storage = {}
# storage['first'] = {}
# storage['middle'] = {}
# storage['last'] = {}

# my_name = 'Magnus Lie Hetland'
# my_sister = 'Anne Lie Hetland'

# storage['first'].setdefault('Magnus', []).append(my_name)
# storage['first'].setdefault('Anne', []).append(my_sister)
# storage['middle'].setdefault('Lie', []).append(my_name)
# storage['middle'].setdefault('Lie', []).append(my_sister)
# storage['last'].setdefault('Hetland', []).append(my_name)
# storage['last'].setdefault('Hetland', []).append(my_sister)

# print(storage['first']['Magnus'])
# print(storage['middle']['Lie'])

def init_storage():
    """初始化存储结构"""
    storage = {}
    storage['first'] = {}
    storage['middle'] = {}
    storage['last'] = {}
    return storage

def look_name(data, label, name):
    """在存储中查找姓名中指定部分符合指定值的姓名列表"""
    return data[label].get(name)

def add_name(data, full_name):
    """新增姓名存储"""
    names = full_name.split(' ')
    if len(names) == 2:
        names.insert(1, '')
    labels = 'first', 'middle', 'last'
    for label, name in zip(labels, names):
        person = look_name(data, label, name)
        if person:
            person.append(full_name)
        else:
            data[label][name] = [full_name]

def store_names(data, *names):
    for name in names:
        add_name(data, name)

my_name = 'Magnus Lie Hetland'
my_sister = 'Anne Lie Hetland'
customer_1 = 'Robin Hood'
customer_2 = 'Robin Locksley'
storage = init_storage()
# add_name(storage, my_name)
# add_name(storage, my_sister)
# add_name(storage, customer_1)
# add_name(storage, customer_2)
store_names(my_name, my_sister, customer_1, customer_2)
print(look_name(storage, 'first', 'Anne'))
print(look_name(storage, 'middle', 'Lie'))
print(look_name(storage, 'last', 'Hetland'))
print(look_name(storage, 'first', 'Roin')) # None
print(look_name(storage, 'first', 'Robin'))
```
