from jabutixlib import *

jabutixAPI = JabutiXAPI()

for i in range(0, 3):
    jabutixAPI.MoveForward()

jabutixAPI.MoveLeft()
jabutixAPI.MoveRight()