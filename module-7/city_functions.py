# Scott Macioce
# Module 7 - city_functions.py
# Purpose: Define a function that formats and returns City, Country - population xxx, Language

def city_country(city, country, population=None, language=None):
    # Return a string in the form City, Country, optionally with population and language.
    if population and language:
        return f"{city.title()}, {country.title()} - population {population}, {language.title()}"
    elif population:
        return f"{city.title()}, {country.title()} - population {population}"
    elif language:
        return f"{city.title()}, {country.title()}, {language.title()}"
    else:
        return f"{city.title()}, {country.title()}"

# Example calls to the function:
print(city_country('santiago', 'chile'))
print(city_country('berlin', 'germany', 3769000))
print(city_country('nairobi', 'kenya', 4397000, 'swahili'))