# The Digital Ilse Aichinger List of Literature (`dial`)

The _Digital Ilse Aichinger List of Literature_ (`dial`) aims at bibliographically listing as many published texts as possible by Ilse Aichinger (1921-2016). A complete bibliography has not yet been provided. Holdings of various archives were searched, above all from the _Deutsches Literaturarchiv Marbach_ (`DLA`), who also funded the project with a fellowship. The `dial` thus comprises 1834 entries (extendible) at the moment, 642 of which are to be understood as original publications and thus as work entities.

## Prerequisites and how to use

The file `dial_(#date).bib` is a text file which follows a certain syntax called `BibLatex` (see [ctan.org/pkg/BibLatex](https://ctan.org/pkg/BibLatex)). It can either be set with `Latex` for example into a `PDF` (see [Comprehensive TeX Archive Network](https://ctan.org/)) or imported into software which can process the format (for example [JabRef](https://www.jabref.org/) or [Zotero](https://www.zotero.org/)).

In the long-term archive of the _Austrian Academy of Sciences_ [ARCHE](https://arche.acdh.oeaw.ac.at/) the current state of the `dial` is stored (Repository ID: _dial_12450_). In addition, it was imported to [Wikidata](https://www.wikidata.org) ([Q54007056](https://www.wikidata.org/wiki/Q54007056)) with the corresponding vocabulary, so that the bibliogaphical data are openly accessible and changeable.

## Specific Explanations

A declared goal of the project was to work in a pragmatic way with the basic idea of the `FRBR` model. The `FRBR` model distinguishes between _work_, _expression_, _manifestation_ and _example_; which is too differentiated for the purposes of this project, but whose basic idea seemed useful: the possibility to connect texts that are probably to be regarded as 'the same' to each other in a specific way.

A declared goal of the project was to work in a pragmatic way with the basic idea of the `FRBR` model. The `FRBR` model distinguishes between _work_, _expression_, _manifestation_ and _example_; which is too differentiated for the purposes of this project, but whose basic idea seemed useful: the possibility to connect texts that are probably to be regarded as 'the same' to each other in a specific way. Finally the platform _Wikidata_ was used, because it offers an open and extensible infrastructure.

### Work entities & Wikidata

The field `wikidata` is not part of the `BibLatex` syntax. In _Wikidata_ the project `dial` has the identification number [Q54007056](https://www.wikidata.org/wiki/Q54007056). In it all work units of the `dial` are collected: each with its own _Wikidata_ ID. If a work has been published more then once, the same _Wikidata_-ID is given to each of these publication in the `BibLatex` file. Thus the different publications are connected with each other.

### Original publications and genre

In order to make the first publications in particular easy to query, only the units regarded as first editions were provided with a term for the genre (in the `keywords` field). The following genres were used:

* prose
* verse
* drama
* prosepoetry
* interview

## Exports

### PDF

The attached PDF export was created with `LaTex` and `BibLaTex`. Consecutive numbering is only stable with this specific bib file and should not be used as a reference. A book publication is planned and should allow a secure referencing.

### HTML

The `bib` file can also be searched locally in the browser with a `JavaScript`-script from *pcooksey* [bibtex-js](https://github.com/pcooksey/bibtex-js). A slightly adapted version of the script for `dial` can be downloaded from `Github` at [diaphon/dial](https://github.com/diaphon/dial).

## further reading

More detailed information can be found in my article of the _Proceedings_ for the conference _digital humanities austria 2018_ (`dha2018`).

## Signe

Andreas Dittrich, Marbach am Neckar, am 16.3.2019

## License

This project is licensed under CC BY, which means that it may be shared and edited as long as the author is credited (see [CC BY](https://creativecommons.org/licenses/by/3.0/)).

## Acknowledgments

The `dial` was made possible by the _Digital Humanities_ scholarship of the [Forschungsverbund MWW](http://www.mww-forschung.de/), to which I am indebted. In addition I would like to thank the employees of the DLA (especially Laura Marie Pohlmann and Karin Schmidgall), furthermore to:

* Hanno Biber of the `ICLTT/AC` at the _Austrian Academy of Sciences_,
* Martina Trognitz of the `ACDH` at the _Austrian Academy of Sciences_,
* Martin Mäntele of the _Hochschule für Gestaltung_ (Ulm) and
* the employees of the _Innsbrucker Zeitungsarchiv_ (IZA).

Above all, I would like to thank Christine Ivanovic (_University of Vienna_) for her support, without whom the project could not have started in the first place: thank you very much!