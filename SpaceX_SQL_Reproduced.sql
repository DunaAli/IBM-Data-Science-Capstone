-- launch_sites
SELECT LaunchSite, COUNT(*) AS launches, SUM(Class) AS successful, ROUND(100.0*AVG(Class),1) AS success_pct FROM spacex GROUP BY LaunchSite ORDER BY launches DESC;

-- payload
SELECT CASE WHEN PayloadMass < 4000 THEN 'Under 4,000 kg' WHEN PayloadMass < 10000 THEN '4,000–9,999 kg' ELSE '10,000+ kg' END AS payload_band, COUNT(*) AS launches, ROUND(100.0*AVG(Class),1) AS success_pct FROM spacex GROUP BY payload_band ORDER BY launches DESC;

-- outcomes
SELECT Outcome, COUNT(*) AS launches FROM spacex GROUP BY Outcome ORDER BY launches DESC LIMIT 5;

