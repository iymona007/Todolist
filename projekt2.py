class Todolist:
    def __init__(self):
        self.task = []

    def add_task(self, name):
        self.task.append(name)
        print(f"{name} vazifasi kiritildi.")

    def remove_task(self, name):
        if name in self.task:
            self.task.remove(name)
            print("Vazifa o‘chirildi.")
        else:
            print("Bunday vazifa topilmadi.")

    def view_task(self):
        if not self.task:
            print("Hech qanday vazifa yo‘q.")
        else:
            print("Vazifalar ro‘yxati:")
            for i, task in enumerate(self.task, 1):
                print(f"{i}. {task}")

    def main(self):
        while True:
            print("\n--- VAZIFALAR MENYUSI ---")
            print("1. Vazifa qo‘shish")
            print("2. Vazifa o‘chirish")
            print("3. Vazifalarni ko‘rish")
            print("4. Chiqish")

            choose = input("Tanlang (1-4): ")

            if choose == "1":
                name = input("Yangi vazifani kiriting: ")
                self.add_task(name)
            elif choose == "2":
                name = input("Ochiriladigan vazifani kiriting: ")
                self.remove_task(name)
            elif choose == "3":
                self.view_task()
            elif choose == "4":
                print("Chiqildi.")
                break
            else:
                print("Tanlov notogri. Iltimos, 1-4 orasida son kiriting.")

# Dasturni ishga tushirish
todolist1 = Todolist()
todolist1.main()
