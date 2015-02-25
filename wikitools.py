import urllib
import json
import time
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

class WikiSolver:
	"""A number of functions to be used with Wikipedia and its API"""
	def __init__(self, linkInit, linkFinal):
		self.linkInit = linkInit
		self.linkFinal = linkFinal
		self.dict_links = []

	def get_source(self, link):
		webPage = urllib.urlopen(link)
		source = webPage.read()	
		webPage.close()
		return source

	def json_to_dict(self, jsonStr):
		json_data = json.loads(jsonStr)
		return json_data

	def crawl(self, initial_link):
		pass

	def get_page_id(self, wiki_link):
		source = self.get_source(wiki_link)
		index_of_ID = source.find("wgArticleId")
		index_of_ID = index_of_ID + 13

		ID = ""
		while is_number(source[index_of_ID]):
			ID = ID + source[index_of_ID]
			index_of_ID = index_of_ID + 1

		return ID

	def generate_link(self, ID):
		return "http://en.wikipedia.org/wiki/index.html?curid=" + ID

	def get_API_link(self, ID):
		#Reread the API for this, maybe search multiple IDs? pageids=ID|ID|ID
		return "http://en.wikipedia.org/w/api.php?action=query&format=json&pageids=" + ID + "&generator=links&gpllimit=max"

	def search_link(self, search):
		return "http://en.wikipedia.org/wiki/" + search.replace(" ", "_")

	def get_all_IDs(self, ID):
		link = self.get_API_link(ID)
		source = self.get_source(link)
		IDs = self.json_to_dict(source)['query']['pages'].keys()
		return IDs

	def extract_words(self, ID):
		link = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&pageids=" + ID
		return self.json_to_dict(self.get_source(link))

w = WikiSolver("Isaac Newton", "Apple")
#print w.get_source("http://en.wikipedia.org/w/api.php?action=query&format=json&pageids=14627&generator=links&gpllimit=max")

#print w.get_page_id(w.search_link("Isaac Newton"))
link = w.search_link("Isaac Newton")
ID = w.get_page_id(link)
links_on_page = w.get_all_IDs(ID)
words = w.extract_words(ID)
print words
