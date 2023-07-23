import tkinter as tk
import tkinter.messagebox as messagebox
import pyodbc
import FE_Con


# Create a tkinter window
window = tk.Tk()
window.title("MAIN PAGE")
window.geometry("1080x1080")
window.configure(bg='#c6e9fe')

# Create a main heading label
heading_label = tk.Label(master=window, text="CAR RENTAL SYSTEM", font=("Lucida Handwriting", 30, "bold underline"), bg='#c6e9fe', foreground='black')
heading_label.pack(padx=30, pady=30)

#CREATE A BUTTON TO OPEN USER CUSTOMER INFORMATION FORM
button = tk.Button(master=window, text="BOOK NOW", command=FE_Con.show_CustomerTable)
button.config(font=("Courier", 12), height=2, width=15)
button.pack(padx=20, pady=20)

#CREATE A BUTTON TO OPEN BILLING FORM
button = tk.Button(master=window, text="GENERATE BILL ", command=FE_Con.Show_Billing_Details)
button.config(font=("Courier", 12), height=2, width=15)
button.pack(padx=30, pady=30)

window.mainloop()