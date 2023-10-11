import argparse
import os
from logic import get_arbitrages

parser = argparse.ArgumentParser(
            prog='ArbitrageFinder',
            description='Finds arbitrages for a certain amount of sports using Odds API!')

parser.add_argument(
    "-k", "--key",
    default=os.environ.get("ODDS_API_KEY"),
    help="The API key of Odds API. Defaults to ODDS_API_KEY in environment."
)
parser.add_argument(
    "-r", "--regions",
    choices=["us", "us2", "eu", "au", "uk"],
    nargs = "+",
    default="us2",
    help="The region (or multiple regions) to be surveyed"
)
parser.add_argument(
    "-m", "--markets",
    choices=["h2h", "spreads", "totals"],
    nargs = "+",
    default="h2h",
    help="The market (or multiple markets) to be surveyed"
)
parser.add_argument(
    "-s", "--numsports",
    type=int,
    default=1,
    help="Number of sports to survey"
)
parser.add_argument(
    "-t", "--threshold",
    type=float,
    default=0.0,
    help="Accounts for percentage losses from vigorish (percentage commission fee from 0 to 1)"
)

args = parser.parse_args()

get_arbitrages(args.key, args.regions, args.markets, args.numsports, args.threshold)
