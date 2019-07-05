import requests
import base64
import re
from bs4 import BeautifulSoup

checkbox = re.compile("[\[]\s?[\]]")

htmlcontent = "<ol>\n<li><p>Use the <code>engine.table_names()</code> to print the table names from <code>rcsample.db</code> located in the <code>/data</code> folder. How many tables were there?</p>\n<ul>\n<li>[ ] None</li>\n<li>[ ] 3</li>\n<li>[ ] 4</li>\n<li>[ ] 5</li>\n<li>2 points</li>\n</ul>\n</li>\n<li><p>Create an engine just like you did in (1) and execute a SQL query to count the number of rows within the <code>employee</code> table. How many rows are there?</p>\n<ul>\n<li>[ ] 18</li>\n<li>[ ] 28</li>\n<li>[ ] 38</li>\n<li>[ ] 48</li>\n<li>2 points</li>\n</ul>\n</li>"


def ExtractChoices(htmlcontent):
    soup = BeautifulSoup(htmlcontent, "html.parser")
    questions = []
    listitems = []
    lis = []
    for ol in soup.findAll("ol"):
        for quest in ol.findAll("li", recursive=False):
            print(f"question: {quest.find('p')}")
            print("----")
            print(f"choices: {quest.find('ul')}")
            print("----")
            x = list(quest.find("ul").li)
    return questions, listitems, x


q, l, x = ExtractChoices(htmlcontent)
print(q)
print(l)


def readmeReader(repo_url):
    req = requests.get("https://api.github.com/repos/" + repo_url + "/readme")
    json = req.json()
    if "content" in json:
        encoded = bytes(json["content"], encoding="utf-8")
        bodytext = base64.decodebytes(encoded)
    return bodytext


# readmeReader("bagasbgy/tidymodels-examples")
