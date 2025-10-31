import customtkinter
from CTkListbox import CTkListbox


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # --- Configuração da Janela ---
        self.title("Lista de Seleção CustomTkinter")
        self.geometry("400x300")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- Lista de Objetos ---
        self.objetos = ["Maçã", "Banana", "Laranja", "Morango", "Uva", "Abacaxi", "Manga"]
        
        # --- Widget CTkListbox ---
        self.listbox = CTkListbox(
            master=self, 
            command=self.item_selecionado, # Chama a função ao selecionar um item
            height=150,
            width=300
        )
        self.listbox.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Insere os itens na lista
        for item in self.objetos:
            self.listbox.insert("end", item)
            
        # Label para mostrar a seleção
        self.label_selecao = customtkinter.CTkLabel(
            master=self, 
            text="Nenhum item selecionado", 
            fg_color="transparent"
        )
        self.label_selecao.grid(row=1, column=0, padx=20, pady=(0, 10))

        # Botão para Ação (exemplo)
        self.botao_acao = customtkinter.CTkButton(
            master=self, 
            text="Mostrar Seleção Atual", 
            command=self.mostrar_selecao_botao
        )
        self.botao_acao.grid(row=2, column=0, padx=20, pady=(0, 20))

    def item_selecionado(self, valor_selecionado):
        """Função chamada quando um item é clicado na lista."""
        self.label_selecao.configure(text=f"Item Selecionado (Click): {valor_selecionado}")
        print(f"Item Selecionado (Click): {valor_selecionado}")

    def mostrar_selecao_botao(self):
        """Função chamada ao clicar no botão."""
        selecao_atual = self.listbox.get() # Obtém o valor atualmente selecionado
        if selecao_atual:
            self.label_selecao.configure(text=f"Seleção Atual (Botão): {selecao_atual}")
            print(f"Seleção Atual (Botão): {selecao_atual}")
        else:
            self.label_selecao.configure(text="Nenhum item selecionado")
            print("Nenhum item selecionado")


if __name__ == "__main__":
    app = App()
    app.mainloop()
