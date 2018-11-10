import axis_helper
import constants
class Translator:

    __commands = {
        'go_up': {'topic': 'up_down', 'command': 'up'},
        'go_down': {'topic': 'up_down', 'command': 'down'},
    }

    __axis_angles = {
        'axis_1': -1,
        'axis_2': -1,
        'axis_3': -1
    }

    __magnetometer_data = {
        'mag_1': 0,
        'mag_2': 0
    }

    __movement_speed = 100


    # Create sensor class
    def set_magnetometer_data(self, reference, value):
        self.__magnetometer_data[reference] = value

    def get_magnetometer_data(self):
        TOL = 1
        mag_1 = self.__magnetometer_data['mag_1']
        mag_2 = self.__magnetometer_data['mag_2']

        if abs(mag_1 - mag_2) > TOL:
            raise Exception('Magnetometer data is not reliable')

        average = (mag_1 + mag_2)/2
        return average



    def go_up(self):
        return self.__commands['go_up']

    def go_down(self):
        return self.__commands['go_down']

    def update_axis(self, new_axis_angles):
        try:
            new_angles = axis_helper.try_update_axis(__axis_angles, new_axis_angles)
        except:
            return 1
        __axis_angles = new_angles
        return 0

    def move_axis(self):
        try:
            gcode = axis_helper.try_move_axis(__axis_angles)
        except:
            DEFAULT_MOVEMENT = 'G1 X0 Y0 Z0 F100'
            gcode = DEFAULT_MOVEMENT

        return gcode


    def move_single_axis(self, axis, angle):
        axis_value = {axis: angle}
        self.update_axis(axis_value)
        gcode = self.move_axis()
        return gcode


