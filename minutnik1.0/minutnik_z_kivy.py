import kivy
import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty
from kivy.clock import Clock




class MyGrid(Widget):
    wartosc = ObjectProperty(None) #to co jest podane
    wyswietlane_minuty = NumericProperty(0) # to co się wyświetla
    sekundy = NumericProperty(0)
    czas = 0
    czas_pocz = 0
    trening = ObjectProperty('Wpisz ilość minut, potem wciśnij "start"\n by zacząć odliczanie')
    wielkosc_czcionki_napis = NumericProperty(20)
    kontrola = False

    def przycisk(self):

        if self.kontrola == False or self.sekundy == 0 and self.wyswietlane_minuty == 0:
            self.wielkosc_czcionki_napis = 50
            self.trening = 'Trening trwa'
            self.kontrola = True
            def odliczanie():
                if self.czas <= 0 and self.sekundy == 0:
                    Clock.unschedule(self.event)
                    self.trening = 'koniec treningu'
                    self.wielkosc_czcionki_napis = 50

                else:
                    self.czas -= 1
                    if self.sekundy >=1:
                        self.sekundy -=1

                    elif self.sekundy < 1:
                        self.sekundy = 59
                        self.sekundy -=1

                    if self.czas_pocz - 60 == self.czas and self.wyswietlane_minuty != 0:
                        self.wyswietlane_minuty -= 1
                        self.czas_pocz = self.czas_pocz - 60


            def czas_licz():
                self.event = Clock.schedule_interval(lambda dt: odliczanie(), 1)
                return self.event

            if self.czas != 0:
                czas_licz()
                odliczanie()
            try:
                self.wyswietlane_minuty = int(self.wartosc.text) - 1
                self.czas = int(self.wartosc.text)*60
                self.czas_pocz = int(self.wartosc.text)*60
                self.sekundy = 60
                czas_licz()
                odliczanie()
            except ValueError:
                pass
            self.wartosc.text = ''
        else:
            self.wartosc.text = ''
    def zatrzymaj(self):
        if self.sekundy > 0:
            print('zatrzymaj')
            Clock.unschedule(self.event)
            self.kontrola = False

            znacznik = random.randint(0, 100)
            if znacznik > 50:
                self.trening = 'przerwa'
                self.wielkosc_czcionki_napis = 50
            elif znacznik == 51:
                self.trening = 'Przerwa? Trzeba jechać dalej ;)'
                self.wielkosc_czcionki_napis = 50
            else:
                self.trening = 'przerwa'
                self.wielkosc_czcionki_napis = 50
        else:
            pass

    def zeruj(self):
        self.czas = 0
        self.wyswietlane_minuty = 0
        self.sekundy = 0
        self.trening = ''

        


class MinutnikApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MinutnikApp().run()
