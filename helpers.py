import os
import requests
import urllib.parse
from amadeus import Client, ResponseError

# from flask import redirect, render_template, request, session

def price(origin, destination):
    amadeus = Client(
        client_id='fFbBgDhSL2d0mQr5cgYT1Gw7AMpgoNYG',
        client_secret='qAmJRbY6yyUqId6d'
    )

    try:
        flights = amadeus.shopping.flight_offers_search.get(originLocationCode=origin, destinationLocationCode=destination, departureDate='2022-07-01', adults=1).data
        print(flights[0]['price'])

    except ResponseError as error:
        raise error