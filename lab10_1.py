import InputBox
import MessageBox


def addcontact():
    InputBox.ShowDialog("Enter first name: ")
    firstname = InputBox.GetInput()

    InputBox.ShowDialog("Enter last name: ")
    lastname = InputBox.GetInput()

    InputBox.ShowDialog("Enter phone number: ")
    phoneno = InputBox.GetInput()

    InputBox.ShowDialog("Enter email address: ")
    emailaddr = InputBox.GetInput()

    f = open("phonebook.dat", 'a')
    f.write(firstname + ":")
    f.write(lastname + ":")
    f.write(phoneno + ":")
    f.write(emailaddr + "\n")

    f.close()


def showcontact():
    msg = "You have the following records:\n\n"
    f = open("phonebook.dat", 'r')

    msg += f.read()
    f.close()

    return msg


def main():
    ans = 'Y'
    i = 0
    while ans != 'N':
        addcontact()
        InputBox.ShowDialog("Add new contact [Y/N]: ")
        ans = InputBox.GetInput()
        ans = ans.upper()
        i = i + 1

    showcontact()
    s = "You entered " + str(i) + " records."

    MessageBox.Show(s)

if __name__ == "__main__":
    main()
