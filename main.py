from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()

#     # calibration
# dataset = "color_data"
# colors = ["green", "purple", "red", "lightblue", "blue", "yellow", "black", "white"]
# for color in colors:
#     data = []
#     samples = 500
#     for i in range(1):
#         print("Sample: ", i+1)
#         next = input("Press enter to calibrate " + color)
#         print("0% ", end="")
#         for j in range(samples):
#             color_data = drone.get_color_data()[0:9]
#             data.append(color_data)
#             sleep(.05)
#             if j % 10 == 0:
#                 print("-", end="")
#         print(" 100%")
#     drone.new_color_data(color, data, dataset)
drone.load_classifier("color_data")
# print("Done calibrating.")

    # button interrupts loop
# button_pressed = False
# while not(button_pressed):
#     button_pressed = drone.l1_pressed()
# print("pressed")

    # get color and set
# color_d = drone.get_color_data()
# pred_color = drone.predict_colors(color_d)
    # deprecated solution
# drone.set_drone_LED(
#     255*eq(pred_color[0], "red"),
#     255*eq(pred_color[0], "green"),
#     255*eq(pred_color[0], "blue"), 100)

def color_sense():
    color_d1 = drone.get_color_data()
    pred_color = drone.predict_colors(color_d1)
    strong_color = pred_color[0]
    print(strong_color)
    if strong_color == "red":
        drone.set_drone_LED(255,0,0,100)
    elif strong_color == "blue":
        drone.set_drone_LED(0,0,255,100)
    elif strong_color == "green":
        drone.set_drone_LED(0,255,0,100)
    elif strong_color == "light_blue":
        drone.set_drone_LED(0,255,255,100)
    elif strong_color == "purple":
        drone.set_drone_LED(255,0,255,100)
    elif strong_color == "yellow":
        drone.set_drone_LED(255,255,0,100)
    elif strong_color == "white":
        drone.set_drone_LED(255,255,255,100)
    elif strong_color == "black":
        drone.set_drone_LED(0,0,0,100)

while True:
    color_sense()
    sleep(.05)

# red = (255, 0, 0)
# blue = (0, 0, 255)
# green = (0, 255, 0)
# light_blue = (0, 255, 255)
# purple = (255, 0, 255)
# yellow = (255, 255, 0)
# white = (255, 255, 255)
# black = (0, 0, 0)