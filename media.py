
# create a shared class for all the movies


class Movie():
    ''' class Movie creates instances of movies by passing specified argumets '''

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        ''' 
        constructor creates title, poster_image_url and trailer_youtube_url
        for each istance of the Movie class
         '''
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
