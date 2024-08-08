-- script to CREATE a user tbale it's params
-- icountry, enumeration of countries: US, CO and TN, never null (= default will be the first element of the enumeration, here US)
SELECT origin, SUM(fans) as nb_fans from metal_bands GROUP BY origin DESC;
