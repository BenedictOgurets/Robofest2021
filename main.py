#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick as brick
from pybricks.ev3devices import (Motor, ColorSensor, UltrasonicSensor)
from pybricks.parameters import Port, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase

# Инициализация моторов
left_motor = Motor(Port.D)      # Левый мотор
right_motor = Motor(Port.A)     # Правый мотор
up_n_down_motor = Motor(Port.C) # Мотор поднимающий и опускающий захват
tube_motor = Motor(Port.B)      # Мотор опускающий и поднимающий трубу
# Инициализация робота
robot = DriveBase(left_motor, right_motor, 69, 127)
# Инициализация датчиков
right_sensor = ColorSensor(Port.S1)
left_sensor = ColorSensor(Port.S4)
sonic_sensor = UltrasonicSensor(Port.S2)
# Подсчёт среднего значения для движения по линии
BLACK = 9
WHITE = 85
threshold = (BLACK + WHITE) / 2
# Скорость робота
DRIVE_SPEED = 100

# Езда по линии
def follow_black_line(s):
    n = 0
    while n != s:
        if right_sensor.color() == Color.WHITE and left_sensor.color() == Color.WHITE:
            robot.drive(100, 0)
        elif right_sensor.color() == Color.WHITE and left_sensor.color() == Color.BLACK:
            robot.drive(100, -50)
        elif right_sensor.color() == Color.BLACK and left_sensor.color() == Color.BLACK:
            robot.drive(100, 0)
            while right_sensor.color() != Color.WHITE or left_sensor.color() != Color.WHITE:
                pass
            n += 1
        elif right_sensor.color() == Color.BLACK and left_sensor.color() == Color.WHITE:
            robot.drive(100, 50)
    robot.stop()

# Сканирование штрих-кода
def barcode():
    pass

# Путь к первой кормушке
def first_feeder():
    pass

# Путь ко второй кормушке
def second_feeder():
    pass

# Путь к третьей кормушке
def third_feeder():
    pass

# Путь к четвётрой кормушке
def fourth_feeder():
    pass


up_n_down_motor.run_time(-700, 2100)
follow_black_line(6)
left_motor.run_time(360, 1000)

