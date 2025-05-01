import requests
from django.shortcuts import render
from .models import Price
from datetime import datetime

def dashboard(request):
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    response = requests.get(url).json()

    btc_price = response["bitcoin"]["usd"]
    eth_price = response["ethereum"]["usd"]

    # Save the price to your database
    Price.objects.create(asset="Bitcoin", price=btc_price, timestamp=datetime.now())
    Price.objects.create(asset="Ethereum", price=eth_price, timestamp=datetime.now())

    context = {
        "btc_price": btc_price,
        "eth_price": eth_price
    }
    return render(request, "tracker/dashboard.html", context)

