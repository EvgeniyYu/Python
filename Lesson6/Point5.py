class Stationery:
    def __init__(self, title):
        self._title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'{self._title}: Отрисовка ручкой')

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'{self._title}: Отрисовка карандашом')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'{self._title}: Отрисовка маркером')

st = Stationery('Канцелярия')
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

st.draw()
pen.draw()
pencil.draw()
handle.draw()