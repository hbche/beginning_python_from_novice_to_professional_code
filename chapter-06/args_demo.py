# def try_to_change(n):
#     n = "Mrs. Gumby"
    
# name = "Mr. Gumby"
# try_to_change(name)
# print(name)

# name = "Mr. Gumby"
# n = name
# n = 'Mrs. Gumby'
# print(name)

# def try_to_change(n):
#     n[0] = 'Mr. Gumby'
    
# name = ['Mrs. Entity', 'Mrs. Thing']
# try_to_change(name)
# print(name) # ['Mr. Gumby', 'Mrs. Thing']

# name = ['Mrs. Entity', 'Mrs. Thing']
# n = name
# n[0] = 'Mr. Gumby'
# print(name) # ['Mr. Gumby', 'Mrs. Thing']

def try_to_change(n):
    n[0] = 'Mr. Gumby'
    
name = ['Mrs. Entity', 'Mrs. Thing']
try_to_change(name[:])
print(name) # ['Mrs. Entity', 'Mrs. Thing']