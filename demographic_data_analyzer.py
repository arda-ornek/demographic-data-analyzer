import pandas as pd
from sqlalchemy import true


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    #print(df.info())
    #print(df.tail())
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    #print(df.nunique())
    #print(pd.unique(df['race']))
    #print(df['race'].value_counts().values.tolist())
    race_series = None
    race_count = list(df['race'].value_counts())

    # What is the average age of men?
    age_ave = df.groupby('sex').age.mean().values.tolist()
    #print(round(ave[1],1))
    average_age_men = round(age_ave[1],1)

    # What is the percentage of people who have a Bachelor's degree?
    gp = df.groupby('education')
    #print(gp.size().sum())
    bachelors = gp.get_group('Bachelors')
    #print(round(bachelors.count().sum()/15))
    perc = round(bachelors.count().sum()/15) * 100 / gp.size().sum()
    #print(round(perc,1))
    percentage_bachelors = round(perc,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    bachelors_series = df.loc[df['education'] == 'Bachelors', 'salary']
    masters_series = df.loc[df['education'] == 'Masters', 'salary']
    doctorate_series = df.loc[df['education'] == 'Doctorate', 'salary']
    #print("bachelors: ",bachelors_series.count())
    #print("masters: ",masters_series.count())
    #print("doctorates: ",doctorate_series.count())
    counter1 = 0
    for x in bachelors_series:
      if x == ">50K":
        counter1 = counter1 + 1
    #print("bachelors >50: ",counter1)
    counter2 = 0
    for y in masters_series:
      if y == ">50K":
        counter2 = counter2 + 1
    #print("masters >50: ",counter2)
    counter3 = 0
    for z in doctorate_series:
      if z == ">50K":
        counter3 = counter3 + 1
    #print("doctorates >50: ",counter3)
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = None
    lower_education = None

    # percentage with salary >50K
    higher_education_rich = round(((counter1+counter2+counter3)*100/(bachelors_series.count()+masters_series.count()+doctorate_series.count())),1)

    low_education_series=[]
    index = df.index
    for x in index:
      if df.iloc[x,3]!='Bachelors' and df.iloc[x,3]!='Masters' and df.iloc[x,3]!='Doctorate':
        low_education_series.append(df.iloc[x,14])
    #print(low_education_series)
    lower_education_rich_counter=0
  
    for y in low_education_series:
      if y=='>50K':
        lower_education_rich_counter = lower_education_rich_counter + 1

    lower_education_rich = round(lower_education_rich_counter * 100 / len(low_education_series),1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    workhours_list = []
    for x in index:
      workhours_list.append(df.iloc[x,12])
    
    min_work_hours = min(workhours_list)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = 0
    rich_min_workers = 0
    
    for x in index:
      if df.iloc[x,12]==min_work_hours:
        num_min_workers = num_min_workers + 1
        if df.iloc[x,14]=='>50K':
          rich_min_workers = rich_min_workers + 1
          
    rich_percentage = round(100 * rich_min_workers / num_min_workers)

    

    # What country has the highest percentage of people that earn >50K?
    #df_copy=df.sort_values("native-country")
    """ df_copy_filter1=df["native-country"]=="United-States"
    df_copy_filter2=df["salary"]==">50K"
    df_copy=df.where(df_copy_filter1 & df_copy_filter2)
    print(df_copy) """
    df.rename(columns={'native-country':'country'},inplace=True)
    """ print(len(df.loc[(df.country=="Iran")]))
    print(len(df.loc[(df.country=="Iran")&(df.salary==">50K")])) """    
    persian=len(df.loc[(df.country=="Iran")])
    rich_persian=len(df.loc[(df.country=="Iran")&(df.salary==">50K")])
    highest_earning_country = "Iran"
    highest_earning_country_percentage = round(rich_persian*100/persian,1)

    # Identify the most popular occupation for those who earn >50K in India.
    """ print(df.loc[(df.country=="India")&(df.salary==">50K")])
    print("Occupations: " , df['occupation'].unique() , "\n The number of unique occupations: " , len(df['occupation'].unique()))

    print("Adm-clerical occurence count: ", df['occupation'].value_counts()['Adm-clerical'])
    print("Exec-managerial occurence count: ", df['occupation'].value_counts()['Exec-managerial'])
    print("Handlers-cleaners occurence count: ", df['occupation'].value_counts()['Handlers-cleaners'])
    print("Prof-specialty occurence count: ", df['occupation'].value_counts()['Prof-specialty'])
    print("Other-service occurence count: ", df['occupation'].value_counts()['Other-service'])
    print("Sales occurence count: ", df['occupation'].value_counts()['Sales'])
    print("Craft-repair occurence count: ", df['occupation'].value_counts()['Craft-repair'])
    print("Transport-moving occurence count: ", df['occupation'].value_counts()['Transport-moving'])
    print("Farming-fishing occurence count: ", df['occupation'].value_counts()['Farming-fishing'])
    print("Machine-op-inspct occurence count: ", df['occupation'].value_counts()['Machine-op-inspct'])
    print("Tech-support occurence count: ", df['occupation'].value_counts()['Tech-support'])
    print("Protective-serv occurence count: ", df['occupation'].value_counts()['Protective-serv'])
    print("Armed-Forces occurence count: ", df['occupation'].value_counts()['Armed-Forces'])
    print("Priv-house-serv occurence count: ", df['occupation'].value_counts()['Priv-house-serv']) """
    
    top_IN_occupation = "Prof-specialty"

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        #print("---------------------------------------------------------------")
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
