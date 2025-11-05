from PyPDF2 import PdfFileReader 



def abrir_Arquivo(nome:str, formato : str) -> None :
    with open (f"{nome}.{formato} ") as arquivo:

        if formato == ".pdf":
            pdf_reader = PdfFileReader(arquivo)
            numpages = pdf_reader.numPages
            for pages in range(numpages):
                page  = pdf_reader.getPage(page)
                texto = page.extract_text()
                print("Texto da página", page + 1, ":", texto)
        else:
            print(arquivo.read())


def list_arquivos(lista_arquivos : list) -> None :
    for j in range(0 , len(list_arquivos)):
        # Abrindo um arquivo PDF existente
        with open(f"{j}.pdf", "rb") as input_pdf:
            # Criando um objeto PdfFileReader
            pdf_reader = PdfFileReader(input_pdf)

            # Obtendo o número de páginas do arquivo PDF
            num_pages = pdf_reader.numPages

            # Lendo o texto de cada página
            for page_number in range(num_pages):
                page = pdf_reader.getPage(page_number)
                text = page.extractText()
                print("Texto da página", page_number + 1, ":", text)

run = True
while run == True:
    if arq == "Não quero continuar":
        run == False
    else: 
        run == True
        arq = input("diga o nome do arquivo que deseja e seu formato: \n")
        partes = arq.rsplit('.', 1)
        nome_arquivo = partes[0]
        formato = partes[1]
        abrir_Arquivo(nome = nome_arquivo, formato = partes)
