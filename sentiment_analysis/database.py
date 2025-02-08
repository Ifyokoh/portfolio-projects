import os
import psycopg2


class Database():
    def __init__(self):
        """
        Connection to work with the database.
        :return: connection
        """
     
        self.__connection = psycopg2.connect(
                        user='flask',
                        password='flask',
                        database='sentiments',
                        host='db',
                        port=5432
                        
             )


    def create_table(self) -> None:
        """
        Create table for storing tweet in database.
        :return: None
        """
        with self.__connection.cursor() as cur:
            cur.execute('''
                CREATE TABLE IF NOT EXISTS tweet (
                    id SERIAL PRIMARY KEY,
                    hashtag VARCHAR,
                    text VARCHAR,
                    created_at TIMESTAMP DEFAULT NOW(),
                    sentiment VARCHAR
                );
        ''')
            self.__connection.commit()

    def insert_record(self, data) -> None:
        """
        Inserts the result
        :return: None
        """
        with self.__connection.cursor() as cur:
            for d in data:
                cur.execute("INSERT into tweet(hashtag, text, created_at, sentiment) VALUES (%s, %s, %s, %s)", d)
 
            self.__connection.commit()
    

    def get_records(self):
        """
        Returns the desired number of most recent results 
        :return:
        """
        with self.__connection.cursor() as cur:
            cur.execute("SELECT * FROM tweet")
            return cur.fetchall()
        


if __name__ == "__main__":
    database = Database()
    database.create_table()