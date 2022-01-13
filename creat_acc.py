import re
class CreatAcc:
    nm_atmts = 0

    @classmethod
    def name_input(cls):
        
        name = input('Enter your full name:  ')

        try:
            if re.match('[a-zA-Z]{3,40}', name):
                return name

            else:
                raise ValueError(f'Your input "{name}" is not valied.')

        except ValueError as ve:
            print(ve)
            CreatAcc.nm_atmts += 1
            if CreatAcc.nm_atmts <= 3:
                CreatAcc.name_input()
            else:
                pass
    
    def ph_input(self):
        self.ph_num = input('Enter Phone Number: ')
        try:
            if self.ph_num.isnumeric() and len(self.ph_num) == 10 and self.ph_num[0] not in range(0,):
                return int(self.ph_num)

            else:
                raise ValueError(f"Your entered number '{self.ph_num}' is not valid")
        except ValueError as ve:
            print(ve)
            self.ph_input()



if __name__ == '__main__':
    name = CreatAcc.name_input()
    cre_ac = CreatAcc()
    ph_num = cre_ac.ph_input()