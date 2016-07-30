import os
import os.path
import time
import InputBox
import MessageBox

files = []


def filterdir(dir):
    for item in os.listdir(dir):
        if os.path.isfile(dir + "\\" + item):
            files.append(item)


def showdatetime(dt):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(dt))


def showfileinfo(p):
    tc = showdatetime(os.path.getctime(p))
    la = showdatetime(os.path.getatime(p))
    lm = showdatetime(os.path.getmtime(p))
    result = os.path.basename(p) + "\t" + str(tc) + "\t"
    result = result + str(la) + "\t"
    result = result + str(lm) + "\t"
    result = result + str(os.path.getsize(p)) + "\n"
    return result


def getreport(dir):
    f = open('fileinfo.dat', 'w+')

    f.write("File Name\tTime Created\tLast Access\tLast Modified\tFile Size\n")
    for item in files:
        s = showfileinfo(dir + "\\" + item)
        f.write(s)
    f.close()


def main():
    InputBox.ShowDialog("Enter a path to a directory: ")
    dir = InputBox.GetInput()
    filterdir(dir)
    getreport(dir)
    f = open('fileinfo.dat', 'r')
    result = f.read() + "\n\n\n"
    MessageBox.Show(result)
    f.close()

if __name__ == "__main__":
    main()
