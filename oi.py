import wpilib
from state import state

def read_input_mecanum ():
	controller = wpilib.Joystick(1)


	x = controller.getX()
	state["mov_x"] = x

	y = controller.getY()
	state["mov_y"] = y

	z = controller.getZ()
	state["mov_z"] = z

	button_x = controller.getRawButton(8)
	state["button_x_active"] = button_x


def read_input_velcrolastick ():
	stick = wpilib.Joystick(1)
	#VELCROLASTICK BUTTON
	e = stick.getRawButton(4)
	state["lift_up"] = e

def read_input_linefollow ():
	stick = wpilib.Joystick(1)
	#LineFollow Button
	y_button = stick.getRawButton(7)
	state["button_y_on"] = y_button

def read_input_cargo ():
	stick = wpilib.Joystick(1)

	button_1_is_pressed = stick.getRawButton(5)
	state["cargo"] = button_1_is_pressed
	
def read_input_lift ():

	stick = wpilib.Joystick(1)
	
	button_2_is_pressed = stick.getRawButton(6)
	state["lift"] = button_2_is_pressed

"""LINE FOLLOW"""

def setup_for_robot (robot):
	
    robot.sensor_EIZ_line = wpilib.DigitalInput(1)
    robot.sensor_MIZ_line = wpilib.DigitalInput(2)
    robot.sensor_MM_line = wpilib.DigitalInput(3)
    robot.sensor_MDE_line = wpilib.DigitalInput(4)
    robot.sensor_EDE_line = wpilib.DigitalInput(5)


    