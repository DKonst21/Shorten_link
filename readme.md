# Bitly URL shortener
Getting the number of clicks on a short link.

## Setting up the environment.
To run the application, you need to get a token from [app.bitly.com/settings/api/](https://app.bitly.com/settings/api/). In the "access token" section, enter the password for your account on the site and click the button "generate key". The token name BITLY_TOKEN contains the value of the API-key and is located in .env.

### How to get a short link through terminal
Launch through terminal: 
#### ```python main.py https://api-ssl.bitly.com```

## How to install

Python3 should already be installed. Use pip (or pip3, if there is a conflict with Python2) to install dependencies:

#### ```pip install -r requirements.txt```

it is recommended to use [virtualenv/venv](https://docs.python.org/3/library/venv.html) for project isolation

## Project Goals
This code was written for educational purposes as part of an online course for web developers at 
[dvmn.org](https://dvmn.org/).