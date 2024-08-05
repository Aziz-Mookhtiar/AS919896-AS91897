import tkinter
from tkinter import ttk
import random






def quit_confirmation():
    quit_window = tkinter.Tk()
    quit_window.title("Quit Confirmation")

    quit_frame = tkinter.Frame(quit_window)
    quit_frame.pack()

    confirmation = tkinter.Label(quit_frame, text="Are you sure you want to quit?")
    confirmation.grid(row=0, column=0,columnspan =2, pady=10)

    def quit_close():
        quit_window.destroy()
        main_window.destroy()

    yes_button = tkinter.Button(quit_frame, text="Yes", command=quit_close, width=5)
    yes_button.grid(row=1, column=0,padx=10,pady=10)

    no_button = tkinter.Button(quit_frame, text="No", command=quit_window.destroy,width=5)
    no_button.grid(row=1, column=1,padx=10,pady=10)

    for widget in quit_frame.winfo_children():
        widget.grid_configure(padx=3)


def order_confirm():
    order_window = tkinter.Tk()
    order_window.title("Receipt")

    confirm_frame = tkinter.Frame(order_window)
    confirm_frame.pack()

    receipt_label = tkinter.Label(confirm_frame, text ="Your Receipt")
    receipt_label.grid(row=0,column=0)

    back_button = tkinter.Button(confirm_frame, text="Back", padx=22, command=order_confirm.destroy,width=10)
    back_button.grid(row=1, column=0)



    

       





def hire_window():
    hire_window = tkinter.Toplevel(main_window)
    hire_window.title("Hire Form")

    hire_frame = tkinter.Frame(hire_window)
    hire_frame.pack()

    user_info_frame = tkinter.LabelFrame(hire_frame, text="Hire Information", padx=80, pady=80)
    user_info_frame.grid(row=0, column=0)

    first_name_label = tkinter.Label(user_info_frame, text="First Name:")
    first_name_label.grid(row=0, column=0)

    last_name_label = tkinter.Label(user_info_frame, text="Last Name:")
    last_name_label.grid(row=1, column=0)

    first_name_entry = tkinter.Entry(user_info_frame)
    first_name_entry.grid(row=0, column=1)

    last_name_entry = tkinter.Entry(user_info_frame)
    last_name_entry.grid(row=1, column=1)

    item = tkinter.Label(user_info_frame, text="Item Chosen:")
    item.grid(row=2, column=0)
    item_combobox = ttk.Combobox(user_info_frame, values=["Three", "one", "Two"])
    item_combobox.grid(row=2, column=1)

    amount = tkinter.Label(user_info_frame, text="Amount of item:")
    amount.grid(row=3, column=0)
    amount_spinbox = tkinter.Spinbox(user_info_frame, from_=1, to=500)
    amount_spinbox.grid(row=3, column=1)

    receipt = tkinter.Button(user_info_frame, text="Print Receipt",command= order_confirm,padx=20,width=10)
    receipt.grid(row=4, column=0)

    back_button = tkinter.Button(user_info_frame, text="Back", padx=22, command=hire_window.destroy,width=10)
    back_button.grid(row=10, column=0)

  

    for widget in user_info_frame.winfo_children():
        widget.grid_configure(pady=5)



def refund_window():
    refund_window = tkinter.Toplevel(main_window)
    refund_window.title("Return Form")

    refund_frame = tkinter.Frame(refund_window)
    refund_frame.pack()

    refund_info_frame = tkinter.LabelFrame(refund_frame, text="Refund Information", padx=80, pady=80)
    refund_info_frame.grid(row=0, column=0)

    first_name_label = tkinter.Label(refund_info_frame, text="First Name:")
    first_name_label.grid(row=0, column=0)

    first_name_entry = tkinter.Entry(refund_info_frame,width=20)
    first_name_entry.grid(row=0, column=1)


    receipt_label = tkinter.Label(refund_info_frame, text="Receipt:")
    receipt_label.grid(row=2, column=0)

    receipt_entry = tkinter.Entry(refund_info_frame,width=20)
    receipt_entry.grid(row=2, column=1)


    item = tkinter.Label(refund_info_frame, text="Item Chosen:")
    item.grid(row=3, column=0)
    item_combobox = ttk.Combobox(refund_info_frame, values=["Three", "one", "Two"],width=20)
    item_combobox.grid(row=3, column=1)

    amount = tkinter.Label(refund_info_frame, text="Amount of item:")
    amount.grid(row=4, column=0)
    amount_spinbox = tkinter.Spinbox(refund_info_frame, from_=1, to=500,width=20)
    amount_spinbox.grid(row=4, column=1)


    back_button = tkinter.Button(refund_info_frame, text="Back", padx=22, command=refund_window.destroy,width=10)
    back_button.grid(row=10, column=0)

    for widget in refund_info_frame.winfo_children():
        widget.grid_configure(pady=5)







def validate_order(name, item, numofitem):
    if not name.isalpha():
        messagebox.showwarning("Warning", "You must only use alpahetcial characters in your name")
        return False
    if not numofitem.isdigit() or not (1 <= int(numofitem) <= 500):
        messagebox.showwarning("Warning", "The maximum amount of items that can be hired is 500")
        return False
    return True





    




# Main window
main_window = tkinter.Tk()
main_window.title("Party Hire")

main_frame = tkinter.Frame(main_window,padx=80,pady=80)
main_frame.pack()

welcome = tkinter.Label(main_frame, text="Welcome to Party Hire, Would you like to refund or hire a item?")
welcome.grid(row=0, column=0,pady=10)

Hire_form = tkinter.Button(main_frame, text="Hire", command=hire_window, width=20)
Hire_form.grid(row=1, column=0, pady=10)


Return_form = tkinter.Button(main_frame, text="Returns/Refund", command=refund_window, width=20)
Return_form.grid(row=2, column=0, pady=10)


quit_button = tkinter.Button(main_frame, text="Quit", command=quit_confirmation, width=20)
quit_button.grid(row=3, column=0, pady=10)




for widget in main_frame.winfo_children():
    widget.grid_configure(pady=5)

main_window.mainloop()




 


    



