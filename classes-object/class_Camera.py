class Camera:

    def __int__(self, serial_number, position, camera_type):
        self.serial_number = serial_number
        self.position = position
        self.camera_type = camera_type

    def __str__(self):
        return f"Serial Numbers: {self.serial}, Camera type: {self.camera_type} Position: {self.position}"
