# def print_human_name(human):
#     print(human['name'])
#
#
# h1 = {'name': 'ABC'}
# h2 = {'name': 'QWE'}
# h3 = {'full_name': 'asdas'}
#
# print_human_name(h3)

class Phone:
    def __init__(self, phone_model):
        self.model = phone_model
        self._serial_number = 654654321
        self._loading()
        self.__bla = 'qwe'

    def call(self):
        print('calling...')

    def _loading(self):
        print(self.model, 'loading...')

    def get_serial_number(self):
        return self._serial_number


# my_phone1 = Phone('nokia1100')
# my_phone1._loading()
# print(my_phone1.get_serial_number())
# print(my_phone1._Phone__bla)


class SmartPhone(Phone):
    def sms(self):
        print('smsing')

    def email(self):
        print('emailing')


# my_phone1 = SmartPhone('nokia1100')
# my_phone1.sms()
# my_phone1.call()


class IPhone(SmartPhone):
    def __init__(self, phone_model):
        super().__init__(phone_model)
        self.show_logo()

    def player(self):
        print('music playing')

    def browser(self):
        print('browsering')

    def sms(self):
        print('Imessage sending')

    def show_logo(self):
        print('Apple is showing')


# iphone = IPhone('6')
# iphone.browser()
# iphone.sms()


class NextGenerationPhone(IPhone):
    def touch_id(self):
        print('touch_id is working')


class Huawei(NextGenerationPhone):
    pass


class Samsung(NextGenerationPhone):
    pass


class Player:
    def player_method(self):
        print('Р РѕРґРёС‚РµР»СЊСЃРєРёР№ РјРµС‚РѕРґ РєР»Р°СЃСЃР° Player')


class Navigator:
    def nav_method(self):
        print('Р РѕРґРёС‚РµР»СЊСЃРєРёР№ РјРµС‚РѕРґ РєР»Р°СЃСЃР° Navigaror')


class Mobile(Player, Navigator):
    def mobile(self):
        print('РґРѕС‡РµСЂРЅРёР№ РјРµС‚РѕРґ')


# mobile = Mobile()
# mobile.mobile()
# mobile.nav_method()
# mobile.player_method()

class Auto:
    def auto_start(self, param1, param2=None):
        if param2 is not None:
            print(param1 + param2)
        else:
            print(param1)


auto1 = Auto()
auto1.auto_start(10, 20)

auto2 = Auto()
auto2.auto_start(10)