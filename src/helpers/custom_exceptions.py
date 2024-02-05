class InvalidCredentials(Exception):
    status_code = 401


class DataAlreadyExists(Exception):
    status_code = 409


class DuplicateEntryError(Exception):
    status_code = 409


class DataNotFound(Exception):
    status_code = 404


class DbException(Exception):
    pass
