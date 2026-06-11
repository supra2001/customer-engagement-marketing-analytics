USE PortfolioProject_MarketingAnalytics;

-- SELECT * FROM customers
-- SELECT * FROM geography

SELECT 
c.CustomerID, c.CustomerName, c.Email, c.Gender, c.Age, 
g.Country, g.City 
FROM
customers c 
LEFT JOIN 
geography g 
ON c.GeographyID = g.GeographyID