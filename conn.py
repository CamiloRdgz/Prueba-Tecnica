import mysql.connector
from mysql.connector import Error

class DataAccessObject():
    def __init__(self) -> None:
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="practicas_okuo"
            )
        except Error as ex:
            print("Error while trying connection: {0}".format(ex))

    def readEmpresasDAO(self):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT * FROM empresas ORDER BY id_empresa ASC")
                result = cursor.fetchall()
                return result
            except Error as ex:
                print("Error while trying to execute query: {0}".format(ex))

    def readEmpresaByIdDAO(self, id_empresa):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT * FROM empresas WHERE id_empresa = {0}".format(id_empresa))
                result = cursor.fetchall()
                return result
            except Error as ex:
                print("Error while trying to execute query: {0}".format(ex))

    def createEmpresaDAO(self, empresa):
        print(empresa)
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                query = "INSERT INTO empresas (nombre) VALUES ('{0}')"
                cursor.execute(query.format(empresa))
                self.connection.commit()
                print("Empresa created succesfully!\n")
            except Error as ex:
                print("Error while trying to execute query: {0}".format(ex))  

    def deleteEmpresaDAO(self, idToDelete):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                query1 = "DELETE FROM empresas WHERE id_empresa = {0}"
                cursor.execute(query1.format(idToDelete))
                query2 = "DELETE FROM plantas WHERE id_empresa = {0}"
                cursor.execute(query2.format(idToDelete))
                self.connection.commit()
                print("Empresa deleted succesfully!\n")
            except Error as ex:
                print("Error while trying to execute query: {0}".format(ex))

    def updateEmpresaDAO(self, empresa):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                query = "UPDATE empresas SET nombre = '{0}' WHERE id_empresa = {1}"
                cursor.execute(query.format(empresa[1], empresa[0]))
                self.connection.commit()
                print("Empresa updated succesfully!\n")
            except Error as ex:
                print("Error while trying to execute query: {0}".format(ex))

    def createPlantaDAO(self, planta):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                query = "INSERT INTO plantas (nombre, nit, ubicacion, id_empresa, tipo, clasificacion) VALUES ('{0}', '{1}', '{2}', {3}, {4}, {5})"
                cursor.execute(query.format(planta[0], planta[1], planta[2], planta[3], planta[4], planta[5]))
                self.connection.commit()
                print("Planta created succesfully!\n")
            except Error as ex:
                print("Error while trying to execute query: {0}".format(ex))

    def readPlantasByEmpresaDAO(self, id_empresa):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                query = "SELECT * FROM plantas WHERE id_empresa = {0} ORDER BY id_planta ASC"
                cursor.execute(query.format(id_empresa))
                result = cursor.fetchall()
                return result
            except Error as ex:
                print("Error while trying to execute query: {0}".format(ex))

    def deletePlantaByEmpresaDAO(self, id_planta):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                query1 = "DELETE FROM plantas WHERE id_planta = {0}"
                cursor.execute(query1.format(id_planta))
                query2 = "DELETE FROM contactos WHERE id_planta = {0}"
                cursor.execute(query2.format(id_planta))
                self.connection.commit()
                print("Planta deleted succesfully!\n")
            except Error as ex:
                print("Error while trying to execute query: {0}".format(ex))

    def updatePlantaByEmpresaDAO(self, planta, id_planta):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                query = "UPDATE plantas SET nombre = '{0}', nit = '{1}', ubicacion = '{2}', id_empresa = {3}, tipo = {4}, clasificacion = {5} WHERE id_planta = '{6}'"
                cursor.execute(query.format(planta[0], planta[1], planta[2], planta[3], planta[4], planta[5], id_planta))
                self.connection.commit()
                print("Planta updated succesfully!\n")
            except Error as ex:
                print("Error while trying to execute query: {0}".format(ex))

    def createContactoDAO(self, contacto):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                query = "INSERT INTO contactos (nombre, email, cargo, telefono, id_planta) VALUES ('{0}', '{1}', {2}, '{3}', {4})"
                cursor.execute(query.format(contacto[0], contacto[1], contacto[2], contacto[3], contacto[4]))
                self.connection.commit()
                print("Contacto created succesfully!\n")
            except Error as ex:
                print("Error while trying to execute query: {0}".format(ex))

    def readContactosByPlantaDAO(self, id_planta):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                query = "SELECT * FROM contactos WHERE id_planta = {0} ORDER BY id_contacto ASC"
                cursor.execute(query.format(id_planta))
                result = cursor.fetchall()
                return result
            except Error as ex:
                print("Error while trying to execute query: {0}".format(ex))

    def readPlantaByIdDAO(self, id_empresa):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT * FROM plantas WHERE id_empresa = {0}".format(id_empresa))
                result = cursor.fetchall()
                return result
            except Error as ex:
                print("Error while trying to execute query: {0}".format(ex))

    def updateContactoDAO(self, contacto, id_contacto):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                query = "UPDATE contactos SET nombre = '{0}', email = '{1}', cargo = '{2}', telefono = '{3}', id_planta = '{4}' WHERE id_contacto = '{5}'"
                cursor.execute(query.format(contacto[0], contacto[1], contacto[2], contacto[3], contacto[4], id_contacto))
                self.connection.commit()
                print("Contacto updated succesfully!\n")
            except Error as ex:
                print("Error while trying to execute query: {0}".format(ex))

    def deleteContactoDAO(self, id_contacto):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                query = "DELETE FROM contactos WHERE id_contacto = {0}"
                cursor.execute(query.format(id_contacto))
                self.connection.commit()
                print("Contacto deleted succesfully!\n")
            except Error as ex:
                print("Error while trying to execute query: {0}".format(ex))

                               
