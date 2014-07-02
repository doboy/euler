all: index.html

index.html: py hs sc

py: build python/README.md
hs: build haskell/README.md
sc: build scala/README.md

pymds := $(patsubst %.py,build/%.md,$(wildcard python/p*.py))
hsmds := $(patsubst %.hs,build/%.md,$(wildcard haskell/p*.hs))
scmds := $(patsubst %.scala,build/%.md,$(wildcard scala/p*.scala))

define make-readme
/bin/echo -n "problem $*: " > "$@"
if [[ "`cat build/$<.out`" != "`grep '^$*[[:space:]]' answers.txt | cut -f 2 -d ' '`" ]] ; then \
	echo "Expected $$(grep '^$*[[:space:]]' answers.txt | cut -f 2 -d ' '), got $$(cat build/$<.out)" >> "$@"; \
else \
	echo "Solved in $$(cat build/$<.time)ms" >> "$@" ; \
fi
endef

build/python/p%.md: python/p%.py
	TIMEFORMAT="%R"; { time python "$<" > "build/$<.out"; } 2> "build/$<.time"
	$(make-readme)

build/scala/p%.md: scala/p%.scala
	scalac -d build/scala $<
	TIMEFORMAT="%R"; { time scala -classpath build/scala "p$*" > "build/$<.out"; } 2> "build/$<.time"
	$(make-readme)

build/haskell/p%.md: haskell/p%.hs
	ghc -o build/$< $<
	TIMEFORMAT="%R"; { time ./build/"$<" > "build/$<.out"; } 2> "build/$<.time"
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

.PHONY: clean build
clean:
	find . -name *.md -delete
	find . -name *.class -delete
	rm -rf build

build:
	mkdir -p "$@"
	mkdir -p "$@"/haskell
	mkdir -p "$@"/python
	mkdir -p "$@"/scala
