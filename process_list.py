import subprocess


def ongoing_list():
    pl = subprocess.Popen(['ps', '-U', '0'], stdout=subprocess.PIPE).communicate()[0]

    process_name_list = []

    for line in pl.decode().splitlines():

        line1 = line.split(" ")

        for i in line1:
            if "/" in i:
                print(i)
                process_name_list.append(i.split("/")[0])

    print(process_name_list)
    return process_name_list


ongoing_list()
if 'firefox' in ongoing_list():
    print(True)
else:
    print(False)
