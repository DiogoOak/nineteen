import psycopg2
def create_tables():
    """ create tables in the SoundBox database"""
    commands = (
        """
        CREATE TABLE utilizador_partilha (
	        numutilizador		 INTEGER DEFAULT 8,
	        nomeutilizador	 VARCHAR(512) NOT NULL,
	        mail			 VARCHAR(512) NOT NULL,
	        nomeplaylist		 VARCHAR(512),
	        partilha_numutilizador INTEGER UNIQUE NOT NULL,
	        partilha_nomemusica	 VARCHAR(512) NOT NULL,
	        PRIMARY KEY(numutilizador)
        )
        """,
        """
        CREATE TABLE album (
	        nalbum			 INTEGER,
	        nomealbum			 VARCHAR(512),
	        listamusicas		 VARCHAR(512),
	        criticas			 TEXT(512) UNIQUE,
	        generomusical		 VARCHAR(512),
	        nomeeditora		 VARCHAR(512),
	        editora_nomeeditora	 VARCHAR(512) NOT NULL,
	        compositores_nomecompositor VARCHAR(512) NOT NULL,
            PRIMARY KEY(nalbum)
        )
        """,
        """
        CREATE TABLE compositores (
	        nomecompositor VARCHAR(512),
	        nomemusica	 VARCHAR(512),
	        PRIMARY KEY(nomecompositor)
        )
        """,
        """
        CREATE TABLE grupo (
        	nomegrupo	 VARCHAR(512),
        	nomemembros	 VARCHAR(512),
        	generomusical BOOL,
        	PRIMARY KEY(nomegrupo)
        )
        """,
        """
        CREATE TABLE letras_musica (
	        nomemusica			 VARCHAR(512),
	        letra				 TEXT(512),
	        musica_nomemusica			 VARCHAR(512) UNIQUE NOT NULL,
	        musica_nomealbum			 VARCHAR(512) NOT NULL,
            musica_nomegrupo			 VARCHAR(512) NOT NULL,
	        musica_nomecompositor		 VARCHAR(512) NOT NULL,
	        musica_letra			 VARCHAR(512) NOT NULL,
	        musica_generomusical		 VARCHAR(512) NOT NULL,
        	musica_grupo_nomegrupo		 VARCHAR(512) UNIQUE NOT NULL,
        	musica_compositores_nomecompositor VARCHAR(512) UNIQUE NOT NULL,
        	musica_album_nalbum		 INTEGER UNIQUE NOT NULL,
	        PRIMARY KEY(nomemusica)
        )
        """,
        """
        CREATE TABLE playlist (
        	nomeplaylist	 VARCHAR(512),
        	nomemusica	 VARCHAR(512),
        	nomeutilizador VARCHAR(512),
        	PRIMARY KEY(nomeplaylist)
        )
        """,
        """
        CREATE TABLE genero_musical (
        	nomegenero VARCHAR(512),
        	PRIMARY KEY(nomegenero)
        )
        """,
        """
        CREATE TABLE criticas (
        	nomeutilizador VARCHAR(512),
        	criticas	 TEXT(512),
        	album_nalbum	 INTEGER NOT NULL,
        	PRIMARY KEY(nomeutilizador)
        )
        """,
        """
        CREATE TABLE editora (
        	nomeeditora VARCHAR(512),
        	nomealbum	 VARCHAR(512),
        	PRIMARY KEY(nomeeditora)
        )
        """,
        """
        CREATE TABLE utilizador_partilha_criticas (
        	utilizador_partilha_numutilizador INTEGER DEFAULT 8,
        	criticas_nomeutilizador		 VARCHAR(512),
        	PRIMARY KEY(utilizador_partilha_numutilizador,criticas_nomeutilizador)
        )
        """,
        """
        CREATE TABLE utilizador_partilha_playlist (
        	utilizador_partilha_numutilizador INTEGER DEFAULT 8,
        	playlist_nomeplaylist		 VARCHAR(512),
        	PRIMARY KEY(utilizador_partilha_numutilizador,playlist_nomeplaylist)
        )
        """,
        """
        CREATE TABLE album_genero_musical (
        	album_nalbum		 INTEGER,
        	genero_musical_nomegenero VARCHAR(512),
        	PRIMARY KEY(album_nalbum,genero_musical_nomegenero)
        )
        """,
        """
        CREATE TABLE letras_musica_playlist (
        	letras_musica_nomemusica VARCHAR(512),
        	playlist_nomeplaylist	 VARCHAR(512),
        	PRIMARY KEY(letras_musica_nomemusica,playlist_nomeplaylist)
        )
        """)
    try:
        conn = psycopg2.connect(host="localhost",database="SoundBox", user="postgres", password="postgres")
        cur = conn.cursor()
        # create table one by one
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

    create_tables()
