class Soda:
    def __init__(self, ing=None):
        self.ing = ing

    def Show_my_drink(self):
        if self.ing:
            print(f'газировка и {self.ing}')

        else:
            print('бычная газировка')

 drink1 = Soda()
drink2 = Soda('малина')
drink1.show_my_drink()
drink2.Show_my_drink()

