# clweather.py  
small weather forecast script for the command line  
[![license: GPL v3](https://img.shields.io/badge/license-GPL--3.0-3da638.svg?style=flat-square&logo=gnu)](https://opensource.org/licenses/GPL-3.0) 
[![donate Bitcoins](https://img.shields.io/badge/donate-Bitcoin-f79413.svg?style=flat-square&logo=bitcoin)](#donations)  
  
  ![cl-weather py.compact](https://raw.githubusercontent.com/0vv1/Oystagony/assets/scrot/20191122_cl-weather.py_compact_tint2.png) &nbsp; &nbsp; ![cl-weather py.text](https://raw.githubusercontent.com/0vv1/Oystagony/assets/scrot/20191122_cl-weather.py_text_tint2.png)  
  
## description
Shows the forecast of the next measuring point within the next three hours by default.  
Uses the forecast API of OpenWeatherMap and therefore needs an API key from OWM being handed over via -k switch.  
Free of charge at https://openweathermap.org.  

## features
 * shows __Unicode symbol__ by default depending on weather condition and daytime..  
 * in order to show (the correct) Unicode symbols the used font needs to be patched with NerdFonts containing the nf-weather group icons  
 * Weather Icons originally designed by Lukas Bischoff (https://artill.de)  
 * see https://github.com/ryanoasis/nerd-fonts for details  
 * ..but has a switch to toggle to '__text mode__ only'  
 * if no geo location is provided via cl the (free) API of a location provider is called to determine the __current location__  
 * has a switch to toggle to __imperial units__ and back to __metric__  
 * shows __location of__ the used __weather station__ if the parameter `-p` is set

## depends on
*   python lib `argparse`  
    for convenient use of command line parameters  
*   python lib `requests`  
    to grab JSON data from an API  
*   python libs `time` and `datetime`  
    to deal with forecast times later then default  

## synopsis
`clweather.py [option ..]`

### options
`-h, --help`  
    show this help message and exit  
`-a (API-)KEY`  
    use api key to retrieve weather data  
`-i, --imperial`  
    switch to imperial units  
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

