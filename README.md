# MX Utils

## Description

This repository holds a collection of methods written in Python that have been useful to my work.
Currently it holds methods under the following sub-headings:

+ Document Preperation
  + Creating latex resources (strings and files)
  + Compiling latex resources (requires pdflatex in PATH)
  + Merging PDF files
+ Database reading
  + Reading a SQL table into memory as a `pandas.DataFrame`
  + Exporting REDCap records
  + Downloading files via SFTP
+ Mailing
  + Send emails via Microsoft Outlook programmatically.

This repository is actively under development, however there's enough in here for now for me to
start using this as my library of generic methods.

## Requirements

This package is written in Python 3.7+.  It should work with Python 3.6, but may not work with
older versions of Python (including Python 2).  In addition, the following packages are needed:

+ `pandas`
+ `numpy`
+ `pyodbc`
+ `pysftp`
+ `requests`
+ `PyPDF2`
+ `pywin32`

`pip` should take care of installing the above dependencies.

## Installation

Simply clone this repository
(https://github.com/marxav0319/MX_Utils)[https://github.com/marxav0319/MX_Utils], navigate to the
directory with `cd <path-to-MX_Utils>`, then install with pip `python -m pip install ./`.  To
uninstall, simply run `python -m pip uninstall mx_utils`.

## Usage

The package can be imported with `import mx_utils`.  Submodules are all pre-loaded in the package,
therefore all public methods can be called from `mx_utils` without needed to navigate to separate
sub-modules.  Here's an example:

```python
import mx_utils as mx

outlook_mailer = mx.Outlook_Mailer(**args, **kwargs)
# Work with outlook_mailer
outlook_mailer.send()
```

## Documentation

Documentation of the methods provided by this package can be found via GitHub Pages
(here)[https://marxav0319.github.io/MX_Utils/].  The generated HTML files can also be found in the
`docs/` directory of this repository.  The documentation was generated with `pdoc3`, a very useful
python package you can find (here)[https://github.com/pdoc3/pdoc].
