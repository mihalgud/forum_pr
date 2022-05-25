
class Sum:
    
    def __init__(self, params):
        self.val_1=params.get('val_1')
        self.val_2=params.get('val_2')

    def call(self):
        return {
            'val_1': self.val_1,
            'val_2': self.val_2,
            'result': self.val_1+self.val_2
        }