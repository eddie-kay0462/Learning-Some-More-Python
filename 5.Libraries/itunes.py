import requests
import sys
import json
if len(sys.argv) != 2:
    sys.exit()


response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=50&term={sys.argv[1]}")

output = response.json()

for result in output["results"]:
    print(result["trackName"])


