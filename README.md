## SUNFLOWER LOW LEVEL
THIS IS PART OF THE SOFTWARE USED IN THE SUNFLOWER PROJECT.

This library converts high level information into lower level information, used to control the system motors.
Function call's are converted into G-Code strings.

## INSTALLING:

### PRODUCTION:
    pip install -i https://test.pypi.org/simple/ sunflower-ll

### DEVELOP:
    python3 setup.py develop


## BASIC USAGE:

### Import
    import sunflower_ll.translator as translator
    tr = translator.Translator()

### Going up/down
    -> tr.go_up() : "returns output to send to broker"
    -> tr.go_down() : "returns output to send to broker"
    -> tr.stop_up_down() : "returns output to send to broker"

### Expanding/contracting
    -> tr.expand() : "returns output to send to broker"
    -> tr.retract() : "returns output to send to broker"
    -> tr.stop_expand_retract() : "returns output to send to broker"

### Moving axis
    -> angles = {
        'angle_1': 11,
        'angle_2': 55,
        'angle_3': 99
    }
    -> tr.set_axis_angles(angles) : "0=sucess, 1=fail"
        - angles is a dictionary like the one above. It has the identifiers 'angle_1', 'angle_2', 'angle_3'
        - output: 0="valid angle", 1="invalid angle"
    -> tr.set_single_axis_angle(identifier, angle) : "0=sucess, 1=fail"
        - identifier options: 'angle_1', 'angle_2', 'angle_3'
        - output: 0="valid angle", 1="invalid angle"
    -> tr.get_axis_angles()


    -> tr.set_movement_speed(number from 1 to 1000) : "0=sucess, 1=fail"
        - output: 0="valid speed", 1="invalid speed"
    -> tr.get_movement_speed()


    -> tr.move_axis() : "returns output to send to broker"

### Sensors

    -> tr.set_magnetometer_data(value_magnetometer_1, value_magnetometer_2)
        - output: 0="ok", 1="bad magnetometers"

    -> tr.get_magnetometer_data() : "returns magnetometer average"
