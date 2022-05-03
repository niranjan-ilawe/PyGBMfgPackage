pygbmfg
--------
``v0.1.5``

### New to v0.1.5
- Added probe hyb QC data pulling

Package contains all the relevant scripts to pull manufacturing and QC data from all the GB Manufacturing process areas. 
The flagship functions of this package are the ``run_gb_pipeline`` scripts that will read the files from Box or relevant locations, transform them into dataframes,
and push the dataframes to the CPPDA postgres database.

The scripts are structured in the following way

pygbmfg
    * func_mfg
        - file_reading_scripts
        - df_creation_scripts
    * func_qc
        - file_reading_scripts
        - df_creation_scripts
    * disp_mfg
        - file_reading_scripts

and so on for other areas.

The flagship function is run as follows

    >>> from pygbmfg.pipeline import run_gb_pipeline
    >>> run_gb_pipeline(days=3)

This defaults to pulling the last 3 days worth of data. For pulling older data

    >>> run_gb_pipeline(days=90)

pulls the last 90 days worth of data.

You can also access individual manufacturing or QC data as follows

    >>> from pygbmfg.disp_mfg.df_creation_scripts import get_disp_mfg_data
    >>> from pydb import get_postgres_connection, batch_upload_df
    >>> conn = get_postgres_connection(service_name="cpdda-postgres", username="cpdda", db_name="cpdda")
    >>> df = get_disp_mfg_data(days=3)
    >>> batch_upload_df(
            conn=conn,
            df=df,
            tablename="gbmfg.disp_mfgdata",
            insert_type="update",
            key_cols="wo",
        )

The above script only gets the Dispensing Mfg data for the last 3 days and uploads it to the relevent DB. 

As above you can access any of the individual functions and run them independently or run the entire pipeline with the flagship function.

Notes::
~~~~~~~~~~~~~
The package assumes that you have access to the Box files the package references. And that you have installed the pybox and pydb packages.
It also assumes that credentials to access the databases are stored using the keyring package since keyring is used to retrieve these from 
your local env.