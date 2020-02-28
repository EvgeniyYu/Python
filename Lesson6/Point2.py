class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calcWeight(self, weight, thickness):
        return self.__length * self.__width * weight * thickness

while True:
    try:
        _length = int(input('Input the road length: '))
        _width = int(input('Input the road width: '))
        _weight = int(input('Input the road weight: '))
        _thickness = int(input('Input the road thickness: '))
        road = Road(_length, _width)
        print(f'The weight of the road is {road.calcWeight(_weight, _thickness)}')
        break
    except ValueError:
        print('Error! Enter the number!')
