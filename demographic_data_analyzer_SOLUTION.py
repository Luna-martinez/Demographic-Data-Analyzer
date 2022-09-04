import pandas as pd

def calculate_demographic_data(print_data = True):
  # Read data from file
  df = pd.read_csv('adult.data.csv')

  # How many of each race are represented in this dataset?
  race_count = df['race'].value_counts()

  # What is the average age of men?
  average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)

  # What is the percentage of people who have a Bachelors degree?
  percentage_bachelors = round(float(((df['education'] == 'Bachelors').sum()) / len(df))*100, 1)

  # What percentage of the people with AND without `education` equal to `Bachelors`, `Masters`, or `Doctorate` also have a `salary` of `>50K` (Note: Every row of data has salary of either '>50K' or '<=50K')?

  # with and without `Bachelors`, `Masters`, or `Doctorate`
  higher_education = df.loc[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
  lower_education = df.loc[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

  # percentage with salary >50K
  higher_education_rich = round((higher_education['salary'] == '>50K').sum() / len(higher_education) * 100, 1)
  lower_education_rich = round((lower_education['salary'] == '>50K').sum() / len(lower_education) * 100, 1)

  # What is the minumum number of hours a person works per week (hours-per-week feature)?
  min_work_hours = df['hours-per-week'].min()

  # What percentage of the people who work the minumum number of hours per week have a salary of >50K?
  num_min_workers = df[df['hours-per-week'] == min_work_hours].shape[0]

  rich_percentage = round((float(df[(df['hours-per-week'] == min_work_hours)
                  & (df['salary'] == '>50K')].shape[0]) / num_min_workers) * 100, 1)

  # What country has the highest percentage of people that earn >50K?
  highest_earning_country = ""
  highest_earning_country_percentage = 0
  for (country), sub_df in df.groupby(['native-country']):
    percentage = len(sub_df[(sub_df['salary'] == '>50K')])/ len(sub_df)
    if highest_earning_country_percentage < percentage:
      highest_earning_country_percentage = round(percentage,3)
      highest_earning_country = country
  highest_earning_country_percentage *= 100
  # Identify the most popular occupation for those who earn >50K in India. 

  top_IN_occupation = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]['occupation'].value_counts().keys()[0]

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

  return {'race_count': race_count, 'average_age_men': average_age_men, 'percentage_bachelors': percentage_bachelors, 'higher_education_rich': higher_education_rich, 'lower_education_rich': lower_education_rich, 'min_work_hours': min_work_hours, 'rich_percentage': rich_percentage, 'top_IN_occupation': top_IN_occupation}