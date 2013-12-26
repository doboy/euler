py: pycaches python/README.md

pycaches: $(patsubst %.py,%.pycache,$(wildcard python/p*.py))
python/p%.pycache: python/p%.py
	python python/check.py $* > "$@"

python/README.md: python/p*.pycache
	cat $^ > python/README.md
	echo "      Solved:      `grep 'Solved' python/README.md | wc -l`" >> python/README.md
	echo "      In Progress: `grep 'In Progress' python/README.md | wc -l`" >> python/README.md
	echo "      Incorrect:   `grep 'Wrong Output' python/README.md | wc -l`" >> python/README.md
	echo "      Error:       `grep 'Error' python/README.md | wc -l`" >> python/README.md

clean:
	find . -name *cache -delete
	rm -f python/README.md
