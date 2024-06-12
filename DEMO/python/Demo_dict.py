person = {
    'name': 'Tom',
    'age': 20
}
print(person['name'])
print(person['age'])
print(person.get('sex', '未知'))

person['aa'] = 'bb'
print(person)

for item in person.keys():
    print(item, end=' ')
print()
for item in person.values():
    print(item, end=' ')

for key, value in person.items():
    print(key, ':', value)

person.update({"country": "USA", "age": 27})  # 更新或添加多个键值对
print(person)

squares = {i: i ** 2 for i in range(5)}
print(squares)

squares.clear()
print(len(squares))

print(person)
print('age' in person )
print()

person = {
    'name': 'Tom',
    'age': 20
}
dict2 =dict(person)
print(dict2)
dict2.update({'name': 'jerry'})

print(person)
print(dict2)