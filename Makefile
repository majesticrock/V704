all: build/main.pdf

# hier Python-Skripte:
build/plot_blei.pdf: plot-blei.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot-blei.py

build/plot_eisen.pdf: plot-eisen.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot-eisen.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/plot_blei.pdf build/plot_eisen.pdf

build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
