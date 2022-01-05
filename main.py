import os, sys, shutil, webbrowser, random, requests, time, traceback, string, json

try:
    from newspaper import Article
except ModuleNotFoundError:
    from askpass import AskPass

    with AskPass() as ask:
        for x in ask:
            os.system(
                "echo " + x + " | sudo -S apt-get install python-dev libxml2-dev libxslt-dev  -y")
            os.system(
                "echo " + x + "| curl https://raw.githubusercontent.com/codelucas/newspaper/master/download_corpora"
                              ".py | python3")
            break
    os.system("pip3 install newspaper3k")

    from newspaper import Article
try:
    from lxml import html
except ImportError:
    os.system("pip3 install lxml==4.6.3")

    from lxml import html
try:
    import string
except ImportError:
    os.system("pip3 install string")

    import string
try:
    from bs4 import BeautifulSoup
except ImportError:
    os.system("pip3 install beautifulsoup4")

    from bs4 import BeautifulSoup
try:
    import datefinder
except ImportError:
    os.system("pip3 install datefinder")

    import datefinder
try:
    from fast_youtube_search import search_youtube
except ImportError:
    os.system(
        "pip3 install fast-youtube-search")

    from fast_youtube_search import search_youtube
try:
    import speech_recognition as sr
except ImportError:
    # os.system("conda install -c anaconda cmake -y")

    os.system("pip3 install askpass")
    from askpass import AskPass

    with AskPass() as ask:
        for x in ask:
            os.system(
                "echo " + x + "| sudo -S apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 "
                              "ffmpeg libav-tools -y")
            break

    os.system(
        "pip3 install pyaudio")

    os.system(
        "pip3 install SpeechRecognition")

    import speech_recognition as sr
try:
    import wikipedia
except ImportError:
    os.system(
        "pip3 install wikipedia")

    import wikipedia
try:
    import datetime
except ImportError:
    os.system(
        "pip3 install DateTime")

    import datetime
try:
    import wolframalpha
except ImportError:
    os.system(
        "pip3 install wolframalpha")

    import wolframalpha
try:
    import serial.tools.list_ports
except ImportError:
    os.system(
        "pip3 install pyserial")

    import serial.tools.list_ports
try:
    import geocoder
except ImportError:
    os.system(
        "pip3 install geocoder")

    import geocoder
try:
    import ctypes
except ImportError:
    os.system(
        "pip3 install ctypes")

    import ctypes
try:
    from tqdm import tqdm
except ImportError:
    os.system(
        "pip3 install tqdm")

    from tqdm import tqdm
try:
    import pyttsx3
except ImportError:
    os.system(
        "pip3 install pyttsx3")

    import pyttsx3
try:
    from fuzzywuzzy import fuzz, process
except ImportError:
    os.system(
        "pip3 install python-Levenshtein")

    os.system(
        "pip3 install fuzzywuzzy")

    from fuzzywuzzy import fuzz, process
try:
    import face_recognition
except ImportError:
    # os.system("conda install -c anaconda cmake -y")
    os.system("conda install -c conda-forge dlib -y")

    os.system("pip3 install askpass")
    from askpass import AskPass

    with AskPass() as ask:
        for x in ask:
            os.system(
                "echo " + x + " | sudo -S apt-get install cmake -y")
            break

    os.system(
        "pip3 install face_recognition")

    import face_recognition
try:
    import cv2
except ImportError:
    os.system(
        "pip3 install opencv-python")

    import cv2
try:
    import numpy as np
except ImportError:
    os.system(
        "pip3 install numpy")

    import numpy as np
try:
    import subprocess
except ImportError:
    os.system(
        "pip3 install subprocess")

    import subprocess
try:
    import facebook
except ImportError:
    os.system(
        "pip3 install facebook-sdk")

    import facebook
try:
    from pyfirmata import Arduino, util
except ImportError:
    os.system(
        "pip3 install pyFirmata")

    from pyfirmata import Arduino, util
try:
    from googletrans import Translator
except ImportError:
    os.system(
        "pip3 install selenium")

    os.system(
        "pip3 install googletrans==3.1.0a0")

    from googletrans import Translator
except AttributeError:
    os.system(
        "pip3 install selenium")

    os.system(
        "pip3 install googletrans==3.1.0a0")

    from googletrans import Translator
except Exception:
    pass
from selenium import webdriver

try:
    import pafy
except ImportError:
    os.system(
        "pip3 install youtube_dl")

    os.system(
        "pip3 install pafy")

    import pafy
try:
    import httplib
except ImportError:
    import http.client as httplib
try:
    import argparse
except ImportError:
    os.system(
        "pip3 install argparse")

    import argparse
try:
    from src.stream_analyzer import Stream_Analyzer
except ModuleNotFoundError:
    os.system(
        "pip3 install pygame")

try:
    from gtts import gTTS
except ModuleNotFoundError:
    os.system(
        "pip3 install gTTS")

    from gtts import gTTS
try:
    from playsound import playsound
except ModuleNotFoundError:
    os.system(
        "pip3 install playsound")

    from playsound import playsound
w = ''


def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent / 100)
    height = int(frame.shape[0] * percent / 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)


def checkInternetHttplib(url="www.google.com", timeout=3):
    conn = httplib.HTTPConnection(url, timeout=timeout)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except Exception as e:
        print(e)

        return False


def myCommand():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening...")

            # r.pause_threshold = 0.5
            audio = r.record(source, duration=5)
        try:
            inquest = r.recognize_google(audio)
            print('User: ' + inquest + '\n')

        except sr.UnknownValueError:
            inquest = ''
        return inquest
    except Exception:
        # try:
        print("the internet connection is very slow...system may will crash")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")

            r.pause_threshold = 0.5
            audio = r.record(source, duration=10)
        try:
            inquest = r.recognize_google(audio, language='en-In')
            print('User: ' + inquest + '\n')

        except Exception:
            inquest = ''
        return inquest


def denypower():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")

        # r.pause_threshold = 0.5
        audio = r.record(source, duration=5)
    try:
        sto = r.recognize_google(audio, language='en-IN')
        print('User answer: ' + sto + '\n')

    except sr.UnknownValueError:
        sto = ''

    return sto


def raise_error(error="this Error is manually raised"):
    raise Exception(error)


def error_popup(phrase=traceback.format_exc(), button='ok', instruction=None):
    try:
        popup_to_show = open(os.path.join(sys.path[0], "error_massege.txt"), 'w+')
        popup_to_show.write(phrase)
        popup_to_show.close()
        button_to_show = open(os.path.join(sys.path[0], "error_massege_button.txt"), 'w+')
        button_to_show.write(button)
        button_to_show.close()
        command_to_do = open(os.path.join(sys.path[0], "instruction.txt"), 'w+')
        command_to_do.write(instruction)
        command_to_do.close()
        try:
            subprocess.Popen(os.path.join(sys.path[0], 'popup.py'))
        except PermissionError:
            import popup

    except Exception:
        print(traceback.format_exc())


def speak(audio, vasa='en'):
    print(audio)
    try:
        tts = gTTS(audio)

        tts.save(os.path.join(sys.path[0], 'hello.mp3'))
        playsound(os.path.join(sys.path[0], 'hello.mp3'))
        os.remove(os.path.join(sys.path[0], 'hello.mp3'))
    except Exception:
        try:
            if audio != None:
                engine = pyttsx3.init()
                engine.say(audio)
                engine.runAndWait()
            else:
                pass
        except Exception:
            try:
                from askpass import AskPass

                with AskPass() as ask:
                    for x in ask:
                        os.system(
                            "echo " + x + " | sudo -S apt-get install espeak -y")
                        os.system("pip3 install python-espeak")
                        break
                engine = pyttsx3.init()
                engine.say(audio)
                engine.runAndWait()
            except AttributeError:
                pass


def chatbot(query):
    try:
        client = wolframalpha.Client('U365V3-L38JGHY94J')
        res = client.query(query)
        to_say = next(res.results).text
        if to_say == '(data not available)':
            to_say = google_bot(query)
    except Exception:
        to_say = google_bot(query)
    if to_say != "":
        return to_say
    else:
        return None


def gui(How_many_inputs=3, heading="what?", input_heading1="Q1.", input_heading2="Q2.", input_heading3="Q3.",
        window_heading="window", theme="DarkGreen4"):
    import PySimpleGUI as sg

    # Add some color
    # to the window
    sg.theme(theme)

    # Very basic window.
    # Return values using
    # automatic-numbered keys
    if How_many_inputs == 1:
        layout = [
            [sg.Text(heading)],
            [sg.Text(input_heading1, size=(15, 1)), sg.InputText()],
            [sg.Submit(), sg.Cancel()]
        ]
    elif How_many_inputs == 2:
        layout = [
            [sg.Text(heading)],
            [sg.Text(input_heading1, size=(15, 1)), sg.InputText()],
            [sg.Text(input_heading2, size=(15, 1)), sg.InputText()],
            [sg.Submit(), sg.Cancel()]
        ]
    elif How_many_inputs == 3:
        layout = [
            [sg.Text(heading)],
            [sg.Text(input_heading1, size=(15, 1)), sg.InputText()],
            [sg.Text(input_heading2, size=(15, 1)), sg.InputText()],
            [sg.Text(input_heading3, size=(15, 1)), sg.InputText()],
            [sg.Submit(), sg.Cancel()]
        ]

    window = sg.Window(window_heading, layout)
    event, values = window.read()
    window.close()

    # The input data looks like a simple list
    # when automatic numbered

    return values


def google_bot(query):
    article = Article('https://www.google.com/search?q=' + query.replace(" ", "+"))
    article.download()
    article.parse()
    article.nlp()

    return article.text


from facerecognition import conformation

if conformation:
    speak("Tell me the password!")
    while True:
        passs = False
        conformation_speech = myCommand().lower()
        if 0xFF == ord('q'):
            passs = gui(1, "Type the password", "password:")
            if passs == "wake up":
                passs = True
            else:
                passs = False
        if "wake up" in conformation_speech or "manav" in conformation_speech or passs:
            speak(
                "Hello, I am you digital assistant manavmitra, if you want to ask me anything try calling me 'sonia'.""Tell me how can I help you?")
            while True:

                def myline(vasa='en'):

                    try:
                        r = sr.Recognizer()
                        with sr.Microphone() as source:

                            # r.pause_threshold = 0.5
                            r.adjust_for_ambient_noise(source)
                            print("Listening...(l)")

                            audio = r.listen(source, timeout=27)

                            # print("audio recorded")
                        print("Processing(+_+)")
                        try:

                            inquest1 = r.recognize_google(audio, language=vasa)
                            print('User:' + inquest1 + '\n')

                        except sr.UnknownValueError:
                            inquest1 = ''
                        except Exception:
                            try:
                                inquest1 = r.recognize_sphinx(audio)
                                print('User: ' + inquest1 + '\n')

                            except (sr.UnknownValueError, sr.RequestError):
                                inquest1 = ""
                        return inquest1
                    except Exception:
                        try:
                            speak("the internet connection is very slow...system may will crash")
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                r.adjust_for_ambient_noise(source)
                                print("Listening...(SL)")

                                # r.pause_threshold = 0.5
                                audio = r.listen(source, timeout=30)
                            try:
                                inquest1 = r.recognize_google(audio, language='en-IN')
                                print('User: ' + inquest1 + '\n')

                            except Exception:
                                try:
                                    inquest1 = r.recognize_sphinx(audio)
                                    print('User: ' + inquest1 + '\n')

                                except (sr.UnknownValueError, sr.RequestError):
                                    inquest1 = ""

                            return inquest1
                        except Exception:

                            speak(
                                "internet connection is lost! waiting to e online,"
                            )

                            while True:
                                if checkInternetHttplib():
                                    break

                            pass


                inquest = myline().lower()

                if inquest != "" and 'sonia' in inquest:
                    inquest = inquest.replace("sonia", "")
                    if 'search ' in inquest or 'open ' in inquest or 'start ' in inquest:
                        try:
                            if 'search' not in inquest:
                                app_name = inquest.replace("open", "").replace("start", "")
                                with open(os.path.join(sys.path[0], "app name.txt"), 'w+') as write_app:
                                    write_app.write(app_name)
                                    write_app.close()
                                os.system("python3 " + os.path.join(sys.path[0], "select_app.py"))
                                with open(os.path.join(sys.path[0], "app_name.txt"), "r") as read_app_name:
                                    result_app = read_app_name.read()
                                    read_app_name.close()
                                speak("is " + str(result_app) + " you, want to open?")
                                yes_no = denypower()
                                if 'no' in yes_no or 'na' in yes_no or "don't" in yes_no:
                                    speak("ok!")
                                    continue
                                else:
                                    '''app_start = subprocess.run([str(result_app)], capture_output=True)
                                    if app_start.returncode != 0:
                                        error_popup(app_start.stderr)
                                        speak("I tried but couldn't do it. Please open manually. Here are some "
                                              "internet info!")
                                        raise_error()
                                    else:
                                        pass'''
                                    try:
                                        os.system('nohup python3 ' + os.path.join(sys.path[0], 'start_app.py') + ' &')
                                    except FileNotFoundError:
                                        os.system("nohup " + str(result_app) + " &")

                                    continue
                            else:
                                raise_error(traceback.format_exc())
                        except Exception:
                            webbrowser.open(
                                "https://www.google.com/search?q=" + inquest.replace("search", "").replace(" ", "+"))
                    elif "close " in inquest or "stop " in inquest:

                        if 'video' in inquest or 'song' in inquest or 'play' in inquest or 'music' in inquest:
                            if x != '' or x is not None:
                                with AskPass() as ask:
                                    for x in ask:
                                        os.system(
                                            "echo " + x + "| sudo kill " + open(os.path.join(sys.path[0], "PID.txt"),
                                                                                "r").read())
                            else:
                                os.system(
                                    "echo " + x + "| sudo kill " + open(os.path.join(sys.path[0], "PID.txt"),
                                                                        "r").read())
                            speak('play down!')
                        else:
                            try:
                                from process_list import ongoing_list

                                success = os.system("pkill " +
                                                    process.extractOne(
                                                        inquest.replace("close", "").replace("stop", "").replace(" ",
                                                                                                                 ""),
                                                        ongoing_list())[0])
                                if success != 0:
                                    with open(os.path.join(sys.path[0], "app name.txt"), 'w+') as write_app:
                                        write_app.write(
                                            inquest.replace("close", "").replace("stop", "").replace(" ", ""))
                                        write_app.close()
                                    os.system("python3 " + os.path.join(sys.path[0], "select_app.py"))
                                    with open(os.path.join(sys.path[0], "app_name.txt"), "r") as read_app_name:
                                        result_app = read_app_name.read()
                                        read_app_name.close()
                                    speak("is " + str(result_app) + " you, want to close?")
                                    yes_no = denypower()
                                    if 'no' in yes_no or 'na' in yes_no or "don't" in yes_no:
                                        speak("ok!")
                                        pass
                                    else:
                                        for pid in subprocess.run(['pidof', str(result_app)],
                                                                  capture_output=True).stdout.decode().split():
                                            kill_point = os.system("kill -9 " + pid)
                                            if kill_point != 0:
                                                raise_error()
                                                break
                                            else:
                                                continue
                                        speak("done!")
                                        continue




                            except Exception:

                                speak("I tried but couldn't do it. Please close manually. ")

                    elif 'silence' in inquest or 'shut up' in inquest:
                        speak("okey!")
                        break
                    elif 'system' in inquest:

                        if 'shutdown' in inquest:
                            with AskPass() as ask:
                                for x in ask:
                                    os.system(
                                        "echo " + x + "| sudo shutdown -n")
                            speak('shutdown incited!')
                        elif 'reboot' in inquest:
                            with AskPass() as ask:
                                for x in ask:
                                    os.system(
                                        "echo " + x + "| sudo reboot")
                                speak('rebooting! ')
                        elif 'log ' in inquest and ' out' in inquest:
                            with AskPass() as ask:
                                for x in ask:
                                    os.system(
                                        "/usr/bin/gnome-session-quit --no-prompt")
                                    speak("Ready to log out!")
                        else:
                            pass
                    elif 'play' in inquest:
                        with open(os.path.join(sys.path[0], "inquest_youtube.txt"), "w+") as youtube_inquest:
                            youtube_inquest.write(inquest)
                            youtube_inquest.close()
                        os.system("nohup python3 " + os.path.join(sys.path[0], "Youtube_video_play.py") + " &")
                    speak(chatbot(inquest))
