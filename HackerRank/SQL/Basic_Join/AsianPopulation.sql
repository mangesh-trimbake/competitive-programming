select sum(CITY.population)
from CITY
Inner join COUNTRY
on CITY.countrycode=COUNTRY.code where COUNTRY.continent='Asia'
