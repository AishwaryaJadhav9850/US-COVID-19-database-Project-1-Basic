spool QueriesQuestion3.txt


--Query 1: Print the name of state with largest in size
select State, LandArea from state where LandArea in (select max(s.landarea) from state s);




/* Query 2:Retrieve the names of counties, their parent state, their population, number of positive cases by date, 
sorted in the order of highest to lowest density of positive cases per thousand of population.*/

select c.county,c.state,c.Population,cc.TestDate, cc.PositiveCount,((cc.PositiveCount*1000)/c.Population)  as Density
from COUNTY c, CONFIRMED_CASES cc 
where cc.state = c.state and cc.county = c.county and c.Population <> 0
order by Density desc;




/* Query 3: Print similar report as above, but for density of deaths per thousand of population.*/

select c.county,c.state,c.Population,d.ReportDate,d.DeathCount,((DeathCount*1000)/c.Population) as Density
from COUNTY c, DEATHS d
where d.state = c.state and d.county = c.county and c.Population <> 0
order by Density desc;




/* Query 4: Show a report for top 10 sensitive counties per state from positive case point of view. */

SET SERVEROUTPUT ON;
BEGIN
DBMS_OUTPUT.put_line ('State    ' || 'County    ' || 'Total Comfirmed Cases  	');
   FOR c IN (select distinct state from CONFIRMED_CASES)
   LOOP
	FOR d IN (SELECT state,county,sum(PositiveCount) as Total FROM CONFIRMED_CASES Where state = c.state GROUP BY state, county Order by Total desc fetch  first 10 rows only)
   	LOOP
		DBMS_OUTPUT.put_line ( d.state ||'    '|| d.county ||'    '|| d.Total );
   	END LOOP;
   END LOOP;
END;
/





/* Query 5: Print similar report (as 4) from number of death point of view.*/

SET SERVEROUTPUT ON;
BEGIN
DBMS_OUTPUT.put_line ('State    ' || 'County    ' || 'Total Deaths 	');
   FOR c IN (select distinct state from DEATHS)
   LOOP
	FOR d IN (SELECT state,county,sum(DeathCount) as Total FROM DEATHS Where state = c.state GROUP BY state, county Order by Total desc fetch  first 10 rows only)
   	LOOP
		DBMS_OUTPUT.put_line ( d.state ||'    '|| d.county ||'    '|| d.Total );
   	END LOOP;
   END LOOP;
END;
/





/* Query 6: Prepare a report to show the progress of vaccinations
a.	Sort states by rate of vaccination for 1st dose */

select state, (PeopleWith1PlusDoses/TotalDistributed) as Rate
from VACCINATIONS
Order by Rate;



/* Query 6: Prepare a report to show the progress of vaccinations
b.	Sort states by rate of vaccination for 2nd dose */

select state, (PeopleWith2PlusDoses/TotalDistributed) as Rate
from VACCINATIONS
Order by Rate;



/* Query 7: Which counties in Texas has at least 5% population have been vaccinated by 1st dose? 
AS VACCINATION DOESNT HAVE COUNTY COLUMN I have applied this query to state: Which states has at least 5% population have been vaccinated by 1st dose?   */

select c.state, ((v.PeopleWith1PlusDoses/sum(c.Population))*100) as Percentage_1st_Dose
from COUNTY c,VACCINATIONS v
where c.state=v.state
group by c.state,v.PeopleWith1PlusDoses
having ((v.PeopleWith1PlusDoses/sum(c.Population))*100) >= 5
order by Percentage_1st_Dose;




/* Query 8: Which one county has largest population yet to be vaccinated, considering 75% of population to be vaccinated to achieve herd immunity.
AS VACCINATION DOESNT HAVE COUNTY COLUMN I have applied this query to state: Which state has largest population yet to be vaccinated, considering 75% of population to be vaccinated to achieve herd immunity.*/

select c.state, (v.PeopleWith1PlusDoses/sum(c.Population)*100) as percentage
from VACCINATIONS v,County c
where c.state=v.state
group by c.state, v.PeopleWith1PlusDoses
order by percentage;

spool off;



