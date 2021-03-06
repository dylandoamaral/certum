# Certum

A dictionary validation library based on partial, composable and expressive rules.

## Why use it

In case you need to assert some propeties from a particular dictionary in a DSL manner without comparing the entire structure or asserting fields.

Certum comes with the following features:
- Easy to use
- English friendly declaration
- Error accumulation
- Customizable
- Anti KeyError

## Using Certum

```bash
pip install certum
```

:warning: The version is currently in alpha which means that I authorize myself to include breaking changes until I decide that the module is stable.  

## How it works

### Basic usage

Imagine you have a very long json and you want to verify that it contains the following informations:
- He should contains a key named 'name' containing a string.
- He should contains a key named 'entities' being a list containing unique elements.
- He should contains a key named 'nested' containing a key 'value' equals to 4.

```python
from certum import ensure, that

my_obj = {
    "name": "hello",
    "entities": [1, 3, 5],
    "nested": {
        "value": 4
    }
}

validator = ensure(my_obj).respects(
    that("name").is_instance_of(str),
    that("entities").has_unique_elements(),
    that("nested", "value").equals(4)
)

validator.check()
```

### Error handling

If there is errors, certum will accumulate and return errors elegantly:

```python
from certum import ensure, that

my_obj = {
    "name": 2,
    "entities": [1, 3, 3],
    "nested": {
        "value": 2
    }
}

validator = (
    ensure(my_obj)
    .respects(
        that("name").is_instance_of(str),
        that("name").equals("Hello"),
        that("entities").foreach(this.equals(1)),
        that("nested", "value").equals(4),
    )
)

validator.check()

# certum.exception.CertumException: 

# [name] => The value is instance of int, expected str.
# [name] => The value is 2, expected Hello.
# [entities -> 2] => The value is 3, expected 1.
# [entities -> 1] => The value is 3, expected 1.
# [nested -> value] => The value is 2, expected 4.
```

### Strategies

Erros can be sorted, filtered and printed using different strategies.

As an example, you may want to try the GroupedPrinting strategy with the AlphabeticalSorting strategy, this will give you a list of errors like this:

```python
from certum import ensure, that, this
from certum.strategy.printing.grouped import GroupedPrinting
from certum.strategy.sorting.alphabetical import AlphabeticalSorting


my_obj = {
    "name": 2,
    "entities": [1, 3, 3],
    "nested": {
        "value": 2
    }
}

validator = (
    ensure(my_obj)
    .respects(
        that("name").is_instance_of(str),
        that("name").equals("Hello"),
        that("entities").foreach(this.equals(1)),
        that("nested", "value").equals(4),
    )
    .using(GroupedPrinting(), AlphabeticalSorting())
)

validator.check()

# certum.exception.CertumException: 

# entities -> 1   => The value is 3, expected 1.
# entities -> 2   => The value is 3, expected 1.
# name            => The value is 2, expected Hello.
#                    The value is instance of int, expected str.
# nested -> value => The value is 2, expected 4.
```
