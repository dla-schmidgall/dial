# Das Digitale Ilse Aichinger Literaturverzeichnis

Das Digitale Ilse Aichinger Literaturverzeichnis (dial) setzt sich zum Ziel, möglichst alle publizierten Texte von Ilse Aichinger (1921-2016) bibliographisch zu verzeichnen. Eine vollständige subjektive Personalbibliographie ist bislang nicht geleistet worden (vgl. die Bibliographien von Reichensperger 1995 ff. und Karnahl 2007). Für das dial wurden Bestände verschiedener Archive durchsucht: das Deutsche Literaturarchiv Marbach, das Innsbrucker Zeitungsarchiv, das Medienarchiv des Österreichischen Rundfunks, das Literaturarchiv der Österreichischen Nationalbibliothek und das Otl Aicher Archiv der Hochschule für Gestaltung. Das dial umfasst damit 1813 Einträge (erweiterbar), wovon 639 als Erstpublikationen und als Werkeinheiten zu verstehen sind.

## Voraussetzungen und Verwendungsmöglichkeiten

Die Datei `dial_(#date).bib` ist eine Textdatei, welche einer bestimmten Syntax folgt, die `BibLaTex` heißt (siehe dazu [ctan.org/pkg/biblatex](https://ctan.org/pkg/biblatex)). Sie kann entweder mit `LaTex` zum Beispiel in ein PDF gesetzt werden (siehe [Comprehensive TeX Archive Network](https://ctan.org/)) oder in Software importiert werden, welche das Format verarbeiten kann (beispielsweise [JabRef](https://www.jabref.org/) oder [Zotero](https://www.zotero.org/)).

## Spezifische Erläuterungen

Ein erkärtes Projektziel war es, auf eine pragmatische Weise mit der grundlegenden Idee des `FRBR`-Modells zu arbeiten. Im `FRBR`-Modell wird zwischen *Werk*, *Expression*, *Manifestation* und *Exemplar* unterschieden; was für die Zwecke dieses Projekts zu differenziert ist, dessen grundlegende Idee aber brauchbar erschien: die Möglichkeit, Texte, die vermutlich als 'die gleichen' anzusehen sind, miteinander in eine spezifische Verbindung zu bringen. Das Format [BIBFRAME](http://bibframe.org/) bietet ein vereinfachtes Vokabular des `FRBR`-Modells und wird -- neben der *Library of Congress* -- auch von der Deutschen Nationalbibliothek eingesetzt (siehe [DNB:bibframe](http://www.dnb.de/bibframe)).

### Werkeinheiten & wikidata

Das Feld `wikidata` ist nicht Teil der BibLaTex-Syntax. Das Projekt `dial` hat in Wikidata die Identifikationsnummer [Q54007056](https://www.wikidata.org/wiki/Q54007056). Darin werden alle Werk-Einheiten des `dial` gesammelt: jeweils mit einer eigenen Wikidata-ID. Wurde ein Werk öfter publiziert, so wird in der BibLaTex-Datei jeder Publikation die selbe Werk-ID gegeben. Dadurch werden die verschiedenen Publikationen miteinander verbunden; auf abstrakte Weise zu einer Werk-Einheit im Sinne des FRBR-Modells konstruiert.

### Erstpublikationen und Gattung

Um speziell die Erstpublikationen leicht abfragbar zu machen, wurden nur die jeweils als Erstausgabe angesehenen Einheiten mit einem Gattungsbegriff versehen. Folgende Gattungsbezeichnungen wurden verwendet:

* prose
* verse
* drama
* prosepoetry
* interview

## Autor

* **Andreas Dittrich** - *dial* - [dial@github](https://github.com/diaphon/dial)

## Lizenz

Dieses Projekt steht unter der Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Lizenz: [CC BY-SA 4.0](http://creativecommons.org/licenses/by-nc-sa/4.0/).

## Danksagung

Dieses Projekt wurde ermöglicht durch das *Digital Humanities* Stipendium des [Forschungsverbund MWW](http://www.mww-forschung.de/). 

Ich bin folgenden Institutionen für ihre Kooperation und Hilfsbereitschaft dankbar:
I am grateful to the following institutions for their cooperation and helpfulness:

* Deutsches Literaturarchiv (DLA) Marbach
* Hochschule für Gestaltung (Ulm)
* Innsbrucker Zeitungsarchiv (IZA)

Ohne die Unterstützung von Christine Ivanovic hätte dieses Projekt erst garnicht richtig anfangen können: herzlichen Dank!