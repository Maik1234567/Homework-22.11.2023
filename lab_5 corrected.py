"""
lab5
"""
class Bug:
    """
    Class for bugs
    """
    def __init__(
        self,
        description="",
        severity=0,
        status="",
        developer="",
    ):
        self.__developer = developer
        self.__description = description
        self.__severity = severity
        self.__deadline = 0
        self.__status = status


    def __str__(self):
        """
        str method
        """
        return (
            f"Description: {self.__description}, "
            f"Severity: {self.__severity}, "
            f"Deadline: {self.__deadline}, Статус: {self.__status}, "
            f"Developer: {self.__developer}"
        )

    def __repr__(self):
        """
        repr
        """
        return f"Bug(\'{self.__description}\', {self.__severity}, \'{self.__status}\',\
\'{self.__developer}\')"

    def __del__(self):
        """
        destructor
        """
        print()

    def get_description(self):
        """
        getter
        """
        return self.__description

    def get_severity(self):
        """
        getter
        """
        return self.__severity

    def get_deadline(self):
        """
        getter
        """
        return self.__deadline

    def get_status(self):
        """
        getter
        """
        return self.__status

    def get_developer(self):
        """
        getter
        """
        return self.__developer

    def set_deadline(self, deadline):
        """
        setter for deadline
        """
        self.__deadline = deadline


class Backlog:
    """
    class for backlog
    """
    def __init__(self):
        self.__bug = []
        self.__developer = ''

    def __del__(self):
        print()

    def __str__(self):
        return f"Developer:{self.__developer}"

    def __repr__(self):
        return f"{self.__developer}"

    def add_bugs(self, *args):
        """
        Add bugs to backlog
        """
        for bugs in args:
            self.__bug.append(bugs)
            print(f"Bug {bugs.get_description()} is added to backlog Backlog. ")

    def sort_by_severity(self) -> list:
        """
        Sort bugs by severity
        """
        sorted_list = self.__bug.copy()
        sorted_list.sort(key = lambda x: x.get_severity(), reverse = True)
        return sorted_list

    def get_resolved_bugs(self, developer=None) -> list:
        """
        Getting bugs with resolved status
        """
        resolved_bugs = []
        for bug in self.__bug:
            if str(bug.get_status()).lower() == "resolved":
                if (developer is None) or (developer == bug.get_developer()):
                    resolved_bugs.append(str(bug))
        return resolved_bugs

    def get_the_hardest_bug(self):
        """
        returns the hardest bug by severity bug bug
        """
        sorted_list = self.__bug.copy()
        sorted_list.sort(key=lambda x: x.get_severity(), reverse=True)
        return sorted_list[0]

    def get_bugs(self) -> list:
        """
        returns the list of the bugs in the current backlog
        """
        return self.__bug


if globals()["__name__"] == "__main__":
    bug_1 = Bug("crash", 5, "Resolved",  "Vasyl")
    bug_2 = Bug("overheating", 4,  "Resolved","Orest")
    bug_3 = Bug("Freeze", 8,  "Not resolved","Oleg")
    bug_4 = Bug("Problem in System32", 9,  "Resolved","Igor")

    back = Backlog()
    back.add_bugs(bug_1, bug_2, bug_3, bug_4)
    print("Sorted by severity: ", back.sort_by_severity())
    for item in back.get_resolved_bugs():
        print(item)
