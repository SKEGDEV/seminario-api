from src.DB.database_init import mysql

class obj_client():
    def create_new_client(
            self,
            references,
            dpi:int,
            first_name:str,
            last_name:str,
            work_phone:int,
            home_phone:int,
            personal_phone:int,
            other_phone:int,
            isMarried:bool,
            isRented:bool,
            work_direction:str,
            home_direction:str,
            email:str,
            facebook:str,
            photo_Base64:str,
            user_id:int
            ): 
        print(isMarried)
        try:
            connect = mysql.connect()
            query = connect.cursor()
            sp_execute = query.execute('CALL create_Client(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                dpi,
                first_name,
                last_name,
                work_phone,
                home_phone, 
                personal_phone,
                other_phone,
                isMarried,
                isRented,
                work_direction,
                home_direction,
                email,
                facebook,
                photo_Base64,
                user_id
                ))
            get_id = query.fetchall()
            connect.commit()
            id_client =0
            for d in get_id:
                id_client = d[0]
            for d in references:
                self.create_reference(id_client,d["first_name"],d["last_name"],d["phone"]) 
            if(sp_execute>0):
                return{"msm":"Se ha insertado con exito el nuevo cliente"}
            return{"msm":"Por razones desconocidas no se ha podido ingresar el cliente"}
        except Exception as e:
            print(e)
            return{"err":str(e)}

    def create_reference(self, client_id:int, firstname:str, lastname:str, phone:int):
        try:
            connect = mysql.connect()
            query = connect.cursor()
            query.execute('CALL create_reference(%s,%s,%s,%s)',(firstname,lastname,phone,client_id))
            connect.commit()
        except Exception as e:
            print(e)

    def get_all_clients(self, user_id:int):
        try:
            connect = mysql.connect()
            query = connect.cursor()
            query.execute('CALL get_clients(%s)',(user_id))
            users = query.fetchall()
            connect.commit()
            if(len(users)>0):
                return{"msm":("Clientes encontrados: "+str(len(users))), "data":users}
            return{"msm":"Aun no ha registrado ningun cliente"}
        except Exception as e:
            return{"err":str(e)}
            
    def get_client_header(self, client_id:int):
        try:
            connect = mysql.connect()
            query = connect.cursor()
            query.execute('CALL get_client_header(%s)',(client_id))
            header = query.fetchall()
            connect.commit() 
            return header
        except:
            return []

    def get_client_contact(self, client_id:int):
        try:
            connect = mysql.connect()
            query = connect.cursor()
            query.execute('CALL get_client_contact(%s)', (client_id))
            contact = query.fetchall()
            connect.commit()
            return contact
        except:
            return []
    
    def get_references(self, client_id:int):
        try:
            connect = mysql.connect()
            query = connect.cursor()
            query.execute('CALL get_references(%s)',(client_id))
            references = query.fetchall()
            connect.commit()
            return references
        except:
            return []

    def get_client_footer(self, client_id:int):
        try:
            connect = mysql.connect()
            query = connect.cursor()
            query.execute('CALL get_client_footer(%s)',(client_id))
            footer= query.fetchall()
            connect.commit()
            return footer
        except:
            return []
    def get_loans_client(self, client_id:int):
        try:
            connect = mysql.connect()
            query = connect.cursor()
            query.execute('CALL get_loans(%s)',(client_id))
            loans = query.fetchall()
            connect.commit()
            return loans
        except:
            return[]

    def get_client_record(self, client_id:int):
        try:
            return {
                    "msm":"Cliente encontrado",
                    "header":self.get_client_header(client_id),
                    "contact":self.get_client_contact(client_id),
                    "footer":self.get_client_footer(client_id),
                    "references":self.get_references(client_id),
                    "loans":self.get_loans_client(client_id)
                    }
        except Exception as e:
            return {"err": str(e)}

