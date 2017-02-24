import kivy
kivy.require('1.9.2') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class LoginScreen(FloatLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        self.confirmationButton = Button(text='Confirm')
        self.confirmationButton.bind(on_press=self.login)
        self.add_widget(self.confirmationButton)

    def login(self, instance):
        print('>> Loging in...')
        print(instance)
        print(self.username.text)
        print(self.password.text)

class BPM(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    BPM().run()