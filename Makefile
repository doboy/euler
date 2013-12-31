all: py hs

py: tmp python/README.md
hs: tmp haskell/README.md

tmp:
	mkdir -p "$@"
	mkdir -p "$@"/haskell
	mkdir -p "$@"/python

pymds := $(patsubst %.py,%.md,$(wildcard python/p*.py))
hsmds := $(patsubst %.hs,%.md,$(wildcard haskell/p*.hs))


define make-readme
/bin/echo -n "problem $*: " > "$@"
if [[ "`cat tmp/$<.out`" != "`grep '^$*[[:space:]]' answers.txt | cut -f 2 -d ' '`" ]] ; then \
	echo "Expected $$(grep '^$*[[:space:]]' answers.txt | cut -f 2 -d ' '), got $$(cat tmp/$<.out)" >> "$@"; \
else \
	echo "Solved in $$(cat tmp/$<.time)ms" >> "$@" ; \
fi
endef

python/p%.md: python/p%.py
	TIMEFORMAT="%R"; { time python "$<" > "tmp/$<.out"; } 2> "tmp/$<.time"
	$(make-out)

haskell/p%.md: haskell/p%.hs
	ghc -o tmp/$< $<
	TIMEFORMAT="%R"; { time ./tmp/"$<" > "tmp/$<.out"; } 2> "tmp/$<.time"
	$(make-out)

define make-readmes
cat $^ > "$@"
sed -i "" 's/^/    /'  "$@"
sed -i "" 's/ $$/ None/'  "$@"
endef

python/README.md: $(pymds)
	$(make-readmes)

haskell/README.md: $(hsmds)
	$(make-readmes)

clean:
	find . -name *.md -delete
	rm -rf tmp
