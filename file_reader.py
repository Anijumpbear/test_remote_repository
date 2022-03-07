# with open('digits_1.txt') as file_object_1:
#     contents = file_object_1.read()
# print(contents)
# print(contents.strip())
# print(1)
# with open(r'C:\pyf\digits_2.txt') as file_object_2:
#     contents_2 = file_object_2.read()
# print(contents_2)
# print(1)


# filename = 'digits_1.txt'
# with open(filename) as file_object:
#     for x in file_object:
#         print(x.rstrip())
# print('-----------------------------------')
# with open(filename) as file_object:
#     lines = file_object.readlines()
#     for line in lines:
#         print(line.rstrip())
# print(lines)
# digit_siring = ''
# for line in lines:
#     digit_siring += line.rstrip()
# print(digit_siring)
# if 'fi' in digit_siring:
#     print('yes')
# else:
#     print('no')


with open('digits_1.txt', 'w') as file_object:
    file_object.write('i love py ^_^\n')
    file_object.write('py love me ^_^\n')
with open('digits_1.txt', 'a') as file_object:
    file_object.write('nonononon\n')
    file_object.write('yesyesyesyesyes')


