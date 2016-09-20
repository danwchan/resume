from pyzotero import zotero

#this is your Zotero login info
from secrets import userID,key

library = zotero.Zotero(userID, 'user', key)

for c in library.collections():
  if c['data']['name'] == "my_publications":
    fetchID = c['key']

fetchbibtex = library.collection_items(fetchID, include = 'bibtex')

with open('my_publications.bib', 'w') as file:
  for items in fetchbibtex:
    file.write(items['bibtex'].encode('utf-8'))

file.close()