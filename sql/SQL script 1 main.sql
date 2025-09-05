SELECT Country, COUNT(*) AS TotalAthletes
FROM athletes
GROUP BY Country
ORDER BY TotalAthletes DESC;

🔹 -- Calculate the total medals won by each country:
SELECT 
TeamCountry,
SUM(Gold) Total_Gold,
SUM(Silver) Total_Silver,
SUM(Bronze) Total_Bronze
FROM medals
GROUP BY TeamCountry
ORDER BY Total_Gold DESC;

🔹 -- calculate the average number of entries by gender for each discipline
SELECT 
    Discipline,
    AVG(CAST(Female AS INT)) AS Avg_Female_Entries,
    AVG(CAST(Male AS INT))   AS Avg_Male_Entries,
    AVG(CAST(Total AS INT))  AS Avg_Total_Entries
FROM EntriesGender
GROUP BY Discipline
ORDER BY Discipline;

Which disciplines have the highest number of athletes?
SELECT 
    Discipline,
    COUNT(*) AS Athlete_Count
FROM athletes
GROUP BY Discipline
ORDER BY Athlete_Count DESC;

🔹 -- Find the top 10 countries with the most gold medals.
SELECT 
    TeamCountry,
    SUM(Gold) AS Total_Gold
FROM medals
GROUP BY TeamCountry
ORDER BY Total_Gold DESC
LIMIT 10;

🔹 -- Calculate medal efficiency (total medals per athlete) by country.
SELECT 
    m.TeamCountry,
    (SUM(m.Gold) + SUM(m.Silver) + SUM(m.Bronze)) AS Total_Medals,
    COUNT(a.ID) AS Total_Athletes,
    ROUND( (SUM(m.Gold) + SUM(m.Silver) + SUM(m.Bronze)) * 1.0 / COUNT(a.ID), 2) AS Medals_Per_Athlete
FROM medals m
JOIN athletes a 
    ON m.TeamCountry = a.Country
GROUP BY m.TeamCountry
ORDER BY Medals_Per_Athlete DESC;

🔹 -- Which discipline has the highest average medals won per country?
SELECT 
    e.Discipline,
    ROUND(AVG(m.Gold + m.Silver + m.Bronze), 2) AS Avg_Medals_Per_Country
FROM EntriesGender e
JOIN medals m 
    ON e.Discipline = m.Discipline
GROUP BY e.Discipline
ORDER BY Avg_Medals_Per_Country DESC;

🔹 -- Gender participation ratio per discipline (Female vs Male).
SELECT 
    Discipline,
    SUM(Female) AS Total_Female,
    SUM(Male) AS Total_Male,
    ROUND(SUM(Female)*1.0 / NULLIF(SUM(Male), 0), 2) AS Female_Male_Ratio
FROM EntriesGender
GROUP BY Discipline
ORDER BY Female_Male_Ratio DESC;