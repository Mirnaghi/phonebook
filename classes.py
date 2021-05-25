class Main:
  from datetime import datetime
  import lorem
  import random
  import names
  import string
  import os
  import json

  def generate_string(self, count):
    return ''.join(self.random.choices(self.string.ascii_lowercase, k=count))


  def generate_phone_number(self):
    return f"+994{self.random.choice(['55', '50', '70'])}{self.random.randint(1000000, 9999999)}"


  def generate_email(self, fname, lname):
    return f"{fname.lower()}_{lname.lower()}@{self.random.choice(['gmail.com', 'mail.ru', 'yahoo.com'])}"  


  def generate_birth_date(self, start, end):
    return self.datetime.strptime(f"{self.random.randint(1, 365)} {self.random.randint(start, end)}", '%j %Y').date().strftime('%d-%m-%Y')


  def generate_insta(self, fname, lname):
    return f'@{fname.lower()[0]}_{lname.lower()}'  


class Json(Main):
  def __init__(self, count=50, file='data.json'):
    self.file = file
    self.count = count
    self.create_file()


  def create_file(self):
    if not self.os.path.exists(self.file):
      with open(self.file, 'w') as f:
        self.json.dump(self.generate_data(), f, indent=2)


  def generate_single_data(self):
    firstname, lastname = self.names.get_full_name().split(" ")
    return {
      'firstname': firstname,
      'lastname': lastname,
      'slug': self.generate_string(8),
      'address': self.lorem.sentence(),
      'phone': self.generate_phone_number(),
      'bdate': self.generate_birth_date(1980, 2021),
      'email': self.generate_email(firstname, lastname),
      'instagram': self.generate_insta(firstname, lastname),
      'note': self.lorem.paragraph(),
    }


  def generate_data(self):
    return [self.generate_single_data() for i in range(self.count)]


  def get_data(self):
    with open(self.file, 'r') as f:
      data = self.json.load(f)
    return data  


m = Json()