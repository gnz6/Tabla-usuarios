import sys

from psycopg2 import pool
from logger import log


class Connection:
    DATABASE = "test_db"
    USERNAME = "postgres"
    PASSWORD = "admin"
    PORT = "5432"
    HOST = "127.0.0.1"
    MIN_CON = 1
    MAX_CON = 5
    pool = None

    @classmethod
    def getPool(cls):
        if cls.pool is None:
            try:
                cls.pool = pool.SimpleConnectionPool(cls.MIN_CON, cls.MAX_CON,
                                                     host=cls.HOST,
                                                     user=cls.USERNAME,
                                                     password=cls.PASSWORD,
                                                     port=cls.PORT,
                                                     database=cls.DATABASE,
                                                     )
                log.debug(f'Successful connection : {cls.pool}')
                return cls.pool
            except Exception as e:
                log.error(f'Exception : {e}')
                sys.exit()
        else:
            return cls.pool

    @classmethod
    def getConnection(cls):
        connection = cls.getPool().getconn()
        log.debug(f'Connection established from pool : {connection}')

    @classmethod
    def freeOnePool(cls, connection):
        cls.getPool().putconn(connection)
        log.debug(f'Returned connection to  {connection}')

    @classmethod
    def closePool(cls):
        cls.getPool().closeall()
        log.debug("Pool closed")

# if __name__ == "__main__":
