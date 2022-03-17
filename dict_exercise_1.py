
# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
conversion = {"M": 1000000, "B": 1000000000}
def damages_to_values(damages):
    converted = [float(damage[:-1]) * conversion.get(damage[-1]) if damage[-1] == "M" or damage[-1] == "B" else damage for damage in damages]
    return converted

damages = damages_to_values(damages)

# write your construct hurricane dictionary function here:
def hurricane_dic(Name, Month, Year, Max_Sustained_Wind, Areas_Affected, Damage, Death):
    hurricanes = {}
    for i in range(len(Name)):
        data = {
            "Name": Name[i],
            "Month": Month[i],
            "Year": Year[i],
            "Max Sustained Wind": Max_Sustained_Wind[i],
            "Areas Affected": Areas_Affected[i],
            "Damage": Damage[i],
            "Death": Death[i]
        }
        hurricane = {Name[i]: data}
        hurricanes.update(hurricane)
    return hurricanes

# write your construct hurricane by year dictionary function here:

def hurricanes_by_year(year):
    indices = [i for i, x in enumerate(years) if x == year]
    hurricanes = hurricane_dic(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
    hurricanes_in_year = [hurricanes.get(names[index]) for index in indices]
    return hurricanes_in_year

# write your count affected areas function here:

from itertools import chain

def areas_count(areas_affected):
    areas_listed = list(chain.from_iterable(areas_affected))
    areas_count = {item: areas_listed.count(item) for item in set(areas_listed)}
    return areas_count

# write your find most affected area function here:

def max_area(areas_affected):
    areas_number = areas_count(areas_affected)
    max_area = ""
    max_area_count = 0

    for k, v in areas_number.items():
        if v > max_area_count:
            max_area_count = v
            max_area = k
    return max_area, max_area_count

# write your greatest number of deaths function here:

def max_deaths(deaths):
    i = deaths.index(max(deaths))
    return names[i], max(deaths)

# write your catgeorize by mortality function here:
def mortality(names, deaths):
    hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
    for name, death in zip(names, deaths):
        if death == 0:
            hurricanes_by_mortality[0].append(name)
        elif death <= 100:
            hurricanes_by_mortality[1].append(name)
        elif death <= 500:
            hurricanes_by_mortality[2].append(name)
        elif death <= 1000:
            hurricanes_by_mortality[3].append(name)
        elif death <= 10000:
            hurricanes_by_mortality[4].append(name)
    return hurricanes_by_mortality

# write your greatest damage function here:

def greatest_damage(damages):
    damages_numbers = [int(x) for x in damages if type(x) == float]
    i = damages.index(max(damages_numbers))
    return names[i], max(damages_numbers)

# write your catgeorize by damage function here:

def hurricanes_by_damage(names, damages):
    hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[]}
    damages_numbers = [int(x) for x in damages if type(x) == float]
    for name, damage in zip(names, damages_numbers):
        if damage == 0:
            hurricanes_by_damage[0].append(name)
        elif damage <= 100000000:
            hurricanes_by_damage[1].append(name)
        elif damage <= 1000000000:
            hurricanes_by_damage[2].append(name)
        elif damage <= 10000000000:
            hurricanes_by_damage[3].append(name)
        elif damage <= 50000000000:
            hurricanes_by_damage[4].append(name)
    return hurricanes_by_damage
