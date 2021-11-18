import pandas as pd
import numpy as np
from pathlib import Path
import os


if __name__ == '__main__' :

    sal = pd.read_csv('C:\\Users\\Lopez\\Documents\\Scripts\\SmoothStack\\Cohort-Assignments\\Assignment 6\\resources\\Salaries.csv')
    
    print("Head of Dataframe:\n\n{}\n\n".format(sal.head(n = 13)) )

    print("info() : \n\n")
    print(sal.info())

    print(f"\n\navg of base pay = {sal['BasePay'].sum() / sal['BasePay'].count()}\n\n")

    print(f"max overtime pay = {sal['OvertimePay'].max()}\n\n")

    index = np.where(sal["EmployeeName"] == 'JOSEPH DRISCOLL')

    print(f"job title of JOSEPH DRISCOLL : {sal.at[index[0][0], 'JobTitle']}\n\n")

    print(f"base pay of JOSEPH DRISCOLL : {sal.at[index[0][0], 'TotalPay']}\n\n")

    index = np.where(sal['TotalPay'] == sal['TotalPay'].max())

    print(f"highest paid person\n\n{ sal.loc[index[0][0]] }\n\n")

    index = np.where(sal['TotalPay'] == sal['TotalPay'].min())

    print(f"lowest paid person\n\n{ sal.loc[index[0][0]] }\n\n")
    
    byYear = sal.groupby('Year')

    print(f"Avg base pay by year : {byYear.mean()}\n\n")

    byJob = sal.groupby('JobTitle')

    byJob = byJob.count()

    byJob.rename(columns = {'id' : 'count'}, inplace = True)

    print(f"Amount of unique jobs : {len(byJob.index)}\n\n")

    print(f"Top 5 most common jobs :\n\n {byJob.sort_values(by = 'Id', ascending = False)[0:5]}\n\n")


    year_2013 = sal.loc[sal['Year'] == 2013]

    by_job_title = year_2013.groupby('JobTitle')

    print("Amount of job titles that were represented by only one person in 2013: {}\n\n".format( len(by_job_title.count().loc[by_job_title.count()['Id'] == 1].index) ) ) 
    

    chief = sal['JobTitle']
    
    count = 0

    for i in chief:
        if 'Chief' in i:
            count += 1

    print("Amount of people that have the word Chief in their job title: {}\n\n".format(count))