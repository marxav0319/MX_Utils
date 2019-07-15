"""
A collection of some utility functions that help me get data out of various databases.

Author: Mark Xavier
"""

from io import StringIO
import requests
import pandas as pd
import pysftp
import pyodbc

def get_redcap_data(api_url, api_token, file_format='csv', content='record', export_type='flat',
                    raw_or_label='raw', raw_or_label_headers='label', export_checkbox_label='true'):
    """
    Generates a pandas.DataFrame of the responses stored in a REDCap database.  This method was
    written specifically to export records.  It may work with other requests, but tread lightly.

    Args:
        api_url <str>: The url to post the http requests to.
        api_token <str>: The token granted to the api user (caller of this method).
        file_format <str>: Can be 'csv', 'json', or 'odm'.  REDCap default is 'odm', this method's
                           default is 'csv'.
        content <str>: The content to return.  May be 'arm', 'record', 'file', etc.  See REDCap api
                       for more details.  Default is 'record'.
        export_type <str>: May be 'flat' or 'eav'.  Default is 'flat'.
        raw_or_label <str>: Whether to get labeled data or raw codelist resposes. Default is 'raw'.
        raw_or_label_headers <str>: Whether to export the column labels or variable names. Default
                                    is 'label'.
        export_checkbox_label <str>: Whether to export the column labels for checkbox entries,
                                    'true' or 'false'. Default is 'true'.

    Returns:
        <pandas.DataFrame>
    """

    payload = {
        'token': api_token,
        'format': file_format,
        'content': content,
        'type': export_type,
        'rawOrLabel': raw_or_label,
        'rawOrLabelHeaders': raw_or_label_headers,
        'exportCheckboxLabel': export_checkbox_label
    }

    response = requests.post(api_url, data=payload)
    results = response.content.decode('UTF8', errors='replace')
    results = StringIO(results)
    return pd.read_csv(results, skiprows=1)

def get_sql_server_table(driver, server_name, db_name, table_name, user_id, user_password,
                         columns=None):
    """
    Generates a pandas.DataFrame of the result of a SQL query on a database (specifically this was
    used/tested on a Microsoft SQL Server).  The resulting frame can be the entire table or a subset
    of the columns.  The main point of this method is to quickly get all records tied to a table,
    not to perform any record-wise subsetting.  Currently this method enforces logging into the
    server.

    Args:
        driver <str>: The string representing the ODBC driver to use when querying the SQL Server.
        server_name <str>: The name of the server to connect to (or the IP address if no name).
        db_name <str>: The specific database to query.
        table_name <str>: The specific table in the database to query.
        user_id <str>: The user's id (to log into the server).
        user_password <str>: The user's password.
        columns <list <str>>: A list of column names to export from the table.  If None, return the
                              entire table.  Default is None.

    Returns:
        <pandas.DataFrame>
    """

    conn = pyodbc.connect(driver=driver, host=server_name, database=db_name, user=user_id,
                          password=user_password)
    selection = '*' if columns is None else ','.join(columns)
    sql_statement = 'SELECT %s FROM %s.%s' % (selection, db_name, table_name)
    return pd.read_sql(sql_statement, conn)

def get_file_from_sftp(filepath, download_filepath, hostname, user_id, user_password, port=22):
    """
    Downloads a file from a remote SFTP server.  This was used only to download .zip files
    containing .csv files.

    Args:
        filepath <str>: The filepath of the file to download in the SFTP server.
        download_filepath <str>: The download location for the file, including the filename.
        hostname <str>: The hostname to connect to.
        user_id <str>: The user id to login to the server.
        user_password <str>: The user password to login to the server.
        port <int>: The port to connect to.  Default is 22.

    Returns:
        None: Download file to download_filepath if the file is available.
    """

    # Ignore the host key
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None

    with pysftp.Connection(host=hostname, username=user_id, password=user_password, port=port,
                           cnopts=cnopts) as sftp:
        try:
            sftp.get(filepath, download_filepath)
            print('Successfully Downloaded %s to %s' % (filepath, download_filepath))
        except FileNotFoundError:
            print('[*] Error: Could not find file %s' % filepath)
            print('Confirm that the file exists.')
