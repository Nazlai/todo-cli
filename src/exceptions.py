class NotFoundException(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        self.message = "entry not found"
