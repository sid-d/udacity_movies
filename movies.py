import media
import fresh_tomatoes
toystory=media.Movie("Toy Story",
                     "A story",
                     "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                     "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar=media.Movie("Avatar",
                   "alien",
                   "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                   "https://www.youtube.com/watch?v=5PSNL1qE6VY")


zu=media.Movie("World War Z",
                    "alien",
                    "https://upload.wikimedia.org/wikipedia/en/7/76/World_War_Z_book_cover.jpg",
                    "https://www.youtube.com/watch?v=HcwTxRuq-uk")

fresh_tomatoes.open_movies_page([toystory,avatar,zu])