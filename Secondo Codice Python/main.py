print("Ciao mondo, sono Bot U.U")

messaggio_simpatico = "Oggi mi sento particolarmente Atzeco!"
print(messaggio_simpatico)

cibo_preferito = "la pizza"
print("Il mio cibo preferito è " + cibo_preferito)

print("\nHey tu, come ti chiami?")
nome = input()
print("\nCiao " + nome + " dispiacere di conoscerti")

if(nome == "pippo"):
  print("Che nome di schifo")
else:
  print("\nBellissimo nome, complimenti hai tuoi genitori adottivi")

lunghezza_nome = len(nome)
lunghezza_nome_stringa = str(lunghezza_nome)
print("\nIl tuo nome ha " + lunghezza_nome_stringa + " lettere")

anno_di_nascita = input("\nIn che anno sei nato?")
anno_di_nascita_int = int(anno_di_nascita)
anno_corrente = input("\nInche anno ci troviamo?")
anno_corrente_int = int(anno_corrente)
eta = anno_corrente_int - anno_di_nascita_int
print(nome + " hai esattamente " + str(eta) + " anni...")

if(eta < 18 ):
  print("...beato te!!")
  anni_da_compiere = eta + 1
  print("\nL'anno prossimo avrai " + str(anni_da_compiere) + " anni...")
else:
  print("...sei proprio in vecchietto! :P")
  
  
risposta = ""
while(risposta != "chi è?"):
  print("\ntoc toc...")
  risposta = input()
print("Mago Merlino")

animali = ["gatto" , "cane" , "topo" , "procione" , "ornitorinco fatto"]
print("\nQual e il tuo animale preferito?")
for animale in animali:
  print(animale)
print("...indicalo con un numero da 0 a 4")
numero_animale = int(input())
if(numero_animale < 0 or numero_animale > 4):
  print("Non hai capito niente, sei piu stupido di un sasso")
else:
  animale_scelto = animali[numero_animale]
  print(animale_scelto + "...ottima scelta!!")
input()
  















