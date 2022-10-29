from datetime import datetime
from src.DB.database_init import mysql
from src.utils.obj_loan import obj_loan

class obj_payment(obj_loan):

    def get_payment_info(self, loan_id:int):
        try:
            connect = mysql.connect()
            query = connect.cursor()
            query.execute("CALL get_loan_to_pay(%s)",(loan_id))
            payment = query.fetchall() 
            connect.commit()
            if(len(payment)>0):
                return {"msm":"Prestamo encontrado con exito", "data":payment}
            return {"msm":"No hemos encontrado el prestamo solicitado"}
        except Exception as e:
            return {"err":str(e)}

    def create_payment(self, 
             loan_id:int,
             client_id:int,
             loan_quote:float,
             loan_amount:float,
             loan_interest_value:float,
             loan_interest_type:int,
             loan_payment_date:str,
             loan_period:str
             ):
        payment_date = datetime.strptime(loan_payment_date,'%Y-%m-%d')
        payment_date = self.get_next_date(loan_period, payment_date)
        try:
            connect = mysql.connect()
            query = connect.cursor()
            exec_sp = query.execute("CALL create_payment(%s,%s,%s,%s,%s,%s,%s)",(
                 loan_id,
                 client_id,
                 loan_quote,
                 loan_amount,
                 loan_interest_value,
                 loan_interest_type,
                 payment_date
                ))
            connect.commit()
            if(exec_sp>0):
                return{"msm":"Pago realizado con exito"}
            return {"msm":"El pago no se pudo realizar por problemas internos de base de datos"}
        except Exception as e:
            return {"err":str(e)}

