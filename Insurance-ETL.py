import mysql.connector
import pandas as pd
from google.cloud import bigquery

proj = 'health-insurance-422323'
dataset = 'Data'
target_table = 'insurance_table'
table_id = f'{proj}.{dataset}.{target_table}'

#data connections
conn = mysql.connector.connect(read_default_file='C:/Users/19523/Downloads/.my1.cnf')
client=bigquery.Client(project=proj)

#sql query
query = """SELECT * FROM `health_insurance`.`insurance`"""

#extract data
df=pd.read_sql(query,conn)

#transform data
# Function to categorize age into age groups
def age_category(age):
    if age <= 20:
        return '1-20'
    elif age <= 30:
        return '21-30'
    elif age <= 40:
        return '31-40'
    elif age <= 50:
        return '41-50'
    elif age <= 60:
        return '51-60'
    else:
        return '60+'

# Function to categorize BMI into BMI categories
def bmi_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi <= 24.9:
        return 'Healthy Weight'
    elif 25.0 <= bmi <= 29.9:
        return 'Overweight'
    else:
        return 'Obese'
# Function to categorize the number of children
def categorize_children(children):
    if children == 0:
        return '0'
    elif children == 1:
        return '1'
    elif children == 2:
        return '2'
    else:
        return '3+'


df['age_group'] = df['age'].apply(age_category)
df['bmi_category'] = df['bmi'].apply(bmi_category)
df['children_group'] = df['children'].apply(categorize_children)
#load data
job_config=bigquery.LoadJobConfig(
     autodetect=True,
     write_disposition='WRITE_TRUNCATE'
)

load_job=client.load_table_from_dataframe(
     df,
     table_id,
     job_config=job_config
)

load_job.result()

#checking how many records were loaded
dest_table=client.get_table(table_id)
print(f"There are {dest_table.num_rows}rows in the table")
