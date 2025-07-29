import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, scrolledtext
import allFunctions as af  

history = []  # To store all results

def quadratic_solver():
    try:
        a = float(simpledialog.askstring("Input", "Enter coefficient a:"))
        b = float(simpledialog.askstring("Input", "Enter coefficient b:"))
        c = float(simpledialog.askstring("Input", "Enter coefficient c:"))
        result = af.solve_quadratic(a, b, c)
        display_result(result)
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def linear_solver():
    try:
        a = float(simpledialog.askstring("Input", "Enter coefficient a:"))
        b = float(simpledialog.askstring("Input", "Enter coefficient b:"))
        result = af.solve_linear(a, b)
        display_result(result)
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def differentiation():
    try:
        expr = simpledialog.askstring("Input", "Enter the expression to differentiate:")
        order = int(simpledialog.askstring("Input", "Enter the order of the derivative:"))
        result = af.differentiate(expr, order)
        display_result(result)
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def integration():
    try:
        expr = simpledialog.askstring("Input", "Enter the expression to integrate:")
        limits = simpledialog.askstring("Input", "Enter lower and upper limits (or leave blank for indefinite):")
        if limits:
            lower, upper = map(float, limits.split())
            result = af.integrate_expression(expr, lower, upper)
        else:
            result = af.integrate_expression(expr)
        display_result(result)
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def limit_calculation():
    try:
        expr = simpledialog.askstring("Input", "Enter the expression:")
        point = float(simpledialog.askstring("Input", "Enter the point to compute the limit at:"))
        result = af.compute_limit(expr, point)
        display_result(result)
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def trigonometric_solver():
    try:
        equation = simpledialog.askstring("Input", "Enter the trigonometric equation (e.g., sin(x) = 0):")
        result = af.solve_trigonometric(equation)
        display_result(result)
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def matrix_operations():
    try:
        rows = int(simpledialog.askstring("Input", "Enter the number of rows:"))
        matrix_values = []
        for i in range(rows):
            row = list(map(float, simpledialog.askstring("Input", f"Enter row {i+1} (space-separated):").split()))
            matrix_values.append(row)
        operation = simpledialog.askstring("Input", "Choose operation (determinant, inverse, transpose):").strip().lower()
        result = af.matrix_operations(matrix_values, operation)
        display_result(result)
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def display_result(result):
    if "error" in result:
        messagebox.showerror("Error", result["error"])
        return

    steps = "\n".join(result.get("steps", []))
    final_result = result.get("solutions") or result.get("solution") or result.get("integral") or result.get("limit") or result.get("result")
    if isinstance(final_result, list):
        final_result = "\n".join(str(x) for x in final_result)
    output_text = f"Steps:\n{steps}\n\nResult:\n{final_result}"


    history.append(output_text)


    output_win = Toplevel(root)
    output_win.title("Result")
    output_box = scrolledtext.ScrolledText(output_win, width=100, height=20)
    output_box.pack(padx=10, pady=10)
    output_box.insert(tk.END, output_text)
    output_box.config(state=tk.DISABLED)

    def save_to_file():
        with open("math_solver_history.txt", "a") as f:
            f.write(output_text + "\n" + "="*40 + "\n")
        messagebox.showinfo("Saved", "Result saved to math_solver_history.txt")

    def show_history():
        history_win = Toplevel(root)
        history_win.title("History")
        hist_box = scrolledtext.ScrolledText(history_win, width=100, height=20)
        hist_box.pack(padx=10, pady=10)
        try:
            with open("math_solver_history.txt", "r") as f:
                hist_content = f.read()
            if not hist_content.strip():
                hist_content = "No history found."
        except FileNotFoundError:
            hist_content = "No history found."
        hist_box.insert(tk.END, hist_content)
        hist_box.config(state=tk.DISABLED)

    btn_frame = tk.Frame(output_win)
    btn_frame.pack(pady=5)
    tk.Button(btn_frame, text="Save", command=save_to_file, width=50).pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame, text="Show History", command=show_history, width=50).pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame, text="Close", command=output_win.destroy, width=50).pack(side=tk.LEFT, padx=5)

# Main GUI
root = tk.Tk()
root.title("Math Solver")

tk.Button(root, text="1. Quadratic Equation Solver", command=quadratic_solver, width=250).pack(pady=6)
tk.Button(root, text="2. Linear Equation Solver", command=linear_solver, width=250).pack(pady=6)
tk.Button(root, text="3. Differentiation", command=differentiation, width=250).pack(pady=6)
tk.Button(root, text="4. Integration", command=integration, width=250).pack(pady=6)
tk.Button(root, text="5. Limit Calculation", command=limit_calculation, width=250).pack(pady=6)
tk.Button(root, text="6. Trigonometric Equation Solver", command=trigonometric_solver, width=250).pack(pady=6)
tk.Button(root, text="7. Matrix Operations", command=matrix_operations, width=250).pack(pady=6)
tk.Button(root, text="Exit", command=root.quit, width=250).pack(pady=6)

root.mainloop()

