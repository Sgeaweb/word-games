import requests, pprint
from bs4 import BeautifulSoup
def definition(word):
	page = requests.get("https://www.merriam-webster.com/dictionary/" + word)
	if page.status_code == 200:
		beautiful_page = BeautifulSoup(page.text, features="html.parser")
		def_sep = ""
		definition = beautiful_page.findAll("span", {"class": "dtText"})[0].text.split("\n")[0]
		definition = def_sep.join(definition)

		pprint.pprint(definition)
	elif page.status_code == 404:
		print("Word not in dictionary.")
	else:
		print(page.status_code)