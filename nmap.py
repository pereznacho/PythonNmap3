import nmap3
import os


if os.geteuid()==0:
  print("[*] Se está ejecutando como ROOT!")
else:
  print("Debe ejecutar el script como ROOT!")
  exit()

nmscan = nmap3.Nmap()

print("Bienvenido a mi primer escaner de puerto")

ip_addr = input("Por favor inserte la ip a escanear: ")

print ("La ip insertada es: ", ip_addr)

type(ip_addr)
outFile = (ip_addr + ".nmap")

opcion = input ("""\nPorfavor seleccione el tipo de escaneo
[*] 1) Escaneo simple
[*] 2) Escaneo que muestre el sistema operativo
[*] 3) Escaneo que ejecuta scripts de vulnerabilidades \n""")

print ("su seleccion fue: ", opcion)

if opcion =="1":
	print("Escaneo básico de puertos: ")
	print("Nmap Version: ", nmscan.nmap_version())
	nmscan.scan_top_ports(ip_addr)
	results = nmscan.scan_top_ports(ip_addr, args="-sV -oN {}.nmap".format(outFile))
	print(results)
	print(nmscan.scaninfo())




elif opcion =="2":
	print("Escaneo que muestre el sistema operativo: ")
#	print("Nmap Version: ", nmscan.nmap_version())
	nmscan.nmap_os_detection(ip_addr)
	os_results = nmscan.nmap_os_detection(ip_addr, args=" -oN {}.nmap".format(outFile))
	print(os_results)



elif opcion =="3":
	print("Escaneo que ejecuta scripts de vulnerabilidades: ")
	nmscan.nmap_version_detection(ip_addr)
	vulns_results = nmscan.nmap_version_detection(ip_addr, args="--script vuln -oN {}.nmap".format(outFile))
	print(vulns_results)
	

