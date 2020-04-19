<<<<<<< HEAD
my_str = input("Введите несколько слов, разделенных пробелами- ").split()
str_num = 1
for i in my_str:
    if int(len(i)) <= 0:
        print(f"{str_num}) {i}")
        str_num += 1
    else:
        print(f"{str_num}) {i[0:9]}")
=======
my_str = input("Введите несколько слов, разделенных пробелами- ").split()
str_num = 1
for i in my_str:
    if int(len(i)) <= 0:
        print(f"{str_num}) {i}")
        str_num += 1
    else:
        print(f"{str_num}) {i[0:9]}")
>>>>>>> c95485a9c8f536e77837f9d33cb6345f40ae5bd1
        str_num += 1