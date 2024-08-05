import tkinter as tk
from tkinter import ttk, messagebox
import random

# Stores data
hired_items = []

def input_data():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()

    if first_name and last_name:
        receipt_number = random.randint(1000, 9999)
        item = item_combobox.get()
        amount = amount_spinbox.get()
       
        hired_items.append((receipt_number, first_name, last_name, item, amount))
        messagebox.showinfo("Info", "Item hired successfully!")
       
        display_receipt(receipt_number, first_name, last_name, item, amount)
    else:
        messagebox.showwarning(title="Error", message="First name and last name are required.")

def quit_confirmation():
    quit_window = tk.Toplevel()
    quit_window.title("Quit Confirmation")
 

    quit_frame = tk.Frame(quit_window,bg='lightgreen')
    quit_frame.pack()

    confirmation = tk.Label(quit_frame, text="Are you sure you want to quit?")
    confirmation.grid(row=0, column=0, columnspan=2, pady=10)

    def quit_close():
        quit_window.destroy()
        main_window.destroy()

    yes_button = tk.Button(quit_frame, text="Yes", command=quit_close, width=5)
    yes_button.grid(row=1, column=0, padx=10, pady=10)

    no_button = tk.Button(quit_frame, text="No", command=quit_window.destroy, width=5)
    no_button.grid(row=1, column=1, padx=10, pady=10)

    for widget in quit_frame.winfo_children():
        widget.grid_configure(padx=3)

def display_receipt(receipt_number, first_name, last_name, item, amount):
    receipt_window = tk.Toplevel()
    receipt_window.title("Receipt")
    receipt_window.configure(bg='lightgreen')

    receipt_frame = tk.Frame(receipt_window,bg='lightgreen')
    receipt_frame.pack(padx=20, pady=20)

    tk.Label(receipt_frame, text=f"Receipt Number: {receipt_number}").pack(pady=5)
    tk.Label(receipt_frame, text=f"First Name: {first_name}").pack(pady=5)
    tk.Label(receipt_frame, text=f"Last Name: {last_name}").pack(pady=5)
    tk.Label(receipt_frame, text=f"Item Chosen: {item}").pack(pady=5)
    tk.Label(receipt_frame, text=f"Amount: {amount}").pack(pady=5)

    return_button = tk.Button(receipt_frame, text="Back", command=receipt_window.destroy)
    return_button.pack(pady=10)

def hire_window():
    hire_window = tk.Toplevel(main_window)
    hire_window.title("Hire Form")


    hire_frame = tk.Frame(hire_window,bg='lightgreen')
    hire_frame.pack()

    user_info_frame = tk.LabelFrame(hire_frame, text="Hire Information", padx=80, pady=80,bg='lightgreen')
    user_info_frame.grid(row=0, column=0)

    label_width = 15
    entry_width = 20

    first_name_label = tk.Label(user_info_frame, text="First Name:", width=label_width)
    first_name_label.grid(row=0, column=0)

    global first_name_entry
    first_name_entry = tk.Entry(user_info_frame, width=entry_width)
    first_name_entry.grid(row=0, column=1)

    last_name_label = tk.Label(user_info_frame, text="Last Name:", width=label_width)
    last_name_label.grid(row=1, column=0)

    global last_name_entry
    last_name_entry = tk.Entry(user_info_frame, width=entry_width)
    last_name_entry.grid(row=1, column=1)

    item_label = tk.Label(user_info_frame, text="Item Chosen:", width=label_width)
    item_label.grid(row=2, column=0)
    global item_combobox
    item_combobox = ttk.Combobox(user_info_frame, values=["Chairs", "Tables", "Benches", "Crockery"], width=entry_width - 2)
    item_combobox.grid(row=2, column=1)

    amount_label = tk.Label(user_info_frame, text="Amount of item:", width=label_width)
    amount_label.grid(row=3, column=0)
    global amount_spinbox
    amount_spinbox = tk.Spinbox(user_info_frame, from_=1, to=500, width=entry_width - 2)
    amount_spinbox.grid(row=3, column=1)

    receipt_button = tk.Button(user_info_frame, text="Add To Order", command=input_data, padx=20, width=10)
    receipt_button.grid(row=4, column=0, pady=10)

    back_button = tk.Button(user_info_frame, text="Back", command=hire_window.destroy, padx=22, width=10)
    back_button.grid(row=4, column=1, pady=10)

    for widget in user_info_frame.winfo_children():
        widget.grid_configure(pady=5)

def display_hired_items():
    display_window = tk.Toplevel(main_window)
    display_window.title("Hired Items")
    display_window.configure(bg='lightgreen')

    display_frame = tk.Frame(display_window,bg='lightgreen')
    display_frame.pack(padx=20, pady=20)

    for item in hired_items:
        tk.Label(display_frame, text=f"Receipt Number: {item[0]}, Name: {item[1]} {item[2]}, Item: {item[3]}, Amount: {item[4]}").pack(pady=5)

    return_button = tk.Button(display_frame, text="Close", command=display_window.destroy)
    return_button.pack(pady=10)

def refund_section():
    def save_refund():
        receipt_number = receipt_entry.get()
        first_name = first_name_entry.get()
        item_to_refund = item_combobox.get()
        amount = amount_spinbox.get()

        for item in hired_items:
            if item[0] == int(receipt_number) and item[1] == first_name and item[3] == item_to_refund:
               

                hired_items.remove(item)
                messagebox.showinfo("Info", "Item returned successfully!")
                break
        else:
            messagebox.showwarning("Warning", "Item not found!")

    refund_window = tk.Toplevel(main_window)
    refund_window.title("Return Form")


    refund_frame = tk.Frame(refund_window,bg='lightgreen')
    refund_frame.pack()
    

    refund_info_frame = tk.LabelFrame(refund_frame, text="Refund Information", padx=80, pady=80,bg='lightgreen')
    refund_info_frame.grid(row=0, column=0)

    label_width = 15
    entry_width = 20

    receipt_label = tk.Label(refund_info_frame, text="Receipt Number:", width=label_width)
    receipt_label.grid(row=0, column=0)

    global receipt_entry
    receipt_entry = tk.Entry(refund_info_frame, width=entry_width)
    receipt_entry.grid(row=0, column=1)

    first_name_label = tk.Label(refund_info_frame, text="First Name:", width=label_width)
    first_name_label.grid(row=1, column=0)

    global first_name_entry
    first_name_entry = tk.Entry(refund_info_frame, width=entry_width)
    first_name_entry.grid(row=1, column=1)

    item_label = tk.Label(refund_info_frame, text="Item to Refund:", width=label_width)
    item_label.grid(row=2, column=0)
    global item_combobox
    item_combobox = ttk.Combobox(refund_info_frame, values=["Chairs", "Tables", "Benches", "Crockery"], width=entry_width - 2)
    item_combobox.grid(row=2, column=1)


    save_button = tk.Button(refund_info_frame, text="Save", command=save_refund, padx=22, width=10)
    save_button.grid(row=4, column=0, pady=10)

    display_button = tk.Button(refund_info_frame, text="Display Hired Items", command=display_hired_items, padx=22, width=15)
    display_button.grid(row=4, column=1, pady=10)

    back_button = tk.Button(refund_info_frame, text="Back", command=refund_window.destroy, padx=22, width=10)
    back_button.grid(row=5, column=0, pady=10)

    for widget in refund_info_frame.winfo_children():
        widget.grid_configure(pady=5)

def validate_order(name, item, numofitem):
    if not name.isalpha():
        messagebox.showwarning("Warning", "You must only use alphabetical characters in your name")
        return False
    if not numofitem.isdigit() or not (1 <= int(numofitem) <= 500):
        messagebox.showwarning("Warning", "The maximum amount of items that can be hired is 500")
        return False
    return True

# Main window
main_window = tk.Tk()
main_window.title("Party Hire")


main_frame = tk.Frame(main_window, padx=80, pady=80,bg='lightgreen')
main_frame.pack()

welcome_label = tk.Label(main_frame, text="Welcome to Party Hire. Would you like to hire or refund an item?")
welcome_label.grid(row=0, column=0, pady=10)

hire_button = tk.Button(main_frame, text="Hire", command=hire_window, width=20)
hire_button.grid(row=1, column=0, pady=10)

refund_button = tk.Button(main_frame, text="Returns/Refund", command=refund_section, width=20)
refund_button.grid(row=2, column=0, pady=10)

display_button = tk.Button(main_frame, text="Display Hired Items", command=display_hired_items, width=20)
display_button.grid(row=3, column=0, pady=10)

quit_button = tk.Button(main_frame, text="Quit", command=quit_confirmation, width=20)
quit_button.grid(row=4, column=0, pady=10)

for widget in main_frame.winfo_children():
    widget.grid_configure(pady=5)

main_window.mainloop()
