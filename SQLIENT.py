import SQLITio as dbsq
cdir = "PYCLI/sqlitio-portable"
help = """
CRDB - Creates a database file
USDB - Selects your desired database
FTCH - Shows Data in a page from the database you chose using the USE command
MKPG - Makes a page in the database you choose
CNCT - Connect to remote database (Coming soon)
Run any command without any parameter to get more info about it
"""
while True:
    iCmd=input(f"{cdir}/ >>")