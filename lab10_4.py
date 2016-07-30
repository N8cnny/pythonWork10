import os
import MessageBox

def outputhtml():
    html = "<!Doctype html><html>"
    if os.name == "nt":
        html += "<body bgcolor = 'pink'>"
        html += "Windows OS<br />"

        sysdrive = os.getenv("Systemdrive")
        dirlist = os.listdir(sysdrive + "\\")
    elif os.name == "posix":
        html += "<body bgcolor = 'yellow'>"
        html += "Unix/Linux OS<br />"
        dirlist = os.listdir("~")

    elif os.name == "mac":
        html += "<body bgcolor = 'menu'>"
        html += "Mac/Apple OS<br />"
        dirlist = os.listdir("::")

    else:
        html += "<body bgcolor = 'orange'>"
        html += "Unknown OS<br />"
        dirlist = os.listdir("")
    html += "Found the following files and directories:<ul>"
    for i in dirlist:
        html += "<li><a href=\'"+ i + "\'>" + i + "</a><br>"
    html += "</ul>"
    html += "</body></html>"
    return html


def main():
    f = open('myos.html', 'w')
    f.write(outputhtml())
    f.close()
    MessageBox.Show("Check the 'myos.html' file")

if __name__ == "__main__":
    main()
