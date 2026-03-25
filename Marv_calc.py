import tkinter

button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["+", "x", "-", "÷", "="]
top_symbols = ["AC", "+/-", "%", "÷"]

row_count = len(button_values)
column_count = len(button_values[0])

color_light_gray = "#D4D4D2"
color_black = "#1c1c1c"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "#FFFFFF"

#window setup
window = tkinter.Tk()
window.title("Calculator")
window.wm_resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Arial", 45), anchor = "e", bg=color_black, fg=color_white, width=column_count)

label.grid(row=0, column=0, columnspan=column_count, sticky="nsew")

for row in range(row_count):
    for column in range(column_count):
        button_value = button_values[row][column]
        if button_value in right_symbols:
            color = color_orange
        elif button_value in top_symbols:
            color = color_light_gray
        else:
            color = color_dark_gray

        if button_value in top_symbols:
            button = tkinter.Button(frame, text=button_value, font=("Arial", 30), bg=color, fg=color_black, command=lambda value=button_value: button_click(value), relief="ridge", bd=3)
        else:
            button = tkinter.Button(frame, text=button_value, font=("Arial", 30), bg=color, fg=color_white, command=lambda value=button_value: button_click(value))
        button.grid(row=row + 1, column=column, sticky="nsew")

frame.pack()

# A+B, A-B, AXB, A/B, A^B, √A, 1/A, A%, AC, +/-, =
A = 0
operator = None
B = None 

def clear_all():
    global A, B, operator
    A = 0
    B = None
    operator = None

def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
        return str(num)
    else:
        return str(num)

def button_click(value):
    global right_symbols, top_symbols, A, B, operator

    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = (label["text"])
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    label["text"] = remove_zero_decimal(numA + numB)
                elif operator == "-":
                    label["text"] = remove_zero_decimal(numA - numB)
                elif operator == "x":
                    label["text"] = remove_zero_decimal(numA * numB)
                elif operator == "÷":
                    label["text"] = remove_zero_decimal(numA / numB)
                    
                clear_all()

        elif value in right_symbols and value != "=":
            if operator is None:
                A = (label["text"])
                label["text"] = "0"
                B = "0"

            operator = value

    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"

        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)
        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)
            
    else:
        if value == "." :
            if value not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value
            else:
                label["text"] += value

# centre the window on the screen
window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (window_width // 2)
y = (window.winfo_screenheight() // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.mainloop()


