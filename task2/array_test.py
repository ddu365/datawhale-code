import task2.array as cusArr
import re




if __name__ == '__main__':
    try:
        a = cusArr.DynamicArray(2)
        a.append(4)
        a.append(5)
        print(a)
        print(len(a))
        print(a.get_capacity())
        # 动态扩容
        a.append(8)
        print(a)
        print(len(a))
        print(a.get_capacity())
        # 改
        a[0] = 9
        print(a)
        print(len(a))
        print(a.get_capacity())
        # 删
        del a[1]
        print(a)
        print(len(a))
        print(a.get_capacity())
        # 读
        print(a[0])

        str = "words and 987"
        a = re.findall(r'^[-+]?\d+', str.strip())  # 正则为：+或-开头出现0或1次，后面为1或多位数字
        print(a)
    except Exception as e:
        print(f'test happen a error:{e}')
