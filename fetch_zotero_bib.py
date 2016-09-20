from pyzotero import zotero

#this is your Zotero login info
import secrets

library = zotero.Zotero(userID, 'user', key)

for c in library.collections():
  if c['data']['name'] == "my_publications":
    fetchID = c['key']

fetchbibtex = zot.collection_items(fetchID, include = 'bibtex')

with open('my_publications.bib', 'w') as file:
  for items in fetchbibtex:
    file.write(items['bibtex'].encode('utf-9'))

file.close()