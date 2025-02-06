# Split integer

Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start.

Write tests for `split_integer` function that takes 2 positive integers `value`
and `number_of_parts` and returns an array containing exactly `number_of_parts` 
integer elements:

- the difference between the max and min number in the array should be <= 1;
- the array should be sorted ascending (from lowest to highest).

**Please note:** you have to use `pytest` for writing tests.

You don't need to validate arguments (they are always valid).

Examples:
```
split_integer(8, 1) == [8]
split_integer(6, 2) == [3, 3]
split_integer(17, 4) == [4, 4, 4, 5]
split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
```

Notes:
- write tests in the `/app/test_split_integer.py` module;
- their names indicate what exactly they should test.

Run `pytest app/` to check if function pass your tests.

Run `pytest --numprocesses=auto tests/` to check if your tests cover all boundary conditions
and pass task tests.

### Note: Check your code using this [checklist](checklist.md) before pushing your solution.

Напишіть тести для функції `split_integer`, яка приймає 2 додатних цілих числа `value`
і `number_of_parts` і повертає масив, що містить саме `number_of_parts`
цілі елементи:

- різниця між максимальним і мінімальним числом у масиві має бути <= 1;
- масив повинен бути відсортований за зростанням (від найменшого до найвищого).

**Зверніть увагу:** для написання тестів потрібно використовувати `pytest`.

Вам не потрібно перевіряти аргументи (вони завжди дійсні).

приклади:
```
split_integer(8, 1) == [8]
split_integer(6, 2) == [3, 3]
split_integer(17, 4) == [4, 4, 4, 5]
split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
```

Примітки:
- писати тести в модулі `/app/test_split_integer.py`;
- їх імена вказують на те, що саме вони повинні перевірити.

Запустіть `pytest app/`, щоб перевірити, чи функція пройшла ваші тести.

Запустіть `pytest --numprocesses=auto tests/`, щоб перевірити, чи охоплюють ваші тести всі граничні умови
та пройдіть тести завдань.
