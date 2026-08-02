"""Read BibTeX files directly and normalise entries for the CV.

This replaces the old bib -> yaml (pandoc) conversion step. It parses .bib
files with the standard library only (no external dependencies, so it runs in
the same Quarto jupyter kernel that renders the CV) and returns a list of
reference dicts shaped exactly like the CSL-ish YAML that ``try-bib.qmd`` used
to consume: each has ``type``, ``title``, ``author`` (list of
``{family, given}``), ``issued`` and the usual bibliographic fields.

Entry-type mapping (BibTeX -> internal ``type`` used by try-bib.qmd):

    @article                      -> article-journal
    @inproceedings / @conference  -> paper-conference
    @incollection / @inbook       -> chapter
    @book                         -> book
    @phdthesis / @mastersthesis   -> thesis
    @software                     -> software
    @unpublished                  -> manuscript
    @misc (and anything else)     -> other
"""

import re

# --- BibTeX -> internal reference type -------------------------------------

TYPE_MAP = {
    "article": "article-journal",
    "inproceedings": "paper-conference",
    "conference": "paper-conference",
    "proceedings": "paper-conference",
    "incollection": "chapter",
    "inbook": "chapter",
    "book": "book",
    "phdthesis": "thesis",
    "mastersthesis": "thesis",
    "thesis": "thesis",
    "software": "software",
    "unpublished": "manuscript",
    "misc": "other",
}

# Entry types that carry no reference (skip them entirely).
SKIP_TYPES = {"preamble", "comment", "string"}

# --- LaTeX -> unicode cleanup ----------------------------------------------

_ACCENTS = {
    ("'", "a"): "á", ("'", "e"): "é", ("'", "i"): "í", ("'", "o"): "ó",
    ("'", "u"): "ú", ("'", "y"): "ý", ("'", "n"): "ń", ("'", "c"): "ć",
    ("'", "A"): "Á", ("'", "E"): "É", ("'", "I"): "Í", ("'", "O"): "Ó",
    ("'", "U"): "Ú",
    ('"', "a"): "ä", ('"', "e"): "ë", ('"', "i"): "ï", ('"', "o"): "ö",
    ('"', "u"): "ü", ('"', "A"): "Ä", ('"', "O"): "Ö", ('"', "U"): "Ü",
    ("`", "a"): "à", ("`", "e"): "è", ("`", "i"): "ì", ("`", "o"): "ò",
    ("`", "u"): "ù",
    ("^", "a"): "â", ("^", "e"): "ê", ("^", "i"): "î", ("^", "o"): "ô",
    ("^", "u"): "û",
    ("~", "n"): "ñ", ("~", "a"): "ã", ("~", "o"): "õ",
}

_RE_ACCENT_BRACED = re.compile(r"\{\\(['\"`^~])\s*([A-Za-z])\}")   # {\'e}
_RE_ACCENT_ARGBR = re.compile(r"\\(['\"`^~])\{([A-Za-z])\}")        # \'{e}
_RE_ACCENT_BARE = re.compile(r"\\(['\"`^~])\s*([A-Za-z])")          # \'e


def _accents(text):
    def repl(m):
        return _ACCENTS.get((m.group(1), m.group(2)), m.group(2))
    text = _RE_ACCENT_BRACED.sub(repl, text)
    text = _RE_ACCENT_ARGBR.sub(repl, text)
    text = _RE_ACCENT_BARE.sub(repl, text)
    return text


def clean(text, is_url=False):
    """Turn a raw BibTeX field value into display-ready text."""
    if text is None:
        return None
    text = text.strip()
    if is_url:
        # URLs: just collapse the whitespace/newlines some entries contain.
        return re.sub(r"\s+", "", text)
    text = _accents(text)
    text = (text.replace(r"\&", "&").replace(r"\%", "%").replace(r"\_", "_")
                .replace(r"\$", "$").replace(r"\#", "#").replace("~", " "))
    text = text.replace("---", "\u2014").replace("--", "\u2013")
    text = text.replace("{", "").replace("}", "")
    return re.sub(r"\s+", " ", text).strip()


# --- name parsing ----------------------------------------------------------

def parse_names(raw):
    """Split a BibTeX author/editor string into ``{family, given}`` dicts."""
    names = []
    for part in re.split(r"\s+and\s+", raw.strip()):
        part = clean(part)
        if not part:
            continue
        if part.lower() == "others":
            names.append({"literal": "others"})
            continue
        if "," in part:                       # "Family, Given" (or "Family Jr, Given")
            family, given = part.split(",", 1)
            names.append({"family": family.strip(), "given": given.strip()})
        else:                                  # "Given Family"
            tokens = part.split()
            names.append({"family": tokens[-1], "given": " ".join(tokens[:-1])})
    return names


# --- low-level BibTeX parsing ----------------------------------------------

def _split_entries(text):
    """Yield ``(entry_type, body)`` for each ``@type{ ... }`` block."""
    i, n = 0, len(text)
    while i < n:
        at = text.find("@", i)
        if at < 0:
            break
        j = at + 1
        while j < n and text[j].isalpha():
            j += 1
        etype = text[at + 1:j].lower()
        while j < n and text[j] in " \t\r\n":
            j += 1
        if j >= n or text[j] != "{":
            i = at + 1
            continue
        depth, k = 0, j
        while k < n:
            if text[k] == "{":
                depth += 1
            elif text[k] == "}":
                depth -= 1
                if depth == 0:
                    break
            k += 1
        yield etype, text[j + 1:k]
        i = k + 1


def _parse_fields(body):
    """Parse the ``key, name = value, ...`` body of one entry."""
    comma = body.find(",")
    if comma < 0:
        return None, {}
    key = body[:comma].strip()
    s, i, n = body[comma + 1:], 0, len(body) - comma - 1
    fields = {}
    while i < n:
        while i < n and s[i] in " \t\r\n,":
            i += 1
        start = i
        while i < n and s[i] not in "= \t\r\n":
            i += 1
        name = s[start:i].strip().lower()
        while i < n and s[i] != "=":
            i += 1
        if i >= n or not name:
            break
        i += 1
        while i < n and s[i] in " \t\r\n":
            i += 1
        if i >= n:
            break
        if s[i] == "{":
            depth, start = 0, i
            while i < n:
                if s[i] == "{":
                    depth += 1
                elif s[i] == "}":
                    depth -= 1
                    if depth == 0:
                        i += 1
                        break
                i += 1
            value = s[start + 1:i - 1]
        elif s[i] == '"':
            start, i, depth = i + 1, i + 1, 0
            while i < n:
                if s[i] == "{":
                    depth += 1
                elif s[i] == "}":
                    depth -= 1
                elif s[i] == '"' and depth == 0:
                    break
                i += 1
            value = s[start:i]
            i += 1
        else:
            start = i
            while i < n and s[i] not in ",\n":
                i += 1
            value = s[start:i].strip()
        fields[name] = value
    return key, fields


# --- normalisation ---------------------------------------------------------

def _issued(fields):
    """Return a sortable/displayable issue date (int year or date string)."""
    date = fields.get("date", "").strip()
    if re.match(r"^\d{4}(-\d{2}){1,2}$", date):
        return date
    year = fields.get("year", "").strip()
    if year.isdigit():
        return int(year)
    if re.match(r"^\d{4}", date):
        return int(date[:4])
    return None


def to_reference(etype, fields):
    ref_type = TYPE_MAP.get(etype, "other")
    ref = {"type": ref_type, "title": clean(fields.get("title", ""))}
    if "author" in fields:
        ref["author"] = parse_names(fields["author"])
    if "editor" in fields:
        ref["editor"] = parse_names(fields["editor"])

    issued = _issued(fields)
    if issued is not None:
        ref["issued"] = issued

    # container title: journal for articles/other, booktitle for chapters,
    # either for conference proceedings.
    if ref_type == "chapter":
        container = fields.get("booktitle")
    elif ref_type == "paper-conference":
        container = fields.get("booktitle") or fields.get("journal")
    else:
        container = fields.get("journal") or fields.get("howpublished")
    if container:
        ref["container-title"] = clean(container)

    for src, dst in (("doi", "doi"), ("volume", "volume"), ("number", "issue"),
                     ("pages", "page"), ("publisher", "publisher")):
        if src in fields and fields[src].strip():
            ref[dst] = clean(fields[src])
    if "url" in fields and fields["url"].strip():
        ref["url"] = clean(fields["url"], is_url=True)
    if "note" in fields and fields["note"].strip():
        ref["note"] = clean(fields["note"])
    return ref


def load_references(paths):
    """Parse every path and return one flat list of normalised references."""
    references = []
    for path in paths:
        with open(path, "r", encoding="utf-8") as fh:
            text = fh.read()
        for etype, body in _split_entries(text):
            if etype in SKIP_TYPES:
                continue
            key, fields = _parse_fields(body)
            if key is None or "title" not in fields:
                continue
            references.append(to_reference(etype, fields))
    return references


if __name__ == "__main__":
    import sys
    from collections import Counter
    refs = load_references(sys.argv[1:] or ["boehm.bib", "boehm-wip.bib"])
    print(f"{len(refs)} references")
    for t, c in sorted(Counter(r["type"] for r in refs).items()):
        print(f"  {c:2}  {t}")
