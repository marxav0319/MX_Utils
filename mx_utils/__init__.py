"""
Welcome to the `mx_utils` package's documentation!
Author: Mark Xavier

`mx_utils` contains a series of methods that have been helpful to me in my work as a developer/data
analyst at my current job.  I decided to take the various code snippets I have floating around in
various different projects and bring together those that seem to have widespread use cases for me.
The result of that (still ongoing) effort is here.

In this package you'll find various methods to aid in: document preperation (mainly latex and pdf),
obtaining data online (SFTP, SQL DB's, etc.), and an automated Outlook mailer.

This package and it's documentation are not complete and will be added to, but since I've gotten so
far in setting this repository up it felt like the time to start introducing proper documentation.
"""

from .databases import *
from .document_preparation import *
from .mailer.outlook_mailer import Outlook_Mailer

__name__ = 'mx_utils'
__version__ = '0.2.0'
