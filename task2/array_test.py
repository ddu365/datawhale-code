import task2.array as cusArr


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
    except Exception as e:
        print(f'test happen a error:{e}')
