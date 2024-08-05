import tkinter as tk
from tkinter import ttk, messagebox
import random

# Stores data
hired_items = []

def input_data():
    first_name = first_name_entry.get().strip()
    last_name = last_name_entry.get().strip()
    item = item_combobox.get()
    amount = amount_spinbox.get()

    # Validate first name and last name
    if not validate_name(first_name) or not validate_name(last_name):
        return

    if first_name and last_name and item and amount:
        receipt_number = random.randint(1000, 9999)

        hired_items.append((receipt_number, first_name, last_name, item, amount))
        messagebox.showinfo("Info", "Item hired successfully!")

        display_receipt(receipt_number, first_name, last_name, item, amount)
    else:
        messagebox.showwarning(title="Error", message="All fields must be completed")

def validate_name(name):
    # Check if the name contains only alphabetical characters
    if not name.replace(' ', '').isalpha():
        messagebox.showwarning("Warning", "Please enter alphabetical characters only")
        return False
    return True

def quit_confirmation():
    quit_window = tk.Toplevel()
    quit_window.title("Quit Confirmation")

    quit_frame = tk.Frame(quit_window, bg='#2A6543')  # Corrected color code
    quit_frame.pack()

    confirmation = tk.Label(quit_frame, text="Are you sure you want to quit?", fg='white', bg='#2A6543')
    confirmation.grid(row=0, column=0, columnspan=2, pady=10)

    def quit_close():
        quit_window.destroy()
        main_window.destroy()

    button_styling = {"bg": "#afeeee", "fg": "#52AA5E", "activebackground": "#7fffd4", "activeforeground": "#008b8b",
                      "font": ("Comic Sans MS", 10, "bold")}

    yes_button = tk.Button(quit_frame, text="Yes", command=quit_close, width=5, **button_styling)
    yes_button.grid(row=1, column=0, padx=10, pady=10)

    no_button = tk.Button(quit_frame, text="No", command=quit_window.destroy, width=5, **button_styling)
    no_button.grid(row=1, column=1, padx=10, pady=10)

    for widget in quit_frame.winfo_children():
        widget.grid_configure(padx=3)

def display_receipt(receipt_number, first_name, last_name, item, amount):
    receipt_window = tk.Toplevel()
    receipt_window.title("Receipt")
    receipt_window.configure(bg='lightgreen')

    receipt_frame = tk.Frame(receipt_window, bg='#2A6543')  # Corrected color code
    receipt_frame.pack(padx=20, pady=20)

    tk.Label(receipt_frame, text=f"Receipt Number: {receipt_number}", fg='white', bg='#2A6543').pack(pady=5)
    tk.Label(receipt_frame, text=f"First Name: {first_name}", fg='white', bg='#2A6543').pack(pady=5)
    tk.Label(receipt_frame, text=f"Last Name: {last_name}", fg='white', bg='#2A6543').pack(pady=5)
    tk.Label(receipt_frame, text=f"Item Chosen: {item}", fg='white', bg='#2A6543').pack(pady=5)
    tk.Label(receipt_frame, text=f"Amount: {amount}", fg='white', bg='#2A6543').pack(pady=5)

    return_button = tk.Button(receipt_frame, text="Back", command=receipt_window.destroy)
    return_button.pack(pady=10)

def hire_window():
    global first_name_entry, last_name_entry, item_combobox, amount_spinbox  # Declare as global
    
    hire_window = tk.Toplevel(main_window)
    hire_window.title("Hire Form")

    button_styling = {"bg": "#afeeee", "fg": "#52AA5E", "activebackground": "#7fffd4", "activeforeground": "#008b8b",
                      "font": ("Comic Sans MS", 10, "bold")}

    hire_frame = tk.Frame(hire_window, bg='#2A6543')  # Corrected color code
    hire_frame.pack()

    user_info_frame = tk.LabelFrame(hire_frame, text="Hire Information", padx=80, pady=80)
    user_info_frame.grid(row=0, column=0)

    label_width = 15
    entry_width = 20

    first_name_label = tk.Label(user_info_frame, text="First Name:", width=label_width)
    first_name_label.grid(row=0, column=0)

    first_name_entry = tk.Entry(user_info_frame, width=entry_width)
    first_name_entry.grid(row=0, column=1)

    last_name_label = tk.Label(user_info_frame, text="Last Name:", width=label_width)
    last_name_label.grid(row=1, column=0)

    last_name_entry = tk.Entry(user_info_frame, width=entry_width)
    last_name_entry.grid(row=1, column=1)

    item_label = tk.Label(user_info_frame, text="Item Chosen:", width=label_width)
    item_label.grid(row=2, column=0)
    
    item_combobox = ttk.Combobox(user_info_frame, values=["Chairs", "Tables", "Benches", "Crockery"],
                                 width=entry_width - 2)
    item_combobox.grid(row=2, column=1)

    amount_label = tk.Label(user_info_frame, text="Amount of item:", width=label_width)
    amount_label.grid(row=3, column=0)

    amount_spinbox = tk.Spinbox(user_info_frame, from_=1, to=500, width=entry_width - 2)
    amount_spinbox.grid(row=3, column=1)

    receipt_button = tk.Button(user_info_frame, text="Add To Order", command=input_data, padx=20, width=10,
                               **button_styling)
    receipt_button.grid(row=4, column=0, pady=10)

    back_button = tk.Button(user_info_frame, text="Back", command=hire_window.destroy, padx=22, width=10,
                            **button_styling)
    back_button.grid(row=4, column=1, pady=10)

    for widget in user_info_frame.winfo_children():
        widget.grid_configure(pady=5, padx=5)

def display_hired_items():
    button_styling = {"bg": "#afeeee", "fg": "#52AA5E", "activebackground": "#7fffd4", "activeforeground": "#008b8b",
                      "font": ("Comic Sans MS", 10, "bold")}
    display_window = tk.Toplevel(main_window)
    display_window.title("Hired Items")
    display_window.configure(bg='#2A6543')  

    display_frame = tk.Frame(display_window, bg='#2A6543')  
    display_frame.pack(padx=20, pady=20)

    for item in hired_items:
        tk.Label(display_frame,
                 text=f"Receipt Number: {item[0]}, Name: {item[1]} {item[2]}, Item: {item[3]}, Amount: {item[4]}",
                 fg='white', bg='#2A6543').pack(pady=5)

    return_button = tk.Button(display_frame, text="Close", command=display_window.destroy, **button_styling)
    return_button.pack(pady=10)

def refund_section():
    def save_refund():
        receipt_number = receipt_entry.get()
        first_name = first_name_entry.get()
        item_to_refund = item_combobox.get()

        for item in hired_items:
            if item[0] == int(receipt_number) and item[1] == first_name and item[3] == item_to_refund:
                hired_items.remove(item)
                messagebox.showinfo("Info", "Item returned successfully!")
                break
        else:
            messagebox.showwarning("Warning", "Item not found!")

    refund_window = tk.Toplevel(main_window)
    refund_window.title("Return Form")

    refund_frame = tk.Frame(refund_window)  
    refund_frame.pack()

    refund_info_frame = tk.LabelFrame(refund_frame, text="Refund Information", padx=80, pady=80, bg='#2A6543')
    refund_info_frame.grid(row=0, column=0)

    label_width = 15
    entry_width = 20

    receipt_label = tk.Label(refund_info_frame, text="Receipt Number:", width=label_width)
    receipt_label.grid(row=0, column=0)

    receipt_entry = tk.Entry(refund_info_frame, width=entry_width)
    receipt_entry.grid(row=0, column=1)

    first_name_label = tk.Label(refund_info_frame, text="First Name:", width=label_width)
    first_name_label.grid(row=1, column=0)

    first_name_entry = tk.Entry(refund_info_frame, width=entry_width)
    first_name_entry.grid(row=1, column=1)

    item_label = tk.Label(refund_info_frame, text="Item to Refund:", width=label_width)
    item_label.grid(row=2, column=0)
    
    item_combobox = ttk.Combobox(refund_info_frame, values=["Chairs", "Tables", "Benches", "Crockery"],
                                 width=entry_width - 2)
    item_combobox.grid(row=2, column=1)

    button_styling = {"bg": "#afeeee", "fg": "#52AA5E", "activebackground": "#7fffd4", "activeforeground": "#008b8b",
                      "font": ("Comic Sans MS", 10, "bold")}

    save_button = tk.Button(refund_info_frame, text="Process Refund", command=save_refund, padx=20, width=10,
                            **button_styling)
    save_button.grid(row=3, column=0, pady=10)

    display_receipt_button = tk.Button(refund_info_frame, text="Display Hired Items", command= display_hired_items,padx=20,width=10, **button_styling)

    back_button = tk.Button(refund_info_frame, text="Back", command=refund_window.destroy, padx=22, width=10,
                            **button_styling)
    back_button.grid(row=3, column=1, pady=10)

    for widget in refund_info_frame.winfo_children():
        widget.grid_configure(pady=5, padx=5)

# Main window
main_window = tk.Tk()
main_window.title("Main Menu")
main_window.geometry("400x300")
main_window.configure(bg='#2A6543')  

button_styling = {"bg": "#afeeee", "fg": "#52AA5E", "activebackground": "#7fffd4", "activeforeground": "#008b8b",
                  "font": ("Comic Sans MS", 12, "bold")}

program_info = tk.Label(main_window, text="Welcome to Julies Party Hire!!")
program_info.pack(pady=10)

hire_button = tk.Button(main_window, text="Hire Item", command=hire_window, **button_styling)
hire_button.pack(pady=10)

display_button = tk.Button(main_window, text="Display Hired Items", command=display_hired_items, **button_styling)
display_button.pack(pady=10)

refund_button = tk.Button(main_window, text="Return Item", command=refund_section, **button_styling)
refund_button.pack(pady=10)

quit_button = tk.Button(main_window, text="Quit", command=quit_confirmation, **button_styling)
quit_button.pack(pady=10)

main_window.mainloop()
