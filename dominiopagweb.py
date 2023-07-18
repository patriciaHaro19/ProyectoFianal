import whois

# Dominio a buscar
domain = "https://unir.com"

try:
  # Consulta de quién es el registro de dominio
  w = whois.whois(domain)
  
  # Mostrar el nombre del dominio
  print("El dominio es: ", w.domain_name)
  
except Exception as e:
  print("Error: ", e)
