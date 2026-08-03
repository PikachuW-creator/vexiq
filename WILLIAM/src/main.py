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

controller = Controller()
#brain.screen.print("WILLIAM HELLO!")

count = 0
def main():
    while True:
        right_velocity = controller.axisD.position()
        right_drive_motor.spin(REVERSE, right_velocity, PERCENT)
        left_velocity = controller.axisA.position()
        left_drive_motor.spin(FORWARD, left_velocity, PERCENT)

main()