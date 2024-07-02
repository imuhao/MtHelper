from PyQt6 import QtWidgets

class NumericTableWidgetItem(QtWidgets.QTableWidgetItem):
    def __lt__(self, other):
        if isinstance(other, NumericTableWidgetItem):
            return float(self.text()) < float(other.text())
        return super().__lt__(other)