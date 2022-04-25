from amadeus import Client, ResponseError

def price():
    amadeus = Client(
        client_id='fFbBgDhSL2d0mQr5cgYT1Gw7AMpgoNYG',
        client_secret='qAmJRbY6yyUqId6d'
    )

    try:
        flights = amadeus.shopping.flight_offers_search.get(originLocationCode='SYD', destinationLocationCode='LOS', departureDate='2022-07-01', adults=1).data
        print(flights[0]['travelerPricings'][0]['fareDetailsBySegment'][0]['cabin'])

    except ResponseError as error:
        raise error

