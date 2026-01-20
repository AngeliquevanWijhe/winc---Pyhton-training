# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
film_names=['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction', 'Forrest Gump']
alphabetical_order= sorted(film_names)
print(alphabetical_order)
won_golden_globe = ["Jaws", "E.T.", "Star Wars", "Memoires of a Geisha"]
print(won_golden_globe)
lowercase_film_names = [film.lower() for film in film_names]
print(lowercase_film_names)
if "The Godfather" in won_golden_globe:
    print("True")