class Movie():
    """Class that holds information of movie data.

    Movie class created for fresh_tomatoes.py, which
    creates a webpage that shows all movies in a collection
    of this class.

    Attributes:
        movie_title: A string representing the title of the movie.
        movie_storyline: A string that describes the movie storyline.
        poster_image: A string representing the url to an image of the Movie's poster
        trailer_youtube: A string representing the url to the trailer of the movie.
    """
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """Inits Movie class with the attributes."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

class TelevisionShow(Movie):
    """Class that repressents a Television series.

    Televesion show inherited from Movie class, adds additional tv series
    data, for example seasons and information about the provider that released
    the show.

    Attributes:
        seasons: An integer representing the number of seasons of the show.
        released_by: A string that represents the releasing or producing company/network
        """
    def __init__(self, show_title, show_storyline, poster_image, trailer_youtube, seasons, released_by):
        Movie.__init__(self, show_title, show_storyline, poster_image, trailer_youtube)
        self.seasons = seasons
        self.released_by = released_by
    
        
