import random


class Transformer:

    def __init__(self):
        print("Transformer is being initialized!")

    def predict(self, text):
        import time
        time.sleep(5)
        return random.randint(1,10)


def get_ml_model():
    return Transformer()

