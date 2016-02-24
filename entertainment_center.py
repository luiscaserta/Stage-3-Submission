import media
#imports media.py file to make it available
import fresh_tomatoes
#imports fresh_tomatoes.py file to make it available

harry_potter = media.Movie("Harry Potter",
						   "http://assets.flicks.co.nz/images/movies/poster/49/494ba9ff03bdad881378a6fd4092a6c7_500x735.jpg",
						   "https://www.youtube.com/watch?v=VyHV0BRtdxo")

song_of_the_sea = media.Movie("Song of the Sea",
							  "https://upload.wikimedia.org/wikipedia/en/4/4f/Song_of_the_Sea_%282014_film%29_poster.jpg",
							  "https://www.youtube.com/watch?v=UBO_0RrNVJc")

mary_poppins = media.Movie("Mary Poppins",
						   "https://upload.wikimedia.org/wikipedia/en/7/78/Marypoppins.jpg",
						   "https://www.youtube.com/watch?v=nOfH7uEojKk")

grease = media.Movie("Grease",
					 "https://upload.wikimedia.org/wikipedia/en/e/e2/Grease_ver2.jpg",
					 "https://www.youtube.com/watch?v=wzWmxjYNfz4")

city_slickers = media.Movie("City Slickers",
							"https://upload.wikimedia.org/wikipedia/en/3/3c/City_Slickers.jpg",
							"https://www.youtube.com/watch?v=rpxVp1g8xMQ")

e_t = media.Movie("E.T.",
				  "https://upload.wikimedia.org/wikipedia/en/6/66/E_t_the_extra_terrestrial_ver3.jpg",
				  "https://www.youtube.com/watch?v=qYAETtIIClk")

#the above variables are defined instances of the class Movie, as scripted in the  media.py file

movies =[harry_potter, song_of_the_sea, mary_poppins, grease, city_slickers, e_t]
#this is my list of movies that will be applied to the function open_movies_page

fresh_tomatoes.open_movies_page(movies)
#this is the syntax that calls the function open_movies_page that is within the fresh_tomatoes.py file

#Note to reviewer: the fresh_tomatoes.py file is the bread and butter of this assignment, as it defines the layout and structure 
#of the web open_movies_page.  I don't feel as if I am able to do this type of codiing on my own.  Is this normal?
#Is this why the code was provided by Udactiy? #What can I do to get a better understanding and learn how to do that type
#of coding on my own?
