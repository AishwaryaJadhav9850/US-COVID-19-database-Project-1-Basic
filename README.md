# US-COVID-19-database-Project-1-Basic
Database Project 1 Basic US COVID-19 database 
In this project, you will get started on how to use a relational DBMS. You can either use the ORACLE RDBMS, or the MySQL system. You will use the interactive SQLPLUS facility, and the SQL programming facility, by creating tables, populating them with data, and querying and updating the tables. You should do the following:

1.	Create the following tables for the US COVID-19 database whose schema is specified in Page 3 of this document: STATE, COUNTY, CONFIRMED CASES, DEATHS, VACCINATIONS. Write your CREATE TABLE statements in a text file and execute the commands from the file through SQLPLUS. You should capture the execution in a spool file that will be turned in. Specify appropriate key and referential integrity constraints. The data types for each attribute are given after the schema diagram.

2.	Write one or more database programs to load the records that will be provided to you into each of the tables that you created.  The supplied data is synthetic and may not represent the ground reality. You might have to pivot some data to suit to the schema given. You can use any programming or scripting language you are familiar with (JAVA with JDBC, Pro*C, PERL, PHP, Python, etc.).

3.	Write down the queries for the English queries that are listed later. Execute each query and display its results. Capture your commands in spool files for turning in.

4.	Execute 3 more Insert commands that attempt to insert 3 more records, such that the records violate the integrity constraints. Make each of the 3 records violate a different type of integrity constraint. Capture your commands in spool files for turning in.

5.	Execute a SQL command to Delete a record that violates a referential integrity constraint. Capture your command in a spool file for turning in.

6.	Repeat 5 but Insert three new records that do not violate any integrity constraints. Capture your commands in spool files for turning in.


Apply the following queries and display the result of each query
1)	Print the name of state with largest in size
2)	Retrieve the names of counties, their parent state, their population, number of positive cases by date, sorted in the order of highest to lowest density of positive cases per thousand of population.
3)	Print similar report as above, but for density of deaths per thousand of population.
4)	Show a report for top 10 sensitive counties per state from positive case point of view.
5)	Print similar report (as 4) from number of death point of view.
6)	Prepare a report to show the progress of vaccinations
a.	Sort states by rate of vaccination for 1st dose
b.	Sort states by rate of vaccination for 2nd dose
7)	Which counties in Texas has at least 5% population have been vaccinated by 1st dose?
8)	Which one county has largest population yet to be vaccinated, considering 75% of population to be vaccinated to achieve herd immunity.
