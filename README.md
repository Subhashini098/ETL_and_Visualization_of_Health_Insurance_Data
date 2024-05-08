# ETL and Visualization of Health Insurance Data
In this project, I conducted Extract, Transform, and Load (ETL) operations on health insurance data sourced from Kaggle and performed visualization. 

# Dataset details
This dataset contains information on the relationship between personal attributes (age, gender, BMI, family size, smoking habits), geographic factors, and their impact on medical insurance charges. It can be used to study how these features influence insurance costs and develop predictive models for estimating healthcare expenses.

Age: The insured person's age.

Sex: Gender (male or female) of the insured.

BMI (Body Mass Index): A measure of body fat based on height and weight.

Children: The number of dependents covered.

Smoker: Whether the insured is a smoker (yes or no).

Region: The geographic area of coverage.

Link for dataset-https://www.kaggle.com/datasets/willianoliveiragibin/healthcare-insurance

# Tools Utilized
MySQL Database: Used for storing and managing the dataset.

Python Pandas: Employed for data manipulation and ETL operations.

BigQuery: Utilized as a data warehouse for storing Data.

Tableau: Used for data visualization and analysis.

# Project steps
1. Transferred data into MySQL Database and stored it in the form of tables.
   ![Screenshot (1112)](https://github.com/Subhashini098/Health_Insurance_Analysis/assets/109629881/c7ec48c1-862c-4c83-9bfb-39ec65d67d51)

2. Utilized MySQL connector to establish a connection between the Python environment and the MySQL database.
3. Employed Python Pandas to perform ETL operations on the dataset.
4. Loaded the transformed dataset into the BigQuery data warehouse.
  ![Screenshot (1121)](https://github.com/Subhashini098/Health_Insurance_Analysis/assets/109629881/fac27c4b-adb5-4d3f-8984-d4dc1cbb4860)
 
5. Connected the transformed data present in BigQuery to Tableau for data visualization and analysis.
  ![Dashboard 1 (2)](https://github.com/Subhashini098/ETL_and_Visualization_of_Health_Insurance_Data/assets/109629881/12557107-c446-440a-979c-39ab4c35a5db)


   
Link for Visualization-https://public.tableau.com/app/profile/subhashini2849/viz/HealthInsuranceDashboard_17148858803120/Dashboard1?publish=yes
