
voters = [(1, "a"), (2, "b"), (3, "c"), (4, "d"), (5, "e")]
for i, j in voters:
    print(j)

countries = ['Pakistan', 'India', 'China', 'Russia', 'USA']
for index, element in zip(range(0, len(countries)), countries):
         print('Index : ', index)
         print(' Element : ', element, '\n')