# Импорт модулей
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Инициализация моторов
left_motor = Motor(Port.D)     # Левый мотор
right_motor = Motor(Port.A)    # Правый мотор
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
def follow_black_line():
    while True:
        if right_sensor.reflection() > threshold:
            if left_sensor.reflection() > threshold:
                robot.drive(100, 0)
            else:
                robot.drive(100, 10)
        else:
            if left_sensor.reflection() <= threshold:
                robot.stop()
            else:
                robot.drive(100, -10)