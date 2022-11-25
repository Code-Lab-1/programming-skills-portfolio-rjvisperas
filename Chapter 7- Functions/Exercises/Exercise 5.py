def city(city, country='Philippines'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

city('Pangasinan')
city('Dubai', 'UAE')
city('Kalookan')