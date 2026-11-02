.PHONY: check sources pdf

check:
	python3 tools/check_repository.py

sources:
	python3 tools/fetch_sources.py

pdf:
	cd manuscript && pdflatex -interaction=nonstopmode -halt-on-error uniformity.tex
	cd manuscript && pdflatex -interaction=nonstopmode -halt-on-error uniformity.tex
	cd manuscript && pdflatex -interaction=nonstopmode -halt-on-error uniformity.tex
