
# Countries informations 

# Short cut path: python /Users/mateussfeir/Desktop/Python/GPT\ Project\ stock\ market/Countries_infs_api.py


import requests
import locale

chosen_country = input('Choose the requested country: ').capitalize()
url = f'https://restcountries.com/v2/name/{chosen_country}'
response = requests.get(url)

data = response.json()[0]

population = data['population']
area = data['area']

# Set the locale to the user's default
locale.setlocale(locale.LC_ALL, '')
# Format the population with the user's default grouping
formatted_population = locale.format_string('%d', population, grouping=True)
formatted_area = locale.format_string('%d', area, grouping=True)

print(f'The population of {chosen_country} is {formatted_population} people.')
print(f'{chosen_country} has an area of {area} Km.')
print(f'Population density: {(population/area):.2f} people per square kilometer.')
