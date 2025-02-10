# Check Your Code Against the Following Points

## Code Style

1. Don't create unnecessary variables for simple tests:

Good example:

```python
def test_():
    assert some_function_to_test() == [10]
```

Bad example:

```python
def test_():
    result_of_testing_function = some_function_to_test()
    assert result_of_testing_function == [10]
```

2. Make sure that you compare the result of function and expected result in `assert` statement.

## Clean Code

Add comments, prints, and functions to check your solution when you write your code. 
Don't forget to delete them when you are ready to commit and push your code.
