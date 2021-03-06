
''' 
    Abbiamo n stringhe di caratteri.  
    All'interno delle stringhe  e' nascosta una parola segreta come sottostringa di 
    caratteri consecutivi. 
    Sappiamo con certezza che la parola si ripete uguale esattamente una volta in ciascuna 
    stringa ma non sappiamo dove. 
    Della parola conosciamo la lunghezza M e sappiamo che non ci sono altre sottostringhe 
    di lunghezza M che si ripetono una sola volta in tutte le stringhe. 
    Vogliamo sapere per ogni stringa  la posizione dove compare il primo carattere 
    della parola nascosta.
    Ad esempio per le 6 stringhe con parola nascosta di lunghezza 3:
    
    moneta
    maratoneta
    pitone
    onesto
    storione
    sonetto
    
    la parola nascosta è 'one' e le posizioni sono nell'ordine: 1, 5, 3, 0, 5, 1
    

    
    Progettare una funzione es1(ftesto) che prende in input  un file contenente la lunghezza 
    della parola nascosta e le n stringhe di caratteri e restituisce una lista di n interi.
    L'intero in  posizione i della lista e' la posizione dove compare il primo carattere 
    della parola nascosta nella stringa i. 
    
    Le informazioni nel file ftesto sono organizzate nel seguente modo:
    - la prima riga contiene la lunghezza della parola nascosta (un intero).
    - seguono poi le stringhe di caratteri, ciascuna stringa occupa una o piu' 
    righe consecutive del file ed e' separata dalla stringa seguente da una linea vuota.
    Ogni riga del file termina con un' andata a capo.
    Vedi ad esempio il file ft1.txt che codifica l'istanza vista prima.
    
    es('ft1.txt') deve restituire la lista [1,5,3,0,5,1]    
   

    NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test

    ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8 
    (ad esempio editatelo dentro Spyder)
   
'''

def es1(ftesto):
    risultato = []
    with open(ftesto) as f:
        testo = f.read()
    width, parole = decoder(testo)
    sottosequenza = trovaparola(width, parole)
    for x in parole:
        risultato.append(x.index(sottosequenza))
    return risultato
    pass


def decoder(testo):
    width = ''
    testo = testo.split('\n\n')
    testo = [ i.replace('\n', '') for i in testo ]
    for x in testo[0]:
        if x.isnumeric():
            width += x
            testo[0] = testo[0].replace(x, '')
        else:
            break
    return int(width), testo

def trovaparola(width, parole):
    prima_par = parole[0]
    start = 0
    end = width
    sottosequenze = []
    occ = {}
    while end != len(prima_par)+1:
        if not prima_par[start:end] in sottosequenze:
            sottosequenze.append(prima_par[start:end])
            occ[prima_par[start:end]] = 1
        else:
            sottosequenze.remove(prima_par[start:end])
            del occ[prima_par[start:end]]
        start += 1
        end += 1
    for i in parole[1:]:
        for j in sottosequenze:
            if j in i:
                a = i.find(j)
                if not j in i[a+1:]:
                    occ[j] += 1
            if occ[j] == len(parole):
                return j

if __name__ == '__main__':
    # inserisci qui i tuoi test
    pass
