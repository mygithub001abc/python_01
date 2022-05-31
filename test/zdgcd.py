# 最大公约数
def gcd(num1, num2):
    # 让num2为较小数
    if num1 < num2:
        num1, num2 = num2, num1
    while num2 != 0:
        temp = num1 % num2
        num1, num2 = num2, temp
    return num1