def validate_axis(axis_angles):
    VALID = 0
    INVALID = 1
    angle_1 = axis_angles['angle_1']
    angle_2 = axis_angles['angle_2']
    angle_3 = axis_angles['angle_3']
    valid_axis = VALID

    if (angle_1 < 0) or (angle_1 >= 360):
        valid_axis = INVALID
    if (angle_2 < 0) or (angle_2 >= 180):
        valid_axis = INVALID
    if (angle_3 < 0) or (angle_3 >= 360):
        valid_axis = INVALID
    return valid_axis

def try_update_axis(old_axis_angles, new_axis_angles):
    axis_angle = dict(old_axis_angles)
    for key in new_axis_angles:
        if key == 'angle_1':
            axis_angle[key] = new_axis_angles[key]
        if key == 'angle_2':
            axis_angle[key] = new_axis_angles[key]
        if key == 'angle_3':
            axis_angle[key] = new_axis_angles[key]
    if (validate_axis(axis_angle) != 0):
        raise Exception('Invalid axis, FROM UPDATE_AXIS')
    return axis_angle


def try_move_axis(axis_angles, speed):
    if (validate_axis(axis_angles) != 0):
        raise Exception('Invalid axis angles, FROM MOVE_AXIS')
    gcode = 'G1 ' + \
        ' X'+str(axis_angles['angle_1']) + \
        ' Y'+str(axis_angles['angle_2']) + \
        ' Z'+str(axis_angles['angle_3']) + \
        ' F'+str(speed)
    return gcode

def update_angles_from_reference(axis_angles, magnetometer_data, elevation_angle_data):
    #TODO: ADD magnetometer_data, elevation_angle_data TO RESPECTIVE ANGLES...
    antenna_angles = {}
    for key in axis_angles:
        if key == 'angle_1':
            antenna_angles[key] = axis_angles[key] 
        if key == 'angle_2':
            antenna_angles[key] = axis_angles[key]
        if key == 'angle_3':
            antenna_angles[key] = axis_angles[key]
    return antenna_angles



