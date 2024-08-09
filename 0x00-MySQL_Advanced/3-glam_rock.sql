-- gets rock artist that have glam rock as a style
SELECT band_name, (IFNULL(split,2020) - formed) AS lifespan FROM metal_bands WHERE style LIKE '%Glam rock%' OR style LIKE '%Glam rock' OR style LIKE 'Glam rock%';
