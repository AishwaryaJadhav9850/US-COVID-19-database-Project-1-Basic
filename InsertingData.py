import cx_Oracle as co
import pandas as pd
connection=None
try:
    #Establish Connection to the Database
    connection = co.connect(user="SYSTEM",password ="Tiger",dsn ='<PUT YOUR DSN HERE>')
    print("Sucessful connection to Database!")
    cursor = connection.cursor()

    #Delete any old data if present
    cursor.execute("TRUNCATE TABLE DEATHS")
    cursor.execute("TRUNCATE TABLE CONFIRMED_CASES")
    cursor.execute("TRUNCATE TABLE VACCINATIONS")
    cursor.execute("TRUNCATE TABLE COUNTY")
    cursor.execute("TRUNCATE TABLE STATE")
    connection.commit()

    #Read State csv file and fetch data into variable to insert into table
    df = pd.read_csv("US_state.csv", header=0,
                     names=["State_id", "State", "Abbreviation", "YearOfStatehood", "Capital", "Capital_Since",
                            "LandArea", "IsPopulousCity", "MunicipalPopulation", "MetroPopulation"])
    df.IsPopulousCity.replace(('Yes', 'No'), (1, 0), inplace=True)
    df.MetroPopulation.fillna(-9999999, inplace=True)
    State_id = list(df['State_id'])
    State = list(df['State'])
    Abbreviation = list(df['Abbreviation'])
    YearOfStatehood = list(df['YearOfStatehood'])
    Capital = list(df['Capital'])
    Capital_Since = list(df['Capital_Since'])
    LandArea = list(df['LandArea'])
    IsPopulousCity = list(df['IsPopulousCity'])
    MunicipalPopulation = list(df['MunicipalPopulation'])
    MetroPopulation = list(df['MetroPopulation'])
    cursor.bindarraysize = 100000000

    #Insert data into State table
    print("Now Inserting Data for State Table")
    for i in range(df.shape[0]):
        cursor.execute("insert into state (State_id,State,Abbreviation,YearOfStatehood,Capital,Capital_Since,LandArea,IsPopulousCity,MunicipalPopulation) values (:1,:2,:3,:4,:5,:6,:7,:8,:9)",(State_id[i],State[i],Abbreviation[i],YearOfStatehood[i],Capital[i],Capital_Since[i],LandArea[i],IsPopulousCity[i],MunicipalPopulation[i]))
        if MetroPopulation[i] != -9999999:
            cursor.execute("update state set MetroPopulation =:1 where State_id=:2", (MetroPopulation[i],State_id[i]))
    connection.commit()
    print("Data Insert Complete for State Table!")

    # Read County csv file and fetch data into variable to insert into County table
    df = pd.read_csv("Us_County.csv", header=0, names=["State", "County", "Population", "Latitude", "Longitude"])
    df.dropna(axis=0, inplace=True)
    State = list(df['State'])
    County = list(df['County'])
    Population = list(df['Population'])
    Latitude = list(df['Latitude'])
    Longitude = list(df['Longitude'])

    # Insert data into County table
    print("Now Inserting Data for County Table")
    for i in range(df.shape[0]):
        cursor.execute("insert into county (State,County,Population,Latitude,Longitude) values (:1,:2,:3,:4,:5)",(State[i],County[i],Population[i],Latitude[i],Longitude[i]))
    connection.commit()
    print("Data Insert Complete for County Table!")

    # Read Death csv file and fetch data into variable to insert into Death table
    df1 = pd.read_csv("Us_deaths.csv")
    df = pd.melt(df1, id_vars=['Province_State', 'County'], var_name='ReportDate', value_name='DeathCount')
    df['ReportDate'] = pd.to_datetime(df['ReportDate']).dt.date
    State = list(df['Province_State'])
    County = list(df['County'])
    ReportDate = list(df['ReportDate'])
    DeathCount = list(df['DeathCount'])

    # Insert data into Death table
    print("Now Inserting Data for Death Table")
    for i in range(df.shape[0]):
        if DeathCount[i] > 0:
            cursor.execute("insert into DEATHS (State,County,ReportDate,DeathCount) values (:1,:2,:3,:4)",(State[i],County[i],ReportDate[i],DeathCount[i]))
        connection.commit()
    print("Data Insert Complete for Death Table!")

    # Read Confirmed Cases csv file and fetch data into variable to insert into Confirmed_Cases table
    df1 = pd.read_csv("Us_confirmed_cases.csv")
    df = pd.melt(df1, id_vars=['Province_State', 'County'], var_name='TestDate', value_name='PositiveCount')
    df['TestDate'] = pd.to_datetime(df['TestDate']).dt.date
    State = list(df['Province_State'])
    County = list(df['County'])
    TestDate = list(df['TestDate'])
    PositiveCount = list(df['PositiveCount'])

    # Insert data into Confirmed_Cases table
    print("Now Inserting Data for Confirmed_Cases Table")
    for i in range(df.shape[0]):
        if PositiveCount[i] > 0:
            cursor.execute("insert into CONFIRMED_CASES (State,County,TestDate,PositiveCount) values (:1,:2,:3,:4)",
                           (State[i], County[i], TestDate[i], PositiveCount[i]))
        connection.commit()
    print("Data Insert Complete for Confirmed_Cases Table!")

    # Read Vaccination csv file and fetch data into variable to insert into Vaccinations table
    df = pd.read_csv("US_Vaccination.csv", header=0,
                     names=["State", "TotalDistributed", "TotalAdministered", "DistributedPer100K",
                            "AdministeredPer100K", "PeopleWith1PlusDoses", "PeopleWith1PlusDosesPer100K",
                            "PeopleWith2PlusDoses", "PeopleWith2Plus"])
    State = list(df['State'])
    TotalDistributed = list(df['TotalDistributed'])
    TotalAdministered = list(df['TotalAdministered'])
    DistributedPer100K = list(df['DistributedPer100K'])
    AdministeredPer100K = list(df['AdministeredPer100K'])
    PeopleWith1PlusDoses = list(df['PeopleWith1PlusDoses'])
    PeopleWith1PlusDosesPer100K = list(df['PeopleWith1PlusDosesPer100K'])
    PeopleWith2PlusDoses = list(df['PeopleWith2PlusDoses'])
    PeopleWith2Plus = list(df['PeopleWith2Plus'])

    # Insert data into Vaccinations table
    print("Now Inserting Data for Vaccinations Table")
    for i in range(df.shape[0]):
        cursor.execute("insert into VACCINATIONS (State,TotalDistributed,TotalAdministered,DistributedPer100K,AdministeredPer100K,PEOPLEWITH1PLUSDOSES,PEOPLEWITH1PLUSDOSESPER100K,PEOPLEWITH2PLUSDOSES,PEOPLEWITH2PLUSDOSESPER100K) values (:1,:2,:3,:4,:5,:6,:7,:8,:9)",(State[i],TotalDistributed[i],TotalAdministered[i],DistributedPer100K[i],AdministeredPer100K[i],PeopleWith1PlusDoses[i],PeopleWith1PlusDosesPer100K[i],PeopleWith2PlusDoses[i],PeopleWith2Plus[i]))
    connection.commit()
    print("Data Insert Complete for Vaccinations Table!")

finally:
    print("Closing Connection")
    if connection:
        connection.close()
        print("Connection is closed")

