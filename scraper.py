from bs4 import BeautifulSoup as bsoup
import requests as req 
import constants as const 
import csv


movies = []

def get_year():
    year = input()
    # try:
        # year = int(year)
    main(year)
        # print(year)
    # except ValueError:
    #     if year == "-help":
    #         help_prompt()
    #     elif year == "exit":
    #         exit()
    #     else:
    #         print("Enter a valid year eg:1950, 2000, 2023")
    #         get_year()

def help_prompt():
    print("help todo")
    # TODO: need to loop back to get the year value
    

def main(year):
    response = req.get(f"{const.MOVIE_BASE_URL}{year}-01-01,{year}-12-31")
    bs = bsoup(response.text, "html.parser")

    searches = bs.find_all(class_=const.TITLE_CONTAINER)

    count = bs.find(class_="desc").find("span").text.strip().split(" ")[2]

    total_movies = int(count.replace(",",""))

    scrap_page(searches)
    
    if total_movies > 50:
        set = 1
        while total_movies >=0:
            response = req.get(f"{const.MOVIE_BASE_URL}{year}-01-01,{year}-12-31&start={(set*50)+1}")
            new_page = bsoup(response.text, "html.parser")
            searches = bs.find_all(class_=const.TITLE_CONTAINER)
            scrap_page(searches)
            total_movies -= 50
            set += 1

    write_csv()

def scrap_page(searches):
    for item in searches:
        index = item.find(class_=const.INDEX).text.strip()[:-1]   
        title = item.find(const.TAG_H3).find(const.TAG_A).text.strip()
        try:
            certificate = item.find("p").find(class_=const.CERTIFICATE).text.strip()
        except:
            certificate = "None"
        genre = item.find("p").find(class_=const.GENRE).text.strip()
        runtime = item.find("p").find(class_=const.RUNTIME).text.strip()
        rating = item.find(class_=const.RATING).find("strong").text.strip()

        movie = {
                "index": index,
                "title": title,
                "certificate": certificate,
                "genre": genre,
                "runtime": runtime,
                "rating": rating
                }

        movies.append(movie)

def write_csv():

    with open("movies19.txt", "w") as f:
        f.write(str(movies))
    
    with open('movies19.csv', 'w') as f:  # You will need 'wb' mode in Python 2.x
        writer = csv.writer(f)
        header = ["index", "title", "certificate", "genre", "runtime", "rating"]
        writer.writerow(header)

        for movie in movies:
            value = []
            for k, v in movie.items():
                value.append(v)
            writer.writerow(value)
    
    print("fin")


if __name__ == "__main__":
    print()
    print("Welcome to Movie Scrapper! Scrap all movie releases by year")
    print()
    print("Enter the year to scrap all the titles..")
    print("Enter -help to get help")
    print()

    get_year()   


