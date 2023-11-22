class Bug:
    def __init__(self, description = '', severity = 0, deadline = 0, status = '', assignee = True, developer = ''):
        self.__developer = developer
        self.__description = description
        self.__severity = severity
        self.__deadline = deadline
        self.__status = status
        self.__assignee = assignee

    def __str__(self):

            return f'Опис: {self.__description}, Тяжкість: {self.__severity}, Дедлайн: {self.__deadline}, Статус: {self.__status}, developer: {self.__developer}'
    def __repr__(self):

            return f'{self.__description}, {self.__severity},  {self.__deadline}, {self.__status}'
    def __del__(self):
        print()

    def get_description(self):
        return self.__description

    def get_severity(self):
        return self.__severity

    def get_deadline(self):
        return self.__deadline

    def get_status(self):
        return self.__status

    def get_developer(self):
        return self.__developer
class Backlog:
    def __init__(self):
        self.__bug = list()

    def __del__(self):
        print()

    def __str__(self):
        return f'Developer:{self.__developer}'

    def add_bugs(self, *args):
        for bugs in args:
            self.__bug.append(bugs)
            print(f"Баг {bugs.get_description()} додано у Backlog. ")

    def sort_by_severity(self):
        sorted_list = self.__bug.copy()
        sorted_list.sort(key=lambda x: x.get_severity(), reverse=True)
        return sorted_list

    def get_resolved_bugs(self, developer = None):
        resolved_bugs = []
        for bug in self.__bug:
            if(str(bug.get_status()).lower() == 'resolved'):
                if(developer == None) or (developer == bug.get_developer()):
                    resolved_bugs.append(str(bug))
        return resolved_bugs

if globals()['__name__'] == '__main__':
    bug_1 = Bug('crash', 5, 20.11, 'Resolved', True, 'Vasyl' )
    bug_2 = Bug('overheating', 4, 10.11, 'Resolved', True, 'Orest')
    bug_3 = Bug('Freeze', 8, 31.11, 'Not resolved', False, 'Oleg')
    bug_4 = Bug('Problem in System32', 9, 01.12, 'Resolved', True, 'Igor')
    print(bug_1.__str__(),'\n', bug_2.__str__(),'\n', bug_3.__str__(),'\n' ,bug_4.__str__(),'\n')


back = Backlog()
back.add_bugs(bug_1, bug_2, bug_3, bug_4)
print('Sorted by severity: ',back.sort_by_severity())
for item in back.get_resolved_bugs():
        print(item)











