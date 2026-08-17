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
JOYSTICK_DEADBAND = 15
BUTTON_MOTOR_SPEED = 100
LOOP_SLEEP_MSEC = 20
CLAW_MAX_TORQUE_PCT = 5
# Brain should be defined by default
brain=Brain()
right_drive_motor = Motor(Ports.PORT6)
left_drive_motor = Motor(Ports.PORT1)
claw_motor = Motor(Ports.PORT4) 
arm_motor = Motor(Ports.PORT10)

controller = Controller()

def apply_deadband(value):
    if abs(value) < JOYSTICK_DEADBAND:
        return 0 
    else:
        return value

#brain.screen.print("WILLIAM HELLO!")


def main():
    claw_motor .set_stopping(HOLD)
    claw_motor.set_max_torque(CLAW_MAX_TORQUE_PCT, PERCENT)
    while True:
        right_velocity = apply_deadband (controller.axisD.position())
        right_drive_motor.spin(REVERSE, right_velocity, PERCENT)
        left_velocity = apply_deadband (controller.axisA.position())
        left_drive_motor.spin(FORWARD, left_velocity, PERCENT)
       
        right_button_pressed_up = controller.buttonRUp.pressing()
        left_button_pressed_up = controller.buttonLUp.pressing()
        claw_motor.spin(FORWARD, (left_button_pressed_up - right_button_pressed_up)*BUTTON_MOTOR_SPEED,PERCENT)

        right_button_pressed_down = controller.buttonRDown.pressing()
        left_button_pressed_down  = controller.buttonLDown.pressing()
        arm_motor.spin(FORWARD, (right_button_pressed_down - left_button_pressed_down)*BUTTON_MOTOR_SPEED,PERCENT)
        sleep(LOOP_SLEEP_MSEC)
main()