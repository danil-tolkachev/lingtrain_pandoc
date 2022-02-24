# Usage

Install [pandoc](https://pandoc.org)
and [panflute](http://scorreia.com/software/panflute)
```bash
sudo apt install pandoc
pip install --user panflute
```

For converting book use the command:
```bash
pandoc --filter lingtrain_filter.py --to plain --output my-book.txt my-book.fb2 # or my-book.epub
```

You can override some meta information by using this command:
```bash
pandoc --filter lingtrain_filter.py --to plain --output my-book.txt my-book.fb2 \
    --metadata=author:"Author Name" \
    --metadata=title:"Book Title" \
    --metadata=translator:"Translator Name"
```

Tested with Ubuntu 20.04, pandoc 2.13 and panflute 2.1.3