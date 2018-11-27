
import psycopg2


def drop_tables():
    """ create tables in the SoundBox database"""
    commands = (
        """
        DROP TABLE utilizador_partilha CASCADE
        """,
        """ 
        DROP TABLE album CASCADE
        """,
        """
        DROP TABLE compositores CASCADE
        """,
        """
        DROP TABLE grupo CASCADE
        """,
        """
        DROP TABLE letras_musica CASCADE 
        """,
        """
        DROP TABLE playlist CASCADE 
        """,
        """
        DROP TABLE editora CASCADE 
        """,
        """
        DROP TABLE criticas CASCADE 
        """,
        """
        DROP TABLE genero_musical CASCADE 
        """,
        """
        DROP TABLE utilizador_partilha_criticas CASCADE 
        """,
        """
        DROP TABLE utilizador_partilha_playlist CASCADE 
        """,
        """
        DROP TABLE album_genero_musical CASCADE
        """,
        """
        DROP TABLE letras_musica_playlist CASCADE 
        """)

    try:

        conn = psycopg2.connect(host="localhost",database="SoundBox", user="postgres", password="postgres")
        cur = conn.cursor()
        # DROP table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
 
if __name__ == '__main__':
    drop_tables()
