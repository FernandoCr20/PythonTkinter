import tkinter as tk
from tkinter import ttk
import modelo

class PrincipalBD():
    def __init__(self, win):
        self.objBD = modelo.AppBD()
        self.janela = win

        self.treeProdutos = ttk.Treeview(self.janela, columns=("Codigo do produto", "Nome", "Precos"), show="headings")
        self.ExibirTela()
        self.treeProdutos.heading("Codigo do produto", text="Codigo do produto")
        self.treeProdutos.heading("Nome", text="Nome:")
        self.treeProdutos.heading("Precos", text="Precos:")
        self.treeProdutos.pack()

        self.lblNome = tk.Label(self.janela, text="Nome")
        self.lblNome.pack()
        self.entryNome = tk.Entry(self.janela)
        self.entryNome.pack()

        self.lblPreco = tk.Label(self.janela, text="Preco")
        self.lblPreco.pack()
        self.entryPreco = tk.Entry(self.janela)
        self.entryPreco.pack()

        self.btnCadastrar = tk.Button(self.janela, text="Adicionar", command=self.CadastrarProduto)
        self.btnCadastrar.pack()

        self.btnAtualizar = tk.Button(self.janela, text="Atualizar", command=self.AtualizarProduto)
        self.btnAtualizar.pack()

        self.btnDeletar = tk.Button(self.janela, text="Deletar", command=self.DeletarProduto)
        self.btnDeletar.pack()

    def CadastrarProduto(self):
        try:
            name = self.entryNome.get()
            price = float(self.entryPreco.get())
            self.objBD.inserirDados(name, price)
            self.ExibirTela()
            self.entryNome.delete(0, tk.END)
            self.entryPreco.delete(0, tk.END)
            print("Produto Cadastrado com Sucesso")
        except: 
            print("Nao foi possivel fazer o cadastro")

    def ExibirTela(self):
        try:
            self.treeProdutos.delete(*self.treeProdutos.get_children())
            products = self.objBD.select_all_products() 
            print("**Dados disponiveis**")
            products = self.objBD.select_all_products()
            for product in products:
                self.treeProdutos.insert("", tk.END, values=product)
        except:
            print("Não foi possível acessar os dados")

    def AtualizarProduto(self):
        try:
            selected_item = self.treeProdutos.selection() # selecionar o item que você quer atualizar
            if not selected_item: # se nada foi selecionado ele encerra a função
                return
            item = self.treeProdutos.item(selected_item) # lista com diferentes tipos de dados
            print(item)
            product = item['values'] # da lista só o values
            print(product)
            product_id = product[0] # do values só o ID que é o indice 0
            print(product_id)
            nome = self.entryNome.get()
            preco = float(self.entryPreco.get())
            self.objBD.update_products(product_id, nome, preco)
            self.exibirTela()
            self.entryNome.delete(0, tk.END)
            self.entryPreco.delete(0, tk.END)
            print("Atualização realizada com sucesso")
        except:
            print("não foi possivel atualizar")
    
    def DeletarProduto(self):
        try:
            selected_item = self.treeProdutos.selection() # selecionar o item que você quer atualizar
            if not selected_item: # se nada foi selecionado ele encerra a função
                return
            item = self.treeProdutos.item(selected_item) # lista com diferentes tipos de dados
            print(item)
            product = item['values'] # da lista só o values
            print(product)
            product_id = product[0] # do values só o ID que é o indice 0
            print(product_id)
            self.objBD.delete_products(product_id) # deletar o item pelo id
            self.exibirTela() 
            print("Item deletado com sucesso")
        except:
            print("não foi possivel deletar")


janela = tk.Tk() # criar a janela principal

product_app = PrincipalBD(janela)

janela.title("Bem vindo a aplicação de banco de dados")
janela.geometry("700x500")
janela.mainloop()
