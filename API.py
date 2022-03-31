import pygal
import requests
from pygal.style import Style
PURL = "https://api.github.com/search/repositories?q=language:python&sort=stars"
JURL = "https://api.github.com/search/repositories?q=language:javascript&sort=stars"
pyresponse = requests.get(PURL)
jsresponse = requests.get(JURL)


print(f"Python status code: {pyresponse.status_code}")
py_response_dict = pyresponse.json()
js_response_dict = jsresponse.json()
print(f"JavaScript status code: {jsresponse.status_code}")
py_repo_dicts = py_response_dict['items']
js_repo_dicts = js_response_dict['items']


py_nimed = []
js_stars = []

i = 0
a = 0

for repo_dict in py_repo_dicts:
    py_nimed.append(py_repo_dicts[a]['stargazers_count'])
    a += 1

for repo_dict in js_repo_dicts:
    js_stars.append(js_repo_dicts[i]['stargazers_count'])
    i += 1

stiil = Style(color = "E71B1B")
config = pygal.Config()

chart = pygal.Bar(style=stiil, x_label_rotation=30, show_legend=True)
chart.title = "Most Starred Python And JavaScript Projects on Github"
chart.add('JavaScript', js_stars)
chart.add('Python', py_nimed)
chart.render_in_browser()