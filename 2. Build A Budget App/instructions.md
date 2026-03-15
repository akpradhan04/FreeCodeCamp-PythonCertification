# Build a Budget App

In this lab, you will build a simple budget app that tracks spending in different categories and can show the relative spending percentage on a graph.

## Objective
Fulfill the user stories below and get all the tests to pass to complete the lab.

---

## User Stories

You should have a `Category` class that accepts a name as the argument.

The `Category` class should have an instance attribute `ledger` that is a list, and contains the list of transactions.

### The Category class should have the following methods:

**deposit method**
- Accepts an amount and an optional description.
- If no description is given, it should default to an empty string.
- The method should append an object to the ledger list in the form:  
`{'amount': amount, 'description': description}`

**withdraw method**
- Accepts an amount and an optional description (default to an empty string).
- The method should store the amount passed in as a negative number in the ledger.
- Should return `True` if the withdrawal succeeded and `False` otherwise.

**get_balance method**
- Returns the current category balance based on the ledger.

**transfer method**
- Accepts an amount and another Category instance.
- Withdraws the amount with description `Transfer to [Destination]`.
- Deposits it into the other category with description `Transfer from [Source]`.
- `[Destination]` and `[Source]` should be replaced with the names of the categories.
- Should return `True` when the transfer is successful and `False` otherwise.

**check_funds method**
- Accepts an amount.
- Returns `False` if the amount exceeds the current balance.
- Returns `True` otherwise.
- This method must be used by both the `withdraw` and `transfer` methods.

---

## Printing the Category Object

When a Category object is printed, it should:

1. Display a title line of **30 characters** with the category name centered between `*` characters.
2. List each ledger entry with:
   - Description left-aligned (maximum **23 characters**)
   - Amount right-aligned (**two decimal places**, maximum **7 characters**)
3. Show a final line:

`Total: [balance]`

Where `[balance]` is the category total.

---

## Example Usage

    food = Category('Food')
    food.deposit(1000, 'initial deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')

    clothing = Category('Clothing')
    food.transfer(50, clothing)

    print(food)

### Example Output

    *************Food*************
    initial deposit        1000.00
    groceries               -10.15
    restaurant and more foo -15.89
    Transfer to Clothing    -50.00
    Total: 923.96

---

## Spend Chart Function

You should create a function outside the Category class named:

`create_spend_chart(categories)`

This function should return a **bar-chart string**.

### Chart Requirements

1. Start with the title:  
   `Percentage spent by category`

2. Calculate percentages from **withdrawals only**, not deposits.

3. The percentage should represent:  
   `(amount spent in category / total spent in all categories)`

4. Percentages should be **rounded down to the nearest 10**.

5. Label the **y-axis from 100 down to 0** in steps of 10.

6. Use `o` characters for the bars.

7. Include a **horizontal line** two spaces past the last bar.

8. Write **category names vertically below the bars**.

9. This function will be tested with **up to four categories**.

---

## Example Chart Output

    Percentage spent by category
    100|          
     90|          
     80|          
     70|          
     60| o        
     50| o        
     40| o        
     30| o        
     20| o  o     
     10| o  o  o  
      0| o  o  o  
        ----------
         F  C  A  
         o  l  u  
         o  o  t  
         d  t  o  
            h     
            i     
            n     
            g     

---

## Note
Open the browser console with **F12** to see a more verbose output of the tests.

---

## Tests

1. The deposit method should create a specific object in the ledger instance variable.
2. Calling the deposit method with no description should create a blank description.
3. The withdraw method should create a specific object in the ledger instance variable.
4. Calling the withdraw method with no description should create a blank description.
5. The withdraw method should return True if the withdrawal took place.
6. Calling `food.deposit(900, 'deposit')` and `food.withdraw(45.67, 'milk, cereal, eggs, bacon, bread')` should return a balance of `854.33`.
7. Calling the transfer method on a category object should create a specific ledger item in that category object.
8. The transfer method should return True if the transfer took place.
9. Calling transfer on a category object should reduce the balance in the category object.
10. The transfer method should increase the balance of the category object passed as its argument.
11. The transfer method should create a specific ledger item in the category object passed as its argument.
12. The check_funds method should return False if the amount passed to the method is greater than the category balance.
13. The check_funds method should return True if the amount passed to the method is not greater than the category balance.
14. The withdraw method should return False if the withdrawal didn't take place.
15. The transfer method should return False if the transfer didn't take place.
16. Printing a Category instance should give a different string representation of the object.
17. Title at the top of create_spend_chart chart should say `Percentage spent by category`.
18. create_spend_chart chart should have correct percentages down the left side.
19. The height of each bar on the create_spend_chart chart should be rounded down to the nearest 10.
20. Each line in create_spend_chart chart should have the same length. Bars should be separated by two spaces, with two additional spaces after the final bar.
21. create_spend_chart should correctly show a horizontal line below the bars using three `-` characters per category and extending two characters past the final bar.
22. create_spend_chart chart should not have a newline character at the end.
23. create_spend_chart chart should have each category name written vertically below the bar with consistent spacing.
24. create_spend_chart should print a different chart representation with exact spacing.
