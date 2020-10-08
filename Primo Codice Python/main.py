print("CARTA-FORBICI-SASSO contro Rino")
premio = "un biscotto"
print("Se vincerai avrai diritto a " + premio)

print("\nCome ti chiami?")
nome = input()
print("Buona fortuna " + nome + ". Che vinca il migliore! ")

print("\nQuale arma scegli?")
armi = ["carta", "forbici", "sasso"]
for arma in armi:
        print(arma)
print("\nPremi 0 per Carta, 1 per Forbici o 2 per Sasso")
numero_scelto = int(input())
arma_scelta = armi[numero_scelto]
print("Hai scelto:" + arma_scelta)

arma_Rino = ""
if(arma_scelta == "carta"):
  arma_Rino = "forbice"
if(arma_scelta == "forbici"):
  arma_Rino = "sasso"
if(arma_scelta == "sasso"):
  arma_Rino = "carta"
print("\n...anche Rino ha fatto la sua scelta!")
print("\nPremi invio per scoprire se hai vinto!")
input()
print("Rino ha scelto " + arma_Rino)
print(nome + "HAI PERSO! Concentrati di più e vincerai!")
input()