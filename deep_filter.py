def iterate(obj):
    if type(obj) == dict:
        return obj.items()
    elif type(obj) == list:
        return enumerate(obj)

def default_filter_function(value):
    return value != None
def deep_filter(obj, filter_func=default_filter_function):
    if type(obj) == dict:
        obj = {key:value for key,value in obj.items() if filter_func(value)}
    elif type(obj) == list:
        obj = [value for value in obj if filter_func(value)]

    for key, value in iterate(obj):
        if type(value) not in [dict, list]:
            continue
        obj[key] = deep_filter(value)
    return obj