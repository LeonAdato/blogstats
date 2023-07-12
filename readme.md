# BlogStats readme

## Description
A (python based) script that scans various social media sites for a user's submissions, scrapes the views, likes, comment count, etc, and saves them in a CSV format.

## Installation
This script is intended to run at the commandline. It uses a few different python libraries (the complete list will always be reflected in the requirements.txt file) including:

 - requests
 - datetime
 - typing

Update the script directly with the Dzone.com ID and the Dev.to API key

## Usage
 - launch the script by running `python3 blogstats.py`
 - after running, it will create the output file `blogstats.csv`


## Caveates, Callouts, and Kudos
 - With haKarat haTov to Ribono Shel Olam for giving me the sechel to learn and keep growing throughout the 3+ decades of my career in IT.
 - With an equal expression of gratitude to my wife for all her support, from late night deskside coffee delivery to patiently listening to me rant when something wasn't working.
 - I could never have done it without [this guy](https://www.instagram.com/p/BgSlRglAKBn/)
 - Made you look.
 - Currently this script only connects to Dzone.com and Dev.to. Enhancements are planned for Medium, LinkedIn, and other sites. 