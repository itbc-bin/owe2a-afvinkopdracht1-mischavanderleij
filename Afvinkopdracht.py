def main():
    controle_bestand = False
    while controle_bestand == False:
        bestand = input("Geef een bestandsnaam: ")
        try:
            lees_inhoud(bestand)
            controle_bestand = True
        except FileNotFoundError:
            print("Bestand niet gevonden, voer de bestandsnaam opnieuw in ")
        except:
            print("Er is iets fout gegaan")

    
    headers, seqs = lees_inhoud(bestand)
    zoekwoord = input("Geef een zoekwoord op: ")
    for i in range(len(headers)):
            if zoekwoord in headers[i]:
                print("Header:",headers[i])
            check_is_dna = is_dna(seqs[i])
            if check_is_dna:
                print("Sequentie is DNA")
                knipt(seqs[i])
            else:
                print("Sequentie is geen DNA. Er is iets fout gegaan.")

    
def lees_inhoud(bestand_naam):
    try:
        bestand = open(bestand_naam)
        headers = []
        seqs = []
        seq = ""
        for line in bestand:
             line=line.strip()
             if ">" in line:
                 if seq != "":
                     seqs.append(seq)
                     seq = ""
                 headers.append(line)
             else:
                 seq += line.strip()
        seqs.append(seq)
        return headers, seqs
    except:
        print("Onbekende fout")
    
def is_dna(seq):
    try:
        dna = False
        a = seq.count("A")
        t = seq.count("T")
        c = seq.count("C")
        g = seq.count("G")
        total = a + t + c + g
        if total == len(seq):
            dna = True
        if dna == False:
            raise SyntaxError
    except SyntaxError:
        print("Er is een fout opgetreden")
    return dna


def knipt(alpaca_seq):
    try:
        bestand = open("enzymen.txt")
    except FileNotFoundError:
        print("Bestand is niet gevonden")
        
    for line in bestand:
        naam, seq = line.split(" ")
        seq = seq.strip().replace("^","")
        if seq in alpaca_seq:
            print(naam, "knipt in sequentie")
    
    

try:
    main()
except KeyboardInterrupt:
    print("Onbekende fout, raadpleeg uw systeembeheerder")

