class Email_validation:
    count = 0

    @classmethod
    def valid(cls):
        mail = input("Enter your mail id: ")

        if mail[-10:] == "@gmail.com" and "." not in list(mail[0:-10]) and "@" not in list(mail[0:-10]):
            return mail

        else:
            Email_validation.count += 1

            print(mail,"is not a valid mail id")
            if Email_validation.count <= 3:
                Email_validation.valid()
                
            else:
                print("Reached the number of attemts")
                breakpoint
            


if __name__ == '__main__':
    mail = Email_validation.valid()

        

