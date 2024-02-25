my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

my_dict = { name: len(name) for name in my_set if len(name) % 2 != 0 }
print(my_dict)