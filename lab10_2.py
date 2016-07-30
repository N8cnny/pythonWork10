import InputBox
import MessageBox


def searchareacode(ac):
    f = open("areacode.txt", 'r')
    arealist = f.readlines()
    rs = 'No matched area code!\n'
    for line in arealist:
        s = line.split('-')
        if s[0] == ac:
            rs = ac + ": " + s[1]
            break
    return rs


def main():
    ans = "y"
    result = "Search Result:\n"
    while ans.upper() != 'N':
        InputBox.ShowDialog("Enter a area code: ")
        ac = InputBox.GetInput()

        result += searchareacode(ac)

        InputBox.ShowDialog("Search again [Y/N]? ")
        ans = InputBox.GetInput()

    MessageBox.Show(result)

if __name__ == "__main__":
    main()

