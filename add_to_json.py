import json
from utils import urls_from_blog, get_timeline_data, links_not_in_doc
from datetime import date


data = get_timeline_data()
links = links_not_in_doc(data['events'], urls_from_blog())
new_events = []

"""data_censura = get_timeline_data(True)
links_censura = links_not_in_doc(data_censura['events'], urls_from_blog())
new_events_censura = []"""

for link in links:

    slash_idx = link.rfind('/')
    dot_idx = link.rfind('.')

    last_part = link[slash_idx+1 : dot_idx].split('p')[0]
    date = last_part.split('_')
    try:
      date[2] = '20' + date[2]
    except IndexError:
      continue

    new_events += [{
        "media": {
          "url": link,
          "caption": "",
          "credit": ""
        },
        "start_date": {
          "month": date[1],
          "day": date[0],
          "year": date[2]
        },
        "text": {
          "headline": "------- ADICIONAR HEADLINE -------",
          "text": f"<p>------- ADICIONAR TEXTO -------</p>"
        }
      }]

data['events'] += new_events
#print(sorted(data['events'], key=lambda e : date(year=int(e['ano']), month=int(e['']))))

with open('timeline.json', 'w') as file:
    json.dump(data, file)
