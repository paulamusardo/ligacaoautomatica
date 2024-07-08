from twilio.rest import Client

account_sid = "..........."
auth_token = "..........."
meu_numero = "+554199880...."
number_twilio = "+14152372...."  

cliente = Client(account_sid, auth_token)

mensagem = """
<Response>
<Say language="pt-BR">
Olá, como você está? Esse é um teste
</Say>
</Response>
"""

ligacao = cliente.calls.create(
    to=meu_numero,
    from_=number_twilio,
    twiml=mensagem
)