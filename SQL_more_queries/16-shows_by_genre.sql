-- Script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows4
-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name
SELECT tv_shows.title, tv_genres.name FROM tv_shows
LEFT JOIN tv_show_genres on tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres on tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
