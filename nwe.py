from peewee import *

db = SqliteDatabase('Cotações.db')

class perfil(Model):
          nome = CharField()
          email = CharField(unique = True)
          senha = CharField()

          class Meta:
                  database = db  

class Moedas(Model):
        nome = ForeignKeyField(perfil, backref='Perfil')
        valor_atualizado = TextField()
        Horário = DecimalField()

        class Meta:
                database = db

class Anuncio(Model):
         nome = ForeignKeyField(perfil , backref='Perfil')
         titulo = CharField()
         valor = FloatField()
         descricao = TextField()
         class Meta:
                 database = db               