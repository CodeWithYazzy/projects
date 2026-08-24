import tkinter as tk

# Calculator — Yasir Javed Khan
# Run: python calculator-app.py

root = tk.Tk()
root.title("Calculator — Yasir Javed Khan")
root.geometry("320x420")
root.configure(bg="#0f172a")
root.resizable(False, False)

display_var = tk.StringVar(value="0")
entry = tk.Entry(root, textvariable=display_var, font=("Inter", 24), bd=0, bg="#1e293b", fg="white",
                 justify="right", insertbackground="white")
entry.pack(fill="x", padx=12, pady=12, ipady=10)

expression = ""

def update_display(val):
    display_var.set(val if val else "0")

def append(char):
    global expression
    expression += char
    update_display(expression)

def clear():
    global expression
    expression = ""
    update_display("0")

def delete():
    global expression
    expression = expression[:-1]
    update_display(expression)

def calculate():
    global expression
    try:
        # safe eval: replace display symbols
        expr = expression.replace("÷", "/").replace("×", "*").replace("−", "-")
        result = str(eval(expr))
        expression = result
        update_display(result)
    except:
        update_display("Error")
        expression = ""

btn_cfg = {"font": ("Inter", 14, "bold"), "bd": 0, "padx": 0, "pady": 0, "highlightthickness": 0}

frame = tk.Frame(root, bg="#0f172a")
frame.pack(padx=12, pady=8, fill="both", expand=True)

buttons = [
    ("C", clear, "#dc2626", "white"),
    ("⌫", delete, "#334155", "white"),
    ("÷", lambda: append("/"), "#0B3D91", "white"),
    ("×", lambda: append("*"), "#0B3D91", "white"),

    ("7", lambda: append("7"), "#334155", "white"),
    ("8", lambda: append("8"), "#334155", "white"),
    ("9", lambda: append("9"), "#334155", "white"),
    ("−", lambda: append("-"), "#0B3D91", "white"),

    ("4", lambda: append("4"), "#334155", "white"),
    ("5", lambda: append("5"), "#334155", "white"),
    ("6", lambda: append("6"), "#334155", "white"),
    ("+", lambda: append("+"), "#0B3D91", "white"),

    ("1", lambda: append("1"), "#334155", "white"),
    ("2", lambda: append("2"), "#334155", "white"),
    ("3", lambda: append("3"), "#334155", "white"),
    ("", None, "#0f172a", "#0f172a"),  # hidden spacer

    ("0", lambda: append("0"), "#334155", "white"),
    (".", lambda: append("."), "#334155", "white"),
    ("=", calculate, "#16a34a", "white"),
]

# grid with = spanning 2 cols
for i, (text, cmd, bg, fg) in enumerate(buttons):
    if not text:
        continue
    r, c = divmod(i, 4)
    # last row: = spans 2 cols
    if text == "=":
        btn = tk.Button(frame, text=text, command=cmd, bg=bg, fg=fg, **btn_cfg)
        btn.grid(row=4, column=2, columnspan=2, sticky="nsew", padx=4, pady=4, ipady=10)
    elif text == "0":
        btn = tk.Button(frame, text=text, command=cmd, bg=bg, fg=fg, **btn_cfg)
        btn.grid(row=4, column=0, sticky="nsew", padx=4, pady=4, ipady=10)
    elif text == ".":
        btn = tk.Button(frame, text=text, command=cmd, bg=bg, fg=fg, **btn_cfg)
        btn.grid(row=4, column=1, sticky="nsew", padx=4, pady=4, ipady=10)
    else:
        btn = tk.Button(frame, text=text, command=cmd, bg=bg, fg=fg, **btn_cfg)
        btn.grid(row=r, column=c, sticky="nsew", padx=4, pady=4, ipady=10)

for i in range(5):
    frame.grid_rowconfigure(i, weight=1)
for i in range(4):
    frame.grid_columnconfigure(i, weight=1)

root.mainloop()
