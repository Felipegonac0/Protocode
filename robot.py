
import wpilib
import wpilib.drive
from state import state

from wpilib.drive import MecanumDrive

from oi import read_input_velcrolastick
from oi import read_input_linefollow
from oi import read_input_mecanum
from oi import read_input_lift
from oi import read_input_cargo


class MyRobot(wpilib.TimedRobot):

	def robotInit(self):
		#Velcrolastick
		self.lift_motor1 = wpilib.Spark(6)
		self.lift_motor2 = wpilib.Spark(7)
		self.sensor1 = wpilib.DigitalInput(7)
		self.sensor2 = wpilib.DigitalInput(8)
   
		# Ismafeeder
		self.cargo_motor = wpilib.Spark(4)
		self.lift_motor = wpilib.Spark(5)
		
		# Mecanum drive
		self.frontLeftMotor = wpilib.Talon(0)
		self.rearLeftMotor = wpilib.Talon(1)
		self.frontRightMotor = wpilib.Talon(2)
		self.rearRightMotor = wpilib.Talon(3)

		self.sensor_1_mec = wpilib.DigitalInput(9)

		self.frontLeftMotor.setInverted(True)

		self.rearLeftMotor.setInverted(True)


		self.drive = MecanumDrive(self.frontLeftMotor,
										 self.rearLeftMotor,
										 self.frontRightMotor,
										 self.rearRightMotor)


	def teleopPeriodic(self):
		"""This function is called periodically during operator control."""

		read_input_mecanum()
		x = state["mov_x"]
		y = state["mov_y"]
		z = state["mov_z"]

		

		if state["button_x_active"]:
			if self.sensor_1.get():
				self.drive.driveCartesian(0, 0, 0, 0)
			else:
				self.drive.driveCartesian(0, -1, 0, 0)

		else:
			self.drive.driveCartesian(x, y, z, 0)


		read_input_cargo()
		if state["cargo"]:
			self.cargo_motor.set(1)
		else:
			self.cargo_motor.set(0)

		read_input_lift()
		if state["lift"]:
			state["timer_lift"] += 1
			if state["timer_lift"] <= 50:
				self.lift_motor.set(1)
			elif state["timer_lift"] > 50 and state["timer_lift"] < 100:
				self.lift_motor.set(0)
				self.cargo_motor.set(-1)
			elif state["timer_lift"] >= 100:
				self.lift_motor.set(-1)
				self.cargo_motor.set(0)
		else:
			state["timer_lift"] = 0
			self.lift_motor.set(0)
		
		print(state)

		read_input_linefollow()
		if state["button_y_on"]:
			if self.sensor_1_line.get():
				self.drive.arcadeDrive(0.7, 0)
			elif self.sensor_2_line.get(): 
				self.drive.arcadeDrive(0.4, 0)
			elif self.sensor_4_line.get(): 
				self.drive.arcadeDrive(-0.4, 0)
			elif self.sensor_5_line.get(): 
				self.drive.arcadeDrive(0.7, 0)
			elif self.sensor_3_line.get(): 
				self.drive.arcadeDrive(0, 0)
		else:
			self.drive.arcadeDrive(y, x)
		read_input_velcrolastick()
		if state["lift_up"]:
			state["timer"] += 1
			if self.sensor1.get() and self.sensor2.get(): 

				if state["timer"] >=1 and state["timer"] <= 50:

					self.lift_motor1.set(0.5)
					self.lift_motor2.set(0)
					print ("piston_3_0")
					print ("piston_4_0")
					print ("piston_5_0")

				elif state["timer"] >= 50 and state["timer"] <=100:

					print ("piston_3_0.5")
					print ("piston_4_0.5")
					print ("piston_5_0.5")
                    
					self.lift_motor1.set(0)
					self.lift_motor2.set(0)
                     
				elif state["timer"] >= 100 and state["timer"] <=150:
                    
					self.lift_motor2.set(-0.5)
                    
					self.lift_motor1.set(0)
					print ("piston_3_0")
					print ("piston_4_0")
					print ("piston_5_0")
				else:
					self.lift_motor1.set(0)
					self.lift_motor2.set(0)
					print ("piston_3_0")
					print ("piston_4_0")
					print ("piston_5_0")   
			else:
				state["timer"] = 0



print("holaaa")

if __name__ == "__main__":
	wpilib.run(MyRobot)