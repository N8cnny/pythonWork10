import urllib
import urllib.request
import InputBox
import MessageBox


def searchfile(filename, keyword):
    f = open(filename, 'r')
    n = 0
    for line in f:
        if line.count(keyword) > 0:
            n = n + line.count(keyword)

    f.close()
    MessageBox.Show("The word \'" + keyword + "\' appears " + str(n) + " time(s) in the webpage.")


def main():
    InputBox.ShowDialog("Enter the URL: ")
    url = InputBox.GetInput()

    wp = urllib.request.urlopen(url)
    webcontent = wp.read()

    webcontent = str(webcontent)

    f = open("webpage.html", 'w')
    f.write(webcontent)
    f.close()

    InputBox.ShowDialog("Enter a keyword: ")
    keyword = InputBox.GetInput()

    searchfile("webpage.html", keyword)

if __name__ == "__main__":
    main()
