# import os
import psycopg2

conn = psycopg2.connect(
    '''host=ec2-54-225-241-25.compute-1.amazonaws.com dbname=d4mmfd28jhu33d user=pkvdgzetxertgh password=8ea6dd1dda6f7b947adf2a378d2494bed62cd58e7b3bf14baa55a16117a2ce90''')
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS loan_history(
    loan_ID integer PRIMARY KEY,
    Status_Checking_Acc text,
    Duration_in_Months integer,
    Credit_History text,
    Purposre_Credit_Taken text,
    Credit_Amount integer,
    Savings_Acc text,
    Years_At_Present_Employment text,
    Inst_Rt_Income integer,
    Marital_Status_Gender text,
    Other_Debtors_Guarantors text,
    Current_Address_Yrs integer,
    Property text,
    Age integer,
    Other_Inst_plans text,
    Housing text,
    Num_CC integer,
    Job text,
    Dependents integer,
    Telephone text,
    Foreign_Worker text,
    Default_On_Payment integer,
    Count integer
)
""")

conn.commit()
