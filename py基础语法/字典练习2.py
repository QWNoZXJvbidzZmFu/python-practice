favorite_places={'a':111,
                 'b':[222,444],
                 'c':333}
for i in favorite_places.keys():
    print(f"{i}'s favorite place is {favorite_places[i]}")
cities={
    'shanxi':{
        'country':'china',
        'population':100000,
        'fact':111
    },
    'shanghai':{
        'country':'china',
        'population':216416,
        'fact':222
    },
    'hangzhou':{
        'country':'china',
        'population':125412,
        'fact':333
    }
}
for i,j in cities.items():
    print(f"\nname:{i}")
    print(f"所属国家:{j['country']}")
    print(f"人口:{j['population']}")