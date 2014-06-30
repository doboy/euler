all: index.html

index.html: py hs sc

py: tmp python/README.md
hs: tmp haskell/README.md
sc: tmp scala/README.md

pymds := $(patsubst %.py,tmp/%.md,$(wildcard python/p*.py))
hsmds := $(patsubst %.hs,tmp/%.md,$(wildcard haskell/p*.hs))
scmds := $(patsubst %.scala,tmp/%.md,$(wildcard scala/p*.scala))

define make-readme
/bin/echo -n "problem $*: " > "$@"
if [[ "`cat tmp/$<.out`" != "`grep '^$*[[:space:]]' answers.txt | cut -f 2 -d ' '`" ]] ; then \
	echo "Expected $$(grep '^$*[[:space:]]' answers.txt | cut -f 2 -d ' '), got $$(cat tmp/$<.out)" >> "$@"; \
else \
	echo "Solved in $$(cat tmp/$<.time)ms" >> "$@" ; \
fi
endef

tmp/python/p%.md: python/p%.py
	TIMEFORMAT="%R"; { time python "$<" > "tmp/$<.out"; } 2> "tmp/$<.time"
	$(make-readme)

tmp/scala/p%.md: scala/p%.scala
	scalac -d tmp/scala $<
	TIMEFORMAT="%R"; { time scala -classpath tmp/scala "p$*" > "tmp/$<.out"; } 2> "tmp/$<.time"
	$(make-readme)

tmp/haskell/p%.md: haskell/p%.hs
	ghc -o tmp/$< $<
	TIMEFORMAT="%R"; { time ./tmp/"$<" > "tmp/$<.out"; } 2> "tmp/$<.time"
	$(make-readme)

define make-readmes
cat $^ > "$@"
sed -i "" 's/^/    /'  "$@"
sed -i "" 's/ $$/ None/'  "$@"
endef

python/README.md: $(pymds)
	$(make-readmes)

haskell/README.md: $(hsmds)
	$(make-readmes)

scala/README.md: $(scmds)
	$(make-readmes)

index.html: */README.md
	 ruby generate_html.rb

.PHONY: clean tmp
clean:
	find . -name *.md -delete
	find . -name *.class -delete
	rm -rf tmp

tmp:
	mkdir -p "$@"
	mkdir -p "$@"/haskell
	mkdir -p "$@"/python
	mkdir -p "$@"/scala
