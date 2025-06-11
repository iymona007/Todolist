class BudgetTracker:
    def __init__(self):
        self.daromat=[]

    def add_income(self,miqdori,malumot):
        self.daromat.append({'miqdori': miqdori,'malomoti': malumot})
        print(f"{miqdori} daromat qoshildi")

    def add_expense(self, miqdor, category, malumot):
        self.daromat.append({'miqdor' : miqdor,'category':category,'malumot':malumot})
        print(f"{miqdor}ming xarajat {category}ga qoshildi.")

    def view_transaction(self):
        if not self.daromat:
            print('hech qanday malumot yoq')

        for i in self.daromat:
            if 'category' in i:
                print(f"xarajat-{i['miqdori']}- {i['category']}-{i['malumot']}")
            else:
                print(f"daromat" - {i['miqdori']}-{i['malumoti']})

    def get_balance(self):
        for i in self.daromat:
            if 'category'in i:
                expense=sum(i['miqdori'])
                print(expense)
            else:
                income=sum (i['miqdori'])
                print(income)

def main():
    budget=BudgetTracker()
    print('xizmatni tanlang')
    print('1.daromat qoshish')
    print('2.xarajat qoshish')
    print('3.daromat va xarajatni korish')
    print('4.balansini korish')

    choose=int(input('Tanlang (1-4): '))
    if choose==1:
        miqdor1=float(input('daroamatni kiriting:'))
        malumot1=input('Malumot kiriting: ')
        budget.add_income(miqdor1,malumot1)
    elif choose == 2:
        budget.add_expense()
        miqdor1=float(input('Xarajat kiriting:'))
        category1=input('kategoriya kiriting')        
        malumot1=input('Malumot kiriting')
        budget.add_expense(miqdor1,category1,malumot1)

    elif choose==3:
        budget.view_transaction()

    elif choose==4:
        budget.get_balance()

main()