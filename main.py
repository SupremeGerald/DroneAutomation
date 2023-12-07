"""Python code"""
from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()

if False:
    dataset = "color_data"
    colors = ["green", "purple", "red", "lightblue", "blue", "yellow", "black", "white"]
    for color in colors:
        data = []
        samples = 500
        for i in range(1):
            print("Sample: ", i+1)
            next = input("Press enter to calibrate " + color)
            print("0% ", end="")
            for j in range(samples):
                color_data = drone.get_color_data()[0:9]
                data.append(color_data)
                time.sleep(.05)
                if j % 10 == 0:
                    print("-", end="")
            print(" 100%")
        drone.new_color_data(color, data, dataset)
    print("Done calibrating.")

drone.load_classifier("color_data")
color_data = drone.get_color_data()
color = drone.get_color_data()

while True:
    color = drone.get_color_data()
    pred_color = drone.predict_colors(color_data)
    print(pred_color)
    drone.set_drone_LED(255*eq(pred_color[0], "red"), 255*eq(pred_color[0], "green"), 255*eq(pred_color[0], "blue"), 100)
    time.sleep(.1)

drone.land()
drone.close()





