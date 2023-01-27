from logger import log
from main import Connection


class PoolCursor:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        log.debug("Init __enter__")
        self.connection = Connection.getConnection()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug("init __exit__")
        if exc_val:
            self.connection.rollback()
            log.debug(f'Exception occurred: {exc_val} {exc_type} {exc_tb}')
        else:
            self.connection.commit()
            log.debug('Committed')
        self.cursor.close()
        Connection.freeOnePool(self.connection)
