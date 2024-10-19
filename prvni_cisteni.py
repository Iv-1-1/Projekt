import pandas as pd

seznam_projektu = pd.read_csv("Seznam_projektu_2022.csv") # Načtení souboru přehled zakázek pomocí pandas z excelu.
print(seznam_projektu)
seznam_projektu = seznam_projektu.rename(columns={"No.": "Cislo", 
                       "lokalita": "Lokalita", 
                       "Doplňky": "Doplnky", 
                       "Výkon (kW)": "Vykon", # kW
                       "budget": "Rozpocet",
                       "Celková zákaznická cena bez DPH (CZK)": "Celkova_cena_bez_DPH",
                       "Kontakt-zájem": "Prvni_poptavka",
                       "Odeslána nabídka": "Odeslana_nabidka",
                       " Odeslání žádosti": "Odeslani_zadosti",
                       "uzavření SoD": "Uzavreni_smlouvy_o_dilo",
                       "Vystavena záloha (60%)": "Datum_prvni_zalohy",
                       " 60% z ceny vč. DPH ": "Prvni_zaloha", # 60%
                       "Zaplacena záloha": "Datum_prvni_uhrady",
                       "Zahajení stavby": "Zahajeni_stavby",
                       "Ukončení stavby": "Ukonceni_stavby",
                       "Druhá fakturace (30%)": "Datum_druhe_zalohy",
                       " 30% z ceny vč. DPH ": "Druha_zaloha", # 30%
                       "Zaplacena 2. záloha": "Datum_druhe_uhrady",
                       "Revize provedena": "Datum_revize",
                       "Žádost o PPP": "Zadost_o_PPP", # Žádost o první paraelní připojení (zprovození FVE od distribuce)
                       "Předání díla": "Datum_predani", # Předání díla
                       "Konečná fakturace (10%)": "Datum_treti_zalohy",
                       " 10% z ceny vč. DPH ": "Treti_zaloha",
                       "Doplaceno": "Datum_treti_uhrady", # 10% (Uhrazeno celé dílo)
                       "Žádost o dotace": "Podani_zadosti_o_dotaci",
                       })
                       
seznam_projektu = seznam_projektu.drop(columns=["referent",
                                                "ID POHODA",
                                                "ID zakázky",
                                                "název projektu",
                                                "AKU",
                                                "Aktualní stav",
                                                "Telef. kontakt zájemce",
                                                "Osobní návštěva",
                                                "Potvrzení zájmu",
                                                "Technická obhlídka žádost",
                                                "Technická obhlídka doručena",
                                                "Vyjádření od distribuce",
                                                "Materiál",
                                                "Harmonogram výstavby",
                                                "Předání stavby ",
                                                "Revize požadavek",
                                                "Proj. dokumentace požadavek",
                                                "Proj. dokumentace provedena"
                                                ])

seznam_projektu["Vykon"] = seznam_projektu["Vykon"].str.replace(" kWp", "").str.replace("kWp", "").str.replace(",", ".").str.replace(" kWh", "").str.replace("kWh", "").str.replace(" kwp", "")

seznam_projektu["Zdroj"] = seznam_projektu["Zdroj"].fillna("")
# seznam_projektu[seznam_projektu["Zdroj"].str.contains("mail|web|tel")]


seznam_projektu.loc[seznam_projektu["Zdroj"].str.contains("mail|web|tel"),"Zdroj"] = "Externi"
seznam_projektu.loc[~seznam_projektu["Zdroj"].str.contains("Externi"),"Zdroj"] = "Interni"

seznam_projektu["Rozpocet"] = seznam_projektu["Rozpocet"].str.replace(" Kč", "").str.replace(",", "")

seznam_projektu["Celkova_cena_bez_DPH"] = seznam_projektu["Celkova_cena_bez_DPH"].str.replace(" Kč", "").str.replace(",", "")

seznam_projektu["Prvni_zaloha"] = seznam_projektu["Prvni_zaloha"].str.replace(" Kč", "").str.replace(",", "")

seznam_projektu["Druha_zaloha"] = seznam_projektu["Druha_zaloha"].str.replace(" Kč", "").str.replace(",", "")

seznam_projektu["Treti_zaloha"] = seznam_projektu["Treti_zaloha"].str.replace(" Kč", "").str.replace(",", "")

seznam_projektu["Prvni_poptavka"] = seznam_projektu["Prvni_poptavka"].str.replace(".","/")
seznam_projektu["Odeslana_nabidka"] = seznam_projektu["Odeslana_nabidka"].str.replace(".","/")
seznam_projektu["Odeslani_zadosti"] = seznam_projektu["Odeslani_zadosti"].str.replace(".","/")
seznam_projektu["Uzavreni_smlouvy_o_dilo"] = seznam_projektu["Uzavreni_smlouvy_o_dilo"].str.replace(".","/")
seznam_projektu["Datum_prvni_zalohy"] = seznam_projektu["Datum_prvni_zalohy"].str.replace(".","/")
seznam_projektu["Datum_prvni_uhrady"] = seznam_projektu["Datum_prvni_uhrady"].str.replace(".","/")
seznam_projektu["Zahajeni_stavby"] = seznam_projektu["Zahajeni_stavby"].str.replace(".","/")
seznam_projektu["Ukonceni_stavby"] = seznam_projektu["Ukonceni_stavby"].str.replace(".","/")
seznam_projektu["Datum_druhe_zalohy"] = seznam_projektu["Datum_druhe_zalohy"].str.replace(".","/")
seznam_projektu["Datum_druhe_uhrady"] = seznam_projektu["Datum_druhe_uhrady"].str.replace(".","/")
seznam_projektu["Datum_revize"] = seznam_projektu["Datum_revize"].str.replace(".","/")
seznam_projektu["Zadost_o_PPP"] = seznam_projektu["Zadost_o_PPP"].str.replace(".","/")
seznam_projektu["Datum_predani"] = seznam_projektu["Datum_predani"].str.replace(".","/")
seznam_projektu["Datum_treti_zalohy"] = seznam_projektu["Datum_treti_zalohy"].str.replace(".","/")
seznam_projektu["Datum_treti_uhrady"] = seznam_projektu["Datum_treti_uhrady"].str.replace(".","/")
seznam_projektu["Podani_zadosti_o_dotaci"] = seznam_projektu["Podani_zadosti_o_dotaci"].str.replace(".","/")

seznam_projektu["Status"] = seznam_projektu["Status"].replace(to_replace={"U": "Ukonceno", 
                       "N": "Nerealizovano", 
                       "R": "Ukonceno", 
                       "PPP": "Pripojeni",
                       "O": "Odlozeno",
                       "DOT": "Ukonceno",
                       "ZR": "Ukonceno",
                       "D": "Nepotvrzena_realizace", # Odešla žádost na distribuci, nevíme, zda dostali povolení FVE postavit
                       "SK": "Slovensko", # Dropnout pryč
                       "CN": "Odeslana_CN", # Odešla CN, ale nevíme, zda se FVE realizovala, či ne
                       "Z": "Storno_zakazky",
                       "SoD + D": "Ukonceno",
                       "K": "Odlozeno",
                       "0": "Error"}) # Dropnout pryč


seznam_projektu.to_csv ("Seznam_projektu.csv",
                  index = None,
                  header = True) # převedení do csv

