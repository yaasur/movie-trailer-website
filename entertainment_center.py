import media
import fresh_tomatoes

fight_club = media.Movie(title="Fight Club",
                         movie_storyline="An insomniac office worker looking for a way to change his life crosses paths with a devil-may-care soap maker and they form an underground fight club that evolves into something much, much more...",
                         poster_image_url="http://images.moviepostershop.com/fight-club-movie-poster-1999-1020215604.jpg",
                         trailer_youtube_url="https://youtu.be/SUXWAEX2jlg")
american_beauty = media.Movie(title="American Beauty",
                              movie_storyline="A sexually frustrated suburban father has a mid-life crisis after becoming infatuated with his daughter's best friend.",
                              poster_image_url="http://i2.listal.com/image/1329255/936full-american-beauty-poster.jpg",
                              trailer_youtube_url="https://www.youtube.com/watch?v=y4DvNwt0FSM")
the_matrix = media.Movie(title="The Matrix",
                         movie_storyline="A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                         poster_image_url="http://www.impawards.com/1999/posters/matrix_ver2_xlg.jpg",
                         trailer_youtube_url="https://youtu.be/m8e-FF8MsqU")
prison_break = media.TelevisionShow(5,
                                    "FO",
                                    title="Prison Break",
                                    movie_storyline="Due to a political conspiracy an innocent man is sent to death row and his only hope is his brother who makes it his mission to deliberately get himself sent to the same prison in order to break the both of them out from the inside out.",
                                    poster_image_url="http://www.impawards.com/tv/posters/prison_break_ver3.jpg",
                                    trailer_youtube_url="https://youtu.be/3zxSwYyb2Vk")
sense8 = media.TelevisionShow(1,
                              "Netflix",
                              title="Sense8",
                              movie_storyline="A group of people around the world are suddenly linked mentally, and must find a way to survive being hunted by those who see them as a threat to the world's order.",
                              poster_image_url="http://ia.media-imdb.com/images/M/MV5BMTY2MjI4MjkxN15BMl5BanBnXkFtZTgwNjU5Nzk4NTE@._V1_.jpg",
                              trailer_youtube_url="https://youtu.be/E9c_KSZ6zMk")
movies = [fight_club, american_beauty, the_matrix, prison_break, sense8]
fresh_tomatoes.open_movies_page(movies)
