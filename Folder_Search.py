import os 
import shutil

class Folder_Search:
     def __init__(self, folder:str):
          self.folder = folder
          self.resultados = []
   
     def listagem_arquivos(self):
          list_arq = os.listdir(self.folder)
          for arquivo in list_arq:
               self.resultados.append(arquivo)
          return self.resultados
     
     def View_results(self) -> None:
          for resultado in self.resultados:
               print(resultado)
     
     def mover_arquivo(self,origem = str, destino = str):
          try:
               shutil.move(origem, destino)
               print(f"Arquivo '{origem}' movido com sucesso para '{destino}'.")

          except FileNotFoundError:
               print(f"Erro: O arquivo de origem '{origem}' não foi encontrado.")

          except Exception as e:
                 print(f"Ocorreu um erro ao mover o arquivo: {e}")


     def Create_Folder(self, Name_folder = str):
          os.makedirs(name=Name_folder, exist_ok=True)
          if os.path.exists(Name_folder):
               print(f"Pasta '{Name_folder}' criada com sucesso.")
          else:
               print(f"Erro ao criar a pasta '{Name_folder}'.")
     
     def Delete_Folder(self, Name_folder = str):
          try:
               shutil.rmtree(Name_folder)
               print(f"Pasta '{Name_folder}' deletada com sucesso.")
          except FileNotFoundError:
               print(f"Erro: A pasta '{Name_folder}' não foi encontrada.")
          except Exception as e:
               print(f"Ocorreu um erro ao deletar a pasta: {e}")