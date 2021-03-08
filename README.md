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

You can't use certum package for the moment, coming soon.

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
    that("nested -> value").equals(4)
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

validator = ensure(my_obj).respects(
    that("name").is_instance_of(str),
    that("entities").has_unique_elements(),
    that("nested -> value").equals(4)
)

validator.check()

# certum.exception.CertumException: 

# [name] => The key is not instance of str but int.
# [nested -> value] => 4 is not equal to 2.
# [entities] => The row 1 and 2 are the same.
```

### Strategies

Erros can be sorted, filtered and printed using different strategies.

As an example, you may want to try the GroupedPrinting strategy with the AlphanumericalSorting strategy, this will give you a list of errors like this:

```python
from certum import ensure, that, this
from certum.strategy.printing.grouped import GroupedPrinting
from certum.strategy.sorting.alphanumerical import AlphanumericalSorting


my_obj = {"name": 2, "entities": [1, 3, 3], "nested": {"value": 2}}

validator = (
    ensure(my_obj)
    .respects(
        that("name").is_instance_of(str),
        that("name").equals("Hello"),
        that("entities").foreach(this.equals(1)),
        that("nested -> value").equals(4),
    )
    .using(GroupedPrinting(), AlphanumericalSorting())
)

validator.check()

# certum.exception.CertumException: 

# entities -> 1   => 1 is not equal to 3.
# entities -> 2   => 1 is not equal to 3.
# name            => Hello is not equal to 2.
#                    The key is not instance of str but int.
# nested -> value => 4 is not equal to 2.
```
