spool TableCreationSpool.txt


CREATE TABLE STATE
(State_id INT NOT NULL,
State VARCHAR(50) NOT NULL,
Abbreviation CHAR(2),
YearOfStatehood INT,
Capital VARCHAR(50),
Capital_Since INT,
LandArea DECIMAL(20,10),
IsPopulousCity NUMBER(1,0),
MunicipalPopulation INT,
MetroPopulation INT,
PRIMARY KEY (State),
UNIQUE (State_id));



CREATE TABLE COUNTY
(State VARCHAR(50) NOT NULL, 
County VARCHAR(50) NOT NULL, 
Population INT,
Latitude DECIMAL(10,8), 
Longitude DECIMAL(20,10),
PRIMARY KEY (County,State),
FOREIGN KEY (State) REFERENCES STATE(State));



CREATE TABLE CONFIRMED_CASES
(State VARCHAR(50) NOT NULL, 
County VARCHAR(50) NOT NULL, 
TestDate DATE NOT NULL, 
PositiveCount INT,
PRIMARY KEY (State,County,TestDate),
FOREIGN KEY (State) REFERENCES STATE(State),
FOREIGN KEY (State,County) REFERENCES COUNTY(State,COUNTY));


CREATE TABLE DEATHS
(State VARCHAR(50) NOT NULL, 
County VARCHAR(50) NOT NULL, 
ReportDate DATE NOT NULL, 
DeathCount INT,
PRIMARY KEY (State,County,ReportDate),
FOREIGN KEY (State) REFERENCES STATE(State),
FOREIGN KEY (State,County) REFERENCES COUNTY(State,COUNTY));


CREATE TABLE VACCINATIONS
(State VARCHAR(50) NOT NULL, 
TotalDistributed INT,
TotalAdministered INT,
DistributedPer100K INT,
AdministeredPer100K INT,
PeopleWith1PlusDoses INT,
PeopleWith1PlusDosesPer100K INT,
PeopleWith2PlusDoses INT,
PeopleWith2PlusDosesPer100K INT,
PRIMARY KEY (State),
FOREIGN KEY (State) REFERENCES STATE(State));


spool off;