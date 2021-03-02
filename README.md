# Certum

A dictionary validation library based on partial, composable and expressive rules.

## Why use it

In case you need to assert some propeties from a particular dictionary in a DSL manner without comparing the entire structure or asserting fields.

Certum comes with the following features:
- Easy to use
- English friendly declaration
- Error accumulation
- Customizable

## Using Certum

You can't use certum package for the moment, coming soon.

## How it works

Imagine you have a very long json and you want to verify that it contains the following informations:
- He should contains a key named 'name' containing a string.
- He should contains a key named 'entities' containing unique elements.
- He should contains a key named 'nested' containing a key 'value' equals to 4.

```python
from certum import ensure, that, this

my_obj = {
    "name": "hello",
    "entities": [1, 2, 3],
    "nested": {
        "value": 4
    }
}

validator = ensure(my_obj).respects(
    this.has_key_type("name", "hello"),
    that("entities").is_list(),
    that("entities").has_unique_elements(),
    that("nested -> value").equals(4)
)

validator.check()
```
