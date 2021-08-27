#!/usr/bin/env python
# @author   (c) 2019 - 2020 Alexander Puls <https://0vv1.io>
# @license  GPL v3 <https://opensource.org/licenses/GPL-3.0>
# @version  1.3
# note:     Needs an API key from OpenWeatherMap, available
#           for free at https://openweathermap.org.
#           The used font needs to be patched with certain
#           symbols e.g. Weather Icons by Lukas Bischoff
#           (https://www.artill.de/weather-icon-font/).
#           This icons are included in most Nerd-Fonts as
#           nf-weather group icons.
#           See https://nerdfonts.com/#home for more infos.
# ----------------------------------------------------------

import argparse
from datetime import datetime
import requests
import sys

# command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("key", help="API key to retrieve weather data")
parser.add_argument('-f', action='store', dest='ftime', type=float, help="show forecast for given number of hours in advance")
parser.add_argument('-i', '--imperial', action='store_true', help="switch to imperial units")
parser.add_argument('--latitude', action='store', dest='lat', help="use latitude of a location")
parser.add_argument('--longitude', action='store', dest='long', help="use longitude of a location")
parser.add_argument('-p', '--place', action='store_true', help="show location of weather station")
parser.add_argument('-t', '--text', action='store_true', help="print text instead of symbols")
args = parser.parse_args()

# API key assignment via argument
if args.key:
    api_key = args.key
else: sys.exit('No API key given.')

# forecast time argument
if args.ftime:
    if float(args.ftime) >= 0 and float(args.ftime) < 120:
        listID = (int(round(args.ftime)) / 3)
    elif float(args.ftime) == 120:
        listID = 39
    else: sys.exit('Forecast from 0 (now) up to 120 hours.')
else: listID = 0

# temperature unit
if args.imperial:
    units = 'imperial'
else: units = 'metric'

# URL of a location API provider
url_locater = ('http://ip-api.com/json')

# function to get geo location from a provider in case of not given as an argument
def get_location_data():
    try:
        ld = requests.get(url_locater, timeout=9)
    except requests.exceptions.Timeout:
        sys.exit('Connection timed out.')
    except requests.exceptions.TooManyRedirects:
        sys.exit('Tried too many times.')
    except requests.exceptions.HTTPError as herr:
        sys.exit(herr)
    except requests.exceptions.RequestException as reerr:
        sys.exit(reerr)
    return ld.json()

location = get_location_data()

# assign geo location either via argument (first) or location API provider (last)
if args.lat:
    lat = args.lat
else: lat = str(location['lat'])
if args.long:
    lon = args.long
else: lon = str(location['lon'])

# URL of a weather forecast provider (formatted for OpenWeatherMap API)
url_forecast = ('https://api.openweathermap.org/data/2.5/forecast?appid={}&lat={}&lon={}&units={}'.format(api_key, lat, lon, units))

# function for an API call for weather forecasts (OpenWeatherMap)
def get_api_data(api_key, url, lat, lon, units):
    try:
        ad = requests.get(url, timeout=9)
    except requests.exceptions.Timeout:
        sys.exit('Connection timed out.')
    except requests.exceptions.TooManyRedirects:
        sys.exit('Tried too many times.')
    except requests.exceptions.HTTPError as herr:
        sys.exit(herr)
    except requests.exceptions.RequestException as reerr:
        sys.exit(reerr)
    return ad.json()

# variables for JSON request
forecast = get_api_data(api_key, url_forecast, lat, lon, units)

# getting errors from OWM directly? (specific)
if forecast['cod'] == 400 or forecast['cod'] == 401:
    sys.exit(forecast['message'] + '.')
if forecast['cod'] == 404:
    sys.exit(forecast['message'] + ' in API.')
if forecast['cod'] == 429:
    sys.exit('More than 60 API calls a minute.')

# variable assignment for print (OWM specific)
conditionID = forecast['list'][listID]['weather'][0]['id']
conditionMain = forecast['list'][listID]['weather'][0]['main']
cityForecast = forecast['city']['name']
tempForecast = str('%.0f'%round(forecast['list'][listID]['main']['temp']))
timeUnixForecast = forecast['list'][listID]['dt']
timeForecast = datetime.fromtimestamp(timeUnixForecast).strftime("%H:%M")

# daylight? (OWM specific)
if forecast['list'][listID]['sys']['pod'] == 'd':
    daylight = True
else: daylight = False

# Unicode clock symbol assignment
if timeForecast == '00:00' or timeForecast == '12:00':
    symbol_clk = u'\ue381'
elif timeForecast == '01:00' or timeForecast == '13:00':
    symbol_clk = u'\ue382'
elif timeForecast == '02:00' or timeForecast == '14:00':
    symbol_clk = u'\ue383'
elif timeForecast == '03:00' or timeForecast == '15:00':
    symbol_clk = u'\ue384'
elif timeForecast == '04:00' or timeForecast == '16:00':
    symbol_clk = u'\ue385'
elif timeForecast == '05:00' or timeForecast == '17:00':
    symbol_clk = u'\ue386'
elif timeForecast == '06:00' or timeForecast == '18:00':
    symbol_clk = u'\ue387'
elif timeForecast == '07:00' or timeForecast == '19:00':
    symbol_clk = u'\ue388'
elif timeForecast == '08:00' or timeForecast == '20:00':
    symbol_clk = u'\ue389'
elif timeForecast == '09:00' or timeForecast == '21:00':
    symbol_clk = u'\ue38a'
elif timeForecast == '10:00' or timeForecast == '22:00':
    symbol_clk = u'\ue38b'
elif timeForecast == '11:00' or timeForecast == '23:00':
    symbol_clk = u'\ue38c'
else: symbol_clk = u'\uf527'

# output as text only (without Unicode symbols)
if args.text:
    if args.place:
        if args.imperial:
            print(conditionMain + ' at ' + tempForecast + ' degF in ' + cityForecast + ' for ' + timeForecast)
        else: print(conditionMain + ' at ' + tempForecast + ' degC in ' + cityForecast + ' for ' + timeForecast)
    else:
        if args.imperial:
            print(conditionMain + ' at ' + tempForecast + ' degF' + ' for ' + timeForecast)
        else: print(conditionMain + ' at ' + tempForecast + ' degC' + ' for ' + timeForecast)

# Unicode condition symbol assignment depending on API condition IDs and daytime (OWM specific)
else:
    # symbol for API group 200: Thunderstorms
    if conditionID == 200 or conditionID == 210:
        if daylight == True:
            symbol_cond = u'\ue30e'
        else: symbol_cond = u'\ue337'

    elif conditionMain == 'Thunderstorm':
        symbol_cond = u'\ue31d'

    # symbol for API group 300: Drizzle
    elif conditionID == 300 or conditionID == 310:
        if daylight == True:
            symbol_cond = u'\ue309'
        else: symbol_cond = u'\ue334'

    elif conditionMain == 'Drizzle':
        symbol_cond = u'\ue319'

    # symbols for API group 500: Rain
    elif conditionID == 500 or conditionID == 501:
        if daylight == True:
            symbol_cond = u'\ue308'
        else: symbol_cond = u'\ue333'

    elif conditionMain == 'Rain':
        symbol_cond = u'\ue318'

    # symbols for API group 600: Snow
    elif conditionID == 600:
        if daylight == True:
            symbol_cond = u'\ue308'
        else: symbol_cond = u'\ue333'

    elif conditionMain == 'Snow':
        symbol_cond = u'\ue318'

    # symbols for API group 700: Atmosphere
    elif conditionMain == 'Mist':
        symbol_cond = u'\uf75f'

    elif conditionMain == 'Smoke':
        symbol_cond = u'\ue35c'

    elif conditionMain == 'Haze':
        if daylight == True:
            symbol_cond = u'\ue3ae'
        else: symbol_cond = u'\ue37b'

    elif conditionID == 731:
        if daylight == True:
            symbol_cond = u'\ue301'
        else: symbol_cond = u'\ue32d'

    elif conditionMain == 'Fog':
        if daylight == True:
            symbol_cond = u'\ue303'
        else: symbol_cond = u'\ue346'

    elif conditionMain == 'Sand':
        symbol_cond = u'\ue37a'

    elif conditionMain == 'Dust':
        symbol_cond = u'\ue35d'

    elif conditionMain == 'Ash':
        symbol_cond = u'\ue3c0'

    elif conditionMain == 'Squall':
        symbol_cond = u'\ue3c6'

    elif conditionMain == 'Tornado':
        symbol_cond = u'\ue351'

    # symbols for API group 800: Clear
    elif conditionID == 800:
        if daylight == True:
            symbol_cond = u'\ue30d'
        else: symbol_cond = u'\ue32b'

    # symbols for API group 80x: Clouds
    elif conditionID == 801:
        if daylight == True:
            symbol_cond = u'\ue30c'
        else: symbol_cond = u'\ue37b'

    elif conditionID == 802:
        if daylight == True:
            symbol_cond = u'\ue302'
        else: symbol_cond = u'\ue32e'

    elif conditionID == 803:
        symbol_cond = u'\ue312'

    elif conditionID == 804:
        symbol_cond = u'\ue33d'

    # no weather condition from the API? - there is an nf-weather icon for that
    else: symbol_cond = u'\ue345'

    # output with symbols
    if args.place:
        if args.imperial:
            print(symbol_clk + ' ' + symbol_cond + ' ' + tempForecast + u'\u00b0' + 'F in ' + cityForecast)
        else: print(symbol_clk + ' ' + symbol_cond + ' ' + tempForecast + u'\u00b0' + 'C in ' + cityForecast)
    else:
        if args.imperial:
            print(symbol_clk + ' ' + symbol_cond + ' ' + tempForecast + u'\ue341')
        else: print(symbol_clk + ' ' + symbol_cond + ' ' + tempForecast + u'\ue339')

# EOF ${SCR_DIR}/clweather.py ------------------------------
