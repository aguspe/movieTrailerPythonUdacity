# This is the defination class file
# webbrowser module opens a browser windows


import webbrowser

# definition of class parent "Video"

class Video():

    """The video class provides all the elements that are common for its
    children,movies and Tvseries"""

        # Init method is the constructor of the class
        # the init method accepts 9 arguments, being self the instances itself

    def __init__(self, video_title, video_storyline, poster_image,
                 trailer_youtube, video_year, video_rate, duration):

        self.title = video_title
        self.time = duration
        self.storyline = video_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year = video_year
        self.rate = video_rate

        """show_trailer method is what it's use to visualize the trailer"""

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class Movie(Video):

    """The movie class defines  movies and its use to generate the movies
    instances in entertainment_center,it's the child of video"""


        # This init method is the constructor of the class Movie
    def __init__(self, video_title, video_storyline, poster_image,
                 trailer_youtube,video_year, video_rate,  duration,
                 movie_director):

        # On the other hand this one is to use its parent class
        Video.__init__(self, video_title, video_storyline, poster_image,
                       trailer_youtube, video_year, video_rate, duration)

        self.director = movie_director

class Tvseries(Video):

    """The TVseries class defines the characteriscts of movies and its use to
        generate the Tvseries instances in entertainment_center,
        it's the child of video"""

    # This init method is the constructor of the class Tvseries
    def __init__(self, video_title, video_storyline, poster_image,
    trailer_youtube, video_year, video_rate, duration, tv_seasons, tv_episodes):

        # On the other hand this one is to use its parent class
        Video.__init__(self, video_title, video_storyline, poster_image,
                       trailer_youtube, video_year, video_rate, duration)

        self.seasons = tv_seasons
        self.episodes = tv_episodes
