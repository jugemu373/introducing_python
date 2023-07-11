# 8.1
e2f = {
    'dog': 'chien',
    'cat': 'chat',
    'walrus': 'morse'
}
print(e2f)

# 8.2
print(e2f['walrus'])

# 8.3
f2e = {}
for english, french in e2f.items():
    f2e[french] = english
print(f2e)

# 8.4
print(f2e['chien'])

# 8.5
print(set(e2f.keys()))

# 8.6
life = {
    'animals': {
        'cats': [
            'Henri', 'Grumpy', 'Lucy'
        ],
        'octopi': {},
        'emus': {},
    },
    'plants': {},
    'other': {},
}

# 8.7
print(list(life.keys()))

# 8.8
print(life['animals'].keys())

# 8.9
print(life['animals']['cats'])

# 8.10
squares = {key: key * key for key in range(10)}
print(squares)

# 8.11
odd = {number for number in range(10) if number % 2 == 1}
print(odd)

# 8.12
keys = ('optimist', 'pessimist', 'troll')
values = (
    'The glass is half hull',
    'The glass is half empty',
    'How did you get a glass?',
)
print(dict(zip(keys, values)))

# 8.13
titles = [
    'Creature of Habit',
    'Crewel Fate',
    'Sharks On a Plane',
]
plots = [
    'A nun turns into a monster',
    'Check your exits',
]
movies = dict(zip(titles, plots))
print(movies)
