import smtplib
import email.message


#Essa linha define a função que tem como utilidade enviar o e-mail
def enviar_email():

    password = "lmoj zxwn qrjy bgbs"

    # A mensagem que irá sair no e-mail
    corpo_email = "<p>Olá professor Daniel, queria lhe perguntar se posso refazer as listas 1,2,3, pois, quando converti para pdf o scanner prejudicou a legibilidade, será que eu poderia fazer novamente é mandar novamente?</p>"

    # Atribuimos o corpo do email a msg
    msg = email.message.Message()
    msg["Subject"] = "Lista de exercícios"
    msg["From"] = "sallyn2544@gmail.com"
    msg["To"] = "daniel.sousa@ifg.edu.br"

    msg.add_header("content-Type", "text/html")

    msg.set_payload(corpo_email)

    #Conexão SMTP
    s = smtplib.SMTP("smtp.gmail.com: 587")
    s.starttls()
    
    #Fazemos o login no servidro SMTP usando o remetente e a senha fornecidos. Em seguida, utilizamos o método "sendemail()" para enviar o e-mail. O método espera o remetente, uma lista de destinatários e a mensagem como uma string 
    s.login(msg["From"], password)
 
    for _ in range(3):
        s.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))

    print("Email Enviado")

enviar_email()