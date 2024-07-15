from conn import DataAccessObject

dao = DataAccessObject()

def readEmpresasFunc(allEmpresas):
    print("\nEmpresas:")
    for emp in allEmpresas:
        data = "id. {0} | Name: {1}"
        print(data.format(emp[0], emp[1]))
    print("")

def getEmpresaInfoFunc():
    print("Create an Empresa")
    name = str(input("Enter empresa name: "))
    empresa = name
    return empresa

def getEmpresaIdDeleteFunc(allEmpresas):
    readEmpresasFunc(allEmpresas)
    idExists = False
    idToDelete = int(input("Enter the id of the Planta you want to delete: "))
    for emp in allEmpresas:
        if emp[0] == idToDelete:
            idExists = True
            break

    if not idExists:
        idToDelete = ""

    return idToDelete

def getEmpresaIdUpdateFunc(allEmpresas):
    readEmpresasFunc(allEmpresas)
    idExists = False
    idToUpdate = int(input("Enter the id of the Empresa to update: "))
    for emp in allEmpresas:
        if emp[0] == idToUpdate:
            idExists = True
            break

    if idExists:
        name = str(input("Enter new empresa name: "))
        empresa = (idToUpdate, name)
    else: 
        empresa = None
    
    return empresa

def getPlantaInfoFunc(allEmpresas):
    readEmpresasFunc(allEmpresas)
    idExists = False
    idToCreate = int(input("Enter the id of the Empresa you want to create a planta for: "))
    for emp in allEmpresas:
        if emp[0] == idToCreate:
           idExists = True
           break
    
    if idExists:
        name = str(input("Enter planta name: "))
        nit = str(input("Enter planta NIT: "))
        ubicacion = str(input("Enter planta location: "))
        id_empresa = idToCreate
        tipo = int(input("Enter planta type: "))
        clasificacion = int(input("Enter planta class: "))
        planta = (name,nit,ubicacion,id_empresa,tipo,clasificacion)
    else: 
        planta = None

    return planta

def readPlantasFunc(allPlantas, id_empresa):
    print("\nPlantas:")
    empresa = dao.readEmpresaByIdDAO(id_empresa)
    for planta in allPlantas:
        data = "id. {0} | Name: {1}, NIT: {2}, Location: {3}, Empresa: {4}, Type: {5}, Class: {6}"
        print(data.format(planta[0], planta[1], planta[2], planta[3], empresa[0][1], planta[5], planta[6]))
    print("")

def updatePlantaByIdFunc(allPlantas, id_empresa,id_planta):
    for plant in allPlantas:
        if plant[0] == id_planta:
            name = str(input("Enter new planta name: "))
            nit = str(input("Enter new planta NIT: "))
            ubicacion = str(input("Enter new planta location: "))
            id_empresa = id_empresa
            tipo = int(input("Enter new planta type: "))
            clasificacion = int(input("Enter new planta class: "))
            planta = (name, nit, ubicacion, id_empresa, tipo, clasificacion)
            return planta
    return None

def deletePlantaByEmpresaFunc(allPlantas, id_empresa):
    readPlantasFunc(allPlantas, id_empresa)
    idExists = False
    idToDelete = int(input("Enter the id of the Planta you want to delete: "))
    for planta in allPlantas:
        if planta[0] == idToDelete:
            idExists = True
            break

    if not idExists:
        idToDelete = ""

    return idToDelete

def getContactoInfoFunc(allPlantas, id_empresa):
    readPlantasFunc(allPlantas, id_empresa)
    idExists = False
    idToCreate = int(input("Enter the id of the Planta you want to create a contacto for: "))
    for plant in allPlantas:
        if plant[0] == idToCreate:
           idExists = True
           break
    
    if idExists:
        name = str(input("Enter contacto name: "))
        email = str(input("Enter contacto email: "))
        cargo = str(input("Enter contacto role: "))
        telefono = int(input("Enter contacto phone number: "))
        id_planta = idToCreate
        contacto = (name,email,cargo,telefono,id_planta)
    else: 
        contacto = None

    return contacto

def readContactosFunc(allContactos, id_empresa):
    print("\nContactos:")
    planta = dao.readPlantaByIdDAO(id_empresa)
    for contacto in allContactos:
        data = "id. {0} | Name: {1}, Email: {2}, Role: {3}, Telefono: {4}, Planta: {5} "
        print(data.format(contacto[0], contacto[1], contacto[2], contacto[3], contacto[4], planta[0][1]))
    print("")

def updateContactoByIdFunc(allContactos, id_contacto,id_planta):
    for contacto in allContactos:
        if contacto[0] == id_contacto:
            name = str(input("Enter contacto name: "))
            email = str(input("Enter contacto email: "))
            cargo = str(input("Enter contacto role: "))
            telefono = int(input("Enter contacto phone number: "))
            id_planta = id_planta
            planta = (name, email, cargo, telefono, id_planta)
            return planta
    return None

def deleteContactoByPlantaFunc(allContactos, id_empresa):
    readContactosFunc(allContactos, id_empresa)
    idExists = False
    idToDelete = int(input("Enter the id of the contacto you want to delete: "))
    for contacto in allContactos:
        if contacto[0] == idToDelete:
            idExists = True
            break

    if not idExists:
        idToDelete = ""

    return idToDelete



                    