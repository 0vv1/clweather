#!/usr/bin/env python
# @author   (c) 2019 Alexander Puls <https://0vv1.io>
# @license  GPL v3 <https://opensource.org/licenses/GPL-3.0>
# @version  1.0
# note:     Needs an API key from OpenWeatherMap, available
#           for free at https://openweathermap.org.
#           Needs a font patched with Nerd Font patches to
#           show the correct Unicode symbols of the
#           Nerd Font nf-weather group.
#           See https://nerdfonts.com/#home.
# ----------------------------------------------------------

import argparse
import json
import requests
#import time
#import datetime
import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

# command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-f', action='store', dest='ftime', type=int, help="show forecast for given number of hours in advance")
parser.add_argument('-i', '--imperial', action='store_true', help="switch to imperial units")
parser.add_argument('-k', '--key', action='store', dest='key', help="use api key to retrieve weather data")
parser.add_argument('--latitude', action='store', dest='lat', help="use latitude of a location")
parser.add_argument('--longitude', action='store', dest='long', help="use longitude of a location")
parser.add_argument('-p', '--place', action='store_true', help="show location of weather station")
parser.add_argument('-t', '--text', action='store_true', help="print text instead of symbols")
args = parser.parse_args()

# geolocation via api of ip-api.com in case of no location given
url_locate = ('http://ip-api.com/json')

def get_location_data():
    ld = requests.get(url_locate)
    return ld.json()

location = get_location_data()

# variables for weather api
if args.key:
    api_key = args.key
else: sys.exit('No api key given.')

if args.ftime:
    if int(args.ftime) == 0:
        listID = 0
    elif int(args.ftime) > 0 and int(args.ftime) <= 120:
        listID = ((args.ftime - 1) / 3)
    else: sys.exit('Forecast(!) up from soon to 120 hours.')
else:
    listID = 0

if args.imperial:
    units = 'imperial'
else: units = 'metric'

# assign geolocation for weather api
if args.lat:
    lat = args.lat
else: lat = str(location['lat'])
if args.long:
    lon = args.long
else: lon = str(location['lon'])

url_forecast = ('https://api.openweathermap.org/data/2.5/forecast?appid={}&lat={}&lon={}&units={}'.format(api_key, lat, lon, units))

#url_weather = ('https://api.openweathermap.org/data/2.5/weather?appid={}&lat={}&lon={}&units={}'.format(api_key, lat, lon, units))

def get_api_data(api_key, url, lat, lon, units):
    # actual api call
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

def main():
    # variables for JSON request
    #weather = get_api_data(api_key, url_weather, lat, lon, units)
    forecast = get_api_data(api_key, url_forecast, lat, lon, units)
    conditionID = forecast['list'][listID]['weather'][0]['id']
    conditionMain = forecast['list'][listID]['weather'][0]['main']
    cityForecast = forecast['city']['name']
    tempForecast = str('%.0f'%round(forecast['list'][listID]['main']['temp']))
    #timeForecast = forecast['list'][listID]['dt']
    #timeSunrise = weather['sys']['sunrise']
    #timeSunset = weather['sys']['sunset']

    # daylight?
    if forecast['list'][listID]['sys']['pod'] == 'd':
        daylight = True
    else: daylight = False

    # return errors from API
    if forecast['cod'] == 400 or forecast['cod'] == 401:
        sys.exit(forecast['message'] + '.')
    elif forecast['cod'] == 404:
        sys.exit(forecast['message'] + ' in API.')
    elif forecast['cod'] == 429:
        sys.exit('More than 60 API calls a minute.')

    else:
        # output without Unicode symbol
        if args.text:
            if args.place:
                if args.imperial:
                    print(conditionMain + ' at ' + tempForecast + ' degF in ' + cityForecast)
                else: print(conditionMain + ' at ' + tempForecast + ' degC in ' + cityForecast)
            else:
                if args.imperial:
                    print(conditionMain + ' at ' + tempForecast + ' degF')
                else: print(conditionMain + ' at ' + tempForecast + ' degC')

        # clock symbol for multiple forecast times in a row
        # TODO like u'\ue383'

        # Unicode condition symbol assignment depending on API condition IDs and daytime
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

            # no condition id from API - Nerd Fonts has an nf-weather icon for that
            else:
                symbol_cond = u'\ue345'

            # output with symbol
            if args.place:
                if args.imperial:
                    print(symbol_cond + ' ' + tempForecast + u'\u00b0' + 'F in ' + cityForecast)
                else:
                    print(symbol_cond + ' ' + tempForecast + u'\u00b0' + 'C in ' + cityForecast)
            else:
                if args.imperial:
                    print(symbol_cond + tempForecast + u'\ue341')
                else:
                    print(symbol_cond + tempForecast + u'\ue339')

if __name__ == '__main__':
        main()

# EOF ${SCR_DIR}/clweather/clweather.py --------------------
