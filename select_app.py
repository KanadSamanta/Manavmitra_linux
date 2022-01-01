import os
import subprocess as sp
import sys
import traceback

'''
Pipe to file in terminal:
 
$ flatpak list --app --show-details > ~/Documents/installed-flatpack.log
$ dpkg --get-selections > ~/Documents/installed-software.log
 
Not using Debian? Here's some others, including BSD Unix.
$ rpm -qa
$ yum list installed
$ pacman -Qi
$ pkg_version | less
 
Why Python when you have pipes, greps, and such?
Why not?
'''


def error_popup(phrase=traceback.format_exc(), button='ok', instruction=""):
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
            sp.Popen(os.path.join(sys.path[0], 'popup.py'))
        except PermissionError:
            import popup
            print("done")
    except Exception:
        pass


def get_flatpak():
    try:
        cmd = ['/usr/bin/flatpak', 'list', '--app', '--show-details']
        process = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode().replace('\t', ' ').split('\n')
    except FileNotFoundError:
        pass


def get_apt():
    cmd = ['/usr/bin/dpkg', '--get-selections']
    process = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode().replace('\t', ' ').split('\n')


if __name__ == "__main__":

    names_only = []
    flatpak = True
    apt = True
    with open(os.path.join(sys.path[0], "app name.txt"), 'r') as read_app:
        search_string = read_app.read()
        read_app.close()

    if search_string != '':
        try:
            if flatpak:
                pkgs = get_flatpak()
                for pkg in pkgs:
                    if ' ' in pkg:
                        names_only.append(pkg.split()[0])
        except FileNotFoundError:

            pass
        except TypeError:
            names_only.clear()
            pass
        finally:
            if apt:
                pkgs = get_apt()
                for pkg in pkgs:
                    if ' ' in pkg:
                        names_only.append(pkg.replace('install', '').replace(" ", ""))

        print(names_only)

        '''result_apps = []
        for app in names_only:
            if search_string:
                if search_string not in app.lower():
                    continue
            result_apps.append(app)
    print(result_apps)'''
        try:
            from fuzzywuzzy import process
        except ModuleNotFoundError:
            os.system('pip3 install fuzzywuzzy')
            from fuzzywuzzy import process

        result_app = process.extractOne(search_string, names_only)[0]
        with open(os.path.join(sys.path[0], "app_name.txt"), "w+") as app_name:
            app_name.write(result_app)
            app_name.close()
        print(result_app)
    else:

        error_popup("There is no app listed!")
