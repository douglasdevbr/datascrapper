import requests, lxml.html
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
form2["searchForm_SUBMIT"] =1

form3 = {}
''' add parameter to open a detail page '''
form3["javax.faces.partial.ajax"] = "true"

form3["javax.faces.partial.ajax"] = "true"
form3["javax.faces.source"] = "searchForm:dtbEntities:2:j_id_2u"
form3["primefaces.resetvalues"] = "true"
form3["javax.faces.partial.execute"] = all 
form3["javax.faces.partial.render"]="searchForm editForm"
form3["searchForm:dtbEntities:2:j_id_2u"] = "searchForm:dtbEntities:2:j_id_2u"
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



response3 = r.post('http://200.221.196.98:8086/stone/pages/cliente/finalizado.jsf',  data=form )
soup2 = BeautifulSoup(response3.text, 'html.parser')

viewState  = soup2.findAll("input", attrs={"name" : "javax.faces.ViewState"})[0]['value']
print(viewState)
form2["javax.faces.ViewState"]= viewState

response3 = r.post('http://200.221.196.98:8086/stone/pages/cliente/finalizado.jsf',  data=form2 )
soup2 = BeautifulSoup(response3.text, 'html.parser')
viewState2  = soup2.findAll("update", attrs={"id" : "javax.faces.ViewState"})[0].text
print(viewState2)

form3["javax.faces.ViewState"]= viewState2

response3 = r.post('http://200.221.196.98:8086/stone/pages/cliente/finalizado.jsf',  data=form3 )
soup2 = BeautifulSoup(response3.text, 'html.parser')
print(soup2.prettify())


'''hidden_inputs = html.xpath(r'//form//input[@type="hidden"]')
form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
'''

'''print(result)'''