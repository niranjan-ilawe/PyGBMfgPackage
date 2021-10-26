pygbmfg
--------
``v0.1``

Package contains all the relevant scripts to pull manufacturing and QC data from all the GB Manufacturing process areas. 
The flagship functions of this package are the ``run_pipeline`` scripts that will read the files from Box or relevant locations, transform them into dataframes,
and push the dataframes to the CPPDA postgres database.

The scripts are structured in the following way

pygbmfg
    * func_mfg
        - file_reading_scripts
        - df_creation_scripts
        - db_upload_scripts
        - run_pipeline
    * func_qc
        - file_reading_scripts
        - df_creation_scripts
        - db_upload_scripts
        - run_pipeline
    * disp_mfg
        - file_reading_scripts

and so on for other areas.

Basic use is as follows (for the GB Functionalization Manufacturing Data)

    >>> import pygbmfg
    >>> pygbmfg.func_mfg.run_pipeline.run_pipeline(days=3)

This defaults to pulling the last 3 days worth of data. For pulling older data

    >>> pygbmfg.func_mfg.run_pipeline.run_pipeline(days=90)

pulls the last 90 days worth of data.

Similarly for the Gb Functionalization QC Data

    >>> pygbmfg.func_qc.run_pipeline.run_pipeline(days=90)

For the GB Dispensing QC Data

    >>> pygbmfg.disp_qc.run_pipeline.run_pipeline(days=90)

You can also use any other function defined in the package directly

    >>> df1 = pygbmfg.func_mfg.df_creation_scripts.get_maverick_data(last_modified_date="2021-01-01")
    >>> pygbmfg.func_mfg.db_upload_scripts.upload_data(df1, username="cpdda", db_name="test")

Notes::
~~~~~~~~~~~~~
The package assumes that you have access to the Box files the package references. And that you have installed the pybox and pydb packages.
It also assumes that credentials to access the databases are stored using the keyring package since keyring is used to retrieve these from 
your local env.