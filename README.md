# deep-filter
A simple package that filters out values from dicts/lists, including all dicts/lists nested within it.

## Usage
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

### deep_filter(dict_or_list, filter_func=default_filter_func)
- **dict_or_list**: A dictionary or list
- **filter_func**: An optional callback function. It will take a value as an argument, and return `True` if the value will be kept and `False` if not. If omitted, `None` values will be filtered out.

Returns your dict or list, filtered.

## Dev instructions

### Get started

1. Install Python (Python 3.7 works, probably other versions too)
2. Install [Poetry](https://poetry.eustace.io). Poetry is used to manage dependencies, the virtual environment and publishing to PyPI
3. Run `poetry install` to install Python package dependencies

I recommend running `poetry config virtualenvs.in-project true`, which makes Poetry store your Python virtual environment inside the project folder. Additionally, it lets VSCode's Python extension detect the virtual environment if you set the `python.pythonPath` setting to `${workspaceFolder}/.venv/bin/python` in your settings.

### Running

To test if things work, you can run the following command to open the Python REPL. Then you can write Python, such as the usage examples:

```
poetry run python
```

### Releasing a new version

1. Consider updating the lockfile by running `poetry update`, then check if thing still work
2. Bump the version number:
    ```
    poetry version <version>
    ```
3. Update `CHANGELOG.md`
4. Build:
    ```
    poetry build
    ```
5. Commit and create git tag
6. Create GitHub release with release notes and attach the build files
7. Publish to PyPi:
    ```
    poetry publish
    ```
