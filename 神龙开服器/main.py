import os
import webbrowser
import sys
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ui_gui import Ui_gui


class Main(QMainWindow, Ui_gui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_tunnel.clicked.connect(self.open_web)
        self.button_launch.clicked.connect(self.launch)
        self.button_flash.clicked.connect(self.flash)
        self.combo_version.currentIndexChanged.connect(self.update_mod)
        self.flash()

        self.show()

    def flash(self):
        self.combo_java.clear()
        self.combo_version.clear()
        self.combo_map.clear()
        self.combo_java.addItems(os.listdir('C:/PROGRA~1/Java'))
        self.combo_version.addItems(os.listdir('D:/server/client'))
        self.combo_map.addItems(os.listdir('D:/server/map'))

    def open_web(self):
        if QMessageBox.question(self,'开启隧道','Yes --- uulap\nNo --- rosmontis{}'.format(os.popen('ipconfig').read().replace('\n\n','\n')))==QMessageBox.Yes:
            webbrowser.open('https://console.uulap.com/')
        else:
            webbrowser.open('https://domain.rosmontis.com/home')

    def update_mod(self):
        for i in os.listdir(f'D:/server/client/{self.combo_version.currentText()}'):
            if 'forge' in i.lower() or 'fabric' in i.lower():
                self.check_mod.setCheckable(True)
                self.check_mod.setText('启用模组(√)')
                break
            else:
                self.check_mod.setCheckable(False)
                self.check_mod.setText('启用模组(×)')
            self.update()

    def launch(self):
        self.hide()

        # set map
        with open('D:/server/server.properties', 'r', encoding='utf-8')as file:
            dic = dict([temp.split('=')
                       for temp in file.read().split('\n') if '=' in temp])
            dic['level-name'] = f'map/{self.combo_map.currentText()}'
        with open('D:/server/server.properties', 'w', encoding='utf-8')as file:
            file.write('\n'.join(['='.join(i) for i in dic.items()]))

        # 1player/100M (0.1G)
        java = f"C:/PROGRA~1/Java/{self.combo_java.currentText()}/bin/java.exe"
        version = self.combo_version.currentText()
        # solve log4j2 bug
        argv='-XX:+UseG1GC -XX:-UseAdaptiveSizePolicy -XX:-OmitStackTraceInFastThrow -Dfml.ignoreInvalidMinecraftCertificates=True -Dfml.ignorePatchDiscrepancies=True -Dlog4j2.formatMsgNoLookups=true'
        # change dir to the server folder,server files will be placed correctly
        os.chdir('D:/server/')
        if self.check_mod.isChecked():
            mod = [i for i in os.listdir(
                f'D:/server/client/{version}') if 'forge' in i][0]
            info=os.system(
                f'{java} -Xmx{int(float(self.ram.text()[:-2])*1024)}m {argv} -jar "D:/server/client/{version}/{mod}"')
        else:
            info=os.system(
                f'{java} -Xmx{int(float(self.ram.text()[:-2])*1024)}m {argv} -jar "D:/server/client/{version}/minecraft_server.{version}.jar"')
        # last=''
        # while True:
        #     temp=info.readline(-1)
        #     if temp!=last:
        #         print(temp,end='')
        #         last=temp
        #     if 'Done'in temp:
        #         break
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec())
