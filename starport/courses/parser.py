import requests
import base64

def readmeReader(repo_url):
    req = requests.get("https://api.github.com/repos/" + repo_url + "/readme")  
    json = req.json()
    if "content" in json:
        encoded = bytes(json["content"], encoding="utf-8")
        bodytext = base64.decodebytes(encoded)
    return bodytext

readmeReader("bagasbgy/tidymodels-examples")