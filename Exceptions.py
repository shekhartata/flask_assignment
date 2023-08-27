# Exception class

class ProcessErrorException(Exception):
    def __init__(self, err_msg):
        self.err_message = err_msg
        super().__init__(self.err_message)
