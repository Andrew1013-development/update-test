import requests
import os
import tqdm
update_dir = os.path.join(os.path.dirname(__file__),"main1.py") #directory to place updated code
update_url = "" #link to download updated code
response = requests.get(update_url,stream=True)
with open(update_dir,"wb") as handler :
    if response.ok : 
        print(response)
    for block in tqdm(response.iter_content(1024)) :
        if not block :
            break
        handler.write(block)
