# movie-scraper
This is a python web scrapper to scrape all the movie released from a given year from the IMBD database. 

## Clone the project
The packages used in the project are installed in a python virtual environment to avoid conflicts with existing packages. Follow the steps to clone and run the project in jupyter notebook
```
https://github.com/rama-2402/imdb-scraper.git
cd movie-scraper/
```
After navigating to the project directory, Create a virtual environment and install the packges using the following commands.
```
python3 -m venv venv/

#If you are using bash shell 
source venv/bin/activate 

#If you are using Fish shell
source venv/bin/activate.fish

#To install the necessary dependencies
pip install -r requirements.txt 
```
## Troubleshooting
```
#Nuke the environment
rm -r venv/

#Install a new environment and dependencies
python3 -m venv venv/                 
pip install -r requirements.txt 
```
## Run the scraper
```
python3 scraper.py 
```
