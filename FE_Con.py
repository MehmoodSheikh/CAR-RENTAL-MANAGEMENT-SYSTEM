import tkinter as tk
from tkinter import messagebox,OptionMenu
import pyodbc
import tkcalendar as tkc
import datetime
from datetime import date
from datetime import datetime

connection = pyodbc.connect('Driver={SQL Server};' 'Server=MOODY-DESKTOP\SQLEXPRESS;'
                             'Database=CRMS;' 'Trusted_connection=yes;')



#------------------------FORM-1------------------------
def show_CustomerTable():

    def submit_form():
        # Get the values from the form fields
        fname = fname_entry.get()
        lname = lname_entry.get()
        phone_no = phone_no_entry.get()
        nic_no = nic_no_entry.get()
        caddress = caddress_entry.get()
        dl_no = dl_no_entry.get()

        # Validate the form fields
        if not fname or not lname or not phone_no or not nic_no or not caddress or not dl_no:
            messagebox.showerror("ERROR", "ALL FIELDS ARE REQUIRED")
            return

        cursor = connection.cursor()

        # Insert the form data into the database
        cursor.execute('insert into CUSTOMER(FNAME,LNAME,PHONE_NO,NIC_NO,CADDRESS,DL_NO) values(?,?,?,?,?,?);',
            (fname, lname, phone_no, nic_no, caddress, dl_no)
        )
        connection.commit()

        # Close the database connection
        cursor.close()
        #connection.close()

        # Save the form data to the database
        # (This part will depend on how you have set up your database)

        # Clear the form fields
        fname_entry.delete(0, 'end')
        lname_entry.delete(0, 'end')
        phone_no_entry.delete(0, 'end')
        nic_no_entry.delete(0, 'end')
        caddress_entry.delete(0, 'end')
        dl_no_entry.delete(0, 'end')

        # Show a success message
        messagebox.showinfo("SUCCESS", "ENTERED DATA SAVED SUCCESSFULLY")

        # Create a "Next" button
        next_button = tk.Button(master=form_frame, text="Next", font=('Helvetica', 12), bg='#f2f2f2', command=show_car_details)
        next_button.config(font=("Courier", 12), height=1, width=8)
        next_button.pack(padx=20, pady=20)


    # Create a tkinter window
    window = tk.Tk()
    window.title("CUSTOMER INFORMATION")
    window.geometry("1080x1080")
    window.configure(bg='#c6e9fe')

    # Create a main heading label
    heading_label = tk.Label(master=window, text="CUSTOMER INFORMATION", font=("Lucida Handwriting", 20, "bold underline"), bg='#c6e9fe', foreground='black')
    heading_label.pack(padx=10, pady=10)

    # Create a form frame
    form_frame = tk.Frame(master=window, bg='#c6e9fe')
    form_frame.pack(pady=20)

    # Create a label and entry field for the first name
    fname_label = tk.Label(master=form_frame, text="First Name:", font=('Serif', 14), bg='#c6e9fe')
    fname_label.pack(padx=10, pady=10)

    fname_entry = tk.Entry(master=form_frame, font=('Helvetica', 12), bg='#f2f2f2')
    fname_entry.pack(padx=10, pady=10)

    # Create a label and entry field for the last name
    lname_label = tk.Label(master=form_frame, text="Last Name:", font=('Serif', 14), bg='#c6e9fe')
    lname_label.pack(padx=10, pady=10)

    lname_entry = tk.Entry(master=form_frame, font=('Helvetica', 12), bg='#f2f2f2')
    lname_entry.pack(padx=10, pady=10)

    # Create a label and entry field for the phone number
    phone_no_label = tk.Label(master=form_frame, text="Phone Number:", font=('Serif', 14), bg='#c6e9fe')
    phone_no_label.pack(padx=10, pady=10)

    phone_no_entry = tk.Entry(master=form_frame, font=('Helvetica', 12), bg='#f2f2f2')
    phone_no_entry.pack(padx=10, pady=10)

    # Create a label and entry field for the NIC number
    nic_no_label = tk.Label(master=form_frame, text="NIC Number:", font=('Serif', 14), bg='#c6e9fe')
    nic_no_label.pack(padx=10, pady=10)

    nic_no_entry = tk.Entry(master=form_frame, font=('Helvetica', 12), bg='#f2f2f2')
    nic_no_entry.pack(padx=10, pady=10)

    # Create a label and entry field for the current address
    caddress_label = tk.Label(master=form_frame, text="Current Address:", font=('Serif', 14), bg='#c6e9fe')
    caddress_label.pack(padx=10, pady=10)

    caddress_entry = tk.Entry(master=form_frame, font=('Helvetica', 12), bg='#f2f2f2')
    caddress_entry.pack(padx=10, pady=10)

    # Create a label and entry field for the driver's license number
    dl_no_label = tk.Label(master=form_frame, text="Driver's License Number:", font=('Serif', 14), bg='#c6e9fe')
    dl_no_label.pack(padx=10, pady=10)

    dl_no_entry = tk.Entry(master=form_frame, font=('Helvetica', 12), bg='#f2f2f2')
    dl_no_entry.pack(padx=10, pady=10)

    # Create a submit button
    submit_button = tk.Button(master=form_frame, text="Submit", command=submit_form)
    submit_button.config(font=("Courier", 12), height=1, width=8)
    submit_button.pack(padx=20, pady=20)

    # Run the tkinter event loop
    window.mainloop()

#------------------------FORM-2------------------------

def show_car_details():
    # Create a form with a dropdown list and a search button
    form = tk.Tk()
    form.title("CAR DETAILS")
    form.geometry("1080x1080")
    form.configure(bg='#c6e9fe')

    # Create a main heading label
    heading_label = tk.Label(master=form, text="CAR DETAILS",font=("Lucida Handwriting", 30, "bold underline"), bg='#c6e9fe', foreground='black').grid(row=0, column=4)
    
    
    # Create a label for the dropdown list
    tk.Label(form, text="CAR_NAME", bg='#c6e9fe',font=("Courier", 12, "bold underline")).grid(row=4, column=2)

    # Create a dropdown list with the car names
    car_name = tk.StringVar(form)
    car_name.set("Select a car") # default value
    car_names = ["3 Series", "Accord", "Camry", "Escape", "A6", "370Z", "Mustang", "Sienna", "F-150"]
    tk.OptionMenu(form, car_name, *car_names).grid(row=4, column=4)

    # Create a search button
    def search():
        # Clear the list widget
        list_widget.delete(0, "end")

        # Get the selected car name
        selected_car = car_name.get()

        # Connect to the database and retrieve the details for the selected car
        # Replace "database_connection" with your own database connection

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM CAR_DETAILS WHERE CAR_NAME = ?", (selected_car,))
        result = cursor.fetchone()
        cursor.execute("SELECT * FROM CAR_CATEGORY WHERE CATEGORY_NAME = ?", (result[4],))
        category_result = cursor.fetchone()
        

        # Add the details for the selected car to the list widget
        list_widget.insert("end", f"REGISTRATION_NO: {result[0]}")
        list_widget.insert("end", f"CAR_NAME: {result[1]}")
        list_widget.insert("end", f"MAKE: {result[2]}")
        list_widget.insert("end", f"MODEL_NAME: {result[3]}")
        list_widget.insert("end", f"CATEGORY_NAME: {result[4]}")
        list_widget.insert("end", f"NO_OF_PERSON: {category_result[1]}")
        list_widget.insert("end", f"COST_PER_DAY: {category_result[2]}")

        # Enable the change_car_name_button
        change_car_name_button.config(state="normal")
        change_car_name_button.update()

        # Enable the Next button
        next_button.config(state="normal")
        next_button.update()

    # Create registration number dropdown menu
    reg_no_label = tk.Label(form, text="REGISTRATION NUMBER:", bg='#c6e9fe',font=("Courier", 12, "bold underline"))
    reg_no_options = ["789GHI", "ABC123", "DEF456", "GHI789", "JKL012", "MNO345", "PQR678", "STU901", "VWX234", "YZ0567"]
    reg_no_var = tk.StringVar(form)
    reg_no_menu = tk.OptionMenu(form, reg_no_var, *reg_no_options)
    reg_no_label.grid(row=14, column=4)
    reg_no_menu.grid(row=14, column=5)

    # Create label to display REGISTRATION NUMBER message
    reg_no_error_label = tk.Label(form, text="KINDLY, SELECT REGISTRATION NUMBER OF YOUR SELECTED CAR.", fg="red", bg='#c6e9fe',font=("Courier", 12))
    reg_no_error_label.grid(row=15, column=4)


    def submit_reg_no():
        cursor = connection.cursor()
        # Insert data into database
        cursor.execute(f"INSERT INTO BOOKING_DETAILS (REGISTRATION_NO) VALUES ('{reg_no_var.get()}')")
        connection.commit()
        tk.messagebox.showinfo("SUCCESS", "ENTERED DATA SAVED SUCCESSFULLY")

    tk.Button(form, text="Search",font=("Courier", 12),  height=1, width=8, command=search).grid(row=4, column=6)

    def change_car_name():
        # Clear the list widget
        list_widget.delete(0, "end")

        # Reset the dropdown list to the default value
        car_name.set("Select a car")

        # Disable the Next button
        next_button.config(state="disabled")
        next_button.update()

        # Enable the change_car_name_button
        change_car_name_button.config(state="disabled")
        change_car_name_button.update()
        
    # Add the "Change car name" button below the search button
    change_car_name_button=tk.Button(form, text="Change Car",font=("Courier"),  height=1, width=10, state="disabled",command=change_car_name)
    change_car_name_button.grid(row=10, column=4)


    # Create a list widget to display the car details
    list_widget = tk.Listbox(form, width=30)
    list_widget.grid(row=5, column=3, columnspan=3)

    #Initiating functions
    def calling_func():
        if reg_no_var.get() == '':
            tk.messagebox.showerror('ERROR', 'PLEASE SELECT A REGISTRATION NUMBER')
        else:
            submit_reg_no()
            show_booking_details(reg_no_var.get())
    
    # Display the "NEXT" button and message encouraging the user to proceed to booking
    next_button = tk.Button(form, text='NEXT',font=("Courier", 12),  height=1, width=8 ,state="disabled", command= calling_func)
    next_button.grid(row=19, column=4) 
    tk.Label(form, text='PRESS NEXT BUTTON TO PROCEED TO BOOKING', fg="red",bg='#c6e9fe',font=("Courier", 12)).grid(row=20, column=4) 
    
    form.mainloop()
    #connection.close()



#------------------------FORM-3------------------------

def show_booking_details(safe_val_reg_no):

    # Create form window
    form_window = tk.Tk()
    form_window.title("BOOKING DETAILS")
    form_window.geometry("1080x1080")
    form_window.configure(bg='#c6e9fe')

    # Create a main heading label
    heading_label = tk.Label(master=form_window, text="BOOKING DETAILS", font=("Lucida Handwriting", 30, "bold underline"),  bg='#c6e9fe', foreground='black')
    heading_label.pack(padx=10, pady=10)
    
    # Create date out calendar widget
    date_out_label = tk.Label(form_window, text="START DATE:",font=('Serif', 14), bg='#c6e9fe')
    date_out_calendar = tkc.DateEntry(form_window, width=12, background='darkblue',
                                      foreground='white', borderwidth=2)
    date_out_label.pack()
    date_out_calendar.pack()
    
    # Create date back calendar widget
    date_back_label = tk.Label(form_window, text="END DATE:",font=('Serif', 14), bg='#c6e9fe')
    date_back_calendar = tkc.DateEntry(form_window, width=12, background='darkblue',
                                       foreground='white', borderwidth=2)
    date_back_label.pack()
    date_back_calendar.pack()
    
    # Create DL number text field
    dl_no_label = tk.Label(form_window, text="DRIVER'S LICENSE NUMBER:",font=('Serif', 14), bg='#c6e9fe')
    dl_no_entry = tk.Entry(form_window)
    dl_no_label.pack()
    dl_no_entry.pack()

    # Create label to display DL number message
    reg_no_error_label = tk.Label(form_window, text="YOUR DRIVING LICENSE NO. MUST BE SAME AS ENTERED PREVIOUSLY", fg="red",font=("Courier", 12), bg='#c6e9fe')
    reg_no_error_label.pack()

    def submit_data():
        # Check that all required fields have been filled in
        if date_out_calendar.get() == '':
            tk.messagebox.showerror('ERROR', 'PLEASE SELECT A START DATE')
        elif date_back_calendar.get() == '':
            tk.messagebox.showerror('ERROR', 'PLEASE SELECT A END DATE')
        elif dl_no_entry.get() == '':
            tk.messagebox.showerror('ERROR', 'PLEASE ENTER A DRIVER\'S LICENSE NUMBER')
        #elif reg_no_var.get() == '':
            #tk.messagebox.showerror('Error', 'Please select a REGISTRATION NUMBER')
        else:
            # Convert date strings to datetime objects
            date_out = datetime.strptime(date_out_calendar.get(), '%m/%d/%y')
            date_back = datetime.strptime(date_back_calendar.get(), '%m/%d/%y')


            # Check that date back is greater than date out
            if date_back < date_out:
                tk.messagebox.showerror('ERROR', 'END DATE MUST BE LATER THAN START DATE')
            else:
                 # Check if DL number already exists in CUSTOMER table
                cursor = connection.cursor()
                cursor.execute(f"SELECT DL_NO FROM CUSTOMER WHERE DL_NO = '{dl_no_entry.get()}'")
                dl_no = cursor.fetchone()

                if dl_no:
                    # DL number already exists, insert data into BOOKING_DETAILS table
                    cursor = connection.cursor()
                    # Insert data into database
                    cursor.execute(f"UPDATE BOOKING_DETAILS SET DATE_OUT = '{date_out_calendar.get()}', DATE_BACK = '{date_back_calendar.get()}', DL_NO = '{dl_no_entry.get()}' WHERE REGISTRATION_NO = '{safe_val_reg_no}'")
                    connection.commit()
                    tk.messagebox.showinfo('SUCCESS', 'BOOKING DETAILS SAVED SUCCESSFULLY')

                    def generate_booking_details():
                        # Create listbox widget
                        listbox = tk.Listbox(form_window)
                        listbox = tk.Listbox(form_window, width=40, height=25)
                        listbox.pack()


                        # Execute SELECT statements to retrieve data
                        #cursor = connection.cursor()
                        cursor.execute("SELECT * FROM CUSTOMER WHERE DL_NO=?", dl_no_entry.get())

                        # Iterate over the results and insert them into the listbox
                        for row in cursor:
                            listbox.insert(tk.END, "DL_NO: " + row[5])
                            listbox.insert(tk.END, "FNAME: " + row[0])
                            listbox.insert(tk.END, "LNAME: " + row[1])
                            listbox.insert(tk.END, "PHONE_NO: " + row[2])
                            listbox.insert(tk.END, "NIC_NO: " + row[3])
                            listbox.insert(tk.END, "CADDRESS: " + row[4])

                        cursor.execute("SELECT * FROM CAR_CATEGORY WHERE CATEGORY_NAME IN (SELECT CATEGORY_NAME FROM CAR_DETAILS WHERE REGISTRATION_NO=?)", safe_val_reg_no)
                        for row in cursor:
                            listbox.insert(tk.END, "CATEGORY_NAME: " + row[0])
                            listbox.insert(tk.END, "NO_OF_PERSON: " + str(row[1]))
                            listbox.insert(tk.END, "COST_PER_DAY: " + str(row[2]))

                        cursor.execute("SELECT * FROM CAR_DETAILS WHERE REGISTRATION_NO=?", safe_val_reg_no)
                        for row in cursor:
                            listbox.insert(tk.END, "REGISTRATION_NO: " + row[0])
                            listbox.insert(tk.END, "CAR_NAME: " + row[1])
                            listbox.insert(tk.END, "MAKE: " + row[2])
                            listbox.insert(tk.END, "MODEL_NAME: " + row[3])
                            #listbox.insert(tk.END, "CATEGORY_NAME: " + row[4])

                        cursor.execute("SELECT * FROM BOOKING_DETAILS WHERE REGISTRATION_NO=?", safe_val_reg_no)
                        for row in cursor:
                            listbox.insert(tk.END, "BOOKING_ID: " + str(row[0]))
                            listbox.insert(tk.END, "DATE_OUT: " + str(row[1]))
                            listbox.insert(tk.END, "DATE_BACK: " + str(row[2]))
                            #listbox.insert(tk.END, "DL_NO: " + row[3])
                            #listbox.insert(tk.END, "REGISTRATION_NO: " + row[4])

                        # Create label to display BILLING NO. message
                        bill_no_msg_label = tk.Label(form_window, text="KINDLY, SAFE BOOKING ID. IT IS REQUIRED TO GENERATE BILL.",font=("Courier", 12), fg="red", bg='#c6e9fe')
                        bill_no_msg_label.pack()

                        # Create label to display GO HOME message
                        go_home_msg_label = tk.Label(form_window, text="TO GENERATE BILL VISIT HOME PAGE.",font=("Courier", 12), fg="red", bg='#c6e9fe')
                        go_home_msg_label.pack()

                        # Close the cursor
                        cursor.close()

                    # Show "Show Booking Details" button
                    show_details_button = tk.Button(form_window, text="View Info",font=("Courier", 10), height=1, width=8, command=generate_booking_details)
                    show_details_button.pack()

                else:
                    tk.messagebox.showerror('ERROR', 'DRIVING LICENSE NO. IS NOT MATCHED')

    # Create submit button
    submit_button = tk.Button(form_window, text="Submit",font=("Courier", 12), height=1, width=8, command=submit_data)
    submit_button.pack()

    form_window.mainloop()

#------------------------FORM-4------------------------


def Show_Billing_Details():

    def check_details():

        # Connect to the database
        cursor = connection.cursor()

        dl_no = dl_no_entry.get()
        booking_id = booking_id_entry.get()

        if not booking_id or not dl_no:
            messagebox.showerror("ERROR", "ALL FIELDS ARE REQUIRED")
            return

        # Retrieve the record with the matching DL_NO from the "CUSTOMER" table
        cursor.execute("SELECT * FROM CUSTOMER WHERE DL_NO = ?", (dl_no_entry.get(),))
        dl_no = cursor.fetchone()

        # If the DL_NO is not found in the "CUSTOMER" table, display an error message
        if not dl_no:
            messagebox.showerror("ERROR", " DRIVER\'S LICENSE NUMBER NOT FOUND")
            return

        # Retrieve the record with the matching BOOKING_ID from the "BOOKING_DETAILS" table
        cursor.execute("SELECT * FROM BOOKING_DETAILS WHERE BOOKING_ID = ?", (booking_id_entry.get(),))
        booking_id = cursor.fetchone()

        # If the BOOKING_ID is not found in the "BOOKING_DETAILS" table, display an error message
        if not booking_id:
            messagebox.showerror("ERROR", "BOOKING ID NOT FOUND.")
            return
        else:

            # Retrieve date_out, date_back, and cost_per_day from the "BOOKING_DETAILS" and "CAR_CATEGORY" tables
            cursor.execute("SELECT DATE_OUT, DATE_BACK, CAR_CATEGORY.COST_PER_DAY FROM BOOKING_DETAILS INNER JOIN CAR_DETAILS ON BOOKING_DETAILS.REGISTRATION_NO = CAR_DETAILS.REGISTRATION_NO INNER JOIN CAR_CATEGORY ON CAR_DETAILS.CATEGORY_NAME = CAR_CATEGORY.CATEGORY_NAME WHERE BOOKING_ID = ?", (booking_id_entry.get(),))
            date_out, date_back, cost_per_day = cursor.fetchone()

            # Calculate the total amount
            date_out = datetime.strptime(date_out, "%Y-%m-%d").date()
            date_back = datetime.strptime(date_back, "%Y-%m-%d").date()
            total_amount = (date_back - date_out).days * cost_per_day

            # Insert the data into the "BILLING_DETAILS" table
            cursor.execute("INSERT INTO BILLING_DETAILS (BILL_DATE, TOTAL_AMOUNT, BOOKING_ID) VALUES (?, ?, ?)", (str(date.today()), total_amount, booking_id_entry.get()))

            # Commit the changes to the database
            connection.commit()

            # Show a success message
            messagebox.showinfo("SUCCESS", "ENTERED DATA SAVED SUCCESSFULLY")

            def generate_bill():

                dl_no = dl_no_entry.get()
                booking_id = booking_id_entry.get()

                # Retrieve the customer's details from the "CUSTOMER" table
                cursor.execute("SELECT FNAME, LNAME, PHONE_NO, NIC_NO, CADDRESS, DL_NO FROM CUSTOMER WHERE DL_NO = ?", (dl_no,))
                customer_details = cursor.fetchone()

                # Retrieve the car's details and category name from the "CAR_DETAILS" and "CAR_CATEGORY" tables
                cursor.execute("SELECT CAR_DETAILS.REGISTRATION_NO, CAR_DETAILS.CAR_NAME, CAR_DETAILS.MAKE, CAR_DETAILS.MODEL_NAME, CAR_CATEGORY.CATEGORY_NAME, CAR_CATEGORY.NO_OF_PERSON, CAR_CATEGORY.COST_PER_DAY FROM CAR_DETAILS JOIN CAR_CATEGORY ON CAR_DETAILS.CATEGORY_NAME = CAR_CATEGORY.CATEGORY_NAME WHERE REGISTRATION_NO = (SELECT REGISTRATION_NO FROM BOOKING_DETAILS WHERE BOOKING_ID = ?)", (booking_id,))
                car_details = cursor.fetchone()

                # Retrieve the booking details from the "BOOKING_DETAILS" table
                cursor.execute("SELECT BOOKING_ID, DATE_OUT, DATE_BACK FROM BOOKING_DETAILS WHERE BOOKING_ID = ?", (booking_id,))
                booking_details = cursor.fetchone()

                # Retrieve the bill details from the "BILLING_DETAILS" table
                cursor.execute("SELECT BILL_DATE, TOTAL_AMOUNT FROM BILLING_DETAILS WHERE BOOKING_ID = ?", (booking_id,))
                bill_details = cursor.fetchone()

                # Close the database connection and cursor
                #cursor.close()

                # Create a new window to display the bill details
                bill_window = tk.Tk()
                bill_window.title("BILL")
                bill_window.configure(bg='#c6e9fe')
                bill_listbox = tk.Listbox(bill_window, width=50, height=25)
                bill_listbox.pack()

                # Insert the customer's details into the listbox
                bill_listbox.insert(tk.END, "Customer Details:")
                bill_listbox.insert(tk.END, "Name: {} {}".format(customer_details[0], customer_details[1]))
                bill_listbox.insert(tk.END, "Phone Number: {}".format(customer_details[2]))
                bill_listbox.insert(tk.END, "NIC Number: {}".format(customer_details[3]))
                bill_listbox.insert(tk.END, "Address: {}".format(customer_details[4]))
                bill_listbox.insert(tk.END, "Driving License Number: {}".format(customer_details[5]))
                bill_listbox.insert(tk.END, "")

                # Insert the car's details and category name into the listbox
                bill_listbox.insert(tk.END, "Car Details:")
                bill_listbox.insert(tk.END, "Registration Number: {}".format(car_details[0]))
                bill_listbox.insert(tk.END, "Car Name: {}".format(car_details[1]))
                bill_listbox.insert(tk.END, "Make: {}".format(car_details[2]))
                bill_listbox.insert(tk.END, "Model: {}".format(car_details[3]))
                bill_listbox.insert(tk.END, "Category Name: {}".format(car_details[4]))
                bill_listbox.insert(tk.END, "No of Person: {}".format(car_details[5]))
                bill_listbox.insert(tk.END, "Cost per Day: {}".format(car_details[6]))
                bill_listbox.insert(tk.END, "")

                # Insert the booking details into the listbox
                bill_listbox.insert(tk.END, "Booking Details:")
                bill_listbox.insert(tk.END, "Booking ID: {}".format(booking_details[0]))
                bill_listbox.insert(tk.END, "Date Out: {}".format(booking_details[1]))
                bill_listbox.insert(tk.END, "Date Back: {}".format(booking_details[2]))
                bill_listbox.insert(tk.END, "")

                # Insert the bill details into the listbox
                bill_listbox.insert(tk.END, "Bill Details:")
                bill_listbox.insert(tk.END, "Bill Date: {}".format(bill_details[0]))
                bill_listbox.insert(tk.END, "Total Amount: {}".format(bill_details[1]))
                bill_listbox.insert(tk.END, "")

                # run the window
                bill_window.mainloop()

                # Close the database connection and cursor
                cursor.close()

            # Generate Billing information
            generate_button = tk.Button(form, text="View Bill",font=("Courier", 12), height=1, width=8, command=generate_bill)
            generate_button.grid(row=10, column=5, padx=5, pady=5)

    # Create a Tkinter form
    form = tk.Tk()
    form.title("BILLING DETAILS")
    form.configure(bg='#c6e9fe')
    #form.geometry("1080x1080")

    # Create a main heading label
    dl_no_label = tk.Label(form, text="Billing Details", font=("Lucida Handwriting", 30, "bold underline"), bg='#c6e9fe', foreground='black')
    dl_no_label.grid(row=0, column=5, padx=30, pady=30)

    # Create input fields for DL_NO, BOOKING_ID, and BILL_DATE
    dl_no_label = tk.Label(form, text="Driver's License  Number ", font=('Serif', 16), bg='#c6e9fe')
    dl_no_label.grid(row=1, column=5, padx=5, pady=5)
    dl_no_entry = tk.Entry(form)
    dl_no_entry.grid(row=2, column=5, padx=20, pady=20)

    booking_id_label = tk.Label(form, text="Booking ID ", font=('Serif', 16), bg='#c6e9fe')
    booking_id_label.grid(row=3, column=5, padx=5, pady=5)
    booking_id_entry = tk.Entry(form)
    booking_id_entry.grid(row=4, column=5, padx=20, pady=20)

    bill_date_label = tk.Label(form, text="Bill Date:" , font=('Serif', 14), bg='#c6e9fe')
    bill_date_label.grid(row=5, column=5, padx=1, pady=5)
    bill_date_entry = tk.Label(form, text=date.today(),bg='#c6e9fe',foreground='Red')
    bill_date_entry.grid(row=6, column=5, padx=1, pady=20)

    check_button = tk.Button(form, text="Submit",font=("Courier", 12), height=1, width=8, command=check_details)
    check_button.grid(row=8, column=5, padx=5, pady=5)

    form.mainloop()


#------------------------END OF CODE------------------------
#------------------------ALL FUNCTIONS CALL VIA MAIN FILE-----------------------
