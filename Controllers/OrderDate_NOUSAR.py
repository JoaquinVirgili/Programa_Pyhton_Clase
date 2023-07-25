import datetime

class OrderDate:
    @staticmethod
    def order_date(date: str):

        formats = ['%d-%m-%Y', '%m-%d-%Y', '%Y-%m-%d']
        for fmt in formats:
            try:
                birthday = datetime.datetime.strptime(date, fmt)
                return birthday, True
            except ValueError:
                pass
        return print("Formato de fecha incorrecto: {}".format(date)), False
        
        