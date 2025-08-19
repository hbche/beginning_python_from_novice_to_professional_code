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