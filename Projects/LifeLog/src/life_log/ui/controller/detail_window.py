from PySide6.QtWidgets import QWidget
from src.life_log.ui.views.ui_detail_window import Ui_DetailWindow


class DetailWindow(QWidget, Ui_DetailWindow):
    """A window for displaying and editing the details of a life log entry."""

    def __init__(self):
        """Initialize the DetailWindow and set up the UI."""
        super().__init__()
        self.setupUi(self)

    def set_title(self, title: str):
        """Set the title of the entry.

        Args:
            title (str): The title text to display.
        """
        self.title_label.setText(title)
        self.title_label.setStyleSheet("font-weight: bold")
        self.title_entry.setText(title)

    def set_status(self, status: str, color: str):
        """Set the status of the entry with a specific color.

        Args:
            status (str): The status text to display.
            color (str): The color of the status text (e.g., 'red', '#00FF00').
        """
        self.status_label.setText(status)
        self.status_label.setStyleSheet(f"color: {color}; font-weight: bold;")

    def set_description(self, description: str):
        """Set the description text of the entry.

        Args:
            description (str): The description text.
        """
        self.description_entry.setText(description)

    def get_title_text(self) -> str:
        """Get the current text from the title entry.

        Returns:
            str: The text in the title entry field.
        """
        return self.title_entry.toPlainText()

    def get_description_text(self) -> str:
        """Get the current text from the description entry.

        Returns:
            str: The text in the description entry field.
        """
        return self.description_entry.toPlainText()

    def get_status_text(self) -> str:
        """Get the currently selected status text.

        Returns:
            str: The text of the selected status from the status menu.
        """
        return self.status_menu.currentText()

    def set_due_date(self, date):
        """Set the due date of the entry.

        Args:
            date (QDate): The date to set in the date edit widget.
        """
        self.date_edit.setDate(date)
