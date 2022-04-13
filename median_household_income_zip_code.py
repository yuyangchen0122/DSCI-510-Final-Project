# Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape():
    URL = "http://www.usa.com/rank/california-state--median-household-income--zip-code-rank.htm"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="hcontent")
    table = results.find("table")

    # Obtain every title of columns with tag <th>
    headers = []
    table_content = table.find_all('tr')
    first_line = table_content[0]
    first_line_content = first_line.find_all('td')
    for i in range(len(first_line_content)):
        if i == 0:
            headers.append(first_line_content[i].text.replace('.', ''))
        elif i == 1:
            headers.append(first_line_content[i].text[:-2])
        else:
            zip, population = first_line_content[i].text.split(' / ')[0], first_line_content[i].text.split(' / ')[1]
            headers.append(zip)
            headers.append(population)
    data = pd.DataFrame(columns=headers)
    # Create a for loop to fill mydata
    for j in table_content[1:]:
        row_data = j.find_all('td')
        row = [i.text for i in row_data]
        row[0] = int(row[0].replace('.', ''))
        row[1] = int(row[1].replace(',', '').replace('$', ''))
        zip, population = int(row[2].split(' / ')[0]), int(row[2].split(' / ')[1].replace(',', ''))
        row[2] = zip
        row.append(population)
        length = len(data)
        data.loc[length] = row
    print(data.head())


if __name__ == '__main__':
    scrape()