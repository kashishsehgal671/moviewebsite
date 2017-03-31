import media
import fresh_tomatoes
avatar = media.Movie( "AVATAR" ,
                      " On the lush alien world of Pandora live the Na'vi, beings who appear primitive but are highly evolved." ,
                      "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg" ,
                      "https://www.youtube.com/watch?v=d1_JBMrrYw8")
hunger_games = media.Movie(" HUNGER GAMES " ,
                           "what was once North America, the Capitol of Panem maintains its hold on its 12 districts by forcing them each to select a boy and a girl, called Tribp",
                           "https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")
mockingjay = media.Movie( "MOCKINGJAY ",
                           "Following her rescue from the devastating Quarter Quell, Katniss (Jennifer Lawrence) awakes in the complex beneath the supposedly destroyed District 13.",
                           "https://upload.wikimedia.org/wikipedia/en/c/cc/Mockingjay.JPG",
                           "https://www.youtube.com/watch?v=C_Tsj_wTJkQ")
toy_story = media.Movie( "TOY STORY",
                          "Woody (Tom Hanks), a good-hearted cowboy doll who belongs to a young boy named Andy (John Morris), sees his position as Andy's favorite toy ",
                          "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                          "https://www.youtube.com/watch?v=KYz2wyBy3kc")
school_of_rock = media.Movie( " SCHOOL OF ROCK ",
                              "Overly enthusiastic guitarist Dewey Finn (Jack Black) gets thrown out of his bar band and finds himself in desperate need of work. ",
                              "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                              "https://www.youtube.com/watch?v=LqEszt5wG9I")
the_boss_baby = media.Movie( " THE BOSS BABY " ,
                             "A new baby's arrival impacts a family, told from the point of view of a delightfully unreliable narrator -- a wildly imaginative 7-year-old named Tim.",
                             "https://upload.wikimedia.org/wikipedia/en/0/0e/The_Boss_Baby_poster.jpg",
                             "https://www.youtube.com/watch?v=O2Bsw3lrhvs")

    
movies = [ avatar , hunger_games , mockingjay , toy_story , school_of_rock , the_boss_baby ]
fresh_tomatoes.open_movies_page( movies)
