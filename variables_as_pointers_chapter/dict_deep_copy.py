def is_iterable(element):
    if isinstance(element, list):
        return "list"
    elif isinstance(element, tuple):
        return "tuple"
    else:
        return False

def nest_loop(item, kind):
    if not kind:
        return item
    nested_iterable = []
    
    for element in item:
        element_kind = is_iterable(element)
        if element_kind:
            nested_iterable.append(nest_loop(element, element_kind))
        else:
            nested_iterable.append(element)
    
    if kind == "list":
        return nested_iterable
    elif kind == "tuple":
        return tuple(nested_iterable)

def dict_deep_copy(original_dict):
    keys_and_values = list(original_dict.items())
    return { key: nest_loop(value, is_iterable(value))
        for (key, value) in keys_and_values }

dict1 = {
    'a': [[7, 1], ['aa', 'aaa']],
    'b': ([3, 2], ['bb', 'bbb']),
}

dict2 = dict_deep_copy(dict1)

print(dict1)
print(dict2)
print(dict1         is dict2)
print(dict1['a']    is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])
print(dict1['a'][0][0] is dict2['a'][0][0])
print(dict1['a'][0][1] is dict2['a'][0][1])
print(dict1['a'][1][0] is dict2['a'][1][0])
print(dict1['a'][1][1] is dict2['a'][1][1])
print(dict1['b'][0][0] is dict2['b'][0][0])
print(dict1['b'][0][1] is dict2['b'][0][1])
print(dict1['b'][1][0] is dict2['b'][1][0])
print(dict1['b'][1][1] is dict2['b'][1][1])