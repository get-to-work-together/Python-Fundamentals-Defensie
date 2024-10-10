def calculate_area(width, height):
    if width < 0 or height < 0:
        raise Exception('Invalid argument')
    return width * height


try:
    area = calculate_area(10, -3)
    print(area)

except Exception as err:
    print(err)
