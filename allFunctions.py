from sympy import symbols, Eq, solve, diff, integrate, limit, Matrix, sympify

# Define symbols
x, y, z = symbols('x y z')

# Quadratic Equation Solver
def solve_quadratic(a, b, c):
    try:
        steps = []
        equation = Eq(a * x**2 + b * x + c, 0)
        steps.append(f"Step 1: The quadratic equation is: {equation}")

        discriminant = b**2 - 4 * a * c
        steps.append(f"Step 2: Compute the discriminant: Δ = b² - 4ac = {b}² - 4*{a}*{c} = {discriminant}")

        if discriminant > 0:
            steps.append("Step 3: The discriminant is positive, so the equation has two real and distinct roots.")
        elif discriminant == 0:
            steps.append("Step 3: The discriminant is zero, so the equation has one real and repeated root.")
        else:
            steps.append("Step 3: The discriminant is negative, so the equation has two complex roots.")

        solutions = solve(equation, x)
        steps.append("Step 4: Solve the equation using the quadratic formula:")
        steps.append("  x = (-b ± √Δ) / 2a")
        for i, sol in enumerate(solutions, start=1):
            steps.append(f"  Root {i}: {sol}")

        return {
            "equation": str(equation),
            "discriminant": discriminant,
            "solutions": [str(sol) for sol in solutions],
            "steps": steps
        }
    except Exception as e:
        return {"error": str(e)}

# Linear Equation Solver
def solve_linear(a, b):
    try:
        steps = []
        equation = Eq(a * x + b, 0)
        steps.append(f"Step 1: The linear equation is: {equation}")

        solution = solve(equation, x)
        steps.append("Step 2: Solve the equation:")
        steps.append(f"  x = -b / a = -({b}) / ({a}) = {solution[0]}")

        return {
            "equation": str(equation),
            "solution": str(solution[0]),
            "steps": steps
        }
    except Exception as e:
        return {"error": str(e)}

# Differentiation
def differentiate(expression, order=1):
    try:
        expr = sympify(expression)
        steps = []
        derivatives = []

        steps.append(f"Step 1: The parsed expression is: {expr}")

        current_expr = expr
        for i in range(1, order + 1):
            derivative = diff(current_expr, x)
            derivatives.append(derivative)
            steps.append(f"Step {i + 1}: Compute the {i} derivative:")
            steps.append(f"  d^{i}({current_expr})/dx^{i} = {derivative}")
            current_expr = derivative

        return {
            "expression": expression,
            "order": order,
            "derivatives": [str(d) for d in derivatives],
            "steps": steps
        }
    except Exception as e:
        return {"error": str(e)}

# Integration
def integrate_expression(expression, lower_limit=None, upper_limit=None):
    try:
        expr = sympify(expression)
        steps = []

        steps.append(f"Step 1: The parsed expression is: {expr}")

        terms = expr.as_ordered_terms()
        steps.append("Step 2: Break the expression into individual terms:")
        for i, term in enumerate(terms, start=1):
            steps.append(f"  Term {i}: {term}")

        integrated_terms = []
        for i, term in enumerate(terms, start=1):
            integral = integrate(term, x)
            integrated_terms.append(integral)
            steps.append(f"Step 3.{i}: Integrate term {i}: ∫{term} dx = {integral}")

        final_integral = sum(integrated_terms)
        steps.append(f"Step 4: Combine the results of all terms: {final_integral}")

        if lower_limit is not None and upper_limit is not None:
            steps.append(f"Step 5: Perform definite integration with limits [{lower_limit}, {upper_limit}]")
            definite_integral = integrate(expr, (x, lower_limit, upper_limit))
            steps.append(f"Step 6: Substitute the limits into the integral:")
            steps.append(f"  Result: {definite_integral}")
            return {
                "expression": expression,
                "type": "definite",
                "integral": str(definite_integral),
                "limits": f"[{lower_limit}, {upper_limit}]",
                "steps": steps
            }
        else:
            steps.append(f"Step 5: The final indefinite integral is: {final_integral} + C")
            return {
                "expression": expression,
                "type": "indefinite",
                "integral": f"{final_integral} + C",
                "steps": steps
            }
    except Exception as e:
        return {"error": str(e)}

# Limit
def compute_limit(expression, point):
    try:
        steps = []
        expr = sympify(expression)
        steps.append(f"Step 1: The parsed expression is: {expr}")

        lim = limit(expr, x, point)
        steps.append(f"Step 2: Compute the limit as x approaches {point}: {lim}")

        return {
            "expression": expression,
            "limit_point": point,
            "limit": str(lim),
            "steps": steps
        }
    except Exception as e:
        return {"error": str(e)}

# Trigonometric Equation Solver
def solve_trigonometric(equation):
    try:
        steps = []  

        lhs, rhs = equation.split('=')
        parsed_eq = Eq(sympify(lhs), sympify(rhs))
        steps.append(f"Step 1: Parse the equation: {parsed_eq}")

        solutions = solve(parsed_eq, x)
        steps.append("Step 2: Solve the equation:")
        for i, sol in enumerate(solutions, start=1):
            steps.append(f"  Solution {i}: {sol}")

        return {
            "equation": str(parsed_eq),
            "solutions": [str(sol) for sol in solutions],
            "steps": steps
        }
    except Exception as e:
        return {"error": str(e)}
    

# Matrix Operations
def matrix_operations(matrix_values, operation):
    try:
        steps = []  
        matrix = Matrix(matrix_values)
        steps.append(f"Step 1: The input matrix is:\n{matrix}")

        if operation == "determinant":
            result = matrix.det()
            steps.append(f"Step 2: Compute the determinant: {result}")
        elif operation == "inverse":
            if matrix.det() != 0:
                result = matrix.inv()
                steps.append(f"Step 2: Compute the inverse:\n{result}")
            else:
                result = "Matrix is singular and cannot be inverted."
                steps.append("Step 2: The matrix is singular, so it has no inverse.")
        elif operation == "transpose":
            result = matrix.T
            steps.append(f"Step 2: Compute the transpose:\n{result}")
        else:
            raise ValueError("Unsupported operation. Choose from determinant, inverse, or transpose.")

        return {
            "matrix": str(matrix),
            "operation": operation,
            "result": str(result),
            "steps": steps
        }
    except Exception as e:
        return {"error": str(e)}