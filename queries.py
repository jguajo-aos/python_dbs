
query_insert = """
INSERT INTO {table_name}
    (id_customer, name_customer, lastname_customer, email_customer, password_customer, register_date) 
VALUES
    ({id_customer}, '{name_customer}', '{lastname_customer}', '{email_customer}', '{password_customer}', '{register_date}')
"""

query_val_user = """
SELECT * 
FROM {table_name} 
WHERE id_customer = {id_customer}
"""