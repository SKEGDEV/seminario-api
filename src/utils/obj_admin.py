from src.DB.database_init import mysql

class admin:
    def get_all_users(self):
        try:
            connect = mysql.connect()
            query = connect.cursor()
            query.execute('CALL get_user_list(%s)',(1))
            users = query.fetchall()
            connect.commit()
            if(len(users)>0):
                return{"msm":("Usuarios activos encontrados: "+str(len(users))), "data":users}
            return{"msm":"Ningun usuario ha sido encontrado, es raro que vea este mensaje puesto que nadie puede acceder"}
        except Exception as e:
            return {"msm":"ha ocurrido un error", "err":str(e)}
    
    def get_user_record(self, user_id:int):
        try:
            connect = mysql.connect()
            query = connect.cursor()
            query.execute('CALL get_user_record(%s)',(user_id))
            user = query.fetchall()
            connect.commit()
            if(len(user)>0):
                return {"msm":"usuario encontrado con exito", "user":user}
            return{"msm":"El usuario no se ha podido encontrar"}
        except Exception as e:
            return {"err": str(e)}

    def get_user_update(self, user_id:int):
        try:
            connect = mysql.connect()
            query = connect.cursor()
            query.execute('CALL get_user_update(%s)',(user_id))
            user = query.fetchall()
            connect.commit()
            if(len(user)>0):
                return {"msm":"usuario encontrado con exito", "user":user}
            return{"msm":"El usuario no se ha podido encontrar"}
        except Exception as e:
            return {"err": str(e)}


    def disable_user(self, user_id:int):
        try:
            connect = mysql.connect()
            query = connect.cursor()
            sp_execute = query.execute('CALL disable_user(%s, %s)',(1,user_id))
            connect.commit()
            if(sp_execute>0):
                return{"msm":"Se ha inhabilitado el usuario correctamente"}
            return{"msm":"Por razones de base de datos el usuario no se ha podido inhabilitar"}
        except Exception as e:
            return{"err":str(e)}

    def get_users_disable(self):
        try:
            connect = mysql.connect()
            query = connect.cursor()
            query.execute('CALL get_user_list(%s)',(2))
            users = query.fetchall()
            connect.commit()
            if(len(users)>0):
                return{"msm":("Usuarios desactivados encontrados: "+str(len(users))), "data":users}
            return{"msm":"Ningun usuario ha sido desactivado"}
        except Exception as e:
            return {"msm":"ha ocurrido un error", "err":str(e)}

    def enable_user(self, user_id):
        try:
            connect = mysql.connect()
            query = connect.cursor()
            sp_execute = query.execute('CALL disable_user(%s, %s)',(2,user_id))
            connect.commit()
            if(sp_execute>0):
                return{"msm":"Se ha habilitado el usuario correctamente"}
            return{"msm":"Por razones de base de datos el usuario no se ha podido habilitar"}
        except Exception as e:
            return{"err":str(e)}

