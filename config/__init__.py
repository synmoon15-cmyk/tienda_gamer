# Si mysqlclient no esta instalado, usa PyMySQL automaticamente (pip install pymysql cryptography)
try:
    import MySQLdb  # noqa: F401
except ImportError:
    try:
        import pymysql
        pymysql.install_as_MySQLdb()
    except ImportError:
        pass
