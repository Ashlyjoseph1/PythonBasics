from json import *
with open("countries.json",encoding="utf-8") as f:
    data=load(f)
# print(data)
print(len(data))
print(data[0])

# print capital of chaina

country_detail=[country.get("capital")for country in data if country["name"]=="China"]
print(country_detail)

# print population of china

country_pop=[country.get("population")for country in data if country["name"]=="China"]
print(country_pop)

# currency of ukraine

# country_curr=[country.get("currencies")for country in data if country["name"]=="Ukraine"]
# print(country_curr)

country_curr=[country.get("currencies")for country in data if country["name"].lower()=="ukraine"]
print(country_curr.pop().pop().get("name"))


# languages of india

country_lang=[country["languages"]for country in data if country["name"].lower()=="india"].pop()
print(country_lang)
language_name=[lan["name"]for lan in country_lang]
print(language_name)

# another method using two if...

languages=[lang["name"]for country in data for lang in country["languages"]if country["name"].lower()=="india" ]
print(languages)

# borders of ukraine all countries
ukn_border=[country["borders"]for country in data if country["name"].lower().startswith("ukrai")][0]
print(ukn_border)

# print full name of ukraine/all countries

cntry_border=[country["borders"]for country in data if country["name"].lower().startswith("ukrai")][0]
border_shairing_countries=[country["name"]for country in data if country["alpha3Code"]in cntry_border]
print(border_shairing_countries)


# print highest populated contry
max_pop=max(data,key=lambda country:country["population"])
print(max_pop["name"])

# print countries whose language is english

eng_lang_country=[country["name"]for country in data for lan in country["languages"] if lan["name"].lower()=="english"]
print(eng_lang_country)