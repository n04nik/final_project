from user import User


class Admin(User):
    """Класс Admin необходим для работы с базой users (вывод базы, изменение роли пользователя, удаление пользователя)."""
    def display_all_users(self):
        """Функция для всех пользователей."""
        self.c.execute("SELECT id, login, name, surname, email, telephone, role FROM users;")
        users = self.c.fetchall()
        for user in users:
            print(user)
    
    def change_user_role(self, user_id, new_role):
        """Функция для изменения роли зарегестрированного пользователя."""
        self.c.execute("UPDATE users SET role = ? WHERE id = ?;", (new_role, user_id))
        self.connect.commit()
        print(f"Роль пользователя с ID {user_id} изменена на {new_role}.")
        
    def dell_user(self, user_id):
        """Функция для удаления пользователя."""
        self.c.execute("DELETE FROM users WHERE id = ?;", (user_id,))
        self.connect.commit()
        print(f"Пользователь с ID {user_id} удален.")
