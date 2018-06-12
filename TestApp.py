from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

#Create the manager
sm = ScreenManager()

#Add few screens
'''
for i in range(4):
    screen=Screen(name='Title %d' %i)
    sm.add_widget(screen)
    
    sm.current ='Title 2'
    '''
class MenuScreen(Screen):
    pass
class SettingScreen(Screen):
    pass

class TestApp(App):
    def build(self):
        return sm

if __name__== '__main__':
    TestApp().run()