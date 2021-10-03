# clweather.py

small weather forecast script for the command line  
[![license: GPL v3](https://img.shields.io/badge/license-GPL--3.0-3da638.svg?style=flat-square&logo=gnu)](https://opensource.org/licenses/GPL-3.0) 
[![script: Python](https://img.shields.io/badge/script-Python-3776ab.svg?style=flat-square&logo=python)](https://python.org) 
[![AUR: clweather](https://img.shields.io/badge/AUR-clweather-1793d1.svg?style=flat-square&logo=arch-linux)](#install) 
  
![cl-weather py.compact](https://0vv1.github.io/img/screenshot/clweather.20191122.compact_tint2.png) &nbsp; ![cl-weather py.text](https://0vv1.github.io/img/screenshot/clweather.20191122.text_tint2.png)  
  
## description

Shows weather forecast on the command line. Defaults to the next coming measuring point in time.  
Uses the forecast API of OpenWeatherMap and therefore needs an API key from OWM.  
Free of charge for personal use at https://openweathermap.org.  
  
## features

 * shows __Unicode symbol__ by default depending on weather condition and daytime..  
 * in order to show (the correct) Unicode symbols the used font needs to be patched with Weather Icons e.g. NerdFonts containing the nf-weather group icons  
 * Weather Icons originally designed by Lukas Bischoff (https://artill.de)  
   (see https://github.com/ryanoasis/nerd-fonts for details)  
 * ..but has a switch to toggle to '__text mode__ only'  
 * if no geo location is provided via cl argument the API of a location provider is called to determine the __current location__  
 * has a switch to use __imperial__ units instead of (default) __metric__  
 * shows __location__ of the used __weather station__ if the parameter `-p` is set  
  
## install

Just put the executable script anywhere inside your `$PATH` or link to it from elsewhere.  
There also is an AUR package at https://aur.archlinux.org/packages/clweather.  
 
### depends on

*   `python` to interpret the script   
*   python lib `argparse` for use of command line parameters  
*   python lib `requests` to grab JSON data from online APIs  
  
## synopsis
execute `clweather.py [option(-s) ..] KEY`  
or `clweather [option(-s) ..] KEY` (if installed systemwide via `PKGBUILD`)

### mandatory argumenent

`KEY` to access weather forecast API  

### options

`-h, --help`       shows help message and exits  
`-i, --imperial`   switches to imperial units  
`--latitude LAT`   uses latitude of a location  
`--longitude LONG` uses longitude of a location  
`-p, --place`      shows location of weather station  
`-t, --text`       prints text instead of symbols  
