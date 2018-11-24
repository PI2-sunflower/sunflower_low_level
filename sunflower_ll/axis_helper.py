# def validate_axis(axis_angles):
#     VALID = 0
#     INVALID = 1
#     angle_1 = axis_angles['angle_1']
#     angle_2 = axis_angles['angle_2']
#     angle_3 = axis_angles['angle_3']
#     valid_axis = VALID

#     if (angle_1 < 0) or (angle_1 >= 360):
#         valid_axis = INVALID
#     if (angle_2 < 0) or (angle_2 >= 90):
#         valid_axis = INVALID
#     if (angle_3 < -360) or (angle_3 >= 360): # NAO DEFINIDO
#         valid_axis = INVALID
#     return valid_axis

# def try_update_axis(old_axis_angles, new_axis_angles):
#     axis_angle = dict(old_axis_angles)
#     for key in new_axis_angles:
#         if key == 'angle_1':
#             axis_angle[key] = new_axis_angles[key]
#         if key == 'angle_2':
#             axis_angle[key] = new_axis_angles[key]
#         if key == 'angle_3':
#             axis_angle[key] = new_axis_angles[key]
#     if (validate_axis(axis_angle) != 0):
#         raise Exception('Invalid axis, FROM UPDATE_AXIS')
#     return axis_angle


# def try_move_axis(axis_angles, speed):
#     if (validate_axis(axis_angles) != 0):
#         raise Exception('Invalid axis angles, FROM MOVE_AXIS')

#     gcode = 'G1 ' + \
#         ' X'+str(axis_angles['angle_1']) + \
#         ' Y'+str(axis_angles['angle_2']) + \
#         ' Z'+str(axis_angles['angle_3']) + \
#         ' F'+str(speed)

#     return gcode

def generate_antenna_angles(axis_angles, angle_error_offset, magnetometer_angle, operation_mode):
    #TODO: ADD magnetometer_data, elevation_angle_data TO RESPECTIVE ANGLES...
    antenna_angles = {}
    for key in axis_angles:

        if key == 'angle_1':
            antenna_angle_1 = 0

            if (operation_mode == 'a'):
                antenna_angle_1 = axis_angles[key] + magnetometer_angle + angle_error_offset[key]

            elif (operation_mode == 'b'):
                antenna_angle_1 = (axis_angles[key] + magnetometer_angle + angle_error_offset[key]) + 180


            if antenna_angle_1 > 360:
                antenna_angle_1 -= 360
            if antenna_angle_1 < 0:
                antenna_angle_1 += 360

            antenna_angles[key] = (-1) * antenna_angle_1


        if key == 'angle_2':
            antenna_angle_2 = 0

            if (operation_mode == 'a'):
                antenna_angle_2 = axis_angles[key] + angle_error_offset[key]

            elif (operation_mode == 'b'):
                antenna_angle_2 = 180 - (axis_angles[key] + angle_error_offset[key])


            if antenna_angle_2 > 360:
                antenna_angle_2 -= 360
            if antenna_angle_2 < 0:
                antenna_angle_2 += 360
                
            antenna_angles[key] = (-1) * antenna_angle_2

        if key == 'angle_3':
            antenna_angle_3 = axis_angles[key] + angle_error_offset[key]

            if antenna_angle_3 > 360:
                antenna_angle_3 -= 360
            if antenna_angle_3 < 0:
                antenna_angle_3 += 360

            antenna_angles[key] = (-1) * antenna_angle_3

    return antenna_angles



