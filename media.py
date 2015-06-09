class Movie():
    """Class that holds information of movie data.

    Movie class created for fresh_tomatoes.py, which
    creates a webpage that shows all movies in a collection
    of this class.

    Attributes:
        **kwargs: Key - Value dictionary, with the following keys
        title: A string representing the title of the movie
        movie_storyline: A string representing a description of the movie
        poster_image_url: A string containing url address to movie poster
        trailer_youtube_url: A string containing url address to trailer
        """
    def __init__(self, **kwargs):
        """Inits Movie with given dictionary args"""
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)


class TelevisionShow(Movie):
    """Class that repressents a Television series.

    Televesion show inherited from Movie class, adds additional tv series
    data, for example seasons and information about the provider that released
    the show.

    Attributes:
        seasons: An integer representing the number of seasons of the show.
        released_by: A string that represents the releasing or company/network
    """
    def __init__(self, seasons, released_by, **kwargs):
        Movie.__init__(self, **kwargs)
        self.seasons = seasons
        self.released_by = released_by
