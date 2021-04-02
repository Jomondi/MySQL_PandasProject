# Exercise Description
i. Import the attached spreadsheet using pandas into a DataFrame - Clean the Data, and import the data into a MySQL Database. 

ii. Separate the Spreadsheet programmatically into 2 separate worksheets as below: 
        a) Identified as Authentication. In the Authentication Tab include the records for Username and Password. 
        
        b) Employee Records. Put the rest of the records except for 'Last % Hike'.
        

# Exercise Resolution
User must have below installed so as to successfully run this program
 - Python and Interpreter
 - pip install xlrd and all other other needed imports
 - MySQL and MySQL Workbench
 
 Run below methods:
  create_database()
      Run thist method to create the MySQL database and print the results.
      
  Connect to the engine using SQLAlchemy
  
  authentication_data()
      Run this method to add the data to the authentication table and print the results.
      
  employee_data()
      Run this method to add the data to the authentication table and print the results.
