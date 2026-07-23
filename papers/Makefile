# TeX/PDF pipeline. Toolchain: user-space TinyTeX (~/.TinyTeX, no root).
# Install once:  wget -qO- "https://yihui.org/tinytex/install-bin-unix.sh" | sh
export PATH := $(HOME)/.TinyTeX/bin/x86_64-linux:$(PATH)

TEX    = pdflatex -interaction=nonstopmode
PAPERS = cubic-thue-exp cubic-thue-certificates

all: $(addsuffix .pdf,$(PAPERS))

%.pdf: %.tex
	$(TEX) $< >/dev/null && $(TEX) $< >/dev/null
	@grep -c "Warning.*undefined" $*.log | xargs -I{} test {} -eq 0 \
		|| (echo "UNDEFINED REFERENCES in $*"; exit 1)
	@echo "$@ OK"

clean:
	rm -f *.aux *.log *.out *.toc

.PHONY: all clean
