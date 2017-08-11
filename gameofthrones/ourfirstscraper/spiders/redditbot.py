import requests, lxml.html
import requests
import shutil
import urllib.request

from bs4 import BeautifulSoup
r = requests.Session()
response = r.get('http://200.221.196.98:8086/stone/login.jsf')
soup = BeautifulSoup(response.text, 'html.parser')

form = {}
csrf = soup.findAll("input", attrs={"name" : "_csrf"})[0]['value']
print(csrf)
form["j_username"] = "273.601.108-23"
form["j_password"] = "magda141"
form["_csrf"] = csrf
response2 = r.post('http://200.221.196.98:8086/stone/j_spring_security_check', data=form)

form2 = {}

form2["javax.faces.partial.ajax"]= "true"
form2["javax.faces.source"] = "searchForm:searchButton"
form2["javax.faces.partial.execute"] = "searchForm:searchButton searchForm:filterGrid searchForm:complementFilterGrid searchForm:complementFilterGrid2"
form2["javax.faces.partial.render"]= "searchForm:dtbEntities searchForm:searchMessages"
form2["searchForm:searchButton"] = "searchForm:searchButton"
form2["searchForm:documentoFilter"] = ""
form2["searchForm:nomeFilter"] = ""
form2["searchForm:statusFilter_focus"] = ""
form2["searchForm:statusFilter_input"] = ""
form2["searchForm:nomeFantasiaFilter"] = ""
form2["searchForm:dataDeFilter_input"] = ""
form2["searchForm:dataAteFilter_input"] = ""
form2["searchForm:consultorFilter_focus"] = ""
form2["searchForm:consultorFilter_input"] = ""
form2["searchForm:backofficeFilter_focus"] = ""
form2["searchForm:backofficeFilter_input"]  = ""
form2["searchForm_SUBMIT"] = 1

form2["javax.faces.partial.render"] = "searchForm:dtbEntities"
form2["searchForm:dtbEntities"] = "searchForm:dtbEntities"
form2["searchForm:dtbEntities_encodeFeature"] = "true"
form2["searchForm:dtbEntities_pagination"] = "true"
form2["searchForm:dtbEntities_first"] = 0
form2["searchForm:dtbEntities_rows"] = 60


for loop in range(14, 16):

    response3 = r.post('http://200.221.196.98:8086/stone/pages/cliente/finalizado.jsf',  data=form )
    soup2 = BeautifulSoup(response3.text, 'html.parser')

    viewState  = soup2.findAll("input", attrs={"name" : "javax.faces.ViewState"})[0]['value']
    print(viewState)
    form2["javax.faces.ViewState"]= viewState

    response3 = r.post('http://200.221.196.98:8086/stone/pages/cliente/finalizado.jsf',  data=form2 )
    soup2 = BeautifulSoup(response3.text, 'html.parser')
    viewState2  = soup2.findAll("update", attrs={"id" : "javax.faces.ViewState"})[0].text
    print(viewState2)

    form3 = {}
    ''' add parameter to open a detail page '''

    #form3["javax.faces.source"] = "searchForm:dtbEntities:1:j_id_2u"
    '''form3["primefaces.resetvalues"] = "true"'''
    form3["javax.faces.partial.execute"] = all 
    form3["javax.faces.partial.render"] = "searchForm editForm"
    #form3["searchForm:dtbEntities:1:j_id_2u"] = "searchForm:dtbEntities:1:j_id_2u"
    form3["searchForm:documentoFilter"] = ""
    form3["searchForm:nomeFilter"] = ""
    form3["searchForm:statusFilter_focus"] = ""
    form3["searchForm:statusFilter_input"] = ""
    form3["searchForm:nomeFantasiaFilter"] = ""
    form3["searchForm:dataDeFilter_input"] = ""
    form3["searchForm:dataAteFilter_input"] = ""
    form3["searchForm:consultorFilter_focus"] = ""
    form3["searchForm:consultorFilter_input"] = ""
    form3["searchForm:backofficeFilter_focus"] = ""
    form3["searchForm:backofficeFilter_input"] = ""
    form3["editForm_SUBMIT"] = 1

    form3["javax.faces.source"] = "searchForm:dtbEntities:{0}:j_id_2u".format(loop)
    form3["searchForm:dtbEntities:{0}:j_id_2u".format(loop)] = "searchForm:dtbEntities:{0}:j_id_2u".format(loop)

    form3["javax.faces.ViewState"]= viewState2

    response3 = r.post('http://200.221.196.98:8086/stone/pages/cliente/finalizado.jsf',  data=form3 )
   
    soup2 = BeautifulSoup(response3.text, 'html.parser')
    inputs = []
    inputs = soup2.find_all("input")

    imgs = []
    imgs = soup2.find_all(title = "Abrir")

    # docs = []
    # docs = soup2.find_all(title = "Download") ####

    #print(soup2.prettify())
    
    number = 0
    for a in imgs:
        number = number + 1

        teste = a["src"]
        print(a["src"])


        from urllib.request import urlretrieve
        url = 'http://200.221.196.98:8086/{0}'.format(teste)
        url = url.replace("min=true", "min=false")
        dst = 'C:/Users/clari/OneDrive/Documentos/TesteGED/{0}-{1}.jpg'.format(inputs[6]["value"], number)
        urlretrieve(url, dst)

    #print(soup2.prettify())


    for x in range(6,10):  #documento, razão social, nome fantasia, faturamento
        print(inputs[x]["value"])


    #MASCARAS
    cpf = inputs[19]["value"]
    cpf = "{0}.{1}.{2}-{3}".format(cpf[0:3], cpf[3:6], cpf[6:9], cpf[9:11])

    cph = inputs[22]["value"]
    cph = "({0}) {1}-{2}".format(cph[0:2], cph[2:7], cph[7:11])

    ph = inputs[23]["value"]
    ph = "({0}) {1}-{2}".format(ph[0:2], ph[2:6], ph[6:10])

    cep = inputs[24]["value"]
    cep = "{0}.{1}-{2}".format(cep[0:2], cep[2:5], cep[5:8])
    #

    form4 = {}
    form4["editForm:documento"] = inputs[6]["value"] #6
    form4["editForm:razaoSocial"] = inputs[7]["value"] #7
    form4["editForm:nomeFatura"] = inputs[8]["value"] #8
    form4["editForm:faturamentoMes"] = inputs[9]["value"] #9
    form4["editForm:banco_filter"] = ""
    form4["editForm:agencia"] = inputs[12]["value"] #12
    form4["editForm:digitoAgencia"] = inputs[13]["value"] #13
    form4["editForm:operacao"] = inputs[14]["value"] #14 vazio*
    form4["editForm:contaCorrente"] = inputs[15]["value"] #15
    form4["editForm:digitoContaCorrente"] = inputs[16]["value"] #16
    form4["editForm:nome"] = inputs[18]["value"] #18
    form4["editForm:cpf"] = cpf #19                                 MASCARA
    form4["editForm:inputDtNasc"] = inputs[20]["value"] #20
    form4["editForm:email"] = inputs[21]["value"] #21
    form4["editForm:celular"] = cph #22                             MASCARA
    form4["editForm:telefone"] = ph #23                             MASCARA
    form4["editForm:cepInstalacao"] = cep #24                       MASCARA
    form4["editForm:bairroInstalacao"] = inputs[25]["value"] #25   
    form4["editForm:numeroInstalacao"] = inputs[26]["value"] #26
    form4["editForm:logradouroInstalacao"] = inputs[27]["value"] #27
    form4["editForm:complementoInstalacao"] = inputs[28]["value"] #28
    form4["editForm:cidadeInstalacao_filter"] = "" 
    form4["editForm:referenciaInstalacao"] = inputs[31]["value"] #31
    form4["editForm:habilitaAdquirencia_input"] = "on"
    form4["editForm:porcentagemDebito"] = inputs[37]["value"] #37
    form4["editForm:porcentagemCredito"] = inputs[38]["value"] #38
    form4["editForm:porcentagemParcelado2a6"] = inputs[39]["value"] #39
    form4["editForm:porcentagemParcelado7a12"] = inputs[40]["value"] #40
    form4["editForm:porcentagemEmissor"] = inputs[41]["value"] #41
    form4["editForm:porcentagemAntecipacao"] = inputs[43]["value"] #43
    form4["editForm:quantidadePos"] = inputs[45]["value"] #45
    form4["editForm:valorPos"] = inputs[46]["value"] #46
    form4["editForm:quantidadeTef"] = inputs[47]["value"] #47
    form4["editForm:valorTef"] = inputs[48]["value"] #48
    form4["editForm:quantidadeMobile"] = inputs[49]["value"] #49
    form4["editForm:valorMobile"] = inputs[50]["value"] #50
    form4["editForm:valorSoftware"] = inputs[51]["value"] #51
    form4["editForm:outros"] = inputs[52]["value"]  #52
    form4["editForm:diaDePagamento"] = inputs[53]["value"] #53
    form4["editForm:obsNumeroSerie"] = ""  #70? não tem value
    form4["editForm:obsOutros"] = inputs[71]["value"] #71 vazio*
    form4["editForm:obsTEFHouse"] = ""
    form4["editForm:j_id_az_4_input"] = "" 
    form4["editForm:j_id_az_b_input"] = ""
    form4["editForm:descricaoGravacao"] = ""
    form4["editForm:descricaoEnvio"] = ""
    form4["editForm:descricaoAprovacao"] = ""
    form4["editForm:descricaoNegacao"] = ""
    form4["editForm:descricaoCancelamento"] = ""
    form4["editForm:descricaoEmAnalise"] = ""
    form4["editForm:descricaoPendentePos"] = ""
    form4["editForm:numeroSerie"] = "" #78? não tem value
    form4["editForm_SUBMIT"] = 1
    form4["javax.faces.ViewState"] = viewState2
    form4["editForm:documentosGrid:0:j_id_ah"] = "editForm:documentosGrid:0:j_id_ah" ##

    response4 = r.post('http://200.221.196.98:8086/stone/pages/cliente/finalizado.jsf',  data=form4 )
    response4.headers["Content-Disposition"] = "attachment;filename='contrato.pdf'"

    # with open('contratoTeste.pdf', 'wb') as code: 
    #     code.write(response4.raw)


    # number = 0
    # for a in docs:
    #     number = number + 1

    # with open('doc{0}-{1}.pdf'.format(inputs[6]["value"], number), 'wb') as f:
    #     response4.raw.decode_content = True
    #     shutil.copyfileobj(response4.raw, f)


    with open('contrato.pdf', 'wb') as f:
        response4.raw.decode_content = True
        shutil.copyfileobj(response4.raw, f)


    soup4 = BeautifulSoup(response4.text, 'html.parser')  
    #print(soup4.prettify())

#SALVANDO IMAGEM:
# from urllib.request import urlretrieve
# url = 'http://200.221.196.98:8086//stone/fotos?idCliente=4403&nomeFoto=fachada.jpg&uid=87d7e01e-0b68-45d7-a4b0-69db029f90ea&temp=false&min=false&pfdrid_c=false&uid=1bde9d0f-0238-4f1e-bbde-ee045a53e713' 
# dst = 'C:/Users/clari/OneDrive/Documentos/TesteGED/img2.jpg'
# urlretrieve(url, dst)

#PARAMETROS POST DOCUMENTO
# form4 = {}
# form4["editForm:documento"] = 10644207000152
# form4["editForm:razaoSocial"] = "IGREJA EVANGELICA VERBO DA VIDA BELO HORIZONTE"
# form4["editForm:nomeFatura"] = "VERBO DA VIDA BH"
# form4["editForm:faturamentoMes"] = 50.000,00
# form4["editForm:banco_filter"] = ""
# form4["editForm:agencia"] = 1229
# form4["editForm:digitoAgencia"] = 7
# form4["editForm:operacao"] = ""
# form4["editForm:contaCorrente"] = "00136950"
# form4["editForm:digitoContaCorrente"] = 4
# form4["editForm:nome"] = "MARCELO SILVA CARVALHO"
# form4["editForm:cpf"] = "687.892.705-68"
# form4["editForm:inputDtNasc"] = "31/01/1975"
# form4["editForm:email"] = "presidencia@verbobh.com"
# form4["editForm:celular"] = "(31) 98872-4311"
# form4["editForm:telefone"] = "(31) 3291-8799"
# form4["editForm:cepInstalacao"] = "30.411-052"
# form4["editForm:bairroInstalacao"] = "PRADO"
# form4["editForm:numeroInstalacao"] = 164
# form4["editForm:logradouroInstalacao"] = "RUA ERE"
# form4["editForm:complementoInstalacao"] = ""
# form4["editForm:cidadeInstalacao_filter"] = ""
# form4["editForm:referenciaInstalacao"] = ""
# form4["editForm:habilitaAdquirencia_input"] = "on"
# form4["editForm:porcentagemDebito"] = "2,09"     ####
# form4["editForm:porcentagemCredito"] = "2,57"
# form4["editForm:porcentagemParcelado2a6"] = "2,62"
# form4["editForm:porcentagemParcelado7a12"] = "2,88"
# form4["editForm:porcentagemEmissor"] = "0,00"
# form4["editForm:porcentagemAntecipacao"] = "0,00"
# form4["editForm:quantidadePos"] = 1
# form4["editForm:valorPos"] = "80,00"
# form4["editForm:quantidadeTef"] = 0
# form4["editForm:valorTef"] = "0,00"
# form4["editForm:quantidadeMobile"] = 0
# form4["editForm:valorMobile"] = "0,00"
# form4["editForm:valorSoftware"] = "0,00"
# form4["editForm:outros"] = "0,00"
# form4["editForm:diaDePagamento"] = 20
# form4["editForm:obsNumeroSerie"] = "524-297-661"
# form4["editForm:obsOutros"] = ""
# form4["editForm:obsTEFHouse"] = ""
# form4["editForm:j_id_az_4_input"] = ""
# form4["editForm:j_id_az_b_input"] = ""
# form4["editForm:descricaoGravacao"] = ""
# form4["editForm:descricaoEnvio"] = ""
# form4["editForm:descricaoAprovacao"] = ""
# form4["editForm:descricaoNegacao"] = ""
# form4["editForm:descricaoCancelamento"] = ""
# form4["editForm:descricaoEmAnalise"] = ""
# form4["editForm:descricaoPendentePos"] = ""
# form4["editForm:numeroSerie"] = ""
# form4["editForm_SUBMIT"] = 1
# form4["javax.faces.ViewState"] = "8FYRNk90oIpCcwecVo7ad0Xb3Ygu+t21lYZPd8atYt5Iqdlp"
# form4["editForm:documentosGrid:0:j_id_ah"] = "editForm:documentosGrid:0:j_id_ah"

# response4 = r.post('http://200.221.196.98:8086/stone/pages/cliente/finalizado.jsf',  data=form4 )
   
# soup2 = BeautifulSoup(response4.text, 'html.parser')
# inputs = []
# inputs = soup2.find_all("input")

# for item in inputs:
#     print(item["value"])


'''print(soup2.find_all("input").get_text())'''

'''hidden_inputs = html.xpath(r'//form//input[@type="hidden"]')
form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
'''

'''print(result)'''
