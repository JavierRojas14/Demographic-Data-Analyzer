import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    personas_con_bachelor = df.loc[df['education'] == 'Bachelors'].shape[0]
    total_de_personas = df.shape[0]
    percentage_bachelors = round((personas_con_bachelor / total_de_personas) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = (df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')
    total_personas_higher = df[higher_education].shape[0]
    lower_education = ~ ((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))
    total_personas_lower = df[lower_education].shape[0]

    # percentage with salary >50K
    higher_education_50k = (higher_education) & (df['salary'] == '>50K')
    lower_education_50k = (lower_education) & (df['salary'] == '>50K')

    higher_education_rich = round((df[higher_education_50k].shape[0] / total_personas_higher) * 100, 1)
    lower_education_rich = round((df[lower_education_50k].shape[0] / total_personas_lower) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    mask = (df['hours-per-week'] == df['hours-per-week'].min()) & (df['salary'] == '>50K')
    total_personas = df[df['hours-per-week'] == df['hours-per-week'].min()].shape[0]

    rich_percentage = (df[mask].shape[0] / total_personas) * 100

    # What country has the highest percentage of people that earn >50K?
    mask_paises_con_mas_de_50K = df['salary'] == '>50K'
    paises_con_mas_de_50K = df[mask_paises_con_mas_de_50K]['native-country'].value_counts().index

    porcentajes_totales = {}
    for pais in paises_con_mas_de_50K:
        personas_pais_totales = df[df['native-country'] == pais].shape[0]

        mask = (df['native-country'] == pais) & (df['salary'] == '>50K')
        personas_pais_50K = df[mask].shape[0]

        porcentaje = (personas_pais_50K / personas_pais_totales) * 100

        porcentajes_totales[pais] = porcentaje

    porcentajes_totales = pd.Series(porcentajes_totales)
    porcentajes_totales = porcentajes_totales.sort_values()

    highest_earning_country = porcentajes_totales.index[-1]
    highest_earning_country_percentage = round(porcentajes_totales[-1], 1)

    # Identify the most popular occupation for those who earn >50K in India.
    mask = (df['salary'] == '>50K') & (df['native-country'] == 'India')

    top_IN_occupation = df[mask]['occupation'].value_counts().index[0]

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
