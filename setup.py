"""
Simple setup script using distutils so I could test this package locally while editing.
"""

from distutils.core import setup

setup(
    name='MX_Utils',
    version='0.1.0a',
    packages=['mx_utils'],
    author='Mark Xavier',
    author_email='mark.j.xavier@gmail.com',
    description='A set of methods I find useful for my daily work',
    long_description=open('README.txt').read(),
    install_requires=[
        'pandas',
        'numpy',
        'pyodbc',
        'pysftp',
        'requests',
        'PyPDF2',
        'pywin32'
    ]
)
