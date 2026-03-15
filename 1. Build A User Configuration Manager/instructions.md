# Build a User Configuration Manager

In this lab, you will build a **User Configuration Manager** that allows users to manage their settings such as **theme, language, and notifications**.

You will implement functions to **add, update, delete, and view user settings**.

---

## Objective

Fulfill the user stories below and get all the tests to pass to complete the lab.

---

## User Stories

### 1. `add_setting` Function

You should define a function named `add_setting` with **two parameters**:

- A dictionary of settings
- A tuple containing a key-value pair

#### Behavior

The `add_setting` function should:

- Convert the **key and value to lowercase**.
- If the key setting **exists**, return:

```
Setting '[key]' already exists! Cannot add a new setting with this name.
```

- If the key setting **doesn't exist**, add the key-value pair to the dictionary and return:

```
Setting '[key]' added with value '[value]' successfully!
```

> The messages returned should have the **key and value in lowercase**.

---

### 2. `update_setting` Function

You should define a function named `update_setting` with **two parameters**:

- A dictionary of settings
- A tuple containing a key-value pair

#### Behavior

The `update_setting` function should:

- Convert the **key and value to lowercase**.
- If the key setting **exists**, update its value and return:

```
Setting '[key]' updated to '[value]' successfully!
```

- If the key setting **doesn't exist**, return:

```
Setting '[key]' does not exist! Cannot update a non-existing setting.
```

> The messages returned should have the **key and value in lowercase**.

---

### 3. `delete_setting` Function

You should define a function named `delete_setting` with **two parameters**:

- A dictionary of settings
- A key

#### Behavior

The `delete_setting` function should:

- Convert the **key to lowercase**.
- If the key setting **exists**, remove it from the dictionary and return:

```
Setting '[key]' deleted successfully!
```

- If the key setting **does not exist**, return:

```
Setting not found!
```

> The returned message should have the **key in lowercase**.

---

### 4. `view_settings` Function

You should define a function named `view_settings` with **one parameter**:

- A dictionary of settings

#### Behavior

The `view_settings` function should:

- Return the following message if the dictionary is **empty**:

```
No settings available.
```

- If settings exist, return a formatted string displaying them.

The string should start with:

```
Current User Settings:
```

Followed by each key-value pair on a new line with the **key capitalized**.

#### Example

```python
view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'})
```

Expected output:

```
Current User Settings:
Theme: dark
Notifications: enabled
Volume: high
```

---

## Testing Requirement

For testing your code, create a dictionary named:

```
test_settings
```

This dictionary should store **sample user configuration preferences**.

---

## Tests

The following tests must pass:

1. Create a dictionary named `test_settings` and add some values to it.
2. Define a function named `add_setting`.
3. `add_setting` should have two parameters.
4. `add_setting` should convert the key to lowercase.
5. `add_setting` should convert the value to lowercase.
6. `add_setting({'theme': 'light'}, ('THEME', 'dark'))` should return:

```
Setting 'theme' already exists! Cannot add a new setting with this name.
```

7. `add_setting({'theme': 'light'}, ('volume', 'high'))` should return:

```
Setting 'volume' added with value 'high' successfully!
```

8. `add_setting` should correctly add the given key-value pair to the dictionary.

9. Define a function named `update_setting`.
10. `update_setting` should have two parameters.
11. `update_setting` should convert key to lowercase.
12. `update_setting` should convert value to lowercase.

13. `update_setting({'theme': 'light'}, ('theme', 'dark'))` should return:

```
Setting 'theme' updated to 'dark' successfully!
```

14. `update_setting({'theme': 'light'}, ('volume', 'high'))` should return:

```
Setting 'volume' does not exist! Cannot update a non-existing setting.
```

15. `update_setting` should correctly update the given key-value pair.

16. Define a function named `delete_setting`.
17. `delete_setting` should have two parameters.
18. `delete_setting` should convert the key to lowercase.

19. `delete_setting({'theme': 'light'}, 'theme')` should return:

```
Setting 'theme' deleted successfully!
```

20. If the key doesn't exist, return:

```
Setting not found!
```

21. `delete_setting` should correctly remove the key from the dictionary.

22. Define a function named `view_settings`.
23. `view_settings` should have one parameter.

24. `view_settings({})` should return:

```
No settings available.
```

25. `view_settings` should return formatted settings for non-empty dictionaries.
26. `view_settings` should capitalize the first letter of each setting name.
27. `view_settings` should display the correct results and end with a **newline character**.

---

✅ **Goal:** Implement all functions so that **every test passes successfully.**
