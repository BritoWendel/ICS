from Database import *

db = Database('dev', 'dev', 'localhost', 'sci_db')
for i in range(200):
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
            ['New Maracanã',
            '13453343',
            'wendelbrito',
            '999995555',
            '19',
            'wendel',
            '0',
            '10669134000153',
            '592063602906',
            '99999994',
            'Rua manoel machado pereira',
            'wendelbrito@email.com.br',
            'Nenhum',
            'facebook.com/wendel',
            '2']
            )
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

