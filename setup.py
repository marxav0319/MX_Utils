"""
Simple setup script using distutils so I could test this package locally while editing.
"""

from distutils.core import setup

setup(
    name='MX_Utils',
    version='0.2.1',
    packages=['mx_utils'],
    author='Mark Xavier',
    author_email='mark.j.xavier@gmail.com',
    url='https://github.com/marxav0319/MX_Utils',
    license='LICENSE.txt',
    description='A set of methods I find useful for my daily work.',
    long_description=open('README.md').read(),
    install_requires=[
        'pandas>=0.24.0',
        'numpy>=1.16.0',
        'pyodbc>=4.0.0',
        'pysftp>=0.2.9',
        'requests',
        'PyPDF2>=1.26.0',
        'pywin32'
    ]
)
