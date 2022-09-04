import pandas as pd

def calculate_demographic_data(print_data = True):
  # Read data from file
  df = None

  # How many of each race are represented in this dataset? This should be a list of integers.
  race_count = None

  # What is the average age of men?
  average_age_men = None

  percentage_bachelors = None
  higher_education = None
  lower_education = None

  # percentage with salary >50K
  higher_education_rich = None
  lower_education_rich = None

  # What is the minimum number of hours a person works per week (hours-per-week feature)?
  min_work_hours = None

  # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  num_min_workers = None

  rich_percentage = None

  # Identify the most popular occupation for those who earn >50K in India. 
  top_IN_occupation = None

  # DO NOT MODIFY BELOW THIS LINE

  if print_data:
    print("Number of each race:\n", race_count)
    print("Average age of men:", average_age_men)
    print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
    print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
    print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
    print(f"Min work time: {min_work_hours} hours/week")
    print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
    print("Top occupations in India:", top_IN_occupation)

  return {'race_count': race_count, 'average_age_men': average_age_men, 'percentage_bachelors': percentage_bachelors, 'higher_education_rich': higher_education_rich, 'lower_education_rich': lower_education_rich, 'min_work_hours': min_work_hours, 'rich_percentage': rich_percentage, 'top_IN_occupation': top_IN_occupation}