class ParseResponse:
    """Parse Response class to return success and error responses"""

    def error_response(self, error_class, message):
        return {
            "message": message,
            "status_code": error_class.status_code,
        }, error_class.status_code

    def success_response(self, response_dict, status_code=200):
        return response_dict, status_code
