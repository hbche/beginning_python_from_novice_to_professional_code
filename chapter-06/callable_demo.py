import math

# 测试 math 模块是否具有可调用性
print(callable(math)) # False
# 测试 math 模块下的 sqrt 函数是否有可调用性
print(callable(math.sqrt)) # True