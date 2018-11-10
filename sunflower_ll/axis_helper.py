def validate_axis(axis_angles):
    VALID = 0
    INVALID = 1
    angle_1 = axis_angles['axis_1']
    angle_2 = axis_angles['axis_2']
    angle_3 = axis_angles['axis_3']
    valid_axis = VALID

    if (angle_1 < 0) or (angle_1 >= 360):
        valid_axis = INVALID

    if (angle_2 < 0) or (angle_2 >= 180):
        valid_axis = INVALID

    if (angle_3 < 0) or (angle_3 >= 360):
        valid_axis = INVALID

    return valid_axis

def try_update_axis(old_axis_angles, new_axis_angles):
    angle_1 = old_axis_angles['axis_1']
    angle_2 = old_axis_angles['axis_2']
    angle_3 = old_axis_angles['axis_3']

    for key in new_axis_angles:
        if key == 'axis_1':
            angle_1 = new_axis_angles[key]
        if key == 'axis_2':
            angle_2 = new_axis_angles[key]
        if key == 'axis_3':
            angle_3 = new_axis_angles[key]

    if (not validate_axis(angle_1, angle_2, angle_3)):
        raise Exception('Invalid axis, FROM UPDATE_AXIS')

    angles_dict = {
        'axis_1': angle_1,
        'axis_2': angle_2,
        'axis_3': angle_3
    }

    return angles_dict


    def try_move_axis(axis_angles, speed):

        if (not self.validate_axis(axis_angles)):
            raise Exception('Invalid axis angles, FROM MOVE_AXIS')

        gcode = 'G1 ' + 'X'+str(angle_1) + ' '\
            + 'Y'+str(angle_2) + ' '\
            + 'Z'+str(angle_3) + ' '\
            + 'F'+str(speed)

        return gcode


