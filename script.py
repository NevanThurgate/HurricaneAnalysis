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


# turns damage costs into floats
def return_damages(damages):
    final_list = []
    for damage in damages:
        if 'Damages not recorded' == damage:
            final_list.append(damage)
        elif damage[-1] == 'M':
            final_list.append(float(damage[:-1]) * 1000000)
        elif damage[-1] == 'B':
            final_list.append(float(damage[:-1]) * 1000000000)
    return final_list

# organize hurricanes into dictionaries with each lists' variables as keys
def construct_hurricane(names=names, months=months, years=years, max_sustained_winds=max_sustained_winds, areas_affected=areas_affected, damages=return_damages(damages), deaths=deaths):
    hurricane_dict = []
    for index in range(0, len(names)):
        hurricane_dict.append({
            'name': names[index], 
            'month': months[index], 
            'year': years[index], 
            'maximum sustained winds': max_sustained_winds[index],
            'areas affected': areas_affected[index],
            'damages': damages[index],
            'deaths': deaths[index]
            })
    return hurricane_dict


# creates a dictionary with areas on keys and how many times that area was affected as a value
def count_areas_affected(areas_affected):
    areas_affected_count = {}
    for areas in areas_affected:
        for area in areas:
            if area in areas_affected_count:
                count = areas_affected_count.pop(area)
                count += 1
                areas_affected_count.update({area: count})
            else:
                areas_affected_count.update({area: 1})
    return areas_affected_count



# returns a dictionary with areas as keys and how many times they've been hit as int values
def area_most_effected(areas_affected_count):
    biggest_count = 0
    most_affected_area = ''
    for area, count in areas_affected_count.items():
        if count > biggest_count:
            biggest_count = count
            most_affected_area = f'{area} was hit the most at {count} times'
    return most_affected_area




# returns a dictionary with the name of the hurricane with the highest death count as a key and the integer value of deaths as the value
def biggest_death_count(names, deaths):
    hurricane_highest_death_count = ''
    highest_death_count = 0
    for i in range(0, len(names)):
        if deaths[i] > highest_death_count:
            hurricane_highest_death_count = names[i]
            highest_death_count = deaths[i]
    return f'Hurricane {hurricane_highest_death_count} killed the most people causing {highest_death_count} deaths.'
            

    
# organizes hurricanes into dictionary based on a mortality scale
def mortality_ranked(hurricane_dict):
    mortality_scale = {0: [],
                       1: [],
                       2: [],
                       3: [],
                       4: [],
                       5: []}
    for hurricane in hurricane_dict:
        if hurricane['deaths'] == 0:
            mortality_scale[0].append(hurricane)
        elif hurricane['deaths'] <= 100:
            mortality_scale[1].append(hurricane)
        elif hurricane['deaths'] <= 500:
            mortality_scale[2].append(hurricane)
        elif hurricane['deaths'] <= 1000:
            mortality_scale[3].append(hurricane)
        elif hurricane['deaths'] <= 10000:
            mortality_scale[4].append(hurricane)
        elif hurricane['deaths'] > 10000:
            mortality_scale[5].append(hurricane)
    return mortality_scale



        

# prints a string with the hurricane that caused the most damages and what those damages cost
def biggest_cost(names, damages):
    hurricane_highest_damage_count = ''
    highest_cost = 0
    for i in range(0, len(names)):
        if damages[i] == 'Damages not recorded':
            pass
        elif damages[i] > highest_cost:
                hurricane_highest_damage_count = names[i]
                highest_cost = damages[i]
    return f'Hurricane {hurricane_highest_damage_count} caused the most damage at ${highest_cost}.'



# ranks hurricane damage into 5 keys 
def damage_ranked(hurricane_dict):
    damage_scale = {0: [],
                    1: [],
                    2: [],
                    3: [],
                    4: [],
                    5: []}
    for hurricane in hurricane_dict:
        if hurricane['damages'] == 'Damages not recorded':
            continue
        elif hurricane['damages'] == 0:
            damage_scale[0].append(hurricane)
        elif hurricane['damages'] <= 100000000:
            damage_scale[1].append(hurricane)
        elif hurricane['damages'] <= 1000000000:
            damage_scale[2].append(hurricane)
        elif hurricane['damages'] <= 10000000000:
            damage_scale[3].append(hurricane)
        elif hurricane['damages'] <= 50000000000:
            damage_scale[4].append(hurricane)
        elif hurricane['damages'] > 50000000000:
            damage_scale[5].append(hurricane)
    return damage_scale







