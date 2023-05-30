class ButtonNotFoundException(Exception):
    def __init__(self, message="A button was not found"):
        self.message = message
        super().__init__(self.message)

class StatsNotFoundException(Exception):
    def __init__(self, message="Stats could not be found"):
        self.message = message
        super().__init__(self.message)

class CaptchaImageNotFoundException(Exception):
    def __init__(self, message="Captcha image was not found"):
        self.message = message
        super().__init__(self.message)