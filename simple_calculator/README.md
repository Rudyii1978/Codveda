# Simple Calculator

A basic calculator application that can perform four primary arithmetic operations: addition, subtraction, multiplication, and division.

## Features

- Addition of two numbers
- Subtraction of two numbers
- Multiplication of two numbers
- Division of two numbers (with zero-division protection)
- Interactive command-line interface
- Error handling for invalid inputs

## Requirements

- Python 3.6 or higher

## Usage

1. Navigate to the simple_calculator directory:
   ```bash
   cd simple_calculator
   ```

2. Run the calculator:
   ```bash
   python calculator.py
   ```

3. Follow the on-screen prompts:
   - Select an operation (1-5)
   - Enter the first number
   - Enter the second number
   - View the result
   - Continue with more calculations or exit (option 5)

## Example

```
========================================
Simple Calculator
========================================

Operations:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exit

----------------------------------------
Select operation (1-5): 1
Enter first number: 10
Enter second number: 5

Result: 10.0 + 5.0 = 15.0
```

## Error Handling

- Division by zero: The calculator will display an error message if you attempt to divide by zero
- Invalid input: Non-numeric inputs will be caught and an error message will be displayed
