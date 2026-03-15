# Build a Polygon Area Calculator

In this project, you will use **object-oriented programming (OOP)** to create a `Rectangle` class and a `Square` class. The `Square` class should be a subclass of `Rectangle` and inherit its methods and attributes.

## 🎯 Objective

Fulfill the user stories below and get all the tests to pass to complete the lab.

---

## 📋 User Stories

### 1. Rectangle Class

You should create a `Rectangle` class.

When a `Rectangle` object is created, it should be initialized with the following attributes:

- `width`
- `height`

The class should contain the following methods:

#### Methods

- **set_width**
  - Sets the width of the rectangle.

- **set_height**
  - Sets the height of the rectangle.

- **get_area**
  - Returns the area of the rectangle.

  ```
  area = width × height
  ```

- **get_perimeter**
  - Returns the perimeter of the rectangle.

  ```
  perimeter = 2(width + height)
  ```

- **get_diagonal**
  - Returns the diagonal of the rectangle.

  ```
  diagonal = √(width² + height²)
  ```

- **get_picture**
  - Returns a string that represents the shape using lines of `*`.
  - The number of lines should equal the **height**.
  - The number of `*` in each line should equal the **width**.
  - Each line should end with a newline `\n`.
  - If the width or height is larger than **50**, return:

  ```
  Too big for picture.
  ```

- **get_amount_inside**
  - Takes another shape (`Square` or `Rectangle`) as an argument.
  - Returns the number of times the passed-in shape can fit inside the current shape **without rotation**.

  Example:
  - A rectangle with width `4` and height `8` can fit **two squares** with side length `4`.

#### String Representation

If a `Rectangle` instance is printed, it should look like:

```
Rectangle(width=5, height=10)
```

---

### 2. Square Class

You should create a `Square` class that **subclasses `Rectangle`**.

When a `Square` object is created:

- It should be initialized with a single **side length**.
- The `__init__` method should store the side length in **both `width` and `height`** attributes inherited from `Rectangle`.

#### Methods

- **set_width**
  - Overrides the `Rectangle` method.
  - Sets **both width and height** to the given value.

- **set_height**
  - Overrides the `Rectangle` method.
  - Sets **both width and height** to the given value.

- **set_side**
  - Sets both **width and height** equal to the side length.

The `Square` class should be able to access all methods from the `Rectangle` class.

#### String Representation

If a `Square` instance is printed, it should look like:

```
Square(side=9)
```

---

## 💻 Usage Example

```python
rect = Rectangle(10, 5)
print(rect.get_area())

rect.set_height(3)
print(rect.get_perimeter())

print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())

sq.set_side(4)
print(sq.get_diagonal())

print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)

print(rect.get_amount_inside(sq))
```

### Expected Output

```
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
```

---

## 🧪 Tests

The following tests must pass:

1. You should have a `Rectangle` class.
2. You should have a `Square` class.
3. The `Square` class should be a subclass of the `Rectangle` class.
4. The `Square` class should be a distinct class from the `Rectangle` class.
5. A square object should be an instance of both the `Square` class and the `Rectangle` class.
6. The string representation of `Rectangle(3, 6)` should be `Rectangle(width=3, height=6)`.
7. The string representation of `Square(5)` should be `Square(side=5)`.
8. `Rectangle(3, 6).get_area()` should return `18`.
9. `Square(5).get_area()` should return `25`.
10. `Rectangle(3, 6).get_perimeter()` should return `18`.
11. `Square(5).get_perimeter()` should return `20`.
12. `Rectangle(3, 6).get_diagonal()` should return `6.708203932499369`.
13. `Square(5).get_diagonal()` should return `7.0710678118654755`.
14. A `Rectangle` instance should update its string representation after setting new values.
15. A `Square` instance should update its string representation after using `.set_side()`.
16. A `Square` instance should update its string representation after using `.set_width()` or `.set_height()`.
17. `.get_picture()` should return the correct visual representation for a `Rectangle`.
18. `.get_picture()` should return the correct visual representation for a `Square`.
19. `.get_picture()` should return `"Too big for picture."` if width or height is greater than `50`.
20. `Rectangle(15,10).get_amount_inside(Square(5))` should return `6`.
21. `Rectangle(4,8).get_amount_inside(Rectangle(3, 6))` should return `1`.
22. `Rectangle(2,3).get_amount_inside(Rectangle(3, 6))` should return `0`.
