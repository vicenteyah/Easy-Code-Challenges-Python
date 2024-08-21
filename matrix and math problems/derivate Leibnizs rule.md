# Compute the Derivative Using Leibniz's Rule

Problem Description:

Given a mathematical function f(x) represented by its coefficients in the form of a polynomial, write a function to compute the derivative of this function using Leibniz's rule.

Leibniz's rule for the derivative of a polynomial function 
𝑓(𝑥) is given by:

$$f'(x) = \frac{d}{dx} (a_n x^n + a_{n-1} x^{n-1} + \cdot \cdot \cdot +a_1x + a_0) $$

### Where
$$f(x) = a_n x^n + a_{n-1} x^{n-1} + \cdot \cdot \cdot +a_1x + a_0 $$
The derivate of 𝑓(𝑥) is:
    $$f'(x) = n \cdot a_n x^{n-1} + (n-1) \cdot a_{n-1} x^{n-2} + \cdot \cdot \cdot + 1 \cdot a_1 $$

You are provided with a polynomial function as a list of integers where each integer represents the coefficient of 𝑥 in decreasing order of powers. The task is to compute and return the derivative of the polynomial.

#### Example 1:
```bash
Input: coefficients = [3, -2, 5, 1]
Output: [9, -4, 5]
Explanation:
The polynomial function is f(x) = 3x^3 - 2x^2 + 5x + 1
The derivative is f'(x) = 9x^2 - 4x + 5
So, the output list of coefficients is [9, -4, 5]
```

#### Example 2:
```bash
Input: coefficients = [4, 0, 2]
Output: [8, 0]
Explanation:
The polynomial function is f(x) = 4x^2 + 2
The derivative is f'(x) = 8x
So, the output list of coefficients is [8, 0]
```

#### Example 3:
```bash
Input: coefficients = [7]
Output: []
Explanation:
The polynomial function is f(x) = 7
The derivative is f'(x) = 0
So, the output list is empty because the derivative is a constant zero polynomial.
```

### Constraints
+ The polynomial will have at most 10 coefficients
+ Coefficients are integers in the range -10^9 to 10^9
+ The polynomial is guaranteed to be of degree at least 0.