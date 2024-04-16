
import pandas as pd
import numpy as np


def get_state(x):
    x = x.split('_')[0]
    return x

def get_column(x):
    x = x.replace('!!', "_")
    x = x.replace(' ', "_")
    x = x.replace('Estimate', "")
    return x

def get_index(x):
    x = x.replace('_Total_', '')
    return x

def total_column(x):
    x = x.replace('!!Estimate', "")
    return x

def male_column(x):
    x = x.replace('!!Estimate', "_Male_")
    return x

def female_column(x):
    x = x.replace('!!Estimate', "_Female_")
    return x

def short_column(x):
    x = " ".join(x.split())
    x = x.replace(':', "")
    return x



def state_abbrev_mapping(df, col, output_abbr = False, add_new_col = False, new_col = None,  case = None):
    #df =  the Pandas dataframe.
    #col = String. The column with the state name or abbreviation you wish to use
    #output_abbr = True/False. Do you want to the output to the the state abbreviation? The other option is the state full name.
    #add_new_col = True/False. Do you want to add a new column? The new column will overwrite the inputted column if not.
    #new_col = String. Name of new column you wish to add.
    #case = 'upper', 'lower', or None. Do you want to specify a letter-case for the data?
 
    #List of states
    state2abbrev = {
        'Alaska': 'AK',
        'Alabama': 'AL',
        'Arkansas': 'AR',
        'Arizona': 'AZ',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'District of Columbia': 'DC',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Iowa': 'IA',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Massachusetts': 'MA',
        'Maryland': 'MD',
        'Maine': 'ME',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Missouri': 'MO',
        'Mississippi': 'MS',
        'Montana': 'MT',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Nebraska': 'NE',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'Nevada': 'NV',
        'New York': 'NY',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Virginia': 'VA',
        'Vermont': 'VT',
        'Washington': 'WA',
        'Wisconsin': 'WI',
        'West Virginia': 'WV',
        'Wyoming': 'WY',
        'Puerto Rico': 'PR',
        'Virigin Islands': 'VI'
    }
 
    #List of states
    abbrev2state = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming',
        'PR': 'Puerto Rico',
        'VI': 'Virigin Islands'
    }
     
    #If user wants to add a new column
    if add_new_col == False:
         
        #Is the output an abbreviation?
        if output_abbr == True:
            df[col] = df[col].str.strip().replace(state2abbrev)
        else:
            df[col] = df[col].str.strip().replace(abbrev2state)
             
        #Does the user want a specific case sensitivity?
        if case == 'upper':
            df[col] = df[col].str.upper()
        elif case == 'lower':
            df[col] = df[col].str.lower()
             
    #If user not want to add a new column       
    if add_new_col == True:
         
        #If new column name is missing
        if new_col == None:
            #Prompt user to enter a new column name
            print("Error: You requested to add a new column but did not specify a new column name. Please add a column name with new_col = ''")
            return()
         
        #Is the output an abbreviation?
        if output_abbr == True:
            df[new_col] = df[col].str.strip().replace(state2abbrev)
        else:
            df[new_col] = df[col].str.strip().replace(abbrev2state)
 
        #Does the user want a specific case sensitivity?
        if case == 'upper':
            df[new_col] = df[new_col].str.upper()
        elif case == 'lower':
            df[new_col] = df[new_col].str.lower()
 
    return(df)



df_ppl = pd.read_csv('/Users/melodywang/Documents/umich/courses/SI568/project2/data/acs_population_2022.csv')
df_major = pd.read_csv('/Users/melodywang/Documents/umich/courses/SI568/project2/data/acs_major_2022.csv')
df_income = pd.read_csv('/Users/melodywang/Documents/umich/courses/SI568/project2/data/acs_wage_2022.csv')


df1 = df_ppl.loc[:,~df_ppl.columns.str.contains('united', case=False)]
df1 = df1.loc[:,~df1.columns.str.contains('grouping', case=False)]  

df2 = df_major.loc[:,~df_major.columns.str.contains('united', case=False)]
df2 = df2.loc[:,~df2.columns.str.contains('grouping', case=False)]

data_ba_degree = pd.DataFrame(data=df1)[12:13]
data_ba_major = pd.DataFrame(data=df2)[:6]
data_ba_degree=data_ba_degree.rename(index={12: 'population_over_25_with_BA'})
data_ba_degree = data_ba_degree.rename(columns=get_column)

data_ba_major=data_ba_major.rename(index={0: 'total', 1:'stem', 2: 'stem_related', 3:'business', 4:'education', 5: 'humanities'})
data_ba_major = data_ba_major.rename(columns=get_column)

data_degree_trans = data_ba_degree.T.reset_index(names = "state")
data_major_trans = data_ba_major.T
data_degree_trans=data_degree_trans.set_index(data_major_trans.index)

data_grad = pd.concat([data_degree_trans, data_major_trans], axis=1)

data_trans = pd.DataFrame(data=data_grad)
data_amount = data_trans.iloc[::2]
data_perc = data_trans.iloc[1::2]

# Save data to CSV
data_perc.to_csv('us-population-perc.csv')
data_amount.to_csv('us-population-amount.csv')


# Construct df_income_total
df_income_total = pd.DataFrame(data=df_income)[0:18]
df_income_total = df_income_total.rename(columns=total_column)
df_income_total = df_income_total.set_index(df_income_total.columns[0])

df_income_male = pd.DataFrame(data=df_income)[18:36]
df_income_male = df_income_male.rename(columns=male_column)
df_income_male = df_income_male.set_index(df_income_male.columns[0])
df_income_male = df_income_male.set_index(df_income_total.index)

df_income_female = pd.DataFrame(data=df_income)[36:]
df_income_female = df_income_female.rename(columns=female_column)
df_income_female = df_income_female.set_index(df_income_female.columns[0])
df_income_female = df_income_female.set_index(df_income_total.index)

df_income_female = df_income_female.T
df_income_male = df_income_male.T
df_income_total = df_income_total.T


# Construct data_income_total
data_gender = pd.concat([df_income_female, df_income_male], join="outer")
data_income = pd.concat([df_income_total, data_gender], join="outer")
data_income = data_income.rename(columns=short_column)

data_income_t = data_income.T
data_income_t = data_income_t.rename(columns=get_state)
data_income_total = data_income_t.T.reset_index(names = "state")

# Save data to CSV
data_income_total.to_csv('us-population_income_total.csv', index=False)




# Construct us_income
cols = ['Total', 'Computers, Mathematics and Statistics', 'Biological, Agricultural, and Environmental Sciences', 'Physical and Related Sciences', 'Psychology', 'Social Sciences', 'Engineering','Multidisciplinary Studies', 'Science and Engineering Related Fields', 'Business', 'Education', 'Literature and Languages','Liberal Arts and History', 'Visual and Performing Arts', 'Communications','Other']

for col in cols:
    data_income_total.replace('-',np.NaN)
    try:
        data_income_total[col] = data_income_total[col].replace('-',np.NaN)
        data_income_total[col] = data_income_total[col].str.replace(',', '').astype(float)
    except:     
        data_income_total[col] = data_income_total[col]

state_abbrev_mapping(df = data_income_total,
                     col= 'state',
                     output_abbr = True,
                     add_new_col = True,
                     new_col = 'state_abbrev',
                     case = 'upper')
data_income_total = data_income_total.reset_index().rename(columns={"index":"index"})	
data_income_total.to_csv('us-income.csv')



def calculate_gender_diff_pop(df, field):
    df = df[field].reset_index()
    df[field] = df[field].str.replace(',', '').astype(float)
    df=df.rename(columns={"index": "index", '{}'.format(field): "field"})
    male =  df.iloc[1::3]
    male = male.reset_index()
    female = df.iloc[2::3]
    female = female.reset_index()
    total = df.iloc[0::3]
    total = total.reset_index()


    total['difference'] = male.field.sub(female.field)
    total['gender_diff'] = total.difference / total.field * 100
    total=total.set_index(df_income_total.index[1:])
    total['state'] = total.index
    state_abbrev_mapping(df = total,
                     col= 'state',
                     output_abbr = True,
                     add_new_col = True,
                     new_col = 'state_abbrev',
                     case = 'upper')
    

    return total
      

def calculate_gender_earning(df, field):
    df = df[field].reset_index()
    df=df.rename(columns={"index": "index", '{}'.format(field): "field"})
    male =  df[54:106]
    male = male.reset_index()
    female = df[107:]
    female = female.reset_index()
    total = df.iloc[1:53]
    total = total.reset_index()

    total['difference'] = male.field.sub(female.field)
    total['gender_diff'] = total.difference / total.field * 100
    total=total.set_index(df_income_total.index[1:])
    total['state'] = total.index
    state_abbrev_mapping(df = total,
                     col= 'state',
                     output_abbr = True,
                     add_new_col = True,
                     new_col = 'state_abbrev',
                     case = 'upper')
    return total



def pop_diff(df, field):
    df = df[field].reset_index()
    df=df.rename(columns={"index": "index", '{}'.format(field): "field"})
    male =  df.iloc[1::3]
    male = male.reset_index()
    female = df.iloc[2::3]
    female = female.reset_index()
    total = df.iloc[0::3]
    total = total.reset_index()

    total=total.set_index(df_income_total.index[1:])
    total['state'] = total.index
    state_abbrev_mapping(df = total,
                     col= 'state',
                     output_abbr = True,
                     add_new_col = True,
                     new_col = 'state_abbrev',
                     case = 'upper')
    return total




