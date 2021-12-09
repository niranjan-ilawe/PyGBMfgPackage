import pkg_resources, shutil, os


def _load_credentials():
    drive_file = pkg_resources.resource_filename(__name__, "data/token-drive.pickle")
    shutil.move(drive_file, ".")
    sheets_file = pkg_resources.resource_filename(__name__, "data/token-sheets.pickle")
    shutil.move(sheets_file, ".")
    cred_file = pkg_resources.resource_filename(
        __name__, "data/credentials-sheets.json"
    )
    shutil.move(cred_file, ".")


def _clear_credentials():
    os.remove("token-drive.pickle")
    os.remove("token-sheets.pickle")
    os.remove("credentials-sheets.json")
