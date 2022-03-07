import name_function as nf
while True:
    first = input()
    if first == 'q':
        break
    last = input()
    if last == 'q':
        break
    f_name = nf.get_formatted_name(first, last)
    print("hello {}".format(f_name))
