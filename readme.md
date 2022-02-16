# Usage

Install [pandoc](https://pandoc.org)
and [panflute](http://scorreia.com/software/panflute)
```bash
sudo apt install pandoc
pip install --user panflute
```

For converting fb2 use the command:
```bash
pandoc my-book.fb2 -F lingtrain_filter.py -t plain -o my-book.txt
```

Tested with Ubuntu 20.04, pandoc 2.13 and panflute 2.1.3