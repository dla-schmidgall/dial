#!/usr/bin/env python3
import re

with open("../../../dial.bib", "r") as fh:
	bib = fh.read()

# Typographische Anpassungen:
bib = re.sub("\\\\enquote{(.+?)}",r"»\1«",bib) # Latex-Quotation austauschen
bib = re.sub("\\\\emph{(.+?)}",r"\1",bib) # Latex-Quotation austauschen
bib = re.sub("„","»",bib) # Anführungszeichen austauschen
bib = re.sub("“","«",bib) # Abführungszeichen austauschen
bib = re.sub("--","–",bib) # Bindestriche austauschen
bib = re.sub("~"," ",bib) # Gesicherte Spaces austauschen
bib = re.sub("\\\\&","&",bib) # Und-Zeichen austauschen
bib = re.sub("%.+?@","@",bib, flags=re.MULTILINE|re.DOTALL) # %-Umgebung aus dial entfernen

# BIBTEX parsen und nach JS exportieren:
import bibtexparser
from bibtexparser.bparser import BibTexParser
parser = BibTexParser()
parser.ignore_nonstandard_types = False
bibdb = bibtexparser.loads(bib, parser)

with open("dial.js", "w") as fh:
	fh.write('var rows = [\n')
	for entry in bibdb.entries:
		fh.write(' {\n')
		# Wenn keywords == wenn Erstpublikation:
		if 'keywords' in entry:
			entry['Erstpublikation'] = 'ja'
		else:
			entry['Erstpublikation'] = 'nein'
		# Genre eintragen
		if 'keywords' not in entry:
			# Genre aus dem Werk-Element mit selber wikidata-ID holen:
			for entry2 in bibdb.entries:
				if 'keywords' in entry2 and entry2['wikidata'] == entry['wikidata']:
					entry['genre'] = entry2['keywords']
		else:
			entry['genre'] = entry['keywords']
		# Datum > Jahr & Jahrzehnt:
		if 'date' in entry:
			if re.findall('^\d+', entry['date']):
				entry['Jahr'] = entry['date'][:4]
				entry['Jahrzehnt'] = entry['date'][:3]+'0er'
			else:
				entry['Jahrzehnt'] = '[o.A.]'
			if len(entry['date']) > 10:
				entry['date'] = re.sub('/',' / ',entry['date'])
		else:
			entry['Jahr'] = 'ohne Jahr'
		if 'ENTRYTYPE' in entry:
			if entry['ENTRYTYPE'] == 'article':
				entry['ENTRYTYPE'] = 'Artikel'
			elif entry['ENTRYTYPE'] == 'book':
				entry['ENTRYTYPE'] = 'Buch'
			elif entry['ENTRYTYPE'] == 'inbook' or 'incollection':
				entry['ENTRYTYPE'] = 'Buchbeitrag'
			elif entry['ENTRYTYPE'] == 'mvbook':
				entry['ENTRYTYPE'] = 'mehrbändiges Buch'
			else:
				entry['ENTRYTYPE'] = 'sonstiges'
		# multiple Autoren:
		if 'author' in entry:
			entry['author'] = re.split(' AND ', entry['author'])
		# multiple Buch-Autoren:
		if 'bookauthor' in entry:
			entry['bookauthor'] = re.split(' AND ', entry['bookauthor'])
		# multiple Orte:
		if 'location' in entry:
			entry['location'] = re.split(' AND ', entry['location'])
		# multiple Verlage:
		if 'publisher' in entry:
			entry['publisher'] = re.split(' AND ', entry['publisher'])
		# multiple Herausgeber:
		if 'editor' in entry:
			entry['editor'] = re.split(' AND ', entry['editor'])
		# Schreiben:
		for element in entry:
			if isinstance(entry[element], str):
				fh.write(
					'  "'+element+'": "'+entry[element]+'",\n')
			elif isinstance(entry[element], list):
				fh.write('  "'+element+'": '+str(entry[element])+',\n')
			else:
				print('Error:', entry[element])
		fh.write(' },\n')
	fh.write(']')