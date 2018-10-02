# deep-filter
A simple package that filters out values from dicts/lists, including all dicts/lists nested within it.

# Usage
```python
from deep_filter import deep_filter
x = {
    'nope': 69,
    'yep': [
        69,
        {'maybe': None},
        99
    ]
}
def filter_func:
    return value != 69
result = deep_filter(x, filter_func)
print(result)
# {'yep': [{}, 99]}
```

#### deep_filter(dict_or_list, filter_func=default_filter_func)
- **dict_or_list**: A dictionary or list
- **filter_func**: An optional callback function. It will take a value as an argument, and return `True` if the value will be kept and `False` if not. If omitted, `None` values will be filtered out.

Returns your dict or list, filtered.