def split_num(number):
    num = [int(i) for i in str(number).zfill(4)]
    return num

a = split_num(23)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
