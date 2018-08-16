

# This is the main file which generates the html page
# Import media import the classes Video,Movie and Tvseries
# Import Utrailers contains the code for the html site

import media
import Utrailers

# instances of the Movie class and Tvseries

harry_potter = media.Movie(
                            "Harry Potter and the philoshopher's stone",
                            "A magical story",
                            "http://www.asset1.net/tv/pictures/movie/harry-potter-and-the-philosopher's-stone-2001/harrypotterandthephilosophersstone-KA-1.jpg",  # noqa
                            "https://www.youtube.com/watch?v=VyHV0BRtdxo",
                            "2001",
                            "PG",
                            "152 minutes",
                            "Chris Columbus")

lord_of_the_rings = media.Movie(
                                "The Lord of the Rings",
                                "Two hobbits one ring",
                                "http://www.cinema52.com/2014/wp-content/uploads/2014/07/The-Lord-of-the-Rings-The-Fellowship-of-the-Ring-Poster.jpg",  # noqa
                                "https://www.youtube.com/watch?v=V75dMMIW2B4",
                                "2001",
                                "PG-13",
                                "178 minutes",
                                "Peter Jackson")

sex_and_the_city = media.Movie(
                               "Sex and the city:the movie",
                               "it's about sex and a city",
                               "http://www.impawards.com/2008/posters/sex_and_the_city.jpg",  # noqa
                               "https://www.youtube.com/watch?v=g9Mx2OLnoGI",
                               "2008",
                               "R",
                               "145 minutes",
                               "Michael Patrick King")

warcraft = media.Movie(
                       "Warcraft:The movie",
                       "Orcs and humans",
                       "http://www.impawards.com/2016/posters/warcraft_ver9_xlg.jpg",  # noqa
                       "https://www.youtube.com/watch?v=RhFMIRuHAL4",
                       "2016",
                       "PG-13",
                       "123 minutes",
                       "Duncan Jones")

monster_inc = media.Movie(
                          "Monster inc",
                          "A terryifing story",
                          "http://www.pixartalk.com/wp-content/uploads/2009/06/monstersuk.jpg",  # noqa
                          "https://www.youtube.com/watch?v=8IBNZ6O2kMk",
                          "2001",
                          "G",
                          "93 minutes",
                          " Pete Docter")

the_simpsons = media.Tvseries(
                              "The Simpsons",
                              "A family story",
                              "https://images-na.ssl-images-amazon.com/images/M/MV5BYjFkMTlkYWUtZWFhNy00M2FmLThiOTYtYTRiYjVlZWYxNmJkXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
                              "https://www.youtube.com/watch?v=tLSy8Tl2bjs",
                              "1989",
                              "TV-14",
                              "22 minutes",
                              "29",
                              "622")

# Array of movies and tv shows
movies = [
            harry_potter,
            lord_of_the_rings,
            sex_and_the_city,
            warcraft,
            monster_inc,
            the_simpsons
    ]

# Generates the html file
# input is our array of movies and tv shows
Utrailers.open_movies_page(movies)
