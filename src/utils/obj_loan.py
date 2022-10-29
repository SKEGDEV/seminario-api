from datetime import timedelta, datetime
from src.DB.database_init import mysql

class obj_loan:
    def get_next_date(self, payment_frecuency:str, last_date_payment:datetime):
        if(payment_frecuency == 'M'):
            return last_date_payment + timedelta(days=30)
        if(payment_frecuency == 'S'):
            return last_date_payment + timedelta(days=7)
        else:
            return last_date_payment + timedelta(days=15)
    
    def get_total_loan(self, proyection):
        total = 0.0
        for data in proyection:
            total += float(data['quote'])
        return total

    def generate_loan_proyection(
            self,
            init_amount:float,
            quote_amount:float,
            interest:float,
            first_payment_date:str,
            payment_frecuency:str,
            type_interest:int
            ):  
        proyection = []
        iteration = 1
        capital = 0 
        amount = float(init_amount) 
        porcent = 0.0
        payment_date = datetime.strptime(first_payment_date,'%Y-%m-%d')
        if(type_interest == 1):  
            porcent = float(interest)
            interest = (float(init_amount) * float(interest))  
        if(float(quote_amount) <= float(interest)):
            return{"msm":"Lo sentimos el interes es mayor a la cuota deseada"}
        while(True):
            if(amount <= float(quote_amount)):
                proyection.append({
                    "no":iteration,
                    "payment_date":payment_date,
                    "quote":round(amount,2),
                    "interest":0,
                    "capital":0,
                    "amount":(amount-amount)
                    })
                break
            capital = round(float(quote_amount) - float(interest),2)
            amount -= capital
            proyection.append({
                "no":iteration,
                "payment_date":payment_date,
                "quote":round(float(quote_amount),2),
                "interest":round(float(interest),2),
                "capital":capital,
                "amount":round(amount,2)
                })
            payment_date = self.get_next_date(payment_frecuency, payment_date)
            if(type_interest == 1):
               interest = amount * porcent
            iteration+=1
        return {"msm":"Cotizacion generada con exito", "proyection":proyection, "total":self.get_total_loan(proyection)}

    def create_loan(self,
            client_id:int,
            amount:float,
            quote:float,
            car_photo:str,
            house_photo:str,
            first_payment_date:str,
            interest:float,
            period_payment:str,
            type_interest:str
            ):
        try:
            connect = mysql.connect()
            query = connect.cursor() 
            exec_sp = query.execute("CALL create_loan(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                client_id,
                amount,
                quote,
                car_photo,
                house_photo,
                first_payment_date,
                interest,
                period_payment,
                type_interest
                ))
            connect.commit()
            if(exec_sp>0):
                return{"msm":"prestamo realizado con esito"}
            return{"msm":"por problemas internos no se pudo realizar el prestamo"}
        except Exception as e:
            print(e)
            return{"err":str(e)}

    def get_all_clients(self):
        try:
            connect = mysql.connect()
            query = connect.cursor()
            query.execute("CALL get_all_clients()")
            clients = query.fetchall()
            connect.commit()
            if(len(clients)>0): 
                return{"msm":"clientes encontrados con exito","clients":clients}
            return {"msm":"no se ha encontrando ningun cliente registrado"}
        except Exception as e:
            return{"err":str(e)}




