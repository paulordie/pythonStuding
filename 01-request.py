#!/usr/bin/env python3.8
#!/usr/bin/env python3

import requests
import json

api_token = 'XFmGfULe09wRwQnfziVd-xq9tZm0WH9Y'
api_url_base = 'https://rd-mantis.aoc.com.br:8080/api/issues?project_id71&page_size500&page'
api_url_baseUpCase = 'http://rd-mantis.aoc.com.br:8080/api/rest/issues?PROJECT_ID71&page_size500&page1'

api_url_base2 = 'http://rd-mantis.aoc.com.br:8080/api/rest/issues'
api_url_base1 = 'http://rd-mantis.aoc.com.br:8080/api/rest'
api_url_base_port_diff = 'http://rd-mantis.aoc.com.br:8011/api/rest/issues'

api_url_base2 = 'http://rd-mantis.aoc.com.br:8080/api/rest&issues'

api_url_base_port = 'http://rd-mantis.aoc.com.br:/api/rest/issues?project_id71&page_size500&page'
api_url_base_char_plus = 'http://rd-mantis.aoc.com.br:/api/rest/issuess'
api_url_ssdp = 'http://172.31.142.27:44642/ssdp-description'



api_url_ok = 'http://rd-mantis.aoc.com.br:8080/api/rest/issues?project_id=71'
api_url_double_var = 'http://rd-mantis.aoc.com.br:8080/api/rest/issues?project_id=71&project_id=53'

headers = {'Content-Type': 'application/json',
           'AUTHORIZATION': api_token}

headers1 = {'Content-Type': 'application/json',
           'Authorization': api_token,
           'Authorization': 'akfhasodbaosbvasnvuioasdiafIiIis'}


headers2 = {'Content-Type': 'application/json',
           'Authorization': api_token,
           'Authorization': api_token}
def get_mantis_double_var():
    response = requests.get(api_url_double_var, headers=headers)
    print(response)
    if response.status_code == 200:
        print('request OK 200')
        return json.loads(response.content.decode('utf-8'))
    else:
        print('result erro response: ', response)
        return None


def get_mantis_double_token():
    response = requests.get(api_url_base2, headers=headers1)
    print(response)
    if response.status_code == 200:
        print('request OK 200')
        return json.loads(response.content.decode('utf-8'))
    else:
        print('result erro response: ', response)
        return None

    
def get_mantis_double_token_good():
    response = requests.get(api_url_base2, headers=headers1)
    print(response)
    if response.status_code == 200:
        print('request OK 200')
        return json.loads(response.content.decode('utf-8'))
    else:
        print('result erro response: ', response)
        return None

def get_mantis_ok():
    response = requests.get(api_url_ok, headers=headers)
    print(response)
    if response.status_code == 200:
        print('request OK 200')
        print(headers)
        return json.loads(response.content.decode('utf-8'))
    else:
        print('result erro response: ', response)
        return None


def get_mantis_without():
    response = requests.get(api_url_base, headers=headers)
    print(response)
    if response.status_code == 200:
        print('request OK 200')
        return json.loads(response.content.decode('utf-8'))
    else:
        print('result erro response: ', response)
        return None

def get_mantis_more_parameter():
    response = requests.get(api_url_base2, headers=headers)
    print(response)
    if response.status_code == 200:
        print('request OK 200')
        return json.loads(response.content.decode('utf-8'))
    else:
        print('result erro response: ', response)
        return None


def get_mantis_port_diff():
    response = requests.get(api_url_base_port_diff, headers=headers)
    print(response)
    if response.status_code == 200:
        print('request OK 200')
        return json.loads(response.content.decode('utf-8'))
    else:
        print('result erro response: ', response)
        return None


def get_mantis_erro():
    response = requests.get(api_url_base1, headers=headers)

    print(response)
    if response.status_code == 200:
        print('request OK 200')
        return json.loads(response.content.decode('utf-8'))
    else:
        print('result erro response: ', response)
        return None


def get_mantis_erro_port():
    response = requests.get(api_url_base_port, headers=headers)
    print(response)
    if response.status_code == 200:
        print('request OK 200')
        return json.loads(response.content.decode('utf-8'))
    else:
        print('result erro response: ', response)
        return None


def get_mantis_erro_char_plus():
    response = requests.get(api_url_base_port, headers=headers)
    print(response)
    if response.status_code == 200:
        print('request OK 200')
        return json.loads(response.content.decode('utf-8'))
    else:
        print('result erro response: ', response)
        return None

def get_mantis_up_case():
    response = requests.get(api_url_baseUpCase, headers=headers)
    print(response)
    if response.status_code == 200:
        print('request OK 200')
        return json.loads(response.content.decode('utf-8'))
    else:
        print('result erro response: ', response)
        return None

def get_ssdp():
    response = requests.get(api_url_ssdp)
    print(response)
    if response.status_code == 200:
        print('request OK 200')
        return json.loads(response.content.decode('utf-8'))
    else:
        print('result erro response: ', response)
        return None
# responseJson = get_mantis()
# print(responseJson)
# print('OK')


#qRequest = input('digite qual é sua opção de request: ')

while True:

    qRequest = input('digite qual é sua opção de request: ')
   

    if qRequest == 'doubleVar':
        resp = get_mantis_double_var()
        print('double var is: ', resp)
        print(api_url_double_var)
        
    if qRequest == 'doubleToken':
        resp = get_mantis_double_token()
        print('double var is: ', resp)
        print(api_url_base2)

    if qRequest == 'doubleToken2':
        resp = get_mantis_double_token_good()
        print('double var is: ', resp)
        print(api_url_base2)

    if qRequest == 'https':
        resp = get_mantis_without()
        print('get1 ', resp)
        print(api_url_base)
    

    elif qRequest == 'erroIssues':
        print('Without /issues/')
        resp = get_mantis_erro()
        print('get2 ', resp)
        print(api_url_base1)
    

    elif qRequest == 'erroPort':
        resp = get_mantis_erro_port()
        print('erro port ', resp)
        print(api_url_base_port)
        

    elif qRequest == 'erroCharPlus':
        resp = get_mantis_erro_char_plus()
        print('erro port ', resp)
        print(api_url_base_char_plus)
        

    elif qRequest == 'erroPortDiff':
        resp = get_mantis_port_diff()
        print('erro port diff ', resp)
        print(api_url_base_port_diff)
        

    elif qRequest == 'erroUpCase':
        resp = get_mantis_up_case()
        print('erro port diff ', resp)
        print(api_url_baseUpCase)
        

    elif qRequest == 'ssdp':
        resp = get_ssdp()
        print('erro port ', resp)
        print(api_url_ssdp)
        


    elif qRequest == 'parameterInexist':
        resp = get_mantis_more_parameter()
        print('erro parameter does not exit ', resp)
        print(api_url_base2)
        

    elif qRequest == 'okProjects':
        resp = get_mantis_ok()
        print('erro parameter does not exit ', resp)
        print(api_url_ok)

    elif qRequest == 'finish':
        break

    else:
        print('vc digitou algo diferente')
