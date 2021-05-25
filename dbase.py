import sqlite3 as dbase


class Database:
  def __init__(self, table):
    # connct db
    connect = dbase.connect('phonebook.db', check_same_thread=False)
    connect.row_factory = dbase.Row
    connect.isolation_level = None

    # initialize cursor
    self.db = connect.cursor()

    self.table = table
    self.create_table()


  def create_table(self):
    query = f'''
      CREATE TABLE IF NOT EXISTS `{self.table}` (
        `id` INTEGER PRIMARY KEY,
        `slug` VARCHAR(8) NOT NULL,
        `firstname` VARCHAR(25) NOT NULL,
        `lastname` VARCHAR(25) NOT NULL,
        `phone` VARCHAR(13) NOT NULL,
        `email` VARCHAR(250) NOT NULL,
        `address` VARCHAR(333) DEFAULT NULL,
        `bdate` DATE DEFAULT NULL,
        `instagram` TEXT DEFAULT NULL,
        `note` TEXT DEFAULT NULL,
        `created` DATETIME DEFAULT CURRENT_TIMESTAMP,
        `status` VARCHAR(15) DEFAULT 'active' 
      )
    '''
    self.db.execute(query)
    

  def create(self, data):
    query = f"""INSERT INTO `{self.table}` (`{'`, `'.join(data.keys())}`)VALUES ('{"', '".join(data.values())}') """
    return self.db.execute(query)
  
  def insert_data(self, data):
    for d in data:
      print(self.create(d))


  def read(self):
    query = f'''
    SELECT 
      * 
    FROM `{self.table}`
    ORDER BY `id`
    '''  
    result = self.db.execute(query).fetchall()
    return [dict(d) for d in result]


  def read_by_id(self, row_id):
    query = f'''
    SELECT 
      * 
    FROM `{self.table}`
    WHERE
      `id` == '{row_id}'
    '''
    result = self.db.execute(query).fetchone()
    return dict(result) if result else False


  def get_id(self, col_name, data):
    query = f'''
    SELECT 
      `id` 
    FROM `{self.table}`
    WHERE
      `{col_name}` == '{data}'
    '''
    result = self.db.execute(query).fetchone()
    return dict(result)['id'] if result else False


  def update(self, row_id, col_name, data):
    query = f'''
    UPDATE 
      {self.table} 
    SET 
      `{col_name}` = '{data}'
    WHERE 
      `id` = {row_id}  
    '''  
    self.db.execute(query)
    return self.read_by_id(row_id)


  def delete(self, row_id):
    query = f'''
    DELETE 
    FROM {self.table}
    WHERE 
      `id` = {row_id}  
    '''  
    data = self.read_by_id(row_id)
    if data:
      self.db.execute(query)
    return data  
