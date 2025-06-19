class Todolist:
    def __init__(self):
        self.task=[]

    def add_task(self,name):
        self.task.append(name)
        print(f"{name} vazifasi kiritildi")

    def remove_task(self,name):  
        if name in self.task:
            self.task.remove(name)
            print('vazifa ochirildi')      
        else:
            print('vazifa ochirilmadi' )

    def view_task(self):
        for i in self.task:
            print(i)

    def main(self):

        print("1. Vazifa qoshish")
        print("2. Vazifa ochirish")
        print("3. Vazifalarni korish")
        print("4. Chiqish")

        choose = input("Tanlang (1-4): ")

        if choose == "1":
            name = input("Yangi vazifa kiriting: ")
            todolist1.add_task(name)
        elif choose == "2":
            name = input("Ochiriladigan vazifani kiriting: ")
            todolist1.remove_task(name)
        elif choose == "3":
            todolist1.view_task()
        else:
            print("tanlov notogri")
todolist1 = Todolist()
todolist1.main()
