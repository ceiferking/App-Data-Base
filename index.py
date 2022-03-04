#Importar as bibliotecas
from ast import Pass
from logging import root
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from telegram import User
import DataBaser

#Cria a janela do app.
jan = Tk()
jan.title("OP Systems - Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.95)
jan.iconbitmap(default="icons/LogoIcon.ico")

#========== Carregar Imagens ===========
Logo = PhotoImage(file="icons/logo.png")

#========== Widgets de Login ==========
LeftFrame = Frame(jan, width=200, height=300, bg="WHITE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=Logo, bg="MIDNIGHTBLUE", border=-1)
LogoLabel.place(x=-15, y=40)

Userlabel = Label(RightFrame, text="Username", font=("Century Gothic", 20),bg="MIDNIGHTBLUE", fg="White")
Userlabel.place(x=30, y=75)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=170, y=85)

Passlabel = Label(RightFrame, text="Password", font=("Century Gothic", 20),bg="MIDNIGHTBLUE", fg="White")
Passlabel.place(x=30, y=115)

PassEntry = ttk.Entry(RightFrame, width=30, show="•")
PassEntry.place(x=170, y=125)

#checa os campos de login 'username' e 'Password' com os dados cadastrados no banco de dados.
def LoginAcess():
    UserLogin = UserEntry.get()
    PassLogin = PassEntry.get()
    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? and Password = ?)                         
    """, (UserLogin, PassLogin))
    print("Selecionou")
    VerifyLogin = DataBaser.cursor.fetchone()
    #Apresenta menssagem de login confirmado caso corresponda aos dados cadastrados no database
    #Apresenta menssagem de erro ao fazer login caso não corresponda aos dados cadastrados no database.
    try:
        if (UserLogin in VerifyLogin and PassLogin in VerifyLogin):
                messagebox.showinfo(title="Aviso de Login", message="Acesso Confimado, bem vindo!")
    except:
        messagebox.showerror(title="Aviso de Login", message="Acesso Negado, email ou senha incorretos!")
        

#Botoes de Login
LoginButton = ttk.Button(RightFrame, text="Login", width=-29, command=LoginAcess)
LoginButton.place(x=110, y=185)

#Função do botão register do Login
def Register():
    #Removendo Widgets de Login
    LoginButton.place(x=5000)
    RegisButton.place(x=5000)
    Userlabel.place(x=5000)
    UserEntry.place(x=5000)
    Passlabel.place(x=5000)
    PassEntry.place(x=5000)

    #Inserir Widgets de cadastro
    NameLabel = Label(RightFrame, text="Name", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
    NameLabel.place(x=30,y=5)
    
    NameEntry = Entry(RightFrame, width=30)
    NameEntry.place(x=120,y=15)
    
    EmailLabel = Label(RightFrame, text="Email", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
    EmailLabel.place(x=30,y=40)
    
    EmailEntry = Entry(RightFrame, width=30)
    EmailEntry.place(x=120,y=50)
    
    UserRegisLabel = Label(RightFrame, text="Username", font=("Century Gothic", 20),bg="MIDNIGHTBLUE", fg="White")
    UserRegisLabel.place(x=30, y=75)

    UserRegisEntry = ttk.Entry(RightFrame, width=30)
    UserRegisEntry.place(x=170, y=85)

    PassRegisLabel = Label(RightFrame, text="Password", font=("Century Gothic", 20),bg="MIDNIGHTBLUE", fg="White")
    PassRegisLabel.place(x=30, y=115)

    PassRegisEntry = ttk.Entry(RightFrame, width=30, show="•")
    PassRegisEntry.place(x=170, y=125)
    
    #Função do botão register da tela de registro
    def RegisterDataBase():
        #Le os dados e armazena no banco de dados.
        Name = NameEntry.get()
        Email = EmailEntry.get()
        User = UserRegisEntry.get()
        Pass = PassRegisEntry.get()
        #Apresenta menssagems em caso de erros do preenchimento
        if(Name == "" or Email == "" or User == "" or Pass == ""):
            messagebox.showerror(title="Register Error", message="Não deixe campo vazio. Preencha Todos os Campos")
        #Armazena as informaçoes do dos campos de cadastro em UserData.db
        else:
            DataBaser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)                         
            """, (Name, Email, User, Pass))
            DataBaser.conn.commit()
            messagebox.showinfo(title="Register Info", message="Register Complete")
    
    #Botão Para armazenar no banco de dados
    RegisButton1 = ttk.Button(RightFrame, text="Register", width=-26, command=RegisterDataBase)
    RegisButton1.place(x=115,y=180)


    def BackToLogin():
        #=====Remove Botões de cadastro======
        NameLabel.place(x=5000)
        NameEntry.place(x=5000)
        EmailEntry.place(x=5000)
        EmailLabel.place(x=5000)
        UserRegisLabel.place(x=5000)
        UserRegisEntry.place(x=5000)
        PassRegisLabel.place(x=5000)
        PassRegisEntry.place(x=5000)
        RegisButton1.place(x=5000)
        Back.place(x=5000)
        #Retorna Botões de login
        Userlabel.place(x=30, y=75)
        UserEntry.place(x=170, y=85)
        PassEntry.place(x=170, y=130)
        Passlabel.place(x=30, y=120)
        RegisButton.place(x=120,y=220)
        LoginButton.place(x=110, y=185)
        
    Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
    Back.place(x=130,y=235)

RegisButton = ttk.Button(RightFrame, text="Register", width=-26, command=Register)
RegisButton.place(x=120,y=220)



jan.mainloop()