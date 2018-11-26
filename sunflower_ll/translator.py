from sunflower_ll.axis_helper import *
#import constants

TOPIC = 'topic'
COMMAND = 'command'

OK = 0
ERROR = 1

class Translator:

    def __init__(self):
        self.__commands = {
            'go_up': {TOPIC: 'movement/up_down', COMMAND: 'up'},
            'go_down': {TOPIC: 'movement/up_down', COMMAND: 'down'},
            'stop_up_down': {TOPIC: 'movement/up_down', COMMAND: 'stop'},
        
            'expand': {TOPIC: 'movement/expand_retract', COMMAND: 'expand'},
            'retract': {TOPIC: 'movement/expand_retract', COMMAND: 'retract'},
            'stop_expand_retract': {TOPIC: 'movement/expand_retract', COMMAND: 'stop'},

            'unlock': {TOPIC: 'movement/axis', COMMAND: 'unlock'},
            'go_home': {TOPIC: 'movement/axis', COMMAND: 'go_home'},
            'move_axis': {TOPIC: 'movement/axis'} # axis feedback -> movement/axis_feedback 
        }

        self.__axis_angles = {
            'angle_1': 0,
            'angle_2': 0,
            'angle_3': 0
        }

        self.__magnetometer_data = {
            'mag_1': 0,
            'mag_2': 0
        }

        self.__angle_error_offset = {
            'angle_1': 0,
            'angle_2': 0,
            'angle_3': 0,
        }

        self.__movement_speed = 500

        self.__operation_mode = 'a'


    ##################################################
    ############## STRUCTURE MOVEMENT ################
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


    ##################################################
    ################# AXIS MOVEMENTS #################
    ##################################################
    
    def unlock(self):
        return self.__commands['unlock']
    def go_home(self):
        return self.__commands['go_home']


    def validate_axis(self, axis_angles):
        # valid_axis_status = OK

        for key in axis_angles:
            if key == 'angle_1':
                if (axis_angles[key] < 0) or (axis_angles[key] >= 360):
                    return ERROR

            if key == 'angle_2':
                if (axis_angles[key] < 0) or (axis_angles[key] >= 90):
                    return ERROR

            if key == 'angle_3':
                if (axis_angles[key] < -360) or (axis_angles[key] >= 360): # NAO DEFINIDO
                    return ERROR

        return OK

    def max_inverse_axis(self, axis_angles):
        status = OK

        for key in axis_angles:
            if key == 'angle_1':
                angle_1 = (-1)* axis_angles[key]

                if (angle_1 < 0):
                    angle_1 = max(0, angle_1)
                    status = ERROR
                if (angle_1 >= 360):
                    angle_1 = min(360, angle_1)
                    status = ERROR

                axis_angles[key] = (-1)* angle_1

            if key == 'angle_2':
                angle_2 = (-1)* axis_angles[key]

                if (angle_2 < 0):
                    angle_2 = max(0, angle_2)
                    status = ERROR
                if (angle_2 >= 180):
                    angle_2 = min(180, angle_2)
                    status = ERROR

                axis_angles[key] = (-1)* angle_2

            if key == 'angle_3':
                angle_3 = (-1)* axis_angles[key]

                if (angle_3 < -360):
                    angle_3 = max(-360, angle_3)
                    status = ERROR
                if (angle_3 >= 360):
                    angle_3 = min(360, angle_3)
                    status = ERROR

                axis_angles[key] = (-1)* angle_3
                

        return status



    def generate_movement_string(self, axis_angles, speed):
        gcode = 'G1 ' + \
            ' X'+str(axis_angles['angle_1']) + \
            ' Y'+str(axis_angles['angle_2']) + \
            ' Z'+str(axis_angles['angle_3']) + \
            ' F'+str(speed)
        return gcode



    def move_axis(self):
        status = OK

        magnetometer_data  = self.get_magnetometer_data()
        movement_speed     = self.get_movement_speed()

        print(self.__axis_angles)

        antenna_angles = generate_antenna_angles( \
                                    self.__axis_angles, 
                                    self.__angle_error_offset,
                                    magnetometer_data, 
                                    self.__operation_mode
                                    )

        print(antenna_angles)

      
        if (self.max_inverse_axis(antenna_angles) != OK):
            print('INVALID')
            # raise Exception('Invalid axis, FROM MOVE_AXIS')
            #print('**** INVALID MOVEMENT ****')
            #return (ERROR, {'topic': 'movement/axis', 'command': 'G1  X0 Y0 Z0 F100'} )
            status = ERROR

        gcode = self.generate_movement_string(antenna_angles, movement_speed)


        move_axis_command = self.__commands['move_axis']
        move_axis_command[COMMAND] = gcode

        return (status, move_axis_command)



    def set_axis_angles(self, new_axis_angles):

        if (self.validate_axis(new_axis_angles) != OK):
            # raise Exception('Invalid axis, FROM UPDATE_AXIS')
            #print('**** INVALID UPDATE ****')
            return ERROR

        for key in new_axis_angles:
            if key == 'angle_1':
                self.__axis_angles[key] = new_axis_angles[key]
            if key == 'angle_2':
                self.__axis_angles[key] = new_axis_angles[key]
            if key == 'angle_3':
                self.__axis_angles[key] = new_axis_angles[key]

        return OK



    def get_axis_angles(self):
        return self.__axis_angles


    ##################################################
    #################### SETTINGS ####################
    ##################################################


    def set_movement_speed(self, movement_speed):
        if (movement_speed > 0) and (movement_speed <= 1000): 
            self.__movement_speed = movement_speed
            return 0
        return 1

    def get_movement_speed(self):
        return self.__movement_speed




    def set_operation_mode(self, operation_mode):
        if (operation_mode == "a") or (operation_mode == "b"): 
            self.__operation_mode = operation_mode
            return 0
        return 1

    def get_operation_mode(self):
        return self.__operation_mode




    ##################################################
    #################### SENSORS ####################
    #################################################

    # Magnetometer Data
    def set_magnetometer_data(self, value):
        self.__magnetometer_data['mag_1'] = value
        return 0

    def get_magnetometer_data(self):
        mag_1 = self.__magnetometer_data['mag_1']
        return mag_1


    def set_angle_error_offset(self, angles):

        for key in angles:
            if key == 'angle_1':
                self.__angle_error_offset[key] = angles[key]
            if key == 'angle_2':
                self.__angle_error_offset[key] = angles[key]
            if key == 'angle_3':
                self.__angle_error_offset[key] = angles[key]

        return 0

    def get_angle_error_offset(self):

        return self.__angle_error_offset






