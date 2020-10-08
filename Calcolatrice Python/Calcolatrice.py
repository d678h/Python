while True:

  print('''
  Benvenuto al programma Calcolatrice!
  Creata da: d678h
  Di seguito un elenco delle varie funzioni disponibili:
  
  -Per effettuare un'Addizione, seleziona 1;
  -Per effettuare una Sottrazione, seleziona 2;
  -Per effettuare una Moltiplicazione, seleziona 3;
  -Per effettuare una Divisione, seleziona 4;
  -Per effettuare un Calcolo Esponenziale, seleziona 5;
  -Per uscire dal programma puoi digitare ESC.
  ''')
  scelta = input('Inserici il numero corrispondente all\'azione desiderata ---> ')

  if scelta == "1":
    print('\nHai scelto: Addizione')
    a = float(input('\nInserisci il primo numero -> '))
    b = float(input('\nInserisci il secondo numero -> '))
    print('\nIl risultato della Somma e\': ' + str(a + b))
  elif scelta == "2":
    print('\nHai scelto: Sottrazione')
    a = float(input('\nInserisci il primo numero -> '))
    b = float(input('\nInserisci il secondo numero -> '))
    print('\nIl risultato della Sottrazione e\': ' + str(a - b))
  elif scelta == "3":
    print('\nHai scelto: Moltiplicazione')
    a = float(input('\nInserisci il primo numero -> '))
    b = float(input('\nInserisci il secondo numero -> '))
    print('\nIl risultato della Moltiplicazione e\': ' + str(a * b))
  elif scelta == "4":
    print('\nHai scelto: Divisione')
    a = float(input('\nInserisci il primo numero -> '))
    b = float(input('\nInserisci il secondo numero -> '))
    print('\nIl risultato della Divisione e\': ' + str(a / b))
  elif scelta == "5":
    print('\nHai scelto: Calcolo Esponenziale')
    a = float(input('\nInserisci la base -> '))
    b = float(input('\nInserisci l\'esponente -> '))
    print('\nIl risultato del Calcolo Esponenziale e\': ' + str(a ** b))
  elif scelta == "ESC":
    break

  loop = input('\nDesideri continuare ad usare l\'applicazione? S/N')
  if loop == "S" or loop == "s":
    continue
  else:
    break







