from lxml import html
import requests

def moviePicker():
    hasSeen = False
    while hasSeen == False:
        import random
        page = requests.get('http://www.imdb.com/chart/top')
        tree = html.fromstring(page.content)
        random = random.randint(1, 250)

        title = tree.xpath('//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr[' + str(random) +']/td[2]/a/text()')
        yearReleased = tree.xpath('//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr[' + str(random) + ']/td[2]/span/text()')

        # Parse the movie's url and pull the summary from the details page
        movieUrl = str(tree.xpath('//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr[' + str(random) + ']/td[2]/a/@href'))
        removeFront = movieUrl.replace("['", "")
        cleanUrl = 'http://www.imdb.com' + removeFront.replace("']", "")
        moviepage = requests.get(cleanUrl)
        details = html.fromstring(moviepage.content)
        movieSummary = details.xpath("normalize-space(//div[@class='summary_text']/text())")

        print(title)
        print(yearReleased)
        # print(cleanUrl)
        print(movieSummary)

        while True:
            answer = str.upper((input("Have you already watched this movie? Enter Y or N. : ")))
            if answer in ['Y', 'N']:
                break
            else:
                print("Invalid input. Please enter a Y or a N. ")
                continue
        if answer == 'Y':
            hasSeen = False
        elif answer == 'N':
            print("Enjoy the movie!")
            hasSeen = True

moviePicker()