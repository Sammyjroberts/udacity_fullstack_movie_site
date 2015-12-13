import media
import rotten_tomatoes
star_wars_ep_4 = media.Movie("https://www.youtube.com/watch?v=1g3_CFmnU7k", "Star Wars: A New Hope", 5,
                        "http://img1.ak.crunchyroll.com/i/spire4/ee1cdb01766aa55c696e9faadc39cd0e1393301343_full.jpg",
                        "Nineteen years after the formation of the Empire, Luke Skywalker is thrust into the struggle of"
                        " the Rebel Alliance when he meets Obi-Wan Kenobi, who has lived for years in seclusion on the "
                        "desert planet of Tatooine. Obi-Wan begins Luke's Jedi training as Luke joins him on a daring "
                        "mission to rescue the beautiful Rebel leader Princess Leia from the clutches of the evil "
                        "Empire. Although Obi-Wan sacrifices himself in a lightsaber duel with Darth Vader, his former "
                        "apprentice, Luke proves that the Force is with him by destroying the Empire's dreaded "
                        "Death Star.")
star_wars_ep_5 = media.Movie("https://www.youtube.com/watch?v=1g3_CFmnU7k", "Star Wars: A New Hope", 5,
                        "http://img1.ak.crunchyroll.com/i/spire4/ee1cdb01766aa55c696e9faadc39cd0e1393301343_full.jpg",
                        "Nineteen years after the formation of the Empire, Luke Skywalker is thrust into the struggle of"
                        " the Rebel Alliance when he meets Obi-Wan Kenobi, who has lived for years in seclusion on the "
                        "desert planet of Tatooine. Obi-Wan begins Luke's Jedi training as Luke joins him on a daring "
                        "mission to rescue the beautiful Rebel leader Princess Leia from the clutches of the evil "
                        "Empire. Although Obi-Wan sacrifices himself in a lightsaber duel with Darth Vader, his former "
                        "apprentice, Luke proves that the Force is with him by destroying the Empire's dreaded "
                        "Death Star.")
star_wars_ep_6 = media.Movie("https://www.youtube.com/watch?v=1g3_CFmnU7k", "Star Wars: A New Hope", 5,
                        "http://img1.ak.crunchyroll.com/i/spire4/ee1cdb01766aa55c696e9faadc39cd0e1393301343_full.jpg",
                        "Nineteen years after the formation of the Empire, Luke Skywalker is thrust into the struggle of"
                        " the Rebel Alliance when he meets Obi-Wan Kenobi, who has lived for years in seclusion on the "
                        "desert planet of Tatooine. Obi-Wan begins Luke's Jedi training as Luke joins him on a daring "
                        "mission to rescue the beautiful Rebel leader Princess Leia from the clutches of the evil "
                        "Empire. Although Obi-Wan sacrifices himself in a lightsaber duel with Darth Vader, his former "
                        "apprentice, Luke proves that the Force is with him by destroying the Empire's dreaded "
                        "Death Star.")

movie_arr = [star_wars_ep_4,star_wars_ep_5,star_wars_ep_6]
rotten_tomatoes.open_movies_page(movie_arr)