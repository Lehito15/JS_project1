import sqlite3
import Team

class DataBase:
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def __del__(self):
        self.connection.close()

    def create_tables(self):
        create_table_query = '''
                    CREATE TABLE IF NOT EXISTS User (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL
                    )
                '''
        self.cursor.execute(create_table_query)
        create_table_league_query = '''
                    CREATE TABLE IF NOT EXISTS League (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nrkolejki INTEGER,
                        my_team INTEGER,
                        user_id INTEGER,
                        FOREIGN KEY (user_id) REFERENCES User(id)
                    )
                '''

        self.cursor.execute(create_table_league_query)
        create_team_table_query = '''
            CREATE TABLE IF NOT EXISTS Team (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code INTEGER,
                nameT TEXT,
                points INTEGER,
                wins INTEGER,
                losses INTEGER,
                draws INTEGER,
                league_id INTEGER,
                FOREIGN KEY (league_id) REFERENCES League(id)
            )
        '''
        self.cursor.execute(create_team_table_query)
        self.connection.commit()
    def save_game(self,user_name,current_round, my_team,teams):
        self.cursor.execute("SELECT id FROM User WHERE name = ?", (user_name,))
        user_row = self.cursor.fetchone()

        if user_row is None:
            # Jeśli użytkownik nie istnieje, dodaj go do tabeli User
            self.cursor.execute("INSERT INTO User (name) VALUES (?)", (user_name,))
            user_id = self.cursor.lastrowid
        else:
            # Jeśli użytkownik istnieje, pobierz jego id
            user_id = user_row[0]
        self.cursor.execute("""
                   INSERT INTO League (nrkolejki, my_team, user_id)
                   VALUES (?, ?, ?)
               """, (current_round, my_team, user_id))
        league_id = self.cursor.lastrowid
        print(league_id)
        print(len(teams))
        i = 0
        for team in teams:
             self.cursor.execute("INSERT INTO Team (code, nameT, points, wins, losses, draws, league_id) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (team.code, team.name, team.points, team.wins, team.losses, team.draws, league_id))
             i+=1
        self.connection.commit()

    def read_database(self,user_name,idL=None):
        query = """
                    SELECT League.nrkolejki, League.my_team, League.id
                    FROM League
                    JOIN User ON League.user_id = User.id
                    WHERE User.name = ?
                """
        parameters = [user_name]

        if idL is not None:
            query += " AND League.id = ?"
            parameters.append(idL)

        self.cursor.execute(query, parameters)
        league_info = self.cursor.fetchall()
        if idL == None:
            idL = league_info[0][2]

        self.cursor.execute("""
                            SELECT  Team.nameT, Team.code, Team.points, Team.wins, Team.losses, Team.draws
                            FROM League
                            JOIN User ON League.user_id = User.id
                            JOIN Team ON Team.league_id = League.id
                            WHERE User.name = ? AND League.id = ?
                        """, (user_name,idL))
        league_info +=self.cursor.fetchall()
        # for info in league_info:
        #     print(info)
        return league_info
    def check_user(self,user_name):
        query = "SELECT COUNT(*) FROM User WHERE name = ?"
        self.cursor.execute(query, (user_name,))
        result = self.cursor.fetchone()

        if result[0] > 0:
            return True
        else:
            return False
    def user_leagues(self,user_name):
        self.cursor.execute("""
                            SELECT League.nrkolejki, League.my_team,League.id
                            FROM League
                            JOIN User ON League.user_id = User.id
                            WHERE User.name = ?
                        """, (user_name,))
        league_info = self.cursor.fetchall()
        #print(league_info)
        return league_info

    def count_saved_leagues(self, user_name):
        self.cursor.execute("""
            SELECT COUNT(*) FROM League
            JOIN User ON League.user_id = User.id
            WHERE User.name = ?
        """, (user_name,))
        result = self.cursor.fetchone()
        count = result[0] if result else 0
        return count

# t1 = Team.Team('Arsenal',1,3)
# t2 = Team.Team('Chealsea',2)
# db = DataBase('test5.db')
# #db.save_game('leh', 7, 7,[t1,t2])
# db.read_database('leh')
# #db.user_leagues('leh1')
# # print(db.check_user('leh1'))
# # print(db.check_user('dfwf'))
