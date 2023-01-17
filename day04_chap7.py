#7.1
year_lists = [1999, 2000, 2001, 2002, 2003]

#7.2
print(year_lists[3])

#7.3
print(year_lists[-1])

#7.4
things = ["mozzarella", "cinderella", "salmonella"]

#7.5
#things[1] = "Cinderella" 이렇게도 가능한데 가변성, 출력을 대문자라고 했기 때문에 이건 사용하지 않는다.
things[2] = things[-2].title()
print(things)

#7.6
#things[0] = "MOZZARELLA" #위와 같은이유.. 출력이 되긴 함
things[0] = things[0].upper()
print(things)

#7.7
#things.remove("salmonella") remove 이용 방법
print(f'{things.pop()}')
print(things)

#7.8
surprise = ["Groucho", "Chico", "Harpo"]

#7.9
#surprise[-1] = "Oprah" #위와 같은 사유로 다른 방법 사용!
print(''.join(reversed(surprise[-1].lower())).title())

#7.10
number = [i for i in range(1, 10) if i % 2 == 0]
print(number)

#7.11
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge","call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done")
]
start2 = "someone better"


start3 = [i.title() for i in start1]
for k in start3:
    print(k, end='! ')

rhymes2 = [d[0].title() for d in rhymes]
for k in rhymes2:
    print(k, end='!')


print('\n',start2, end=' ')

rhymes2 = [d[1].title() for d in rhymes]
for k in rhymes2:
    print(k, end='.')
