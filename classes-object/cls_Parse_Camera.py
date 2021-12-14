class ParseCamera:
    def __init__(self):
        pass

    def parse_camera(self):

        with open("cameras.txt") as f:
            d = f.read().strip().split(' ')
            serial_number = d[0]
            position = Position(int(d[1]), int(d[2]), int(d[3]))
            camera_type = Camera.CameraType[d[4]]
        return Camera(serial_number, position, camera_type)