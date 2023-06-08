DELETE FROM your_table
WHERE generated_date < DATE_SUB(NOW(), INTERVAL 3 MONTH);
