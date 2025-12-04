YEAR := $(shell date +%Y)
PREV_YEAR = $(shell date -d "last year" +%Y)
DAY := $(shell date +%d)
DAY_FNAME = $(YEAR)/d$(DAY).py


new_year:
	mkdir $(YEAR)
	mkdir $(YEAR)/input
	touch $(YEAR)/README.md
	cp $(PREV_YEAR)/template.py $(YEAR)/template.py
	cp $(PREV_YEAR)/utils.py $(YEAR)/utils.py


new_day:
	if [ -e $(DAY_FNAME) ]; then echo file already exists; exit 1; fi
	cp $(YEAR)/template.py $(DAY_FNAME)
	touch $(YEAR)/input/d$(DAY).txt


run:
	@cd $(YEAR) && . ../.venv/bin/activate && python -m d$(DAY)
