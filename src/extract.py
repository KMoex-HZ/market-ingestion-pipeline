import requests
import pandas as pd
from datetime import datetime

def fetch_market_data():
    """
    Fetches cryptocurrency price data from the CoinGecko API.
    Retrieves current USD prices and timestamps for Bitcoin, Ethereum, and Solana.
    
    Returns:
        pd.DataFrame: A formatted DataFrame containing coin names, prices, and timestamps.
    """
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd&include_last_updated_at=true"
    
    # Send GET request to the API
    response = requests.get(url)
    
    # Parse JSON response
    data = response.json()

    rows = []
    for coin, info in data.items():
        rows.append({
            'coin_name': coin,
            'price_usd': info['usd'],
            'updated_at': datetime.fromtimestamp(info['last_updated_at'])
        })
    
    # Return processed data as a pandas DataFrame for easier downstream loading
    return pd.DataFrame(rows)