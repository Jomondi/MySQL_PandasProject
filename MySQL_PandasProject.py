# You, your name here [] been hired by a reputable company in Maputo with branches in
# Johannesburg and headquartered in Nairobi with several employees in an en Excel spreadsheet.
# Please import the attached spreadsheet using pandas into a DataFrame - Clean the Data, and import
# the data into a MySQL Database. Disclaimer - The datasets are generated through random logic in
# VBA. These are not real human resource data and should not be used for any other purpose other
# than testing. Separate the Spreadsheet programmatically into 2 separate worksheets.
# 1]: Identified as Authentication and the
# 2]: Employee Records. In the Authentication Tab include the records for Username and Password,
# in the Employee Records put the rest of the records except for Last % Hike. Good Luck

from sqlalchemy import create_engine
import pandas as pd
import mysql.connector


def create_database():
    database = mysql.connector.connect(host='localhost', user='root', password='FidelliaAdhiambo')
    cursor = database.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS Employees")
    print('Database successfully created!')
    print('\n')


create_database()


# Connect to MySQL database engine
engine = create_engine("mysql+pymysql://root:FidelliaAdhiambo@localhost/Employees")
print(f'Connected to database successfully!\n')


# Read the username/password columns of the excel file, convert it into a dataframe and print the head/tail
def authentication_data():
    doc = pd.read_excel('100 Records.xlsx', usecols='AJ, AK')
    doc_df = pd.DataFrame(doc)
    print(f'--------Column Details--------- \n\n{doc_df}\n')
    doc_df.to_sql('Authentication', con=engine, if_exists='replace')


authentication_data()


# Read the other columns of the excel file, convert it into a dataframe and print the head/tail
# Skip column AA
def employee_data():
    doc = pd.read_excel('100 Records.xlsx', usecols='A:Z, AB:AI',)
    doc_df = pd.DataFrame(doc)
    print(f'------------------------Column Details------------------------ \n\n{doc_df}\n')
    doc_df.to_sql('Employee_Records', con=engine, if_exists='replace')


employee_data()
