[17/07/17 14:43:30] Clarissa Abreu: eu agora preciso fazer com que retornem so as campanhas com IdDistributor igual ao IdDistributor da session
[17/07/17 14:43:49] Clarissa Abreu: eu tentei olhar a Merchant, mas ta bem estranha
[17/07/17 14:43:57] Clarissa Abreu: tem uma ideia de como fazer?
[18/07/17 13:05:24] douglasdevbr: https://manager.cloudwalk.io/users/sign_in
[18/07/17 14:54:26] Clarissa Abreu: douglas, dá p usar o JsonConvert na facade? Pq na WebApiHelper funciona. Pode baixar o newtonsoft na ServiceAgents, no caso?
[20/07/17 13:02:54] Clarissa Abreu: oi Douglas
[20/07/17 16:52:00] Clarissa Abreu: Douglas, falei com Lucas e validei aqui com Christian
[20/07/17 16:52:10] Clarissa Abreu: create view as Vendedor as 
select replace(upper(uaA.Name) ,'"','') as 'Vendedor', replace(upper(uaB.Name) ,'"','') as 'Representante' 
from UserAccount uaA 
join UserAccount uaB on uaA.IdUserAccountFather = uaB.IdUserAccount
join UserAccessGroupAssociation uagaA on uagaA.IdUserAccount = uaA.IdUserAccount
join UserAccessGroupAssociation uagaB on uagaB.IdUserAccount = uaB.IdUserAccount
join AccessGroup agA on agA.IdAccessGroup = uagaA.IdAccessGroup
join AccessGroup agB on agB.IdAccessGroup = uagaB.IdAccessGroup
where uagaA.IdAccessGroup = 10 and uagaB.IdAccessGroup = 9
[20/07/17 16:52:37] Clarissa Abreu: Quando você puder criar e dar acesso a Renato do BI, me avisa por favor
[21/07/17 13:44:09] douglasdevbr: select * from 
(
	select 1 as col1, 2 as col2 
	union all 
	select 3 as col1 ,4 as col2
)b
where b.col1 = b.col2
[24/07/17 13:37:26] douglasdevbr: select m.name,  amount, m.IdAcquirer,
(case when  dsDescriptor = 'cellphone_recharge' then 'venda de recarga' when dsDescriptor = 'par_concil_redepay' then 'conciliacao_parcial'
						   when dsDescriptor = 'concil_redepay' then 'conciliacao' when dsDescriptor = 'recharge' then 'venda de recarga' end) as tipo_transacao,
  convert(varchar(10), dtCreated, 103) as data_transacao, dtCreated from merchant m 
join merchantAccountBalance mb
on m.IdAcquirer  = mb.IdAcquirer
where month(dtCreated) = 7 
--and dsDescriptor = 'par_concil_redepay'
order by dtCreated,  m.idMerchant
[24/07/17 13:39:01] douglasdevbr: select m.name,  amount, m.IdAcquirer,
(case when  dsDescriptor = 'cellphone_recharge' then 'venda de recarga' when dsDescriptor = 'par_concil_redepay' then 'conciliacao_parcial'
						   when dsDescriptor = 'concil_redepay' then 'conciliacao' when dsDescriptor = 'recharge' then 'venda de recarga' end) as tipo_transacao,
  convert(varchar(10), dtCreated, 103) as data_transacao, dtCreated from merchant m 
join merchantAccountBalance mb
on m.IdAcquirer  = mb.IdAcquirer
where month(dtCreated) = 7 
and year(dtcreated) = 2017
--and dsDescriptor = 'par_concil_redepay'
order by dtCreated,  m.idMerchant
[26/07/17 18:58:06] Clarissa Abreu: Douglas, comecei a criar uma tela no SPLIT para fazer o Distribuidor visualizar tambem a Association (para conseguir ver os estabelecimentos e os status) através da IdCampaign que já tem na index que tá funcionando.
Tipo... ele visualiza as campanhas, e do lado de cada uma tem um botao que redireciona para outra tela que mostra a "association"  (os estabelecimentos participando da campanha e os status individuais)
[31/07/17 15:35:53] Clarissa Abreu: oi Douglas
[31/07/17 15:36:08] Clarissa Abreu: acabei de dar um checkin com a busca por status funcionando
[31/07/17 15:53:33] douglasdevbr: ok
[31/07/17 15:53:58] douglasdevbr: eu estou em casa hoje tive que levar no meu pai para fazer exames
[31/07/17 15:54:13] douglasdevbr: http://credenciamento.stone.com.br/docs/affiliate
[31/07/17 15:54:23] douglasdevbr: abre esse link
[31/07/17 15:54:42] douglasdevbr: da uma olhada no manual da integração da stone
[31/07/17 15:54:55] douglasdevbr: cria uma console app
[31/07/17 15:55:32] douglasdevbr: e tenta usar a api para cadastrar algum merchant passando valores fixos
[31/07/17 15:56:30] Clarissa Abreu: tá, vou tentar aqui
[01/08/17 16:34:43] Clarissa Abreu: update useraccount set IdSaleChannel = 1 where idsalechannel = 3
[01/08/17 16:52:05] douglasdevbr: https://first-web-scraper.readthedocs.io/en/latest/
[01/08/17 17:18:13] Clarissa Abreu: alter view Estabelecimento as
select convert(varchar(10), m.CreatedDate, 103) as 'Data Inicial', m.Document as 'CNPJ/CPF', m.CNAE, replace(upper(m.Name) ,'"','') as 'Nome Fantasia',  replace(upper(m.SocialReason) ,'"','') as 'Razão Social', upper(a.Street) as 'Rua', a.Number as 'Número', upper(a.Complement) as 'Complemento', upper(a.District) as 'Bairro', upper(c.Name) as 'Cidade', upper(e.Name) as 'Estado', a.Zip as 'CEP', upper(e.UF) as 'UF', m.Phone as 'Telefone Comercial', o.Phone as 'Telefone Residencial', o.Cellphone as 'Telefone Pessoal', upper(o.Name) as 'Contato', upper(o.Email) as 'Email', upper(ua.Name) as 'Responsável', 
(select SerialNumber + ' , ' +  LogicNumber + ' , ' + convert(varchar,Value/100) + ' ;   ' from Device where idMerchant = m.idMerchant for xml path('')) as 'Número Físico, Número Lógico e Valor Unitário',
(select sum(Value)/100 from Device where IdMerchant = m.IdMerchant group by IdMerchant) as 'Valor Total', th.Name as 'SITEF'
from Merchant m join Address a on a.IdMerchant = m.Idmerchant
join City c on c.IdCity = a.IdCity
join Estate e on e.IdEstate = a.IdEstate
join Owner o on o.IdMerchant = m.IdMerchant
join UserAccount ua on ua.IdUserAccount = m.IdAccountable
join tefhouse th on m.IdTefhouse = th.IdTefHouse
[01/08/17 17:20:10] Clarissa Abreu: É do chamado #000479
[01/08/17 17:20:22] Clarissa Abreu: Adição de CNAE
[02/08/17 14:05:50] douglasdevbr: USE [GenesisAero]
GO

/**** Object:  View [dbo].[PDV]    Script Date: 8/2/2017 2:05:31 PM ****/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

alter view [dbo].[PDV]
as
select convert(varchar(10), m.CreatedDate, 103) as 'Data Inicial', m.Document as 'CNPJ/CPF', replace(upper(m.Name) ,'"','') as 'Nome Fantasia',  replace(upper(m.SocialReason) ,'"','') as 'Razão Social', upper(a.Street) as 'Rua', a.Number as 'Número', upper(a.Complement) as 'Complemento', upper(a.District) as 'Bairro', upper(c.Name) as 'Cidade', upper(e.Name) as 'Estado', a.Zip as 'CEP', upper(e.UF) as 'UF', m.Phone as 'Telefone Comercial', o.Phone as 'Telefone Residencial', o.Cellphone as 'Telefone Pessoal', upper(o.Name) as 'Contato', upper(o.Email) as 'Email', upper(ua.Name) as 'Responsável', 
(select SerialNumber + ' , ' +  LogicNumber + ' , ' + convert(varchar,Value/100) + ' ;   ' from Device where idMerchant = m.idMerchant for xml path('')) as 'Número Físico, Número Lógico e Valor Unitário',
(select sum(Value)/100 from Device where IdMerchant = m.IdMerchant group by IdMerchant) as 'Valor Total'
from Merchant m join Address a on a.IdMerchant = m.Idmerchant
join City c on c.IdCity = a.IdCity
join Estate e on e.IdEstate = a.IdEstate
join Owner o on o.IdMerchant = m.IdMerchant
join UserAccount ua on ua.IdUserAccount = m.IdAccountable
GO
[02/08/17 14:20:23] Clarissa Abreu: create view Antecipacao as
select at.dtCreated, at.dtAnticipation, m.Document, m.SocialReason, at.vlTotalAmount, at.vlNetAmount, at.vlAcquirerFee, at.vlSpreadFee,
 at.vlAnticipationFee, at.idStatus from AnticipationTransaction at
join Merchant m on m.IdAcquirer = at.AcquirerID
[02/08/17 14:20:48] douglasdevbr: '''  images = response.css('img::attr(data-img)').extract()'''
[02/08/17 14:21:40] douglasdevbr: https://www.analyticsvidhya.com/blog/2017/07/web-scraping-in-python-using-scrapy/
[02/08/17 14:29:44] Clarissa Abreu: COM FILTRO STATUS 200

create view Antecipacao as
select at.dtCreated, at.dtAnticipation, m.Document, m.SocialReason, at.vlTotalAmount, at.vlNetAmount, at.vlAcquirerFee, at.vlSpreadFee,
 at.vlAnticipationFee, at.idStatus from AnticipationTransaction at
join Merchant m on m.IdAcquirer = at.AcquirerID
where at.idStatus = 200
[02/08/17 14:31:29] Clarissa Abreu: create view Antecipacao as
select at.dtCreated as 'Data de criação', at.dtAnticipation as 'Data da antecipação', m.Document as 'CNPJ', m.SocialReason as 'Razão social', at.vlTotalAmount, at.vlNetAmount, at.vlAcquirerFee, at.vlSpreadFee,
 at.vlAnticipationFee, at.idStatus from AnticipationTransaction at
join Merchant m on m.IdAcquirer = at.AcquirerID
where at.idStatus = 200
[03/08/17 17:42:32] Clarissa Abreu: alter view Estabelecimento as
select convert(varchar(10), m.CreatedDate, 103) as 'Data Inicial', m.Document as 'CNPJ/CPF', m.CNAE, replace(upper(m.Name) ,'"','') as 'Nome Fantasia',  replace(upper(m.SocialReason) ,'"','') as 'Razão Social', upper(a.Street) as 'Rua', a.Number as 'Número', upper(a.Complement) as 'Complemento', upper(a.District) as 'Bairro', upper(c.Name) as 'Cidade', upper(e.Name) as 'Estado', a.Zip as 'CEP', upper(e.UF) as 'UF', m.Phone as 'Telefone Comercial', 
o.Phone as 'Telefone Residencial', o.Cellphone as 'Telefone Pessoal', upper(o.Name) as 'Contato', upper(o.Email) as 'Email', 
upper(ua.Name) as 'Responsável', 
(select SerialNumber + ' , ' +  LogicNumber + ' , ' + convert(varchar,Value/100) + ' ;   ' from Device where idMerchant = m.idMerchant for xml path('')) as 'Número Físico, Número Lógico e Valor Unitário',
(select sum(Value)/100 from Device where IdMerchant = m.IdMerchant group by IdMerchant) as 'Valor Total', th.Name as 'SITEF'
from Merchant m join Address a on a.IdMerchant = m.Idmerchant
join City c on c.IdCity = a.IdCity
join Estate e on e.IdEstate = a.IdEstate
left join Owner o on o.IdMerchant = m.IdMerchant
join UserAccount ua on ua.IdUserAccount = m.IdAccountable
join tefhouse th on m.IdTefhouse = th.IdTefHouse
order by m.CreatedDate;
[03/08/17 18:08:23] Clarissa Abreu: alter view PoliticaComercial as 
select distinct m.Document as 'CNPJ/CPF',  replace(upper(m.SocialReason) ,'"','') as 'Razão Social',
cp.Name as 'Política Comercial'
from Merchant m 
left join Negotiation n on n.IdMerchant = m.IdMerchant
left join CommercialPolicy cp on cp.IdCommercialPolicy = n.IdCommercialPolicy
[04/08/17 13:43:48] douglasdevbr: re_citosbwx3070ln95ylt6mx3d8
[04/08/17 14:00:47] Clarissa Abreu: Douglas, avisa se Jocler  responder o email
[04/08/17 14:09:54] douglasdevbr: ok
[04/08/17 14:15:16] Clarissa Abreu: falei com magda e com christian
[04/08/17 14:15:23] Clarissa Abreu: eles disseram que é só com ele mesmo
[04/08/17 14:37:25] Clarissa Abreu: douglas
[04/08/17 14:37:30] douglasdevbr: oi
[04/08/17 14:38:08] Clarissa Abreu: Jocler mandou um áudio p christian dizendo que tem um estabelecimento cadastrado na stone com o nome REDEPAY e stoneCode 200682757
[04/08/17 14:38:19] Clarissa Abreu: ele tá perguntando se é isso
[04/08/17 14:38:37] douglasdevbr: ha blz vlw
[04/08/17 14:38:55] Clarissa Abreu: então é isso mesmo ne?
[04/08/17 14:39:12] douglasdevbr: não e isso nao
[04/08/17 14:39:22] Clarissa Abreu: vixe D:
[07/08/17 13:18:56] Clarissa Abreu: select convert(varchar(10), rt.DtCreated, 103) as 'Data da transação', rt.SerialNumber as 'Número de série', d.LogicNumber as 'Número lógico', 
m.Document as 'CNPJ/CPF', rt.Carrier as 'Operadora', rt.NuTotal as 'Valor da recarga', rt.NuBuyPrice as 'Valor de compra RedePay', 
(NuMerchantPrice - NuBuyPrice) as 'Repasse RedePay', rt.NuMerchantPrice 'Valor de compra Estabelecimento', 
(nuTotal - NuMerchantPrice) as 'Repasse Estabelecimento' 
from RechargeTransaction rt
join Merchant m on m.IdMerchant = rt.idMerchant
left join Device d on d.SerialNumber = rt.SerialNumber
[07/08/17 14:11:37] Clarissa Abreu: where (NuMerchantPrice - NuBuyPrice) <= 0
[07/08/17 14:52:22] douglasdevbr: create view vw_recarga_redepay
as
select convert(varchar(10), rt.DtCreated, 103) as 'Data da transação', rt.SerialNumber as 'Número de série', d.LogicNumber as 'Número lógico', 
m.Document as 'CNPJ/CPF', rt.Carrier as 'Operadora', rt.NuTotal as 'Valor da recarga', rt.NuBuyPrice as 'Valor de compra RedePay', 
(NuMerchantPrice - NuBuyPrice) as 'Repasse RedePay', rt.NuMerchantPrice 'Valor de compra Estabelecimento', 
(nuTotal - NuMerchantPrice) as 'Repasse Estabelecimento'
from RechargeTransaction rt
join Merchant m on m.IdMerchant = rt.idMerchant
left join Device d on d.SerialNumber = rt.SerialNumber
where rt.idstatus = 200 and rt.DtCreated >= '2017-03-01 00:00:00.000'
[07/08/17 14:58:33] douglasdevbr: http://200.221.196.98:8086/stone/login.jsf
[07/08/17 14:58:42] douglasdevbr: form["j_username"] = "273.601.108-23"
form["j_password"] = "magda141"
[07/08/17 15:21:53] douglasdevbr: https://github.com/douglasdevbr/datascrapper
[07/08/17 16:26:16] douglasdevbr: git remote add origin
[07/08/17 16:26:21] douglasdevbr: https://github.com/douglasdevbr/datascrapper.git
[07/08/17 16:40:56] douglasdevbr: https://github.com/douglasdevbr/datascrapper.git
[07/08/17 16:42:58] Clarissa Abreu: import requests, lxml.html
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