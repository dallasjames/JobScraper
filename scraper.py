import requests
from bs4 import BeautifulSoup


def asc():
    print("   O")
    print("  OOO")
    print("   O\n")
    print("  / )")
    print("  | |")
    print("  | |")
    print("  | |")
    print("  | |")
    print("  ( )")


def indeed():
    asc()
    counter = 0
    url = 'https://www.indeed.com/q-full-stack-developer-l-Boise,-ID-jobs.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='resultsBody')
    jobs = results.findAll('div', class_='jobsearch-SerpJobCard')
    for job in jobs:
        counter += 1
        title = job.find("h2", class_="title")
        location = job.find('span', class_="location")
        location2 = job.find('div', class_="location")
        company = job.find('span', class_="company")
        salary = job.find('span', class_="salaryText")
        print("********************************************************************************")
        print("Title:", title.text.strip())
        if location and not location2:
            print("Location:", location.text.strip())
        elif location2 and not location:
            print("Location:", location2.text.strip())
        print("Company:", company.text.strip())
        if salary:
            print("Salary:", salary.text.strip())
        else:
            print("Salary: Not listed")
    print("********************************************************************************")
    print(counter, "Results from Indeed")


def asc2():
    print("|‾ ‾\\      /‾ ‾|")
    print("| |\\ \\    / /| |")
    print("| | \\ \\  / / | |")
    print("| |  \\ \\/ /  | |")
    print("| |   \\  /   | |")
    print("| |    \\/    | |")
    print("| |          | |")
    print("| |          | |")
    print("|_|          |_|")


def monster():
    asc2()
    counter = 0
    url = 'https://www.monster.com/jobs/search/?q=Full-Stack-Developer&where=Boise__2C-ID'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id="SearchResults")
    cards = results.findAll('section', class_='card-content')
    for card in cards:
        counter += 1
        title = card.find('h2', class_="title")
        company = card.find('div', class_="company")
        location = card.find('div', class_="location")
        if None in (title, company, location):
            continue
        print("********************************************************************************")
        print("Title:", title.text.strip())
        print("Company:", company.text.strip())
        print("Location:", location.text.strip())
    print("********************************************************************************")
    print(counter, " Results from MonsterBoard")


indeed()
monster()
