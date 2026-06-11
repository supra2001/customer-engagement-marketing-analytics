USE PortfolioProject_MarketingAnalytics;

-- SELECT * FROM products

-- Categorizing products based on their price
SELECT ProductId, ProductName, Price,
CASE 
  WHEN Price < 50 THEN 'Low'
  WHEN Price BETWEEN 50 AND 200 THEN 'Medium'
  ELSE 'High'
END AS ProductCategory
FROM products