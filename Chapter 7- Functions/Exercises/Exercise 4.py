def shirt(size='large', message='I love Bagiuo!'):
    """Summarize the shirt that's going to be made."""
    print("\Emma gonna make a " + size + " t-shirt.")
    print('And it will say, "' + message + '"')

shirt()
shirt(size='medium')
shirt('small', 'Programmers are babaeros')