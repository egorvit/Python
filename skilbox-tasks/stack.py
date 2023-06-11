
class Mystack:

    def __init__(self):
        self.stack = list()

    def add(self, elem):
        self.stack.append(elem)

    def remove(self):
        result = self.stack.pop()
        return result


class TaskManager:

    def __init__(self):
        self.task_manager = dict()

    def add(self, task, priority):
        if priority in self.task_manager.keys():
            self.task_manager[priority].append(task)
        else:
            self.task_manager[priority] = list()
            self.task_manager[priority].append(task)

    def view(self):
        for key in sorted(self.task_manager.keys()):
            print(key, ' ', end='')
            for task in self.task_manager[key]:
                if len(self.task_manager[key]) > 1:
                    print(task, end='; ')
                else:
                    print(task)


test_manager = TaskManager()
test_manager.add('Сделать уборку', 2)
test_manager.add('Заняться учебой', 1)
test_manager.add('отдохнуть', 1)
test_manager.add('сдать ДЗ', 3)
test_manager.view()