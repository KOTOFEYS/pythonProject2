< strong > < em >
import < / em > < / strong > requests
< strong > < em >
from < / em > < / strong > bs4 < strong > < em >
import < / em > < / strong > BeautifulSoup
URL = "https://www.x-rates.com/table/?from=USD&amount=1"
r = requests.get(URL)
soup = BeautifulSoup(r.content, "html.parser")
ratelist = soup.findAll("table", {"class": "ratesTable"})[0].findAll("tbody")
< strong > < em >
for < / em > < / strong > tableVal < strong > < em > in < / em > < / strong > ratelist:
    trList = tableVal.findAll("tr")
    < strong > < em >
    for < / em > < / strong > trVal < strong > < em > in < / em > < / strong > trList[:6]:
    print(trVal.text)