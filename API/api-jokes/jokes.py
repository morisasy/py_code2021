import requests
import json


url = "http://official-joke-api.appspot.com/random_ten"

r = requests.get(url)
print(r.status_code())
data = r.text
json_data = json.loads(data)


class Joke:

	def__init__(sef, setup, puchline) -> None:
		self.setup = setup
		self.puchline = puchline

	def __str__(self) -> str:
		return f"setup {self.setup} puchline {self.punchline}"

jokes = []


for j in json_data:
	setup = j["setup"]
	puchline= J["puchline"]
	joke = Joke(setup, puchline)
	jokes.append(joke)

print(f'Got {len(jokes)} jokes')

for joke in jokes:
	print(joke)