# clweather.py  
  a small weather forecast script for the command line  
  
  ![20190426_cl-weather py_inTint2](https://user-images.githubusercontent.com/19635210/56842723-d1760080-6898-11e9-8f7c-0b47a067b0cb.png)  
  ![20190427_cl-weather py_FwP_inTint2](https://user-images.githubusercontent.com/19635210/56851279-81855100-690d-11e9-8345-2e4660638c85.png)  
  ![20190427_cl-weather py_ot_inTint2](https://user-images.githubusercontent.com/19635210/56851285-9d88f280-690d-11e9-9610-d2b0778115b7.png)
  
## description
Shows the forecast of the coming measuring point within the next three hours by default.
Uses the free forecast API of OpenWeatherMap, therefore needs an API key from OWM being handed over via -k switch.
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
