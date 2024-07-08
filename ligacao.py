from twilio.rest import Client

account_sid = "AC34b0c73e3e516ab9b23180bc4ee15654"
auth_token = "e40f498b488b651068703cd5da30daa9"
meu_numero = "+5541998801921"
number_twilio = "+14152372613"  

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