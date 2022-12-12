from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

inicio = time.time()
tiempo_total = 0

print('leyendo el txt....')
archivotxt = open ('insumo.txt','r', encoding='utf8')
print('1. El archivo contiene los siguientes datos:\n')
lineas_text = archivotxt.readlines()
print(lineas_text)

for i in lineas_text:
		lineaPorLinea = i.split("\n")
		print(lineaPorLinea[0])



#datos del txt en variables
cliente1 = str(lineas_text[0])
cliente2 = str(lineas_text[1])
cliente3 = str(lineas_text[2])
cliente4 = str(lineas_text[3])
cliente5 = str(lineas_text[4])
print('\n')

print(f'2. El numero de filas en el archivo es de: {len(lineas_text)}\n')

print('3. Datos de los asociados:\n')
print('Asociado 1')
cadena1 = cliente1
separador = "-"
separado_por_guion = cadena1.split(separador)

#print(f'Primer Nombre: {separado_por_guion}')

print(f'Primer Nombre: {separado_por_guion[0]}')
nombre1 = separado_por_guion[0]

print(f'Segundo Nombre: {separado_por_guion[1]}')
nombre2 = separado_por_guion[1]

print(f'Primer Apellido: {separado_por_guion[2]}')
apellido1 = separado_por_guion[2]

print(f'Segundo Apellido: {separado_por_guion[3]}')
apellido2 = separado_por_guion[3]

print(f'Telefono: {separado_por_guion[4]}')
telefono1 = separado_por_guion[4]

print(f'Fecha de ingreso: {separado_por_guion[5]}')
fechaIngreso = separado_por_guion[5]
print('\n')

#///////////////////
print('Asociado 2')
cadena2 = cliente2
separado_por_guion = cadena2.split(separador)

print(f'Primer Nombre: {separado_por_guion[0]}')
nombre1 = separado_por_guion[0]

print(f'Segundo Nombre: {separado_por_guion[1]}')
nombre2 = separado_por_guion[1]

print(f'Primer Apellido: {separado_por_guion[2]}')
apellido1 = separado_por_guion[2]

print(f'Segundo Apellido: {separado_por_guion[3]}')
apellido2 = separado_por_guion[3]

print(f'Telefono: {separado_por_guion[4]}')
telefono = separado_por_guion[4]

print(f'Fecha de ingreso: {separado_por_guion[5]}')
fechaIngreso = separado_por_guion[5]
print('\n')

#///////////////////
print('Asociado 3')
cadena3 = cliente3
separado_por_guion = cadena3.split(separador)

print(f'Primer Nombre: {separado_por_guion[0]}')
nombre1 = separado_por_guion[0]

print(f'Segundo Nombre: {separado_por_guion[1]}')
nombre2 = separado_por_guion[1]

print(f'Primer Apellido: {separado_por_guion[2]}')
apellido1 = separado_por_guion[2]

print(f'Segundo Apellido: {separado_por_guion[3]}')
apellido2 = separado_por_guion[3]

print(f'Telefono: {separado_por_guion[4]}')
telefono = separado_por_guion[4]

print(f'Fecha de ingreso: {separado_por_guion[5]}')
fechaIngreso = separado_por_guion[5]
print('\n')

#///////////////////
print('Asociado 4')
cadena4 = cliente4
separado_por_guion = cadena4.split(separador)

print(f'Primer Nombre: {separado_por_guion[0]}')
nombre1 = separado_por_guion[0]

print(f'Segundo Nombre: {separado_por_guion[1]}')
nombre2 = separado_por_guion[1]

print(f'Primer Apellido: {separado_por_guion[2]}')
apellido1 = separado_por_guion[2]

print(f'Segundo Apellido: {separado_por_guion[3]}')
apellido2 = separado_por_guion[3]

print(f'Telefono: {separado_por_guion[4]}')
telefono = separado_por_guion[4]

print(f'Fecha de ingreso: {separado_por_guion[5]}')
fechaIngreso = separado_por_guion[5]
print('\n')

#///////////////////
print('Asociado 5')
cadena5 = cliente5
separado_por_guion = cadena5.split(separador)
#print(f'Primer Nombre: {separado_por_guion}')

print(f'Primer Nombre: {separado_por_guion[0]}')
nombre1 = separado_por_guion[0]

print(f'Segundo Nombre: {separado_por_guion[1]}')
nombre2 = separado_por_guion[1]

print(f'Primer Apellido: {separado_por_guion[2]}')
apellido1 = separado_por_guion[2]

print(f'Segundo Apellido: {separado_por_guion[3]}')
apellido2 = separado_por_guion[3]

print(f'Telefono: {separado_por_guion[4]}')
telefono = separado_por_guion[4]

print(f'Fecha de ingreso: {separado_por_guion[5]}')
fechaIngreso = separado_por_guion[5]
print('\n')


#///////////////////////Chrome web driver
options = webdriver.ChromeOptions()
s=Service(r"\WebDriverChrome\chromedriver.exe")
print("Inicializando navegador......")
driver = webdriver.Chrome(service=s)


driver.get("https://www.way2automation.com/way2auto_jquery/index.php")
print("Navegador Inicializado")
time.sleep(10)
#driver.close()

#//Envio del nombre
print('Enviando el nombre del usuario ....\n')
nombre = '/html/body/div[4]/div/div/div/div/div/form/fieldset[1]/input'
#nombre = 'name'
#nombre = '//*[@id="load_form"]/fieldset[1]/input'
WebDriverWait(driver, 6)\
    .until(EC.visibility_of_element_located((By.XPATH, nombre)))
driver.find_element(By.XPATH, nombre).send_keys(nombre1)
print('Nombre del usuario  enviado\n')
time.sleep(2)
#xpath = '/html/body/div[4]/div/div/div/div/div/form/fieldset[1]/input'

#Envio del telefono
print('Enviando el telefono del usuario ....\n')
telefono = '/html/body/div[4]/div/div/div/div/div/form/fieldset[2]/input'
WebDriverWait(driver, 6)\
    .until(EC.visibility_of_element_located((By.XPATH, telefono)))
driver.find_element(By.XPATH, telefono).send_keys(telefono1)
print('Telefono del usuario  enviado\n')
time.sleep(2)

#Envio del email
print('Enviando el mail del usuario ....\n')
email = '/html/body/div[4]/div/div/div/div/div/form/fieldset[3]/input'
WebDriverWait(driver, 6)\
    .until(EC.visibility_of_element_located((By.XPATH, email)))
driver.find_element(By.XPATH, email).send_keys(nombre1+'@'+apellido1+'.com')
print('Telefono del usuario enviado\n')
time.sleep(2)

#Envio del pais
print('Enviando el pais del usuario ....\n')
pais = '/html/body/div[4]/div/div/div/div/div/form/fieldset[4]/select'
WebDriverWait(driver, 6)\
    .until(EC.visibility_of_element_located((By.XPATH, pais)))
driver.find_element(By.XPATH, pais).send_keys('Egypt')
print('Pais del usuario enviado\n')
time.sleep(2)


#Envio de la ciudad
print('Enviando la ciudad del usuario ....\n')
city = '/html/body/div[4]/div/div/div/div/div/form/fieldset[5]/input'
WebDriverWait(driver, 6)\
    .until(EC.visibility_of_element_located((By.XPATH, city)))
driver.find_element(By.XPATH, city).send_keys('El Cairo')
print('Ciudad del usuario enviado\n')
time.sleep(2)


#Envio del username
print('Enviando el user del cliente ....\n')
username= '/html/body/div[4]/div/div/div/div/div/form/fieldset[6]/input'
WebDriverWait(driver, 6)\
    .until(EC.visibility_of_element_located((By.XPATH, username)))
driver.find_element(By.XPATH, username).send_keys(nombre1[0:2]+apellido1[0:2])
print('user del cliente enviado\n')
time.sleep(2)

#Envio del password
print('Enviando el password del usuario ....\n')
password = '/html/body/div[4]/div/div/div/div/div/form/fieldset[7]/input'
WebDriverWait(driver, 6)\
    .until(EC.visibility_of_element_located((By.XPATH, password)))
driver.find_element(By.XPATH, password).send_keys('admin123')
print('password del usuario enviado\n')
time.sleep(2)


#click en submit
print('Enviando la informacion ....\n')
submit = '/html/body/div[4]/div/div/div/div/div/form/div[1]/div[2]/input'
WebDriverWait(driver, 4)\
	.until(EC.element_to_be_clickable((By.XPATH, submit)))
driver.find_element(By.XPATH, submit).click()

#////Captura del alert

alert = '/html/body/div[4]/div/div/div/div/div/form/p'
WebDriverWait(driver, 9)\
	.until(EC.visibility_of_element_located((By.XPATH, alert)))
mensaje = driver.find_element(By.XPATH,alert)
str(mensaje.text)
print(f'El mensaje retornado fue: {mensaje.text}')
time.sleep(4)

# ////calcular el tiempo de ejecucion del script
fin = time.time()
tiempo_total = fin - inicio
print(f'El tiempo de ejecucion de este ciclo fue de {tiempo_total:.2f} segundos')
driver.close()
