import pymysql.cursors

def get_current_balance():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 database='hematinaja',
                                 cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        sql = "SELECT saldo FROM hitunguang ORDER BY id DESC LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchone()
        return int(result['saldo']) if result else 0  # Pastikan saldo dikonversi ke integer

def insert_data(date, category, income, spending):
    income = int(income.replace('.', '')) if isinstance(income, str) else income
    spending = int(spending.replace('.', '')) if isinstance(spending, str) else spending

    current_balance = get_current_balance()
    new_balance = current_balance + income - spending

    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 database='hematinaja',
                                 cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        sql = "INSERT INTO hitunguang (tanggal, kategori, pemasukan, pengeluaran, saldo) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (date, category, income, spending, new_balance))
        connection.commit()


def show_data():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 database='hematinaja',
                                 cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        sql = "SELECT * FROM hitunguang"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

def update_data(self):
    record_id = self.id_var.get()
    date = self.date_var.get()
    category = self.category_var.get()
    nominal = int(self.nominal_var.get())  # Pastikan nominal adalah integer
    income = self.income_var.get()
    spending = self.spending_var.get()

    connection = pymysql.connect(host='localhost', user='root', password='', database='hematinaja')
    with connection.cursor() as cursor:
        cursor.execute("SELECT saldo, pemasukan, pengeluaran FROM hitunguang WHERE id = %s", (record_id,))
        result = cursor.fetchone()

        if not result:
            messagebox.showerror("Error", "Record not found")
            return

        # Konversi result ke integer jika mereka bukan integer
        current_balance = int(result[0]) if result[0] is not None else 0
        current_income = int(result[1]) if result[1] is not None else 0
        current_spending = int(result[2]) if result[2] is not None else 0

        if income:
            new_income = nominal
            new_spending = current_spending
            new_balance = current_balance - current_income + new_income
        elif spending:
            new_spending = nominal
            new_income = current_income
            new_balance = current_balance + current_spending - new_spending

        sql = """UPDATE hitunguang 
                 SET tanggal=%s, kategori=%s, pemasukan=%s, pengeluaran=%s, saldo=%s 
                 WHERE id=%s"""
        cursor.execute(sql, (date, category, new_income, new_spending, new_balance, record_id))
        connection.commit()

    messagebox.showinfo("Success", "Data updated successfully")
    self.reset_fields()


def delete_data(id):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 database='hematinaja',
                                 cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        sql = "DELETE FROM hitunguang WHERE id = %s"
        cursor.execute(sql, (id,))
        
        # Recalculate balance for all subsequent records
        sql = "SELECT id, pemasukan, pengeluaran FROM hitunguang ORDER BY id ASC"
        cursor.execute(sql)
        rows = cursor.fetchall()
        previous_balance = 0

        for row in rows:
            new_balance = previous_balance + row['pemasukan'] - row['pengeluaran']
            sql_update_balance = "UPDATE hitunguang SET saldo = %s WHERE id = %s"
            cursor.execute(sql_update_balance, (new_balance, row['id']))
            previous_balance = new_balance

        connection.commit()
