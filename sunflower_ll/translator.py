from sunflower_ll.axis_helper import *
#import constants

TOPIC = 'topic'
COMMAND = 'command'

class Translator:

    __commands = {
        'go_up': {TOPIC: 'up_down', COMMAND: 'up'},
        'go_down': {TOPIC: 'up_down', COMMAND: 'down'},
        'stop_up_down': {TOPIC: 'up_down', COMMAND: 'stop'},
    
        'expand': {TOPIC: 'expand_retract', COMMAND: 'expand'},
        'retract': {TOPIC: 'expand_retract', COMMAND: 'retract'},
        'stop_expand_retract': {TOPIC: 'expand_retract', COMMAND: 'stop'},

        'move_axis': {TOPIC: 'move_axis'}
    }

    __axis_angles = {
        'angle_1': 0,
        'angle_2': 0,
        'angle_3': 0
    }

    __magnetometer_data = {
        'mag_1': 0,
        'mag_2': 0
    }

    __elevation_angle_data = {
        'angle_1': 0,
        'angle_2': 0
    }

    __movement_speed = 100



    ##################################################
    ################### ACTUATORS ####################
    ##################################################

    # ************** UP AND DOWN **************
    def go_up(self):
        return self.__commands['go_up']
    def go_down(self):
        return self.__commands['go_down']
    def stop_up_down(self):
        return self.__commands['stop_up_down']


    # ************** EXPAND AND RETRACT **************
    def expand(self):
        return self.__commands['expand']
    def retract(self):
        return self.__commands['retract']
    def stop_expand_retract(self):
        return self.__commands['stop_expand_retract']


    # ************** AXIS MOVEMENTS **************
    def set_axis_angles(self, new_axis_angles):
        VALID = 0
        INVALID = 1
        try:
            new_angles = try_update_axis(self.__axis_angles, new_axis_angles)
        except:
            print('**** INVALID UPDATE ****')
            return INVALID
        self.__axis_angles = new_angles
        return VALID

    def set_single_axis_angle(self, axis, angle):
        single_axis = {axis: angle}
        return self.set_axis_angles(single_axis)

    def get_axis_angles(self):
        return self.__axis_angles

    def move_axis(self):
        try:
            magnetometer_data = self.get_magnetometer_data()
            elevation_angle_data = self.get_elevation_angle_data()
            antenna_angles = update_angles_from_reference( \
                                        self.__axis_angles, 
                                        magnetometer_data,
                                        elevation_angle_data)
            gcode = try_move_axis(antenna_angles, self.__movement_speed)
        except:
            print('**** INVALID MOVEMENT ****')
            gcode = ''
        move_axis_command = self.__commands['move_axis']
        move_axis_command[COMMAND] = gcode
        return move_axis_command

    def set_movement_speed(self, movement_speed):
        if (movement_speed > 0) and (movement_speed < 1000): 
            self.__movement_speed = movement_speed
            return 0
        return 1

    def get_movement_speed(self):
        return self.__movement_speed




    ##################################################
    #################### SENSORS ####################
    #################################################

    # Magnetometer Data
    def set_magnetometer_data(self, value1, value2):
        TOL = 1
        if abs(value1 - value2) > TOL:
            print('******** Magnetometer data is not reliable ********')
            return 1
        else:
            self.__magnetometer_data['mag_1'] = value1
            self.__magnetometer_data['mag_2'] = value2
            return 0

    def get_magnetometer_data(self):
        mag_1 = self.__magnetometer_data['mag_1']
        mag_2 = self.__magnetometer_data['mag_2']

        average = (mag_1 + mag_2)/2
        return average


    # Elevation Angle data
    def set_elevation_angle_data(self, value1, value2):
        TOL = 1
        if abs(value1 - value2) > TOL:
            print('******** Elevation data is not reliable ********')
            return 1
        else:
            self.__elevation_angle_data['angle_1'] = value1
            self.__elevation_angle_data['angle_2'] = value2
            return 0

    def get_elevation_angle_data(self):
        ead_1 = self.__elevation_angle_data['angle_1']
        ead_2 = self.__elevation_angle_data['angle_2']

        average = (ead_1 + ead_2)/2
        return average
