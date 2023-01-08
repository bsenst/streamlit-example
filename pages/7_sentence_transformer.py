import streamlit as st

st.header("Retrieve Documents using Vectors")
st.subheader("Method")
st.markdown("""
* model and instructions provided at https://huggingface.co/svalabs/bi-electra-ms-marco-german-uncased
* 631k documents, each having a vector of 768 floats (dimensions), 1,9 GB
* calculating the vectors for all documents took 10 workers and ~72hrs (kaggle)
* enter query, calculate vector for query
* retrieve documents which correspond to the query using cosine similarity
""")
st.subheader("Example Queries")
st.markdown("""
queries = [
    "kleider abgeben an kleidercontainern um kleider zu spenden",
    "kleiderkammer und rot-kreuzladen wo wohnungslose menschen kleidung kaufen können"
    "obdachlosenunterkunft oder wohnungslosenheime zur übernachtung",
    "tafel und lebensmittelausgabe für bedürftige menschen",
    "sozialstation an der bedürftige beratungen in anspruch nehmen können"
]

### Query: kleider abgeben an kleidercontainern um kleider zu spenden
Kleiderspende - Kreisverband Rotenburg (Wümme) e.V
Kleider-Behälter - DRK KV Esslingen e.V. Suche sta
Kleidercontainerfinder - DRK KV Esslingen e.V. Suc
Kleider-Behälter - DRK KV Osnabrück-Land e.V. Such
Kleidercontainer - DRK KV Esslingen e.V. Suche sta
Kleidercontainer - DRK KV Esslingen e.V. Suche sta
Kleidercontainer - DRK KV Esslingen e.V. Suche sta
Kleidercontainer - DRK KV Esslingen e.V. Suche sta
Kleidercontainerfinder - DRK Kreisverband Goslar e
Kleiderkammer - DRK Kreisverband Solingen e.V. Zur
Kleiderkammer - DRK Kreisverband Solingen e.V. Zur
Kleidercontainerfinder - DRK KV Fallingbostel Such
Kleidercontainer - DRK Kreisverband Goslar e.V. Su
Kleidercontainer - DRK KV Osnabrück-Land e.V. Such
Kleidercontainer - DRK KV Osnabrück-Land e.V. Such
Kleiderspende - DRK KV Schaumburg e. V. Suche star
Kleiderspende - DRK KV Schaumburg e. V. Suche star
Kleiderkammern - DRK KV Esslingen e.V. Suche start
Kleiderkammern - DRK KV Esslingen e.V. Suche start
DRK Altkleidersammlung am 17.09.2022 | DRK-Kreisve
Kleider-Behälter - DRK Kreisverband Goslar e.V. Su
Kleider-Behälter - DRK Kreisverband Goslar e.V. Su
Kleider-Behälter - DRK KV Fallingbostel Suche star
Kleiderkammern - DRK KV Esslingen e.V. Suche start
Kleiderkammern - DRK KV Esslingen e.V. Suche start
Kleidercontainerfinder - DRK KV Osterholz e.V. Suc
als Kleiderspender/in – Bayerisches Rotes Kreuz Ba
Kleider-Behälter - DRK KV Osnabrück-Nord Suche sta
Kleider spenden - DRK KV Peine e.V. Suche starten 
Kleider spenden - DRK KV Peine e.V. Suche starten 
Kleider-Behälter - DRK KV Schwäbisch Hall - Crails
Kleidercontainer - DRK KV Osterholz e.V. Suche sta
Kleidercontainer - DRK KV Osnabrück-Nord Suche sta
Kleiderkammern - DRK Kreisverband Goslar e.V. Such
Kleiderspende - einfach Helfen - DRK KV Osterholz 
Kleider-Behälter - DRK KV Osterholz e.V. Suche sta
Kleidercontainerfinder - DRK KV Bodenseekreis e.V.
Dachauer Tafel braucht dringend Lebensmittel – Bay
Kleiderkammer - DRK Kreisverband Solingen e.V. Zur
Kleidercontainerfinder - BRK KV Eichstätt Suche st
Kleidercontainerfinder - DRK KV Bodenseekreis e.V.
Kleiderkammer - DRK Kreisverband Wesermünde e.V. Z
Kleidercontainerfinder - BRK KV Eichstätt Suche st
Kleiderspende - DRK KV Heidenheim e.V. Suche start
Kleiderspende - DRK KV Heidenheim e.V. Suche start
Kleiderspende - einfach Helfen - DRK KV Osterholz 
Kleidercontainer - DRK KV Bodenseekreis e.V. Suche
Kleider-Kammern - DRK Kreisverband Goslar e.V. Suc
Fragen und Antworten zur Kleiderspende - DRK-KV We
Kleider-Behälter - DRK KV Bremervörde e.V. Suche s
Fragen und Antworten zur Kleiderspende - DRK-KV We
Kleider spenden - DRK KV Schwäbisch Hall - Crailsh
Kleider spenden - DRK KV Schwäbisch Hall - Crailsh
Kleiderläden - DRK KV Osnabrück-Land e.V. Suche st
600 Portionen Erbsensuppe für Aktion "Keiner soll 
Kleiderläden - DRK KV Osnabrück-Land e.V. Suche st
Kleidercontainer - DRK KV Bodenseekreis e.V. Suche
Kleidercontainer - BRK KV Eichstätt Suche starten 
Kleider-Behälter - DRK KV Osterholz e.V. Suche sta
Einladung bedürftiger Senioren der Dachauer Tafel 
Schätze für die RotKreuzShops – Landrat spendet au
Kleiderspenden - BRK KV Miesbach Suche starten + A
Kleiderspenden - BRK KV Miesbach Suche starten + A
Zieglerbräu spendet an Weihnachten an bedürftige F
Kleidercontainer - BRK KV Eichstätt Suche starten 
Kleidercontainer - DRK KV Heidenheim e.V. Suche st
Kleidercontainerfinder - DRK KV Soltau e.V. Suche 
Newsletter des BRK-Kreisverband Garmisch-Partenkir
Einladung bedürftiger Senioren der Dachauer Tafel 
Einladung bedürftiger Seniorinnen und Senioren der
Kleiderkammer – DRK-Kreisverband Duderstadt e. V. 
Masken Nähen – Bayerisches Rotes Kreuz Bayerisches
Kleiderladen - DRK KV Osterode Suche starten + Ang
Kleiderladen - DRK KV Osterode Suche starten + Ang
Kleiderkammern - DRK KV Peine e.V. Suche starten +
Kleiderkammern - DRK KV Peine e.V. Suche starten +
Flohmarkt – Bayerisches Rotes Kreuz Bayerisches Ro
Dachau ist auf dem Weg Fairtrade Town zu werden un
Altkleider - DRK KV Schwäbisch Hall - Crailsheim e
Kleiderläden - DRK Kreisverband Goslar e.V. Suche 
Kleiderläden - DRK KV Schwäbisch Hall - Crailsheim
Kleiderläden - DRK KV Schwäbisch Hall - Crailsheim
Kleiderkammern - DRK KV Peine e.V. Suche starten +
Kleiderkammern - DRK KV Peine e.V. Suche starten +
Kleidersammlung - DRK Kreisverband Viersen e.V. Zu
Kleider-Shops - DRK KV Peine e.V. Suche starten + 
Kleider-Shops - DRK KV Peine e.V. Suche starten + 
Kleiderkammer - DRK Kreisverband Solingen e.V. Kre
Einladung 40 bedürftiger Seniorinnen und Senioren 
Neuer BRK-Kleiderladen in Markt Indersdorf eröffne
Tafel richtet Notbetrieb ein. Freiwillige Helfer*i
Der neue Kühltransporter für die Dachauer Tafel is
Private Spende von 500 Euro an die Dachauer Tafel 
Döneria-Aktionstag – 2.000 Euro für die Dachauer T
Kleider-Behälter - DRK KV Heidenheim e.V. Suche st
Meldung - DRK KV Osterode Suche starten + Angebote
Kleiderkammern - DRK KV Osterode Suche starten + A
Kleider-Spende - DRK KV Göppingen e.V. Suche start
Meldung - DRK KV Osterode Suche starten + Angebote
Was wir brauchen – Bayerisches Rotes Kreuz Bayeris
...
### Query: sozialstation an der bedürftige beratungen in anspruch nehmen können
Betreuungsgruppe - DRK Kreisverband Viersen e.V. Z
Sozialtraining - DRK Kreisverband Wesermünde e.V. 
Entlastende Dienste | DRK-Kreisverband 05921 8836-
Tagesstruktur - DRK KV Schaumburg e. V. Suche star
Tagesstruktur - DRK KV Schaumburg e. V. Suche star
Tafel versorgt im Notbetrieb 150 hilfsbedürftige P
Schulbegleitung | DRK-Kreisverband 05921 8836-0 in
Zusatzangebot - Fachberatung Kindergartenbetreuung
Zusatzangebot - Fachberatung Kindergartenbetreuung
Jugendhilfestation - DRK Kreisverband Wesermünde e
Tagespflege | DRK-Kreisverband 05921 8836-0 info@d
Betreuungsverein - Sozialpädagogen / Sozialarbeite
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Angebote | DRK-Kreisverband 05921 8836-0 info@drk-
Beratung - DRK Kreisverband Wesermünde e.V. Zur Na
Begegnungsstätten - DRK KV Bremervörde e.V. Suche 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Besuchsdienst - BRK Bereitschaft Freising Suche st
Besuchs- und Unterstützungsdienste - DRK KV Schwäb
Besuchs- und Unterstützungsdienste - DRK KV Schwäb
Tafeln - DRK KV Schaumburg e. V. Suche starten + A
Tafeln - DRK KV Schaumburg e. V. Suche starten + A
Betreuungsgruppe - DRK Kreisverband Solingen e.V. 
Anregungen/Beschwerden - DRK Kreisverband Wesermün
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
FSJ (m/w/d) im Krankentransport | DRK-Kreisverband
Personal - DRK Kreisverband Wesermünde e.V. Zur Na
Bereitschafts-Dienste - DRK Kreisverband Goslar e.
Bereitschaften - DRK Kreisverband Viersen e.V. Zur
Besuchs-Dienst - BRK Bereitschaft Freising Suche s
Bereitschaften - DRK Kreisverband Solingen e.V. Kr
Hygiene für die „Sau“ - JRK KV Calw e.V. Link 0308
Service Wohnen | DRK-Kreisverband 05921 8836-0 inf
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Betreutes Wohnen - DRK Kreisverband Wesermünde e.V
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Jugendtreff Vehrte - DRK KV Osnabrück-Land e.V. Su
Betreuungsdienst - DRK KV Osnabrück-Land e.V. Such
Tages-Stätten und Begegnungs-Stätten - DRK Kreisve
Tagesbetreuung Stadthagen - DRK KV Schaumburg e. V
Tagesbetreuung Stadthagen - DRK KV Schaumburg e. V
Betreuungsdienst - DRK KV Osnabrück-Land e.V. Such
Psychosoziale Kontakte - DRK Kreisverband Goslar e
Ehrenamtliche Mitarbeit - DRK Kreisverband Wesermü
Betreuungsgruppe - DRK Kreisverband Solingen e.V. 
Jugendtreff Vehrte - DRK KV Osnabrück-Land e.V. Su
Meldung - DRK Kreisverband Goslar e.V. Suche start
Wir über uns - DRK Wohnheim Leher Landtraße Zur Na
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Engagement | DRK-Kreisverband 05921 8836-0 info@dr
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Betreuungsgruppe - DRK Kreisverband Solingen e.V. 
Betreuungsgruppe - DRK Kreisverband Solingen e.V. 
Tagespflege - DRK Kreisverband Wesermünde e.V. Zur
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Angebote Home Wer wir sind Grundsätze DRK Kreisver
Angebote Home Wer wir sind Grundsätze DRK Kreisver
Tagespflege Home Wer wir sind Grundsätze DRK Kreis
Tagespflege Home Wer wir sind Grundsätze DRK Kreis
Mitwirken - DRK Kreisverband Wesermünde e.V. Zur N
Aktivierender Hausbesuch - DRK KV Freudenstadt e.V
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Bereitschaft - DRK KV Peine e.V. Suche starten + A
Bereitschaft - DRK KV Peine e.V. Suche starten + A
freiwilligenAgentur region uelzen Startseite Info 
Tages- und Begegnungsstätten - DRK Kreisverband Go
Besuchsdienst - BRK KV Miesbach Suche starten + An
Besuchsdienst - BRK KV Miesbach Suche starten + An
Unser Profil - DRK Kreisverband Wesermünde e.V. Zu
Online Bewerbung - DRK KV Schaumburg e. V. Suche s
Online Bewerbung - DRK KV Schaumburg e. V. Suche s
Bereitschafts-Dienste - DRK KV Bremervörde e.V. Su
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Ambulanter Besuchsdienst - DRK-KV Weserbergland e.
Ambulanter Besuchsdienst - DRK-KV Weserbergland e.
Begegnen - DRK Kreisverband Wesermünde e.V. Zur Na
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Bereitschaft - DRK KV Peine e.V. Suche starten + A
Bereitschaft - DRK KV Peine e.V. Suche starten + A
Online Bewerbung - DRK KV Schaumburg e. V. Suche s
Online Bewerbung - DRK KV Schaumburg e. V. Suche s
Tages-Stätten und Begegnungs-Stätten - DRK KV Brem
Babybegrüßung - DRK Kreisverband Wesermünde e.V. Z
Bereitschafts-Dienste - DRK KV Fallingbostel Suche
Bereitschaften - DRK KV Schwäbisch Hall - Crailshe
...
### Query: tafel und lebensmittelausgabe für bedürftige menschen
Tafel versorgt im Notbetrieb 150 hilfsbedürftige P
Dachauer Tafel bleibt im Notbetrieb. Engagierte He
Dachauer Tafel braucht dringend Lebensmittel – Bay
Tafel richtet Notbetrieb ein. Freiwillige Helfer*i
Menü Service - Kreisverband Rotenburg (Wümme) e.V.
Kleiderkammer - DRK Kreisverband Wesermünde e.V. Z
BRK Tafel: Pizza für die Ehrenamtlichen, die in de
Was wir brauchen – Bayerisches Rotes Kreuz Bayeris
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Tafeln - DRK KV Schaumburg e. V. Suche starten + A
Tafeln - DRK KV Schaumburg e. V. Suche starten + A
Hygiene für die „Sau“ - JRK KV Calw e.V. Link 0308
Aufzunehmender Personenkreis - DRK Kreisverband We
Weihnachtsessen für bedürftige Bürgerinnen und Bür
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Spenden Basar für Kindergärten im Ahrtal  - DRK Kr
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Dachauer Tafel jetzt im 14tägigen Rhythmus. Corona
Einladung bedürftiger Senioren der Dachauer Tafel 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Einladung bedürftiger Seniorinnen und Senioren der
Tagespflege | DRK-Kreisverband 05921 8836-0 info@d
Kleiderkammer Home Wer wir sind Grundsätze DRK Kre
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Tafel Hausham freut sich über Spende - BRK KV Mies
Tafel Hausham freut sich über Spende - BRK KV Mies
BRK-Neujahrsempfang für die Mitarbeiterinnen und M
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Die Wohnstätten - DRK Kreisverband Wesermünde e.V.
Tagespflege Home Wer wir sind Grundsätze DRK Kreis
Tagespflege Home Wer wir sind Grundsätze DRK Kreis
Kindertagesstätte Krümelkiste - DRK Kreisverband S
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Ehrenamtliche Arbeit – in der Adventszeit in der D
Service Wohnen | DRK-Kreisverband 05921 8836-0 inf
Einladung 40 bedürftiger Seniorinnen und Senioren 
Meldung - DRK-KV Weserbergland e.V. Suche starten 
Essens-Liefer-Dienst - DRK KV Bremervörde e.V. Suc
DRK Presseinformationen https://www.drk-uelzen.de 
Kleiderspende - Kreisverband Rotenburg (Wümme) e.V
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Weihnachtlicher Dank für unsere Tafel-Helfer - BRK
Weihnachtlicher Dank für unsere Tafel-Helfer - BRK
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
BRK Dachau Fachtagung zur Kinderarmut. Jedes fünft
Essen und Rituale - DRK Kreisverband Wesermünde e.
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Flohmarkt – Bayerisches Rotes Kreuz Bayerisches Ro
Betretungsverbot  für die Kindertagestätten und Ki
freiwilligenAgentur region uelzen Startseite Info 
Weihnachtlicher Dank für unsere Tafel-Helfer - BRK
Weihnachtlicher Dank für unsere Tafel-Helfer - BRK
Unser Profil - DRK Kreisverband Wesermünde e.V. Zu
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Tafel Hausham freut sich über Spende - BRK KV Mies
Tafel Hausham freut sich über Spende - BRK KV Mies
Kindertagesstätten - DRK Kreisverband Solingen e.V
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Babybegrüßung - DRK Kreisverband Wesermünde e.V. Z
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Kiddys@Home - DRK Kreisverband Viersen e.V. Zur Na
Soziale Dienste - DRK Kreisverband Wesermünde e.V.
Spende für die Tafel - BRK KV Miesbach Suche start
Spende für die Tafel - BRK KV Miesbach Suche start
Betreuungsgruppe - DRK Kreisverband Viersen e.V. Z
Menü Service - DRK KV Osterholz e.V. Suche starten
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Einladung bedürftiger Senioren der Dachauer Tafel 
Tagespflege - DRK Kreisverband Wesermünde e.V. Zur
Kindertagesstätten - DRK Kreisverband Solingen e.V
Kindertagesstätten - DRK Kreisverband Solingen e.V
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
Meldung - DRK KV Schaumburg e. V. Suche starten + 
...
""")
