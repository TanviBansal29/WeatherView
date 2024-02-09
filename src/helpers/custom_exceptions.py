class InvalidCredentials(Exception):
    """
    Exception raised when invalid credentials provided by the user to login
    """

    status_code = 401


class DataAlreadyExists(Exception):
    """
    Exception raised if data already exists in the database
    """

    status_code = 409


class DuplicateEntryError(Exception):
    """
    Exception raised if duplicate data entered
    """

    status_code = 409


class DataNotFound(Exception):
    """
    Exception raised when data is not found or empty
    """

    status_code = 404


class DbException(Exception):
    """
    Raised when any database exception occurs
    """

    status_code = 500
