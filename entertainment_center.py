import media
import rotten_tomatoes

star_wars_ep_1 = media.Movie("https://www.youtube.com/watch?v=bD7bpG-zDJQ", "Star Wars: The Phantom Menace", 1,
                             "http://moviesfire.net/wp-content/uploads/2015/09/Star-Wars-Episode-I-The-Phantom-Menace-1999.jpg")

star_wars_ep_2 = media.Movie("https://www.youtube.com/watch?v=gYbW1F_c9eM", "Star Wars: Attack of the Clones", 2,
                             "https://i.kinja-img.com/gawker-media/image/upload/cjccaje7aliirg5topj8.jpg")

star_wars_ep_3 = media.Movie("https://www.youtube.com/watch?v=1g3_CFmnU7k", "Star Wars: Revenge of the Sith", 4,
                             "http://ia.media-imdb.com/images/M/MV5BNTc4MTc3NTQ5OF5BMl5BanBnXkFtZTcwOTg0NjI4NA@@._V1_SX640_SY720_.jpg")

star_wars_ep_4 = media.Movie("https://www.youtube.com/watch?v=1g3_CFmnU7k", "Star Wars: A New Hope", 5,
                             "http://img1.ak.crunchyroll.com/i/spire4/ee1cdb01766aa55c696e9faadc39cd0e1393301343_full.jpg")

star_wars_ep_4 = media.Movie("https://www.youtube.com/watch?v=1g3_CFmnU7k", "Star Wars: A New Hope", 5,
                             "http://img1.ak.crunchyroll.com/i/spire4/ee1cdb01766aa55c696e9faadc39cd0e1393301343_full.jpg")

star_wars_ep_5 = media.Movie("https://www.youtube.com/watch?v=PkEKIw0FU6Y", "Star Wars: Empire Strikes Back", 5,
                             "http://vignette3.wikia.nocookie.net/starwars/images/e/e4/Empire_strikes_back_old.jpg/revision/latest?cb=20061201083417")

star_wars_ep_6 = media.Movie("https://www.youtube.com/watch?v=5UfA_aKBGMc", "Star Wars: Return of the Jedi", 5,
                             "https://www.movieposter.com/posters/archive/main/111/MPW-55925")

movie_arr = [star_wars_ep_4, star_wars_ep_5, star_wars_ep_6, star_wars_ep_1, star_wars_ep_2, star_wars_ep_3]

rotten_tomatoes.open_movies_page(movie_arr)
