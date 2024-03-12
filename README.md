# CAR-RENTAL-MENAGEMENT-SYSTEM
The Car Rental Management System (CRMS) is a database-driven application that facilitates the management of a car rental business. The system allows customers to book cars, handles billing details, and manages car information, customer details, and booking history. This README file provides a detailed overview of the system.

## TABLE OF CONTENTS

1. **Prerequisites**
2. **Database Details**
3. **Getting Started**
4. **Features**
5. **Screenshots**
6. **Contributing**
7. **License**
8. **Acknowledgments**

## PREREQUISITES
Python: Make sure you have Python installed on your system. If not, you can download it from the official Python website.

Microsoft SQL Server Management Studio: Ensure that you have Microsoft SQL Server Management Studio installed on your system to manage the database.

`Note: You must have Microsoft SQL Server Management Studio and Python installed`

## DATABASE DETAILS
The Car Rental Management System uses a Microsoft SQL Server database named "CRMS" to store and manage data. Before running the application, ensure you have created the database.

  A. **Database Name:**
      CRMS
      
  B. **Database Schema:**
      ![RDBMS DIAGRAM](/RDBMS%20DIAGRAM.png)
      
  C. **Sample Data Insertion:**
      For demonstration purposes, sample data has been inserted into the CAR_CATEGORY and CAR_DETAILS tables. However, in a real-world application, this data 
      would be dynamically managed based on the inventory and customer preferences.
      
  D. **Important Notes:**
      This database script is intended for demonstration purposes and may require modifications and optimizations to suit specific production environments.
      Ensure to handle sensitive customer data securely and comply with data protection regulations. Always back up your database regularly to prevent data loss.

## GETTING STARTED

  A. **Installation:**
  
      a. Clone the repository to your local machine using the following command: 
      
          ```bash
          git clone https://github.com/MehmoodSheikh/CAR-RENTAL-MANAGEMENT-SYSTEM.git
          ```
      
      b. Install the required Python modules by running the following command:
      
          ```bash
          pip install -r requirements.txt
          ```
      
  B. **Usage:**

      a. In 'FE_Con.py' file, Replace <Your-Server-Name-Here> with server name you are running on your local machine,
        
          ```bash
          connection = pyodbc.connect('Driver={SQL Server};' 'Server=<Your-Server-Name-Here>;' 
          'Database=CRMS;' 'Trusted_connection=yes;')
          ```

      b. Open 'DATABASE.sql' with Microsoft SQL Server Management Studio and execute the script to create the database, tables, and insert data.

      c. Run the frontend of the application using the following command:
      
            ```bash
            python PAGE1.py
            ```
  
## FEATURES
The Car Rental Management System (CRMS) offers several essential features to efficiently manage a car rental business. Some of the key features of this system include:

A. **Customer Information Management:** The system allows the storage and management of customer details, such as names, contact information, address, and driving license numbers. This feature facilitates easy retrieval of customer information for booking and billing purposes.

B. **Car Category Management:** CRMS enables the creation and management of different car categories, specifying the number of persons each category can accommodate and the cost per day for renting a car in each category. This helps customers choose the right car based on their requirements and budget.

C. **Car Inventory Management:** The system maintains a comprehensive record of available cars, including their registration numbers, make, model, and the category they belong to. This feature ensures efficient management of the car fleet and assists in assigning cars to bookings.

D. **Booking and Rental Management:** CRMS allows customers to book cars for specific rental dates, specifying the date of pickup and return. The system ensures that there are no conflicts in the booking schedule and helps manage the rental duration.

E. **Billing and Payment Management:** The system generates billing details for each booking, calculating the total amount based on the rental duration and the car's category. It also provides a mechanism for accepting payments from customers.

F. **Data Integrity and Constraints:** The database schema includes various constraints to ensure data integrity, such as unique constraints on phone numbers and national identity card numbers, primary keys for each table, and foreign key references between related tables.

G. **Sample Data Insertion:** The system includes sample data insertion to demonstrate the functionality of the application. However, in a real-world scenario, data insertion and management would be dynamically handled based on actual customer bookings and available cars.

H. **Scalability:** The system's database design and structure are scalable, allowing the addition of new car categories, cars, customers, and bookings as the business expands.

I. **Security Considerations:** While not explicitly mentioned in the provided code snippet, a real-world implementation of CRMS would consider security measures to protect customer data, prevent unauthorized access, and ensure data privacy compliance.

J. **User Interface:** In a complete implementation, CRMS would feature a user-friendly graphical interface that enables customers to interact with the system easily and allows staff to manage bookings, view reports, and handle administrative tasks efficiently.
   
## SCREENSHOTS
The "INTERFACE AND MSGS SNAP SHOTS" folder contains screenshots of the Car Rental Management System application. These images provide visual representations of the user interface, Error messages and demonstrate how to interact with the system effectively.

## CONTRIBUTING
We welcome contributions from the community! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## LICENSE
The Car Rental Management System is released under the MIT License. Feel free to use, modify, and distribute the codebase according to the terms of the license.

## ACKNOWLEDGMENTS
The Car Rental Management System was developed as part of a project and is provided here as a simplified representation. Any real-world implementation may require additional features, security measures, and scalability considerations.

