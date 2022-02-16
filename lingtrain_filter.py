#!/usr/bin/env python
import sys
import panflute as pf


def prepare(doc):
    insertion = []
    title = doc.get_metadata('title')
    if title:
        insertion.append(pf.Para(pf.Str(f'{title}%%%%%title.')))
    for author in doc.get_metadata('author'):
        insertion.append(pf.Para(pf.Str(f'{author}%%%%%author.')))
    doc.content[0:0] = insertion


def action(elem, doc):
    # parse headers
    if isinstance(elem, pf.Header):
        elem.content.append(pf.Str(f'%%%%%h{elem.level}.'))

    # remove footnotes
    elif isinstance(elem, pf.Note):
        return []

    # parse epigraphs and cites
    elif ((isinstance(elem, pf.Div) and 'epigraph' in elem.classes)
          or isinstance(elem, pf.BlockQuote)):
        pars = [e for e in elem.content if isinstance(e, pf.Para)]
        if len(pars) == 1:
            pars[0].content.append(pf.Str('%%%%%qtext.'))
        else:
            for par in pars[:-1]:
                par.content.append(pf.Str('%%%%%qtext.'))
            pars[-1].content.append(pf.Str('%%%%%qname.'))
        return pars


def main(doc=None):
    return pf.run_filter(action, prepare=prepare, doc=doc)


if __name__ == '__main__':
    main()
