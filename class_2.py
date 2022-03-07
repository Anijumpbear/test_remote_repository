import math
print('q to quit')
while True:
    z = input('z = ')
    if z == 'q':
        break
    else:
        z = int(z)
        sigmoid_z = 1/(1+math.exp(-z))
        print('sigmoid(z) = {}'.format(sigmoid_z))
