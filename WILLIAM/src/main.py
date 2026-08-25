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
CLAW_MAX_TORQUE_PCT = 25
FRONT_STOP_DISTANCE_MM = 80
SENSOR_WARMUP_MSEC = 1000
TOUCHLED_BRIGHTNESS = 120
OPTICAL_LIGHT_POWER_PCT = 70

# Brain should be defined by default
brain=Brain()
controller = Controller()

front_distant_sensor = Distance(Ports.PORT5)
front_optical_sensor = Optical(Ports.PORT2)
rear_bumper_switch = Bumper(Ports.PORT9)
side_touch_led = Touchled(Ports.PORT12)

right_drive_motor = Motor(Ports.PORT6)
left_drive_motor = Motor(Ports.PORT1)
claw_motor = Motor(Ports.PORT4) 
arm_motor = Motor(Ports.PORT10)

def is_front_blocked():
    front_near_by_distance = front_distant_sensor.is_object_detected() and front_distant_sensor.object_distance(MM) < FRONT_STOP_DISTANCE_MM
    front_near_by_optical = front_optical_sensor.is_near_object()
    return front_near_by_distance or front_near_by_optical

def update_side_touchled():
    if is_front_blocked() or rear_bumper_switch.pressing():
        side_touch_led.on(Color.RED)
    else:
        side_touch_led.on(Color.GREEN)

def limit_backward_velocity(velocity):
    if velocity < 0 and rear_bumper_switch.pressing():
        return 0
    else:
        return velocity

def limit_forward_velocity(velocity):
    if velocity < 0 and rear_bumper_switch.pressing():
        return 0
    else:
        return velocity
    
def apply_deadband(value):
    if abs(value) < JOYSTICK_DEADBAND:
        return 0 
    else:
        return value

#brain.screen.print("WILLIAM HELLO!")


def main():
    arm_motor.set_stopping(HOLD)
    arm_motor.set_max_torque(CLAW_MAX_TORQUE_PCT, PERCENT)

    front_optical_sensor.set_light_power(OPTICAL_LIGHT_POWER_PCT, PERCENT)
    side_touch_led.set_brightness(TOUCHLED_BRIGHTNESS)
    sleep(SENSOR_WARMUP_MSEC)

    while True:
        right_velocity = apply_deadband(controller.axisD.position())
        right_velocity = limit_forward_velocity(right_velocity)
        right_velocity = limit_backward_velocity(right_velocity)
        right_drive_motor.spin(REVERSE, right_velocity, PERCENT)

        left_velocity = apply_deadband(controller.axisA.position())
        left_velocity = limit_forward_velocity(left_velocity)
        left_velocity = limit_backward_velocity(left_velocity)
        left_drive_motor.spin(FORWARD, left_velocity, PERCENT)
       
        right_button_pressed_up = controller.buttonRUp.pressing()
        left_button_pressed_up = controller.buttonLUp.pressing()
        claw_motor.spin(FORWARD, (left_button_pressed_up - right_button_pressed_up) * BUTTON_MOTOR_SPEED,PERCENT)

        right_button_pressed_down = controller.buttonRDown.pressing()
        left_button_pressed_down  = controller.buttonLDown.pressing()
        arm_motor.spin(FORWARD, (right_button_pressed_down - left_button_pressed_down) * BUTTON_MOTOR_SPEED,PERCENT)

        update_side_touchled()

        sleep(LOOP_SLEEP_MSEC)
main()