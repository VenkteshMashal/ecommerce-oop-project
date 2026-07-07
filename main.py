from database.connection import create_tables
from ui.login_ui import LoginUI

if __name__ == "__main__":
    create_tables()

    app = LoginUI()
    app.mainloop()