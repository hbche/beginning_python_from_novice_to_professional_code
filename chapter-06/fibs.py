# # 声明最小阶数的斐波那契数列
# fibs = [0, 1]

# for i in range(8):
#     fibs.append(fibs[-2] + fibs[-1])
    
# print(fibs)

def fibs(num):
    """计算 num 对应的斐波那契数列"""
    results = [0, 1]
    for i in range(num-2):
        results.append(results[-2] + results[-1])
    return results

# 将用户输入的 字符串 转换成数值，否则函数 fibs 内部使用 range 生成列表时将会报错，因为未转换的输入参数默认是字符串类型
num = int(input("Please input number of fibs:"))
print(fibs(num))