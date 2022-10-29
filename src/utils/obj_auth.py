from src.DB.database_init import mysql
from src.auth.obj_password import Password
from src.auth.obj_token import token

class obj_auth():

    def get_token(self, user_id:int):
        try:
            connect = mysql.connect()
            query = connect.cursor()
            query.execute('CALL get_UserToken(%s)',(user_id))
            data = query.fetchall()
            connect.commit() 
            if(len(data)>0):
                first_name = ""
                rol = ""
                token_data={}
                for d in data:
                    token_data={
                            "id":d[0]
                            }
                    first_name = d[1]
                    rol = d[2]
                return{
                        "firstname":first_name,
                        "rol":rol,
                        "token":token().generate_token(token_data)
                        }
            return{
                     "msm":"no se encontro informacion del usuario"
                     }
                
        except Exception as e:
            return{"msm":"un error ha ocurrido", "err":str(e)}


    def get_user(self, user_session_name:str, user_password:str):
        try:
            connect = mysql.connect()
            query = connect.cursor()
            query.execute('CALL get_User(%s)', (user_session_name))
            user = query.fetchall()
            connect.commit()
            if(len(user)>0):
                password_DB = ""
                user_id = 0
                for data in user: 
                    password_DB = data[0]
                    user_id = data[1]
                if Password().match_password(password_DB, user_password):
                    return self.get_token(user_id)
                return {"msm":"el usuario/contrasena son inconrrectos"}
            return{"msm":"el usuario/contrasena son inconrrectos"}
        except Exception as e:
            return{
                    "msm":"Un error ha ocurrido",
                    "err":str(e)
                    }

    def create_User(self, user_session_name:str, user_password:str, user_first_name:str, user_last_name:str, user_birthday:str,
            user_email:str, user_phone:int, user_nit:int, user_rol:int):
        try:
            connect = mysql.connect()
            query = connect.cursor()
            exec_sp = query.execute('CALL create_User(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                user_session_name,
                Password().create_password(user_password),
                user_first_name,
                user_last_name,
                user_birthday,
                user_email,
                user_phone,
                user_nit,
                user_rol
                ))
            connect.commit() 
            if(exec_sp>0):
                return{"msm":"El usuario ha sido coreado con exito"}
            return {"msm":"Por eventos externos el usuario no ha podido ser creado"}
        except Exception as e:
            return{"msm":"un error ha ocurrido","err":str(e)}

    def update_user(self, id_user:int, user_session_name:str, user_password:str, user_first_name:str, user_last_name:str, user_birthday:str,
            user_email:str, user_phone:int, user_nit:int, user_rol:int):
        type_update = 0
        if(user_password == "no password update"):
            type_update = 2 
        else:
            type_update=1
        try:
            connect = mysql.connect()
            query = connect.cursor() 
            exec_sp = query.execute('CALL update_user(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',( 
                type_update,
                id_user,
                user_session_name,
                Password().create_password(user_password),
                user_first_name,
                user_last_name,
                user_birthday,
                user_email,
                user_phone,
                user_nit,
                user_rol
                ))
            connect.commit() 
            if(exec_sp>0):
                return{"msm":"El usuario ha sido actualizado con exito"}
            return {"msm":"Por eventos externos el usuario no ha podido ser creado"}
        except Exception as e:
            print(e);
            return{"msm":"un error ha ocurrido","err":str(e)}

    def authorize_user(self, user_session_name:str, user_password:str):
        try:
            connect = mysql.connect()
            query = connect.cursor()
            query.execute('CALL get_User(%s)', (user_session_name))
            user = query.fetchall()
            connect.commit()
            if(len(user)>0):
                password_DB = "" 
                for data in user: 
                    password_DB = data[0] 
                if Password().match_password(password_DB, user_password):
                    return {"msm":"Usuario autorizado correctamente", "isAuth":"Yes"}
                return {"msm":"la contrasena son inconrrectos", "isAuth":"No"}
            return{"msm":"la contrasena son inconrrectos", "isAuth":"No"}
        except Exception as e:
            print(e);
            return{
                    "msm":"Un error ha ocurrido",
                    "err":str(e)
                    }

