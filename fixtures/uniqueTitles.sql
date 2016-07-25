INSERT INTO buzztitles (title)
SELECT DISTINCT title FROM junebuzz
WHERE NOT EXISTS (
  SELECT * FROM buzztitles
  WHERE (
    buzztitles.title=sourcetable.title
  )
);
