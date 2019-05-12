import requests

from bs4 import BeautifulSoup

import csv

import time

import sys

import os

import socket

from PyQt5 import uic, QtGui

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QLabel, QFileDialog

from PyQt5.QtGui import QPixmap, QIcon, QPalette, QImage

from PyQt5.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('qt_1.ui')
        self.ui.setWindowTitle('Employee Selection')

        self.options_ui = uic.loadUi('qt_options.ui')
        self.options_ui.setWindowTitle('Options')
        self.light()

        self.directory_ = os.path.abspath(os.curdir)

        self.start_button = self.ui.start_button
        self.start_button.setIcon(QIcon('E:\SHIT\Second course\Coursework\Task\icons\\start.png'))
        self.start_button.setIconSize(QSize(80, 80))
        self.start_button.clicked.connect(self.start)

        self.options_button = self.ui.options_button
        self.options_button.setIcon(QIcon('E:\SHIT\Second course\Coursework\Task\icons\\options.png'))
        self.options_button.setIconSize(QSize(80, 80))
        self.options_button.clicked.connect(self.options)

        self.quit_button = self.ui.quit_button
        self.quit_button.setIcon(QIcon('E:\SHIT\Second course\Coursework\Task\icons\\quit.png'))
        self.quit_button.setIconSize(QSize(80, 80))
        self.quit_button.clicked.connect(self.quit)

        self.folder_button = self.ui.folder_button
        self.folder_button.setIcon(QIcon('E:\SHIT\Second course\Coursework\Task\icons\\folder.png'))
        self.folder_button.setIconSize(QSize(80, 80))
        self.folder_button.clicked.connect(self.directory)

        self.ui.show()

    def start(self):
        while True:
            try:
                self.profession_box = self.ui.profession_enter
                self.experience_1_box = self.ui.experience_1_enter
                self.proff = self.profession_box.text()
                self.exp1  = self.experience_1_box.text()
                self.age_box_from = self.ui.age_from
                self.age_f = self.age_box_from.value()
                self.age_box_to = self.ui.age_to
                self.age_t = self.age_box_to.value()
                conect = self.connection()
                if str(self.proff) == '':
                    self.warning_message()
                elif conect == False:
                    self.conection_error()
                else:
                    call_pars = ScrapPars(self.proff, self.exp1, self.directory_, self.age_f, self.age_t)
                    call_pars.scrap_url()
                    call_pars.work_experience()
                    if self.age_f != 0.0 and self.age_t != 0.0:
                        call_pars.age()
                    if self.ui.english.isChecked():
                        call_pars._language()
                    call_pars.name()
                    reply = QMessageBox.information(self, 'End', '\nThanks for choosing us!\n', QMessageBox.Ok)
                break
            except RuntimeError:
                print('Error')

    def warning_message(self):
        reply = QMessageBox.warning(self, 'Profession', '\nYou need to enter profession!\n', QMessageBox.Ok)

    def conection_error(self):
        conect_error = QMessageBox.warning(self, 'Warning', '\nNo internet connection!\n', QMessageBox.Ok)

    def connection(self):
        try:
            socket.create_connection(("www.google.com", 80))
            return True
        except OSError:
            pass
        return False

    def quit(self, event):
        reply = QMessageBox.question(self, 'Quit', 'Are you shure to quit?', QMessageBox.Yes, QMessageBox.No)
        if reply ==  QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def options(self):

        self.light = self.options_ui.light
        self.dark = self.options_ui.dark
        self.start_button = self.options_ui.pushButton_2.clicked.connect(lambda: self.accept())

        self.options_ui.show()

    def directory(self):
        self.directory_ = QFileDialog.getExistingDirectory()

    def accept(self):
        if self.light.isChecked():
            self.ui.setStyleSheet('background-image: url(light_background.jpg); color: black')
            self.ui.label.setStyleSheet('background-image: url(widget_background.jpg); color: black')
            self.ui.profession_enter.setStyleSheet('background-image: url(widget_background.jpg); color: black')
            self.ui.experience_1_enter.setStyleSheet('background-image: url(widget_background.jpg); color: black')
            self.ui.age.setStyleSheet('background-image: url(widget_background.jpg); color: black')
            self.ui.age_text_from.setStyleSheet('background-image: url(widget_background.jpg); color: black')
            self.ui.age_text_to.setStyleSheet('background-image: url(widget_background.jpg); color: black')
            self.ui.age_from.setStyleSheet('background-image: url(widget_background.jpg); color: black')
            self.ui.age_to.setStyleSheet('background-image: url(widget_background.jpg); color: black')
            self.ui.label_3.setStyleSheet('background-image: url(widget_background.jpg); color: black')
            self.ui.english.setStyleSheet('background-image: url(widget_background.jpg); color: black')
            self.ui.show()
            self.options_ui.setStyleSheet('background-image: url(options_light.jpg); color: black')
            self.options_ui.light.setStyleSheet('background-image: url(back.jpg); color: black')
            self.options_ui.dark.setStyleSheet('background-image: url(back.jpg); color: black')
            self.options_ui.pushButton_2.setStyleSheet('background-image: url(back.jpg); color: black')

        elif self.dark.isChecked():
            self.ui.setStyleSheet('background-image: url(dark_background.jpg); color: white')
            self.ui.label.setStyleSheet('background-image: url(widget_background_dark.jpg); color: white')
            self.ui.profession_enter.setStyleSheet('background-image: url(widget_background_dark.jpg); color: white')
            self.ui.experience_1_enter.setStyleSheet('background-image: url(widget_background_dark.jpg); color: white')
            self.ui.age.setStyleSheet('background-image: url(widget_background_dark.jpg); color: white')
            self.ui.age_text_from.setStyleSheet('background-image: url(widget_background_dark.jpg); color: white')
            self.ui.age_text_to.setStyleSheet('background-image: url(widget_background_dark.jpg); color: white')
            self.ui.age_from.setStyleSheet('background-image: url(widget_background_dark.jpg); color: white')
            self.ui.age_to.setStyleSheet('background-image: url(widget_background_dark.jpg); color: white')
            self.ui.label_3.setStyleSheet('background-image: url(widget_background_dark.jpg); color: white')
            self.ui.english.setStyleSheet('background-image: url(widget_background_dark.jpg); color: white')
            self.ui.show()
            self.options_ui.setStyleSheet('background-image: url(options_dark.jpg); color: white')
            self.options_ui.light.setStyleSheet('background-image: url(back_2.jpg); color: white')
            self.options_ui.dark.setStyleSheet('background-image: url(back_2.jpg); color: white')
            self.options_ui.pushButton_2.setStyleSheet('background-image: url(back_2.jpg); color: white')

        self.options_ui.close()

    def light(self):
        self.ui.setStyleSheet('background-image: url(light_background.jpg); color: black')
        self.ui.label.setStyleSheet('background-image: url(widget_background.jpg); color: black')
        self.ui.profession_enter.setStyleSheet('background-image: url(widget_background.jpg); color: black')
        self.ui.experience_1_enter.setStyleSheet('background-image: url(widget_background.jpg); color: black')
        self.ui.age.setStyleSheet('background-image: url(widget_background.jpg); color: black')
        self.ui.age_text_from.setStyleSheet('background-image: url(widget_background.jpg); color: black')
        self.ui.age_text_to.setStyleSheet('background-image: url(widget_background.jpg); color: black')
        self.ui.age_from.setStyleSheet('background-image: url(widget_background.jpg); color: black')
        self.ui.age_to.setStyleSheet('background-image: url(widget_background.jpg); color: black')
        self.ui.label_3.setStyleSheet('background-image: url(widget_background.jpg); color: black')
        self.ui.english.setStyleSheet('background-image: url(widget_background.jpg); color: black')
        self.ui.show()
        self.options_ui.setStyleSheet('background-image: url(options_light.jpg); color: black')
        self.options_ui.light.setStyleSheet('background-image: url(back.jpg); color: black')
        self.options_ui.dark.setStyleSheet('background-image: url(back.jpg); color: black')
        self.options_ui.pushButton_2.setStyleSheet('background-image: url(back.jpg); color: black')


class ScrapPars:

    def __init__(self, proff, exp1, directory_, age_f, age_t):

        self.proxies = {'http': 'http://95.47.122.75:80808'}
        self.prof = proff
        self.exp = exp1
        self.dir = directory_
        self.age_from = int(age_f)
        self.age_to = int(age_t)

    def scrap_url(self):

        self.url_list = []
        a = 0
        while True:
            try:
                a+=1
                self.page_link = 'https://rabota.ua/employer/find/cv_list?keywords=' + self.prof + '&period=7&sort=date&pg=' + str(a)

                time_url_list = []
                self.results_page = []
                self.pages_links = []

                for i in range(0, 1):
                    self.page_link = self.page_link.replace('&pg='+str(i), '&pg='+str(i+1))
                    self.pages_links.append(self.page_link)

                for i in self.pages_links:
                    page_response = requests.get(i, proxies=self.proxies, timeout=5)
                    soup = BeautifulSoup(page_response.text, 'html.parser')
                    results = soup.find_all('div', attrs={'class': 'cv-list__item fd-f new full'})
                    self.results_page.append(results)

                for i in self.results_page:
                    for result in i:
                        url = result.find('a')['href']
                        person_url = 'https://rabota.ua' + url
                        time_url_list.append(person_url)
                if time_url_list == []:
                    break
                self.url_list = self.url_list+ time_url_list
                break
            except ReadTimeError:
                print('Sorry')

    def work_experience(self):
        key_words = [self.exp]
        time_list = []

        for i in self.url_list:
            link_responce = requests.get(i, proxies=self.proxies, timeout=5)
            link_soup = BeautifulSoup(link_responce.content, 'html.parser')
            exp = link_soup.find('div', id='ExperienceHolder').text
            exp_text = exp.lower()
            b = self.url_list.index(i)
            for j in key_words:
                if j in exp_text:
                    time_list.append(i)

        self.url_list = list(set(time_list))

    def age(self):
        time_list = []
        for link in self.url_list:
            print(link)
            link_responce = requests.get(link, proxies=self.proxies, timeout=5)
            link_soup = BeautifulSoup(link_responce.content, 'html.parser')
            name = link_soup.find('p', attrs={'class': 'rua-p-t_12'}).get_text()
            name_lst = list(name)
            str = ''
            for i in list(name):
                if i.isdigit():
                    str += i
            digt = int(str)
            if digt in range(self.age_from, self.age_to):
                time_list.append(link)
                print(time_list)
        self.url_list = time_list
        print(self.url_list)

    def _language(self):
        language_key = ['Английский', 'English', 'Англійська']
        time_list = []
        for i in self.url_list:
            link_responce = requests.get(i, proxies=self.proxies, timeout=5)
            link_soup = BeautifulSoup(link_responce.content, 'html.parser')

            language = link_soup.find('div', id='LanguagesHolder')
            language = [i.text for i in language.find_all('b')]

            for j in language_key:
                if j in language:
                    time_list.append(i)
        self.url_list = list(set(time_list))
        return self.url_list

    def name(self):

        self.name_list = []
        for i in self.url_list:
            link_responce = requests.get(i, proxies=self.proxies, timeout=5)
            link_soup = BeautifulSoup(link_responce.content, 'html.parser')
            name = link_soup.find('span', attrs={'class': 'rua-p-t_20'}).text
            self.name_list.append(name)
        for i in range(len(self.url_list)):
            data = {'Name': self.name_list[i], 'Url': self.url_list[i]}
            exel_record(data, self.dir)


def exel_record(data, dir):

    timestr = time.strftime("%Y-%m-%d_%H-%M-%S")
    timestr = str(dir) + '\\' + timestr
    with open(timestr + '.csv','a', newline="") as f:
        colums = ['Name', 'Url']
        writer = csv.DictWriter(f, fieldnames=colums, delimiter=";")
        writer.writerow(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
