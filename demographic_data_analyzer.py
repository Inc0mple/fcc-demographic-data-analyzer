import pandas as pd
import numpy as np

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    df_total = len(df.index)
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    age_gender_df = df[["age","sex"]]
    male_age_df = age_gender_df[age_gender_df["sex"] == "Male"]["age"]
    average_age_men = round(male_age_df.mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    edu_df = df["education"]
    percentage_bachelors = round(((edu_df == "Bachelors").sum()/df_total)*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    advanced_bool =  ((edu_df == "Bachelors") | (edu_df == "Masters") | (edu_df == "Doctorate"))
    advanced_total = advanced_bool.sum()
    earners_bool = (df["salary"] == ">50K")
    advanced_earners = df[advanced_bool & earners_bool]

    # What percentage of people without advanced education make more than 50K?
    basic_bool = ~advanced_bool
    basic_earners = df[basic_bool & earners_bool]

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = advanced_total
    lower_education = basic_bool.sum()

    # percentage with salary >50K
    higher_education_rich = round((len(advanced_earners)/advanced_total)*100,1)
    lower_education_rich = round((len(basic_earners)/basic_bool.sum())*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = (df["hours-per-week"] == min_work_hours).sum()
    
    rich_percentage = (((earners_bool) & (df["hours-per-week"] == min_work_hours)).sum()/num_min_workers) * 100
    
    # What country has the highest percentage of people that earn >50K?
    country_salary_df = df[["native-country","salary"]]
    rich_by_country_df = country_salary_df[country_salary_df["salary"] == ">50K"]
    country_values = country_salary_df["native-country"].value_counts()
    rich_by_country_values = (rich_by_country_df["native-country"].value_counts())
    highest_earning_country_percentage = round(((rich_by_country_values/country_values)*100).max(),1)
    highest_earning_country = ((rich_by_country_values/country_values)*100).sort_values(ascending = False).index[0]

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df["native-country"] == "India") & (df["salary"] == ">50K")].occupation.value_counts().index[0]


    # DO NOT MODIFY BELOW THIS LINE
    
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)
    
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }