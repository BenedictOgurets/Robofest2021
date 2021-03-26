#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


def line():
    if dcl.color() == Color.BLACK and dcp.color() == Color.WHITE:
        robot.drive_time(0, -7, 1000)
    elif dcp.color() == Color.BLACK and dcl.color() == Color.WHITE:
        robot.drive_time(0, 7, 1000)


def sh_code():
    global skr
    global skk
    for i in range(4):
        n1 = ''
        n2 = ''
        for j in range(2):
            cl = dcl.color()
            cp = dcp.color()

            if cl == Color.BLACK:
                n1 = '1' + n1
            else:
                n1 = '0' + n1

            if cp == Color.BLACK:
                n2 = '1' + n2
            else:
                n2 = '0' + n2
            robot.drive_time(50, 0, 360)

        if n1 == '00':
            n1 = '1'
        elif n1 == '01':
            n1 = '2'
        elif n1 == '10':
            n1 = '3'
        elif n1 == '11':
            n1 = '4'

        if n2 == '00':
            n2 = '2'
        elif n2 == '01':
            n2 = '4'
        elif n2 == '10':
            n2 = '6'
        elif n2 == '11':
            n2 = '8'

        skr.append(n1)
        skk.append(n2)


def shr_hr():
    # global skk
    # global i
    robot.drive_time(50, 0, 100)
    for j in range(2):
        for x in range(3):
            mb.track_target(-360)
            wait(1300)
            mb.stop()
            wait(300)
        for y in range(2):
            mb.track_target(360)
            wait(1300)
            mb.stop()
            wait(300)
        robot.drive_time(-40, 0, 1140)
        if j == 1:
            robot.drive_time(-50, 0, 300)
            robot.drive(60, 0)
            while not (dcl.color() == Color.BLACK and dcp.color() == Color.BLACK):
                wait(10)
        wait(1000)


def nch_hr():
    for j in range(6):
        robot.drive(200, 0)
        while not (dcl.color() == Color.BLACK and dcp.color() == Color.BLACK):
            wait(10)
        line()
        robot.drive_time(200, 0, 200)
        line()


def hr_k3():
    robot.drive(200, 0)
    while not (dcl.color() == Color.BLACK and dcp.color() == Color.BLACK):
        wait(10)
    line()
    robot.drive_time(200, 0, 200)
    line()
    robot.drive_time(0, -100, 810)
    line()
    robot.drive(200, 0)
    while not (dcl.color() == Color.BLACK and dcp.color() == Color.BLACK):
        wait(10)
    robot.stop()
    wait(500)
    line()


def hr_k4():
    for j in range(3):
        robot.drive(200, 0)
        while not (dcl.color() == Color.BLACK and dcp.color() == Color.BLACK):
            wait(10)
        line()
        robot.drive_time(200, 0, 200)
        line()
    wait(500)
    robot.drive_time(0, -100, 810)
    line()
    robot.drive(200, 0)
    while not (dcl.color() == Color.BLACK and dcp.color() == Color.BLACK):
        wait(10)
    robot.stop()
    line()


def k3_hr():
    robot.drive(200, 0)
    while not (dcl.color() == Color.BLACK and dcp.color() == Color.BLACK):
        wait(10)
    line()
    robot.drive_time(200, 0, 200)
    line()
    robot.drive_time(0, 100, 820)
    line()
    robot.drive(200, 0)
    while not (dcl.color() == Color.BLACK and dcp.color() == Color.BLACK):
        wait(10)
    line()
    robot.drive_time(200, 0, 200)
    line()


def k4_hr():
    robot.drive(200, 0)
    while not (dcl.color() == Color.BLACK and dcp.color() == Color.BLACK):
        wait(10)
    line()
    robot.drive_time(200, 0, 200)
    line()
    wait(500)
    robot.drive_time(0, 100, 835)
    wait(500)
    line()
    for j in range(3):
        robot.drive(200, 0)
        while not (dcl.color() == Color.BLACK and dcp.color() == Color.BLACK):
            wait(10)
        line()
        robot.drive_time(200, 0, 200)
        line()


dcl = ColorSensor(Port.S4)
dcp = ColorSensor(Port.S1)
dr = UltrasonicSensor(Port.S2)
lev_kol = Motor(Port.D)
pr_kol = Motor(Port.A)
mb = Motor(Port.B)
mc = Motor(Port.C)

robot = DriveBase(lev_kol, pr_kol, 69, 127)

skr = list()
skk = list()

for i in range(3):
    robot.drive(100, 0)
    while not (dcl.color() == Color.BLACK and dcp.color() == Color.BLACK):
        wait(10)
    robot.drive_time(50, 0, 330)
    if i == 0:
        mc.run_time(-700, 2100)
sh_code()
# robot.drive_time(150, 0, 870)
nch_hr()
for j in range(2):
    mb.track_target(360)
    wait(1300)
    mb.stop()
    wait(300)
# mc.run_time(-300, 1000)
for i in range(2):
    robot.drive(100, 0)
    while dr.distance() > 45:
        wait(10)
    robot.stop()
    line()
    robot.drive_time(0, 100, 835)
    # mc.run_time(300, 1000)
    if i == 0:
        mc.run_time(700, 2100)
    else:
        mc.run_time(300, 1000)
        mc.run_time(400, 3000)
    shr_hr()
    robot.drive_time(60, 0, 10)
    mc.run_time(-300, 1000)
    robot.drive_time(0, 100, 830)
    line()
    robot.drive_time(50, 0, 50)
    line()
    if skr[i] == '3':
        hr_k3()
    elif skr[i] == '4':
        hr_k4()
    wait(500)
    line()
    robot.drive_time(40, 0, 1130)
    line()
    robot.drive_time(0, -100, 810)
    robot.drive_time(-40, 0, 1000)
    mc.run_time(-600, 2200)
    robot.drive_time(40, 0, 1010)
    robot.drive_time(0, -100, 790)
    line()
    robot.drive_time(40, 0, 1130)
    line()
    if skr[i] == '3':
        k3_hr()
    elif skr[i] == '4':
        k4_hr()