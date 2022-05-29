import os
import sys
import time
from modules import updater

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QPushButton, QHBoxLayout, QLineEdit, QWidget, \
    QLabel, QAction, QComboBox, QTextEdit, QDialog, QInputDialog, QFontDialog, QVBoxLayout, QFileDialog, QTableWidget, \
    QAbstractItemView, QHeaderView, QCheckBox, QTableWidgetItem


class MainWindow(QMainWindow):
    def __init__(self, parent=None):  # 主要控件和布局
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("TrackingCOVID Pre 1")
        self.setFixedSize(370, 330)
        self.widget = QWidget()
        self.setCentralWidget(self.widget)

        self.updater = updater.Updater(2022)

        self.all_v_layout = QVBoxLayout(self)

        self.intro_title_label = QLabel("TrackingCOVID", self)
        self.intro_version_label = QLabel("Version: Pre 1 (GUI)", self)
        self.intro_data_label = QLabel("数据时间(2022):", self)
        self.intro_data_selection_label = QLabel("载入数据:", self)
        self.intro_data_selection_combobox = QComboBox(self)
        self.intro_generate_button = QPushButton("数据生成", self)
        self.intro_analyze_button = QPushButton("数据分析", self)
        self.intro_render_button = QPushButton("数据渲染", self)
        self.intro_update_button = QPushButton("更新数据", self)

        self.all_v_layout.addWidget(self.intro_title_label)
        self.all_v_layout.addWidget(self.intro_version_label)
        self.all_v_layout.addWidget(self.intro_data_label)
        self.all_v_layout.addWidget(self.intro_data_selection_label)
        self.all_v_layout.addWidget(self.intro_data_selection_combobox)
        self.all_v_layout.addWidget(self.intro_generate_button)
        self.all_v_layout.addWidget(self.intro_analyze_button)
        self.all_v_layout.addWidget(self.intro_render_button)
        self.all_v_layout.addWidget(self.intro_update_button)

        self.widget.setLayout(self.all_v_layout)
        self.initUI()

    def initUI(self):
        self.intro_title_label.setFont(QFont("Microsoft YaHei", 20, QFont.Bold))
        self.intro_title_label.setAlignment(Qt.AlignCenter)
        self.intro_version_label.setAlignment(Qt.AlignCenter)
        self.intro_data_selection_combobox.addItem("2022")
        self.intro_data_selection_combobox.currentIndexChanged.connect(self.intro_data_selection_combobox_changes)
        self.intro_update_button.clicked.connect(self.intro_update_data)
        self.intro_get_updated_file_time()

    def intro_get_updated_file_time(self):
        self.intro_data_label.setText("数据时间(2022):" + time.ctime(os.path.getmtime(f"data_backup/Tracking the Epidemic (2022).html")))

    def intro_data_selection_combobox_changes(self):
        print(self.intro_data_selection_combobox.currentText())

    def intro_update_data(self):
        reply = self.updater.download_html()
        if "online" in reply:
            QMessageBox.information(self, "提示", "已成功更新疫情数据")
        elif "offline" in reply:
            QMessageBox.warning(self, "警告", "更新疫情数据失败，已使用近期的备份数据")
        self.intro_get_updated_file_time()


if __name__ == "__main__":
    start = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(start.exec_())
