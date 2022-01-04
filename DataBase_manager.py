import pandas as pd
import mysql.connector;
import numpy as np
from sqlalchemy import create_engine


class database:
    def __init__(self) -> None:
        self.db=None
        self.engine=None


    def connect(self,user,password,host="localhost"):

        try: #connexion
            mydb = mysql.connector.connect(
                                        host=host,
                                        user=str(user),
                                        passwd=str(password),
                                        #database="Vehicule_CO2_Emmission",
                                        auth_plugin="mysql_native_password"
                                        )
            self.db=mydb
            
        except:
            print("échec de connexion")
            return None

    


    def createDatabase(self,database_name,sql_file="./DATA_BASE_CSV/database_sql.sql"):

        mycursor=self.db.cursor()

        print("début creation")

        #-create database-------------------------------------------------------
        """command=f'''DROP SCHEMA IF EXISTS {database_name};'''
        mycursor.execute(command)
        self.db.commit()"""

        #print("fin drop")
        #-create database-------------------------------------------------------
        command=f'''CREATE DATABASE IF NOT EXISTS {database_name};'''
        mycursor.execute(command)
        self.db.commit()

        print("use database")
        command=f'''USE {database_name} ;''' 
        mycursor.execute(command)
        self.db.commit()
     
        #--create tables--------------------------------------------------
        with open(sql_file, 'r') as sql_file:
            result_iterator = mycursor.execute(sql_file.read(), multi=True)
            for res in result_iterator:
                print("Running query: ", res)  # Will print out a short representation of the query
                print(f"Affected {res.rowcount} rows" )
            self.db.commit() 
        print("fin de création")

    def useDataBase(self,database_name):
        mycursor=self.db.cursor()
        command=f'''USE {database_name} ;''' 
        mycursor.execute(command)
        self.db.commit()

    
    def isExistsDataBase(self,name):
        return pd.read_sql_query('''SHOW DATABASES LIKE 'co2';''',self.db).count()[0]

    
    def getData(self,database_name,params_con_server):
        # Create SQLAlchemy engine to connect to MySQL Database
        self.engine= create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                        .format(host=params_con_server['host'], db=database_name, user=params_con_server['user'], pw=params_con_server['password']))
        # fill marque :
        print("fill marque")
        count_marque=np.array(pd.read_sql_query('select count(*) as count from Marque;',self.db))[0][0]
        if count_marque==0:
            df_marque=pd.read_csv("./DATA_BASE_CSV/Marque.csv")
            self.addDataToTable("Marque",df_marque)
            print("marque remplie avec succès. ")


        # fill Gamme :
        print("fill gamme")
        count_gamme=np.array(pd.read_sql_query('select count(*) as count from Gamme;',self.db))[0][0]
        if count_gamme==0:
            df_gamme=pd.read_csv("./DATA_BASE_CSV/Gamme.csv")
            self.addDataToTable("Gamme",df_gamme)
            print("gamme remplie avec succès. ")

        # fill Energie :
        print("fill energie")
        count_energie=np.array(pd.read_sql_query('select count(*) as count from Energie;',self.db))[0][0]
        if count_energie==0:
            df_energie=pd.read_csv("./DATA_BASE_CSV/Energie.csv")
            self.addDataToTable("Energie",df_energie)
            print("energie remplie avec succès. ")

        # fill Consommation :
        print("fill Consommation")
        count_consommation=np.array(pd.read_sql_query('select count(*) as count from Consommation;',self.db))[0][0]
        if count_consommation==0:
            df_Consommation=pd.read_csv("./DATA_BASE_CSV/Consommation.csv")
            self.addDataToTable("Consommation",df_Consommation)
            print("consommation remplie avec succès. ")

        # fill Puissance :
        print("fill Puissance")
        count_puissance=np.array(pd.read_sql_query('select count(*) as count from Puissance;',self.db))[0][0]
        if count_puissance==0:
            df_Puissance=pd.read_csv("./DATA_BASE_CSV/Puissance.csv")
            self.addDataToTable("Puissance",df_Puissance)
            print("puissance remplie avec succès. ")

        #fill Emmissions :
        print("fill Emmissions")
        count_emmissions=np.array(pd.read_sql_query('select count(*) as count from Emmissions;',self.db))[0][0]
        if count_emmissions==0:
            df_Emmissions=pd.read_csv("./DATA_BASE_CSV/Emmissions.csv")
            self.addDataToTable("Emmissions",df_Emmissions)
            print("emmissions remplie avec succès. ")

        #fill Carrosserie :
        print("fill Carrosserie")
        count_carrosserie=np.array(pd.read_sql_query('select count(*) as count from Carrosserie;',self.db))[0][0]
        if count_carrosserie==0:
            df_Carrosserie=pd.read_csv("./DATA_BASE_CSV/Carrosserie.csv")
            self.addDataToTable("Carrosserie",df_Carrosserie)
            print("carrosserie remplie avec succès. ")

        #fill Voiture :
        print("fill Voiture")
        count_voiture=np.array(pd.read_sql_query('select count(*) as count from Voiture;',self.db))[0][0]
        if count_voiture==0:
            df_Voiture=pd.read_csv("./DATA_BASE_CSV/Voiture.csv")
            self.addDataToTable("Voiture",df_Voiture)
            print("voiture remplie avec succès. ")



    def clearTable(self,table_name: str):
        mycursor=self.db.cursor()
        command=f'''delete from {table_name}'''
        print(command)
        mycursor.execute(command)
        self.db.commit()
        

    def addDataToTable(self,table_name: str, data: pd.DataFrame):
        mycursor = self.db.cursor()
        data=data.replace("",0)
        
        #------------------------------
        # table marque:
        #------------------------------
        
        if table_name=="Marque":
            #data=data.set_index([pd.Index([i for i in range(data.shape[0])])])
            try:
                for i in data.index.to_list():
                    marque=data.loc[i,"Marque"]
                    Modele_com=data.loc[i,"Modele_com"]
                    Designation_com=data.loc[i,"Designation_com"]

                    command=f'''insert into Marque(ID_Marque,Marque,Modele_com, Designation_com) Values({i},"{marque}","{Modele_com}","{Designation_com}")'''

                    mycursor.execute(command)
                    self.db.commit()
                
                mycursor.close() 
            except:
                print("error table Marque ou  déjà complétée")
                
                
        #------------------------------
        # table Gamme:
        #------------------------------
        elif table_name=="Gamme":
            #data=data.set_index([pd.Index([i for i in range(data.shape[0])])])
            try:
                for i in data.index.to_list():
                    gamme=data.loc[i,"Gamme"].replace('\n','')

                    command=f'''insert into Gamme(ID_Gamme,Gamme) Values({i},"{gamme}")'''

                    mycursor.execute(command)
                    self.db.commit()

                mycursor.close()  
            except:
                print("error table Gamme ou  déjà complétée")
                
        #------------------------------
        # table Energie:
        #------------------------------
        elif table_name=="Energie":
            #hybride_dict={"non":0,"oui":1}
            #data=data.set_index([pd.Index([i for i in range(data.shape[0])])])
            try:
                for i in data.index.to_list():
                    Carburant=data.loc[i,"Carburant"]
                    Hybride=data.loc[i,"Hybride"]

                    command=f'''insert into Energie(ID_Energie,Carburant, Hybride) Values({i},"{Carburant}","{Hybride}")'''
                
                    mycursor.execute(command)
                    self.db.commit()
                    
                mycursor.close() 
            except:
                print("error table Energie ou  déjà complétée")
            
            
        #------------------------------------------------------------
        # Table: Consommation
        #------------------------------------------------------------
        elif table_name=="Consommation":
            #data=data.set_index([pd.Index([i for i in range(data.shape[0])])])
            try:
                for i in data.index.to_list():
                    Conso_urb=data.loc[i,"Conso_urb"]
                    Conso_exurb=data.loc[i,"Conso_exurb"]
                    Conso_mixte=data.loc[i,"Conso_mixte"]
                    
                    
                    command=f'''insert into Consommation(ID_Consommation,Conso_urb, Conso_exurb, Conso_mixte) Values({i},{Conso_urb},{Conso_exurb},{Conso_mixte})'''
                    
                    mycursor.execute(command)
                    self.db.commit()
                    
                mycursor.close() 
            except:
                print("error table Consommation ou  déjà complétée")
        
        #------------------------------
        # table Puissance:
        #------------------------------
        elif table_name=="Puissance":
            #data=data.set_index([pd.Index([i for i in range(data.shape[0])])])
            try:
                for i in data.index.to_list():
                    Puissance_max=data.loc[i,"Puissance_max"]
                    Puissance_admin=data.loc[i,"Puissance_admin"]
                    Boite_vitesse=data.loc[i,"Boite_vitesse"]
                    Masse=data.loc[i,"Masse"]

                    command=f'''insert into Puissance(ID_Puissance,Puissance_max, Puissance_admin, Boite_vitesse, Masse) Values({i},{Puissance_max},{Puissance_admin},'{Boite_vitesse}',{Masse})'''         

                    mycursor.execute(command)
                    self.db.commit()

                mycursor.close() 
            except:
                print("error table Puissance ou  déjà complétée")
                

        
        #------------------------------------------------------------
        # Table: Emmissions
        #------------------------------------------------------------
        elif table_name=="Emmissions":
            #data=data.set_index([pd.Index([i for i in range(data.shape[0])])])
            try:
                for i in data.index.to_list():
                    Co2=data.loc[i,"Co2"]
                    CO=data.loc[i,"CO"]
                    HC=data.loc[i,"HC"]
                    NOx=data.loc[i,"NOx"]
                    HC_NOX=data.loc[i,"HC_NOX"]
                    Particules=data.loc[i,"Particules"]
                    
                    command=f'''insert into Emmissions(ID_Emmissions,Co2, CO, HC, NOx, HC_NOX,Particules ) Values({i},{Co2},{CO},{HC},{NOx},{HC_NOX},{Particules})'''
                
                    mycursor.execute(command)
                    self.db.commit()
                    
                mycursor.close()     
            except:
                print("error table Emmissions ou  déjà complétée")
        
        #------------------------------------------------------------
        # Table: Carrosserie
        #------------------------------------------------------------
        elif table_name=="Carrosserie":
            #data=data.set_index([pd.Index([i for i in range(data.shape[0])])])
            try:
                for i in data.index.to_list():
                    Carrosserie=data.loc[i,"Carrosserie"]
                    command=f'''insert into Carrosserie(ID_Carrosserie,Carrosserie) Values({i},"{Carrosserie}")'''
                    mycursor.execute(command)
                    
                    self.db.commit()
                
                mycursor.close()     
            except:
                print("error table Carrosserie ou  déjà complétée")
                
        #------------------------------------------------------------
        # Table: Voiture
        #------------------------------------------------------------
        elif table_name=="Voiture":
            #data=data.set_index([pd.Index([i for i in range(data.shape[0])])])
            try:
                for i in data.index.to_list():
                    Cnit=data.loc[i,"Cnit"]
                    ID_Gamme=data.loc[i,"ID_Gamme"]
                    ID_Carrosserie=data.loc[i,"ID_Carrosserie"]
                    ID_Energie=data.loc[i,"ID_Energie"]
                    ID_Marque=data.loc[i,"ID_Marque"]
                    ID_Emmissions=data.loc[i,"ID_Emmissions"]
                    ID_Puissance=data.loc[i,"ID_Puissance"]
                    ID_Consommation=data.loc[i,"ID_Consommation"]
                    
                    command=f'''insert into Voiture(Cnit,ID_Gamme, ID_Carrosserie, ID_Energie, ID_Marque, ID_Emmissions,ID_Puissance,ID_Consommation ) Values("{Cnit}",{ID_Gamme},{ID_Carrosserie},{ID_Energie},{ID_Marque},{ID_Emmissions},{ID_Puissance},{ID_Consommation})'''
                    
                    mycursor.execute(command)
                    self.db.commit()

                mycursor.close() 
            except:
                print("error table Voiture ou  déjà complétée")


    def getMarque(self,column,condition=""):
        if condition!="":
            param_dict={"Modele_com":"Marque","Designation_com":"Modele_com"}
            where=f" where {param_dict[column]}='{condition}' "
            command=f'''select  distinct {column} from Marque {where};'''
            print(column,command)
            return pd.read_sql_query(command,self.db)

        else:
            command=f'''select distinct {column} from Marque;'''
            print(column,command)
            return pd.read_sql_query(command,self.db)

    def getDataFrameMaque(self,database_name,marque,modele_com,Designation_com):
        return pd.read_sql_query(f'''select * from {database_name} where (Marque='{marque}' and Modele_com='{modele_com}' and Designation_com='{Designation_com}'  );''',self.db)

    def getDataFrameCnit(self,cnit):
        return pd.read_sql_query(f'''select * from Voiture where  Cnit='{cnit}' ;''',self.db)
