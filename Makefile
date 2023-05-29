all: README.md

ROOT=.
TEMPLATE=$(ROOT)/src/_README.md
DATA=$(ROOT)/db/
RENDER=$(ROOT)/src/render_from_template.py

README.md: $(TEMPLATE) $(DATA)* $(RENDER)
	python $(RENDER) $< $(DATA) -o ./$@