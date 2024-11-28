import sqlalchemy as sqla

CONNECTION = "mysql+pymysql://is61-9:b6btmug4@192.168.3.111/beauty_salon"

class Database:
    def __init__(self):
        self.engine = sqla.create_engine(CONNECTION)
        self.connection = self.engine.connect()

    def add_registration(self, name,telephone,service_id,employee_id):
        query = sqla.text("INSERT INTO beauty_salon.registration (name,telephone,service_id,employee_id) VALUES (:name,:telephone,:service_id,:employee_id)")
        query = query.bindparams(sqla.bindparam("name", name))
        query = query.bindparams(sqla.bindparam("telephone", telephone))
        query = query.bindparams(sqla.bindparam("service_id", service_id))
        query = query.bindparams(sqla.bindparam("employee_id", employee_id))
        self.connection.execute(query)
        self.connection.commit()



    def get_employee_id(self, id:int):
        query = sqla.text("SELECT * FROM employee WHERE id = :id")
        query = query.bindparams(sqla.bindparam("id", id))
        result = self.connection.execute(query).fetchone()._asdict()
        return result

    def get_employee(self):
        query = sqla.text("SELECT * FROM employee")
        result = self.connection.execute(query).all()
        result_dict = []
        for r in result:
            result_dict.append(r._asdict())
        return result_dict
    def get_services(self):
        query = sqla.text("SELECT * FROM services")
        result = self.connection.execute(query).all()
        result_dict = []
        for r in result:
            result_dict.append(r._asdict())
        return result_dict
    def get_registration(self):
        query = sqla.text("SELECT * FROM registration")
        result = self.connection.execute(query).all()
        result_dict = []
        for r in result:
            result_dict.append(r._asdict())
        return result_dict 

    def get_services(self):
        query = sqla.text("SELECT * FROM services ")
        result = self.connection.execute(query).all()
        result_dict = []
        for r in result:
            result_dict.append(r._asdict())
        return result_dict     