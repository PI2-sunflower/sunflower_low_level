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

    
    def validate_axis(self, angle_1, angle_2, angle_3):
        valid_axis = True
        
        if (angle_1 < 0) or (angle_1 >= 360):
            valid_axis = False

        if (angle_2 < 0) or (angle_2 >= 180):
            valid_axis = False

        if (angle_3 < 0) or (angle_3 >= 360):
            valid_axis = False
        
        return valid_axis

    def update_axis(self, axis_value):
        angle_1 = self.__axis_angles['axis_1']
        angle_2 = self.__axis_angles['axis_2']
        angle_3 = self.__axis_angles['axis_3']
        
        for key in axis_value:
            if key == 'axis_1':
                angle_1 = axis_value[key]
            if key == 'axis_2':
                angle_2 = axis_value[key]
            if key == 'axis_3':
                angle_3 = axis_value[key]

        if (not self.validate_axis(angle_1, angle_2, angle_3)):
            raise Exception('Invalid axis, FROM UPDATE_AXIS')

        self.__axis_angles['axis_1'] = angle_1
        self.__axis_angles['axis_2'] = angle_2
        self.__axis_angles['axis_3'] = angle_3


    def move_axis(self):
        angle_1 = self.__axis_angles['axis_1']
        angle_2 = self.__axis_angles['axis_2']
        angle_3 = self.__axis_angles['axis_3']
 
        if (not self.validate_axis(angle_1, angle_2, angle_3)):
            raise Exception('Invalid axis angles, FROM MOVE_AXIS')

        gcode = 'G1 ' + 'X'+str(angle_1) + ' '\
                      + 'Y'+str(angle_2) + ' '\
                      + 'Z'+str(angle_3) + ' '\
                      + 'F'+str(self.__movement_speed)
        
        return gcode


    def move_single_axis(self, axis, angle):
        axis_value = {axis: angle}
        self.update_axis(axis_value)
        gcode = self.move_axis()
        return gcode




