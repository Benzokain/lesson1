my_citys = {
    'city':'Москва',
    'temperature':20,
    }
print(my_citys['city'])
my_citys['temperature'] -=5
print(my_citys)
##################
print('*'*50)
print('country' in my_citys)
print(my_citys.get('country', 'Россия'))
my_citys['date'] = '27.05.2019'
print(len(my_citys))