import fresh_tomatoes
import media

#Collates data in form of movie classes and sends it to fresh_tomatoes 

WWDitS= media.Movie("What We Do in the Shadows ",
                       "A documentary team films the lives of a group of vampires for a few months. The vampires share a house in Wellington, New Zealand. Turns out vampires have their own domestic problems too.",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAwNDA5NzEwM15BMl5BanBnXkFtZTgwMTA1MDUyNDE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                       "https://www.youtube.com/watch?v=Cv568AzZ-i8",
                       "Taika Waititi", "15aa")

HftW = media.Movie("Hunt for the Wilderpeople",
                     "A national manhunt is ordered for a rebellious kid and his foster uncle who go missing in the wild New Zealand bush.",
                     "https://upload.wikimedia.org/wikipedia/en/4/44/Hunt_for_the_Wilderpeople.png",
                     "https://www.youtube.com/watch?v=tICv8QH3oM0",
                   "Taika Waititi", "12A")

EvsS = media.Movie("Eagle vs Shark",
                     "Eagle vs Shark is the tale of two socially awkward misfits and the strange ways they try to find love; through revenge on high-school bullies, burgers, and video games.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BOTUxMzY3MzI0NV5BMl5BanBnXkFtZTcwMDUwMDU0MQ@@._V1_.jpg",
                     "https://www.youtube.com/watch?v=b4HdAKMQ1Ew",
                   "Taika Waititi", "15")

Boy = media.Movie("Boy",
                     "Set on the east coast of New Zealand in 1984, Boy, an 11-year-old kid and devout Michael Jackson fan, gets a chance to know his father, who has returned to find a bag of money he buried years ago.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMjc4MjQ2ODQyNF5BMl5BanBnXkFtZTcwOTE0NzIzNw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=ESD3mlgpSwM",
                   "Taika Waititi", "Not Rated")

AFiE = media.Movie("A Field in England",
                     "Set on the east coast of New Zealand in 1984, Boy, an 11-year-old kid and devout Michael Jackson fan, gets a chance to know his father, who has returned to find a bag of money he buried years ago.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMjcyNzQyMjI0NF5BMl5BanBnXkFtZTgwNjU2MDc5MDE@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=cRRvzjkzu2U",
                   "Ben Wheatley", "15")
OBrother = media.Movie("O Brother, Where Art Thou?",
                     "In the deep south during the 1930s, three escaped convicts search for hidden treasure while a relentless lawman pursues them.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTI3MTEwMTAzMF5BMl5BanBnXkFtZTYwMTMxNTI5._V1_.jpg",
                     "https://www.youtube.com/watch?v=eW9Xo2HtlJI",
                   "The Coen Brothers", "12A")

movies = (WWDitS, HftW, OBrother, EvsS, Boy, AFiE)

fresh_tomatoes.open_movies_page(movies)


