# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       영재정보교육                                                       #
# 	Created:      7/27/2026, 2:17:15 PM                                        #
# 	Description:  IQ2 project                                                  #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()
right_drive_motor = Motor(Ports.PORT6)
left_drive_motor = Motor(Ports.PORT1)
claw_motor = Motor(Ports.PORT4) 

controller = Controller()

def apply_deadband(value):
    if abs(value) < 15:
        return 0 
    else:
        return value

#brain.screen.print("WILLIAM HELLO!")


def main():
    while True:
        right_velocity = apply_deadband (controller.axisD.position())
        right_drive_motor.spin(REVERSE, right_velocity, PERCENT)
        left_velocity = apply_deadband (controller.axisA.position())
        left_drive_motor.spin(FORWARD, left_velocity, PERCENT)

        right_button_pressed_up = controller.buttonRUp.pressing()
        left_button_pressed_up = controller.buttonLUp.pressing()
        claw_motor.spin(FORWARD, (right_button_pressed_up - left_button_pressed_up)*50,PERCENT)
main()