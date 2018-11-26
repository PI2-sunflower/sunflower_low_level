import unittest
import sunflower_ll.translator as translator

class TranslatorTests(unittest.TestCase):
    def setUp(self):
        self.tr = translator.Translator()
    
    def test_basic_movements(self):
        # can run the basic movements...
        self.assertTrue(self.tr.go_up())
        self.assertTrue(self.tr.go_down())
        self.assertTrue(self.tr.stop_up_down())
        self.assertTrue(self.tr.expand())
        self.assertTrue(self.tr.retract())
        self.assertTrue(self.tr.stop_expand_retract())

    def test_go_up(self):
        self.assertEqual(self.tr.go_up(), {'topic': 'movement/up_down', 'command': 'up'})
    def test_go_down(self):
        self.assertEqual(self.tr.go_down(), {'topic': 'movement/up_down', 'command': 'down'})
    def test_expand(self):
        self.assertEqual(self.tr.expand(), {'topic': 'movement/expand_retract', 'command': 'expand'})
    def test_retract(self):
        self.assertEqual(self.tr.retract(), {'topic': 'movement/expand_retract', 'command': 'retract'})

    def test_unlock(self):
        self.assertEqual(self.tr.unlock(), {'topic': 'movement/axis', 'command': 'unlock'})
    def test_go_home(self):
        self.assertEqual(self.tr.go_home(), {'topic': 'movement/axis', 'command': 'go_home'})


    def test_get_set_speed(self):
        self.assertEqual(self.tr.set_movement_speed(321), 0)
        self.assertEqual(self.tr.get_movement_speed(), 321)

        self.assertEqual(self.tr.set_movement_speed(1321), 1)
        self.assertEqual(self.tr.get_movement_speed(), 321)


    def test_get_set_operation_mode(self):
        self.assertEqual(self.tr.set_operation_mode("a"), 0)
        self.assertEqual(self.tr.get_operation_mode(), "a")

        self.assertEqual(self.tr.set_operation_mode("c"), 1)
        self.assertEqual(self.tr.get_operation_mode(), "a")

        self.assertEqual(self.tr.set_operation_mode("b"), 0)
        self.assertEqual(self.tr.get_operation_mode(), "b")

        self.assertEqual(self.tr.set_operation_mode("c"), 1)
        self.assertEqual(self.tr.get_operation_mode(), "b")

        self.assertEqual(self.tr.set_operation_mode("a"), 0)
        self.assertEqual(self.tr.get_operation_mode(), "a")



    def test_magnetometer_data(self):
        self.assertEqual(self.tr.set_magnetometer_data(359.5), 0)
        self.assertEqual(self.tr.get_magnetometer_data(), 359.5)



    def test_set_and_get_axis_angles(self):
        good_angles = {
            'angle_1': 11,
            'angle_2': 55,
            'angle_3': 99
        }
        # Good angles
        self.assertEqual(self.tr.set_axis_angles(good_angles), 0)
        self.assertEqual(self.tr.get_axis_angles(), good_angles)
        
        bad_angles = {
            'angle_1': 100,
            'angle_2': -10,
            'angle_3': 150
        }
        # Bad angles
        self.assertEqual(self.tr.set_axis_angles(bad_angles), 1)
        self.assertEqual(self.tr.get_axis_angles(), good_angles)
        
        # Bad single angles
        bad_angle1 = {
            'angle_1': 1000
        }
        self.assertEqual(self.tr.set_axis_angles(bad_angle1), 1)
        bad_angle2 = {
            'angle_2': 1000
        }
        self.assertEqual(self.tr.set_axis_angles(bad_angle2), 1)
        bad_angle3 = {
            'angle_3': 1000
        }
        self.assertEqual(self.tr.set_axis_angles(bad_angle3), 1)
        self.assertEqual(self.tr.get_axis_angles(), good_angles)

        # Good single angle
        good_angle2 = {
            'angle_2': 70
        }
        good_angles['angle_2'] = 70
        self.assertEqual(self.tr.set_axis_angles(good_angle2), 0)
        self.assertEqual(self.tr.get_axis_angles(), good_angles)


    def test_axis_movement(self):
        self.assertEqual(self.tr.move_axis(), (0, {'topic': 'movement/axis', 'command': 'G1  X0 Y0 Z0 F500'}))

        good_angles = {
            'angle_1': 11,
            'angle_2': 55,
            'angle_3': 99
        }
        # Good angles
        self.assertEqual(self.tr.set_axis_angles(good_angles), 0)
        self.assertEqual(self.tr.set_movement_speed(211), 0)
        self.assertEqual(self.tr.move_axis(), (0, {'topic': 'movement/axis', 'command': 'G1  X-11 Y-55 Z-99 F211'}))


    def test_angle_error_offset(self):
        self.assertEqual(self.tr.move_axis(), (0, {'topic': 'movement/axis', 'command': 'G1  X0 Y0 Z0 F500'}))

        angle_error_offset = {
            'angle_1': 4.5,
            'angle_2': 9.3,
            'angle_3': 3.3,
        }
        self.assertEqual(self.tr.set_angle_error_offset(angle_error_offset), 0);
        self.assertEqual(self.tr.get_angle_error_offset(), angle_error_offset);
        self.assertEqual(self.tr.move_axis(), (0, {'topic': 'movement/axis', 'command': 'G1  X-4.5 Y-9.3 Z-3.3 F500'}))


    def test_axis_movement_with_mag_and_error(self):
        self.assertEqual(self.tr.move_axis(), (0, {'topic': 'movement/axis', 'command': 'G1  X0 Y0 Z0 F500'}))

        good_angles = {
            'angle_1': 11,
            'angle_2': 55,
            'angle_3': 99
        }

        self.assertEqual(self.tr.set_magnetometer_data(358.5), 0)

        angle_error_offset = {
            'angle_1': 0.3,
            'angle_2': 0.3,
            'angle_3': 0.3333333,
        }
        self.assertEqual(self.tr.set_angle_error_offset(angle_error_offset), 0);


        # Good angles
        self.assertEqual(self.tr.set_axis_angles(good_angles), 0)
        self.assertEqual(self.tr.set_movement_speed(715), 0)
        self.assertEqual(self.tr.move_axis(), (0, {'topic': 'movement/axis', 'command': 'G1  X-9.8 Y-55.3 Z-99.3333 F715'}))


        angle_error_offset_2 = {
            'angle_1': -50,
            'angle_2': 0,
            'angle_3': -100,
        }
        self.assertEqual(self.tr.set_angle_error_offset(angle_error_offset_2), 0);
        self.assertEqual(self.tr.move_axis(), (0, {'topic': 'movement/axis', 'command': 'G1  X-319.5 Y-55 Z-359 F715'}))


        limit_angle_error_offset = {
            'angle_1': 0,
            'angle_2': -56,
            'angle_3': 0,
        }
        self.assertEqual(self.tr.set_angle_error_offset(limit_angle_error_offset), 0);
        self.assertEqual(self.tr.move_axis(), (1, {'topic': 'movement/axis', 'command': 'G1  X-9.5 Y0 Z-99 F715'}))




if __name__ == '__main__':
    unittest.main()



