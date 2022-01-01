import cv2
import os
import sys
from time import sleep

key = cv2.waitKey(1)
webcam = cv2.VideoCapture(0)
sleep(2)
while True:

    try:
        check, frame = webcam.read()
        print(check)  # prints true as long as the webcam is running
        print(frame)  # prints matrix values of each framecd
        cv2.imshow("to save your pic press 's' key, to quit press 'q'", frame)
        key = cv2.waitKey(1)
        if key == ord('s'):
            cv2.imwrite(filename=os.path.join(sys.path[0], "user_pic.jpg"), img=frame)
            webcam.release()
            print("Processing image...")
            img_ = cv2.imread(os.path.join(sys.path[0], "user_pic.jpg"), cv2.IMREAD_ANYCOLOR)
            # print("Converting RGB image to grayscale...")
            # gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            # print("Converted RGB image to grayscale...")
            # print("Resizing image to 28x28 scale...")
            # img_ = cv2.resize(gray,(28,28))
            # print("Resized...")
            img_resized = cv2.imwrite(filename=os.path.join(sys.path[0], "user_pic.jpg"), img=img_)
            print("Image saved!")

            break

        elif key == ord('q'):
            webcam.release()
            cv2.destroyAllWindows()
            break

    except KeyboardInterrupt:
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break
try:
    import PySimpleGUI as sg
except ImportError:
    from askpass import AskPass

    with AskPass() as ask:
        for x in ask:
            os.system(
                "echo " + x + " | sudo -S apt-get install python3-tk  -y")

            break
    os.system("pip3 install PySimpleGUI")
    import PySimpleGUI as sg
sg.theme('DarkAmber')
layout = [[sg.Text('Type your name here.')],
                 [sg.InputText()],
                 [sg.Submit(), sg.Cancel()]]

window = sg.Window('What is Your name?', layout)

event, values = window.read()
window.close()

text_input = values[0]
sg.popup('Your name is', text_input)
print(text_input)
username = open(os.path.join(sys.path[0], "username.txt"), 'w+')
username.write(text_input)
username.close()
