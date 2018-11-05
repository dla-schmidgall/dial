# The Digital Ilse Aichinger List of Literature (dial)

The Digital Ilse Aichinger List of Literature (dial) aims at bibliographically listing as many published texts as possible by Ilse Aichinger (1921-2016). A complete bibliography has not yet been provided (cf. the bibliographies of Reichensperger 1995 ff. and Karnahl 2007). Holdings of various archives were searched: the Deutsches Literaturarchiv Marbach (DLA Marbach), the Innsbrucker Zeitungsarchiv (IZA), the Media Archive of the Österreichischer Rundfunk (ORF), the Literature Archive of the Österreichische Nationalbibliothek (ÖNB) and the Otl Aicher Archive at the Hochschule für Gestaltung (HfG). The dial thus comprises 1.813 entries (extendible), 639 of which are to be understood as original publications and thus as work entities.

## Prerequisites and how to use

The file `dial_(#date).bib` is a text file which follows a certain syntax called `BibLaTex` (see [ctan.org/pkg/biblatex](https://ctan.org/pkg/biblatex)). It can either be set with `LaTex` for example into a PDF (see [Comprehensive TeX Archive Network](https://ctan.org/)) or imported into software which can process the format (for example [JabRef](https://www.jabref.org/) or [Zotero](https://www.zotero.org/)).

## Specific Explanations

A declared goal of the project was to work in a pragmatic way with the basic idea of the `FRBR` model. The `FRBR` model distinguishes between *work*, *expression*, *manifestation* and *example*; which is too differentiated for the purposes of this project, but whose basic idea seemed useful: the possibility to connect texts that are probably to be regarded as 'the same' to each other in a specific way. The format [BIBFRAME](http://bibframe.org/) offers a simplified vocabulary of the `FRBR` model and is also used -- besides the *Library of Congress* -- by the German National Library (see [DNB:bibframe](http://www.dnb.de/bibframe)).

The latest version of the `dial` is available on [Wikidata](https://www.wikidata.org/wiki/Q54007056). The [ARCHE-System](https://arche.acdh.oeaw.ac.at/) contains a long-term backup.

### work entities & wikidata

Das Feld `wikidata` ist nicht Teil der BibLaTex-Syntax. Das Projekt `dial` hat in Wikidata die Identifikationsnummer [Q54007056](https://www.wikidata.org/wiki/Q54007056). Darin werden alle Werk-Einheiten des `dial` gesammelt: jeweils mit einer eigenen Wikidata-ID. Wurde ein Werk öfter publiziert, so wird in der BibLaTex-Datei jeder Publikation die selbe Werk-ID gegeben. Dadurch werden die verschiedenen Publikationen miteinander verbunden; auf abstrakte Weise zu einer Werk-Einheit im Sinne des FRBR-Modells konstruiert.

The field `wikidata` is not part of the BibLaTex syntax. In Wikidata the project `dial` has the identification number [Q54007056](https://www.wikidata.org/wiki/Q54007056). In it all work units of the `dial` are collected: each with its own Wikidata ID. If a work has been published more then once, the same Wikidata-ID is given to each of these publication in the BibLaTex file. Thus the different publications are connected with each other; constructed in an abstract way to a work unit in the sense of the FRBR model.

### Original publications and genre

In order to make the original publications more easily searchable, only the units regarded as first editions were given a genre term. The following genre terms were used:

* prose
* verse
* drama
* prosepoetry
* interview

## Exports

### PDF

The attached PDF export was created with `LaTex` and `BibLaTex`. The consecutive numbering is only stable with this specific Bib-file and should not be used as a reference. A book publication is planned and should allow a secure referencing.

### HTML

The `bib`-file can also be searched locally in the browser with a Javascript from *pcooksey* [bibtex-js](https://github.com/pcooksey/bibtex-js). A slightly for `dial` adapted version of the script can be downloaded from Github at [diaphon/dial](https://github.com/diaphon/dial).

## Signe

Andreas Dittrich, Passau on 5th of November 2018

## License

This project is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International licence: [CC BY-SA 4.0](http://creativecommons.org/licenses/by-nc-sa/4.0/).

## Acknowledgments

This project was made possible by the *Digital Humanities* scholarship of [Forschungsverbund MWW](http://www.mww-forschung.de/).

I am grateful to the following institutions for their cooperation and helpfulness:

* Deutsches Literaturarchiv Marbach (DLA) 
* Hochschule für Gestaltung (Ulm)
* Innsbrucker Zeitungsarchiv (IZA)

Without the support of Christine Ivanovic, this project could not have started: thank you so much!