import pickle
from server import *

# run this file to reset default server object

choice = input("CAUTION: \nThis will overwrite the existing default.dat file so all information stored there cannot be retrieved. Do you still wish to proceed? (Y/N)")

if choice.lower() == 'y':
    print("Reconfiguring defualt.dat")
    #setting default server ID to none  
    default = Server(None)
    serverConfigs = {'default':default}

    with open("serverConfig.dat", "wb") as file:
        pickle.dump(serverConfigs, file)

    with open("serverConfig.dat", "rb") as file:
        guilds = pickle.load(file)
        print(serverConfigs)

else:
    print("Reconfiguration aborted")
