class ExceptionApi(Exception):
    status_code=500
    message="server internal error"
    def __init__(self, status_code,message,error_code="N/A"):
        self.status_code=status_code
        self.message=message
        self.error_code = error_code