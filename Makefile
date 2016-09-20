TEXFILE = highlight_biology

my_publications.bib:
	python fetch_zotero_bib.py

$(TEXFILE)/$(TEXFILE).pdf: $(TEXFILE)/$(TEXFILE).tex my_publications.bib
	pdflatex -interaction nonstopmode -halt-on-error -file-line-error $(TEXFILE).tex;
	bibtex $(TEXFILE).aux;
	pdflatex -interaction nonstopmode -halt-on-error -file-line-error $(TEXFILE).tex;
	pdflatex -interaction nonstopmode -halt-on-error -file-line-error $(TEXFILE).tex;
	rm -v $(TEXFILE).blg $(TEXFILE).out $(TEXFILE).aux $(TEXFILE).bbl $(TEXFILE).log