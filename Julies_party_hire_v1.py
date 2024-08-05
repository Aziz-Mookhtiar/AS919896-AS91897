
import tkinter
from tkinter import ttk
import random



window = tkinter.Tk()
window.title("Hire Form")









hire_frame = tkinter.Frame(window)
hire_frame.pack()


user_info_frame =tkinter.LabelFrame(hire_frame,text ="Item Information",padx=80,pady=80)
user_info_frame.grid(row =0, column = 0)


first_name_label = tkinter.Label(user_info_frame,text = "First Name:")
first_name_label.grid(row=0,column=0)


last_name_label =tkinter.Label(user_info_frame,text = "Last Name:")
last_name_label.grid(row=1,column=0)


first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row =0,column=1)


last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row=1,column=1)



item = tkinter.Label(user_info_frame, text ="Item Chosen:")
item.grid(row =2,column =0)
item_combobox = ttk.Combobox(user_info_frame, values =["Three","one","Two"])
item_combobox.grid(row=2,column=1)


amount = tkinter.Label(user_info_frame,text = "Amount of item")
amount.grid(row=3,column=0)
amount_spinbox = tkinter.Spinbox(user_info_frame,from_ =1, to =500)
amount_spinbox.grid(row=3, column= 1)

add_order = tkinter.Button(user_info_frame, text = "Add to Order")
add_order.grid(row=4,column =4)

back_button = tkinter.Button(user_info_frame, text = "back")
back_button.grid(row=4,column =4)



for widget in user_info_frame.winfo_children():
    widget.grid_configure(pady = 5)





#allow window to stay appearing and not disapear
window.mainloop() 



 























