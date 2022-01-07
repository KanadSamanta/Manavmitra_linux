import os, sys, subprocess

'''apps = subprocess.run('for app in /usr/share/applications/*.desktop; do echo "${app:24:-8}"; done', capture_output=True)
print(apps)'''
app_names = []
for app in os.listdir('/usr/share/applications/'):
    if app.endswith(".desktop"):
        app_names.append(app.replace(".desktop", ""))
print(app_names)
if 'pycharm-community-2021.3/' in app_names:
    print("True")