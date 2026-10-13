import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data
    df = pd.read_csv('adult.data.csv')

    # 1. Count of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(
        df[df['sex'] == 'Male']['age'].mean(), 1
    )

    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1
    )

    # 4. Higher education salary percentage
    higher_education = df[
        df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    ]
    lower_education = df[
        ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    ]

    higher_education_rich = round(
        (higher_education['salary'] == '>50K').mean() * 100, 1
    )
    lower_education_rich = round(
        (lower_education['salary'] == '>50K').mean() * 100, 1
    )

    # 5. Minimum working hours
    min_work_hours = df['hours-per-week'].min()

    # 6. Percentage of people working minimum hours who earn >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (num_min_workers['salary'] == '>50K').mean() * 100, 1
    )

    # 7. Country with highest percentage earning >50K
    country_salary = df.groupby('native-country')['salary'].apply(
        lambda x: (x == '>50K').mean() * 100
    )
    highest_earning_country = country_salary.idxmax()
    highest_earning_country_percentage = round(
        country_salary.max(), 1
    )

    # 8. Most popular occupation among people in India earning >50K
    india_rich = df[
        (df['native-country'] == 'India') &
        (df['salary'] == '>50K')
    ]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    # Return results
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelor's degree:", percentage_bachelors)
        print("Higher education earning >50K:", higher_education_rich)
        print("Lower education earning >50K:", lower_education_rich)
        print("Minimum hours worked:", min_work_hours)
        print("Minimum-hours workers earning >50K:", rich_percentage)
        print("Country with highest salary percentage:", highest_earning_country)
        print("Percentage:", highest_earning_country_percentage)
        print("Top occupation in India earning >50K:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


from demographic_data_analyzer import calculate_demographic_data

if __name__ == "__main__":
    calculate_demographic_data()