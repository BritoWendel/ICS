from Database import *
from random import randint

rsociais = ['Wendel Brito', 'Aline Aparecida', 'Andre Ricardo', 'Jeferson Luiz', 'João Gabriel', 'Rodney de Andrade', 'Tiffany Carvalho']
cnpjs = ['68559950000194','24525844000114','95475845000140','74614401000178','68486686000106','77156187000141','99967166000149']
iestaduais = ['737430566205','437625328589','855099423414','977927890277','353345380120','300560160705','055593537275']

db = Database('dev', 'dev', 'localhost', 'sci_db')
for i in range(200):
    rsocial = rsociais[randint(0,6)]
    iestadual = iestaduais[randint(0,6)]
    cnpj = cnpjs[randint(0,6)]

    db.insert("CLIENTE", ['bairro_cliente',
            'cep_cliente',
            'rsocial_cliente',
            'ncel_cliente',
            'ddd_cel_cliente',
            'nfantasia_cliente',
            'whatsapp_cliente',
            'cnpj_cliente',
            'iestadual_cliente',
            'imunicipal_cliente',
            'logradouro_cliente',
            'email_cliente',
            'complemento_cliente',
            'url_cliente',
            'id_municipio_cliente'],
            ['Barão',
            '13453343',
            rsocial,
            '999995555',
            '19',
            rsocial.lower().strip(" "),
            '0',
            cnpj,
            iestadual,
            '99999994',
            'Rua manoel machado pereira',
            rsocial.lower().strip(" ") + '@email.com.br',
            'Nenhum',
            'facebook.com/'+ rsocial.lower().strip(" "),
            '4'])
    id_cliente = str(db.last_insert_id()[0]['LAST_INSERT_ID()'])
    db.insert("TELEFONE",
            ["ddd_telefone",
            "numero_telefone",
            "id_cliente_telefone"],
            ["19",
            '32617735',
            id_cliente])
    db.insert("TELEFONE",
            ["ddd_telefone",
            "numero_telefone",
            "id_cliente_telefone"],
            ["19",
            '32217799',
            id_cliente])
    db.insert("TELEFONE",
            ["ddd_telefone",
            "numero_telefone",
            "id_cliente_telefone"],
            ["19",
            '32226539',
            id_cliente])

db.close()

