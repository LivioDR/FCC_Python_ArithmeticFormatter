def arithmetic_arranger(problems, booleano = False):

  numeros_y_signos = []

  for problemas in problems:
    numeros_y_signos.append(problemas.split())
  
  for items in numeros_y_signos:
    if not items[1] == "+" and not items[1] == "-":
      return "Error: Operator must be '+' or '-'." 

  for items in numeros_y_signos:
    if len(items[0]) > 4 or len(items[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

  if len(numeros_y_signos) > 5:
    return "Error: Too many problems."
  
  #chequeo que sean numeros y los convierto de string a int
  for numeros in numeros_y_signos:
    try:
      numeros[0] = int(numeros[0])
      numeros[2] = int(numeros[2])
    except:
      return "Error: Numbers must only contain digits."


  # calculo los resultados
  resultados = []
  for problemas in numeros_y_signos:
    if problemas[1] == "+":
      resultados.append(problemas[0] + problemas[2])
    else:
      resultados.append(problemas[0] - problemas[2])

  # vuelvo a convertir todo a strings para concatenar
  for numeros in numeros_y_signos:
    numeros[0] = str(numeros[0])
    numeros[2] = str(numeros[2])
  

  for problemas in numeros_y_signos:
    diferencia = len(str(problemas[0])) - len(str(problemas[2]))

    if diferencia == -4:
      problemas[0] = "      " + problemas[0]
      problemas[2] = problemas[1] + " " + problemas[2]
    elif diferencia == -3:
      problemas[0] = "     " + problemas[0]
      problemas[2] = problemas[1] + " " + problemas[2]
    elif diferencia == -2:
      problemas[0] = "    " + problemas[0]
      problemas[2] = problemas[1] + " " + problemas[2]
    elif diferencia == -1:
      problemas[0] = "   " + problemas[0]
      problemas[2] = problemas[1] + " " + problemas[2]
    elif diferencia == 0:
      problemas[0] = "  " + problemas[0]
      problemas[2] = problemas[1] + " " + problemas[2]
    elif diferencia == 1:
      problemas[0] = "  " + problemas[0]
      problemas[2] = problemas[1] + "  " + problemas[2]
    elif diferencia == 2:
      problemas[0] = "  " + problemas[0]
      problemas[2] = problemas[1] + "   " + problemas[2]
    elif diferencia == 3:
      problemas[0] = "  " + problemas[0]
      problemas[2] = problemas[1] + "    " + problemas[2]
    elif diferencia == 4:
      problemas[0] = "  " + problemas[0]
      problemas[2] = problemas[1] + "     " + problemas[2]
    else:
      return "Error: Number too long."

  # creo el subrayado de los problemas
  subrayado = []
  for problemas in numeros_y_signos:
    lineas = len(problemas[0])
    subrayado.append("-" * lineas)

  # normalizo el largo del resultado
  numero_de_problemas = len(numeros_y_signos)
  i = 0
  while i < numero_de_problemas:
    diferencia = len(str(numeros_y_signos[i][0])) - len(str(resultados[i]))
    resultados[i] = " " * diferencia + str(resultados[i])
    i = i+1 

  # print(subrayado)


  linea_superior = []
  linea_inferior = []
  subrayado_inferior = []
  linea_resultado = []

  #concateno
  for problemas in numeros_y_signos:
    linea_superior.append(problemas[0])
    linea_inferior.append(problemas[2])
  

  linea_superior = "    ".join(map(str,linea_superior))
  # print(linea_superior)
  linea_inferior = "    ".join(map(str,linea_inferior))
  subrayado_inferior = "    ".join(map(str,subrayado))
  linea_resultado = "    ".join(map(str,resultados))

  arranged_problems = linea_superior + "\n" + linea_inferior + "\n" + subrayado_inferior
  print(arranged_problems)

  if booleano:
    arranged_problems = arranged_problems + "\n" + linea_resultado

  return arranged_problems