# clweather.py  
small weather forecast script for the command line  
[![license: GPL v3](https://img.shields.io/badge/license-GPL--3.0-3da638.svg?style=flat-square&logo=gnu)](https://opensource.org/licenses/GPL-3.0) 
[![donate Bitcoins](https://img.shields.io/badge/donate-Bitcoin-f79413.svg?style=flat-square&logo=bitcoin)](#donations)  
  
  ![20190426_cl-weather py_inTint2](https://raw.githubusercontent.com/0vv1/Oystagony/assets/scrot/cl-weather.py_%40tint2_20190426.png) &nbsp; &nbsp; ![20190427_cl-weather py_FwP_inTint2](https://raw.githubusercontent.com/0vv1/Oystagony/assets/scrot/cl-weather.py_text_%40tint2_20190427.png) &nbsp; &nbsp; ![20190427_cl-weather py_ot_inTint2](https://raw.githubusercontent.com/0vv1/Oystagony/assets/scrot/cl-weather.py_extnsv_%40tint2_20190427.png)  
  
## description
Shows the forecast of the coming measuring point within the next three hours by default.
Uses the forecast API of OpenWeatherMap, therefore needs an API key from OWM being handed over via -k switch.
Free of charge at https://openweathermap.org.

## features
 * shows __Unicode symbol__ by default depending on weather condition and daytime
 * therefore works with any font being patched with NerdFonts, but has a switch to toggle to '__text mode__ only' showing the main weather condition at the given time
 (see https://github.com/ryanoasis/nerd-fonts or https://nerdfonts.com for details)
 * by default the API of ip-api-com is called to determine the __current location__ if none is provided via cl parameters
 * has a switch to toggle to __imperial units__, while using __metric units__ by default
 * shows __location of weather station__ if the parameter -p is set

## depends on
 * `python lib argparse`
    for convenient use of command line parameters
 * `python lib requests`
    to grab JSON data from an API

## synopsis
`clweather.py [option ..]`

### options
`-h, --help`  
  show this help message and exit  
`-i, --imperial`  
  switch to imperial units  
`-k KEY, --key KEY`  
  use api key to retrieve weather data  
`--latitude LAT`  
  use latitude of a location  
`--longitude LONG`  
  use longitude of a location  
`-p, --place`  
  show location of weather station  
`-t, --text`  
  print text instead of symbols

## donations
![bc address btn](https://raw.githubusercontent.com/0vv1/Oystagony/assets/button/bc-add.png)  

