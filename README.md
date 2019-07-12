# MX Utils
*Ver 0.1.0a*

---

## Description

This is a collection of methods I use pretty often at work or in my personal/school projects.  I use
Python for work mainly, although my school projects can range in language choice.  This repository
holds only the python code that I work with.

**Note:** This repository is nowhere near complete, I'm actively gathering all the bits of code I've
written in a few different places and combining them here so that I have one place I can grab these
pieces from.  Therefore, you should expect many changes in the future as well as random
restructuring of this repository.  Also, many of the methods I'm gathering were built for specific
tasks, and in grabbing those methods here I'm in the process of generalizing the methods.  Because
of this, updates may be slow to come due to the work needed to refactor the methods and wittle them
down to general use-cases.

---

## Usage

Forthcoming.

---

## Repository Structure

The actual package is `mx_utils`, this parent directory serves as a holding place for the future if
I decide to make this a full-blown, pip-installable package (which I very well may do).  Currently
I've installed on my local machine during development with
`python -m pip install -e <path-to-MX_Utils>`.  This creates a link in the currently active `python`
distribution's `site-packages` directory, allowing access to the current version of the repository.
This is, of course, bad practice if this package will be used as an actual library, but when that
time comes I'll have a more competent `setup.py` as well as other resources, for now these are just
placeholders.

```
mx_utils
|
|-databases.py
```

---

## Documentation

Currently all documentation is in the `.py` files themselves.  When this repository gets large
enough that proper documentation is needed, all methods will be properly documented (format to be
determined).
