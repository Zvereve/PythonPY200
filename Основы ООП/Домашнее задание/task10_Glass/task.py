from typing import Union


class Glass:
    def __init__(self, material: Union[str]):
        self.material = material


    def get_material(self):
        return self.material



if __name__ == "__main__":
    glass1 = Glass("glass")
    print(glass1.material)

