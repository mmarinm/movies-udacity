import media

# create instances of the Movie class with uniqe values

it = media.Movie(
    'It',
    'https://images-na.ssl-images-amazon.com/images/M/MV5BOTE0NWEyNDYtYWI5MC00MWY0LTg1NDctZjAwMjkyMWJiNzk1XkEyXkFqcGdeQXVyNjk5NDA3OTk@._V1_SY1000_CR0,0,674,1000_AL_.jpg',
    'https://www.youtube.com/watch?v=xKJmEC5ieOk'
)

mother = media.Movie(
    'Mother!',
    'https://images-na.ssl-images-amazon.com/images/M/MV5BMzc5ODExODE0MV5BMl5BanBnXkFtZTgwNDkzNDUxMzI@._V1_SY1000_CR0,0,674,1000_AL_.jpg',
    'https://www.youtube.com/watch?v=vtTE_DBKpRY'
)

tsow = media.Movie(
    'The Shape of Water',
    'https://images-na.ssl-images-amazon.com/images/M/MV5BODU5NTAzOTI3OV5BMl5BanBnXkFtZTgwOTc0MjQ1MzI@._V1_SY1000_CR0,0,674,1000_AL_.jpg',
    'https://www.youtube.com/watch?v=XFYWazblaUA'
)

aass = media.Movie(
    'American Assassin',
    'https://images-na.ssl-images-amazon.com/images/M/MV5BMjM0MjY4MTk5NV5BMl5BanBnXkFtZTgwNDE2NTQyMzI@._V1_SY1000_CR0,0,674,1000_AL_.jpg',
    'https://www.youtube.com/watch?v=XwHAGKxsbcg'
)

bdirver = media.Movie(
    'Baby Driver',
    'https://images-na.ssl-images-amazon.com/images/M/MV5BMjM3MjQ1MzkxNl5BMl5BanBnXkFtZTgwODk1ODgyMjI@._V1_SY1000_CR0,0,674,1000_AL_.jpg',
    'https://www.youtube.com/watch?v=z2z857RSfhk'
)

# create a list of all the istances

list_of_movies = [it, mother, tsow, aass, bdirver]
