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

            antenna_angle_1 = round(antenna_angle_1, 4)
            antenna_angles[key] = (-1) * antenna_angle_1


        if key == 'angle_2':
            antenna_angle_2 = 0

            if (operation_mode == 'a'):
                antenna_angle_2 = axis_angles[key] + angle_error_offset[key]

            elif (operation_mode == 'b'):
                antenna_angle_2 = 180 - (axis_angles[key] + angle_error_offset[key])

            # NOT VALID FOR ANGLE 2
            # if antenna_angle_2 > 360:
            #     antenna_angle_2 -= 360
            # if antenna_angle_2 < 0:
            #     antenna_angle_2 += 360
            
            antenna_angle_2 = round(antenna_angle_2, 4) 
            antenna_angles[key] = (-1) * antenna_angle_2

        if key == 'angle_3':
            antenna_angle_3 = axis_angles[key] + angle_error_offset[key]

            if antenna_angle_3 > 360:
                antenna_angle_3 -= 360
            if antenna_angle_3 < 0:
                antenna_angle_3 += 360

            antenna_angle_3 = round(antenna_angle_3, 4)
            antenna_angles[key] = (-1) * antenna_angle_3

    return antenna_angles



