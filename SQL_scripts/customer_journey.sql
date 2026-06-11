WITH Duplicates AS 
    (SELECT *, 
            ROW_NUMBER() OVER(PARTITION BY CustomerID, ProductID, VisitDate, Stage, Action ORDER BY JourneyID) AS row_count 
            FROM customer_journey) 
SELECT * FROM Duplicates WHERE row_count>1;

WITH CleanedJourney AS
(   SELECT 
        *,
        AVG(Duration) OVER(PARTITION BY VisitDate) AS avg_duration,
        ROW_NUMBER() OVER(PARTITION BY CustomerID, ProductID, VisitDate, UPPER(Stage), Action  ORDER BY JourneyID) AS row_count
    FROM customer_journey)

SELECT 
JourneyID, CustomerId, ProductID, VisitDate, 
UPPER(Stage) AS Stage,
Action,
COALESCE(Duration, avg_duration) AS Duration
FROM CleanedJourney
WHERE row_count = 1

