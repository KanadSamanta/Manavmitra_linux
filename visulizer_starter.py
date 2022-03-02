import os, sys

x = None
try:
    from askpass import AskPass
except ModuleNotFoundError:
    os.system("pip install askpass")
    from askpass import AskPass
if os.system("nohup xterm vis") == 0:
    pass
else:
    if x is None:
        with AskPass() as ask:
            for x in ask:
                os.system(
                    "echo " + x + "|sudo add-apt-repository ppa:ubuntu-toolchain-r/test; sudo apt-get update; sudo "
                                  "apt-get install "
                                  "gcc-4.9 "
                                  "g++-4.9 -y; sudo apt install libfftw3-dev libncursesw5-dev cmake libpulse-dev -y")
                if os.system(
                        "echo " + x + "|git clone https://github.com/dpayne/cli-visualizer.git; cd cli-visualizer; "
                                      "sudo "
                                      "./install.sh") == 0:
                    os.system("xterm vis")
                    break
    else:
        os.system(
            "echo " + x + "|sudo add-apt-repository ppa:ubuntu-toolchain-r/test; sudo apt-get update; sudo apt-get "
                          "install "
                          "gcc-4.9 "
                          "g++-4.9 -y; sudo apt install libfftw3-dev libncursesw5-dev cmake libpulse-dev -y")
        if os.system(
                "echo " + x + "|git clone https://github.com/dpayne/cli-visualizer.git; cd cli-visualizer; sudo "
                              "./install.sh") == 0:
            os.system("xterm vis")
        else:
            with AskPass() as ask:
                for x in ask:
                    os.system(
                        "echo " + x + "|sudo add-apt-repository ppa:ubuntu-toolchain-r/test; sudo apt-get update; "
                                      "sudo apt-get install "
                                      "gcc-4.9 "
                                      "g++-4.9 -y; sudo apt install libfftw3-dev libncursesw5-dev cmake libpulse-dev -y")
                    if os.system(
                            "echo " + x + "|git clone https://github.com/dpayne/cli-visualizer.git; cd "
                                          "cli-visualizer; sudo "
                                          "./install.sh") == 0:
                        os.system("xterm vis")
                        break
