import media
import fresh_tomatoes

fight_club = media.Movie("Fight Club",
                         "An insomniac office worker looking for a way to change his life crosses paths with a devil-may-care soap maker and they form an underground fight club that evolves into something much, much more...",
                         "http://images.moviepostershop.com/fight-club-movie-poster-1999-1020215604.jpg",
                         "https://youtu.be/SUXWAEX2jlg")
american_beauty = media.Movie("American Beauty",
                              "A sexually frustrated suburban father has a mid-life crisis after becoming infatuated with his daughter's best friend.",
                              "http://i2.listal.com/image/1329255/936full-american-beauty-poster.jpg",
                              "https://www.youtube.com/watch?v=y4DvNwt0FSM")
the_matrix = media.Movie("The Matrix",
                         "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                         "http://www.impawards.com/1999/posters/matrix_ver2_xlg.jpg",
                         "https://youtu.be/m8e-FF8MsqU")
prison_break = media.TelevisionShow("Prison Break",
                                    "Due to a political conspiracy an innocent man is sent to death row and his only hope is his brother who makes it his mission to deliberately get himself sent to the same prison in order to break the both of them out from the inside out.",
                                    "http://www.impawards.com/tv/posters/prison_break_ver3.jpg",
                                    "https://youtu.be/3zxSwYyb2Vk",
                                    5,
                                    "FOX")
sense8 = media.TelevisionShow("Sense8",
                              "A group of people around the world are suddenly linked mentally, and must find a way to survive being hunted by those who see them as a threat to the world's order.",
                              "http://ia.media-imdb.com/images/M/MV5BMTY2MjI4MjkxN15BMl5BanBnXkFtZTgwNjU5Nzk4NTE@._V1_.jpg",
                              "https://youtu.be/E9c_KSZ6zMk",
                              1,
                              "Netflix")
                     
movies = [fight_club, american_beauty, the_matrix, prison_break, sense8]
fresh_tomatoes.open_movies_page(movies)
