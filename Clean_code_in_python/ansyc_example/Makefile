all: sync asyncio

requirements:
	pip install -r requirements.txt

sync:
	python3.8 write_genre.py

asyncio:
	python3.8 asyncio_write_genre.py

clean:
	rm -f out/*.txt