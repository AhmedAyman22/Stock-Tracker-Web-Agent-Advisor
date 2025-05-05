from polygon import RESTClient
from dotenv import load_dotenv
import os
import datetime
import requests
from datetime import datetime, timedelta

startDate = datetime.now() - timedelta(3)
endDate = datetime.now() - timedelta(1)
startDate = str(startDate).split(' ')[0]
endDate = str(endDate).split(' ')[0]

load_dotenv()

api_key = os.environ.get('POLYGON_API_KEY')

client = RESTClient(api_key=api_key)

def performanceFetcher(tickers):
    data = {}
    for ticker in tickers:
        url = f'https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{startDate}/{endDate}?apiKey={api_key}'
        response = requests.get(url)
        data[ticker]= response.text
    return data
            
    
