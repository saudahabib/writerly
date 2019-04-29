from flaskblog import app
import urllib.request,json
from flaskblog.models import Quote

# Base URL
base_url = app.config["QUOTES_API"]

def get_quote():
    '''
    Function that gets the json response to our url request
    '''
    get_quotes_url = base_url.format()

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quotes_data)

        displayed_quote = None

        if get_movies_response:
            quote = get_quote_response
            displayed_quote = process_results(quote)


    return displayed_quote


    def process_results(quote):
        '''
        Process quote
        '''
        quote = quote.get('quote')
        author = quote.get('author')

        quote_component = Quote(quote, author)

        return quote_component
