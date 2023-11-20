import mysql.connector
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivymd.icon_definitions import md_icons
import sys

sm = ScreenManager()


class signup_screen(Screen):
    pass


class login_screen(Screen):
    pass


class login_1(Screen):
    pass


class app(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.vuu = Builder.load_file("login_screen.kv")
        sm.add_widget(login_screen(name='login'))
        sm.add_widget(signup_screen(name='signup'))
        sm.add_widget(login_1(name='login1'))
        return sm

    # this is a function that changes the theme of the app from the default light to dark
    def theme(self):
        self.theme_cls.theme_style = "Light"

    # this section is used as a button in the main screen to close the application
    @staticmethod
    def exit():
        print("Application Closed")
        sys.exit()

    # This part is used in the carousel to go to the next data entry page
    def next(self):
        self.root.get_screen('signup').ids.carousel.load_next(mode='next')

    #This part is used in the carousel to go to the next data entry page
    def next1(self):
        self.root.get_screen('signup').ids.carousel.load_next(mode='next')

    def previous(self):
        self.root.get_screen('signup').ids.carousel.load_previous()

    # this part uses mysql.connetor and the inputs from the signup form to enter data to the database
    def submit(self):
        studentID = self.root.get_screen('signup').ids.StudID.text
        print(studentID)
        newFname = self.root.get_screen('signup').ids.FName.text
        print(newFname)
        newMI = self.root.get_screen('signup').ids.MI.text
        print(newMI)
        newLname = self.root.get_screen('signup').ids.LName.text
        print(newLname)
        newEmail = self.root.get_screen('signup').ids.Email.text
        print(newEmail)
        newphone = self.root.get_screen('signup').ids.phone.text
        print(newphone)
        newResidence = self.root.get_screen('signup').ids.RD.text
        print(newResidence)
        newRoomNo = self.root.get_screen('signup').ids.RN.text
        print(newRoomNo)
        newPassw = self.root.get_screen('signup').ids.passw.text
        print(newPassw)

        # connecting to the mysql database using mysql connector
        dbase = mysql.connector.connect(host="localhost",
                                        user="root",
                                        passwd="Dc762019",
                                        database="vuu_dbalert")
        myCursor = dbase.cursor()
        print("Database connected!")

        # This command gets the data from the textboxes and transforms it to an executable sql code
        command = "INSERT INTO vuu_dbalert.student(StudentID, LastName, MiddleI, FirstName, Email, Pasword, PhoneNumber, " \
                  "HallID, RoomNo) VALUES (" + "'" + studentID + "'" + "," + "'" + newLname + "'" + "," + "'" + newMI + "'" + "," + "'" + newFname + "'" + "," + "'" + newEmail + "'" \
                  + "," + "'" + newPassw + "'" + "," + "'" + newphone + "'" + "," + "'" + newResidence + "'" + "," + "'" + newRoomNo + "'" + ");"

        print(command)
        myCursor.execute(command)
        dbase.commit()
        print("done")
        self.root.get_screen('signup').manager.current = 'login'


if __name__ == '__main__':
    Window.size = (360, 640)  # not specifying sizes for ios and android
    app().run()
