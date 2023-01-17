#8.1
e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
print(e2f)

#8.2
print(e2f['walrus'])

#8.3
f2e = e2f.items()
print(f2e)
for i, j in f2e:
    print('영어 :', i, '프랑스어:', j)

#8.4
print([k for k, v in e2f.items() if v == 'chien'])

#8.5
print(e2f.keys())

#8.6
life = {'animals': {'cats': 'Henri', 'octopi': 'Grumpy', 'emus': 'Lucy'}, 'plants': {}, 'other': {}}
print(life)

#8.7
print(life.keys())

#8.8
print(life['animals'].keys())

#8.9
print(life['animals']['cats'])

#8.10
squares ={i : i**2 for i in range(10)}
print(squares)

#8.11
A_set = {num for num in range(10) if num % 2 == 1}
print(A_set)

#8.12
aa = (a for a in range(10))
for a in aa:
    print('Got', a)

#8.13
a = ('optimist', 'pessmist', 'troll')
b = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')
print(dict(zip(a, b)))

#8.14
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a mon ster', 'A haunted yarn shop']
print(dict(zip(titles, plots)))
