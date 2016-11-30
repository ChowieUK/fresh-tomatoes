import webbrowser

#Defines parent Video and child Movie / TvShow classes

class Video():
    """ This parent class provides a way to store video related information"""

    VALID_UK_RATINGS = ["U", "PG", "12A", "12", "15", "18", "R18", "Not Rated"]
    VALID_RATINGS = ["G", "PG", "PG-13", "R", "Not Rated"]

    def __init__(self, title,
                 synopsis,
                 poster_image,
                 trailer_youtube):
        self.title = title
        self.synopsis = synopsis
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    


class Movie(Video):
    """ This child class provides a way to store movie related information"""

    def __init__(self, movie_title,
                 movie_synopsis,
                 poster_image,
                 trailer_youtube,
                 movie_director, UK_rating):
        
        Video.__init__(self, movie_title,
                 movie_synopsis,
                 poster_image,
                 trailer_youtube)
        
        self.director = movie_director

        if UK_rating in Video.VALID_UK_RATINGS:
            self.UK_rating = UK_rating
        else:
            print("The listing for " +movie_title + " contains an invalid UK rating")

class TvShow(Video):
    """ This child class provides a way to store Tv Show related information"""

    def __init__(self, show_title,
                 show_synopsis,
                 poster_image,
                 trailer_youtube,
                 network):
        Video.__init__(self, movie_title,
                 show_synopsis,
                 poster_image,
                 trailer_youtube)
        
        self.network = network
