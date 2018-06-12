from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
import pymysql
from kivy import Config

Config.set('graphics', 'multisamples', '0')
conn=pymysql.connect(host="localhost",user="root",password='',db="project_1")

class ScreenManagement(ScreenManager):
    pass
#sm=ScreenManager()
class MainScreen(Screen):
    fw = open('session_test.txt','r')
    str=fw.read()
    print(str)
    if str=='':
        print("new login")
    else:
        print("old user")
        #self.parent.current = 'homepage'
        #sm.add_widget(HomePage())
    
    def login(self, *args):
        #conn=pymysql.connect(host="localhost",user="root",password='',db="project_1")
        mycur = conn.cursor()
        username = self.ids.username_input
        username_text = username.text
        print(username_text)
        password = self.ids.password_input
        password_text = password.text
        print(password_text)
        
        fw = open('session_test.txt','w')
        fw.write(username_text+'#'+password_text)
        #fw.write("{}{}",username_text,password_text)
        fw.close()
        fr=open('session_test.txt','r')
        text=fr.read()
        print(text)
        
        
        #if username_text == "root" and password_text == "123":
        if username_text=="" or password_text=="":
            label = self.ids.success
            label.text="Please enter the required field"
        #elif username_text!="" or password_text!="":
        else:
            mycur.execute("select * from users where username='%s' and password ='%s'" %(username_text,password_text))
            #print("else if is working")
            data=mycur.fetchone()
            print(data)
            #if mycur.fetchone is not None:
            if data is not None:   
                label = self.ids.success
                label.text="Login sucessful"
                self.parent.current = 'homepage'
                
                conn.commit()
               
            else:
                label = self.ids.success
                label.text="Invalid username or password"
               
            
        label = self.ids.username_input
        username_text=None
        label = self.ids.password_input
        password_text=None

    def logout(self,*args):
      
        fw = open('session_test.txt','w')
        fw.truncate()
        label = self.ids.success
        label.text="Logout sucessfully"
        
        label = self.ids.username_input
        username_input=""
        label = self.ids.password_input
        password_input=""
        
        conn.close() 
        #self.parent.current = 'main_screen'
        #MainScreen()
        
        
class HomePage(Screen):
    
    pass
                
class Registration(Screen):
    
    
    def regis(self, *args):
             
        username = self.ids.username_input
        username_text = username.text
        '''
        useremail = self.ids.useremail_input
        useremail_text = useremail.text
        
        userphone = self.ids.userphone_input
        userphone_text = userphone.text
        '''
        password = self.ids.password_input
        password_text = password.text
        mycur = conn.cursor()
        mycur.execute('INSERT INTO users values ("%s","%s")' % (username_text,password_text))
        conn.commit()      
        print('Data entered')
        conn.close()
        label = self.ids.success
        label.text="Registration successful"


class login(App):
    def build(self):
        return ScreenManagement()

if __name__ == '__main__':
    login().run()