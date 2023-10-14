import requests

BASE_URL = "https://api.the-odds-api.com/v4"

# TODO
# - Account for arbitrages across bookmakers

def get_sports(key) -> list:
    url = f"{BASE_URL}/sports/"

    response = requests.get(url, params= {
        "apiKey" : key
    })

    return list({sport["key"] for sport in response.json()})

def get_data(key, sport, regions, markets) -> list:

    url = f"{BASE_URL}/sports/{sport}/odds/"

    response = requests.get(url, params={
        "apiKey" : key,
        "regions" : ",".join(regions),
        "markets" : ",".join(markets),
        "oddsFormat" : "decimal" # American = +/-100 * (fraction odds of winning or losing, whichever >= 1). Sign based on win/loss

        # finding select bookmakers with frequent mispricings would improve arbitrage finding rates
        # "bookmakers" : TBA
    })

    print('Remaining requests', response.headers['x-requests-remaining'])
    print('Used requests', response.headers['x-requests-used'])
    
    return response.json()

def filter_arbitrages(data, threshold):
    arbitrages = {}
    for match in data:
        for bookmaker in match["bookmakers"]:
            for market in bookmaker["markets"]:
                implied_odds = sum(1/outcome["price"] for outcome in market["outcomes"])
                
                if implied_odds < 1 - threshold:

                    match_name = f'{match["home_team"]} vs. {match["away_team"]}'

                    if implied_odds > arbitrages.get(match_name, (-1, -1, -1))[-1]:
                        arbitrages[match_name] = {"bookmaker" : bookmaker["key"], "market" : market["key"], "odds" : implied_odds}

    return arbitrages

def get_arbitrages(key, regions, markets, numSports, threshold):
    sports = get_sports(key)

    for i in range(min(len(sports), numSports)):
        sport = sports[i]
        pricings_data = get_data(key, sport, regions, markets)
        arbitrages = filter_arbitrages(pricings_data, threshold) 

        if len(arbitrages) == 0:
            print(f"No arbitrages found for threshold {threshold} in sport {sport}.")

        for match_name in arbitrages:
            details = arbitrages[match_name]
            print(f'Sport: {sport}, Match: {match_name}, Bookmaker: {details["bookmaker"]}, \
                Market: {details["market"]}, Total Implied Odds: {details["odds"]}')