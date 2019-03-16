# Das Digitale Ilse Aichinger Literaturverzeichnis

Das Digitale Ilse Aichinger Literaturverzeichnis (`dial`) setzt sich zum Ziel, möglichst alle publizierten Texte von Ilse Aichinger (1921-2016) bibliografisch zu verzeichnen. Eine vollständige subjektive Personalbibliografie ist bislang nicht geleistet worden. Für das `dial` wurden Bestände verschiedener Archive durchsucht: vor allem die Bestände am _Deutschen Literaturarchiv Marbach_, welches das Projekt auch mit einem Stipendium gefördert hat. Das `dial` umfasst damit 1834 Einträge, von denen 642 Einträge als Erstpublikationen und als Werkeinheiten zu verstehen sind.

## Voraussetzungen und Verwendungsmöglichkeiten

Die Datei `dial_(#date).bib` ist eine Textdatei, welche einer bestimmten Syntax folgt, die `BibLaTex` heißt (siehe dazu [ctan.org/pkg/biblatex](https://ctan.org/pkg/biblatex)). Sie kann entweder mit `LaTex` zum Beispiel in ein `PDF` gesetzt werden (siehe [Comprehensive TeX Archive Network](https://ctan.org/)) oder in Software importiert werden, welche das Format verarbeiten kann (beispielsweise [JabRef](https://www.jabref.org/) oder [Zotero](https://www.zotero.org/)).

Im Langzeitarchiv der _Österreichischen Akademie der Wissenschaften_ [ARCHE](https://arche.acdh.oeaw.ac.at/) wird der derzeitige Stand des `dial` gesichert (Repository ID: _dial_12450_). Zusätzlich wurde es auf [Wikidata](https://www.wikidata.org) ([Q54007056](https://www.wikidata.org/wiki/Q54007056)) mit dem entsprechenden Vokabular importiert, sodass die bibliografischen Daten dort offen zugänglich und veränderbar sind.

## Spezifische Erläuterungen

Ein erklärtes Projektziel war es, auf eine pragmatische Weise mit der grundlegenden Idee des `FRBR`-Modells zu arbeiten. Im `FRBR`-Modell wird zwischen *Werk*, *Expression*, *Manifestation* und *Exemplar* unterschieden; was für die Zwecke dieses Projekts zu differenziert ist, dessen grundlegende Idee aber brauchbar erschien: die Möglichkeit, Texte, die vermutlich als 'die gleichen' anzusehen sind, miteinander in eine spezifische Verbindung zu bringen. Schließlich wurde die Plattform _Wikidata_ verwendet, da diese eine offene und erweiterbare Infrastruktur bietet.

### Werkeinheiten & Wikidata

Die Datei mit der Endung `bib` folgt im Wesentlichen der Syntax von `BibLaTex`, erweitert diese aber um das Feld Feld `wikidata`, welches von Parsern einfach ignoriert werden kann. Unter der _Wikidata_-ID [Q54007056](https://www.wikidata.org/wiki/Q54007056) werden alle Werkeinheiten des `dial` gesammelt: jeweils mit einer eigenen _Wikidata_-ID. Wurde ein Werk öfter publiziert, so wird in der BibLaTex-Datei jeder Publikation dieselbe Werk-ID gegeben. Dadurch werden die verschiedenen Publikationen miteinander verbunden.

### Erstpublikationen und Gattung

Um speziell die Erstpublikationen leicht abfragbar zu machen, wurden nur die jeweils als Erstausgabe angesehenen Einheiten (im Feld `keywords`) mit einem Gattungsbegriff versehen. Folgende Gattungsbezeichnungen wurden dabei verwendet:

* prose
* verse
* drama
* prosepoetry
* interview

### PDF

Der beigefügte PDF-Export ist mit `LaTex` und `BibLaTex` erzeugt worden. Die fortlaufende Nummerierung ist nur mit dieser spezifischen Bib-Datei stabil und sollte nicht als Referenz genommen werden. Eine Buchpublikation ist in Planung und soll eine gesicherte Referenzierung ermöglichen.

### HTML

Die `bib`-Datei kann auch mit einem Javascript von *pcooksey* [bibtex-js](https://github.com/pcooksey/bibtex-js) im Browser lokal durchsucht werden. Eine für das `dial` leicht adaptierte Version des Skripts kann auf Github unter [diaphon/dial](https://github.com/diaphon/dial) heruntergeladen werden.

## weiterführendes

Ausführlichere Informationen sind in meinem Artikel der _Proceedings_ zur Tagung _digital humanities austria 2018_ (`dha2018`) zu finden.

## Signe

Andreas Dittrich, Marbach am Neckar, am 16.3.2019

## Lizenz

Dieses Projekt steht unter der Lizenz CC BY, das heißt, dass es geteilt und bearbeitet werden darf, solange der Urheber genannt wird (vgl. [CC BY](https://creativecommons.org/licenses/by/3.0/)).

## Danksagung

Ermöglicht wurde das `dial` durch das _Digital Humanities_ Stipendium des [Forschungsverbund MWW](http://www.mww-forschung.de/), dem ich zum Dank verpflichtet bin. Zusätzlich gebührt mein Dank den Beschäftigten des DLA (insbesondere Laura Marie Pohlmann und Karin Schmidgall) und:

* Hanno Biber des `ICLTT/AC` an der Österreichischen Akademie der Wissenschaften,
* Martina Trognitz des `ACDH` der _Österreichischen Akademie der Wissenschaften_,
* Martin Mäntele der _Hochschule für Gestaltung_ (Ulm) und
* den Beschäftigten des _Innsbrucker Zeitungsarchivs_ (IZA).

Vor allem gebührt mein Dank aber der Unterstützung von Christine Ivanovic (_Universität Wien_), ohne die das Projekt erst gar nicht anfangen hätte können: herzlichen Dank!