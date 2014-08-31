JsonForm
========

Form validation for JSON-like data (i.e. document) in Python.


Introduction
------------

`JsonForm` is mainly based on [jsonschema][1], which is an implementation of [JSON Schema][2] for Python.

Unlike the other validation libraries in Python, `JsonForm` is dedicated to validating JSON-like data, which means it's a document-oriented validation library.


Validation Rules
----------------

All possible validation keywords supported by `JsonForm` is in `JSON Schema` style.

As an example, the `type` keyword is fundamental to JSON Schema. It specifies the data type for a schema. The following table maps from the names of JavaScript types to their analogous types in Python:

JavaScript | Python
---------- | --------------------------------------------------------
string     | string (`unicode` on Python 2.x and `str` on Python 3.x)
number     | int/float
object     | dict
array      | list
boolean    | bool
null       | None

For more keywords, see [JSON Schema Validation][3].


Getting Started
---------------

### Basic example

    from jsonform import JsonForm

    class ProductForm(JsonForm):
        schema = {
            'type': 'object',
            'properties': {
                'name': {'type': 'string'},
                'price': {'type': 'number'},
            },
        }

    >>> # Valid document
    >>> form = ProductForm({'name': 'Eggs', 'price': 34.99})
    >>> if not form.is_valid():
    ...     print(form.errors)
    ...

    >>> # Invalid document
    >>> form = ProductForm({'name': 'Eggs', 'price': 'Invalid'})
    >>> if not form.is_valid():
    ...     print(form.errors)
    ...
    {'price': "'Invalid' is not of type 'number'"}

### Customizing messages

    from jsonform import JsonForm

    class ProductForm(JsonForm):
        schema = {
            'type': 'object',
            'properties': {
                'name': {'type': 'string'},
                'price': {'type': 'number'},
            },
        }
        messages = {
            'properties.price.type': "Hey, it's not ok..."
        }

    >>> form = ProductForm({'name': 'Eggs', 'price': 'Invalid'})
    >>> if not form.is_valid():
    ...     print(form.errors)
    ...
    {'price': "Hey, it's not ok..."}

### Partial validation

    from jsonform import JsonForm

    class ProductForm(JsonForm):
        schema = {
            'type': 'object',
            'properties': {
                'name': {'type': 'string'},
                'price': {'type': 'number'},
            },
            'required': ['name'],
        }

    >>> # Normal validation
    >>> form = ProductForm({'price': 'Invalid'})
    >>> if not form.is_valid():
    ...     print(form.errors)
    ...
    {'price': "'Invalid' is not of type 'number'", 'name': "'name' is a required property"}

    >>> # Partial validation
    >>> form = ProductForm({'price': 'Invalid'}, partial=True)
    >>> if not form.is_valid():
    ...     print(form.errors)
    ...
    {'price': "'Invalid' is not of type 'number'"}

### Customizing validator

    from jsonform import JsonForm

    class ProductForm(JsonForm):
        def validate_name(value):
            if not value.istitle():
                return 'name must be title'

        schema = {
            'type': 'object',
            'properties': {
                'name': {'custom': validate_name}
                'price': {'type': 'number'},
            },
        }

    >>> form = ProductForm({'name': 'eggs', 'price': 34.99})
    >>> if not form.is_valid():
    ...     print(form.errors)
    ...
    {'name': 'name must be title'}


[1]: https://github.com/Julian/jsonschema
[2]: http://json-schema.org
[3]: http://json-schema.org/latest/json-schema-validation.html
