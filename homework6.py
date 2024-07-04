my_dict={'Константин': 1981,
         'Вера': 1987,
         'Элина': 2016,
         'Алиса': 2016,}
print(my_dict)
print(my_dict['Вера'])
my_dict['Аня']=2010
print(my_dict)
my_dict.update({'Женя': 1985,
                'Настя': 1985})
print(my_dict)
del my_dict['Настя']
print(my_dict)

my_set={1,1,2,2,3,3,4,5,'external', False, (1,2,3)}
print(my_set)
my_list=[1,1,2,2,3,3,4,5,'external', False, (1,2,3)]
my_list=set(my_list)
print(my_list)
print(my_list.add(type))
print(my_list.add(6))
print(my_list)
print(my_list.discard(1))
print(my_list)