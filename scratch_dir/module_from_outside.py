import class_related.lawn as cl

my_lawn = cl.Lawn(my_width=20, my_length=40)
print(f'my lawn"s width is: {my_lawn.width}')
print(f'my lawn"s length is: {my_lawn.length}')
print(f'This is the width of my_lawn: {my_lawn.get_lawn_width()}')
print(f'This is the length of my_lawn: {my_lawn.get_lawn_length()}')


