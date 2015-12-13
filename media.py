import webbrowser
class Movie():
    def __init__(self, trailer_url, title, rating, poster_art, movie_plot):
        self.trailer_url = trailer_url
        self.title = title
        self.rating = rating
        self.poster_art = poster_art
        self.movie_plot = movie_plot

    def show_trailer(self):
        webbrowser.open(self.trailer_url)
