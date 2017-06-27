# main file to run the app with allocating threading

from PyQt5 import QtWidgets
import sys
from UI.main_window import Ui_MainWindow
from UI.login import Ui_Dialog

def main():
    pass
# Zip Test
    # archive = zip.Make_presskit("presskit.zip")
    # if archive.Validate_presskit() is True:
    #     archive.make_presskit()
    # else:
    #     print("Something went wrong")
    #
    # archive.options["full"]()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()