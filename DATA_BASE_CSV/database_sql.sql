#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------

#------------------------------------------------------------
# Table: Puissance
#------------------------------------------------------------


CREATE TABLE IF NOT EXISTS  Puissance(
        ID_Puissance    INT NOT NULL ,
        Puissance_max   Int ,
        Puissance_admin Int ,
        Boite_vitesse   Varchar (3)  ,
        Masse           Int 
	,CONSTRAINT Puissance_PK PRIMARY KEY (ID_Puissance)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Consommation
#------------------------------------------------------------


CREATE TABLE IF NOT EXISTS   Consommation(
        ID_Consommation        Int NOT NULL ,
        Conso_urb   Double ,
        Conso_exurb Double ,
        Conso_mixte Double 
	,CONSTRAINT Consommation_PK PRIMARY KEY (ID_Consommation)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Emmissions
#------------------------------------------------------------


CREATE TABLE IF NOT EXISTS   Emmissions(
        ID_Emmissions  Int NOT NULL ,
        Co2        Double ,
        CO         Double ,
        HC         Double ,
        NOx        Double ,
        HC_NOX     Double ,
        Particules Double 
	,CONSTRAINT Emmissions_PK PRIMARY KEY (ID_Emmissions)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Carrosserie
#------------------------------------------------------------



CREATE TABLE IF NOT EXISTS  Carrosserie(
        ID_Carrosserie Int NOT NULL ,
        Carrosserie    Varchar (19) NOT NULL
	,CONSTRAINT Carrosserie_PK PRIMARY KEY (ID_Carrosserie)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Energie
#------------------------------------------------------------

CREATE TABLE IF NOT EXISTS  Energie(
        ID_Energie Int NOT NULL ,
        Carburant  Varchar (10) NOT NULL ,
        Hybride    Bool NOT NULL
	,CONSTRAINT Energie_PK PRIMARY KEY (ID_Energie)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Gamme
#------------------------------------------------------------


CREATE TABLE IF NOT EXISTS   Gamme(
        ID_Gamme Int NOT NULL ,
        Gamme    Varchar (14) NOT NULL
	,CONSTRAINT Gamme_PK PRIMARY KEY (ID_Gamme)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Marque
#------------------------------------------------------------


CREATE TABLE IF NOT EXISTS   Marque(
        ID_Marque  Int NOT NULL ,
        Marque     Varchar (12) NOT NULL ,
        Modele_com Varchar (20) NOT NULL ,
        Designation_com Varchar (91) 
	,CONSTRAINT Marque_PK PRIMARY KEY (ID_Marque)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Voiture
#------------------------------------------------------------


CREATE TABLE IF NOT EXISTS  Voiture(
        Cnit            Varchar (15) NOT NULL ,
        ID_Gamme        Int NOT NULL ,
        ID_Carrosserie  Int NOT NULL ,
        ID_Energie      Int NOT NULL ,
        ID_Marque       Int NOT NULL ,
        ID_Emmissions   Int NOT NULL ,
        ID_Puissance   Int NOT NULL ,
        ID_Consommation   Int NOT NULL
        
	,CONSTRAINT Voiture_PK PRIMARY KEY (Cnit)

	,CONSTRAINT Voiture_Gamme_FK FOREIGN KEY (ID_Gamme) REFERENCES Gamme(ID_Gamme)
	,CONSTRAINT Voiture_Carrosserie_FK FOREIGN KEY (ID_Carrosserie) REFERENCES Carrosserie(ID_Carrosserie)
	,CONSTRAINT Voiture_Energie_FK FOREIGN KEY (ID_Energie) REFERENCES Energie(ID_Energie)
	,CONSTRAINT Voiture_Marque_FK FOREIGN KEY (ID_Marque) REFERENCES Marque(ID_Marque)
    ,CONSTRAINT Voiture_Emmissions_FK FOREIGN KEY (ID_Emmissions) REFERENCES Emmissions(ID_Emmissions)
    ,CONSTRAINT Voiture_Puissance_FK FOREIGN KEY (ID_Puissance) REFERENCES Puissance(ID_Puissance)
    ,CONSTRAINT Voiture_Consommation_FK FOREIGN KEY (ID_Consommation) REFERENCES Consommation(ID_Consommation)
)ENGINE=InnoDB;
