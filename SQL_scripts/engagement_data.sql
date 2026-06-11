SELECT
    EngagementID, ContentID, CampaignID, ProductID, Likes,
    UPPER(REPLACE(ContentType, 'Socialmedia', 'Social Media')) AS ContentType,
    CAST(LEFT(ViewsClicksCombined, CHARINDEX('-', ViewsClicksCombined)-1) AS INT) AS VIEWS,
    CAST(RIGHT(ViewsClicksCombined, LEN(ViewsClicksCombined) - CHARINDEX('-', ViewsClicksCombined)) AS INT) AS CLICKS,
    FORMAT(CONVERT(DATE, EngagementDate), 'dd.MM.yyyy') AS EngagementDate
FROM engagement_data
WHERE ContentType != 'Newsletter'