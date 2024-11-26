import pandas as pd

# Load the dataset
data = pd.read_csv('C:/Users/johnn/COVID-19-Data-Analysis/data/owid-covid-data.csv')

# Filter for relevant columns
columns_to_keep = [
    'date', 'country', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 
    'population', 'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated'
]
covid_data = data[columns_to_keep]

# Add calculated columns (e.g., cases per 100k population)
covid_data['cases_per_100k'] = (covid_data['total_cases'] / covid_data['population']) * 100000
covid_data['deaths_per_100k'] = (covid_data['total_deaths'] / covid_data['population']) * 100000

# Save the processed data to a new file
output_file = 'C:/Users/johnn/COVID-19-Data-Analysis/data/processed_covid_data.csv'
covid_data.to_csv(output_file, index=False)

print(f"Data processed and saved to {output_file}")