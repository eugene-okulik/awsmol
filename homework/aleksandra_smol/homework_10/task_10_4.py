# PRICE_LIST = '''тетрадь 50р
# книга 200р
# ручка 100р
# карандаш 70р
# альбом 120р
# пенал 300р
# рюкзак 500р'''
#
# our_dict = {}
# items = PRICE_LIST.split('\n')
# print(items)
#
# for i in items:
#     name = i.split()[0]
#     print(name)
#     price = i.split()[-1][:-1]
#     print(price)
#     our_dict[name] = int(price)
# print(our_dict)


PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

our_dict = {i.split()[0]: int(i.split()[-1][:-1]) for i in PRICE_LIST.split('\n')}
print(our_dict)
