from pathlib import Path
path = Path(__file__)
print(path)


# def over_age(data, getter):
#     return getter(data) >= 18
#
#
# user = {'username': 'rolf123', 'age': '35'}
#
# print(over_age(user, lambda x: int(x['age'])))