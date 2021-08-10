class Loader:
    """
    The Loader class unifies the API load workflow. It has a method to accept a filename
    and attempt to upload it to the API.
    """

    def __init__(self, input_filename: str):
        
        self.input_filename = input_filename


class LoaderException(Exception):
    """
    The LoaderException class is for exceptions raised during a load operation. It is
    raised as part of the exception handling of the Loader class. Use of this exception
    generally follows a two step process:

    1. A JSONBuilderException, CsvIngestException, or APIException is caught by an
    instance of the Loader class.

    2. That original exception is reported to the user with a print statement.

    3. A loader exception is raised that contains the original message as well as
    any additional context information of for the Loader exception.

    4. The code calling the instance of this Loader class can then catch the
    LoaderException and report it to the user.

    Additionally, a LoaderException can be raised on its own by the Loader class
    for errors that fall outside the scope of the other three exceptions.
    """

    def __init__(self, message: str):
        super(LoaderException, self).__init__(message)
