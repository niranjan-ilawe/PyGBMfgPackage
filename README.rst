pygbmfg
--------
v0.1

Package contains all the relevant scripts to pull manufacturing and QC data from all the GB Manufacturing process areas. 
The flagship functions of this package are the `run_*_pipeline` scripts that will read the files from Box, transform them into dataframes,
and push the dataframes to the CPPDA postgres database.

Basic use is as follows

    >>> import pygbmfg
    >>> pygbmfg.run_gb_func_pipeline()

This defaults to pulling the last 3 days worth of data. For pulling older data

    >>> pygbmfg.run_gb_func_pipeline(days=90)

pulls the last 90 days worth of data.

If you want to push data to a different database or download to a file. Utilize the other functions defined in the package

    >>> df1 = get_maverick_data(last_modified_date=last_modified_date)
    >>> upload_func_data(df1, username="cpdda", db_name="test")

### Notes:
The package assumes that you have access to the Box files the package references. And that you have installed the pybox and pydb packages.
It also assumes that credentials to access the databases are stored using the keyring package since keyring is used to retrieve these from 
your local env.