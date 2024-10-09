import json
from utils import urls_from_blog, get_timeline_data, links_not_in_doc
from youtube_auto import get_videos_from_channel, youtube_auto
from datetime import date

def append_blog_images():

  data = get_timeline_data()
  links = links_not_in_doc(data['events'], urls_from_blog())
  new_events = []

  for link in links:

      slash_idx = link.rfind('/')
      dot_idx = link.rfind('.')

      last_part = link[slash_idx+1 : dot_idx].split('p')[0]
      date_ = last_part.split('_')
      try:
        date_[2] = '20' + date_[2]
      except IndexError:
        continue

      new_events += [{
          "media": {
            "url": link,
            "caption": "",
            "credit": ""
          },
          "start_date": {
            "month": date_[1],
            "day": date_[0],
            "year": date_[2]
          },
          "text": {
            "headline": "------- ADICIONAR HEADLINE -------",
            "text": f"<p>------- ADICIONAR TEXTO -------</p>"
          }
        }]

  data['events'] += new_events
  data['events'] = sorted(data['events'], key=lambda e : date(year=int(e["start_date"]['year']), month=int(e["start_date"]['month']), day=int(e["start_date"]['day'])))

  with open('timeline.json', 'w') as file:
    json.dump(data, file)
    print('File updated!')

#------------------------------------------------------------------------------------------------------------------------------------------------------

def append_yt_videos():

  data = get_timeline_data()

  youtube_client = youtube_auto()
  video_links = get_videos_from_channel(youtube_client)

  links = links_not_in_doc(data['events'], video_links, tuples=True)
  new_events = []

  for name, link in links:

      name = name.split('p')[0].split(' ')

      if 'VID' in name:
        continue

      try:
        name[2] = '20' + name[2]
      except IndexError:
        continue

      new_events += [{
          "media": {
            "url": link,
            "caption": "",
            "credit": ""
          },
          "start_date": {
            "month": name[1],
            "day": name[0],
            "year": name[2]
          },
          "text": {
            "headline": "------- ADICIONAR HEADLINE -------",
            "text": f"<p>------- ADICIONAR TEXTO -------</p>"
          }
        }]
      
  print(new_events)
  data['events'] += new_events
  data['events'] = sorted(data['events'], key=lambda e : date(year=int(e["start_date"]['year']), month=int(e["start_date"]['month']), day=int(e["start_date"]['day'])))

  with open('timeline.json', 'w') as file:
    json.dump(data, file)
    print('File updated!')
  
append_yt_videos()