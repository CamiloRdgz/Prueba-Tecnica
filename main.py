from conn import DataAccessObject
import functions

dao = DataAccessObject()

def MainMenu():
    continueApp = True
    while(continueApp):
        validOption = False
        while(not validOption):
            print("\n=== MAIN MENU ===")
            print("1. Menu Empresas")
            print("2. Menu Plantas")
            print("3. Menu Contactos")
            print("4. Exit App")
            print("===")
            option = int(input("Choose an option: "))
            
            if option < 1 or option > 4:
                print("Invalid option! Choose again...")
            elif option == 4:
                print("Bye! Thanks for using our App...")
                continueApp = False
                break
            else:
                executeOptionMainMenu(option)

def executeOptionMainMenu(option):
    if option == 1:
        MenuEmpresas()
    elif option == 2:
        MenuPlantas()
    elif option == 3:
        MenuContactos()

""" MENU EMPRESA """
def MenuEmpresas():
    continueMenu = True
    while(continueMenu):
        validOption = False
        while(not validOption):
            print("\n=== MENU EMPRESAS ===")
            print("1. Create Empresa")
            print("2. Read Empresas")
            print("3. Update Empresa")
            print("4. Delete Empresa")
            print("5. Back to Main Menu")
            print("===")
            option = int(input("Choose an option: "))
            
            if option < 1 or option > 5:
                print("Invalid option! Choose again...")
            else:
                validOption = True
        
        if option == 1:
            createEmpresa()
        elif option == 2:
            readEmpresas()
        elif option == 3:
            updateEmpresa()
        elif option == 4:
            deleteEmpresa()
        elif option == 5:
            continueMenu = False

""" FUNCTIONS EMPRESA """
def createEmpresa():
    empresa = functions.getEmpresaInfoFunc()
    try:
        dao.createEmpresaDAO(empresa)
    except Exception as e:
        print("An error has occured: ", str(e))

def readEmpresas():
    try:
        allEmpresas = dao.readEmpresasDAO()
        print("Empresas:")
        if len(allEmpresas) > 0:
            functions.readEmpresasFunc(allEmpresas)
        else:
            print("No empresas found!")
    except Exception as e:
        print("An error has occured: ", str(e))


def updateEmpresa():
    try:
        allEmpresas = dao.readEmpresasDAO()
        if len(allEmpresas) > 0:
            empresa = functions.getEmpresaIdUpdateFunc(allEmpresas)
            if empresa:
                dao.updateEmpresaDAO(empresa)
            else:
                print("Empresa id not found!")
        else:
            print("No empresas found!")
    except Exception as e:
        print("An error has occured: ", str(e))

def deleteEmpresa():
    try:
        allEmpresas = dao.readEmpresasDAO()
        if len(allEmpresas) > 0:
            idToDelete = functions.getEmpresaIdDeleteFunc(allEmpresas)
            if not(idToDelete == ""):
                dao.deleteEmpresaDAO(idToDelete)
            else:
                print("Empresa id not found!")
        else:
            print("No empresas found!")
    except Exception as e:
        print("An error has occured: ", str(e))

""" MENU PLANTAS """
def MenuPlantas():
    continueMenu = True
    while(continueMenu):
        validOption = False
        while(not validOption):
            print("\n=== MENU PLANTAS ===")
            print("1. Create Planta for Empresa")
            print("2. Read Plantas by Empresa")
            print("3. Update Planta by Empresa")
            print("4. Delete Planta by Empresa")
            print("5. Back to Main Menu")
            print("===")
            option = int(input("Choose an option: "))
            
            if option < 1 or option > 5:
                print("Invalid option! Choose again...")
            else:
                validOption = True
        
        if option == 1:
            createPlanta()
        elif option == 2:
            readPlantasByEmpresa()
        elif option == 3:
            updatePlantaByEmpresa()
        elif option == 4:
            deletePlantaByEmpresa()
        elif option == 5:
            continueMenu = False

""" FUNCTIONS PLANTA """
def createPlanta():
    try:
        allEmpresas = dao.readEmpresasDAO()
        if len(allEmpresas) > 0:
            planta = functions.getPlantaInfoFunc(allEmpresas)
            if planta:
                dao.createPlantaDAO(planta)
            else:
                print("Planta not created!")
        else:
            print("No empresas found!")
    except Exception as e:
        print("An error has occured: ", str(e))

def readPlantasByEmpresa():
    try:
        allEmpresas = dao.readEmpresasDAO()
        if len(allEmpresas) > 0:
            functions.readEmpresasFunc(allEmpresas)
            id_empresa = int(input("Select an Empresa to see its Plantas: "))
            allPlantas = dao.readPlantasByEmpresaDAO(id_empresa)
            if len(allPlantas) > 0:
                functions.readPlantasFunc(allPlantas, id_empresa)
            else:
                print("No plantas found for this empresa!")
        else:
            print("No empresas found!")
    except Exception as e:
        print("An error has occured: ", str(e))

def updatePlantaByEmpresa():
    try:
        allEmpresas = dao.readEmpresasDAO()
        if len(allEmpresas) > 0:
            functions.readEmpresasFunc(allEmpresas)
            id_empresa = int(input("Select an Empresa to update its Plantas: "))
            allPlantas = dao.readPlantasByEmpresaDAO(id_empresa)
            if len(allPlantas) > 0:
                functions.readPlantasFunc(allPlantas, id_empresa)
                id_planta = int(input("Select a Planta to update: "))
                planta = functions.updatePlantaByIdFunc(allPlantas, id_empresa, id_planta)
                dao.updatePlantaByEmpresaDAO(planta, id_planta)
            else:
                print("No plantas found for this empresa!")
        else: 
            print("No empresas found!")
    except Exception as e:
        print("An error has occured: ", str(e))

def deletePlantaByEmpresa():
    try:
        allEmpresas = dao.readEmpresasDAO()
        if len(allEmpresas) > 0:
            functions.readEmpresasFunc(allEmpresas)
            id_empresa = int(input("Select an Empresa to see its Plantas: "))
            allPlantas = dao.readPlantasByEmpresaDAO(id_empresa)
            if len(allPlantas) > 0:
                id_planta = functions.deletePlantaByEmpresaFunc(allPlantas, id_empresa)
                dao.deletePlantaByEmpresaDAO(id_planta)
            else:
                print("No plantas found for this empresa!")
        else:
            print("No empresas found!")
    except Exception as e:
        print("An error has occured: ", str(e))

""" MENU CONTACTOS """
def MenuContactos():
    continueMenu = True
    while(continueMenu):
        validOption = False
        while(not validOption):
            print("\n=== MENU CONTACTOS ===")
            print("1. Create Contacto for Planta")
            print("2. Read Contactos by Planta")
            print("3. Update Contacto by Planta")
            print("4. Delete Contacto by Planta")
            print("5. Back to Main Menu")
            print("===")
            option = int(input("Choose an option: "))

            if option < 1 or option > 5:
                print("Invalid option! Choose again...")
            else:
                validOption = True
        
        if option == 1:
            createContacto()
        elif option == 2:
            readContactosByPlanta()
        elif option == 3:
            updateContactoByPlanta()
        elif option == 4:
            deleteContactoByPlanta()
        elif option == 5:
            continueMenu = False

""" FUNCTIONS CONTACTOS """
def createContacto():
    try:
        allEmpresas = dao.readEmpresasDAO()
        if len(allEmpresas) > 0:
            functions.readEmpresasFunc(allEmpresas)
            id_empresa = int(input("Select an Empresa to see its Plantas: "))
            allPlantas = dao.readPlantasByEmpresaDAO(id_empresa)
            if len(allPlantas) > 0:
                contacto = functions.getContactoInfoFunc(allPlantas, id_empresa)
                dao.createContactoDAO(contacto)
            else:
                print("No plantas found for this empresa!")
        else:
            print("No empresas found!")
    except Exception as e:
        print("An error has occured: ", str(e))

def readContactosByPlanta():
    try:
        allEmpresas = dao.readEmpresasDAO()
        if len(allEmpresas) > 0:
            functions.readEmpresasFunc(allEmpresas)
            id_empresa = int(input("Select an Empresa to see its Plantas: "))
            allPlantas = dao.readPlantasByEmpresaDAO(id_empresa)
            if len(allPlantas) > 0:
                functions.readPlantasFunc(allPlantas, id_empresa)
                id_planta = int(input("Select a Planta to see its Contactos: "))
                allContactos = dao.readContactosByPlantaDAO(id_planta)
                if len(allContactos) > 0:
                    functions.readContactosFunc(allContactos, id_empresa)
                else:
                    print("No contactos found for this planta!")
            else:
                print("No plantas found for this empresa!")
        else:
            print("No empresas found!")
    except Exception as e:
        print("An error has occured: ", str(e))

def updateContactoByPlanta():
    try:
        allEmpresas = dao.readEmpresasDAO()
        if len(allEmpresas) > 0:
            functions.readEmpresasFunc(allEmpresas)
            id_empresa = int(input("Select an Empresa to see its Plantas: "))
            allPlantas = dao.readPlantasByEmpresaDAO(id_empresa)
            if len(allPlantas) > 0:
                functions.readPlantasFunc(allPlantas, id_empresa)
                id_planta = int(input("Select a Planta to see its Contactos: "))
                allContactos = dao.readContactosByPlantaDAO(id_planta)
                if len(allContactos) > 0:
                    functions.readContactosFunc(allContactos, id_empresa)
                    id_contacto = int(input("Select a Contacto to update: "))
                    contacto = functions.updateContactoByIdFunc(allContactos, id_contacto, id_planta)
                    dao.updateContactoDAO(contacto, id_contacto)
                else:
                    print("No contactos found for this planta!")
            else:
                print("No plantas found for this empresa!")
        else:
            print("No empresas found!")
    except Exception as e:
        print("An error has occured: ", str(e))

def deleteContactoByPlanta():
    try:
        allEmpresas = dao.readEmpresasDAO()
        if len(allEmpresas) > 0:
            functions.readEmpresasFunc(allEmpresas)
            id_empresa = int(input("Select an Empresa to see its Plantas: "))
            allPlantas = dao.readPlantasByEmpresaDAO(id_empresa)
            if len(allPlantas) > 0:
                functions.readPlantasFunc(allPlantas, id_empresa)
                id_planta = int(input("Select a Planta to see its Contactos: "))
                allContactos = dao.readContactosByPlantaDAO(id_planta)
                if len(allContactos) > 0:
                    id_contacto = functions.deleteContactoByPlantaFunc(allContactos, id_empresa)
                    dao.deleteContactoDAO(id_contacto)
                else:
                    print("No contactos found for this planta!")
            else:
                print("No plantas found for this empresa!")
        else:
            print("No empresas found!")
    except Exception as e:
        print("An error has occured: ", str(e))


MainMenu()