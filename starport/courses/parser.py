import requests
import base64
import re
from bs4 import BeautifulSoup
from quizdown.models import QuestionSet, Question, Choice

checkbox = re.compile("(?<=<li>[\[]\s[\]])(\s?)(.+)(?=</li>)")

htmlcontent = "<ol>\n<li><p>Use the <code>engine.table_names()</code> to print the table names from <code>rcsample.db</code> located in the <code>/data</code> folder. How many tables were there?</p>\n<ul>\n<li>[ ] None</li>\n<li>[ ] 3</li>\n<li>[ ] 4</li>\n<li>[ ] 5</li>\n<li>2 points</li>\n</ul>\n</li>\n<li><p>Create an engine just like you did in (1) and execute a SQL query to count the number of rows within the <code>employee</code> table. How many rows are there?</p>\n<ul>\n<li>[ ] 18</li>\n<li>[ ] 28</li>\n<li>[ ] 38</li>\n<li>[ ] 48</li>\n<li>2 points</li>\n</ul>\n</li>"


def ExtractChoices(htmlcontent, cs_id):
    soup = BeautifulSoup(htmlcontent, "html.parser")
    questions = []
    maxscore = 0
    num_of_questions = 0
    qs = QuestionSet(cs_id=cs_id)
    qs.save()
    for ol in soup.findAll("ol"):
        for quest in ol.findAll("li", recursive=False):
            num_of_questions += 1
            choices = []
            prompt = quest.find("p")
            print(f"question: {prompt}")
            print("----")
            x = list(quest.find("ul").findAll("li"))
            x = list(map(str, x))
            p_matched = re.search(
                "(?<=<li>)(\s?)(\d+)(?=\s?(point|points)</li>)", x[-1]
            )
            if p_matched:
                score = p_matched.group(2)
                del x[-1]
            else:
                score = 1
            maxscore += int(score)
            for choice in x:
                choices.append(
                    re.search("(?<=<li>[\[]\s[\]])(\s?)(.+)(?=</li>)", choice).group(2)
                )
            print(choices)
            q = Question(prompt=prompt, questionscore=score, questionset=qs)
            q.save()
            Choice.objects.bulk_create(
                [Choice(content=i, question=q) for choice in choices]
            )
    passingscore = max(1, int(maxscore * 0.8))
    print(f"Num of questions: {num_of_questions}")
    qs.maxscore = maxscore
    qs.passingscore = passingscore
    qs.save()
    return maxscore


maxscore = ExtractChoices(htmlcontent, 14)

# Testing:
# Check if capturing the choice ignoring html tags
# re.search("(?<=<li>[\[]\s[\]])(\s?)(.+)(?=</li>)", x[2]).group(2)
# re.search("(?<=<li>)(\s?)(\d+)(?=\s?(point|points)</li>)", x[4]).group(2)


def readmeReader(repo_url):
    req = requests.get("https://api.github.com/repos/" + repo_url + "/readme")
    json = req.json()
    if "content" in json:
        encoded = bytes(json["content"], encoding="utf-8")
        bodytext = base64.decodebytes(encoded)
    return bodytext


# readmeReader("bagasbgy/tidymodels-examples")


for choice in x:
    choices.append(re.search("(?<=<li>[\[]\s[\]])(\s?)(.+)(?=</li>)", choice).group(2))
    print(choices)
