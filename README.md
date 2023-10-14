# Arbitrage Bet Finder
A tool for finding arbitrages using implicit odds. This repository contains a notebook version, simple code version, and command-line interface. This repository relies on [Odds API](https://the-odds-api.com/).

Note that it's often true that there are no arbitrages -- bookmakers verify their pricings very often and mispricings often only occur in less popular sports/markets (e.g. college sports, totals, local tournaments). Try to download `code_only.py` and print `sports` to find the least popular sports with highest arbitrage chance to save your API calls! Finding arbitrages is very time specific since they are removed once they are discovered.

Also, note the importance of `THRESHOLD` since there will often be fees for placing bets in houses. 

## 💻 CLI Install

In order to interact with the commandline interface, clone the project with

```
  git clone https://github.com/nathanjzhao/Arbitrage-Bet-Finder.git
```

Then, in terminal, enter

```
  python find_arbitrages.py --key <YOUR_API_KEY>
```

for running the initial commands

## Usage

`-k`, `--key`: Your [Odds API](https://the-odds-api.com/) key.
`-r`, `--regions`: The region (or multiple regions) to be surveyed. The different regions choices for bookmakers are `["us", "us2", "eu", "au", "uk"]`.
`-m`, `--markets`: The market (or multiple markets) to be surveyed. The different market choices of this project are `["h2h", "spreads", "totals"]`.
`-s`, `--numsports`: The number of sports to survey. Control based on your API key's request limitations!
`-t`, `--threshold`: The threshold for returning arbitrages. Accounts for percentage losses from vigorish (percentage commission fee from 0 to 1).

