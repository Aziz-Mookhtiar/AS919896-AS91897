import tkinter as tk
from tkinter import ttk, messagebox
import random
import json
import os

# file where data will be stored using json text file
data_file = "hired_items.txt"

# Stores hired items data
hired_items = []

# Load data from file if it exists
if os.path.exists(data_file):
    with open(data_file, "r") as file:
        hired_items = json.load(file)

# Save data to file
def save_data():
    with open(data_file, "w") as file:
        json.dump(hired_items, file)

# function to make sure same receipt number is never generated twice
def unique_receipt_number():
    receipt_number = random.randint(1000, 9999)
    if not any(item[0] == receipt_number for item in hired_items):
        return receipt_number

# Get users data from refund or hire form inputs
def input_data():
    first_name = first_name_entry.get().strip().title()
    last_name = last_name_entry.get().strip().title()
    item = item_combobox.get().strip()
    amount = amount_spinbox.get().strip()

    # Check if any field is empty
    if not first_name or not last_name or not item or not amount:
        messagebox.showwarning(title="Error", message="All fields must be completed")
        return

    # check if amount is less than 500 and greater than 1
    try:
        amount = int(amount)
        if amount < 1 or amount > 500:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Warning!", "Please enter a valid input: amount must be less than 500 or more than 1")
        return

    # Validate first name and last name
    if not validate_name(first_name) or not validate_name(last_name):
        return

    # If all inputs are valid, process data, and if so save all data
    receipt_number = unique_receipt_number()
    hired_items.append((receipt_number, first_name, last_name, item, amount))
    save_data()  
    messagebox.showinfo("Info", "Item hired successfully!")
    display_receipt(receipt_number, first_name, last_name, item, amount)

def validate_name(name):
    # Check if the name contains only alphabetical characters
    if not name.replace(' ', '').isalpha():
        messagebox.showwarning("Warning", "Please enter alphabetical characters only in the name(s) field ")
        return False
    return True

# Function to validate input length to 15 characters
def validate_length(new_value):
    if len(new_value) > 15:
        messagebox.showwarning("Warning", "Max Length is 15 characters")
        return False
    return True

# Ask user to confirm quitting the program       
def quit_confirmation():
    quit_window = tk.Toplevel()
    quit_window.title("Quit Confirmation")
    quit_window.configure(bg="#2A6543")

    quit_frame = tk.Frame(quit_window, bg="#2A6543")
    quit_frame.pack()

    confirmation = tk.Label(quit_frame, text="Are you sure you want to quit?", fg='white', bg="#2A6543")
    confirmation.grid(row=0, column=0, columnspan=2, pady=5)

    # yes and no buttons for quitting program
    def quit_close():
        quit_window.destroy()
        main_window.destroy()

    button_styling = {"bg": "#afeeee", "fg": "#52AA5E", "activebackground": "#7fffd4", "activeforeground": "#008b8b",
                      "font": ("Comic Sans MS", 8, "bold")}

    yes_button = tk.Button(quit_frame, text="Yes", command=quit_close, width=5, **button_styling)
    yes_button.grid(row=1, column=0, padx=5, pady=5)

    no_button = tk.Button(quit_frame, text="No", command=quit_window.destroy, width=5, **button_styling)
    no_button.grid(row=1, column=1, padx=5, pady=5)

    for widget in quit_frame.winfo_children():
        widget.grid_configure(padx=2)

# Display all orders made and their details that have been entered
def display_receipt(receipt_number, first_name, last_name, item, amount):
    receipt_window = tk.Toplevel()
    receipt_window.title("Receipt")
    receipt_window.configure(bg='lightgreen')

    receipt_frame = tk.Frame(receipt_window, bg='#2A6543')
    receipt_frame.pack(padx=10, pady=10)

    tk.Label(receipt_frame, text=f"Receipt Number: {receipt_number}", fg='white', bg='#2A6543').pack(pady=2)
    tk.Label(receipt_frame, text=f"First Name: {first_name}", fg='white', bg='#2A6543').pack(pady=2)
    tk.Label(receipt_frame, text=f"Last Name: {last_name}", fg='white', bg='#2A6543').pack(pady=2)
    tk.Label(receipt_frame, text=f"Item Chosen: {item}", fg='white', bg='#2A6543').pack(pady=2)
    tk.Label(receipt_frame, text=f"Amount: {amount}", fg='white', bg='#2A6543').pack(pady=2)

    return_button = tk.Button(receipt_frame, text="Back", command=receipt_window.destroy)
    return_button.pack(pady=5)

# hire window
def hire_window():
    global first_name_entry, last_name_entry, item_combobox, amount_spinbox, gif

    hire_window = tk.Toplevel(main_window)
    hire_window.title("Hire Form")
    hire_window.configure(bg="#2A6543")

    button_styling = {"bg": "#afeeee", "fg": "#52AA5E", "activebackground": "#7fffd4", "activeforeground": "#008b8b",
                      "font": ("Comic Sans MS", 8, "bold")}

    text_styling = {"bg": "#2A6543", "fg": "white", "font": ("Comic San MS", 10, "bold")}

    # Frame for widgets to be put on
    hire_frame = tk.Frame(hire_window)
    hire_frame.pack()

    # Load the GIF image
    gif = tk.PhotoImage(file="hire.png")

    # label frame which has widgets inside
    user_info_frame = tk.LabelFrame(hire_frame, text="Hire Information", padx=20, pady=20, fg="white", bg="#2A6543")
    user_info_frame.grid(row=0, column=0)

    # Create a label to display the GIF
    label = tk.Label(user_info_frame, image=gif)
    label.grid(row=0, column=0, columnspan=2, pady=2)

    
    label_width = 10
    entry_width = 15

    first_name_label = tk.Label(user_info_frame, text="First Name:", width=label_width, **text_styling)
    first_name_label.grid(row=1, column=0, sticky="e")

    # Register validation command for first name
    vcmd_first_name = (main_window.register(validate_length), '%P')
    first_name_entry = tk.Entry(user_info_frame, width=entry_width, validate="key", validatecommand=vcmd_first_name)
    first_name_entry.grid(row=1, column=1, sticky="w")

    last_name_label = tk.Label(user_info_frame, text="Last Name:", width=label_width, **text_styling)
    last_name_label.grid(row=2, column=0, sticky="e")

    # Register validation command for last name
    vcmd_last_name = (main_window.register(validate_length), '%P')
    last_name_entry = tk.Entry(user_info_frame, width=entry_width, validate="key", validatecommand=vcmd_last_name)
    last_name_entry.grid(row=2, column=1, sticky="w")

    item_label = tk.Label(user_info_frame, text="Item Chosen:", width=label_width, **text_styling)
    item_label.grid(row=3, column=0, sticky="e")

    item_combobox = ttk.Combobox(user_info_frame, values=["Chairs", "Tables", "Benches", "Crockery"],
                                 width=entry_width - 2, state='readonly')
    item_combobox.grid(row=3, column=1)

    amount_label = tk.Label(user_info_frame, text="Item Amount:", width=label_width, **text_styling)
    amount_label.grid(row=4, column=0, sticky="e")

    amount_spinbox = tk.Spinbox(user_info_frame, from_=1, to=500, width=entry_width - 2)
    amount_spinbox.grid(row=4, column=1)

    receipt_button = tk.Button(user_info_frame, text="Add To Order", command=input_data, padx=10, width=8,
                               **button_styling)
    receipt_button.grid(row=6, column=0, pady=5)

    back_button = tk.Button(user_info_frame, text="Back", command=hire_window.destroy, padx=10, width=8,
                            **button_styling)
    back_button.grid(row=6, column=1, pady=5)

    for widget in user_info_frame.winfo_children():
        widget.grid_configure(pady=2, padx=2)

# initial display for hired items instantly after items have been hired 
def display_hired_items():
    button_styling = {"bg": "#afeeee", "fg": "#52AA5E", "activebackground": "#7fffd4", "activeforeground": "#008b8b",
                      "font": ("Comic Sans MS", 8, "bold")}

    display_window = tk.Toplevel(main_window)
    display_window.title("Hired Items")
    display_window.configure(bg='#2A6543')
    display_window.geometry("400x300") 

    display_frame = tk.Frame(display_window, bg='#2A6543')
    display_frame.pack(padx=10, pady=10)

    for item in hired_items:
        tk.Label(display_frame,
                 text=f"Receipt Number: {item[0]}, Name: {item[1]} {item[2]}, Item: {item[3]}, Amount: {item[4]}",
                 fg='white', bg='#2A6543', font=("Comic San MS", 8)).pack(pady=2)

    return_button = tk.Button(display_frame, text="Close", command=display_window.destroy, **button_styling)
    return_button.pack(pady=5)

# refund window
def refund_section():
    # get refund inputs if valid
    def save_refund():
        receipt_number = receipt_entry.get().strip()
        first_name = first_name_entry.get().strip().title()
        item_to_refund = item_combobox.get()

        # Validation
        # Check if any field is empty
        if not receipt_number or not first_name or not item_to_refund:
            messagebox.showwarning("Warning", "All fields must be completed")
            return

        # Check if receipt number is a number
        try:
            receipt_number = int(receipt_number)
        except ValueError:
            messagebox.showwarning("Warning", "Receipt Number must be a number")
            return

        # Validate first name
        if not validate_name(first_name):
            return

        # Check if the receipt number, first name and item to refund match
        for item in hired_items:
            if item[0] == receipt_number and item[1] == first_name and item[3] == item_to_refund:
                hired_items.remove(item)
                save_data()  
                messagebox.showinfo("Info", "Item returned successfully!")
                break
        else:
            messagebox.showwarning("Warning", "Item not found!")

    # Refund window
    refund_window = tk.Toplevel(main_window)
    refund_window.title("Return Form")
    refund_window.configure(bg='#2A6543')

    refund_frame = tk.Frame(refund_window)
    refund_frame.pack()

    refund_info_frame = tk.LabelFrame(refund_frame, text="Refund Information", padx=20, pady=20, bg='#2A6543', fg="white", font=("Comic San MS", 12))
    refund_info_frame.grid(row=0, column=0)

    label_width = 10
    entry_width = 15

    text_styling = {"bg": "#2A6543", "fg": "white", "font": ("Comic San MS", 10)}

    receipt_label = tk.Label(refund_info_frame, text="Receipt Number:", width=label_width, **text_styling)
    receipt_label.grid(row=0, column=0, sticky="e")

    receipt_entry = tk.Entry(refund_info_frame, width=entry_width)
    receipt_entry.grid(row=0, column=1)

    first_name_label = tk.Label(refund_info_frame, text="First Name:", width=label_width, **text_styling)
    first_name_label.grid(row=1, column=0)

    first_name_entry = tk.Entry(refund_info_frame, width=entry_width)
    first_name_entry.grid(row=1, column=1)

    item_label = tk.Label(refund_info_frame, text="Item:", width=label_width, **text_styling)
    item_label.grid(row=2, column=0)

    item_combobox = ttk.Combobox(refund_info_frame, values=["Chairs", "Tables", "Benches", "Crockery"],
                                 width=entry_width - 2, state='readonly')
    item_combobox.grid(row=2, column=1)

    button_styling = {"bg": "#afeeee", "fg": "#52AA5E", "activebackground": "#7fffd4", "activeforeground": "#008b8b",
                      "font": ("Comic Sans MS", 8, "bold")}

    save_button = tk.Button(refund_info_frame, text="Process Refund", command=save_refund, padx=10, width=8, **button_styling)
    save_button.grid(row=3, column=0, pady=5)

    display_receipt_button = tk.Button(refund_info_frame, text="Display Hired Items", command=display_hired_items, padx=10, width=15, **button_styling)
    display_receipt_button.grid(row=3, column=1, pady=5)

    back_button = tk.Button(refund_info_frame, text="Back", command=refund_window.destroy, padx=10, width=8, **button_styling)
    back_button.grid(row=4, column=0, pady=5)

    for widget in refund_info_frame.winfo_children():
        widget.grid_configure(pady=2, padx=2)

# Main window
main_window = tk.Tk()
main_window.title("Main Menu")
main_window.geometry("250x200") 
main_window.configure(bg='#2A6543')

button_styling = {"bg": "#afeeee", "fg": "#52AA5E", "activebackground": "#7fffd4", "activeforeground": "#008b8b",
                  "font": ("Comic Sans MS", 8, "bold")}

text_styling = {"bg": "#2A6543", "fg": "white", "font": ("Comic San MS", 12, "bold")}

program_info = tk.Label(main_window, text="Welcome to Julies Party Hire!!", **text_styling)
program_info.pack(pady=10)

hire_button = tk.Button(main_window, text="Hire Item(s)", command=hire_window, **button_styling, width=15)
hire_button.pack(pady=5)

refund_button = tk.Button(main_window, text="Return Item(s)", command=refund_section, **button_styling, width=15)
refund_button.pack(pady=5)

display_button = tk.Button(main_window, text="Display Hired Item(s)", command=display_hired_items, **button_styling, width=15)
display_button.pack(pady=5)

quit_button = tk.Button(main_window, text="Quit", command=quit_confirmation, **button_styling, width=15)
quit_button.pack(pady=5)

main_window.mainloop()
