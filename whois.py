import whois

dominio = input("target: ")
consulta_whois = whois.whois(dominio)

# print consulta whois 
print (consulta_whois.text)