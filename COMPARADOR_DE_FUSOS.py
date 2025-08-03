#coding: utf-8
from datetime import datetime
from pytz import timezone
print("+---------------------------+")
print("|    COMPARADOR DE FUSOS    |")
print("+---------------------------+")
print()
intCont = 1
while intCont>0:
	print("Digite 1 para converter o horário atual")
	print("Digite 2 para converter um horário específico")
	while True:
		stroption = input("Sua escolha: ")
		print()
		print()
		if stroption == "1":
			paisinicial = str(input("Escolha o país atual: "))
			paisfinal = str(input("Escolha o país a ser comparado: "))
			paisinicial = paisinicial.lower()
			paisfinal = paisfinal.lower()
			paisinicial = paisinicial.strip()
			paisfinal = paisfinal.strip()
			print()
			confirma = str(input("Pressione ENTER para confirmar "))
			print ()
			if confirma == "lista":
				import pytz
				for tz in pytz.all_timezones:
					print(tz)
				break
			if paisfinal == paisinicial:
				print("Selecione países diferentes")
				break
				
				
			elif paisinicial == "brasil" and paisfinal == "mexico" or paisfinal == "méxico":
				data_e_hora_atuais = datetime.now()
				fuso_horario = timezone('America/Sao_Paulo')
				data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
				data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')
				data_e_hora_atuais = datetime.now()
				fuso_horario = timezone('America/Mexico_City')
				data_e_hora_mexico_city = data_e_hora_atuais.astimezone(fuso_horario)
				data_e_hora_mexico_city_em_texto = data_e_hora_mexico_city.strftime('%d/%m/%Y %H:%M')
				print("Brasil: {}".format(data_e_hora_sao_paulo_em_texto))
				print("México: {}".format(data_e_hora_mexico_city_em_texto))
				break
			elif paisinicial == "mexico" or paisinicial == "méxico" and paisfinal == "brasil":
				data_e_hora_atuais = datetime.now()
				fuso_horario = timezone('America/Mexico_City')
				data_e_hora_mexico_city = data_e_hora_atuais.astimezone(fuso_horario)
				data_e_hora_mexico_city_em_texto = data_e_hora_mexico_city.strftime('%d/%m/%Y %H:%M')
				data_e_hora_atuais = datetime.now()
				fuso_horario = timezone('America/Sao_Paulo')
				data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
				data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')
				print("México: {}".format(data_e_hora_mexico_city_em_texto))
				print("Brasil: {}".format(data_e_hora_sao_paulo_em_texto))
				break

			elif paisinicial == "brasil" and paisfinal == "chile":
				data_e_hora_atuais = datetime.now()
				fuso_horario = timezone('America/Sao_Paulo')
				data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
				data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')
				data_e_hora_atuais = datetime.now()
				fuso_horario = timezone('America/Santiago')
				data_e_hora_santiago = data_e_hora_atuais.astimezone(fuso_horario)
				data_e_hora_santiago_em_texto = data_e_hora_santiago.strftime('%d/%m/%Y %H:%M')
				print("Brasil: {}".format(data_e_hora_sao_paulo_em_texto))
				print("Chile:  {}".format(data_e_hora_santiago_em_texto))
				break
			elif paisinicial == "chile" and paisfinal == "brasil":
				data_e_hora_atuais = datetime.now()
				fuso_horario = timezone('America/Santiago')
				data_e_hora_santiago = data_e_hora_atuais.astimezone(fuso_horario)
				data_e_hora_santiago_em_texto = data_e_hora_santiago.strftime('%d/%m/%Y %H:%M')
				data_e_hora_atuais = datetime.now()
				fuso_horario = timezone('America/Sao_Paulo')
				data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
				data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')
				print("Chile:  {}".format(data_e_hora_santiago_em_texto))
				print("Brasil: {}".format(data_e_hora_sao_paulo_em_texto))
				break
				
			elif paisinicial == "brasil" and paisfinal == "peru":
				data_e_hora_atuais = datetime.now()
				fuso_horario = timezone('America/Sao_Paulo')
				data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
				data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')
				data_e_hora_atuais = datetime.now()
				fuso_horario = timezone('America/Lima')
				data_e_hora_lima = data_e_hora_atuais.astimezone(fuso_horario)
				data_e_hora_lima_em_texto = data_e_hora_lima.strftime('%d/%m/%Y %H:%M')
				print("Brasil: {}".format(data_e_hora_sao_paulo_em_texto))
				print("Peru:   {}".format(data_e_hora_lima_em_texto))
				break
			elif paisinicial == "peru" and paisfinal == "brasil":
				data_e_hora_atuais = datetime.now()
				fuso_horario = timezone('America/Lima')
				data_e_hora_lima = data_e_hora_atuais.astimezone(fuso_horario)
				data_e_hora_lima_em_texto = data_e_hora_lima.strftime('%d/%m/%Y %H:%M')
				data_e_hora_atuais = datetime.now()
				fuso_horario = timezone('America/Sao_Paulo')
				data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
				data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')
				print("Peru:   {}".format(data_e_hora_lima_em_texto))
				print("Brasil: {}".format(data_e_hora_sao_paulo_em_texto))
				break
				
			else:
				print ("País(es) não encontrado(s)")
				print ()
				break
				
		elif stroption == "2":
			paisinicial = str(input("Escolha o país atual: "))
			paisfinal = str(input("Escolha o país a ser comparado: "))
			paisinicial = paisinicial.lower()
			paisfinal = paisfinal.lower()
			paisinicial = paisinicial.strip()
			paisfinal = paisfinal.strip()
			print()
			horario = input("Digite as horas no formato 24hrs(hh:mm): ")
			horas = horario[0]+horario[1]
			minutos = horario[3]+horario[4]
			if horas == "00":
				horas = 0
			elif horas == "01":
				horas = 1
			elif horas == "02":
				horas = 2
			elif horas == "03":
				horas = 3
			elif horas == "04":
				horas = 4
			elif horas == "05":
				horas = 5
			elif horas == "06":
				horas = 6
			elif horas == "07":
				horas = 7
			elif horas == "08":
				horas = 8
			elif horas == "09":
				horas = 9
			elif horas == "10":
				horas = 10
			elif horas == "11":
				horas = 11
			elif horas == "12":
				horas = 12
			elif horas == "13":
				horas = 13
			elif horas == "14":
				horas = 14
			elif horas == "15":
				horas = 15
			elif horas == "16":
				horas = 16
			elif horas == "17":
				horas = 17
			elif horas == "18":
				horas = 18
			elif horas == "19":
				horas = 19
			elif horas == "20":
				horas = 20
			elif horas == "21":
				horas = 21
			elif horas == "22":
				horas = 22
			elif horas == "23":
				horas = 23
			elif horas =="24":
				horas = 24
			
			if horas == 0 or horas == 1 or horas == 2 or horas == 3 or horas == 4 or horas == 5 or horas == 6 or horas == 7 or horas == 8 or horas == 9 or horas == 10 or horas == 11 or horas == 12 or horas == 13 or horas == 14 or horas == 15 or horas == 16 or horas == 17 or horas == 18 or horas == 19 or horas == 20 or horas == 21 or horas == 22 or horas == 23 or horas == 24 and horario[3] == "0" or horario[3] == "1" or horario[3] == "2" or horario[3] == "3" or horario[3] == "4" or horario[3] == "5" or horario[3] == "6" or horario[3] == "7" or horario[3] == "8" or horario[3] == "9":
				
				if paisinicial == "brasil" and paisfinal == "méxico" or paisfinal == "mexico":
					#horário de verão -3 / horário normal -2
					if horas == 0:
						horas = 21
						print()
						print("Brasil: {}".format(horario))
						print("México: {}:{}".format(horas,minutos))
					elif horas == 1:
						horas = 22
						print()
						print("Brasil: {}".format(horario))
						print("México: {}:{}".format(horas,minutos))
					elif horas == 2:
						horas = 23
						print()
						print("Brasil: {}".format(horario))
						print("México: {}:{}".format(horas,minutos))
					elif horas == 13:
						horas-=3
						print()
						print("Brasil: {}".format(horario))
						print("México: {}:{}".format(horas,minutos))
					elif horas == 14:
						horas-=3
						print()
						print("Brasil: {}".format(horario))
						print("México: {}:{}".format(horas,minutos))
					elif horas == 15:
						horas-=3
						print()
						print("Brasil: {}".format(horario))
						print("México: {}:{}".format(horas,minutos))
					elif horas == 16:
						horas-=3
						print()
						print("Brasil: {}".format(horario))
						print("México: {}:{}".format(horas,minutos))
					elif horas == 17:
						horas-=3
						print()
						print("Brasil: {}".format(horario))
						print("México: {}:{}".format(horas,minutos))
					elif horas == 18:
						horas-=3
						print()
						print("Brasil: {}".format(horario))
						print("México: {}:{}".format(horas,minutos))
					elif horas == 19:
						horas-=3
						print()
						print("Brasil: {}".format(horario))
						print("México: {}:{}".format(horas,minutos))
					elif horas == 20:
						horas-=3
						print()
						print("Brasil: {}".format(horario))
						print("México: {}:{}".format(horas,minutos))
					elif horas == 21:
						horas-=3
						print()
						print("Brasil: {}".format(horario))
						print("México: {}:{}".format(horas,minutos))
					elif horas == 22:
						horas-=3
						print()
						print("Brasil: {}".format(horario))
						print("México: {}:{}".format(horas,minutos))
					elif horas == 23:
						horas-=3
						print()
						print("Brasil: {}".format(horario))
						print("México: {}:{}".format(horas,minutos))
					elif horas == 24:
						horas-=3
						print()
						print("Brasil: {}".format(horario))
						print("México: {}:{}".format(horas,minutos))
					else:
						horas -= 3
						print()
						print("Brasil: {}".format(horario))
						print("México: 0{}:{}".format(horas,minutos))
					break

				if paisinicial == "mexico" or paisinicial == "méxico" and paisfinal == "brasil":
					#horário de verão -3 / horário normal -2
					if horas ==24:
						horas = 3
						print()
						print("México: {}".format(horario))
						print("Brasil: 0{}:{}".format(horas,minutos))
					elif horas == 23:
						horas = 2
						print()
						print("México: {}".format(horario))
						print("Brasil: 0{}:{}".format(horas,minutos))
					elif horas == 22:
						horas = 1
						print()
						print("México: {}".format(horario))
						print("Brasil: 0{}:{}".format(horas,minutos))
					elif horas == 7:
						horas+=3
						print()
						print("México: {}".format(horario))
						print("Brasil: {}:{}".format(horas,minutos))
					elif horas == 8:
						horas+=3
						print()
						print("México: {}".format(horario))
						print("Brasil: {}:{}".format(horas,minutos))
					elif horas == 9:
						horas+=3
						print()
						print("México: {}".format(horario))
						print("Brasil: {}:{}".format(horas,minutos))
					elif horas == 10:
						horas+=3
						print()
						print("México: {}".format(horario))
						print("Brasil: {}:{}".format(horas,minutos))
					elif horas == 11:
						horas+=3
						print()
						print("México: {}".format(horario))
						print("Brasil: {}:{}".format(horas,minutos))
					elif horas == 12:
						horas+=3
						print()
						print("México: {}".format(horario))
						print("Brasil: {}:{}".format(horas,minutos))
					elif horas == 13:
						horas+=3
						print()
						print("México: {}".format(horario))
						print("Brasil: {}:{}".format(horas,minutos))
					elif horas == 14:
						horas+=3
						print()
						print("México: {}".format(horario))
						print("Brasil: {}:{}".format(horas,minutos))
					elif horas == 15:
						horas+=3
						print()
						print("México: {}".format(horario))
						print("Brasil: {}:{}".format(horas,minutos))
					elif horas == 16:
						horas+=3
						print()
						print("México: {}".format(horario))
						print("Brasil: {}:{}".format(horas,minutos))
					elif horas == 17:
						horas+=3
						print()
						print("México: {}".format(horario))
						print("Brasil: {}:{}".format(horas,minutos))
					elif horas == 18:
						horas+=3
						print()
						print("México: {}".format(horario))
						print("Brasil: {}:{}".format(horas,minutos))
					elif horas == 19:
						horas+=3
						print()
						print("México: {}".format(horario))
						print("Brasil: {}:{}".format(horas,minutos))
					elif horas == 20:
						horas+=3
						print()
						print("México: {}".format(horario))
						print("Brasil: {}:{}".format(horas,minutos))
					elif horas == 21:
						horas+=3
						print()
						print("México: {}".format(horario))
						print("Brasil: {}:{}".format(horas,minutos))
					else:
						horas+=3
						print()
						print("México: {}".format(horario))
						print("Brasil: 0{}:{}".format(horas,minutos))
					break
						
						
						
				elif paisinicial == "brasil" and paisfinal == "peru":
					if horas == 0:
						horas = 22
						print()
						print("Brasil: {}".format(horario))
						print("Peru:   {}:{}".format(horas,minutos))
					elif horas == 1:
						horas = 23
						print()
						print("Brasil: {}".format(horario))
						print("Peru:   {}:{}".format(horas,minutos))
					elif horas == 2:
						horas = 0
						print()
						print("Brasil: {}".format(horario))
						print("Peru:   0{}:{}".format(horas,minutos))
					elif horas == 12:
						horas-=2
						print()
						print("Brasil: {}".format(horario))
						print("Peru:   {}:{}".format(horas,minutos))
					elif horas == 13:
						horas-=2
						print()
						print("Brasil: {}".format(horario))
						print("Peru:   {}:{}".format(horas,minutos))
					elif horas == 14:
						horas-=2
						print()
						print("Brasil: {}".format(horario))
						print("Peru:   {}:{}".format(horas,minutos))
					elif horas == 15:
						horas-=2
						print()
						print("Brasil: {}".format(horario))
						print("Peru:   {}:{}".format(horas,minutos))
					elif horas == 16:
						horas-=2
						print()
						print("Brasil: {}".format(horario))
						print("Peru:   {}:{}".format(horas,minutos))
					elif horas == 17:
						horas-=2
						print()
						print("Brasil: {}".format(horario))
						print("Peru:   {}:{}".format(horas,minutos))
					elif horas == 18:
						horas-=2
						print()
						print("Brasil: {}".format(horario))
						print("Peru:   {}:{}".format(horas,minutos))
					elif horas == 19:
						horas-=2
						print()
						print("Brasil: {}".format(horario))
						print("Peru:   {}:{}".format(horas,minutos))
					elif horas == 20:
						horas-=2
						print()
						print("Brasil: {}".format(horario))
						print("Peru:   {}:{}".format(horas,minutos))
					elif horas == 21:
						horas-=2
						print()
						print("Brasil: {}".format(horario))
						print("Peru:   {}:{}".format(horas,minutos))
					elif horas == 22:
						horas-=2
						print()
						print("Brasil: {}".format(horario))
						print("Peru:   {}:{}".format(horas,minutos))
					elif horas == 23:
						horas-=2
						print()
						print("Brasil: {}".format(horario))
						print("Peru:   {}:{}".format(horas,minutos))
					elif horas == 24:
						horas-=2
						print()
						print("Brasil: {}".format(horario))
						print("Peru:   {}:{}".format(horas,minutos))
					else:
						horas -= 2
						print()
						print("Brasil: {}".format(horario))
						print("Peru:   0{}:{}".format(horas,minutos))
					break

				elif paisinicial == "peru" and paisfinal == "brasil":
					if horas ==24:
						horas = 2
						print()
						print("peru:   {}".format(horario))
						print("Brasil: 0{}:{}".format(horas,minutos))
					elif horas == 23:
						horas = 1
						print()
						print("Peru:   {}".format(horario))
						print("Brasil: 0{}:{}".format(horas,minutos))
					elif horas == 22:
						horas = 0
						print()
						print("Peru:   {}".format(horario))
						print("Brasil: 0{}:{}".format(horas,minutos))
					elif horas == 8:
						horas+=2
						print()
						print("Peru:   {}".format(horario))
						print("Brasil: {}:{}".format(horas,minutos))
					elif horas == 9:
						horas+=2
						print()
						print("Peru:   {}".format(horario))
						print("Brasil: {}:{}".format(horas,minutos))
					elif horas == 10:
						horas+=2
						print()
						print("Peru:   {}".format(horario))
						print("Brasil: {}:{}".format(horas,minutos))
					elif horas == 11:
						horas+=2
						print()
						print("Peru:   {}".format(horario))
						print("Brasil: {}:{}".format(horas,minutos))
					elif horas == 12:
						horas+=2
						print()
						print("Peru:   {}".format(horario))
						print("Brasil: {}:{}".format(horas,minutos))
					elif horas == 13:
						horas+=2
						print()
						print("Peru:   {}".format(horario))
						print("Brasil: {}:{}".format(horas,minutos))
					elif horas == 14:
						horas+=2
						print()
						print("Peru:   {}".format(horario))
						print("Brasil: {}:{}".format(horas,minutos))
					elif horas == 15:
						horas+=2
						print()
						print("Peru:   {}".format(horario))
						print("Brasil: {}:{}".format(horas,minutos))
					elif horas == 16:
						horas+=2
						print()
						print("Peru:   {}".format(horario))
						print("Brasil: {}:{}".format(horas,minutos))
					elif horas == 17:
						horas+=2
						print()
						print("Peru:   {}".format(horario))
						print("Brasil: {}:{}".format(horas,minutos))
					elif horas == 18:
						horas+=2
						print()
						print("Peru:   {}".format(horario))
						print("Brasil: {}:{}".format(horas,minutos))
					elif horas == 19:
						horas+=2
						print()
						print("Peru:   {}".format(horario))
						print("Brasil: {}:{}".format(horas,minutos))
					elif horas == 20:
						horas+=2
						print()
						print("Peru:   {}".format(horario))
						print("Brasil: {}:{}".format(horas,minutos))
					elif horas == 21:
						horas+=2
						print()
						print("Peru:   {}".format(horario))
						print("Brasil: {}:{}".format(horas,minutos))
					else:
						horas+=2
						print()
						print("Peru: {}".format(horario))
						print("Brasil: 0{}:{}".format(horas,minutos))
					break


				elif paisinicial == "brasil" and paisfinal == "chile":
					print()
					print("Brasil: {}".format(horario))
					print("Chile:  {}".format(horario))
					break
						
				elif paisinicial == "chile" and paisfinal == "brasil":
					print()
					print("Chile:  {}".format(horario))
					print("Brasil: {}".format(horario))
					break
					


				else:
					print ()
					print ("País(es) não encontrado(s)")
					print ()
					break
			else:
				print()
				print("Erro, valor de horas e/ou minutos inválido(s)")
				print()
				break
		else:
			print("Opção não existente!")
			print()
			print()
			
	while True:
		print()
		controledeloop = input("Deseja continuar comparando fusos?[s/n]: ")
		if controledeloop == "s" or controledeloop == "S":
			print(".")
			print(".")
			print(".")
			print(".")
			break
			intCont = 1
		elif controledeloop == "n" or controledeloop == "N":
			print(".")
			print(".")
			print(".")
			print(".")
			print("OBRIGADO POR USAR ESSE PROGRAMA")
			print("Desenvolvido por Hiago da Silva")
			input()
			intCont = 0
			break
		else:
			print ("Erro, tente novamente")
			print()
