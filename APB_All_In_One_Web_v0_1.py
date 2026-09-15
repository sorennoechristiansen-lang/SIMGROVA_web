# APB All-In-One Web v0.30
# v0.30: Logout now recreates the login fields with fresh Streamlit widget keys so browser password-manager/autofill suggestions can reappear without closing and reopening the tab.
# v0.29: Built portfolio now expands vertically to show every position at once instead of capping the table height and requiring vertical scrolling.
# v0.28: Fixes European money parsing for values with multiple thousands separators such as 1.000.000, so capital is no longer interpreted as zero.
# v0.27: When capital and minimum-position constraints leave no optimisation room, offers Build portfolio anyway, reduces the requested stock count by 20% to a whole number, updates the visible field and continues the build.
# v0.26: Adds a permanent neutral Skool community link below the login form, suitable for both existing members and public test users.
# APB All-In-One Web v0.25
# v0.25: Adds first-use validation for Currency/capital/minimum position/stock count, synchronized sliders for the three numeric basic rules, and a web Dividend preference with Off/On heading, High priority and 3% target. Result view/PDF show weighted portfolio dividend yield.
# v0.9d: Adds synchronized drag sliders to all required 100% allocations (Structure, Sectors, Regions). Slider changes use the same automatic proportional/equal rebalance logic as direct numeric edits.
# v0.9c: When automatic balancing is switched on for a required 100% allocation, the current values are immediately normalized proportionally to exactly 100.0%.
# v0.9k: Fixes Industry Custom setup completely: adds it to the dropdown, uses the Industry preset callback, prevents Custom from changing values, keeps heading/dropdown synchronized, and preserves High priority behavior for real presets.
# v0.9j: Adds Industry Custom setup behavior consistent with Structure/Sector/Region: the dropdown reflects manual special values, matching presets are detected automatically, and selecting Custom setup preserves current values.
# v0.9i: Adds synchronized sliders to Industry preferences while preserving the existing -100 to +100 soft-preference scale and preset logic.
# v0.9h: Keeps the allocation section heading synchronized with the visible preset dropdown in every situation. Preset changes are applied in the dropdown callback before the expander heading is rendered, while Custom setup remains non-destructive.
# v0.9g: Adds Custom setup as a real option in Structure/Sector/Region preset dropdowns. Manual allocation edits automatically switch the dropdown to Custom setup (or back to a matching preset); selecting Custom setup itself preserves the current values unchanged.
# v0.9f: Allocation expanders stay open when an edit first changes the heading from a preset to Custom setup; user collapse behavior remains unchanged afterwards.
# v0.9b: Adds build-time validation for all required 100% allocations. The build engine will not start unless Structure layers, Sector targets and Region targets each total exactly 100.0%; the user is told which distributions need correction.
# v0.9: Adds optional automatic 100% balancing for Structure layers, Sector targets and Region targets. The edited value is preserved; remaining values can be redistributed proportionally or equally. Manual mode shows the exact percentage still to distribute/remove. Auto-calculated values use max. one decimal.
# Generated from the supplied APB input, desktop builder v0.43 and result portal.

# Porteføljebygger version 0.43
# Baseret på Porteføljesimulator v7.49
# VERSION 6.48 – Porteføljesimulator
# Formål:
# - Simpel porteføljesimulator baseret på JSON-portefølje og TradingView-kursdata.
# - Default-portefølje gemmes i portefolje_default.json i samme mappe som programmet.
# - En anden JSON-portefølje kan importeres via knap. Indholdet kopieres til default-filen,
#   uden at den valgte kildefil ændres.
# - Porteføljens udvikling beregnes vægtet ud fra antal aktier og seneste kurs.
# - Version 1.2: Nr-kolonne efter porteføljevægt og redigering i separat vindue.
# - Version 1.3: Retter talformat, så antal fra JSON ikke ganges med 100 ved genindlæsning.
# - Version 1.4: Tilføjer %4M, %5M, %4Y og %5Y i periodekolonnerne.
# - Version 1.5: Valutakurser hentes fra TradingView, og porteføljevægt beregnes i DKK.
# - Version 1.6: Tilføjer faner med Fase 1 og Fase 2 fundamentale porteføljedata.
# - Version 1.7: Dags-cache: hvis data allerede findes for dagen, hentes kun manglende data.
# - Version 1.8: Retter topbar-layout, så knapper ikke skubbes ud af statuslinjen.
# - Version 1.9: Tilføjer %1D, %5D og %14D før %1M i Fase 1.
# - Version 2.0: Tilføjer Fase 3 med sektor-, industri- og PE-fordeling af porteføljen.
# - Version 2.1: Gør kolonnerne i Rediger portefølje-vinduet sorterbare.
# - Version 2.2: Rediger portefølje-vinduet åbner maksimeret, så knapperne ses med det samme.
# - Version 2.3: Retter layout i redigeringsvinduet, så knaplinjen altid er synlig nederst.
# - Version 2.4: Tilføjer Analytiker analyse og vægtet FC1Y% i fase 3-grupperinger.
# - Version 2.5: Tilføjer Land / Region i fase 2 og region-/landeanalyse i fase 3.
# - Version 2.6: Tilføjer FC1Y median i Analytiker analyse.
# - Version 2.7: Tilføjer risikoanalyse med gennemsnit af 3 seneste drawdowns, aktiescore og anbefalet %PF.
# - Version 2.8: Erstatter Risiko DD med Trendstyrke og Robusthed baseret på 3M/1Y/3Y kursdata.
# - Version 2.9: Tilføjer Bull/Base/Median/Bear analytikerdata, spænd, datakontrol og rød advarselsmarkering.
# - Version 3.0: Tilføjer kvalitetsscore fra fundamentaler og ulineær anbefalet porteføljevægt.
# - Version 3.1: Kvalitet gøres ulineær, og aktiescore bygges hierarkisk: Potentiale × Kvalitet med mindre trend-/robusthedskorrektion.
# - Version 3.2: Potentialescore gøres ulineær med S-kurve, så meget høje forecasts mættes i stedet for at dominere.
# - Version 3.3: Tilføjer Aktier+/- efter Anbefalet %PF baseret på hele aktier og valutakorrigerede kurser.
# - Version 3.4: Retter OTC-markedets valuta fra standard DKK til USD.
# - Version 3.5: Tilføjer knappen Beregningsforklaring med dybtgående modelbeskrivelse.
# - Version 4.0: Tilføjer Fase 4 – gevinstsikring med GAK, Nordnet-CSV, analytikerhistorik og handlingsanbefaling.
# - Version 4.1: Robust direkte Nordnet-import (UTF-16/TAB), sikker kobling til børs+ticker og lagring af alle Nordnet-felter.
# - Version 4.4: Fjerner Anbefaling og tilføjer Procent af mål fra start med grafisk bar.
# - Version 4.5: Omdøber kolonnen til Procent af startmål og højrestiller en fastbredde-bar.
# - Version 4.6: Tilføjer Base- og Bull-startmål med separate grafiske målbjælker og fjerner Change 1Y%.
# - Version 4.8: Tilføjer grafiske søjler for procent af aktuelle Base- og Bullmål.
# - Version 4.9: Retter aktuelle Base/Bull-mål, så dagens 1Y%-potentiale omregnes til samlet mål fra GAK.
# - Version 5.0: Tilføjer forceret dataopdatering uden dags-cache. Fase 4 beregner selv Ureal.% og Ureal. DKK fra GAK, aktuel kurs, antal og valutakurs.
# - Version 5.1: Finjusterer Aktiescore med mild analytikerenighed samt S-kurver for PEG og EBIT-margin. PE, vægte, Trendstyrke og Robusthed er uændrede.
# - Version 5.2: Ugyldige TradingView-scenarier bruger Base alene uden straf. Enighedsfaktoren mildnes til 0,95-1,05.
# - Version 5.3: Retter TradingView High/Median/Low-kursmål for ikke-amerikanske aktier ved robust USD-til-lokal valutanormalisering.
# - Version 5.4: Håndterer selskaber med ét fælles analytikerkursmål, hvor Max/Median/Min skal være lig Base.
# - Version 5.5: Oprydder analytikerlogikken, fjerner overflødig kode og samler validering/normalisering uden at ændre beregningsresultatet.
# - Version 5.6: Fase 4 bruger første gyldige positive Base- og Bull-historik som låste startmål og springer gamle fejlbehæftede værdier over.
# - Version 5.7: Tilføjer Tillidsscore fra analytikerspændet og lader den indgå med 10% i Aktiescore.
# - Version 5.8: Tillid multipliceres ind som sandsynlighedsfaktor i Potentiale × Kvalitet i stedet for at være et separat 10%-tillæg.
# - Version 5.9: Kvalitet udvides med ROIC, FCF-margin og FCF-vækst og vægtes mere balanceret mellem vækst og dokumenteret kapitalforrentning.
# - Version 6.0: Kvalitet gøres til fundamentet i Aktiescore. Analytikerpotentiale × Tillid bliver en mindre 15%-modifikator.
# - Version 6.1: Anbefalet %PF bruger adaptiv eksponent efter spredningen i Aktiescore.
# - Version 6.2: Anbefalet %PF bruger logistisk S-kurve omkring porteføljens median-Aktiescore.
# - Version 6.3: Udvider Programforklaring og Beregningsforklaring med arkitektur, datakilder, cache, alle faser, formler, argumentation, eksempler, styrker og begrænsninger.
# - Version 6.4: Tilføjer Fase 2B – Indre værdi med materiel egenkapital, Bogført kurs og markedspræmie.
# - Version 6.5: Omdøber Fase 2B til Bogført værdi, bruger egenkapital som bogført værdi og forenkler tabellen.
# - Version 6.6: Omdøber visningen til Fase 1B, tilføjer Værdiscore, redigerbar præmie-tabel og dynamisk værdipåvirkning af Anbefalet %PF.
# - Version 6.7: Ændrer standardtabellen for Værdiscore, så dæmpningen starter blødt allerede ved 1× præmie.
# - Version 6.8: Tilføjer Strukturscore, fire porteføljelag og fanen Porteføljestruktur i Fase 3.
# - Version 6.9: Tilføjer altid Kontanter til rådighed i DKK i Fase 2 og medregner kontanter i Aktier+/−-målet.
# - Version 6.10: Kontanter tælles ikke som en position i statuslinjen, og Porteføljestruktur viser lagandele normaliseret til aktiedelen uden kontanter.
# - Version 6.11: Alle fordelinger i Fase 3 normaliseres til aktiedelen uden kontanter, inkl. sektor, industri, PE, region og analytikerdækning.
# - Version 6.12: Tilføjer %1D i Fase 2 mellem Valuta og Værdi DKK med samme data, format og sortering som i Fase 1.
# - Version 6.13: Tilføjer Importer Saxo CSV/XLSX i Fase 4 med oversættelse af Saxo-felter til programmets GAK, antal og positionshistorik.
# - Version 6.14: Retter Saxo-decimaltal med tre decimaler, så fx 167.394 læses som 167,394 og ikke 167.394.
# - Version 6.15: Tilføjer en fast sum-/gennemsnitslinje nederst i Fase 4, uafhængigt af sortering.
# - Version 6.16: Tilføjer faste region- og sektorgrupper, redigerbare målfordelinger, Region-/Sektorscore og påvirkningsskydere til Anbefalet %PF.
# - Version 6.17: Tilføjer Industriscore med automatisk koncentrationsmål pr. TradingView-industri, individuelle mål og påvirkningsskyder.
# - Version 6.18: Tilføjer knappen Bedste forslag til perfekt aktie i porteføljen, som beregner den mest manglende profil på region, sektor, industri og strukturlag.
# - Version 6.19: Tilføjer hårdt minimum-upside-filter i Fase 2: Bull skal være mindst +20 %, og ved negativ Bear skal Bull være mindst 2× den numeriske Bear-risiko. Afviste aktier markeres røde og får "Sælg" i Anbefalet %PF.
# - Version 6.20: Markerer attraktive analytikerscenarier grønt i Fase 2, når Bear er over -10 % og Bull er over +30 %. Markeringen ændrer ingen beregninger eller tekst i Anbefalet %PF.
# - Version 6.21: Skjuler kolonnerne Median % og Spænd % i Fase 2, så Bull %, Base % og Bear % kan ses samlet uden vandret scrolling. Beregningerne bevares uændret.
# - Version 6.22: Vender den visuelle analytikermarkering om i Fase 2: aktier, der ikke opfylder Bear > -10 % og Bull > +30 %, markeres svagt gul/orange; øvrige rækker beholder normal zebravisning.
# - Version 6.24: Gør forklaringsvinduet til rækkefarver højere, så hele indholdet og Luk-knappen kan ses uden manuel ændring af vinduets størrelse.
# - Version 6.26: Tilføjer KM alder og Til regnskab i Fase 2. KM alder måler dage siden senest observerede ændring i TradingViews absolutte Bull/Base/Median/Bear-kursmål, og Til regnskab viser dage til næste earnings-dato.
# - Version 6.27: Skelner mellem kendt og ukendt kursmålsalder. Kendte ændringer vises som fx 3, mens ukendt startdato først vises som +5, +6 osv. Til regnskab-kolonnen er gjort en anelse bredere.
# - Version 6.28: Ukendt KM-alder vises fra første observation som +0, +1 osv.; Til regnskab-kolonnen er udvidet yderligere, og summeringsrækken hedder Samlet udvikling.
# - Version 6.29: Navn-kolonnen i Fase 2 gøres fast og ca. fem tegn smallere, så Til regnskab kan ses.
# - Version 6.33: Retter KM alder, så flere hentninger på første observationsdag altid forbliver +0; først ændringer på en senere dato bliver kendt alder 0.
# - Version 6.34: Samler KM-alder og kursmålshistorik i én JSON. Gemmer kun absolutte Bull/Base/Median/Bear-kursmål ved reelle ændringer samt kursen på observationsdagen. Procenter rekonstrueres efter behov, og Fase 4 bruger den absolutte historik.
# - Version 6.35: Forenkler Fase 4 ved at fjerne Procent af start Base-/Bullmål og reducerer kursmålshistorikken til Bull/Base/Bear med tilhørende rekonstruerede procentmål.
# - Version 6.36: Ufuldstændige kursmålsposter skjules og kan ikke starte historikken. Første komplette registrering oprettes på dagens dato, og KM alder forbliver +0, indtil en senere komplet kursmålsændring observeres.
# - Version 6.37: Kursmålshistorikkens rullemenu viser kun aktienavne alfabetisk. Fase 2 får en Kursmålshistorik-knap, som åbner historikken direkte for den markerede aktie.
# - Version 6.38: Kursmålshistorikken forvælger markeret aktie fra både Fase 2 og Fase 4. Uden markering vises første aktie alfabetisk straks i rullemenuen.
# - Version 6.39: Kursmålshistorikkens rullemenu viser altid navnet på den forvalgte aktie. Fase 4 viser Bull 1Y%, Base 1Y% og Bear 1Y% og fjerner de to startkolonner.
# - Version 6.40: Opretter et permanent aktiekartotek. Solgte aktier bevares, analytikerhistorikken opdateres fortsat én gang dagligt i batch, og tidligere aktier kan genvælges direkte i Rediger portefølje.
# - Version 6.41: Retter ikke-amerikanske kursmål, når TradingViews Max/Median/Min er USD-normaliserede, men indbyrdes ulogiske. Enheden vælges nu uafhængigt af rækkefølgen, så værdierne vises som i TradingView.
# - Version 6.42: Renser automatisk kursmålshistorikken for blandede valutaenheder og efterfølgende afledte omregningsposter, så forurenede JSON-punkter fjernes og næste gyldige hentning etablerer en ren reference.
# - Version 6.43: Datavarsling accepterer små afvigelser i TradingViews Bull/Base/Median/Bear-rækkefølge. Lys rød bruges kun ved tydelige scenariebrud; JSON-rensningen fra v6.42 bevares uændret.
# - Version 6.44: Fjerner ugyldige og ufuldstændige kursmålsposter fra JSON-historikken. KM alder og metadata genopbygges kun fra komplette poster, så én gyldig første observation vises som +0.
# - Version 6.45: Tilføjer Tidligere aktier i Fase 2 med oversigt, grøn genkøbsmarkering, fuld JSON-sletning og genkøb direkte til den aktive portefølje.
# - Version 6.46: Omdøber Tidligere aktier til Watch list og indfører fem prioriterede farveniveauer ud fra Base 1Y forecast samt Bull/Bear-forholdet.
# - Version 6.47: Filtrerer kursmålshistorikken for TradingView-støj. En ny post gemmes kun, når Bull, Base eller Bear ændres mindst 2 %, og eksisterende støjposter fjernes automatisk fra JSON-historikken.
# - Version 6.48: Registrerer næste regnskabsdato som en fremtidig begivenhed i kursmålshistorikken. Kursmålsændringer og regnskaber vises samlet i kronologisk rækkefølge, uden at regnskabsdatoer påvirker KM-alder eller kursmålsstøjfilter.
# - Version 6.49: Vinduet navngives efter programmets mappe. Fase 2 viser dagligt VIX samt anbefalet kontantandel i procent og DKK, med redigerbar VIX-tabel. Forceret opdatering henter altid VIX på ny.
# - Version 6.50: Fase 2 viser også aktuel kontantbeholdning i procent og DKK. Watch list får Kursmålshistorik for den markerede aktie.
# - Version 6.51: Watch list-opdateringen henter og registrerer også næste regnskabsdato i kursmålshistorikken.
# - Version 6.52: Kursmålshistorikken viser næste regnskabsdato særskilt; først når datoen er passeret, flyttes den til regnskabshistorikken.
# - Version 6.56: Begivenhed-kolonnen i kursmålshistorikken udvides fra 125 til 155 pixels.
# - Version 6.57: Fase 2 viser aktuel kontantprocent og DKK, VIX samt anbefalet procent og DKK som fem farvede kort på én linje; indstillingsknappen bevares.
# - Version 6.58: Strukturscoren bruger redigerbare TradingView Market Cap-grænser, husker markedsprofilen, fjerner børshistorik og anvender en redigerbar spekulationsstraf fra ekstreme Bull-procenter.
# - Version 6.62: Opdaterer standardtabellen for spekulationsstraf til Bull-grænserne 100/200/250/300/350/400/450/500 med straf 1-8. Strukturmotor og laggrænser er uændrede.
# - Version 6.65: Retter ETF-holdingsudtræk med rekursiv JSON-læsning, fleksibel feltorden og tekstfallback fra TradingViews Fund composition-tabel.
# - Version 6.66: Renser ETF-holdings for hjælpefelter og dubletter, viser Min vægt, kort Match-tekst og samlet ETF-temaoversigt.
# - Version 6.67: Gør Fase 5 beslutningsorienteret med kompakt ETF-temaoversigt, trend, acceleration, datadækning og Temaanalyse-signaler. Fjerner Model/Kapital fra ETF-listen.
# - Version 6.68: Gør alle tabeller i Fase 5 sorterbare via klik på kolonneoverskrifter med korrekt tal-, procent-, DKK- og datosortering.
# - Version 6.69: Aktive aktier og Watch list bruger samme daglige kursmålskæde. Seneste kurs/Bull/Base/Bear gemmes som aktuel observation, KM-alder vedligeholdes ens, og Watch list viser altid seneste normale eller forcerede opdatering uden at gøre dagskurser til historikstøj.
# - Version 6.70: Afstemmer efter hver vellykket hentning den aktuelle observation mod seneste kursmålshistorik. Ved mindst 2 % ændring i Bull/Base/Bear oprettes eller erstattes dagens historikpost, så Watch list og kursmålshistorik ikke kan være uenige.
# - Version 6.71: ETF-positioner viser Bull/Base/Bear 1Y-procenter fra TradingView før ETF-vægten. Fase 5 opdaterer automatisk den normale ETF Benchmark, når hovedfanen vælges.
# - Version 6.72: ETF-positioner viser også Sektor, Industri og Land / Region fra TradingView før Bull/Base/Bear. Klassifikationen hentes i samme batch og efterhentes automatisk i eksisterende dags-cache.
# - Version 6.73: ETF-positioner får en fast totalrække med gennemsnit for Bull/Base/Bear samt summering af ETF-vægt og Min vægt. Manglende analytikerværdier udelades fra gennemsnittene.
# - Version 6.74: Tilføjer fanen Oversigt over ETF positioner med alle fundne positioner samlet og ETF-navn som sidste kolonne.
# - Version 6.75: Oversigt over ETF positioner bruger Watch listens beslutningsfarver. Totalrækken viser kun gennemsnit for Bull/Base/Bear og summerer ikke ETF-vægt eller Min vægt.
# - Version 6.76: Programmet starter i Fase 2. Gul/orange-markeringen i Fase 2 erstattes af Watch listens Base-baserede beslutningsfarver, mens mørkerød Sælg og lys rød datavarsling bevares uændret.
# - Version 6.77: Fase 3 viser Anbefalet %PF efter den aktuelle porteføljeandel for sektorer, industrier og regioner ud fra indstillingerne i Fase 2.
# - Version 6.78: Fase 3 summerer Anbefalet %PF og viser alle sektor- og regionkategorier, også når den aktuelle andel er 0 %, så målfordelingerne altid summerer til 100 %.
# - Version 6.79: Gør ETF-listen i Rediger ETF-liste-vinduet sorterbar ved klik på Børs, Ticker og Navn.
# - Version 6.80: Tilføjer en fast indtastningslinje med Børs, Ticker og Navn i Rediger ETF-liste-vinduet, så ETF'er kan tilføjes direkte uden dialogbokse. Felterne bevarer deres indhold, indtil brugeren ændrer dem.
# - Version 6.81: Fase 5 sletter ETF'er permanent fra liste, holdings, manuelle tilpasninger og cache med det samme. Oprettelse med samme børs+ticker overskriver eventuelle gamle rester i stedet for at afvise ETF'en som dublet.
# - Version 6.82: Fase 2 får et dybgrønt Køb-signal tæt på Bear-målet samt skyderen Kursmålets påvirkning.
# - Version 6.83: Kursmålets påvirkning gælder kun aktive købsvinduer og kan løfte den normale Anbefalet %PF op til 5× uden at reducere andre aktiers normale anbefaling. Faktiske køb i købsvinduet huskes som Maks. godkendt %PF. Tilladelsen bortfalder ved Sælg eller ved mindst 20 % fald i Bull- eller Bear-kursmålet siden det godkendte køb.
# - Version 6.84: Købsvinduets % over Bear og maksimale faktor kan indstilles. Den faktiske købsvinduefaktor er dynamisk og afhænger af afstand til Bear samt Bull/Base-potentiale med 70/30-vægtning; maksimal faktor er et loft, ikke en fast multiplikator.
# - Version 6.85: Faktiske køb foretaget i et aktivt købsvindue gemmes som særskilte begivenheder i kursmålshistorikken med kurs, Bull/Base/Bear, procentmål, antal og opnået %PF. Begivenhederne påvirker ikke KM-alder eller kursmålsstøjfilter.
# - Version 6.86: Gør Forklaring til farve på rækker lodret scrollbar. Købsvinduets øvre grænse beregnes nu som Bear + den indstillede procent af spændet (Bull − Bear), i stedet for procent af Bear.
# - Version 6.87: Omdøber Kursmålshistorik til Aktiens historik, registrerer alle reelle køb og salg med kurs/Bull/Base/Bear samt procentmål, og flytter de fire Fase 2-handlingsknapper mod venstre.
# - Version 6.88: Venstrestiller knappen Indstil købsvindue med de øvrige indstillingsknapper og gør Begivenhed-kolonnen i Aktiens historik bredere.
# - Version 6.89: Gør Aktiens historik-vinduet bredere, så hele informationslinjen øverst kan ses uden manuel udvidelse.
# - Version 6.90: Fase 2 får en kompakt kurspositionsindikator mellem Aktier+/- og Bull %, hvor Bear er venstre ende, Bull højre ende, Base markeres diskret og aktuel kurs tydeligt. Navn og Antal gøres lidt smallere.
# - Version 6.91: Forenkler Kursmål-indikatoren til 15 faste tegn med prikker og én lodret kursmarkør. Fase 2 viser scenarierne i rækkefølgen Bear %, Base %, Bull %.
# - Version 6.92: Fase 2 får kolonnen Udbytte % mellem Til regnskab og Tillid. Værdien hentes som TradingViews aktuelle/indikerede dividend yield og påvirker endnu ingen scorer eller anbefalet %PF.
# - Version 6.93: Fase 2 får Frekvens og Næste udbytte efter Udbytte %. Frekvens hentes fra TradingViews dividend-side og vises på dansk; Næste udbytte viser måneden for næste kendte betalingsdato. Felterne påvirker endnu ingen scorer eller anbefalet %PF.
# - Version 6.94: Retter Næste udbytte med robust betalingsdato-fallback og beregnet næste måned fra seneste kendte udbyttedato + frekvens. Beregnede måneder markeres med ~. Fjerner den overflødige købsvindue-forklaringstekst under skyderen i Fase 2.
# - Version 6.95: Erstatter Næste udbytte med Seneste udbytte (rå TradingView-dato vist som måned), beregner Udbyttemåned(er) fra seneste dato + frekvens og viser forventet Udbytte i måneden i DKK ud fra positionsværdi og årligt dividend yield.
# - Version 6.96: Gør Seneste udbytte robust med et særskilt TradingView-scanner-fallback for seneste/kommende ex-/betalingsdato. Udbytte-cache hæves til schema v6, så datoerne genhentes efter opgraderingen.
# - Version 6.97: Fjerner langsom felt-probing pr. aktie. Udbyttedato-fallback hentes nu i batch én gang for hele porteføljen, så normal datahentning igen er hurtig.
# - Version 6.98: Fase 2 gør Navn-kolonnen ca. 30 % smallere og udvider den eksisterende øverste summeringslinje med relevante summer og gennemsnit.
# - Version 6.99: Gør Børs- og Ticker-kolonnerne i Fase 2 en smule smallere fra 105 til 95 pixels.
# - Version 7.00: Gør Kurs (nu)- og Valuta-kolonnerne i Fase 2 tilsvarende lidt smallere.
# - Version 7.01: Gør Navn-kolonnen i Fase 2 lidt smallere igen for at frigøre plads, så Bull % lettere kan ses uden vandret scrolling.
# - Version 7.02: Retter den aktive Treeview-overskrivning i Fase 2, som hidtil tvang Navn tilbage til 205 px. Navn vises nu reelt med 125 px, så Bull % får mere plads i vinduet.
# - Version 7.04: Fjerner den synlige kolonne Udbytte i måneden i Fase 2 og tilføjer Udbytteoversigt med Januar-December samt Året. Alle aktier med positiv Udbytte % medtages, det fulde årlige estimerede udbytte fordeles på måneder, og øverste Samlet-række summerer både hver måned og hele året i DKK.
# - Version 7.05: Udbytteoversigt får Nr-kolonne med løbenummer, en tydelig fremhævet Samlet-række og åbner maksimeret.
# - Version 7.06: Udbytteoversigt får større/federe Samlet-række end øvrige rækker samt kliksortering på alle kolonner, mens summeringen forbliver låst øverst.
# - Version 7.07: Samlet-rækken bruger samme skriftstørrelse som øvrige rækker, men fed skrift, og summeringer afrundes til hele DKK.
# - Version 7.08: Fjerner lys rød Fase 2-datavarsling for kort aktiehistorik. Kort historik kan fortsat dæmpe Aktiescore som hidtil; datavarsling bruges nu kun ved ugyldige analytikerscenarier.
# - Version 7.09: Bytter Bear- og Bull-kolonnerne i Fase 4, så rækkefølgen er Bear 1Y%, Base 1Y%, Bull 1Y%. Beregningerne er uændrede.
# - Version 7.10: Watch list-data hentes ikke længere ved programstart/hovedopdatering. Watch list opdateres normalt først ved åbning, kan forceres manuelt og kan redigeres direkte med nye potentielle aktier uden falske porteføljehandler.
# - Version 7.11: Watch list kan sorteres ved klik på alle kolonneoverskrifter. Gentaget klik skifter mellem stigende og faldende sortering, og aktiv sortering vises med ▲/▼.
# - Version 7.12: Fase 3-fordelinger kan sorteres på alle kolonner ved klik på kolonneoverskrifter. Sektorer, industrier, PE-grupper, regioner og Analytiker analyse bruger korrekt tekst-/talsortering med ▲/▼, mens summeringsrækker holdes fast øverst.
# - Version 7.13: Fase 2 får AI-katalysator via OpenAI Responses API med web search. Manuel batch-opdatering udfylder en sorterbar AI-katalysator-kolonne, markeret aktie kan åbnes i en uddybende analyse, og AI-prompten kan redigeres eller nulstilles til standard. API-nøglen gemmes ikke i programfilen.
# - Version 7.14: Erstatter OpenAI-katalysatoren med gratis Marketaux-data. Lokal cache pr. programmappe, 100 kald/dag, prioritering af manglende/ældste aktier, justerbar opdateringsfrekvens og deterministisk 0-10 katalysatorscore.
# - Version 7.15: Optimerer Fase 2-layout: Katalysator flyttes direkte efter Bull %, og Maks. godkendt %PF flyttes direkte efter Til regnskab.
# - Version 7.16: Watch list viser kursmål og procentmål i rækkefølgen Bear, Base, Bull, så scenarierækkefølgen matcher Fase 2 og Fase 4.
# - Version 7.17: Marketaux API-token gemmes i en separat fil i programmappen efter første indtastning og genbruges automatisk ved senere programstarter.
# - Version 7.18: Omdøber strukturlaget Spekulation til Potentiale og bruger laggrænserne Fundament 70-100, Vækst 56-69, Accelerator 40-55 og Potentiale 0-39.
# - Version 7.19: Aktiens historik viser både absolutte kursmål og procentmål i rækkefølgen Bear, Base, Bull.
# - Version 7.20: Tilføjer Rotationsanalyse i Fase 2. En potentiel aktie sammenlignes med de mest rollelignende aktive positioner ud fra strukturlag, sektor, industri, region og kvalitet. Rotation foreslås kun ved tydeligt bedre aktuelt forecast, moden eksisterende position og tilstrækkeligt rollematch.
# - Version 7.21: Forenkler Rotationsanalysens Modenhed til kun Base %-potentiale (40 % = 0, 0 % = 100), viser Udfordreren som blå første række, omdøber Konklusion til Note, fjerner Forecast-fordel fra visningen og gør vinduet bredt uden vandret scrollbar.
# - Version 7.22: Udfordreren får samme Base %-baserede Modenhedsscore som porteføljeaktierne, så modenhed kan sammenlignes direkte i Rotationsanalysen.
# - Version 7.23: Rotationsanalysen gør alle kolonner sorterbare, lader Udfordreren indgå normalt i sorteringen med blå markering, tilføjer Region og renser Rollematch til Strukturlag/Sektor/Industri/Region.
# - Version 7.24: Rotationsanalysen viser Kurs samt absolutte Bear/Base/Bull-kursmål før procentkolonnerne og åbner i fuld skærmbredde. De nye kolonner er sorterbare.
# - Version 7.25: Rotationsanalysens Modenhed er nu kursens direkte procentvise afstand til absolut Base: (Kurs/Base - 1) x 100. Base er 0 %, under Base er negativt og over Base positivt. Tabellen åbner som standard sorteret efter højeste Modenhed.
# - Version 7.28: Fjerner det valgfrie navneinput i Rotationsanalysen. Kun Børs og Ticker indtastes; selskabsnavnet hentes automatisk fra TradingView.
# - Version 7.29: Tilføjer Struktur som ekstra Fase 3-fordeling med de fire strukturlag, aktuel lagandel, anbefalet lagandel, antal positioner og vægtet FC1Y%.
# - Version 7.30: Nummererer strukturlag visuelt som 1 Fundament, 2 Vækst, 3 Accelerator og 4 Potentiale i Fase 3. Struktur-fordelingen bruger kolonnenavnet Strukturlag og åbner i fast lagrækkefølge med Fundament først.
# - Version 7.32: Fase 4 – gevinstsikring får kolonnen Værdi DKK mellem Antal og GAK. Værdien er aktuel positionsværdi i DKK, kan sorteres og summeres i den faste sum-/gennemsnitsrække.
# - Version 7.33: Flytter den faste Sum / gennemsnit-række i Fase 4 fra nederst til øverst. Rækken forbliver låst øverst uafhængigt af sortering.
# - Version 7.34: Tilføjer Kontanter til rådighed som fast nederste række i Fase 4 og afrunder PF-værdi DKK i statuslinjen til hele kroner.
# - Version 7.35: Fase 4 medregner Kontanter til rådighed i Værdi DKK på den øverste Sum / gennemsnit-række.
# - Version 7.36: Aktiens historik efterfylder køb registreret før første dataopdatering med handelsdagens første komplette Kurs/Bear/Base/Bull-snapshot og tilhørende procentmål.
# - Version 7.26: Rotationsanalysen erstatter Modenhed med beslutningsmarginer til Skift: Potentiale til Skift, Rollematch til Skift og Kvalitet til Skift. Base % bevares som rådata. Skift kræver +20 pp Base-potentiale, Rollematch 80, kvalitet højst 10 point lavere og højst ét strukturlag væk. Overvej bruges ved mindst +10 pp Base-potentiale og Rollematch 70 med samme kvalitets-/lagkrav. Note viser Udfordreren/Behold/Overvej/Skift og er gjort bredere.
# - Version 7.27: Rotationsanalysen kræver nu identisk Strukturlag mellem udfordrer og eksisterende position for både Skift og Overvej. Øvrige rotationskrav er uændrede.
# - Version 6.64: Retter ETF-positioner, så valgt ETF findes via entydig børs:ticker-nøgle, og tabellen genindlæses ved faneskift og efter hentning af toppositioner.
# - Version 6.61: Retter strukturmotoren med glidende Market Cap-score, reel finansiel modenhed og nye laggrænser: Fundament 70+, Vækst 55-69,9, Accelerator 40-54,9 og Spekulation under 40 (senere justeret i v7.18). Spekulationsstraffen er uændret.
# - Version 6.60: Ændrer Strukturscorens grundvægte til 45% størrelse, 30% kvalitet, 15% finansiel modenhed og 10% robusthed. Spekulationsstraffen er uændret.
# - Version 6.59: Ændrer Strukturscorens grundvægte til 40% størrelse, 30% kvalitet, 20% finansiel modenhed og 10% robusthed. Spekulationsstraffen er uændret.
# - Version 6.54: Næste regnskabsdato vises som en tydelig række i kursmålshistorikken. Kalenderdata genhentes én gang for både aktive aktier og Watch list.
# - Version 6.53: Retter kalender-cache for både aktive aktier og Watch list, så næste regnskabsdato faktisk genhentes og vises.
# - Version 6.23: Tilføjer knappen Forklaring til farve på rækker i Fase 2 med forklaring af salg, datavarsling og gul/orange analytikermarkering.
#
# JSON-format:
# [
#   {"exchange": "NASDAQ", "ticker": "NVDA", "name": "Nvidia", "antal": 10},
#   {"exchange": "XETR", "ticker": "SXR8", "name": "iShares Core S&P 500", "antal": 5}
# ]

import json
import re
import os
import csv
import threading
import time
import unicodedata
from zipfile import ZipFile
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import date, datetime, timezone, timedelta
from html import unescape
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen
try:
    import tkinter as tk
    from tkinter import ttk, messagebox, filedialog, simpledialog
    import tkinter.font as tkfont
except Exception:
    tk = ttk = messagebox = filedialog = simpledialog = tkfont = None

import pandas as pd

try:
    from tvDatafeed import TvDatafeed, Interval
except Exception:
    TvDatafeed = None
    Interval = None

DEFAULT_PORTFOLIO_FILE = Path.cwd() / "portefolje_default.json"
DAILY_CACHE_FILE = Path.cwd() / "portefolje_dagsdata_cache.json"
VALUE_SETTINGS_FILE = Path.cwd() / "portefolje_vaerdiscore_indstillinger.json"
ALLOCATION_SETTINGS_FILE = Path.cwd() / "portefolje_region_sektor_indstillinger.json"
TARGET_AGE_FILE = Path.cwd() / "portefolje_kursmaal_alder.json"
STOCK_REGISTRY_FILE = Path.cwd() / "portefolje_aktiekartotek.json"
VIX_SETTINGS_FILE = Path.cwd() / "portefolje_vix_kontant_indstillinger.json"
STRUCTURE_SETTINGS_FILE = Path.cwd() / "portefolje_struktur_indstillinger.json"
ETF_LIST_FILE = Path.cwd() / "etf_liste.json"
ETF_HOLDINGS_FILE = Path.cwd() / "portefolje_etf_positioner.json"
ETF_SETTINGS_FILE = Path.cwd() / "portefolje_etf_tema_indstillinger.json"
ETF_CACHE_FILE = Path.cwd() / "portefolje_etf_cache.json"
BUY_WINDOW_MEMORY_FILE = Path.cwd() / "portefolje_koebsvindue_hukommelse.json"
CATALYST_FILE = Path.cwd() / "portefolje_marketaux_katalysator.json"
MARKETAUX_TOKEN_FILE = Path.cwd() / "marketaux_api_token.txt"

# Porteføljebygger v0.41
# v0.41: Synkroniserer relevante Fase 3-forbedringer fra Porteføljesimulator v7.78. Nye sektor-defaults er 35/9/15/6/10/5/6/6/3/2/3/0 og gamle urørte defaults migreres uden at overskrive brugerens egne valg. Fase 3 får udvidet præsentation med Struktur først, anbefalet antal positioner/diversifikationsmål, PE- og FC1Y-mål samt tydeligt nedtrykte fordelingsknapper. Industriens neutrale anbefaling kobles til sektorernes mål: Samlet og Efter sektor bruger samme sektormål, manglende sektorer vises korrekt, og Andre industrier placeres nederst så neutral anbefaling summerer til 100 %. Industriscore i analysevisningen bruger samme dynamiske sektorbaserede mål, mens Porteføljebyggerens særskilte brugerpræferencer for industrier i selve optimeringen bevares.
# Porteføljebygger v0.40
# v0.40: Opdaterer Fase 1-standardmålene til samme profil som Porteføljesimulatoren: Strukturlag 60/25/10/5 og sektorfordeling med 35 % Teknologi. Gamle uændrede standardværdier migreres automatisk, mens egne brugerdefinerede værdier bevares.
# Porteføljebygger v0.39
# v0.39: Tilpasser webordreimporten til det aktuelle APB-webformat med visningsnavne i Priorities,
# kundens frivillige navn, servergenereret ordrenummer, submitted_at_display/status og robust validering.
# Ældre snake_case-webordrer understøttes fortsat for bagudkompatibilitet.
# Porteføljebygger v0.38
# v0.43: Fase 4 – Kundeoutput genererer nu kun én samlet JSON-resultatfil til SIMGROVA.
# JSON-resultatet bevarer webordrens user_id, access_code og order_number samt kundeoplysninger og originale inputvalg.
# Resultatet indeholder den byggede portefølje, kontanter, kundeegnede Fase 2-data og Fase 3-analyser – uden interne scorer.
# v0.38: Webordreimport, DKK/EUR/USD i Fase 1 og ny Fase 4 – Kundeoutput.
# Webordre JSON overfører grundregler, prioriteringer, sektorer, industrier, regioner, strukturlag, kursmålstrend og udbytte.
# Kunde-Excel udelader interne scorer; analyse-PDF samler Fase 3 i præsentationsform.
# Porteføljebygger v0.35
# v0.37: Tilføjer knappen Reklame ved forklaringsknapperne. Knappen åbner Startscreen.png som en centreret reklame/startskærm oven på programmet med en lille Luk-knap og Esc-genvej. Opstarts-startskærmen og automatisk maksimering fra v0.36 bevares.
# v0.36: Hovedvinduet maksimeres automatisk ved opstart og maksimeres igen, hvis det flyttes til en anden skærm.
# v0.35: Tilføjer en professionel startskærm. Hvis Startscreen.png findes i samme mappe som programfilen (eller i den aktuelle programmappe), vises billedet centreret uden vinduesramme under opstart. Hovedvinduet holdes skjult, indtil aktieunivers og gemte data er klargjort. Startskærmen vises mindst ca. 1,8 sekunder og lukkes derefter automatisk. Hvis billedet mangler eller ikke kan læses, starter programmet normalt uden fejl.
# Porteføljebygger v0.34
# v0.34: Retter manuel kolonnebredde i alle fælles Fase-tabeller. Kolonner strækkes ikke længere automatisk mod vinduets bredde, så ændring af én kolonne ikke kollapser nabokolonnen. Alle kolonner får samtidig en reel minimumsbredde, og vandret scrollbar overtager pladsstyringen når den samlede tabel bliver bredere end vinduet.
# Porteføljebygger v0.33
# v0.33: Fase 1 opdeler den tidligere region Norden i Danmark og Øvrige Norden. Standardfordelingen er 5 % Danmark og 5 % Øvrige Norden. TradingView-landet Denmark mappes til Danmark, mens Norge, Sverige, Finland og Island mappes til Øvrige Norden. Gamle gemte Fase 1-indstillinger med Norden migreres automatisk ved at dele den tidligere Norden-procent ligeligt mellem de to nye regioner.
# Porteføljebygger v0.32
# v0.32: Fase 1 får separate Default-knapper for Prioritering, Sektorer, Regioner og Strukturlag. Hver knap nulstiller kun sin egen sektion til programmets forudindstillede standardværdier. De aktuelle Fase 1-indstillinger gemmes desuden ved normal programlukning, så senest anvendte/viste værdier gendannes ved næste start, også hvis der ikke blev bygget en portefølje.
# Porteføljebygger v0.31
# v0.31: BYG PORTEFØLJE kører nu selve den tunge optimering i en baggrundstråd, så Tkinter-GUI ikke fryser. En heartbeat-status opdateres cirka hvert sekund og viser løbende hvilket trin/iteration/test byggemotoren arbejder med. Byggelogik, scorer, byttekriterier og kapitaloptimering er uændrede.
# Porteføljebygger v0.30
# v0.30: Retter den tilbagevendende Fase 0-fejl, hvor aktieuniverset kunne skrumpe under samtidig cacheopdatering og GUI-refresh. Aktieuniverset læses/skrivebeskyttes nu med trådlås, gemmes atomisk og får en backup. En midlertidig JSON-læsefejl må ikke længere udløse fallback til aktiekartoteket og overskrive det fulde univers.
# Porteføljebygger v0.29
# v0.29: Fase 2 overtager Porteføljesimulator v7.54's kontinuerlige Bear/Base/Bull-farvelogik inkl. den tidligere og kraftigere visuelle påvirkning fra den hårde salgsregel. Manglende/ugyldige analytikerdata markeres lilla som i simulatoren. Fase 0 bruger samme analytikerfarve kun for aktier med komplette indlæste data; ikke-indlæste aktier vises neutralt. Låste aktier har altid højeste visuelle prioritet i Fase 0 og markeres neutralt grå, så låsestatus ikke kan forveksles med et køb/salgssignal.
# Porteføljebygger v0.28
# v0.28: VIX gøres robust i Porteføljebyggeren. Dagens VIX hentes og caches automatisk, hvis den mangler, når Fase 2 aktiveres. Normal opdatering af aktieuniverset henter kun VIX hvis dagens værdi mangler, mens forceret opdatering altid henter VIX på ny. Hentning ved faneskift kører i baggrundstråd, så brugerfladen ikke fryser.
# Porteføljebygger v0.27
# v0.27: Rydder Fase 2 op til ren analysevisning. Alle påvirkningsskydere og tilhørende indstillingsknapper fjernes fra Fase 2, da den byggede %PF er faktisk porteføljevægt og ikke en efterfølgende anbefalet vægt. Kontant-/VIX-styring fjernes også; kun aktuel VIX-information bevares som markedsreference. Fase 2 viser herefter kun VIX samt knapperne Forklaring til farve på rækker, Aktiens historik og Udbytteoversigt.
# Porteføljebygger v0.26
# v0.26: Aktiens historik er nu beskyttet mod manuel sletning. Knappen og den tilhørende slettefunktion er fjernet fra historikvinduet; historikken bevares permanent og udbygges fortsat automatisk.
# Porteføljebygger v0.25
# v0.25: Fase 2 får knappen Aktiens historik for den markerede aktie. Historikvinduet i Porteføljebyggeren viser kun kursmålsændringer og regnskaber (ingen køb/salg), samt de to tidsseriegrafer med hover.
# Fase 3 får fanen Kursmålsanalyse samlet som i Porteføljesimulatoren: gennemsnitlige Bear/Base/Bull-kursmål absolut i DKK og procentuelt, samt diskret gennemsnitlig kursudvikling for den aktuelt byggede portefølje.
# Porteføljebygger v0.25
# v0.25: Retter langsom/blokerende opstart fra v0.25. GUI vises før cache-genopbygning, og Fase 0-preview genbruger én indlæst historik uden at skrive kursmål/regnskabsbegivenheder pr. aktie.
# Opstartsstatus forklarer tydeligt, når gemte data og senest byggede portefølje gendannes.
# Porteføljebygger v0.25
# v0.25: Fase 0 viser de bagvedliggende analyse-/byggedata efter Industri. Fase 2 udfylder Regionscore, Sektorscore og Industriscore ud fra den færdigbyggede portefølje.
# Aktiens historik opdateres permanent for hele aktieuniverset og bevares uafhængigt af aktieunivers.json; historikken kan ikke slettes fra brugerfladen.
# Fase 1 får den valgfri, bløde prioritering Kursmålstrend baseret på de to seneste reelle Bear/Base/Bull-kursmål (25/50/25). Manglende historik behandles neutralt.
# Porteføljebygger v0.25
# v0.25: Fase 0 markerer låste aktier med en lidt dybere grøn/rød nuance end frie aktier.
# Fase 2 skjuler Frekvens, Seneste udbytte og Udbyttemåned i hovedtabellen; Udbytte % og Udbytteoversigt bevares.
# Porteføljebygger v0.25
# v0.25: Fase 0 – tilføjer Region, Sektor og Industri efter Status. Kolonnerne er sorterbare.
# Porteføljebygger v0.25
# v0.25: Fase 0 – Aktieunivers kan sorteres på alle kolonner via klik på overskriften.
# Gentaget klik skifter stigende/faldende, og aktiv kolonne markeres med ▲/▼.
# Porteføljebygger v0.25
# v0.25: Udbytteoversigten låser nu præcis den aktuelt viste Fase 2-portefølje ved klik.
# Porteføljen genindlæses eller genopbygges ikke under udbytteopdateringen; kun udbyttefelter opdateres.
# Match sker entydigt på børs+ticker, mens layout og progress-visning fra v0.25 bevares.
# Porteføljebygger v0.25
# v0.25: Udbytteoversigtens layout er genetableret til v0.12-layoutet uændret.
# Udbytteopdateringen kører i baggrundstråd med synlig status/progress, så GUI ikke fryser.
# Den byggede portefølje i portefolje_fase2.json er fortsat entydig sandhedskilde.
# Porteføljebygger v0.25
# v0.25: Udbytteoversigten bruger portefolje_fase2.json som entydig sandhedskilde,
# opdaterer udbyttedata for netop disse positioner og genopbygger Fase 2 før visning.
# v0.25: Udbytteoversigten synkroniseres altid med den senest byggede portefølje.
# Den byggede Fase 2-porteføljesammensætning gemmes desuden i portefolje_fase2.json
# (børs, ticker, navn og antal), indlæses automatisk ved næste programstart og kan
# kopieres direkte til en anden programmappe som standardportefølje.
# Industripræferencerne fra v0.25 bevares uændret.
STOCK_UNIVERSE_FILE = Path.cwd() / "aktieunivers.json"
STOCK_UNIVERSE_BACKUP_FILE = Path.cwd() / "aktieunivers_backup.json"
# Fase 0 kan læses fra GUI-tråden samtidig med, at data-worker gemmer universet.
# Låsen + atomisk filudskiftning forhindrer, at GUI'en ser en halvskrevet JSON-fil.
_stock_universe_file_lock = threading.RLock()
_stock_universe_last_good = []
BUILDER_SETTINGS_FILE = Path.cwd() / "portefoljebygger_indstillinger.json"
BUILT_PORTFOLIO_FILE = Path.cwd() / "portefolje_bygget.json"
PHASE2_PORTFOLIO_FILE = Path.cwd() / "portefolje_fase2.json"
WEB_ORDER_CONTEXT_FILE = Path.cwd() / "apb_webordre_aktiv.json"
CUSTOMER_OUTPUT_DIR = Path.cwd() / "kundeoutput"
SUPPORTED_PORTFOLIO_CURRENCIES = ("DKK", "EUR", "USD")

# Marketaux-katalysator. Token gemmes separat i programmappen efter første indtastning.
# MARKETAUX_API_TOKEN kan fortsat valgfrit sættes som miljøvariabel og har første prioritet.
MARKETAUX_DAILY_LIMIT = 100
DEFAULT_CATALYST_UPDATE_DAYS = 1
_marketaux_api_token_session = ""

# TradingViews offentliggjorte Market Cap-kategorier i USD.
# Grænserne kan ændres fra Fase 3 -> Porteføljestruktur.
DEFAULT_MARKET_CAP_LIMITS_USD = [
    [50_000_000.0, "Nano", 0.0],
    [300_000_000.0, "Micro", 20.0],
    [2_000_000_000.0, "Small", 40.0],
    [10_000_000_000.0, "Mid", 65.0],
    [200_000_000_000.0, "Large", 90.0],
    [None, "Mega", 100.0],
]

# Spekulationskorrektion: højeste opfyldte Bull-grænse giver den angivne straf.
# Kun ekstreme Bull-forventninger påvirkes; normale aktier får 0 i straf.
DEFAULT_SPECULATION_PENALTIES = [
    [100.0, 1.0],
    [200.0, 2.0],
    [250.0, 3.0],
    [300.0, 4.0],
    [350.0, 5.0],
    [400.0, 6.0],
    [450.0, 7.0],
    [500.0, 8.0],
]
market_cap_limits_usd = [row[:] for row in DEFAULT_MARKET_CAP_LIMITS_USD]
speculation_penalties = [row[:] for row in DEFAULT_SPECULATION_PENALTIES]
saved_structure_profile = "Balanceret"

DEFAULT_VIX_CASH_LEVELS = [
    [15.0, 4.0],
    [18.0, 5.0],
    [20.0, 7.0],
    [23.0, 10.0],
    [25.0, 15.0],
    [28.0, 20.0],
    [30.0, 25.0],
    [35.0, 30.0],
    [None, 40.0],
]
vix_cash_levels = [row[:] for row in DEFAULT_VIX_CASH_LEVELS]
current_vix_value = None
_vix_fetch_in_progress = False

# Mindste relative ændring i et synligt absolut kursmål, før den regnes som
# en reel analytikeropdatering og gemmes i historikken.
TARGET_HISTORY_MIN_CHANGE_PCT = 2.0

OLD_DEFAULT_VALUE_SCORE_POINTS = [
    [2.0, 100.0],
    [3.0, 98.0],
    [5.0, 94.0],
    [8.0, 88.0],
    [12.0, 80.0],
    [20.0, 65.0],
    [30.0, 50.0],
    [50.0, 35.0],
]

DEFAULT_VALUE_SCORE_POINTS = [
    [1.0, 100.0],
    [2.0, 98.0],
    [3.0, 95.0],
    [5.0, 90.0],
    [8.0, 82.0],
    [12.0, 72.0],
    [20.0, 55.0],
    [30.0, 40.0],
    [50.0, 25.0],
]
DEFAULT_VALUE_INFLUENCE = 0.50
value_score_points = [row[:] for row in DEFAULT_VALUE_SCORE_POINTS]
value_influence = DEFAULT_VALUE_INFLUENCE

REGION_CATEGORIES = ["USA", "Canada", "Danmark", "Øvrige Norden", "Europa", "Japan", "Kina / Hongkong", "Øvrige Asien", "Emerging Markets", "Andre lande"]
SECTOR_CATEGORIES = ["Teknologi", "Finans", "Sundhed", "Industri", "Forbrug cyklisk", "Forbrug defensivt", "Energi", "Materialer", "Forsyning", "Transport", "Kommunikation", "Andre sektorer"]

DEFAULT_REGION_TARGETS = {
    "USA": 45.0, "Canada": 5.0, "Danmark": 5.0, "Øvrige Norden": 5.0, "Europa": 20.0,
    "Japan": 5.0, "Kina / Hongkong": 4.0, "Øvrige Asien": 6.0,
    "Emerging Markets": 3.0, "Andre lande": 2.0,
}
OLD_DEFAULT_SECTOR_TARGETS = {
    "Teknologi": 15.0, "Finans": 12.0, "Sundhed": 12.0, "Industri": 14.0,
    "Forbrug cyklisk": 10.0, "Forbrug defensivt": 10.0, "Energi": 8.0,
    "Materialer": 7.0, "Forsyning": 6.0, "Transport": 3.0,
    "Kommunikation": 3.0, "Andre sektorer": 0.0,
}
PREVIOUS_DEFAULT_SECTOR_TARGETS = {
    "Teknologi": 35.0, "Finans": 9.0, "Sundhed": 12.0, "Industri": 10.0,
    "Forbrug cyklisk": 10.0, "Forbrug defensivt": 5.0, "Energi": 6.0,
    "Materialer": 5.0, "Forsyning": 3.0, "Transport": 2.0,
    "Kommunikation": 3.0, "Andre sektorer": 0.0,
}
DEFAULT_SECTOR_TARGETS = {
    "Teknologi": 35.0, "Finans": 9.0, "Sundhed": 15.0, "Industri": 6.0,
    "Forbrug cyklisk": 10.0, "Forbrug defensivt": 5.0, "Energi": 6.0,
    "Materialer": 6.0, "Forsyning": 3.0, "Transport": 2.0,
    "Kommunikation": 3.0, "Andre sektorer": 0.0,
}
DEFAULT_COUNTRY_MAP = {
    "United States": "USA", "Canada": "Canada",
    "Denmark": "Danmark", "Norway": "Øvrige Norden", "Sweden": "Øvrige Norden", "Finland": "Øvrige Norden", "Iceland": "Øvrige Norden",
    "Ireland": "Europa", "Luxembourg": "Europa", "Switzerland": "Europa", "Germany": "Europa", "Italy": "Europa",
    "France": "Europa", "United Kingdom": "Europa", "Spain": "Europa", "Netherlands": "Europa", "Belgium": "Europa",
    "Austria": "Europa", "Portugal": "Europa", "Greece": "Europa", "Poland": "Europa", "Czech Republic": "Europa",
    "Japan": "Japan", "China": "Kina / Hongkong", "Hong Kong": "Kina / Hongkong",
    "Taiwan": "Øvrige Asien", "Singapore": "Øvrige Asien", "South Korea": "Øvrige Asien", "Australia": "Øvrige Asien", "New Zealand": "Øvrige Asien",
    "India": "Emerging Markets", "Brazil": "Emerging Markets", "Mexico": "Emerging Markets", "Argentina": "Emerging Markets",
    "South Africa": "Emerging Markets", "Indonesia": "Emerging Markets", "Malaysia": "Emerging Markets", "Thailand": "Emerging Markets",
    "United Arab Emirates": "Emerging Markets", "Israel": "Andre lande", "Bermuda": "Andre lande",
}
DEFAULT_SECTOR_MAP = {
    "Technology Services": "Teknologi", "Electronic Technology": "Teknologi",
    "Finance": "Finans",
    "Health Technology": "Sundhed", "Health Services": "Sundhed",
    "Producer Manufacturing": "Industri", "Industrial Services": "Industri", "Commercial Services": "Industri",
    "Retail Trade": "Forbrug cyklisk", "Consumer Durables": "Forbrug cyklisk", "Consumer Services": "Forbrug cyklisk",
    "Consumer Non-Durables": "Forbrug defensivt",
    "Energy Minerals": "Energi",
    "Non-Energy Minerals": "Materialer", "Process Industries": "Materialer",
    "Utilities": "Forsyning", "Transportation": "Transport", "Communications": "Kommunikation",
    "Miscellaneous": "Andre sektorer", "Sektor ukendt": "Andre sektorer",
}
DEFAULT_ALLOCATION_INFLUENCE = 0.35
DEFAULT_INDUSTRY_INFLUENCE = 0.25
# Kursmålets påvirkning er 0 som standard, så eksisterende porteføljer bevarer
# deres nuværende vægtning, indtil skyderen aktivt tages i brug.
DEFAULT_TARGET_INFLUENCE = 0.0
# Købsvindue-indstillinger. Maksimal faktor er et loft; den faktiske faktor
# beregnes dynamisk ud fra prisens placering tæt på Bear samt Bull/Base-potentialet.
DEFAULT_BUY_WINDOW_MAX_FACTOR = 5.0
DEFAULT_BUY_WINDOW_ABOVE_BEAR_PCT = 10.0
BUY_WINDOW_BULL_WEIGHT = 0.70
BUY_WINDOW_BASE_WEIGHT = 0.30
buy_window_max_factor = DEFAULT_BUY_WINDOW_MAX_FACTOR
buy_window_above_bear_pct = DEFAULT_BUY_WINDOW_ABOVE_BEAR_PCT
DEFAULT_INDUSTRY_TARGET = 3.0
DEFAULT_KNOWN_INDUSTRIES = [
    "Packaged Software", "Semiconductors", "Internet Software/Services", "Electrical Products",
    "Integrated Oil", "Aerospace & Defense", "Internet Retail", "Finance/Rental/Leasing",
    "Electric Utilities", "Property/Casualty Insurance", "Major Banks", "Pharmaceuticals: Major",
    "Engineering & Construction", "Telecommunications Equipment", "Air Freight/Couriers",
    "Industrial Machinery", "Regional Banks", "Electronic Production Equipment", "Managed Health Care",
    "Oil & Gas Production", "Precious Metals", "Biotechnology", "Other Transportation",
    "Electronic Components", "Recreational Products", "Specialty Stores", "Hospital/Nursing Management",
    "Other Metals/Minerals", "Medical Specialties", "Steel", "Beverages: Non-Alcoholic",
    "Computer Peripherals", "Information Technology Services", "Data Processing Services",
    "Apparel/Footwear", "Motor Vehicles", "Computer Processing Hardware", "Specialty Telecommunications",
    "Investment Trusts/Mutual Funds", "Financial Publishing/Services", "Insurance Brokers/Services",
    "Trucks/Construction/Farm Machinery", "Chemicals: Specialty", "Hotels/Resorts/Cruise lines",
    "Real Estate Development", "Miscellaneous Commercial Services", "Food Retail", "Airlines",
    "Forest Products", "Household/Personal Care", "Real Estate Investment Trusts",
    "Investment Banks/Brokers", "Investment Managers", "Consumer Sundries",
    "Agricultural Commodities/Milling",
]
region_targets = dict(DEFAULT_REGION_TARGETS)
sector_targets = dict(DEFAULT_SECTOR_TARGETS)
country_map = dict(DEFAULT_COUNTRY_MAP)
sector_map = dict(DEFAULT_SECTOR_MAP)
region_influence = DEFAULT_ALLOCATION_INFLUENCE
sector_influence = DEFAULT_ALLOCATION_INFLUENCE
industry_influence = DEFAULT_INDUSTRY_INFLUENCE
target_influence = DEFAULT_TARGET_INFLUENCE
industry_default_target = DEFAULT_INDUSTRY_TARGET
industry_target_overrides = {}
unknown_country_values = set()
unknown_sector_values = set()

DEFAULT_PORTFOLIO = [
    {"exchange": "NASDAQ", "ticker": "NVDA", "name": "Nvidia", "antal": 1},
    {"exchange": "NASDAQ", "ticker": "MSFT", "name": "Microsoft", "antal": 1},
    {"exchange": "NASDAQ", "ticker": "AMZN", "name": "Amazon", "antal": 1},
    {"exchange": "XETR", "ticker": "SXR8", "name": "iShares Core S&P 500", "antal": 1},
]

CASH_EXCHANGE = "CASH"
CASH_TICKER = "DKK"
CASH_NAME = "Kontanter til rådighed"



# Børs -> valuta.
# Børs-kolonnen bruges dermed til at omregne hver positions markedsværdi til DKK.
# Tilføj blot flere børser her, hvis porteføljen senere udvides.
EXCHANGE_CURRENCY = {
    # Kontanter / Danmark
    "CASH": "DKK",
    "OMXCOP": "DKK", "CPH": "DKK", "NASDAQCOPENHAGEN": "DKK",
    # Sverige / Norge
    "OMXSTO": "SEK", "STO": "SEK",
    "OSL": "NOK", "OSE": "NOK",
    # USA / Canada
    "NASDAQ": "USD", "NYSE": "USD", "AMEX": "USD", "NYSEARCA": "USD", "BATS": "USD",
    "OTC": "USD", "OTCMKTS": "USD", "OTCQX": "USD", "OTCQB": "USD", "OTCGREY": "USD",
    "TSX": "CAD", "TSXV": "CAD",
    # Euro-børser
    "XETR": "EUR", "FWB": "EUR", "GETTEX": "EUR", "TRADEGATE": "EUR",
    "OMXHEX": "EUR", "HEL": "EUR", "NASDAQHELSINKI": "EUR",
    "EURONEXT": "EUR", "EPA": "EUR", "PAR": "EUR", "AMS": "EUR", "MIL": "EUR", "BIT": "EUR",
    # UK – TradingView/LSE bruger ofte GBX (pence) for London-noterede papirer.
    "LSE": "GBX", "LON": "GBX",
    # Schweiz
    "SIX": "CHF", "SWX": "CHF",
}

# Valutapar på TradingView. Kursen betyder: 1 valutaenhed = X DKK.
# GBX håndteres særskilt som GBP/100.
FX_SYMBOLS_DKK = {
    "USD": ("FX_IDC", "USDDKK", 1.0),
    "EUR": ("FX_IDC", "EURDKK", 1.0),
    "SEK": ("FX_IDC", "SEKDKK", 1.0),
    "NOK": ("FX_IDC", "NOKDKK", 1.0),
    "GBP": ("FX_IDC", "GBPDKK", 1.0),
    "GBX": ("FX_IDC", "GBPDKK", 0.01),
    "CAD": ("FX_IDC", "CADDKK", 1.0),
    "CHF": ("FX_IDC", "CHFDKK", 1.0),
}

# Kun nødløsning hvis TradingView ikke returnerer et valutapar.
# Tallene kan ændre sig; statuslinjen viser, hvis fallback er brugt.
FALLBACK_FX_DKK = {
    "DKK": 1.0,
    "USD": 6.40,
    "EUR": 7.46,
    "SEK": 0.68,
    "NOK": 0.64,
    "GBP": 8.70,
    "GBX": 0.087,
    "CAD": 4.70,
    "CHF": 7.95,
}

PERIODS = [
    ("pct_1d", "%1D", 1),
    ("pct_5d", "%5D", 5),
    ("pct_14d", "%14D", 14),
    ("pct_1m", "%1M", 21),
    ("pct_2m", "%2M", 42),
    ("pct_3m", "%3M", 63),
    ("pct_4m", "%4M", 84),
    ("pct_5m", "%5M", 105),
    ("pct_6m", "%6M", 126),
    ("pct_12m", "%12M", 252),
    ("pct_2y", "%2Y", 504),
    ("pct_3y", "%3Y", 756),
    ("pct_4y", "%4Y", 1008),
    ("pct_5y", "%5Y", 1260),
]

COLUMNS = [
    ("rank", "Nr", 60),
    ("exchange", "Børs", 105),
    ("ticker", "Ticker", 105),
    ("name", "Navn", 280),
    ("antal", "Antal", 105),
    ("price", "Kurs (nu)", 105),
    ("currency", "Valuta", 75),
    ("value_dkk", "Værdi DKK", 130),
    ("weight", "% andel af PF", 145),
    ("pct_1d", "%1D", 95),
    ("pct_5d", "%5D", 95),
    ("pct_14d", "%14D", 95),
    ("pct_1m", "%1M", 95),
    ("pct_2m", "%2M", 95),
    ("pct_3m", "%3M", 95),
    ("pct_4m", "%4M", 95),
    ("pct_5m", "%5M", 95),
    ("pct_6m", "%6M", 95),
    ("pct_12m", "%12M", 100),
    ("pct_2y", "%2Y", 95),
    ("pct_3y", "%3Y", 95),
    ("pct_4y", "%4Y", 95),
    ("pct_5y", "%5Y", 95),
]

COLUMN_IDS = [c[0] for c in COLUMNS]

PHASE2_COLUMNS = [
    ("rank", "Nr", 60),
    ("exchange", "Børs", 95),
    ("ticker", "Ticker", 95),
    ("name", "Navn", 125),
    ("antal", "Antal", 85),
    ("price", "Kurs (nu)", 120),
    ("currency", "Valuta", 85),
    ("pct_1d", "%1D", 95),
    ("value_dkk", "Værdi DKK", 130),
    ("weight", "%PF", 145),
    ("target_position", "Kursmål", 105),
    ("analyst_bear_pct", "Bear %", 105),
    ("analyst_base_pct", "Base %", 105),
    ("analyst_bull_pct", "Bull %", 105),
    ("days_to_earnings", "Til regnskab", 118),
    ("dividend_yield", "Udbytte %", 100),
    ("stock_score", "Aktiescore", 120),
    ("quality_score", "Kvalitet", 110),
    ("confidence_score", "Tillid", 100),
    ("trend_strength", "Trendstyrke", 130),
    ("robustness", "Robusthed", 125),
    ("structure_score", "Strukturscore", 135),
    ("structure_layer", "Strukturlag", 135),
    ("value_score", "Værdiscore", 120),
    ("region_score", "Regionscore", 120),
    ("sector_score", "Sektorscore", 120),
    ("industry_score", "Industriscore", 125),
    ("pe", "PE", 85),
    ("peg", "PEG", 85),
    ("revenue_growth_3y", "Oms.vækst 3 år", 150),
    ("ebit_margin_ttm", "EBITmargin TTM", 145),
    ("roic", "ROIC", 100),
    ("fcf_margin_ttm", "FCF-margin", 125),
    ("fcf_growth_3y", "FCF-vækst 3 år", 145),
    ("kurs_f2", "Kurs", 105),
    ("sma50", "SMA50", 105),
    ("sector", "Sektor", 180),
    ("industry", "Industri", 230),
    ("country", "Land / Region", 170),
]
PHASE2_COLUMN_IDS = [c[0] for c in PHASE2_COLUMNS]

PHASE2B_COLUMNS = [
    ("rank", "Nr", 60),
    ("ticker", "Ticker", 105),
    ("name", "Navn", 320),
    ("price", "Kurs", 110),
    ("currency", "Valuta", 85),
    ("weight", "% andel af PF", 135),
    ("intrinsic_tangible_price", "Bogført kurs", 145),
    ("market_premium", "Præmie", 115),
    ("total_assets", "Samlede aktiver", 165),
    ("total_liabilities", "Samlede forpligtelser", 185),
    ("goodwill", "Goodwill", 135),
    ("shares_outstanding", "Antal aktier", 145),
    ("total_tangible_value", "Bogført værdi", 165),
]
PHASE2B_COLUMN_IDS = [c[0] for c in PHASE2B_COLUMNS]
PHASE3_COLUMNS = [
    ("category", "Kategori", 330),
    ("weight", "% andel af PF", 145),
    ("target_weight", "Anbefalet %PF", 155),
    ("count", "Antal positioner", 145),
    ("recommended_count", "Antal positioner anbefalet", 205),
    ("sector_count", "Antal sektorer", 135),
    ("recommended_sector_count", "Antal sektorer anbefalet", 195),
    ("industry_count", "Antal industrier", 140),
    ("region_count", "Antal regioner", 130),
    ("weighted_fc1y", "Vægtet FC1Y%", 150),
    ("recommended_fc1y", "Anbefalet FC1Y%", 165),
]
PHASE3_COLUMN_IDS = [c[0] for c in PHASE3_COLUMNS]

STRUCTURE_COLUMNS = [
    ("layer", "Strukturlag", 180),
    ("exchange", "Børs", 110),
    ("ticker", "Ticker", 110),
    ("name", "Navn", 360),
    ("structure_score", "Strukturscore", 135),
    ("weight", "% andel af PF", 145),
    ("target", "Anbefalet lagandel", 175),
    ("deviation", "Afvigelse", 130),
]
STRUCTURE_COLUMN_IDS = [c[0] for c in STRUCTURE_COLUMNS]

STRUCTURE_PROFILES = {
    "Balanceret": {
        "targets": {"Fundament": 60.0, "Vækst": 25.0, "Accelerator": 10.0, "Potentiale": 5.0},
        "description": "Normalmarked: 60% fundament, 25% vækst, 10% accelerator og 5% potentiale.",
    },
    "Defensiv / risk-off": {
        "targets": {"Fundament": 65.0, "Vækst": 25.0, "Accelerator": 8.0, "Potentiale": 2.0},
        "description": "Uroligt marked eller lav risikovillighed: større fundament og meget lille potentiale.",
    },
    "Offensiv / risk-on": {
        "targets": {"Fundament": 35.0, "Vækst": 40.0, "Accelerator": 20.0, "Potentiale": 5.0},
        "description": "Stærkt marked og høj risikovillighed: mere vækst og accelerator, men potentiale holdes stadig begrænset.",
    },
}
STRUCTURE_LAYER_ORDER = ["Fundament", "Vækst", "Accelerator", "Potentiale"]
STRUCTURE_LAYER_DISPLAY = {
    layer: f"{index}. {layer}" for index, layer in enumerate(STRUCTURE_LAYER_ORDER, start=1)
}

def structure_layer_display(layer):
    """Vis strukturlag med fast positionsnummer uden at ændre intern laglogik."""
    layer = str(layer or "Potentiale")
    return STRUCTURE_LAYER_DISPLAY.get(layer, layer)

def structure_layer_from_display(label):
    """Omsæt nummereret visningsnavn tilbage til internt strukturlag."""
    text = str(label or "").strip()
    for layer, display in STRUCTURE_LAYER_DISPLAY.items():
        if text == display:
            return layer
    return text

PHASE4_COLUMNS = [
    ("rank", "Nr", 55),
    ("ticker", "Ticker", 95),
    ("name", "Navn", 220),
    ("antal", "Antal", 85),
    ("value_dkk", "Værdi DKK", 115),
    ("gak", "GAK", 100),
    ("price", "Kurs nu", 100),
    ("unrealized_pct", "Ureal.%", 95),
    ("unrealized_dkk", "Ureal. DKK", 115),
    ("bear_now", "Bear 1Y%", 118),
    ("analyst_now", "Base 1Y%", 118),
    ("bull_now", "Bull 1Y%", 118),
    ("stock_score", "Aktiescore", 103),
    ("current_base_goal_progress", "Procent af Basemål", 240),
    ("current_bull_goal_progress", "Procent af Bullmål", 240),
]
PHASE4_COLUMN_IDS = [c[0] for c in PHASE4_COLUMNS]

FC1Y_BUCKETS = [
    ("FC1Y < 0%", None, 0),
    ("FC1Y 0-10%", 0, 10),
    ("FC1Y 10-20%", 10, 20),
    ("FC1Y 20-30%", 20, 30),
    ("FC1Y 30-40%", 30, 40),
    ("FC1Y 40-50%", 40, 50),
    ("FC1Y >50%", 50, None),
]

PE_BUCKETS = [
    ("PE 1-10", 1, 10),
    ("PE 10-20", 10, 20),
    ("PE 20-50", 20, 50),
    ("PE 50-100", 50, 100),
    ("PE 100-200", 100, 200),
    ("PE >200", 200, None),
]

PE_TARGET_WEIGHTS = {
    "PE 1-10": 5.0,
    "PE 10-20": 20.0,
    "PE 20-50": 55.0,
    "PE 50-100": 10.0,
    "PE 100-200": 5.0,
    "PE >200": 5.0,
}

FC1Y_TARGET_WEIGHTS = {
    "FC1Y < 0%": 0.0,
    "FC1Y 0-10%": 25.0,
    "FC1Y 10-20%": 15.0,
    "FC1Y 20-30%": 25.0,
    "FC1Y 30-40%": 10.0,
    "FC1Y 40-50%": 5.0,
    "FC1Y >50%": 20.0,
}

FC1Y_RECOMMENDED_LEVELS = {
    "FC1Y < 0%": 0.0,
    "FC1Y 0-10%": 5.0,
    "FC1Y 10-20%": 10.0,
    "FC1Y 20-30%": 25.0,
    "FC1Y 30-40%": 30.0,
    "FC1Y 40-50%": 40.0,
    "FC1Y >50%": 60.0,
}

STRUCTURE_RECOMMENDED_POSITION_SHARE = {
    "Fundament": 40.0, "Vækst": 30.0, "Accelerator": 20.0, "Potentiale": 10.0,
}

STRUCTURE_RECOMMENDED_SECTOR_MIN = {
    "Fundament": 5, "Vækst": 3, "Accelerator": 2, "Potentiale": 2,
}

portfolio = []
rows = []
phase2_rows = []
phase2b_rows = []
phase3_rows = []
phase3_current_view = ""
phase3_industry_mode = "flat"
phase3_current_sort = ""
phase3_descending = False
phase4_rows = []
phase4_current_sort = "rank"
phase4_descending = False
phase5_etf_rows = []
phase5_benchmark_rows = []
phase5_current_etf_key = ""
current_sort = "rank"
descending = False
phase2_current_sort = "rank"
phase2_descending = False
phase2b_current_sort = "rank"
phase2b_descending = False

# Når Fase 0 kun laver en visuel preview af cachedata, må make_phase2_row ikke
# skrive til historikfilen for hver enkelt aktie. Det gjorde v0.25-opstarten
# meget langsom, fordi samme JSON blev læst/renset/gemt hundredvis af gange.
_phase0_preview_mode = False
_phase0_preview_history = None





def load_ai_catalyst_data():
    """Indlæs lokal Marketaux-cache og indstillinger for denne programmappe."""
    data = {
        "schema": "PORTEFOLJE_MARKETAUX_CATALYST_V1",
        "update_frequency_days": DEFAULT_CATALYST_UPDATE_DAYS,
        "usage_date": today_key(),
        "requests_used": 0,
        "catalysts": {},
    }
    try:
        if CATALYST_FILE.exists():
            with CATALYST_FILE.open("r", encoding="utf-8") as f:
                loaded = json.load(f)
            if isinstance(loaded, dict):
                data.update({k: v for k, v in loaded.items() if k in data})
                catalysts = loaded.get("catalysts", {})
                if isinstance(catalysts, dict):
                    data["catalysts"] = catalysts
                try:
                    data["update_frequency_days"] = max(1, min(30, int(loaded.get("update_frequency_days", DEFAULT_CATALYST_UPDATE_DAYS))))
                except Exception:
                    data["update_frequency_days"] = DEFAULT_CATALYST_UPDATE_DAYS
                if str(data.get("usage_date", "")) != today_key():
                    data["usage_date"] = today_key()
                    data["requests_used"] = 0
    except Exception:
        pass
    return data


def save_ai_catalyst_data(data):
    try:
        clean = dict(data or {})
        clean["schema"] = "PORTEFOLJE_MARKETAUX_CATALYST_V1"
        clean.setdefault("update_frequency_days", DEFAULT_CATALYST_UPDATE_DAYS)
        clean.setdefault("usage_date", today_key())
        clean.setdefault("requests_used", 0)
        clean.setdefault("catalysts", {})
        with CATALYST_FILE.open("w", encoding="utf-8") as f:
            json.dump(clean, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


def _ai_catalyst_key(exchange, ticker):
    # Internt navn bevares for at minimere ændringer i resten af programmet.
    return f"{str(exchange or '').upper().strip()}:{str(ticker or '').upper().strip()}"


def _parse_iso_datetime(value):
    try:
        text = str(value or "").strip()
        if not text:
            return None
        return datetime.fromisoformat(text.replace("Z", "+00:00"))
    except Exception:
        return None


def _catalyst_age_days(result):
    if not isinstance(result, dict):
        return None
    dt = _parse_iso_datetime(result.get("updated_at"))
    if dt is None:
        try:
            d = date.fromisoformat(str(result.get("updated_date", ""))[:10])
            return max(0, (date.today() - d).days)
        except Exception:
            return None
    try:
        now = datetime.now(dt.tzinfo) if dt.tzinfo else datetime.now()
        return max(0, int((now - dt).total_seconds() // 86400))
    except Exception:
        return None


def _ai_catalyst_display(result):
    if not isinstance(result, dict):
        return "-", -999999.0
    importance = parse_float(result.get("importance"), None)
    category = str(result.get("category", "") or "").strip() or "Ingen"
    if importance is None:
        return "Fejl", -1.0
    importance = max(0.0, min(10.0, float(importance)))
    age = _catalyst_age_days(result)
    age_txt = f" +{age}d" if age and age > 0 else ""
    if importance <= 0.01:
        return "0 Ingen" + age_txt, 0.0
    return f"{importance:.1f} {category}".replace(".", ",") + age_txt, importance


def apply_ai_catalyst_cache_to_phase2_rows():
    """Vis seneste Marketaux-resultat, også hvis det er ældre end i dag."""
    data = load_ai_catalyst_data()
    catalysts = data.get("catalysts", {}) if isinstance(data.get("catalysts"), dict) else {}
    for row in phase2_rows:
        if row.get("is_summary") or is_cash_row(row):
            row["ai_catalyst"] = "-"
            row["sort_ai_catalyst"] = -999999.0
            continue
        key = _ai_catalyst_key(row.get("exchange"), row.get("ticker"))
        display, sort_value = _ai_catalyst_display(catalysts.get(key))
        row["ai_catalyst"] = display
        row["sort_ai_catalyst"] = sort_value


def _load_marketaux_token_file():
    """Læs gemt Marketaux-token fra programmappen."""
    try:
        if MARKETAUX_TOKEN_FILE.exists():
            return MARKETAUX_TOKEN_FILE.read_text(encoding="utf-8").strip()
    except Exception:
        pass
    return ""


def _save_marketaux_token_file(token):
    """Gem Marketaux-token i en separat fil i programmappen."""
    token = str(token or "").strip()
    if not token:
        return False
    try:
        MARKETAUX_TOKEN_FILE.write_text(token + "\n", encoding="utf-8")
        return True
    except Exception:
        return False


def _get_openai_api_key(prompt_if_missing=True, parent=None):
    """Kompatibilitetsnavn: returnerer nu Marketaux API-token."""
    global _marketaux_api_token_session
    env_key = str(os.environ.get("MARKETAUX_API_TOKEN", "") or os.environ.get("MARKETaux_API_TOKEN", "") or "").strip()
    if env_key:
        return env_key
    if _marketaux_api_token_session:
        return _marketaux_api_token_session

    file_key = _load_marketaux_token_file()
    if file_key:
        _marketaux_api_token_session = file_key
        return file_key

    if not prompt_if_missing:
        return ""
    value = simpledialog.askstring(
        "Marketaux API-token",
        "Indsæt dit Marketaux API-token.\n\n"
        "Tokenet gemmes i filen marketaux_api_token.txt i samme mappe som programmet, "
        "så det normalt kun skal indtastes én gang.",
        show="*",
        parent=parent or root,
    )
    value = str(value or "").strip()
    if value:
        _marketaux_api_token_session = value
        if not _save_marketaux_token_file(value):
            messagebox.showwarning(
                "Marketaux",
                "Tokenet virker i denne kørsel, men kunne ikke gemmes i programmappen.\n\n"
                "Kontrollér at programmet har skriverettighed til mappen.",
                parent=parent or root,
            )
    return value


def _marketaux_error_text(exc):
    try:
        body = exc.read().decode("utf-8", errors="ignore")
        payload = json.loads(body)
        if isinstance(payload, dict):
            for field in ("message", "error"):
                value = payload.get(field)
                if isinstance(value, str) and value.strip():
                    return value.strip()
                if isinstance(value, dict) and value.get("message"):
                    return str(value.get("message"))
        return body[:800] or str(exc)
    except Exception:
        return str(exc)


def _strip_html_tags(text):
    return re.sub(r"<[^>]+>", "", unescape(str(text or ""))).strip()


CATALYST_RULES = [
    ("M&A", 9.0, ("acquisition", "acquire", "merger", "takeover", "buyout", "strategic review")),
    ("Godkendelse", 9.0, ("fda approval", "approved by", "regulatory approval", "ema approval", "authorization", "clearance")),
    ("Guidance", 8.5, ("raises guidance", "raised guidance", "cuts guidance", "cut guidance", "guidance raised", "guidance cut", "profit warning", "outlook raised", "outlook cut")),
    ("Regnskab", 7.5, ("earnings", "quarterly results", "full-year results", "annual results", "revenue beat", "profit beat", "misses estimates", "beats estimates")),
    ("Kontrakt", 8.0, ("major contract", "contract award", "awarded contract", "order worth", "framework agreement", "large order")),
    ("Produkt", 7.0, ("product launch", "launches", "new product", "phase 3", "phase iii", "clinical trial", "trial results")),
    ("Kapital", 7.0, ("share buyback", "buyback", "dividend increase", "dividend cut", "capital raise", "rights issue", "offering")),
    ("Ledelse", 6.5, ("ceo resigns", "ceo steps down", "new ceo", "cfo resigns", "management change")),
    ("Retssag", 7.0, ("lawsuit", "litigation", "investigation", "antitrust", "fine", "settlement")),
]


def _marketaux_article_entity(article, ticker):
    ticker = str(ticker or "").upper().strip()
    entities = article.get("entities", []) if isinstance(article, dict) else []
    best = None
    for entity in entities or []:
        if not isinstance(entity, dict):
            continue
        if str(entity.get("symbol", "")).upper().strip() != ticker:
            continue
        if best is None or float(entity.get("match_score", 0) or 0) > float(best.get("match_score", 0) or 0):
            best = entity
    return best or {}


def _classify_marketaux_article(article, ticker):
    entity = _marketaux_article_entity(article, ticker)
    title = _strip_html_tags(article.get("title"))
    description = _strip_html_tags(article.get("description"))
    snippet = _strip_html_tags(article.get("snippet"))
    highlights = " ".join(_strip_html_tags(x.get("highlight")) for x in entity.get("highlights", []) if isinstance(x, dict))
    text = " ".join((title, description, snippet, highlights)).lower()

    category = "Nyhed"
    base = 4.0
    matched_terms = []
    for candidate_category, candidate_base, words in CATALYST_RULES:
        hits = [word for word in words if word in text]
        if hits and candidate_base > base:
            category = candidate_category
            base = candidate_base
            matched_terms = hits

    match_score = max(0.0, float(entity.get("match_score", 0) or 0))
    sentiment = max(-1.0, min(1.0, float(entity.get("sentiment_score", 0) or 0)))
    relevance_bonus = min(1.0, match_score / 100.0)
    sentiment_bonus = min(0.8, abs(sentiment) * 0.8)
    importance = max(0.0, min(10.0, base + relevance_bonus + sentiment_bonus))

    if sentiment > 0.12:
        direction = "positiv"
    elif sentiment < -0.12:
        direction = "negativ"
    else:
        direction = "neutral"

    published_at = str(article.get("published_at", "") or "")
    return {
        "importance": round(importance, 1),
        "category": category,
        "direction": direction,
        "headline": title or "Marketaux-nyhed",
        "summary": description or snippet or highlights or "Ingen beskrivelse returneret.",
        "why_it_matters": (
            f"Marketaux match-score {match_score:.1f} og sentiment {sentiment:+.2f}."
            + (f" Nøgleord: {', '.join(matched_terms[:3])}." if matched_terms else "")
        ),
        "time_horizon": "Ny/aktuel nyhed",
        "published_at": published_at,
        "match_score": match_score,
        "sentiment_score": sentiment,
        "source": str(article.get("source", "") or ""),
        "url": str(article.get("url", "") or ""),
    }


def fetch_ai_catalyst_batch(api_key, stocks, custom_prompt=None):
    """Kompatibilitetsnavn: ét Marketaux-kald pr. aktie. Returnerer én katalysatorpost."""
    if not stocks:
        return []
    item = stocks[0]
    ticker = str(item.get("ticker", "")).upper().strip()
    exchange = str(item.get("exchange", "")).upper().strip()
    name = str(item.get("name", ticker) or ticker)
    if not ticker:
        return []

    # Ved første opslag ser vi 7 dage tilbage. Senere opslag ser mindst tilbage til
    # sidste vellykkede opdatering, så vi ikke skaber huller mellem kørsler.
    data = load_ai_catalyst_data()
    old = data.get("catalysts", {}).get(_ai_catalyst_key(exchange, ticker), {})
    last_dt = _parse_iso_datetime(old.get("updated_at")) if isinstance(old, dict) else None
    if last_dt is None:
        from datetime import timedelta
        after_dt = datetime.now(timezone.utc) - timedelta(days=7)
    else:
        after_dt = last_dt.astimezone(timezone.utc) if last_dt.tzinfo else last_dt.replace(tzinfo=timezone.utc)

    params = {
        "api_token": api_key,
        "symbols": ticker,
        "filter_entities": "true",
        "language": "en",
        "limit": 3,
        "sort": "published_at",
        "published_after": after_dt.strftime("%Y-%m-%dT%H:%M"),
    }
    url = "https://api.marketaux.com/v1/news/all?" + urlencode(params)
    req = Request(url, headers={"User-Agent": "PortefoljeSimulator/7.14", "Accept": "application/json"})
    try:
        with urlopen(req, timeout=30) as resp:
            payload = json.loads(resp.read().decode("utf-8", errors="ignore"))
    except Exception as exc:
        raise RuntimeError(_marketaux_error_text(exc)) from exc

    articles = payload.get("data", []) if isinstance(payload, dict) else []
    scored = []
    for article in articles or []:
        if isinstance(article, dict):
            scored.append(_classify_marketaux_article(article, ticker))
    scored.sort(key=lambda x: (float(x.get("importance", 0) or 0), str(x.get("published_at", ""))), reverse=True)

    now_iso = datetime.now(timezone.utc).isoformat()
    if not scored:
        return [{
            "exchange": exchange, "ticker": ticker, "name": name,
            "importance": 0.0, "category": "Ingen", "direction": "neutral",
            "headline": "Ingen nye relevante Marketaux-nyheder i perioden.",
            "summary": "Marketaux returnerede ingen artikler for aktien siden sidste opslag.",
            "why_it_matters": "Ingen ny selskabsspecifik katalysator identificeret.",
            "time_horizon": "-", "sources": [], "articles": [],
            "updated_at": now_iso, "updated_date": today_key(), "provider": "Marketaux",
        }]

    best = scored[0]
    sources = []
    for row in scored:
        if row.get("url"):
            sources.append({"title": row.get("headline") or row.get("source") or "Kilde", "url": row.get("url"), "source": row.get("source", "")})
    return [{
        "exchange": exchange, "ticker": ticker, "name": name,
        "importance": best["importance"], "category": best["category"], "direction": best["direction"],
        "headline": best["headline"], "summary": best["summary"], "why_it_matters": best["why_it_matters"],
        "time_horizon": best["time_horizon"], "sources": sources[:3], "articles": scored[:3],
        "updated_at": now_iso, "updated_date": today_key(), "provider": "Marketaux",
    }]


def _phase2_stock_items_for_ai():
    return [dict(x) for x in portfolio if not is_cash_item(x)]


def _marketaux_due_stocks(stocks, data):
    catalysts = data.get("catalysts", {}) if isinstance(data.get("catalysts"), dict) else {}
    frequency = max(1, int(data.get("update_frequency_days", DEFAULT_CATALYST_UPDATE_DAYS) or 1))
    ranked = []
    for item in stocks:
        key = position_key(item)
        result = catalysts.get(key)
        age = _catalyst_age_days(result)
        if age is None:
            ranked.append((0, -999999, item))  # helt manglende først
        elif age >= frequency:
            ranked.append((1, -age, item))     # derefter ældste først
    ranked.sort(key=lambda x: (x[0], x[1], position_key(x[2])))
    return [x[2] for x in ranked]


def start_ai_catalyst_update():
    """Opdatér de manglende/for gamle aktier med Marketaux inden for dagens lokale kvote."""
    api_key = _get_openai_api_key(prompt_if_missing=True, parent=root)
    if not api_key:
        status_var.set("Katalysator: opdatering annulleret – intet Marketaux-token.")
        return
    stocks = _phase2_stock_items_for_ai()
    if not stocks:
        messagebox.showinfo("Katalysator", "Der er ingen aktier i porteføljen at opdatere.")
        return

    data = load_ai_catalyst_data()
    due = _marketaux_due_stocks(stocks, data)
    used = max(0, int(data.get("requests_used", 0) or 0))
    remaining = max(0, MARKETAUX_DAILY_LIMIT - used)
    if not due:
        status_var.set("Katalysator: alle aktier er friske nok efter den valgte opdateringsfrekvens.")
        apply_ai_catalyst_cache_to_phase2_rows()
        show_phase2()
        return
    if remaining <= 0:
        status_var.set("Katalysator: dagens lokale Marketaux-kvote på 100 kald er brugt. Fortsætter næste dag.")
        return

    queue = due[:remaining]
    try:
        ai_update_button.config(state="disabled")
    except Exception:
        pass
    status_var.set(f"Katalysator: Marketaux opdaterer {len(queue)} af {len(due)} aktier | {remaining} kald tilbage i dag.")

    def worker():
        try:
            cache = load_ai_catalyst_data()
            catalysts = cache.setdefault("catalysts", {})
            updated = 0
            errors = []
            quota_stopped = False
            for idx, item in enumerate(queue, start=1):
                key = position_key(item)
                root.after(0, lambda i=idx, n=len(queue), k=key: status_var.set(
                    f"Katalysator: Marketaux {i}/{n} – {k}..."
                ))
                try:
                    result_list = fetch_ai_catalyst_batch(api_key, [item], None)
                    # Et API-forsøg tælles lokalt som ét request, også ved tomt resultat.
                    cache["usage_date"] = today_key()
                    cache["requests_used"] = max(0, int(cache.get("requests_used", 0) or 0)) + 1
                    if result_list:
                        catalysts[key] = dict(result_list[0])
                        updated += 1
                    save_ai_catalyst_data(cache)
                except Exception as exc:
                    msg = str(exc)
                    # 429/quota/rate-limit: stop straks og gem det, vi allerede har.
                    if "429" in msg or "quota" in msg.lower() or "limit" in msg.lower() and "request" in msg.lower():
                        quota_stopped = True
                        cache["usage_date"] = today_key()
                        cache["requests_used"] = MARKETAUX_DAILY_LIMIT
                        save_ai_catalyst_data(cache)
                        break
                    errors.append(f"{key}: {msg}")
                    # Netværks-/symbolfejl bruger normalt også et request hos udbyderen.
                    cache["usage_date"] = today_key()
                    cache["requests_used"] = min(MARKETAUX_DAILY_LIMIT, max(0, int(cache.get("requests_used", 0) or 0)) + 1)
                    save_ai_catalyst_data(cache)

            def finish():
                apply_ai_catalyst_cache_to_phase2_rows()
                show_phase2()
                update_phase2_headers()
                left = max(0, MARKETAUX_DAILY_LIMIT - int(load_ai_catalyst_data().get("requests_used", 0) or 0))
                if quota_stopped:
                    status_var.set(f"Katalysator: Marketaux-kvoten er nået. {updated} opdateret; resten fortsætter næste dag.")
                elif errors:
                    status_var.set(f"Katalysator: {updated} opdateret, {len(errors)} fejl | ca. {left} lokale kald tilbage.")
                else:
                    status_var.set(f"Katalysator: {updated} aktier opdateret via Marketaux | ca. {left} lokale kald tilbage i dag.")
                try:
                    ai_update_button.config(state="normal")
                except Exception:
                    pass
                if errors:
                    messagebox.showwarning("Marketaux-katalysator", "Nogle opslag fejlede:\n\n" + "\n".join(errors[:10]))
            root.after(0, finish)
        except Exception as exc:
            msg = str(exc)
            def finish_error():
                try:
                    ai_update_button.config(state="normal")
                except Exception:
                    pass
                status_var.set("Katalysator: fejl under Marketaux-opdatering.")
                messagebox.showerror("Marketaux-katalysator", f"Opdateringen mislykkedes.\n\n{msg}")
            root.after(0, finish_error)

    threading.Thread(target=worker, daemon=True).start()


def _selected_phase2_ai_key():
    selected = phase2_tree.selection()
    if not selected:
        return "", ""
    item_id = selected[0]
    exchange = str(phase2_tree.set(item_id, "exchange") or "").upper().strip()
    ticker = str(phase2_tree.set(item_id, "ticker") or "").upper().strip()
    name = str(phase2_tree.set(item_id, "name") or ticker).strip()
    if not exchange or not ticker or exchange in ("-", CASH_EXCHANGE) or ticker in ("-", CASH_TICKER):
        return "", name
    return f"{exchange}:{ticker}", name


def open_ai_prompt_settings(parent=None):
    """Kompatibilitetsnavn: Marketaux-indstillinger (ingen AI-prompt længere)."""
    global _marketaux_api_token_session
    win = tk.Toplevel(parent or root)
    win.title("Indstil Marketaux-katalysator")
    win.geometry("620x330")
    win.minsize(560, 300)
    win.transient(parent or root)

    data = load_ai_catalyst_data()
    tk.Label(win, text="Marketaux-indstillinger", font=table_font, anchor="w").pack(fill="x", padx=14, pady=(14, 8))
    tk.Label(
        win,
        text="Hver programmappe har sin egen cache og opdateringsrytme. Marketaux-tokenet gemmes separat i marketaux_api_token.txt i programmappen.",
        font=small_font, anchor="w", justify="left", wraplength=570,
    ).pack(fill="x", padx=14, pady=(0, 12))

    row = tk.Frame(win)
    row.pack(fill="x", padx=14, pady=6)
    tk.Label(row, text="Opdateringsfrekvens (dage):", font=small_font, width=28, anchor="w").pack(side="left")
    frequency_var = tk.StringVar(value=str(data.get("update_frequency_days", DEFAULT_CATALYST_UPDATE_DAYS)))
    tk.Spinbox(row, from_=1, to=30, textvariable=frequency_var, width=8, font=small_font).pack(side="left")

    used = int(data.get("requests_used", 0) or 0)
    usage_var = tk.StringVar(value=f"Lokalt registreret i dag: {used}/{MARKETAUX_DAILY_LIMIT} Marketaux-kald")
    tk.Label(win, textvariable=usage_var, font=small_font, anchor="w").pack(fill="x", padx=14, pady=6)
    token_var = tk.StringVar(value=("Token: klar" if (_marketaux_api_token_session or os.environ.get("MARKETAUX_API_TOKEN") or _load_marketaux_token_file()) else "Token: ikke gemt endnu"))
    tk.Label(win, textvariable=token_var, font=small_font, anchor="w").pack(fill="x", padx=14, pady=6)

    buttons = tk.Frame(win)
    buttons.pack(fill="x", padx=14, pady=(18, 14))

    def set_token():
        token = _get_openai_api_key(prompt_if_missing=True, parent=win)
        if token:
            token_var.set("Token: klar og gemt")

    def save_settings():
        try:
            freq = int(str(frequency_var.get()).strip())
            if not 1 <= freq <= 30:
                raise ValueError
        except Exception:
            messagebox.showwarning("Marketaux", "Opdateringsfrekvens skal være et helt tal fra 1 til 30 dage.", parent=win)
            return
        current = load_ai_catalyst_data()
        current["update_frequency_days"] = freq
        save_ai_catalyst_data(current)
        win.destroy()

    tk.Button(buttons, text="Indtast API-token", font=small_font, command=set_token).pack(side="left")
    tk.Button(buttons, text="Annuller", font=small_font, command=win.destroy).pack(side="right")
    tk.Button(buttons, text="Gem", font=status_font, command=save_settings).pack(side="right", padx=(0, 8))


def show_selected_ai_catalyst_analysis():
    key, name = _selected_phase2_ai_key()
    if not key:
        messagebox.showinfo("Katalysator", "Markér først en aktie i Fase 2.")
        return
    data = load_ai_catalyst_data()
    result = data.get("catalysts", {}).get(key)
    if not isinstance(result, dict):
        messagebox.showinfo("Katalysator", f"Der findes endnu ingen Marketaux-data for {name}.\n\nTryk 'Opdater katalysatorer' først.")
        return

    win = tk.Toplevel(root)
    win.title(f"Katalysator – {name}")
    win.geometry("980x720")
    win.minsize(760, 540)
    win.transient(root)

    importance = parse_float(result.get("importance"), None)
    importance_text = format_num(importance, 1) if importance is not None else "-"
    header = tk.Frame(win)
    header.pack(fill="x", padx=14, pady=(14, 8))
    tk.Label(header, text=f"{name}  |  {key}", font=table_font, anchor="w").pack(side="left")
    tk.Label(header, text=f"Vigtighed {importance_text}/10  |  {result.get('category','-')}  |  {result.get('direction','-')}", font=status_font, anchor="e").pack(side="right")

    updated = str(result.get("updated_at") or result.get("updated_date") or "-")
    tk.Label(win, text=f"Marketaux-opdateret: {updated}  |  Fast, regelbaseret score i Python", font=small_font, anchor="w").pack(fill="x", padx=14, pady=(0, 10))

    body_frame = tk.Frame(win)
    body_frame.pack(fill="both", expand=True, padx=14, pady=(0, 10))
    body = tk.Text(body_frame, wrap="word", font=small_font)
    scroll = ttk.Scrollbar(body_frame, orient="vertical", command=body.yview)
    body.configure(yscrollcommand=scroll.set)
    body.pack(side="left", fill="both", expand=True)
    scroll.pack(side="right", fill="y")

    for title, value in [
        ("Katalysator", result.get("headline", "")),
        ("Nyhedsbeskrivelse", result.get("summary", "")),
        ("Programmets vurderingsgrundlag", result.get("why_it_matters", "")),
        ("Tidshorisont", result.get("time_horizon", "")),
    ]:
        body.insert("end", title + "\n", ("section",))
        body.insert("end", (str(value).strip() or "-") + "\n\n")

    articles = result.get("articles", []) if isinstance(result.get("articles"), list) else []
    if articles:
        body.insert("end", "Marketaux-data\n", ("section",))
        for i, article in enumerate(articles, 1):
            body.insert("end", f"{i}. {article.get('headline','-')}\n")
            body.insert("end", f"   Publiceret: {article.get('published_at','-')} | Match: {article.get('match_score',0):.1f} | Sentiment: {article.get('sentiment_score',0):+.2f}\n\n")

    body.insert("end", "Kilder\n", ("section",))
    sources = result.get("sources", []) if isinstance(result.get("sources"), list) else []
    if sources:
        for index, source in enumerate(sources, start=1):
            if isinstance(source, dict):
                body.insert("end", f"{index}. {source.get('title','Kilde')}\n{source.get('url','')}\n")
    else:
        body.insert("end", "-\n")
    body.tag_configure("section", font=tkfont.Font(family="Segoe UI", size=12, weight="bold"))
    body.configure(state="disabled")

    buttons = tk.Frame(win)
    buttons.pack(fill="x", padx=14, pady=(0, 14))
    tk.Button(buttons, text="Indstil Marketaux", font=small_font, command=lambda: open_ai_prompt_settings(win)).pack(side="left")
    tk.Button(buttons, text="Luk", font=status_font, command=win.destroy).pack(side="right")


def load_structure_settings():
    """Indlæs Market Cap-grænser, spekulationsstraf og senest valgte markedsprofil."""
    global market_cap_limits_usd, speculation_penalties, saved_structure_profile
    market_cap_limits_usd = [row[:] for row in DEFAULT_MARKET_CAP_LIMITS_USD]
    speculation_penalties = [row[:] for row in DEFAULT_SPECULATION_PENALTIES]
    saved_structure_profile = "Balanceret"
    try:
        if not STRUCTURE_SETTINGS_FILE.exists():
            return
        with STRUCTURE_SETTINGS_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            return

        limits = data.get("market_cap_limits_usd", [])
        clean_limits = []
        for row in limits:
            if not isinstance(row, (list, tuple)) or len(row) < 3:
                continue
            upper = None if row[0] is None else float(row[0])
            name = str(row[1])
            score = float(row[2])
            clean_limits.append([upper, name, score])
        finite = [row for row in clean_limits if row[0] is not None]
        terminal = [row for row in clean_limits if row[0] is None]
        finite.sort(key=lambda row: row[0])
        if len(finite) == 5 and len(terminal) == 1:
            loaded_limits = finite + [terminal[0]]
            old_scores = [0.0, 20.0, 40.0, 60.0, 80.0, 100.0]
            loaded_scores = [round(float(row[2]), 6) for row in loaded_limits]
            # Automatisk migrering fra v6.60-standard. Egne brugerdefinerede
            # scores bevares uændret.
            if loaded_scores == old_scores:
                market_cap_limits_usd = [row[:] for row in DEFAULT_MARKET_CAP_LIMITS_USD]
            else:
                market_cap_limits_usd = loaded_limits

        penalties = []
        for row in data.get("speculation_penalties", []):
            if isinstance(row, (list, tuple)) and len(row) >= 2:
                penalties.append([float(row[0]), max(0.0, float(row[1]))])
        penalties.sort(key=lambda row: row[0])
        if len(penalties) >= 2:
            speculation_penalties = penalties

        profile = str(data.get("structure_profile", "Balanceret"))
        if profile in STRUCTURE_PROFILES:
            saved_structure_profile = profile
    except Exception:
        market_cap_limits_usd = [row[:] for row in DEFAULT_MARKET_CAP_LIMITS_USD]
        speculation_penalties = [row[:] for row in DEFAULT_SPECULATION_PENALTIES]
        saved_structure_profile = "Balanceret"


def save_structure_settings():
    try:
        with STRUCTURE_SETTINGS_FILE.open("w", encoding="utf-8") as f:
            json.dump({
                "schema": "PORTEFOLJE_STRUCTURE_SETTINGS_V1",
                "structure_profile": saved_structure_profile,
                "market_cap_limits_usd": market_cap_limits_usd,
                "speculation_penalties": speculation_penalties,
            }, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


def speculation_penalty_from_bull(bull_pct):
    """Returnér en positiv scorestraf fra den højeste Bull-grænse, der overskrides."""
    bull = parse_float(bull_pct, None)
    if bull is None:
        return 0.0
    penalty = 0.0
    for threshold, points in sorted(speculation_penalties, key=lambda row: row[0]):
        if bull > threshold:
            penalty = max(0.0, float(points))
        else:
            break
    return penalty


def load_vix_settings():
    """Indlæs brugerens VIX-grænser og anbefalede kontantandele."""
    global vix_cash_levels
    vix_cash_levels = [row[:] for row in DEFAULT_VIX_CASH_LEVELS]
    try:
        if not VIX_SETTINGS_FILE.exists():
            return
        with VIX_SETTINGS_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
        rows_in = data.get("levels", []) if isinstance(data, dict) else []
        clean = []
        for row in rows_in:
            if not isinstance(row, (list, tuple)) or len(row) < 2:
                continue
            upper = None if row[0] is None else float(row[0])
            cash = float(row[1])
            clean.append([upper, cash])
        finite = [row for row in clean if row[0] is not None]
        terminal = [row for row in clean if row[0] is None]
        finite.sort(key=lambda row: row[0])
        if len(finite) == 8 and len(terminal) == 1:
            vix_cash_levels = finite + [terminal[0]]
    except Exception:
        vix_cash_levels = [row[:] for row in DEFAULT_VIX_CASH_LEVELS]


def save_vix_settings():
    try:
        with VIX_SETTINGS_FILE.open("w", encoding="utf-8") as f:
            json.dump({
                "schema": "PORTEFOLJE_VIX_CASH_SETTINGS_V1",
                "levels": vix_cash_levels,
            }, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


def recommended_cash_pct_for_vix(vix_value):
    value = parse_float(vix_value, None)
    if value is None:
        return None
    for upper, cash_pct in vix_cash_levels:
        if upper is None or value < upper:
            return float(cash_pct)
    return float(vix_cash_levels[-1][1])


def fetch_vix_value(tv):
    """Hent seneste VIX-luk fra TradingView."""
    candidates = [("CBOE", "VIX"), ("TVC", "VIX")]
    last_error = None
    for exchange, symbol in candidates:
        try:
            df = tv.get_hist(symbol=symbol, exchange=exchange, interval=Interval.in_daily, n_bars=10)
            if df is not None and not df.empty:
                df = df.dropna(subset=["close"])
                if not df.empty:
                    return float(df["close"].iloc[-1])
        except Exception as exc:
            last_error = exc
    if last_error:
        raise RuntimeError(str(last_error))
    raise RuntimeError("TradingView returnerede ingen VIX-data.")


def ensure_vix_for_today(force_refresh=False, tv=None):
    """Sørg for at dagens VIX findes i dags-cachen og i current_vix_value.

    Normal brug genbruger dagens cache. force_refresh=True henter altid en ny
    TradingView-værdi og overskriver dagens cache.
    """
    global current_vix_value
    cache = load_daily_cache()
    cache.setdefault("vix", {})
    cached = parse_float(cache.get("vix", {}).get("value"), None)
    cached_date = str(cache.get("vix", {}).get("date", "") or "")

    if not force_refresh and cached is not None and (not cached_date or cached_date == today_key()):
        current_vix_value = cached
        return current_vix_value, False

    if TvDatafeed is None:
        raise RuntimeError("Python-modulet tvDatafeed er ikke installeret.")
    own_tv = tv is None
    if own_tv:
        tv = TvDatafeed()
    value = fetch_vix_value(tv)
    current_vix_value = value
    cache["vix"] = {
        "value": value,
        "date": today_key(),
        "updated_at": datetime.now().isoformat(timespec="seconds"),
    }
    save_daily_cache(cache)
    return value, True


def ensure_vix_when_phase2_opened():
    """Ved aktivering af Fase 2: vis cache straks eller hent manglende VIX i baggrunden."""
    global current_vix_value, _vix_fetch_in_progress
    cache = load_daily_cache()
    cached = parse_float(cache.get("vix", {}).get("value"), None)
    if cached is not None:
        current_vix_value = cached
        update_vix_display()
        return
    if _vix_fetch_in_progress:
        return
    _vix_fetch_in_progress = True
    status_var.set("Fase 2: VIX mangler i dagens cache – henter fra TradingView...")

    def worker():
        try:
            value, _ = ensure_vix_for_today(force_refresh=False)
            def finish_ok():
                global _vix_fetch_in_progress
                _vix_fetch_in_progress = False
                update_vix_display()
                status_var.set(f"Fase 2: VIX {format_num(value, 2)} hentet og gemt i dagens cache.")
            root.after(0, finish_ok)
        except Exception as exc:
            msg = str(exc)
            def finish_error():
                global _vix_fetch_in_progress
                _vix_fetch_in_progress = False
                update_vix_display()
                status_var.set("Fase 2: VIX kunne ikke hentes – prøver igen ved næste aktivering/opdatering.")
            root.after(0, finish_error)

    threading.Thread(target=worker, daemon=True).start()


def portfolio_total_value_dkk():
    return sum(
        float(row.get("sort_value_dkk", 0.0) or 0.0)
        for row in phase2_rows
        if not row.get("is_summary")
    )


def current_cash_value_dkk():
    """Returnér den aktuelle kontantpost i DKK fra de viste Fase 2-rækker."""
    return sum(
        float(row.get("sort_value_dkk", 0.0) or 0.0)
        for row in phase2_rows
        if not row.get("is_summary") and is_cash_row(row)
    )


def update_vix_display():
    pct = recommended_cash_pct_for_vix(current_vix_value)
    total_value = portfolio_total_value_dkk()
    current_cash = current_cash_value_dkk()
    current_cash_pct = current_cash / total_value * 100.0 if total_value > 0 else None
    if "vix_value_var" in globals():
        vix_value_var.set(format_num(current_vix_value, 2) if current_vix_value is not None else "-")
    if "vix_cash_pct_var" in globals():
        vix_cash_pct_var.set((format_num(pct, 1) + " %") if pct is not None else "-")
    if "vix_cash_dkk_var" in globals():
        amount = total_value * pct / 100.0 if pct is not None and total_value > 0 else None
        vix_cash_dkk_var.set((format_dkk(amount) + " DKK") if amount is not None else "-")
    if "current_cash_pct_var" in globals():
        current_cash_pct_var.set((format_num(current_cash_pct, 1) + " %") if current_cash_pct is not None else "-")
    if "current_cash_dkk_var" in globals():
        current_cash_dkk_var.set((format_dkk(current_cash) + " DKK") if total_value > 0 else "-")


def open_vix_cash_settings():
    global vix_cash_levels
    win = tk.Toplevel(root)
    win.title("Indstil VIX og kontantbeholdning")
    win.geometry("620x560")
    win.minsize(560, 500)
    win.transient(root)

    tk.Label(
        win,
        text="Angiv den anbefalede kontantandel for hvert VIX-interval.",
        font=small_font, anchor="w",
    ).pack(fill="x", padx=12, pady=(12, 8))

    table = tk.Frame(win)
    table.pack(fill="both", expand=True, padx=12)
    tk.Label(table, text="VIX-interval", font=small_font, width=24, anchor="w").grid(row=0, column=0, padx=6, pady=5)
    tk.Label(table, text="Kontanter %", font=small_font).grid(row=0, column=1, padx=6, pady=5)

    entries = []
    previous = None
    for index, (upper, cash_pct) in enumerate(vix_cash_levels, start=1):
        if upper is None:
            interval_text = f"VIX ≥ {format_num(previous, 1)}"
        elif previous is None:
            interval_text = f"VIX < {format_num(upper, 1)}"
        else:
            interval_text = f"{format_num(previous, 1)} ≤ VIX < {format_num(upper, 1)}"
        tk.Label(table, text=interval_text, font=small_font, anchor="w").grid(row=index, column=0, padx=6, pady=4, sticky="w")
        var = tk.StringVar(value=format_num(cash_pct, 1))
        tk.Entry(table, textvariable=var, width=12, justify="center", font=small_font).grid(row=index, column=1, padx=6, pady=4)
        entries.append(var)
        if upper is not None:
            previous = upper

    def reset_entries():
        for var, (_upper, cash_pct) in zip(entries, DEFAULT_VIX_CASH_LEVELS):
            var.set(format_num(cash_pct, 1))

    def save_entries():
        global vix_cash_levels
        try:
            updated = []
            for var, (upper, _old_cash) in zip(entries, vix_cash_levels):
                cash = normalize_number(var.get(), None)
                if cash is None or not 0.0 <= cash <= 100.0:
                    raise ValueError("Alle kontantandele skal ligge mellem 0 og 100 %.")
                updated.append([upper, float(cash)])
            vix_cash_levels = updated
            save_vix_settings()
            update_vix_display()
            win.destroy()
        except Exception as exc:
            messagebox.showerror("Ugyldige indstillinger", str(exc), parent=win)

    buttons = tk.Frame(win)
    buttons.pack(fill="x", padx=12, pady=12)
    tk.Button(buttons, text="Reset til standard", font=small_font, command=reset_entries).pack(side="left")
    tk.Button(buttons, text="Annuller", font=small_font, command=win.destroy).pack(side="right")
    tk.Button(buttons, text="Gem", font=small_font, command=save_entries).pack(side="right", padx=(0, 8))


def load_stock_registry():
    """Indlæs permanent kartotek over alle aktier, der har været i programmet."""
    try:
        if STOCK_REGISTRY_FILE.exists():
            with STOCK_REGISTRY_FILE.open("r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, dict):
                data.setdefault("stocks", {})
                return data
    except Exception:
        pass
    # Første gang v6.40 startes, genbruges alle allerede kendte aktier fra
    # kursmålshistorikken, så tidligere solgte aktier ikke går tabt.
    migrated = {"schema": "PORTEFOLJE_STOCK_REGISTRY_V1", "stocks": {}}
    try:
        if TARGET_AGE_FILE.exists():
            with TARGET_AGE_FILE.open("r", encoding="utf-8") as f:
                history_data = json.load(f)
            for key, entry in history_data.get("positions", {}).items():
                if not isinstance(entry, dict) or ":" not in key:
                    continue
                exchange, ticker = key.split(":", 1)
                migrated["stocks"][key.upper()] = {
                    "exchange": exchange.upper(), "ticker": ticker.upper(),
                    "name": str(entry.get("name", ticker)).strip() or ticker,
                    "currency": currency_for_exchange(exchange), "active": False,
                    "first_seen_date": entry.get("observation_start_date", today_key()),
                    "last_seen_date": entry.get("last_change_date", today_key()),
                    "last_analyst_check_date": "",
                }
    except Exception:
        pass
    if migrated["stocks"]:
        save_stock_registry(migrated)
    return migrated


def save_stock_registry(data):
    try:
        data["schema"] = "PORTEFOLJE_STOCK_REGISTRY_V1"
        data.setdefault("stocks", {})
        with STOCK_REGISTRY_FILE.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


def remember_stock(item, active=True):
    """Gem aktiens stamdata permanent, også efter den forlader porteføljen."""
    if not item or is_cash_item(item):
        return
    exchange = str(item.get("exchange", "")).upper().strip()
    ticker = str(item.get("ticker", "")).upper().strip()
    if not exchange or not ticker:
        return
    key = f"{exchange}:{ticker}"
    data = load_stock_registry()
    stocks = data.setdefault("stocks", {})
    entry = stocks.get(key, {}) if isinstance(stocks.get(key), dict) else {}
    entry.update({
        "exchange": exchange,
        "ticker": ticker,
        "name": str(item.get("name", ticker)).strip() or ticker,
        "currency": currency_for_exchange(exchange),
        "active": bool(active),
        "last_seen_date": today_key(),
    })
    entry.setdefault("first_seen_date", today_key())
    entry.setdefault("last_analyst_check_date", "")
    stocks[key] = entry
    save_stock_registry(data)


def sync_stock_registry_with_portfolio():
    """Markér aktuelle positioner aktive uden at slette tidligere aktier."""
    data = load_stock_registry()
    stocks = data.setdefault("stocks", {})
    active_keys = {position_key(item) for item in portfolio if not is_cash_item(item)}
    for key, entry in stocks.items():
        if isinstance(entry, dict):
            entry["active"] = key in active_keys
    for item in portfolio:
        if is_cash_item(item):
            continue
        key = position_key(item)
        entry = stocks.get(key, {}) if isinstance(stocks.get(key), dict) else {}
        entry.update({
            "exchange": item["exchange"], "ticker": item["ticker"],
            "name": item.get("name", item["ticker"]),
            "currency": currency_for_exchange(item["exchange"]),
            "active": True, "last_seen_date": today_key(),
        })
        entry.setdefault("first_seen_date", today_key())
        entry.setdefault("last_analyst_check_date", "")
        stocks[key] = entry
    save_stock_registry(data)


def stock_registry_choices(include_active=False):
    data = load_stock_registry()
    choices = []
    active_keys = {position_key(item) for item in portfolio if not is_cash_item(item)}
    for key, entry in data.get("stocks", {}).items():
        if not isinstance(entry, dict):
            continue
        if not include_active and key in active_keys:
            continue
        name = str(entry.get("name", "")).strip() or key
        choices.append((f"{name} — {key}", key, entry))
    return sorted(choices, key=lambda x: (str(x[2].get("name", "")).casefold(), x[1].casefold()))

def load_value_settings():
    """Indlæs brugerens præmieknækpunkter og standardpåvirkning."""
    global value_score_points, value_influence
    value_score_points = [row[:] for row in DEFAULT_VALUE_SCORE_POINTS]
    value_influence = DEFAULT_VALUE_INFLUENCE
    try:
        if VALUE_SETTINGS_FILE.exists():
            with VALUE_SETTINGS_FILE.open("r", encoding="utf-8") as f:
                data = json.load(f)
            points = data.get("points", []) if isinstance(data, dict) else []
            clean = []
            for row in points:
                if isinstance(row, (list, tuple)) and len(row) >= 2:
                    premium = float(row[0])
                    score = float(row[1])
                    clean.append([premium, score])
            clean.sort(key=lambda x: x[0])
            if len(clean) >= 2:
                # Automatisk overgang fra v6.6-standard til den nye v6.7-standard.
                # Egne brugerdefinerede tabeller bevares uændret.
                if clean == OLD_DEFAULT_VALUE_SCORE_POINTS:
                    value_score_points = [row[:] for row in DEFAULT_VALUE_SCORE_POINTS]
                else:
                    value_score_points = clean
            if isinstance(data, dict):
                value_influence = max(0.0, min(1.0, float(data.get("influence", DEFAULT_VALUE_INFLUENCE))))
    except Exception:
        value_score_points = [row[:] for row in DEFAULT_VALUE_SCORE_POINTS]
        value_influence = DEFAULT_VALUE_INFLUENCE


def save_value_settings():
    try:
        with VALUE_SETTINGS_FILE.open("w", encoding="utf-8") as f:
            json.dump({
                "schema": "PORTEFOLJE_VALUE_SCORE_SETTINGS_V1",
                "influence": value_influence,
                "points": value_score_points,
            }, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


def value_score_from_premium(premium):
    """Lineær interpolation i den redigerbare præmie/Værdiscore-tabel."""
    p = parse_float(premium, None)
    if p is None or p <= 0:
        return 100.0
    points = sorted(value_score_points, key=lambda x: x[0])
    if not points:
        return 100.0
    if p <= points[0][0]:
        return max(0.0, min(100.0, points[0][1]))
    if p >= points[-1][0]:
        return max(0.0, min(100.0, points[-1][1]))
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        if x0 <= p <= x1:
            fraction = (p - x0) / (x1 - x0) if x1 != x0 else 0.0
            return max(0.0, min(100.0, y0 + fraction * (y1 - y0)))
    return 100.0


def load_allocation_settings():
    """Indlæs målfordelinger, mappings og påvirkning for regioner, sektorer og industrier."""
    global region_targets, sector_targets, country_map, sector_map, region_influence, sector_influence
    global industry_influence, target_influence, industry_default_target, industry_target_overrides
    global buy_window_max_factor, buy_window_above_bear_pct
    region_targets = dict(DEFAULT_REGION_TARGETS)
    sector_targets = dict(DEFAULT_SECTOR_TARGETS)
    country_map = dict(DEFAULT_COUNTRY_MAP)
    sector_map = dict(DEFAULT_SECTOR_MAP)
    region_influence = DEFAULT_ALLOCATION_INFLUENCE
    sector_influence = DEFAULT_ALLOCATION_INFLUENCE
    industry_influence = DEFAULT_INDUSTRY_INFLUENCE
    target_influence = DEFAULT_TARGET_INFLUENCE
    buy_window_max_factor = DEFAULT_BUY_WINDOW_MAX_FACTOR
    buy_window_above_bear_pct = DEFAULT_BUY_WINDOW_ABOVE_BEAR_PCT
    industry_default_target = DEFAULT_INDUSTRY_TARGET
    industry_target_overrides = {}
    try:
        if ALLOCATION_SETTINGS_FILE.exists():
            with ALLOCATION_SETTINGS_FILE.open("r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, dict):
                saved_sector_targets = data.get("sector_targets", {})

                def _matches_sector_defaults(defaults):
                    return (
                        isinstance(saved_sector_targets, dict)
                        and all(
                            category in saved_sector_targets
                            and abs(float(saved_sector_targets[category]) - defaults[category]) < 1e-9
                            for category in SECTOR_CATEGORIES
                        )
                    )

                migrate_old_sector_defaults = (
                    _matches_sector_defaults(OLD_DEFAULT_SECTOR_TARGETS)
                    or _matches_sector_defaults(PREVIOUS_DEFAULT_SECTOR_TARGETS)
                )
                for category in REGION_CATEGORIES:
                    if category in data.get("region_targets", {}):
                        region_targets[category] = max(0.0, float(data["region_targets"][category]))
                for category in SECTOR_CATEGORIES:
                    if not migrate_old_sector_defaults and category in saved_sector_targets:
                        sector_targets[category] = max(0.0, float(saved_sector_targets[category]))
                country_map.update({str(k): str(v) for k, v in data.get("country_map", {}).items() if str(v) in REGION_CATEGORIES})
                sector_map.update({str(k): str(v) for k, v in data.get("sector_map", {}).items() if str(v) in SECTOR_CATEGORIES})
                region_influence = clamp(float(data.get("region_influence", DEFAULT_ALLOCATION_INFLUENCE)), 0.0, 1.0)
                sector_influence = clamp(float(data.get("sector_influence", DEFAULT_ALLOCATION_INFLUENCE)), 0.0, 1.0)
                industry_influence = clamp(float(data.get("industry_influence", DEFAULT_INDUSTRY_INFLUENCE)), 0.0, 1.0)
                target_influence = clamp(float(data.get("target_influence", DEFAULT_TARGET_INFLUENCE)), 0.0, 1.0)
                buy_window_max_factor = clamp(float(data.get("buy_window_max_factor", DEFAULT_BUY_WINDOW_MAX_FACTOR)), 1.0, 10.0)
                buy_window_above_bear_pct = clamp(float(data.get("buy_window_above_bear_pct", DEFAULT_BUY_WINDOW_ABOVE_BEAR_PCT)), 0.0, 50.0)
                industry_default_target = clamp(float(data.get("industry_default_target", DEFAULT_INDUSTRY_TARGET)), 0.1, 25.0)
                industry_target_overrides = {str(k): clamp(float(v), 0.0, 25.0) for k, v in data.get("industry_target_overrides", {}).items()}
    except Exception:
        pass


def save_allocation_settings():
    try:
        with ALLOCATION_SETTINGS_FILE.open("w", encoding="utf-8") as f:
            json.dump({
                "schema": "PORTEFOLJE_REGION_SEKTOR_INDUSTRI_SETTINGS_V2",
                "region_influence": region_influence,
                "sector_influence": sector_influence,
                "industry_influence": industry_influence,
                "target_influence": target_influence,
                "buy_window_max_factor": buy_window_max_factor,
                "buy_window_above_bear_pct": buy_window_above_bear_pct,
                "industry_default_target": industry_default_target,
                "industry_target_overrides": industry_target_overrides,
                "region_targets": region_targets,
                "sector_targets": sector_targets,
                "country_map": country_map,
                "sector_map": sector_map,
            }, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


def mapped_region(country):
    raw = clean_category(country, "Land / region ukendt")
    if raw in country_map:
        return country_map[raw]
    unknown_country_values.add(raw)
    return "Andre lande"


def mapped_sector(sector):
    raw = clean_category(sector, "Sektor ukendt")
    if raw in sector_map:
        return sector_map[raw]
    unknown_sector_values.add(raw)
    return "Andre sektorer"


def allocation_balance_score(actual_pct, target_pct):
    """Retningsscore 80-120 ud fra afvigelsen i procentpoint fra målet."""
    actual = parse_float(actual_pct, 0.0) or 0.0
    target = parse_float(target_pct, 0.0) or 0.0
    return clamp(100.0 + 2.0 * (target - actual), 80.0, 120.0)


def normalized_industry(industry):
    """Bevar TradingViews konkrete industri. Manglende data får en særskilt neutral gruppe."""
    return clean_category(industry, "Industri ukendt")



def dynamic_industry_targets(data_rows):
    """Industrimål baseret direkte på de faste sektoranbefalinger.

    Hver sektor bruger præcis samme anbefalede %PF som Fase 3 / Sektorer.
    Sektorens mål deles ligeligt mellem de kendte industrier fra sektoren,
    som findes i den aktuelle portefølje. Der normaliseres ikke efter hvilke
    sektorer der er repræsenteret.

    Funktionen bruges af den flade 'Samlet'-visning, så dens industrimål er
    identiske med de samme industrirækker i 'Efter sektor'.
    """
    industries_by_sector = {}
    for row in data_rows:
        if row.get("is_summary") or is_cash_row(row):
            continue
        industry = row.get("industry_group") or normalized_industry(row.get("industry"))
        if industry == "Industri ukendt":
            continue
        sector = row.get("sector_group") or mapped_sector(row.get("sector"))
        industries_by_sector.setdefault(sector, set()).add(industry)

    targets = {}
    for sector, industries_set in industries_by_sector.items():
        industries = sorted(industries_set)
        if not industries:
            continue

        sector_target = max(
            0.0,
            parse_float(sector_targets.get(sector, 0.0), 0.0) or 0.0,
        )

        # Samme synlige 1-decimalsfordeling som i "Efter sektor":
        # lige fordeling, med evt. afrundingsrest på sidste industri.
        raw_per_industry = sector_target / len(industries)
        remaining = sector_target
        for idx, industry in enumerate(industries):
            if idx == len(industries) - 1:
                target_value = remaining
            else:
                target_value = round(raw_per_industry, 1)
                remaining -= target_value
            targets[industry] = targets.get(industry, 0.0) + target_value

    return targets

def industry_target_for(industry, dynamic_targets=None):
    name = normalized_industry(industry)
    if name == "Industri ukendt":
        return 0.0
    if dynamic_targets is not None:
        return parse_float(dynamic_targets.get(name), 0.0) or 0.0
    # Bagudkompatibel fallback til steder, der ikke har en aktuel portefølje-kontekst.
    return industry_target_overrides.get(name, industry_default_target)



def industry_balance_score(actual_pct, target_pct, industry_name):
    """Neutral industriscore: ingen bonus under målet, kun moderat koncentrationsdæmpning."""
    if normalized_industry(industry_name) == "Industri ukendt":
        return 100.0
    actual = parse_float(actual_pct, 0.0) or 0.0
    target = parse_float(target_pct, 0.0) or 0.0
    if target <= 0.0 or actual <= target:
        return 100.0
    return clamp(100.0 - 2.0 * (actual - target), 80.0, 100.0)



def today_key():
    return date.today().isoformat()


def position_key(item):
    return f"{str(item.get('exchange', '')).upper().strip()}:{str(item.get('ticker', '')).upper().strip()}"

def load_buy_window_memory():
    try:
        if BUY_WINDOW_MEMORY_FILE.exists():
            with BUY_WINDOW_MEMORY_FILE.open("r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, dict):
                data.setdefault("positions", {})
                return data
    except Exception:
        pass
    return {"schema": "PORTEFOLJE_BUY_WINDOW_MEMORY_V1", "positions": {}}


def save_buy_window_memory(data):
    try:
        data["schema"] = "PORTEFOLJE_BUY_WINDOW_MEMORY_V1"
        data.setdefault("positions", {})
        with BUY_WINDOW_MEMORY_FILE.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception:
        pass



def register_buy_window_event(row, previous_shares, new_shares, actual_weight):
    """Gem et faktisk køb i aktivt købsvindue som særskilt historikbegivenhed.

    Begivenheden ligger separat fra kursmålshistorikkens målposter og påvirker
    derfor hverken KM-alder eller 2 %-støjfilteret. Der gemmes samtidig de
    aktuelle kursmål og potentialer, så årsagen kan genfindes senere.
    """
    try:
        previous_shares = float(previous_shares)
        new_shares = float(new_shares)
        if new_shares <= previous_shares + 1e-9:
            return

        key = f"{str(row.get('exchange', '')).upper()}:{str(row.get('ticker', '')).upper()}"
        if key == ":":
            return

        data = load_target_age_history()
        positions = data.setdefault("positions", {})
        entry = positions.get(key)
        if not isinstance(entry, dict):
            entry = {
                "exchange": str(row.get("exchange", "")).upper(),
                "ticker": str(row.get("ticker", "")).upper(),
                "name": str(row.get("name", "")),
                "observation_start_date": today_key(),
                "last_change_date": today_key(),
                "change_date_known": False,
                "targets": {},
                "history": [],
                "earnings_events": [],
                "buy_window_events": [],
                "trade_events": [],
                "next_earnings_date": None,
            }
            positions[key] = entry

        entry["name"] = str(row.get("name", entry.get("name", "")))
        events = entry.setdefault("buy_window_events", [])

        event = {
            "date": today_key(),
            "type": "buy_window_purchase",
            "previous_shares": previous_shares,
            "new_shares": new_shares,
            "shares_bought": new_shares - previous_shares,
            "weight_pct": float(actual_weight),
            "price": parse_float(row.get("sort_price"), None),
            "bull_target": parse_float(row.get("bull_target_abs"), None),
            "base_target": parse_float(row.get("base_target_abs"), None),
            "bear_target": parse_float(row.get("bear_target_abs"), None),
            "bull_pct": parse_float(row.get("analyst_bull_pct"), None),
            "base_pct": parse_float(row.get("analyst_base_pct"), None),
            "bear_pct": parse_float(row.get("analyst_bear_pct"), None),
            "normal_recommended_weight_pct": parse_float(row.get("normal_recommended_weight_raw"), None),
            "buy_window_recommended_weight_pct": parse_float(row.get("sort_recommended_weight"), None),
            "buy_window_factor": parse_float(row.get("target_factor_raw"), None),
        }

        # Samme observerede køb må ikke kunne registreres igen ved gentagen
        # genberegning samme dag.
        duplicate = any(
            isinstance(old, dict)
            and str(old.get("date", "")) == event["date"]
            and abs(float(old.get("previous_shares", -1) or -1) - previous_shares) < 1e-9
            and abs(float(old.get("new_shares", -1) or -1) - new_shares) < 1e-9
            for old in events
        )
        if not duplicate:
            events.append(event)
            events.sort(key=lambda e: (
                str(e.get("date", "")),
                float(e.get("new_shares", 0.0) or 0.0),
            ))
            save_target_age_history(data)
    except Exception:
        # Historikregistrering må aldrig blokere den normale porteføljeberegning.
        pass


def update_buy_window_memory(rows):
    """Husk kun faktisk opbyggede positioner under et aktivt købsvindue.

    Første observation etablerer kun et antal-referencepunkt. En permanent
    godkendelse opstår først, når antal aktier senere stiger, mens købsvinduet
    er åbent. Kursstigning alene lukker vinduet, men sletter ikke godkendelsen.
    Godkendelsen bortfalder ved programmets Sælg-signal eller hvis Bull- eller
    Bear-kursmålet er faldet mindst 20 % siden det senest godkendte køb.
    """
    data = load_buy_window_memory()
    positions = data.setdefault("positions", {})
    changed = False
    active_keys = set()

    for row in rows:
        if row.get("is_summary") or is_cash_row(row):
            continue
        key = f"{str(row.get('exchange','')).upper()}:{str(row.get('ticker','')).upper()}"
        active_keys.add(key)
        shares = max(0.0, float(row.get("sort_antal", 0.0) or 0.0))
        actual_weight = max(0.0, float(row.get("sort_weight", 0.0) or 0.0))
        bull = parse_float(row.get("bull_target_abs"), None)
        bear = parse_float(row.get("bear_target_abs"), None)
        entry = positions.get(key)

        if not isinstance(entry, dict):
            positions[key] = {
                "observed_shares": shares,
                "approved_shares": 0.0,
                "approved_weight_pct": None,
                "approved_date": None,
                "approved_bull_target": None,
                "approved_bear_target": None,
            }
            row["approved_buy_weight"] = "-"
            row["sort_approved_buy_weight"] = -999999
            changed = True
            continue

        previous_shares = max(0.0, float(entry.get("observed_shares", shares) or 0.0))
        approved_weight = parse_float(entry.get("approved_weight_pct"), None)
        approved_bull = parse_float(entry.get("approved_bull_target"), None)
        approved_bear = parse_float(entry.get("approved_bear_target"), None)

        deterioration = False
        if approved_weight is not None:
            if approved_bull and bull and bull <= 0.80 * approved_bull:
                deterioration = True
            if approved_bear and bear and bear <= 0.80 * approved_bear:
                deterioration = True

        if row.get("upside_sell") or deterioration:
            for field, value in (
                ("approved_shares", 0.0), ("approved_weight_pct", None),
                ("approved_date", None), ("approved_bull_target", None),
                ("approved_bear_target", None),
            ):
                if entry.get(field) != value:
                    entry[field] = value
                    changed = True
            approved_weight = None

        elif shares > previous_shares + 1e-9 and row.get("buy_opportunity"):
            # Først her ved et faktisk højere aktieantal opstår både den
            # permanente godkendelse og en særskilt historikbegivenhed.
            register_buy_window_event(row, previous_shares, shares, actual_weight)
            entry["approved_shares"] = shares
            entry["approved_weight_pct"] = actual_weight
            entry["approved_date"] = today_key()
            entry["approved_bull_target"] = bull
            entry["approved_bear_target"] = bear
            approved_weight = actual_weight
            changed = True

        elif shares < previous_shares - 1e-9 and approved_weight is not None:
            approved_shares = max(0.0, float(entry.get("approved_shares", 0.0) or 0.0))
            if shares <= 0:
                entry["approved_shares"] = 0.0
                entry["approved_weight_pct"] = None
                entry["approved_date"] = None
                entry["approved_bull_target"] = None
                entry["approved_bear_target"] = None
                approved_weight = None
            elif approved_shares > 0 and shares < approved_shares:
                entry["approved_shares"] = shares
                entry["approved_weight_pct"] = min(approved_weight, actual_weight)
                approved_weight = entry["approved_weight_pct"]
            changed = True

        if entry.get("observed_shares") != shares:
            entry["observed_shares"] = shares
            changed = True

        row["approved_buy_weight"] = (format_pct(approved_weight).replace("+", "") if approved_weight is not None else "-")
        row["sort_approved_buy_weight"] = approved_weight if approved_weight is not None else -999999

    if changed:
        save_buy_window_memory(data)



def load_daily_cache():
    """Indlæs seneste tilgængelige dags-cache, også når den er ældre end i dag.

    Webversionen må gerne bygge en portefølje på senest uploadede data.
    Cache-datoen bevares som metadata og bruges ikke længere som et krav for,
    at phase1/phase2/fx-data kan anvendes.
    """
    try:
        if DAILY_CACHE_FILE.exists():
            with DAILY_CACHE_FILE.open("r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, dict):
                data.setdefault("schema", "PORTEFOLJE_SIMULATOR_DAILY_CACHE_V1")
                data.setdefault("date", "")
                data.setdefault("fx_rates", {})
                data.setdefault("phase1", {})
                data.setdefault("phase2", {})
                data.setdefault("vix", {})
                return data
    except Exception:
        pass
    return {"schema": "PORTEFOLJE_SIMULATOR_DAILY_CACHE_V1", "date": "", "fx_rates": {}, "phase1": {}, "phase2": {}, "vix": {}}


def save_daily_cache(cache):
    try:
        cache["date"] = today_key()
        cache.setdefault("schema", "PORTEFOLJE_SIMULATOR_DAILY_CACHE_V1")
        cache.setdefault("fx_rates", {})
        cache.setdefault("phase1", {})
        cache.setdefault("phase2", {})
        cache.setdefault("vix", {})
        with DAILY_CACHE_FILE.open("w", encoding="utf-8") as f:
            json.dump(cache, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


def value_is_missing(value):
    if value is None:
        return True
    if isinstance(value, str) and value.strip() in ("", "-"):
        return True
    return False


def has_required_fields(data, fields):
    if not isinstance(data, dict):
        return False
    return all(field in data and not value_is_missing(data.get(field)) for field in fields)


def cache_raw_from_item(item, cached_row, fx_rates):
    try:
        price = float(cached_row["price_raw"])
    except Exception:
        return None
    antal = float(item.get("antal", 0.0) or 0.0)
    currency = currency_for_exchange(item["exchange"])
    fx_to_dkk = float(fx_rates.get(currency, cached_row.get("fx_to_dkk", 1.0)) or 1.0)
    out = dict(cached_row)
    out.update({
        "exchange": item["exchange"],
        "ticker": item["ticker"],
        "name": item["name"],
        "antal_raw": antal,
        "currency": currency,
        "fx_to_dkk": fx_to_dkk,
        "usd_to_dkk": float(fx_rates.get("USD", cached_row.get("usd_to_dkk", FALLBACK_FX_DKK["USD"])) or FALLBACK_FX_DKK["USD"]),
        "value_native_raw": price * antal,
        "value_raw": price * antal * fx_to_dkk,
    })
    return out


def normalize_phase2_cache(data):
    if not isinstance(data, dict):
        return {}
    return {k: v for k, v in data.items() if not value_is_missing(v)}


def normalize_number(value, fallback=0.0, prefer_decimal=False):
    """Robust talfortolkning til JSON, dansk indtastning og importfiler.

    ``prefer_decimal=True`` bruges til maskin-genererede eksportfelter som
    Saxo XLSX/CSV, hvor et enkelt punktum er et decimaltegn. Dermed læses fx
    167.394 som 167,394 i stedet for 167.394 (et hundrede syvogtres tusind).

    Standardadfærden bevares til manuel dansk indtastning, hvor 1.234 normalt
    betyder tusind to hundrede og fireogtredive.
    """
    try:
        if value is None:
            return fallback

        # JSON-/Excel-tal skal bruges direkte og må ikke tekst-normaliseres.
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return float(value)

        text = str(value).strip().replace(" ", "").replace(" ", "")
        if text == "":
            return fallback

        has_comma = "," in text
        has_dot = "." in text

        if has_comma and has_dot:
            # Sidste separator antages at være decimaltegn.
            # Dansk: 1.234,56 -> 1234.56
            # Engelsk: 1,234.56 -> 1234.56
            if text.rfind(",") > text.rfind("."):
                text = text.replace(".", "").replace(",", ".")
            else:
                text = text.replace(",", "")
        elif has_comma:
            # Et enkelt komma er decimaltegn. Flere kommaer er tusindtalsdeling.
            parts = text.split(",")
            if len(parts) > 2:
                text = "".join(parts)
            else:
                text = text.replace(",", ".")
        elif has_dot:
            parts = text.split(".")
            if len(parts) > 2:
                # 1.234.567 er tusindtalsformat. I eksportdata forekommer
                # decimaltal normalt kun med ét decimalpunktum.
                text = "".join(parts)
            elif (
                not prefer_decimal
                and len(parts) == 2
                and len(parts[1]) == 3
                and parts[0].lstrip("+-").isdigit()
                and parts[1].isdigit()
            ):
                # Manuel dansk indtastning: 1.234 -> 1234.
                text = "".join(parts)
            # Med prefer_decimal=True bevares 41.759, 167.394 osv.

        return float(text)
    except Exception:
        return fallback


def normalize_item(item):
    exchange = str(item.get("exchange", item.get("børs", item.get("bors", "")))).strip().upper()
    ticker = str(item.get("ticker", "")).strip().upper()
    name = str(item.get("name", item.get("navn", ""))).strip()
    antal = normalize_number(item.get("antal", item.get("shares", item.get("amount", 0))), 0.0)
    gak = normalize_number(item.get("gak", item.get("GAK", item.get("average_price", item.get("avg_price", 0)))), 0.0)
    if not name:
        name = ticker
    out = {"exchange": exchange, "ticker": ticker, "name": name, "antal": antal}
    if gak > 0:
        out["gak"] = gak

    # Bevar fase 4-data ved hver indlæsning/gemning. Tidligere blev ukendte felter
    # fjernet af normaliseringen, hvilket ville slette Nordnet-data igen.
    nordnet = item.get("nordnet")
    if isinstance(nordnet, dict):
        out["nordnet"] = dict(nordnet)
    saxo = item.get("saxo")
    if isinstance(saxo, dict):
        out["saxo"] = dict(saxo)
    history = item.get("position_history")
    if isinstance(history, list):
        out["position_history"] = [dict(x) for x in history if isinstance(x, dict)]
    return out


def is_cash_item(item):
    return (
        str((item or {}).get("exchange", "")).strip().upper() == CASH_EXCHANGE
        and str((item or {}).get("ticker", "")).strip().upper() == CASH_TICKER
    )


def is_cash_row(row):
    return bool((row or {}).get("is_cash")) or (
        str((row or {}).get("exchange", "")).strip().upper() == CASH_EXCHANGE
        and str((row or {}).get("ticker", "")).strip().upper() == CASH_TICKER
    )


def ensure_cash_position(data):
    """Sørg for præcis én kontantpost, som redigeres via Antal-feltet i DKK."""
    clean = []
    cash_amount = 0.0
    found = False
    for item in data or []:
        if is_cash_item(item):
            if not found:
                cash_amount = max(0.0, normalize_number(item.get("antal", 0), 0.0))
                found = True
            continue
        clean.append(item)
    clean.append({
        "exchange": CASH_EXCHANGE,
        "ticker": CASH_TICKER,
        "name": CASH_NAME,
        "antal": cash_amount,
    })
    return clean


def make_cash_raw(item):
    amount = max(0.0, normalize_number((item or {}).get("antal", 0), 0.0))
    out = {
        "exchange": CASH_EXCHANGE,
        "ticker": CASH_TICKER,
        "name": CASH_NAME,
        "antal_raw": amount,
        "price_raw": 1.0,
        "sma50_raw": None,
        "trend_strength_raw": None,
        "robustness_raw": None,
        "history_days_raw": None,
        "currency": "DKK",
        "fx_to_dkk": 1.0,
        "usd_to_dkk": FALLBACK_FX_DKK["USD"],
        "value_native_raw": amount,
        "value_raw": amount,
        "data_date": today_key(),
        "is_cash": True,
    }
    for key, _title, _bars in PERIODS:
        out[key + "_raw"] = None
    return out


def load_portfolio_from_file(path):
    with Path(path).open("r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, dict) and "positions" in data:
        data = data["positions"]
    if not isinstance(data, list):
        raise ValueError("JSON skal være en liste af positioner eller et objekt med feltet 'positions'.")
    clean = [normalize_item(x) for x in data]
    clean = [x for x in clean if x["exchange"] and x["ticker"]]
    clean = ensure_cash_position(clean)
    if not [x for x in clean if not is_cash_item(x)]:
        raise ValueError("Filen indeholder ingen gyldige aktiepositioner med børs og ticker.")
    return clean


def save_phase2_portfolio_snapshot(data=None):
    """Gem den senest byggede porteføljesammensætning i et enkelt flytbart JSON-format."""
    if data is None:
        data = portfolio
    clean = []
    for item in data or []:
        normalized = normalize_item(item)
        if not normalized.get("exchange") or not normalized.get("ticker"):
            continue
        clean.append({
            "exchange": normalized["exchange"],
            "ticker": normalized["ticker"],
            "name": normalized.get("name", normalized["ticker"]),
            "antal": normalized.get("antal", 0),
        })
    clean = ensure_cash_position(clean)
    PHASE2_PORTFOLIO_FILE.write_text(json.dumps(clean, ensure_ascii=False, indent=2), encoding="utf-8")
    return clean


def load_saved_built_portfolio():
    """Indlæs senest byggede portefølje. Fase 2-filen har første prioritet."""
    for path in (PHASE2_PORTFOLIO_FILE, BUILT_PORTFOLIO_FILE):
        try:
            if path.exists():
                return load_portfolio_from_file(path)
        except Exception:
            continue
    return None


def sync_phase2_to_saved_built_portfolio(show_errors=False):
    """Sørg for at Fase 2/øvrige visninger bruger den senest gemte byggede portefølje."""
    global portfolio
    saved = load_saved_built_portfolio()
    if not saved:
        return False
    try:
        portfolio = ensure_cash_position(saved)
        refresh_built_portfolio_from_cache()
        return True
    except Exception as exc:
        if show_errors:
            messagebox.showwarning(
                "Bygget portefølje",
                "Den gemte porteføljesammensætning blev fundet, men visningerne kunne ikke "
                f"genopbygges fra den aktuelle Fase 0-cache.\n\n{exc}",
            )
        return False


def _trade_snapshot_for_key(key):
    """Find seneste kendte kurs og Bull/Base/Bear til en handelsbegivenhed."""
    try:
        data = load_target_age_history()
        entry = data.get("positions", {}).get(str(key or "").upper(), {})
        if isinstance(entry, dict):
            snapshot = entry.get("current_snapshot")
            if isinstance(snapshot, dict) and _history_point_complete(snapshot):
                return dict(snapshot)
            complete = _complete_history_entries(entry.get("history", []))
            if complete:
                return dict(complete[-1])
    except Exception:
        pass

    # Fallback til den aktuelle Fase 2-række, hvis historikfilen endnu ikke har
    # et komplet snapshot. Det er især nyttigt ved en handel umiddelbart efter
    # programstart, før næste dataopdatering er gennemført.
    try:
        for row in phase2_rows:
            row_key = f"{str(row.get('exchange','')).upper()}:{str(row.get('ticker','')).upper()}"
            if row_key == str(key or "").upper() and not row.get("is_summary") and not is_cash_row(row):
                return {
                    "date": today_key(),
                    "price": parse_float(row.get("sort_price"), None),
                    "bull_target": parse_float(row.get("bull_target_abs"), None),
                    "base_target": parse_float(row.get("base_target_abs"), None),
                    "median_target": parse_float(row.get("median_target_abs"), None),
                    "bear_target": parse_float(row.get("bear_target_abs"), None),
                }
    except Exception:
        pass
    return {}


def register_portfolio_trade_events(previous_data, new_data):
    """Registrér alle reelle ændringer i aktieantal som Køb eller Salg.

    Begivenhederne gemmes separat fra kursmålshistorikken og påvirker derfor
    hverken KM-alder eller 2 %-støjfilteret. Et senere købsvindue-event kan
    genkende samme antalændring; visningen prioriterer da "Køb i købsvindue"
    frem for at vise det samme køb to gange.
    """
    try:
        previous_map = {
            position_key(item): item for item in (previous_data or [])
            if not is_cash_item(item) and position_key(item) != ":"
        }
        new_map = {
            position_key(item): item for item in (new_data or [])
            if not is_cash_item(item) and position_key(item) != ":"
        }
        keys = set(previous_map) | set(new_map)
        if not keys:
            return

        data = load_target_age_history()
        positions = data.setdefault("positions", {})
        changed = False

        for key in sorted(keys):
            old_item = previous_map.get(key, {})
            new_item = new_map.get(key, {})
            old_shares = max(0.0, normalize_number(old_item.get("antal", 0.0), 0.0))
            new_shares = max(0.0, normalize_number(new_item.get("antal", 0.0), 0.0))
            if abs(new_shares - old_shares) <= 1e-9:
                continue

            item = new_item or old_item
            entry = positions.get(key)
            if not isinstance(entry, dict):
                entry = {
                    "exchange": str(item.get("exchange", "")).upper(),
                    "ticker": str(item.get("ticker", "")).upper(),
                    "name": str(item.get("name", item.get("ticker", ""))),
                    "observation_start_date": today_key(),
                    "last_change_date": today_key(),
                    "change_date_known": False,
                    "targets": {},
                    "history": [],
                    "earnings_events": [],
                    "buy_window_events": [],
                    "trade_events": [],
                    "next_earnings_date": None,
                }
                positions[key] = entry

            entry["name"] = str(item.get("name", entry.get("name", "")))
            events = entry.setdefault("trade_events", [])
            event_type = "buy" if new_shares > old_shares else "sell"
            snapshot = _trade_snapshot_for_key(key)
            price = parse_float(snapshot.get("price"), None)
            bull_target = parse_float(snapshot.get("bull_target"), None)
            base_target = parse_float(snapshot.get("base_target"), None)
            bear_target = parse_float(snapshot.get("bear_target"), None)

            def upside(target):
                if price is None or price <= 0 or target is None or target <= 0:
                    return None
                return (target / price - 1.0) * 100.0

            event = {
                "date": today_key(),
                "type": event_type,
                "previous_shares": old_shares,
                "new_shares": new_shares,
                "shares_changed": abs(new_shares - old_shares),
                "price": price,
                "bull_target": bull_target,
                "base_target": base_target,
                "bear_target": bear_target,
                "bull_pct": upside(bull_target),
                "base_pct": upside(base_target),
                "bear_pct": upside(bear_target),
            }
            duplicate = any(
                isinstance(old, dict)
                and str(old.get("date", "")) == event["date"]
                and str(old.get("type", "")) == event_type
                and abs(float(old.get("previous_shares", -1) or -1) - old_shares) < 1e-9
                and abs(float(old.get("new_shares", -1) or -1) - new_shares) < 1e-9
                for old in events
            )
            if not duplicate:
                events.append(event)
                events.sort(key=lambda e: (
                    str(e.get("date", "")),
                    str(e.get("type", "")),
                    float(e.get("new_shares", 0.0) or 0.0),
                ))
                changed = True

        if changed:
            save_target_age_history(data)
    except Exception:
        # Handelslog må aldrig blokere almindelig lagring af porteføljen.
        pass


def save_portfolio(data=None):
    if data is None:
        data = portfolio
    clean = [normalize_item(x) for x in data if normalize_item(x)["exchange"] and normalize_item(x)["ticker"]]
    clean = ensure_cash_position(clean)

    # Sammenlign med den senest gemte portefølje, før filen overskrives.
    # Dermed registreres både manuel redigering, import og andre reelle
    # antalændringer ensartet. Første oprettelse af filen skaber ingen falske køb.
    previous_saved = None
    if DEFAULT_PORTFOLIO_FILE.exists():
        try:
            previous_saved = load_portfolio_from_file(DEFAULT_PORTFOLIO_FILE)
        except Exception:
            previous_saved = None
    if previous_saved is not None:
        register_portfolio_trade_events(previous_saved, clean)

    with DEFAULT_PORTFOLIO_FILE.open("w", encoding="utf-8") as f:
        json.dump(clean, f, ensure_ascii=False, indent=2)
    # Aktier slettes aldrig fra kartoteket; deres aktive status opdateres blot.
    try:
        sync_stock_registry_with_portfolio()
    except Exception:
        pass


def load_default_portfolio():
    if DEFAULT_PORTFOLIO_FILE.exists():
        try:
            data = load_portfolio_from_file(DEFAULT_PORTFOLIO_FILE)
            save_portfolio(data)
            return data
        except Exception as e:
            messagebox.showwarning("Porteføljefil kunne ikke læses", f"Bruger standardportefølje.\n\nFejl:\n{e}")
    default_data = ensure_cash_position([normalize_item(x) for x in DEFAULT_PORTFOLIO])
    save_portfolio(default_data)
    return default_data


def format_num(value, decimals=2):
    try:
        if value is None or pd.isna(value):
            return "-"
        return f"{float(value):,.{decimals}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except Exception:
        return "-"


def format_antal(value):
    try:
        value = float(value)
        if abs(value - round(value)) < 0.000001:
            return f"{int(round(value)):,}".replace(",", ".")
        return format_num(value, 4)
    except Exception:
        return "-"


def format_dkk(value):
    try:
        if value is None or pd.isna(value):
            return "-"
        return f"{float(value):,.0f}".replace(",", ".")
    except Exception:
        return "-"


def currency_for_exchange(exchange):
    return EXCHANGE_CURRENCY.get(str(exchange or "").strip().upper(), "DKK")


def fetch_fx_rates(tv, needed_currencies):
    rates = {"DKK": 1.0}
    used_fallback = []
    for currency in sorted(set(needed_currencies)):
        if currency == "DKK":
            continue
        fx_info = FX_SYMBOLS_DKK.get(currency)
        rate = None
        if fx_info:
            fx_exchange, fx_symbol, multiplier = fx_info
            try:
                df = tv.get_hist(
                    symbol=fx_symbol,
                    exchange=fx_exchange,
                    interval=Interval.in_daily,
                    n_bars=10,
                )
                if df is not None and not df.empty:
                    df = df.dropna(subset=["close"])
                    if not df.empty:
                        rate = float(df["close"].iloc[-1]) * float(multiplier)
            except Exception:
                rate = None
        if rate is None:
            rate = FALLBACK_FX_DKK.get(currency, 1.0)
            used_fallback.append(currency)
        rates[currency] = rate
    return rates, used_fallback


def format_pct(value):
    try:
        if value is None or pd.isna(value):
            return "-"
        return f"{float(value):+.1f}%".replace(".", ",")
    except Exception:
        return "-"


def pct_change_from_bars(df, bars_back):
    try:
        if df is None or len(df) <= bars_back:
            return None
        now = float(df["close"].iloc[-1])
        then = float(df["close"].iloc[-1 - bars_back])
        if then == 0:
            return None
        return (now / then - 1.0) * 100.0
    except Exception:
        return None



def clamp(value, low=0.0, high=100.0):
    try:
        return max(low, min(high, float(value)))
    except Exception:
        return low


def _linear_regression_scores(closes, window_bars):
    """Returnerer (trendstyrke, robusthed) for et vindue.

    Trendstyrke: 0-100 baseret på annualiseret hældning af log-kursens regressionslinje.
    Robusthed: 0-100 baseret på hvor meget kursen typisk afviger fra regressionslinjen.
    Et jævnt fald kan derfor stadig være robust, mens en voldsomt hoppende aktie scorer lavt.
    """
    try:
        vals = [float(x) for x in closes[-window_bars:] if float(x) > 0]
        n = len(vals)
        if n < max(30, min(window_bars, 60)):
            return None, None

        # Simpel lineær regression uden numpy, så programmet fortsat kun kræver pandas/tvDatafeed.
        import math
        ys = [math.log(v) for v in vals]
        xs = list(range(n))
        mean_x = (n - 1) / 2.0
        mean_y = sum(ys) / n
        denom = sum((x - mean_x) ** 2 for x in xs)
        if denom <= 0:
            return None, None
        slope = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys)) / denom
        intercept = mean_y - slope * mean_x

        annualized_pct = (math.exp(slope * 252.0) - 1.0) * 100.0
        # -30% annualiseret trend -> 0 point, +50% -> 100 point. Over/under klippes.
        trend_score = clamp((annualized_pct + 30.0) / 80.0 * 100.0)

        residual_pcts = []
        for x, y in zip(xs, ys):
            fitted = intercept + slope * x
            residual_pcts.append((math.exp(abs(y - fitted)) - 1.0) * 100.0)
        noise = sum(residual_pcts) / len(residual_pcts) if residual_pcts else None
        if noise is None:
            return trend_score, None

        # 0% støj -> 100. 7% typisk afstand -> 50. Højere støj straffes progressivt.
        robustness_score = 100.0 / (1.0 + (noise / 7.0) ** 2)
        return clamp(trend_score), clamp(robustness_score)
    except Exception:
        return None, None


def trend_robustness_scores(df):
    """Samlet trendstyrke og robusthed baseret på 3M/1Y/3Y.

    Vægtning: 3M = 50%, 1Y = 30%, 3Y = 20%.
    Der vises kun de samlede scorer i tabellen, men delberegningerne giver scoren mere nutidighed.
    """
    try:
        if df is None or df.empty or "close" not in df.columns:
            return None, None
        closes = [float(x) for x in df["close"].dropna().tolist() if float(x) > 0]
        if len(closes) < 60:
            return None, None
        windows = [(63, 0.50), (252, 0.30), (756, 0.20)]
        trend_sum = robust_sum = weight_sum_trend = weight_sum_robust = 0.0
        for bars, weight in windows:
            t, r = _linear_regression_scores(closes, min(bars, len(closes)))
            if t is not None:
                trend_sum += t * weight
                weight_sum_trend += weight
            if r is not None:
                robust_sum += r * weight
                weight_sum_robust += weight
        trend = trend_sum / weight_sum_trend if weight_sum_trend > 0 else None
        robust = robust_sum / weight_sum_robust if weight_sum_robust > 0 else None
        return trend, robust
    except Exception:
        return None, None

def fetch_one(tv, item, fx_rates):
    try:
        df = tv.get_hist(
            symbol=item["ticker"],
            exchange=item["exchange"],
            interval=Interval.in_daily,
            n_bars=1350,
        )
    except Exception:
        return None
    if df is None or df.empty:
        return None
    df = df.dropna(subset=["close"]).copy()
    if df.empty:
        return None
    price = float(df["close"].iloc[-1])
    sma50 = float(df["close"].tail(50).mean()) if len(df) >= 50 else None
    trend_strength, robustness = trend_robustness_scores(df)
    antal = float(item.get("antal", 0.0) or 0.0)
    value_native = price * antal
    currency = currency_for_exchange(item["exchange"])
    fx_to_dkk = float(fx_rates.get(currency, 1.0) or 1.0)
    value_dkk = value_native * fx_to_dkk
    result = {
        "exchange": item["exchange"],
        "ticker": item["ticker"],
        "name": item["name"],
        "antal_raw": antal,
        "price_raw": price,
        "sma50_raw": sma50,
        "trend_strength_raw": trend_strength,
        "robustness_raw": robustness,
        "history_days_raw": len(df),
        "currency": currency,
        "fx_to_dkk": fx_to_dkk,
        "usd_to_dkk": float(fx_rates.get("USD", FALLBACK_FX_DKK["USD"]) or FALLBACK_FX_DKK["USD"]),
        "value_native_raw": value_native,
        "value_raw": value_dkk,
        "data_date": str(pd.Timestamp(df.index[-1]).date()),
    }
    for key, _title, bars in PERIODS:
        result[key + "_raw"] = pct_change_from_bars(df, bars)
    return result


def make_display_row(raw, total_value):
    weight = raw["value_raw"] / total_value * 100.0 if total_value > 0 else 0.0
    display = {
        "rank": "",
        "exchange": raw["exchange"],
        "ticker": raw["ticker"],
        "name": raw["name"],
        "antal": format_antal(raw["antal_raw"]),
        "price": format_num(raw["price_raw"], 2),
        "currency": raw.get("currency", "DKK"),
        "value_dkk": format_dkk(raw.get("value_raw")),
        "weight": format_pct(weight).replace("+", ""),
        "sort_rank": 999999,
        "sort_exchange": raw["exchange"].casefold(),
        "sort_ticker": raw["ticker"].casefold(),
        "sort_name": raw["name"].casefold(),
        "sort_antal": raw["antal_raw"],
        "sort_price": raw["price_raw"],
        "sort_currency": raw.get("currency", "DKK"),
        "sort_value_dkk": raw.get("value_raw", 0.0),
        "sort_weight": weight,
        "is_summary": False,
        "is_cash": bool(raw.get("is_cash")),
        "data_date": raw.get("data_date", ""),
    }
    for key, _title, _bars in PERIODS:
        v = raw.get(key + "_raw")
        display[key] = format_pct(v)
        display["sort_" + key] = -999999 if v is None else float(v)
    return display


def make_summary_row(display_rows):
    summary = {
        "rank": "",
        "exchange": "",
        "ticker": "",
        "name": "Samlet udvikling",
        "antal": "",
        "price": "",
        "currency": "DKK",
        "value_dkk": format_dkk(sum(r.get("sort_value_dkk", 0.0) for r in display_rows)) if display_rows else "-",
        "weight": "100,0%" if display_rows else "-",
        "is_summary": True,
        "data_date": "",
    }
    for col in COLUMN_IDS:
        summary["sort_" + col] = 0
    for key, _title, _bars in PERIODS:
        weighted = 0.0
        has_value = False
        for r in display_rows:
            pct = r.get("sort_" + key, -999999)
            weight = r.get("sort_weight", 0.0) / 100.0
            if pct != -999999:
                weighted += weight * pct
                has_value = True
        summary[key] = format_pct(weighted) if has_value else "-"
        summary["sort_" + key] = weighted if has_value else -999999
    summary["sort_name"] = ""
    summary["sort_currency"] = "DKK"
    summary["sort_value_dkk"] = sum(r.get("sort_value_dkk", 0.0) for r in display_rows)
    summary["sort_weight"] = 100
    return summary



def parse_float(value, default=None):
    try:
        if value is None:
            return default
        txt = str(value).strip().replace("%", "")
        if txt == "" or txt == "-":
            return default
        if "," in txt and "." in txt:
            txt = txt.replace(".", "").replace(",", ".")
        elif "," in txt:
            txt = txt.replace(",", ".")
        return float(txt)
    except Exception:
        return default


def format_plain_pct(value):
    v = parse_float(value, None)
    if v is None:
        return "-"
    return f"{v:+.1f}%".replace(".", ",")


def _as_tv_number(value):
    if value is None or value == "":
        return ""
    try:
        v = float(value)
    except Exception:
        return str(value).strip()
    if abs(v) >= 1000:
        return f"{v:.0f}"
    if abs(v) >= 100:
        return f"{v:.1f}"
    return f"{v:.2f}".rstrip("0").rstrip(".")


def _decode_tv_value(value):
    if value is None:
        return ""
    txt = str(value).strip()
    try:
        txt = json.loads(f'"{txt}"')
    except Exception:
        pass
    return unescape(txt).strip()


def _extract_by_column(columns, values, *names):
    if not values:
        return None
    index = {c: i for i, c in enumerate(columns)}
    for name in names:
        i = index.get(name)
        if i is not None and i < len(values) and values[i] not in (None, ""):
            return values[i]
    return None


def _tv_post_json(url, payload):
    data = json.dumps(payload).encode("utf-8")
    req = Request(url, data=data, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
        "Accept": "application/json,text/plain,*/*",
        "Accept-Language": "en-US,en;q=0.9,da;q=0.8",
        "Content-Type": "application/json",
        "Origin": "https://www.tradingview.com",
        "Referer": "https://www.tradingview.com/",
    }, method="POST")
    with urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8", errors="ignore"))


TV_FUNDAMENTAL_COLUMNS = [
    "name", "description", "sector", "industry", "country", "close", "market_cap_basic",
    "price_target_high", "price_target_1y", "price_target_median", "price_target_low",
    "earnings_release_next_date",
    "dividends_yield_current",
    "number_of_analysts", "recommendation_mark", "recommendation_buy", "recommendation_hold", "recommendation_sell",
    "total_revenue_3y_growth", "revenue_3y_growth", "total_revenue_cagr_3y", "revenue_cagr_3y",
    "total_revenue_yoy_growth_ttm", "revenue_yoy_growth_ttm",
    "ebit_margin_ttm", "operating_margin_ttm",
    # Kapitalforrentning og cash flow. TradingView-feltnavne kan variere
    # mellem markeder, så flere kendte varianter anmodes og første gyldige bruges.
    "return_on_invested_capital", "return_on_invested_capital_ttm", "return_on_invested_capital_fq",
    "free_cash_flow_margin_ttm", "free_cash_flow_margin",
    "free_cash_flow_3y_growth", "free_cash_flow_growth_3y", "free_cash_flow_cagr_3y",
    "free_cash_flow_yoy_growth_ttm",
    "price_earnings_ttm", "price_earnings_growth_ttm",
    # Fase 2B – seneste offentliggjorte balanceposter og udestående aktier.
    # Flere varianter anmodes, fordi TradingViews feltnavne varierer mellem markeder.
    "total_assets_fq", "total_assets",
    "total_liabilities_fq", "total_liabilities",
    "goodwill_fq", "goodwill",
    "total_equity_fq", "total_equity", "total_stockholders_equity_fq", "stockholders_equity_fq",
    "total_common_shares_outstanding", "common_shares_outstanding", "total_shares_outstanding", "total_shares_outstanding_fq", "common_stock_shares_outstanding_fq",
]


def fetch_fundamental_row_from_tradingview_scanner(item):
    exchange = str(item.get("exchange", "")).upper().strip()
    ticker = str(item.get("ticker", "")).upper().strip()
    if not exchange or not ticker:
        return {}
    symbols = {"tickers": [f"{exchange}:{ticker}"], "query": {"types": []}}
    payload = {"symbols": symbols, "columns": TV_FUNDAMENTAL_COLUMNS, "ignore_unknown_fields": True}
    last_error = None
    for market in ("global", "america"):
        try:
            result = _tv_post_json(f"https://scanner.tradingview.com/{market}/scan", payload)
            rows_found = result.get("data") or []
            if not rows_found:
                continue
            values = rows_found[0].get("d") or []
            out = {}
            name = _extract_by_column(TV_FUNDAMENTAL_COLUMNS, values, "description", "name")
            if name:
                out["name"] = str(name).strip()
            mapping = {
                "sector": ("sector",),
                "industry": ("industry",),
                "country": ("country",),
                "kurs_f2": ("close",),
                "market_cap": ("market_cap_basic",),
                "target_high": ("price_target_high",),
                "target_base": ("price_target_1y",),
                "target_median": ("price_target_median",),
                "target_low": ("price_target_low",),
                "earnings_next_date": ("earnings_release_next_date",),
                "dividend_yield": ("dividends_yield_current",),
                "analyst_count": ("number_of_analysts",),
                "revenue_growth_3y": ("total_revenue_3y_growth", "revenue_3y_growth", "total_revenue_cagr_3y", "revenue_cagr_3y", "total_revenue_yoy_growth_ttm", "revenue_yoy_growth_ttm"),
                "ebit_margin_ttm": ("ebit_margin_ttm", "operating_margin_ttm"),
                "roic": ("return_on_invested_capital", "return_on_invested_capital_ttm", "return_on_invested_capital_fq"),
                "fcf_margin_ttm": ("free_cash_flow_margin_ttm", "free_cash_flow_margin"),
                "fcf_growth_3y": ("free_cash_flow_3y_growth", "free_cash_flow_growth_3y", "free_cash_flow_cagr_3y", "free_cash_flow_yoy_growth_ttm"),
                "pe": ("price_earnings_ttm",),
                "peg": ("price_earnings_growth_ttm",),
                "total_assets": ("total_assets_fq", "total_assets"),
                "total_liabilities": ("total_liabilities_fq", "total_liabilities"),
                "goodwill": ("goodwill_fq", "goodwill"),
                "total_equity": ("total_equity_fq", "total_equity", "total_stockholders_equity_fq", "stockholders_equity_fq"),
                "shares_outstanding": ("total_common_shares_outstanding", "common_shares_outstanding", "total_shares_outstanding", "total_shares_outstanding_fq", "common_stock_shares_outstanding_fq"),
            }
            for field, cols in mapping.items():
                v = _extract_by_column(TV_FUNDAMENTAL_COLUMNS, values, *cols)
                if v not in (None, ""):
                    out[field] = _as_tv_number(v) if field not in ("sector", "industry", "country") else str(v).strip()
            return out
        except Exception as e:
            last_error = e
            continue
    if last_error:
        raise RuntimeError(str(last_error))
    return {}



def fetch_scanner_rows_batch(items, batch_size=100):
    """Hent TradingView-scannerdata for mange aktier i få batch-opslag."""
    result_by_key = {}
    clean_items = [item for item in items if item.get("exchange") and item.get("ticker")]
    for start in range(0, len(clean_items), batch_size):
        chunk = clean_items[start:start + batch_size]
        ticker_strings = [f"{str(x['exchange']).upper()}:{str(x['ticker']).upper()}" for x in chunk]
        payload = {
            "symbols": {"tickers": ticker_strings, "query": {"types": []}},
            "columns": TV_FUNDAMENTAL_COLUMNS,
            "ignore_unknown_fields": True,
        }
        response = None
        for market in ("global", "america"):
            try:
                candidate = _tv_post_json(f"https://scanner.tradingview.com/{market}/scan", payload)
                if candidate.get("data"):
                    response = candidate
                    break
            except Exception:
                continue
        if not response:
            continue
        for row in response.get("data", []):
            symbol = str(row.get("s", "")).upper().strip()
            values = row.get("d") or []
            if not symbol:
                continue
            out = {}
            name = _extract_by_column(TV_FUNDAMENTAL_COLUMNS, values, "description", "name")
            if name:
                out["name"] = str(name).strip()
            for field, cols in {
                "sector": ("sector",),
                "industry": ("industry",),
                "country": ("country",),
                "kurs_f2": ("close",), "target_high": ("price_target_high",),
                "target_base": ("price_target_1y",), "target_median": ("price_target_median",),
                "target_low": ("price_target_low",),
                "earnings_next_date": ("earnings_release_next_date",),
                "dividend_yield": ("dividends_yield_current",),
                "analyst_count": ("number_of_analysts",),
            }.items():
                value = _extract_by_column(TV_FUNDAMENTAL_COLUMNS, values, *cols)
                if value not in (None, ""):
                    out[field] = str(value).strip() if field in ("sector", "industry", "country") else _as_tv_number(value)
            result_by_key[symbol] = out
    return result_by_key


def update_archived_analyst_history(fx_rates, force_refresh=False):
    """Opdatér Watch list med samme kursmålskæde som aktive aktier.

    En vellykket normal opdatering udføres højst én gang pr. dag. En forceret
    opdatering henter altid på ny. Fejlede opslag markeres ikke som gennemført,
    så de kan forsøges igen ved næste opdatering samme dag.
    """
    registry = load_stock_registry()
    stocks = registry.setdefault("stocks", {})
    active_keys = {position_key(item) for item in portfolio if not is_cash_item(item)}
    candidates = []
    for key, entry in stocks.items():
        if not isinstance(entry, dict) or key in active_keys:
            continue
        calendar_current = entry.get("calendar_schema_v3") == 3
        if not force_refresh and entry.get("last_analyst_check_date") == today_key() and calendar_current:
            continue
        candidates.append(entry)
    if not candidates:
        return 0, 0

    fetched = fetch_scanner_rows_batch(candidates)
    updated = checked = 0
    for entry in candidates:
        key = f"{str(entry.get('exchange','')).upper()}:{str(entry.get('ticker','')).upper()}"
        row = fetched.get(key)
        checked += 1
        entry["last_analyst_attempt_date"] = today_key()
        if not row:
            continue
        # Kun et vellykket TradingView-opslag tæller som dagens opdatering.
        entry["last_analyst_check_date"] = today_key()
        entry["calendar_schema_v3"] = 3
        if row.get("name"):
            entry["name"] = row["name"]
        price = parse_float(row.get("kurs_f2"), None)
        currency = entry.get("currency") or currency_for_exchange(entry.get("exchange"))
        targets = _normalize_scenario_targets(
            row, currency=currency,
            fx_to_dkk=fx_rates.get(currency, FALLBACK_FX_DKK.get(currency, 1.0)),
            usd_to_dkk=fx_rates.get("USD", FALLBACK_FX_DKK["USD"]),
        )
        display_stub = {"exchange": entry.get("exchange"), "ticker": entry.get("ticker"), "name": entry.get("name")}
        before = load_target_age_history().get("positions", {}).get(key, {}).get("last_change_date")
        target_age_days_for_row(display_stub, targets, price)
        # Watch list-aktier skal have samme regnskabshistorik som aktive aktier.
        # Batch-opslaget henter derfor også næste regnskabsdato, som registreres
        # som en selvstændig begivenhed uden at påvirke KM-alder eller støjfilter.
        register_earnings_date_for_row(display_stub, row.get("earnings_next_date"))
        after = load_target_age_history().get("positions", {}).get(key, {}).get("last_change_date")
        if after != before:
            updated += 1
    save_stock_registry(registry)
    return checked, updated

def tradingview_symbol_slug(item):
    exchange = str(item.get("exchange", "")).upper().strip()
    ticker = str(item.get("ticker", "")).upper().strip()
    if not exchange or not ticker:
        return ""
    return quote(f"{exchange}-{ticker}", safe="")


def _read_url_text(url, timeout=15):
    req = Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,application/json,text/plain,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9,da;q=0.8",
        "Referer": "https://www.tradingview.com/",
    })
    with urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def _translate_dividend_frequency(value):
    """Oversæt TradingViews udbyttefrekvens til kompakt dansk visning."""
    raw = str(value or "").strip().lower()
    if not raw:
        return ""
    raw = raw.replace("semiannual", "semi-annual")
    mapping = {
        "weekly": "Uge",
        "monthly": "Måned",
        "quarterly": "Kvartal",
        "semi-annually": "Halvår",
        "semi-annual": "Halvår",
        "semiannual": "Halvår",
        "annually": "År",
        "annual": "År",
        "yearly": "År",
        "other": "Andet",
    }
    if raw in mapping:
        return mapping[raw]
    for key, label in mapping.items():
        if key in raw:
            return label
    return str(value).strip()


def _extract_dividend_dates_from_tv_html(html):
    """Find historiske udbyttedatoer i TradingViews dividenddata.

    TradingView beskriver den almindelige dividend-"Date" som ex-dividend-dato.
    Websiden kan samtidig indeholde pay/payment dates. Til kolonnen "Seneste
    udbytte" er målet blot et stabilt rytmeanker, så begge typer accepteres,
    men kun datoer i dag eller tidligere kan blive valgt som seneste rå dato.
    """
    if not html:
        return []
    decoded = unescape(html).replace("\\/", "/")
    found = set()

    # Eksplicitte dato-felter, som TradingView kan lægge i indlejret JSON.
    date_keys = (
        r'payment_date|pay_date|paymentDate|payDate|dividend_payment_date|'
        r'dividendPaymentDate|paymentDateTimestamp|payDateTimestamp|payment_timestamp|'
        r'ex_date|exDate|ex_dividend_date|exDividendDate|exDateTimestamp|'
        r'dividend_date|dividendDate|dividendDateTimestamp'
    )
    for pattern in [
        rf'"(?:{date_keys})"\s*:\s*"([^"]+)"',
        rf'"(?:{date_keys})"\s*:\s*([0-9]{{9,13}})',
    ]:
        for match in re.finditer(pattern, decoded, flags=re.IGNORECASE):
            parsed = _date_from_tv_value(match.group(1))
            if parsed is not None:
                found.add(parsed)

    # Synlig tekst omkring Payment date / Pay date / Ex-dividend date.
    text = re.sub(r"<[^>]+>", " ", decoded)
    text = re.sub(r"\s+", " ", text)
    month_names = r"January|February|March|April|May|June|July|August|September|October|November|December"
    for match in re.finditer(
        rf"(?:payment|pay|ex[- ]?dividend)\s+date[^A-Za-z0-9]{{0,50}}(({month_names})\s+\d{{1,2}},?\s+\d{{4}})",
        text, flags=re.IGNORECASE,
    ):
        raw = match.group(1).replace(",", "")
        try:
            found.add(datetime.strptime(raw, "%B %d %Y").date())
        except Exception:
            pass

    # TradingViews tekst/JSON ændres løbende. Som sidste fallback gennemsøges
    # små tekstvinduer omkring ordet dividend for ISO- og engelske datoer.
    # Det begrænser risikoen for at samle fx earnings- eller copyright-datoer op.
    for marker in re.finditer(r"dividend", decoded, flags=re.IGNORECASE):
        lo = max(0, marker.start() - 350)
        hi = min(len(decoded), marker.end() + 700)
        window = decoded[lo:hi]
        for iso in re.finditer(r"\b(20\d{2}-\d{2}-\d{2})(?:[T ][^\"<\s]+)?", window):
            parsed = _date_from_tv_value(iso.group(1))
            if parsed is not None:
                found.add(parsed)
        window_text = re.sub(r"<[^>]+>", " ", window)
        for human in re.finditer(rf"\b(({month_names})\s+\d{{1,2}},?\s+20\d{{2}})\b", window_text, flags=re.IGNORECASE):
            raw = human.group(1).replace(",", "")
            try:
                found.add(datetime.strptime(raw, "%B %d %Y").date())
            except Exception:
                pass

    today = date.today()
    return sorted(d for d in found if d <= today)


def _frequency_month_step(frequency):
    """Omsæt dansk/engelsk udbyttefrekvens til hele måneder mellem betalinger."""
    raw = str(frequency or "").strip().lower()
    if raw in ("måned", "monthly"):
        return 1
    if raw in ("kvartal", "quarterly"):
        return 3
    if raw in ("halvår", "semi-annual", "semi-annually", "semiannual"):
        return 6
    if raw in ("år", "annual", "annually", "yearly"):
        return 12
    return None


def _payments_per_year(frequency):
    """Antal normale udbyttebetalinger pr. år ud fra frekvensen."""
    raw = str(frequency or "").strip().lower()
    if raw in ("uge", "weekly"):
        return 52
    if raw in ("måned", "monthly"):
        return 12
    if raw in ("kvartal", "quarterly"):
        return 4
    if raw in ("halvår", "semi-annual", "semi-annually", "semiannual"):
        return 2
    if raw in ("år", "annual", "annually", "yearly"):
        return 1
    return None


def _add_months_keep_day(source_date, months):
    """Læg hele måneder til en dato uden ekstern afhængighed."""
    import calendar
    month_index = source_date.year * 12 + (source_date.month - 1) + int(months)
    year, month0 = divmod(month_index, 12)
    month = month0 + 1
    day = min(source_date.day, calendar.monthrange(year, month)[1])
    return date(year, month, day)


def _danish_month_name(month, short=False):
    full = [
        "Januar", "Februar", "Marts", "April", "Maj", "Juni",
        "Juli", "August", "September", "Oktober", "November", "December",
    ]
    short_names = ["Jan", "Feb", "Mar", "Apr", "Maj", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dec"]
    try:
        idx = int(month) - 1
        return (short_names if short else full)[idx] if 0 <= idx < 12 else "-"
    except Exception:
        return "-"


def format_dividend_last_month(value):
    """Vis kun måneden for seneste rå TradingView-udbyttedato."""
    parsed = _date_from_tv_value(value)
    return _danish_month_name(parsed.month) if parsed is not None else "-"


def dividend_month_schedule(last_date_value, frequency):
    """Beregn de normale udbyttemåneder ud fra seneste dato og frekvens.

    Fx seneste udbytte i september + Kvartal => Mar/Jun/Sep/Dec.
    Rækkefølgen vises som kalenderår, fordi tabellen senere skal kunne bruges
    direkte til en månedsbaseret samlet udbytteoversigt.
    """
    last_date = _date_from_tv_value(last_date_value)
    if last_date is None:
        return "-", []
    raw = str(frequency or "").strip().lower()
    if raw in ("uge", "weekly"):
        return "Løbende", list(range(1, 13))
    step = _frequency_month_step(frequency)
    payments = _payments_per_year(frequency)
    if step is None or payments is None:
        return "-", []
    months = sorted({(_add_months_keep_day(last_date, step * i)).month for i in range(payments)})
    if len(months) >= 12:
        return "Alle måneder", months
    return "/".join(_danish_month_name(m, short=True) for m in months), months


def dividend_payment_amount_dkk(position_value_dkk, dividend_yield_pct, frequency):
    """Estimer brutto-DKK pr. normal betaling fra årligt yield og frekvens."""
    value = parse_float(position_value_dkk, None)
    yield_pct = parse_float(dividend_yield_pct, None)
    payments = _payments_per_year(frequency)
    if value is None or value < 0 or yield_pct is None or yield_pct <= 0 or not payments:
        return None
    return value * yield_pct / 100.0 / float(payments)


def _fetch_dividend_dates_batch(items):
    """Hent mulige udbyttedatoer i batch for hele porteføljen.

    v6.96 probede op til mange screenerfelter separat for HVER aktie, hvilket
    kunne udløse meget mange netkald. v6.97 prøver kun et lille sæt relevante
    kandidatfelter og sender hele porteføljen med i samme request. Resultatet
    gemmes i et dict pr. symbol og genbruges af alle aktier i samme opdatering.
    """
    clean = [x for x in (items or []) if x.get("exchange") and x.get("ticker") and not is_cash_item(x)]
    if not clean:
        return {}

    symbols = [f"{str(x['exchange']).upper()}:{str(x['ticker']).upper()}" for x in clean]
    result = {symbol: [] for symbol in symbols}

    # Begrænset kandidatpakke: nok til fallback, men uden v6.96's 22 felter pr. aktie.
    candidates = [
        ("recent_ex", "dividend_ex_date_recent"),
        ("recent_ex", "dividends_ex_date_recent"),
        ("recent_pay", "dividend_payment_date_recent"),
        ("recent_pay", "dividend_pay_date_recent"),
        ("upcoming_ex", "dividend_ex_date_upcoming"),
        ("upcoming_pay", "dividend_payment_date_upcoming"),
    ]

    for kind, field in candidates:
        payload = {
            "symbols": {"tickers": symbols, "query": {"types": []}},
            "columns": [field],
            "ignore_unknown_fields": True,
        }
        response = None
        # Normalt er ét globalt batch-opslag nok. America prøves kun hvis global
        # slet ikke returnerer data for feltet.
        for market in ("global", "america"):
            try:
                candidate = _tv_post_json(f"https://scanner.tradingview.com/{market}/scan", payload)
                if candidate.get("data"):
                    response = candidate
                    break
            except Exception:
                continue
        if not response:
            continue

        for row in response.get("data", []):
            symbol = str(row.get("s", "")).upper().strip()
            values = row.get("d") or []
            if not symbol or not values:
                continue
            parsed = _date_from_tv_value(values[0])
            if parsed is None:
                continue
            pair = (parsed, kind)
            if pair not in result.setdefault(symbol, []):
                result[symbol].append(pair)

    return result


_dividend_date_batch_cache = {}

def fetch_tradingview_dividend_schedule(item):
    """Hent rå udbyttefrekvens og seneste historiske udbyttedato fra TradingView.

    Fremtidige måneder beregnes ikke her. Funktionen returnerer kun rådata;
    selve Udbyttemåned-kolonnen bygges senere i make_phase2_row, så grænsen
    mellem hentede data og programmets egen beregning er tydelig.
    """
    slug = tradingview_symbol_slug(item)
    if not slug:
        return {}

    pages = []
    for url in (
        f"https://www.tradingview.com/symbols/{slug}/financials-dividends/",
        f"https://www.tradingview.com/symbols/{slug}/",
    ):
        try:
            pages.append(_read_url_text(url, timeout=10))
        except Exception:
            continue
    if not pages:
        return {}

    combined = "\n".join(pages)
    decoded = unescape(combined)
    text = re.sub(r"<[^>]+>", " ", decoded)
    text = re.sub(r"\s+", " ", text).strip()

    frequency = ""
    frequency_patterns = [
        r"Payouts\s+are\s+made\s+(weekly|monthly|quarterly|semi-annually|semi-annual|annually|annual|yearly|other)",
        r"dividends?\s+are\s+paid\s+(weekly|monthly|quarterly|semi-annually|semi-annual|annually|annual|yearly|other)",
        r"paid\s+(weekly|monthly|quarterly|semi-annually|semi-annual|annually|annual|yearly)",
    ]
    for pattern in frequency_patterns:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            frequency = _translate_dividend_frequency(match.group(1))
            break

    if not frequency:
        for pattern in [r'"(?:dividend_frequency|dividends_frequency|frequency)"\s*:\s*"([^"]+)"']:
            match = re.search(pattern, decoded, flags=re.IGNORECASE)
            if match:
                candidate = _translate_dividend_frequency(match.group(1))
                if candidate in {"Uge", "Måned", "Kvartal", "Halvår", "År", "Andet"}:
                    frequency = candidate
                    break

    historical_dates = _extract_dividend_dates_from_tv_html(decoded)

    # v6.96: Hvis symbolsidens HTML ikke indeholder en brugbar historisk dato,
    # spørg TradingViews screener separat. Vi foretrækker en historisk ex-/pay-
    # dato (rådata). Hvis screeneren kun har en kommende dato, gemmes den som
    # rytmeanker i et særskilt felt; Seneste udbytte forbliver da '-'.
    symbol_key = f"{str(item.get('exchange', '')).upper()}:{str(item.get('ticker', '')).upper()}"
    scanner_dates = _dividend_date_batch_cache.get(symbol_key, [])
    scanner_historical = sorted({
        d for d, kind in scanner_dates
        if d <= date.today() and kind.startswith("recent_")
    })
    if not scanner_historical:
        scanner_historical = sorted({d for d, _kind in scanner_dates if d <= date.today()})

    all_historical = sorted(set(historical_dates) | set(scanner_historical))
    last_date = all_historical[-1] if all_historical else None

    future_scanner = sorted({d for d, _kind in scanner_dates if d > date.today()})
    upcoming_anchor = future_scanner[0] if future_scanner else None

    return {
        "dividend_frequency": frequency,
        "dividend_last_date": last_date.isoformat() if last_date else "",
        "dividend_upcoming_anchor_date": upcoming_anchor.isoformat() if upcoming_anchor else "",
    }


def _normal_number_from_text(txt):
    if txt is None:
        return None
    s = str(txt).strip()
    if not s:
        return None
    s = s.replace("\u202f", "").replace("&nbsp;", "")
    s = re.sub(r"[^0-9,.-]", "", s)
    if not s or s in ("-", ".", ","):
        return None
    if "," in s and "." in s:
        if s.rfind(",") > s.rfind("."):
            s = s.replace(".", "").replace(",", ".")
        else:
            s = s.replace(",", "")
    elif "," in s:
        s = s.replace(",", ".")
    return parse_float(s, None)


def _extract_tv_forecast_target_price(html):
    if not html:
        return None, "tom side"
    decoded = unescape(html)
    text = re.sub(r"<[^>]+>", " ", decoded)
    text = re.sub(r"\s+", " ", text)
    for pattern in [
        r"price target is\s*([0-9][0-9.,\s]*)",
        r"analysts[^.]{0,180}?price target[^0-9]{0,40}([0-9][0-9.,\s]*)",
        r"average target price[^0-9]{0,40}([0-9][0-9.,\s]*)",
        r"1Y\s+forecast[^0-9]{0,80}([0-9][0-9.,\s]*)",
        r"Price Target\s+1Y\s+Forecast[^0-9]{0,80}([0-9][0-9.,\s]*)",
    ]:
        m = re.search(pattern, text, flags=re.IGNORECASE)
        if m:
            v = _normal_number_from_text(m.group(1))
            if v is not None and v > 0:
                return v, "TradingView forecast tekst"
    for pattern in [
        r'"price_target_mean"\s*:\s*([-+]?[0-9]+(?:\.[0-9]+)?)',
        r'"price_target_average"\s*:\s*([-+]?[0-9]+(?:\.[0-9]+)?)',
        r'"target_price_mean"\s*:\s*([-+]?[0-9]+(?:\.[0-9]+)?)',
        r'"targetMeanPrice"\s*:\s*([-+]?[0-9]+(?:\.[0-9]+)?)',
        r'"target_mean_price"\s*:\s*([-+]?[0-9]+(?:\.[0-9]+)?)',
        r'"targetConsensus"\s*:\s*([-+]?[0-9]+(?:\.[0-9]+)?)',
        r'"consensus_target_price"\s*:\s*([-+]?[0-9]+(?:\.[0-9]+)?)',
        r'"priceTarget"\s*:\s*([-+]?[0-9]+(?:\.[0-9]+)?)',
        r'"price_target"\s*:\s*([-+]?[0-9]+(?:\.[0-9]+)?)',
        r'"target_price"\s*:\s*([-+]?[0-9]+(?:\.[0-9]+)?)',
    ]:
        m = re.search(pattern, decoded, flags=re.IGNORECASE)
        if m:
            v = _normal_number_from_text(m.group(1))
            if v is not None and v > 0:
                return v, "TradingView forecast JSON"
    return None, "Price Target 1Y Forecast ikke fundet"


def fetch_tradingview_forecast_upside(item, price):
    slug = tradingview_symbol_slug(item)
    if not slug:
        return "", "mangler TradingView-symbol"
    if price is None or price <= 0:
        return "", "mangler kurs til beregning"
    last_msg = ""
    for url in [f"https://www.tradingview.com/symbols/{slug}/forecast/", f"https://www.tradingview.com/symbols/{slug}/"]:
        try:
            html = _read_url_text(url, timeout=15)
            target, msg = _extract_tv_forecast_target_price(html)
            last_msg = msg
            if target is not None and target > 0:
                upside = (target / price - 1.0) * 100.0
                return _as_tv_number(upside), f"{msg}; target={_as_tv_number(target)}"
        except Exception as e:
            last_msg = str(e)
            continue
    return "", last_msg or "ingen TradingView forecast data"



def upside_from_target(target_value, price):
    target = parse_float(target_value, None)
    try:
        price = float(price)
    except Exception:
        price = None
    if target is None or price is None or price <= 0:
        return None
    return (target / price - 1.0) * 100.0


def _targets_are_logical(bull_target, base_target, median_target, bear_target):
    """True når kursmålene har en mulig Bull/Base/Median/Bear-rækkefølge."""
    targets = (bull_target, base_target, median_target, bear_target)
    if any(value is None for value in targets):
        return False
    return bear_target <= median_target <= bull_target and bear_target <= base_target <= bull_target


def _nearly_equal(values, relative_tolerance=0.005, absolute_tolerance=0.01):
    """True når alle værdier praktisk talt er ens."""
    values = [float(value) for value in values if value is not None]
    if len(values) < 2:
        return False
    tolerance = max(absolute_tolerance, abs(sum(values) / len(values)) * relative_tolerance)
    return max(values) - min(values) <= tolerance


def _convert_usd_targets_to_local(targets, currency, fx_to_dkk, usd_to_dkk):
    """Omregn scannerens USD-normaliserede kursmål til noteringens lokale valuta."""
    currency = str(currency or "USD").upper()
    local_fx = parse_float(fx_to_dkk, None)
    usd_fx = parse_float(usd_to_dkk, None)

    if currency == "USD" or not local_fx or local_fx <= 0 or not usd_fx or usd_fx <= 0:
        return None

    usd_to_local = usd_fx / local_fx
    return tuple(value * usd_to_local if value is not None else None for value in targets)


def _normalize_scenario_targets(fundamental, currency="USD", fx_to_dkk=1.0, usd_to_dkk=None):
    """Returnér TradingViews kursmål i aktiens lokale handelsvaluta.

    TradingViews Base/Avg leveres normalt i lokal valuta, mens Max/Median/Min
    på nogle ikke-amerikanske aktier leveres USD-normaliseret. Tidligere blev
    USD-omregningen kun accepteret, hvis scenarierne samtidig havde den logiske
    rækkefølge Bear <= Median/Base <= Bull. Det gav meget forkerte procenter,
    når TradingView selv viste en usædvanlig rækkefølge, fx Min > Avg.

    Enhedsvalget er derfor nu adskilt fra datavalideringen: rå og omregnede
    Max/Median/Min sammenlignes med Base, og den skala der ligger klart tættest
    på Base vælges. Den indbyrdes rækkefølge bevares præcis som TradingView
    leverer den. Ulogiske scenarier markeres fortsat som datavarsling senere.
    """
    import math

    base_target = parse_float(fundamental.get("target_base"), None)
    raw_targets = (
        parse_float(fundamental.get("target_high"), None),
        parse_float(fundamental.get("target_median"), None),
        parse_float(fundamental.get("target_low"), None),
    )
    bull_raw, median_raw, bear_raw = raw_targets

    # TradingView viser ved ét fælles kursmål Max = Avg = Min. Scannerfelterne
    # kan stadig være i en anden enhed end Base; Base er da den sikreste værdi.
    if base_target is not None and _nearly_equal(raw_targets):
        return {
            "bull_target": base_target,
            "base_target": base_target,
            "median_target": base_target,
            "bear_target": base_target,
        }

    converted = _convert_usd_targets_to_local(raw_targets, currency, fx_to_dkk, usd_to_dkk)

    def scale_distance(values):
        """Robust log-afstand mellem scenariernes skala og Base."""
        if base_target is None or base_target <= 0:
            return float("inf")
        distances = []
        for value in values or ():
            value = parse_float(value, None)
            if value is not None and value > 0:
                distances.append(abs(math.log(value / base_target)))
        if not distances:
            return float("inf")
        distances.sort()
        return distances[len(distances) // 2]

    selected = raw_targets
    if converted is not None:
        raw_distance = scale_distance(raw_targets)
        converted_distance = scale_distance(converted)
        # Brug den omregnede skala, når den tydeligt passer bedre til Base.
        # Faktoren forhindrer skift på grund af små valuta-/afrundingsforskelle.
        if converted_distance + 0.10 < raw_distance:
            selected = converted

    bull_target, median_target, bear_target = selected
    return {
        "bull_target": bull_target,
        "base_target": base_target,
        "median_target": median_target,
        "bear_target": bear_target,
    }


def _scenario_targets_materially_invalid(targets, relative_tolerance=0.10):
    """True kun ved et tydeligt brud på scenariernes forventede rækkefølge.

    TradingView kan levere små afrundings- eller kildeforskelle, hvor Bull fx
    ligger en anelse under Base. Det skal ikke give lys rød datavarsling.

    Tolerancen er 10 % af kursmålenes fælles størrelsesorden. Først når Bear,
    Base eller Median ligger tydeligt uden for intervallet mellem Bear og Bull,
    betragtes scenariet som ugyldigt.
    """
    bull = parse_float((targets or {}).get("bull_target"), None)
    base = parse_float((targets or {}).get("base_target"), None)
    median = parse_float((targets or {}).get("median_target"), None)
    bear = parse_float((targets or {}).get("bear_target"), None)

    if base is None:
        return True
    if any(value is None for value in (bull, median, bear)):
        return False

    scale = max(abs(bull), abs(base), abs(median), abs(bear), 1.0)
    tolerance = scale * relative_tolerance

    return (
        bear > bull + tolerance
        or base > bull + tolerance
        or base < bear - tolerance
        or median > bull + tolerance
        or median < bear - tolerance
    )


def analyst_scenario_values(fundamental, price, currency="USD", fx_to_dkk=1.0, usd_to_dkk=None):
    """Beregn Bull/Base/Median/Bear-procenter, spænd og datavalidering."""
    targets = _normalize_scenario_targets(
        fundamental,
        currency=currency,
        fx_to_dkk=fx_to_dkk,
        usd_to_dkk=usd_to_dkk,
    )

    bull = upside_from_target(targets["bull_target"], price)
    base = upside_from_target(targets["base_target"], price)
    if base is None:
        base = parse_float(fundamental.get("analyst_1y_upside_pct"), None)
    median = upside_from_target(targets["median_target"], price)
    bear = upside_from_target(targets["bear_target"], price)

    invalid = _scenario_targets_materially_invalid(targets)

    values = [value for value in (bull, base, median, bear) if value is not None]
    spread = max(values) - min(values) if len(values) >= 2 else None

    return {
        "bull": bull,
        "base": base,
        "median": median,
        "bear": bear,
        "spread": spread,
        "invalid": invalid,
    }


def nonlinear_potential_curve(adjusted_pct):
    """Ulineær 0-100 potentialescore fra justeret analytikerpotentiale.

    S-kurven betyder, at potentiale omkring 15-35% differentierer meget,
    mens meget høje forecasts gradvist mættes. Dermed får 100-300% bull-cases
    ikke lov til at dominere porteføljevægten alene.

    Omtrentlige niveauer før analytiker-spænd/konfidens:
    0% -> 0, 10% -> ca. 20, 20% -> ca. 50, 30% -> ca. 78, 40% -> ca. 92, 50%+ -> tæt på 100.
    """
    try:
        import math
        x = max(0.0, float(adjusted_pct))
        # Logistisk S-kurve centreret omkring 20% med moderat hældning.
        raw = 100.0 / (1.0 + math.exp(-(x - 20.0) / 7.0))
        # Normaliser så 0% bliver 0 i stedet for logistisk bundværdi.
        raw0 = 100.0 / (1.0 + math.exp(-(0.0 - 20.0) / 7.0))
        score = (raw - raw0) / (100.0 - raw0) * 100.0
        return clamp(score)
    except Exception:
        return 0.0


def analyst_adjusted_potential_score(analyst):
    """0-100 potentialescore med robust håndtering af TradingView-fejl.

    Når Bull, Base, Median og Bear er komplette og logisk sammenhængende,
    vægtes scenarierne konservativt. Enighed påvirker kun mildt med en faktor
    mellem 0,95 og 1,05.

    Hvis scenarierne er mangelfulde eller logisk ugyldige, bruges Base alene
    uden straf. En datakildefejl hos TradingView må dermed ikke sænke aktiens
    score ud over det, som selve Base-estimatet tilsiger.
    """
    base = analyst.get("base")
    if base is None:
        return None
    bull = analyst.get("bull")
    median = analyst.get("median")
    bear = analyst.get("bear")

    if analyst.get("invalid") or any(v is None for v in (bull, median, bear)):
        return nonlinear_potential_curve(base)

    adjusted = 0.50 * base + 0.25 * median + 0.15 * bull + 0.10 * bear
    spread = max(0.0, analyst.get("spread") or 0.0)
    capped_spread = min(spread, 200.0)
    # 0 pp -> 1,05; 100 pp -> 1,00; 200+ pp -> 0,95.
    agreement_factor = 1.05 - (capped_spread / 200.0) * 0.10
    return clamp(nonlinear_potential_curve(adjusted) * agreement_factor)



def analyst_confidence_score(analyst):
    """Tillidsscore 0-100 baseret på spændet mellem Bull og Bear.

    Et smalt spænd betyder, at analytikernes scenarier ligger relativt tæt,
    mens et meget bredt spænd signalerer stor usikkerhed. Scoren interpoleres
    lineært mellem disse praktiske knækpunkter:

    40 pp -> 100, 60 -> 90, 80 -> 80, 100 -> 70,
    130 -> 60, 170 -> 50, 220 -> 40, 300+ -> 30.

    Ugyldige eller mangelfulde scenarier får neutral score 50, så en fejl i
    datakilden hverken belønner eller straffer aktien urimeligt.
    """
    if analyst.get("invalid"):
        return 50.0
    spread = parse_float(analyst.get("spread"), None)
    bull = analyst.get("bull")
    base = analyst.get("base")
    median = analyst.get("median")
    bear = analyst.get("bear")
    if spread is None or any(v is None for v in (bull, base, median, bear)):
        return 50.0

    points = [
        (40.0, 100.0),
        (60.0, 90.0),
        (80.0, 80.0),
        (100.0, 70.0),
        (130.0, 60.0),
        (170.0, 50.0),
        (220.0, 40.0),
        (300.0, 30.0),
    ]
    spread = max(0.0, float(spread))
    if spread <= points[0][0]:
        return points[0][1]
    if spread >= points[-1][0]:
        return points[-1][1]

    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        if x0 <= spread <= x1:
            fraction = (spread - x0) / (x1 - x0)
            return clamp(y0 + fraction * (y1 - y0))
    return 50.0



def _score_linear(value, low, high, reverse=False, default=None):
    """Lineær 0-100 score. Hvis reverse=True er lav værdi bedst."""
    v = parse_float(value, None)
    if v is None:
        return default
    if reverse:
        return clamp((high - v) / (high - low) * 100.0)
    return clamp((v - low) / (high - low) * 100.0)


def peg_quality_score(peg):
    """PEG-score med glat S-kurve, hvor lavere positiv PEG er bedst.

    Kurven undgår hårde spring omkring fx PEG 1,0 eller 2,0. Omtrentlige
    niveauer er:
    - PEG 0,5 -> 94
    - PEG 1,0 -> 87
    - PEG 1,5 -> 73
    - PEG 2,0 -> 52
    - PEG 3,0 -> 15

    Manglende eller ikke-positiv PEG får fortsat neutral score 50, fordi
    negative PEG-værdier ofte skyldes negativ indtjening eller ubrugelige data.
    """
    v = parse_float(peg, None)
    if v is None or v <= 0:
        return 50.0
    try:
        import math
        return clamp(100.0 / (1.0 + math.exp((v - 2.05) / 0.55)))
    except Exception:
        return 50.0


def ebit_margin_quality_score(margin):
    """EBIT-margin-score med S-kurve.

    Marginen måler den løbende driftsindtjening i forhold til omsætningen.
    S-kurven gør forskellen mellem svag og god indtjening tydelig, mens meget
    høje marginer gradvist mættes.

    Omtrentlige niveauer:
    - 0%  -> 0
    - 5%  -> 10
    - 10% -> 24
    - 15% -> 50
    - 20% -> 76
    - 25% -> 92
    - 30%+ -> 100
    """
    v = parse_float(margin, None)
    if v is None:
        return 50.0
    try:
        import math
        x = clamp(v, 0.0, 30.0)
        raw = 1.0 / (1.0 + math.exp(-(x - 15.0) / 5.0))
        raw0 = 1.0 / (1.0 + math.exp(-((0.0 - 15.0) / 5.0)))
        raw30 = 1.0 / (1.0 + math.exp(-((30.0 - 15.0) / 5.0)))
        return clamp((raw - raw0) / (raw30 - raw0) * 100.0)
    except Exception:
        return 50.0


def pe_quality_score(pe):
    """PE-score. Meget lav/moderat PE belønnes, ekstrem PE straffes, men vægten er lav."""
    v = parse_float(pe, None)
    if v is None or v <= 0:
        return 50.0
    if v <= 20.0:
        return 100.0
    if v <= 40.0:
        return 100.0 - (v - 20.0) * 1.5
    if v <= 100.0:
        return 70.0 - (v - 40.0) * 0.75
    return 20.0


def roic_quality_score(roic):
    """ROIC-score 0-100. Høj og vedvarende kapitalforrentning belønnes.

    Omtrentlige niveauer: 0% -> 0, 8% -> 25, 15% -> 55,
    25% -> 85 og 35%+ -> 100. Manglende data er neutralt 50.
    """
    v = parse_float(roic, None)
    if v is None:
        return 50.0
    try:
        import math
        x = clamp(v, 0.0, 40.0)
        raw = 1.0 / (1.0 + math.exp(-(x - 14.0) / 6.0))
        raw0 = 1.0 / (1.0 + math.exp(-((0.0 - 14.0) / 6.0)))
        raw40 = 1.0 / (1.0 + math.exp(-((40.0 - 14.0) / 6.0)))
        return clamp((raw - raw0) / (raw40 - raw0) * 100.0)
    except Exception:
        return 50.0


def fcf_margin_quality_score(margin):
    """FCF-margin 0-100; sammenlignelig på tværs af selskabsstørrelser."""
    return _score_linear(margin, -5.0, 25.0, default=50.0)


def fcf_growth_quality_score(growth):
    """FCF-vækst 0-100. Negativ vækst straffes, 30%+ mættes."""
    return _score_linear(growth, -10.0, 30.0, default=50.0)


def calculate_quality_score(fundamental):
    """Kvalitetsscore 0-100 baseret på seks komplementære mål.

    Vægtning før ulineær skalering:
    - PEG: 20%
    - EBIT-margin TTM: 20%
    - Omsætningsvækst 3 år: 20%
    - FCF-vækst 3 år: 15%
    - FCF-margin TTM: 10%
    - ROIC: 15%

    ROIC og FCF belønner virksomheder, der dokumenteret skaber et højt afkast
    på kapitalen og omsætter indtjening til kontanter. Dermed bliver modellen
    mindre ensidigt orienteret mod de mest voldsomme vækstvirksomheder.
    Manglende værdier får neutral score 50.
    """
    peg_s = peg_quality_score(fundamental.get("peg"))
    ebit_s = ebit_margin_quality_score(fundamental.get("ebit_margin_ttm"))
    rev_s = _score_linear(fundamental.get("revenue_growth_3y"), -5.0, 35.0, default=50.0)
    fcf_growth_s = fcf_growth_quality_score(fundamental.get("fcf_growth_3y"))
    fcf_margin_s = fcf_margin_quality_score(fundamental.get("fcf_margin_ttm"))
    roic_s = roic_quality_score(fundamental.get("roic"))

    base_quality = clamp(
        0.20 * peg_s
        + 0.20 * ebit_s
        + 0.20 * rev_s
        + 0.15 * fcf_growth_s
        + 0.10 * fcf_margin_s
        + 0.15 * roic_s
    )

    quality_power = 1.30
    return clamp(100.0 * (base_quality / 100.0) ** quality_power)


def calculate_book_value_metrics(price, fundamental):
    """Returnér bogført værdi, bogført kurs og præmie fra balanceposter."""
    fundamental = fundamental or {}
    assets = parse_float(fundamental.get("total_assets"), None)
    liabilities = parse_float(fundamental.get("total_liabilities"), None)
    equity_reported = parse_float(fundamental.get("total_equity"), None)
    shares = parse_float(fundamental.get("shares_outstanding"), None)

    book_value = None
    if assets is not None and liabilities is not None:
        book_value = assets - liabilities
    elif equity_reported is not None:
        book_value = equity_reported

    book_price = None
    if book_value is not None and shares is not None and shares > 0:
        book_price = book_value / shares

    premium = None
    if price is not None and book_price is not None and book_price > 0:
        premium = price / book_price
    return book_value, book_price, premium


def market_cap_structure_score(market_cap, currency="USD", fx_to_dkk=1.0, usd_to_dkk=None):
    """Glidende 0-100 størrelsesscore fra Market Cap i USD.

    De redigerbare Market Cap-grænser bruges som knækpunkter, men scoren
    interpoleres logaritmisk mellem dem. Dermed får et selskab på fx 40 mia.
    USD en højere score end et selskab lige over 10 mia. USD, selv om begge
    tilhører TradingViews Large-kategori. Det fjerner det tidligere store
    spring og den meget brede 80-points-kasse.
    """
    import math

    cap = parse_float(market_cap, None)
    local_fx = parse_float(fx_to_dkk, None)
    usd_fx = parse_float(usd_to_dkk, None)
    if cap is None or cap <= 0:
        return 50.0
    if str(currency or "USD").upper() != "USD" and local_fx and usd_fx and usd_fx > 0:
        cap = cap * local_fx / usd_fx

    finite = sorted(
        [(float(upper), float(score)) for upper, _name, score in market_cap_limits_usd if upper is not None],
        key=lambda row: row[0],
    )
    terminal_score = next(
        (float(score) for upper, _name, score in market_cap_limits_usd if upper is None),
        100.0,
    )
    if not finite:
        return 50.0
    if cap <= finite[0][0]:
        return clamp(finite[0][1])

    for (lower_cap, lower_score), (upper_cap, upper_score) in zip(finite, finite[1:]):
        if cap <= upper_cap:
            fraction = (math.log(cap) - math.log(lower_cap)) / (math.log(upper_cap) - math.log(lower_cap))
            return clamp(lower_score + fraction * (upper_score - lower_score))

    # Fra sidste endelige grænse til Mega interpoleres videre over én dekade.
    # 10× sidste grænse eller mere giver terminalscoren.
    lower_cap, lower_score = finite[-1]
    upper_cap = lower_cap * 10.0
    if cap >= upper_cap:
        return clamp(terminal_score)
    fraction = (math.log(cap) - math.log(lower_cap)) / (math.log(upper_cap) - math.log(lower_cap))
    return clamp(lower_score + fraction * (terminal_score - lower_score))


def structure_layer_from_score(score):
    """Omsæt Strukturscore til en funktionel porteføljerolle.

    Fundament er bevidst gjort bredere, mens Accelerator er gjort smallere.
    Potentiale er bundlaget og påvirkes fortsat af den
    redigerbare Bull-straf.
    """
    value = parse_float(score, 0.0) or 0.0
    if value >= 70.0:
        return "Fundament"
    if value >= 56.0:
        return "Vækst"
    if value >= 40.0:
        return "Accelerator"
    return "Potentiale"


def _maturity_piecewise(value, points, default=65.0):
    """Lineær modenhedsscore mellem dokumenterede knækpunkter."""
    v = parse_float(value, None)
    if v is None:
        return default
    if v <= points[0][0]:
        return clamp(points[0][1])
    if v >= points[-1][0]:
        return clamp(points[-1][1])
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        if x0 <= v <= x1:
            fraction = (v - x0) / (x1 - x0) if x1 != x0 else 0.0
            return clamp(y0 + fraction * (y1 - y0))
    return default


def financial_maturity_score(fundamental):
    """0-100 score for dokumenteret finansiel modenhed.

    Modenhed måler stabil, positiv drift og balancesundhed i stedet for blot
    at gentage Kvalitetsscorens vækstprofil. Manglende data er neutralt 65,
    mens negativ drift eller negativ egenkapital straffes tydeligt.
    """
    fundamental = fundamental or {}
    ebit = _maturity_piecewise(
        fundamental.get("ebit_margin_ttm"),
        [(-10.0, 0.0), (0.0, 45.0), (5.0, 65.0), (10.0, 80.0), (20.0, 95.0), (30.0, 100.0)],
    )
    fcf = _maturity_piecewise(
        fundamental.get("fcf_margin_ttm"),
        [(-10.0, 0.0), (0.0, 45.0), (5.0, 65.0), (10.0, 80.0), (20.0, 95.0), (30.0, 100.0)],
    )
    roic = _maturity_piecewise(
        fundamental.get("roic"),
        [(-5.0, 0.0), (0.0, 30.0), (5.0, 55.0), (10.0, 75.0), (20.0, 95.0), (30.0, 100.0)],
    )

    assets = parse_float(fundamental.get("total_assets"), None)
    equity = parse_float(fundamental.get("total_equity"), None)
    if equity is None:
        liabilities = parse_float(fundamental.get("total_liabilities"), None)
        if assets is not None and liabilities is not None:
            equity = assets - liabilities
    equity_ratio = (equity / assets * 100.0) if assets and assets > 0 and equity is not None else None
    balance = _maturity_piecewise(
        equity_ratio,
        [(-10.0, 0.0), (0.0, 20.0), (10.0, 50.0), (25.0, 75.0), (40.0, 90.0), (60.0, 100.0)],
    )

    return clamp(0.35 * ebit + 0.30 * fcf + 0.20 * roic + 0.15 * balance)


def calculate_structure_score(fundamental, raw_row, quality_score, robustness, bull_pct=None):
    """Beregn virksomhedens rolle i porteføljen – ikke dens købsværdighed.

    Strukturmotoren bruger 45% glidende selskabsstørrelse, 30% fundamental
    kvalitet, 15% finansiel modenhed og 10% kursrobusthed. Modenhed måler
    positiv drift og balancesundhed, så defensive, etablerede selskaber ikke
    fejlagtigt behandles som Accelerator alene på grund af lav vækst.

    Den redigerbare spekulationsstraf fra ekstreme Bull-forventninger
    fratrækkes uændret til sidst.
    """
    fundamental = fundamental or {}
    raw_row = raw_row or {}

    size_score = market_cap_structure_score(
        fundamental.get("market_cap"),
        currency=raw_row.get("currency", "USD"),
        fx_to_dkk=raw_row.get("fx_to_dkk", 1.0),
        usd_to_dkk=raw_row.get("usd_to_dkk", FALLBACK_FX_DKK["USD"]),
    )
    quality_component = 50.0 if quality_score is None else clamp(quality_score)
    robustness_component = 50.0 if robustness is None else clamp(robustness)
    financial_maturity = financial_maturity_score(fundamental)

    raw_score = clamp(
        0.45 * size_score
        + 0.30 * quality_component
        + 0.15 * financial_maturity
        + 0.10 * robustness_component
    )
    penalty = speculation_penalty_from_bull(bull_pct)
    return clamp(raw_score - penalty), raw_score, penalty, size_score, financial_maturity



def _date_from_tv_value(value):
    """Fortolk TradingView-dato som Unix-tid, ISO-dato eller ISO-datetime."""
    if value in (None, "", "-"):
        return None
    try:
        if isinstance(value, (int, float)) or str(value).strip().replace(".", "", 1).isdigit():
            stamp = float(value)
            if stamp > 10_000_000_000:  # millisekunder
                stamp /= 1000.0
            return datetime.fromtimestamp(stamp, tz=timezone.utc).date()
    except Exception:
        pass
    text = str(value).strip()
    for candidate in (text, text[:10]):
        try:
            return datetime.fromisoformat(candidate.replace("Z", "+00:00")).date()
        except Exception:
            continue
    return None


def days_until_tv_date(value):
    target_date = _date_from_tv_value(value)
    if target_date is None:
        return None
    days = (target_date - date.today()).days
    return days if days >= 0 else None


def _positive_target_values(point):
    """Returnér positive Bull/Base/Median/Bear-værdier fra en historikpost."""
    fields = ("bull_target", "base_target", "median_target", "bear_target")
    values = {}
    for field in fields:
        value = parse_float((point or {}).get(field), None)
        if value is not None and value > 0:
            values[field] = float(value)
    return values


def _mixed_target_units_signature(point):
    """Find et tydeligt enheds-outlier i en kursmålspost.

    Forureningstypen er eksempelvis HANZA 2026-07-29, hvor Base er ca. 182 SEK,
    mens Bull/Median/Bear er ca. 19 i en anden valuta. Ét felt skal ligge mindst
    faktor 5 fra de tre øvrige, og de tre øvrige skal selv være nogenlunde samlet.
    Dermed rammes normale brede analytikerspænd ikke.
    """
    values = _positive_target_values(point)
    if len(values) != 4:
        return None

    for outlier_field, outlier_value in values.items():
        peers = {field: value for field, value in values.items() if field != outlier_field}
        peer_values = list(peers.values())
        if min(peer_values) <= 0 or max(peer_values) / min(peer_values) > 2.5:
            continue
        peer_mid = sorted(peer_values)[1]
        ratio = max(outlier_value, peer_mid) / min(outlier_value, peer_mid)
        if 5.0 <= ratio <= 20.0:
            return {
                "outlier_field": outlier_field,
                "peer_fields": tuple(peers.keys()),
                "ratio": ratio,
            }
    return None


def _is_derived_from_polluted_point(source, candidate, signature):
    """Genkend en senere post skabt ved omregning af den forurenede post.

    De tre ensartede felter skal være ganget med omtrent samme valutafaktor,
    mens outlier-feltet stort set er uændret. Det er præcis mønstret 19 -> 182,
    18,9 -> 181 og 18,38 -> 176, mens Base forblev ca. 182,7.
    """
    source_values = _positive_target_values(source)
    candidate_values = _positive_target_values(candidate)
    if len(source_values) != 4 or len(candidate_values) != 4:
        return False

    outlier_field = signature["outlier_field"]
    old_anchor = source_values[outlier_field]
    new_anchor = candidate_values[outlier_field]
    if abs(new_anchor - old_anchor) > max(0.05, abs(old_anchor) * 0.02):
        return False

    factors = []
    for field in signature["peer_fields"]:
        old = source_values[field]
        new = candidate_values[field]
        if old <= 0 or new <= 0:
            return False
        factors.append(new / old)

    common_factor = sum(factors) / len(factors)
    if not (5.0 <= common_factor <= 20.0):
        return False
    if max(abs(factor - common_factor) / common_factor for factor in factors) > 0.02:
        return False

    # Efter omregningen skal de fire værdier være kommet over i samme skala.
    converted = list(candidate_values.values())
    return max(converted) / min(converted) <= 2.5


def _sanitize_target_history_data(data):
    """Fjern sikre enhedsforureninger samt alle ugyldige/ufuldstændige historikposter.

    Kun komplette poster med positiv kurs samt positive Bull/Base/Bear-mål
    bevares i JSON-filen. Derefter fjernes poster, hvor ingen af de tre mål
    er ændret mindst 2 % siden seneste bevarede post. Metadata for KM alder
    genopbygges alene fra den rensede historik.

    Det betyder blandt andet, at en gammel post med ``price: null`` ikke kan
    få programmet til fejlagtigt at tro, at en kursmålsændring er kendt.
    """
    if not isinstance(data, dict):
        return data, False

    positions = data.setdefault("positions", {})
    changed = False

    for entry in positions.values():
        if not isinstance(entry, dict):
            continue

        history = entry.get("history")
        if not isinstance(history, list):
            history = []
            entry["history"] = history
            changed = True

        # Regnskabsdatoer opdeles i:
        # - next_earnings_date: den aktuelle kommende dato, vist særskilt.
        # - earnings_events: kun passerede regnskaber, vist i historikken.
        # Ældre versioner gemte også fremtidige datoer i earnings_events; de
        # migreres automatisk til next_earnings_date ved indlæsning.
        earnings_events = entry.get("earnings_events")
        if not isinstance(earnings_events, list):
            earnings_events = []
            entry["earnings_events"] = earnings_events
            changed = True

        # Køb i købsvindue er beslutningsbegivenheder og holdes helt adskilt
        # fra kursmålsposterne, så de ikke påvirkes af 2 %-støjfilteret.
        buy_window_events = entry.get("buy_window_events")
        if not isinstance(buy_window_events, list):
            buy_window_events = []
            entry["buy_window_events"] = buy_window_events
            changed = True

        clean_buy_events = []
        seen_buy_events = set()
        for event in buy_window_events:
            if not isinstance(event, dict):
                continue
            event_date = _date_from_tv_value(event.get("date"))
            prev_shares = parse_float(event.get("previous_shares"), None)
            new_shares = parse_float(event.get("new_shares"), None)
            if event_date is None or prev_shares is None or new_shares is None or new_shares <= prev_shares:
                continue
            dedupe_key = (event_date.isoformat(), round(prev_shares, 8), round(new_shares, 8))
            if dedupe_key in seen_buy_events:
                continue
            seen_buy_events.add(dedupe_key)
            clean_event = dict(event)
            clean_event["date"] = event_date.isoformat()
            clean_event["type"] = "buy_window_purchase"
            clean_buy_events.append(clean_event)
        clean_buy_events.sort(key=lambda event: (
            str(event.get("date", "")),
            float(event.get("new_shares", 0.0) or 0.0),
        ))
        if clean_buy_events != buy_window_events:
            entry["buy_window_events"] = clean_buy_events
            changed = True

        # Almindelige køb og salg er selvstændige beslutningsbegivenheder og
        # må – ligesom købsvindue-køb – aldrig påvirke kursmålsstøjfilteret.
        trade_events = entry.get("trade_events")
        if not isinstance(trade_events, list):
            trade_events = []
            entry["trade_events"] = trade_events
            changed = True
        clean_trade_events = []
        seen_trade_events = set()
        for event in trade_events:
            if not isinstance(event, dict):
                continue
            event_date = _date_from_tv_value(event.get("date"))
            event_type = str(event.get("type", "")).lower().strip()
            prev_shares = parse_float(event.get("previous_shares"), None)
            new_shares = parse_float(event.get("new_shares"), None)
            if event_date is None or event_type not in ("buy", "sell") or prev_shares is None or new_shares is None:
                continue
            if event_type == "buy" and new_shares <= prev_shares:
                continue
            if event_type == "sell" and new_shares >= prev_shares:
                continue
            dedupe_key = (event_date.isoformat(), event_type, round(prev_shares, 8), round(new_shares, 8))
            if dedupe_key in seen_trade_events:
                continue
            seen_trade_events.add(dedupe_key)
            clean_event = dict(event)
            clean_event["date"] = event_date.isoformat()
            clean_event["type"] = event_type
            clean_trade_events.append(clean_event)
        clean_trade_events.sort(key=lambda event: (
            str(event.get("date", "")), str(event.get("type", "")),
            float(event.get("new_shares", 0.0) or 0.0),
        ))
        if clean_trade_events != trade_events:
            entry["trade_events"] = clean_trade_events
            changed = True

        today = date.today()
        clean_earnings = []
        future_dates = []
        seen_earnings_dates = set()
        for event in earnings_events:
            if not isinstance(event, dict):
                continue
            event_date = _date_from_tv_value(event.get("date"))
            if event_date is None:
                continue
            date_text = event_date.isoformat()
            if event_date < today:
                if date_text in seen_earnings_dates:
                    continue
                seen_earnings_dates.add(date_text)
                clean_earnings.append({"date": date_text, "type": "earnings"})
            else:
                future_dates.append(event_date)

        stored_next = _date_from_tv_value(entry.get("next_earnings_date"))
        if stored_next is not None:
            if stored_next < today:
                date_text = stored_next.isoformat()
                if date_text not in seen_earnings_dates:
                    clean_earnings.append({"date": date_text, "type": "earnings"})
                    seen_earnings_dates.add(date_text)
            else:
                future_dates.append(stored_next)

        clean_earnings.sort(key=lambda event: event["date"])
        next_date_text = min(future_dates).isoformat() if future_dates else None

        if clean_earnings != earnings_events:
            entry["earnings_events"] = clean_earnings
            changed = True
        if entry.get("next_earnings_date") != next_date_text:
            entry["next_earnings_date"] = next_date_text
            changed = True

        # 1) Find sikre valuta-/enhedsforureninger og deres afledte poster.
        remove_indexes = set()
        for index, point in enumerate(history):
            if not isinstance(point, dict):
                remove_indexes.add(index)
                continue

            signature = _mixed_target_units_signature(point)
            if not signature:
                continue

            remove_indexes.add(index)

            # Fjern også senere poster, der tydeligt er afledt af netop denne
            # forurening via en fælles valutakonvertering.
            for later_index in range(index + 1, len(history)):
                later = history[later_index]
                if isinstance(later, dict) and _is_derived_from_polluted_point(point, later, signature):
                    remove_indexes.add(later_index)

        without_pollution = [
            point
            for index, point in enumerate(history)
            if index not in remove_indexes and isinstance(point, dict)
        ]

        # 2) Fjern alle ufuldstændige poster fysisk fra JSON-filen.
        # En historikpost er kun brugbar, når Kurs samt Bull/Base/Bear er positive.
        complete_candidates = [point for point in without_pollution if _history_point_complete(point)]

        # 3) Fjern allerede gemte støjposter. Første komplette observation
        # bevares altid. Hver senere post sammenlignes med den seneste BEVAREDE
        # post, så flere små daglige udsving først bliver gemt, når den samlede
        # ændring faktisk når mindst 2 % i Bull, Base eller Bear.
        complete = []
        for point in complete_candidates:
            if not complete:
                complete.append(point)
                continue
            previous_kept = complete[-1]
            if _visible_targets_changed(
                _clean_absolute_targets(previous_kept),
                _clean_absolute_targets(point),
            ):
                complete.append(point)

        if complete != history:
            entry["history"] = complete
            changed = True

        # 4) Genopbyg metadata alene fra de komplette, støjfiltrerede poster.
        if complete:
            first = complete[0]
            latest = complete[-1]
            first_date = first.get("date") or today_key()

            # Find den seneste dokumenterede reelle ændring i de synlige mål.
            last_change_point = first
            previous = first
            actual_change_count = 0
            for point in complete[1:]:
                if _visible_targets_changed(
                    _clean_absolute_targets(previous),
                    _clean_absolute_targets(point),
                ):
                    actual_change_count += 1
                    last_change_point = point
                previous = point

            last_change_date = (
                (last_change_point.get("date") or first_date)
                if actual_change_count > 0
                else first_date
            )

            rebuilt_targets = {
                field: parse_float(latest.get(field), None)
                for field in ("bull_target", "base_target", "median_target", "bear_target")
            }

            rebuilt_values = {
                "targets": rebuilt_targets,
                "observation_start_date": first_date,
                "last_change_date": last_change_date,
                "change_date_known": actual_change_count > 0,
            }
            for field, value in rebuilt_values.items():
                if entry.get(field) != value:
                    entry[field] = value
                    changed = True
        else:
            reset_values = {
                "targets": {},
                "history": [],
                "observation_start_date": today_key(),
                "last_change_date": today_key(),
                "change_date_known": False,
            }
            for field, value in reset_values.items():
                if entry.get(field) != value:
                    entry[field] = value
                    changed = True

    return data, changed


def load_target_age_history():
    """Indlæs og rens samlet KM-alder og absolut kursmålshistorik."""
    try:
        if TARGET_AGE_FILE.exists():
            with TARGET_AGE_FILE.open("r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, dict):
                data.setdefault("positions", {})
                data["schema"] = "PORTEFOLJE_TARGET_HISTORY_V2"
                data, changed = _sanitize_target_history_data(data)
                if changed:
                    with TARGET_AGE_FILE.open("w", encoding="utf-8") as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)
                return data
    except Exception:
        pass
    return {"schema": "PORTEFOLJE_TARGET_HISTORY_V2", "positions": {}}


def save_target_age_history(data):
    try:
        data["schema"] = "PORTEFOLJE_TARGET_HISTORY_V2"
        data.setdefault("positions", {})
        data, _changed = _sanitize_target_history_data(data)
        with TARGET_AGE_FILE.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


def _clean_absolute_targets(targets):
    names = ("bull_target", "base_target", "median_target", "bear_target")
    clean = {}
    for name in names:
        value = parse_float((targets or {}).get(name), None)
        clean[name] = round(value, 8) if value is not None and value > 0 else None
    return clean


def _absolute_targets_changed(previous, current):
    """Sammenlign absolutte mål med lille tolerance mod datastøj."""
    for name in ("bull_target", "base_target", "median_target", "bear_target"):
        old = parse_float((previous or {}).get(name), None)
        new = parse_float((current or {}).get(name), None)
        if old is None and new is None:
            continue
        if old is None or new is None:
            return True
        tolerance = max(0.01, abs(old) * 0.0001)
        if abs(new - old) > tolerance:
            return True
    return False


def _history_point_complete(point):
    """True når alle syv viste historikværdier kan beregnes.

    De syv værdier er Kurs, Bull/Base/Bear mål samt de tre afledte
    procentmål. Procenterne kan beregnes, når kursen og de tre synlige
    absolutte mål er positive. Medianmålet er fortsat gemt internt, men er
    ikke længere et krav for en brugbar række i kursmålshistorikken.
    """
    price = parse_float((point or {}).get("price"), None)
    if price is None or price <= 0:
        return False
    for field in ("bull_target", "base_target", "bear_target"):
        value = parse_float((point or {}).get(field), None)
        if value is None or value <= 0:
            return False
    return True


def _complete_history_entries(entries):
    """Returnér kun historikposter, der kan vises med alle syv værdier."""
    return [point for point in (entries or []) if isinstance(point, dict) and _history_point_complete(point)]


def _visible_targets_changed(previous, current, minimum_change_pct=TARGET_HISTORY_MIN_CHANGE_PCT):
    """True når mindst ét synligt absolut kursmål ændres væsentligt.

    Bull, Base og Bear sammenlignes procentuelt med den seneste gemte
    historikpost. En ny post accepteres kun, når mindst ét mål ændres med
    ``minimum_change_pct`` eller mere. Små ændringer under grænsen betragtes
    som TradingView-støj og må hverken nulstille KM alder eller gemmes i JSON.

    Manglende værdier regnes fortsat som en ændring, men komplette
    historikposter kræver i praksis positive Bull/Base/Bear-mål.
    """
    threshold = max(0.0, float(minimum_change_pct)) / 100.0
    for name in ("bull_target", "base_target", "bear_target"):
        old = parse_float((previous or {}).get(name), None)
        new = parse_float((current or {}).get(name), None)
        if old is None or new is None:
            return old != new
        if old <= 0:
            return new != old
        relative_change = abs(new - old) / abs(old)
        if relative_change >= threshold:
            return True
    return False


def register_earnings_date_for_row(display_row, earnings_value):
    """Gem næste regnskabsdato særskilt og arkivér den først efter passage.

    ``next_earnings_date`` indeholder altid den aktuelle kommende dato.
    Når denne dato er passeret ved en senere programkørsel, flyttes den til
    ``earnings_events`` og bliver dermed en historisk regnskabsbegivenhed.
    """
    earnings_date = _date_from_tv_value(earnings_value)

    key = f"{str(display_row.get('exchange', '')).upper()}:{str(display_row.get('ticker', '')).upper()}"
    if key == ":":
        return earnings_date

    data = load_target_age_history()
    positions = data.setdefault("positions", {})
    entry = positions.get(key)
    today = date.today()
    if not isinstance(entry, dict):
        entry = {
            "exchange": str(display_row.get("exchange", "")).upper(),
            "ticker": str(display_row.get("ticker", "")).upper(),
            "name": str(display_row.get("name", "")),
            "observation_start_date": today_key(),
            "last_change_date": today_key(),
            "change_date_known": False,
            "targets": {},
            "history": [],
            "earnings_events": [],
            "next_earnings_date": None,
        }
        positions[key] = entry

    entry["name"] = str(display_row.get("name", entry.get("name", "")))
    events = entry.setdefault("earnings_events", [])
    changed = False

    # Arkivér den hidtil kendte næste dato, når den er passeret.
    stored_next = _date_from_tv_value(entry.get("next_earnings_date"))
    if stored_next is not None and stored_next < today:
        stored_text = stored_next.isoformat()
        if stored_text not in {
            str(event.get("date"))
            for event in events
            if isinstance(event, dict)
        }:
            events.append({"date": stored_text, "type": "earnings"})
            changed = True
        entry["next_earnings_date"] = None
        changed = True

    # Den nye TradingView-dato er den aktuelle næste regnskabsdato.
    if earnings_date is not None:
        new_text = earnings_date.isoformat()
        if earnings_date < today:
            # Robusthed ved forsinkede data: en allerede passeret dato går
            # direkte i historikken og må ikke stå som næste regnskab.
            if new_text not in {
                str(event.get("date"))
                for event in events
                if isinstance(event, dict)
            }:
                events.append({"date": new_text, "type": "earnings"})
                changed = True
            if entry.get("next_earnings_date") is not None:
                entry["next_earnings_date"] = None
                changed = True
        elif entry.get("next_earnings_date") != new_text:
            entry["next_earnings_date"] = new_text
            changed = True

    events.sort(key=lambda event: str(event.get("date", "")))
    if changed:
        save_target_age_history(data)
    return earnings_date


def _entry_has_history_content(entry):
    """True når aktien har kursmålsposter eller registrerede regnskaber."""
    if not isinstance(entry, dict):
        return False
    return bool(
        _complete_history_entries(entry.get("history", []))
        or entry.get("earnings_events")
        or entry.get("buy_window_events")
        or entry.get("trade_events")
        or entry.get("next_earnings_date")
    )


def _backfill_trade_events_from_current_snapshot(entry, snapshot):
    """Efterfyld handler fra samme dag, som blev registreret før data var klar.

    Et helt nyt køb kan blive gemt i porteføljen, før aktien har fået sit første
    komplette TradingView-snapshot. I så fald eksisterer handelsbegivenheden,
    men Kurs/Bear/Base/Bull kan være tomme. Når dagens første komplette snapshot
    senere etableres, udfyldes kun handler fra SAMME dato. Dermed får køb og salg
    samme komplette historik uden at en ældre handel fejlagtigt får senere data.
    """
    if not isinstance(entry, dict) or not isinstance(snapshot, dict) or not _history_point_complete(snapshot):
        return False

    snapshot_date = str(snapshot.get("date", ""))
    price = parse_float(snapshot.get("price"), None)
    bear_target = parse_float(snapshot.get("bear_target"), None)
    base_target = parse_float(snapshot.get("base_target"), None)
    bull_target = parse_float(snapshot.get("bull_target"), None)
    if not snapshot_date or price is None or price <= 0:
        return False

    def upside(target):
        if target is None or target <= 0:
            return None
        return (target / price - 1.0) * 100.0

    changed = False
    for event in entry.get("trade_events", []) or []:
        if not isinstance(event, dict) or str(event.get("date", "")) != snapshot_date:
            continue
        # Efterfyld kun manglende handelsdata. Allerede registrerede værdier
        # bevares, så en korrekt handel aldrig overskrives af et senere kald.
        replacements = {
            "price": price,
            "bear_target": bear_target,
            "base_target": base_target,
            "bull_target": bull_target,
            "bear_pct": upside(bear_target),
            "base_pct": upside(base_target),
            "bull_pct": upside(bull_target),
        }
        for field, value in replacements.items():
            if parse_float(event.get(field), None) is None and value is not None:
                event[field] = value
                changed = True
    return changed


def target_age_days_for_row(display_row, absolute_targets, observed_price=None):
    """Opdatér kursmålshistorik og returnér (alder, kendt ændringsdato).

    En ufuldstændig post må hverken vises, starte KM-alderen eller bruges som
    sammenligningsgrundlag. Når programmet første gang har Kurs samt komplette
    Bull/Base/Bear-mål, oprettes en komplet referencepost på dagens dato, og
    KM alder starter som +0. Først en senere komplet ændring på mindst 2 %
    i Bull, Base eller Bear gør datoen kendt og skifter visningen til 0.
    """
    values = _clean_absolute_targets(absolute_targets)
    price = parse_float(observed_price, None)
    current_point = {"date": today_key(), "price": price, **values}
    current_complete = _history_point_complete(current_point)

    # Uden nogen brugbar kursmålsregistrering kan KM alder ikke etableres.
    if all(value is None for value in values.values()) and not current_complete:
        return None, False

    key = f"{str(display_row.get('exchange', '')).upper()}:{str(display_row.get('ticker', '')).upper()}"
    data = load_target_age_history()
    positions = data.setdefault("positions", {})
    entry = positions.get(key)
    today = today_key()
    changed = False

    if not isinstance(entry, dict):
        entry = {
            "exchange": str(display_row.get("exchange", "")).upper(),
            "ticker": str(display_row.get("ticker", "")).upper(),
            "name": str(display_row.get("name", "")),
            "observation_start_date": today,
            "last_change_date": today,
            "change_date_known": False,
            "targets": values,
            "history": [current_point],
        }
        positions[key] = entry
        changed = True
    else:
        entry.setdefault("exchange", str(display_row.get("exchange", "")).upper())
        entry.setdefault("ticker", str(display_row.get("ticker", "")).upper())
        entry["name"] = str(display_row.get("name", entry.get("name", "")))
        entry.setdefault("observation_start_date", entry.get("last_change_date") or today)
        entry.setdefault("last_change_date", entry.get("observation_start_date") or today)
        entry.setdefault("change_date_known", False)
        history_entries = entry.setdefault("history", [])

        # Migrér eventuelle gamle V1-mål. Den migrerede post er bevidst
        # ufuldstændig uden kurs og bliver derfor skjult og ignoreret.
        old_targets = entry.get("targets") or {}
        if not history_entries and old_targets:
            migrated = _clean_absolute_targets({
                "bull_target": old_targets.get("target_high"),
                "base_target": old_targets.get("target_base"),
                "median_target": old_targets.get("target_median"),
                "bear_target": old_targets.get("target_low"),
            })
            history_entries.append({"date": entry["observation_start_date"], "price": None, **migrated})
            entry["targets"] = migrated
            changed = True

        complete_entries = _complete_history_entries(history_entries)

        if not complete_entries:
            # Gamle ufuldstændige registreringer kan ikke være startgrundlag.
            # Første komplette hentning etablerer derfor en ny reference i dag.
            if current_complete:
                entry["observation_start_date"] = today
                entry["last_change_date"] = today
                entry["change_date_known"] = False
                entry["targets"] = values
                if history_entries and history_entries[-1].get("date") == today:
                    history_entries[-1] = current_point
                else:
                    history_entries.append(current_point)
                changed = True
        elif current_complete:
            previous_point = complete_entries[-1]
            previous_targets = _clean_absolute_targets(previous_point)
            if _visible_targets_changed(previous_targets, values):
                entry["targets"] = values
                entry["last_change_date"] = today
                # Ændringer på selve første komplette observationsdag kan ikke
                # tidsfæstes nærmere og bevarer derfor +0. Først en ændring på
                # en senere dato gør KM-alderen kendt som 0.
                if not entry.get("change_date_known") and entry.get("observation_start_date") == today:
                    entry["change_date_known"] = False
                else:
                    entry["change_date_known"] = True
                if history_entries and history_entries[-1].get("date") == today:
                    history_entries[-1] = current_point
                else:
                    history_entries.append(current_point)
                changed = True
            elif history_entries and history_entries[-1].get("date") == today and not _history_point_complete(history_entries[-1]):
                # Samme dags ufuldstændige post må gerne erstattes af en komplet.
                history_entries[-1] = current_point
                changed = True

    # Gem altid den seneste komplette observation særskilt fra historikken.
    # Historikken er fortsat støjfiltreret og får kun nye rækker ved mindst 2 %
    # ændring i Bull/Base/Bear, mens current_snapshot bruges til dagens aktuelle
    # kurs og procentberegninger i både aktive tabeller og Watch list.
    if current_complete:
        current_snapshot = {
            "date": today,
            "price": price,
            **values,
        }
        if entry.get("current_snapshot") != current_snapshot:
            entry["current_snapshot"] = current_snapshot
            changed = True

        # Et nyt køb kan være registreret få øjeblikke før den første
        # dataopdatering. Efterfyld i så fald købets historikrække med netop
        # handelsdagens komplette snapshot, så køb og salg dokumenteres ens.
        if _backfill_trade_events_from_current_snapshot(entry, current_snapshot):
            changed = True

        if entry.get("last_observation_date") != today:
            entry["last_observation_date"] = today
            changed = True

        # Afsluttende afstemning: Watch list må aldrig kunne vise en aktuel
        # observation, som afviger mindst 2 % fra seneste historikpost, uden at
        # ændringen også registreres i kursmålshistorikken. Denne kontrol er
        # bevidst placeret efter opdateringen af current_snapshot og fungerer
        # som sikkerhedsnet for både aktive aktier og Watch list-aktier.
        history_entries = entry.setdefault("history", [])
        complete_entries = _complete_history_entries(history_entries)
        latest_history = complete_entries[-1] if complete_entries else None
        latest_targets = _clean_absolute_targets(latest_history) if latest_history else {}

        if latest_history is None or _visible_targets_changed(latest_targets, values):
            entry["targets"] = values
            entry["last_change_date"] = today

            # Første komplette observation er fortsat kun et dokumenteret
            # minimum (+0). En senere ændring får kendt KM-alder 0.
            if latest_history is None:
                entry["observation_start_date"] = today
                entry["change_date_known"] = False
            elif not entry.get("change_date_known") and entry.get("observation_start_date") == today:
                entry["change_date_known"] = False
            else:
                entry["change_date_known"] = True

            # Der gemmes højst én kursmålspost pr. dato. Er dagens række allerede
            # til stede med ældre værdier, erstattes den; ellers tilføjes en ny.
            today_indexes = [
                index for index, point in enumerate(history_entries)
                if isinstance(point, dict) and str(point.get("date", "")) == today
            ]
            if today_indexes:
                history_entries[today_indexes[-1]] = current_point
                # Fjern eventuelle ældre dubletter fra samme dato.
                for index in reversed(today_indexes[:-1]):
                    del history_entries[index]
            else:
                history_entries.append(current_point)
            changed = True

    if changed:
        save_target_age_history(data)

    complete_entries = _complete_history_entries(entry.get("history", []))
    if not complete_entries:
        return 0 if current_complete else None, False

    age_source = entry.get("last_change_date") if entry.get("change_date_known") else entry.get("observation_start_date")
    age_date = _date_from_tv_value(age_source)
    days = (date.today() - age_date).days if age_date is not None else None
    return days, bool(entry.get("change_date_known"))

def format_target_age_days(value, change_date_known):
    """Vis kendt alder præcist og ukendt alder som et dokumenteret minimum.

    Eksempler:
    - 3  = programmet observerede kursmålsændringen for 3 dage siden.
    - +5 = kursmålene har mindst været uændrede i 5 dage; den reelle alder er ukendt.

    Ved ukendt startdato vises minimumsalderen straks som +0, +1, +2 osv.
    Bindestreg bruges kun, når der ikke findes kursmålsdata.
    """
    try:
        if value is None:
            return "-"
        days = int(value)
        if change_date_known:
            return str(days)
        return f"+{days}"
    except Exception:
        return "-"


def format_days(value):
    try:
        return str(int(value)) if value is not None else "-"
    except Exception:
        return "-"


def make_cash_phase2_row(display_row):
    """Kontanter vises som nederste række i Fase 2 uden aktieanalyse."""
    out = dict(display_row)
    out.update({
        "rank": "",
        "exchange": "-",
        "ticker": "-",
        "name": CASH_NAME,
        "antal": "-",
        "price": "-",
        "currency": "DKK",
        "recommended_weight": "0,0%",
        "approved_buy_weight": "-",
        "shares_delta": "-",
        "is_cash": True,
        "data_warning": False,
    })
    for key in PHASE2_COLUMN_IDS:
        out.setdefault(key, "-")
        out.setdefault("sort_" + key, -999999)
    # De få meningsfulde kontantfelter bevares. Resten skal stå som '-'.
    for key in ("analyst_bull_pct", "analyst_base_pct", "analyst_median_pct", "analyst_bear_pct",
                "analyst_spread_pct", "confidence_score", "target_age_days", "days_to_earnings", "dividend_yield", "dividend_frequency", "dividend_last", "dividend_months", "dividend_payment_dkk", "trend_strength", "robustness",
                "quality_score", "stock_score", "structure_score", "structure_layer", "value_score", "region_score", "sector_score", "industry_score",
                "pe", "peg", "revenue_growth_3y", "ebit_margin_ttm", "roic", "fcf_margin_ttm",
                "fcf_growth_3y", "kurs_f2", "sma50", "sector", "industry", "country"):
        out[key] = "-"
        out["sort_" + key] = -999999
    out["sort_rank"] = 999999999
    out["sort_name"] = CASH_NAME.casefold()
    out["sort_recommended_weight"] = 0.0
    out["sort_shares_delta"] = -999999
    return out


def make_phase2_row(display_row, raw_row=None, fundamental=None, analyst_error=None):
    fundamental = fundamental or {}
    out = dict(display_row)
    if display_row.get("is_summary"):
        for key in PHASE2_COLUMN_IDS:
            out.setdefault(key, "")
            out.setdefault("sort_" + key, 0)
        out["recommended_weight"] = "100,0%"
        out["approved_buy_weight"] = "-"
        out["shares_delta"] = "0"
        for k in ("analyst_bull_pct", "analyst_base_pct", "analyst_median_pct", "analyst_bear_pct", "analyst_spread_pct", "confidence_score", "target_age_days", "days_to_earnings", "dividend_yield", "dividend_frequency", "dividend_last", "dividend_months", "dividend_payment_dkk"):
            out[k] = "-"
            out["sort_" + k] = -999999
        out["trend_strength"] = "-"
        out["robustness"] = "-"
        out["quality_score"] = "-"
        out["stock_score"] = "-"
        out["structure_score"] = "-"
        out["structure_layer"] = "-"
        out["value_score"] = "-"
        out["region_score"] = "-"
        out["sector_score"] = "-"
        out["industry_score"] = "-"
        out["sort_recommended_weight"] = 100.0
        out["sort_approved_buy_weight"] = -999999
        out["sort_shares_delta"] = 0
        out["sort_trend_strength"] = -999999
        out["sort_robustness"] = -999999
        out["sort_quality_score"] = -999999
        out["sort_confidence_score"] = -999999
        out["sort_stock_score"] = -999999
        out["sort_structure_score"] = -999999
        out["sort_structure_layer"] = ""
        out["sort_value_score"] = -999999
        out["sort_region_score"] = -999999
        out["sort_sector_score"] = -999999
        out["sort_industry_score"] = -999999
        return out
    price = raw_row.get("price_raw") if raw_row else parse_float(display_row.get("price"), None)
    kurs_f2 = parse_float(fundamental.get("kurs_f2"), None)
    if kurs_f2 is None:
        kurs_f2 = price
    analyst = analyst_scenario_values(
        fundamental,
        price,
        currency=(raw_row.get("currency") if raw_row else display_row.get("currency", "USD")),
        fx_to_dkk=(raw_row.get("fx_to_dkk", 1.0) if raw_row else 1.0),
        usd_to_dkk=(raw_row.get("usd_to_dkk", FALLBACK_FX_DKK["USD"]) if raw_row else FALLBACK_FX_DKK["USD"]),
    )
    # Base fra de nye scannerdata bruges også som den synlige 1Y-værdi i analyserne.
    analyst_raw = analyst.get("base")
    trend_strength = raw_row.get("trend_strength_raw") if raw_row else None
    robustness = raw_row.get("robustness_raw") if raw_row else None
    history_days = raw_row.get("history_days_raw") if raw_row else None
    analyst_data_warning = bool(analyst.get("invalid"))
    short_history_score_penalty = history_days is not None and history_days < 252
    # Kort aktiehistorik giver ikke længere lys rød datavarsling i Fase 2.
    # Datavarsling bruges nu kun ved reelt ugyldige analytikerscenarier.
    data_warning = analyst_data_warning
    potential_score = analyst_adjusted_potential_score(analyst)
    confidence_score = analyst_confidence_score(analyst)
    absolute_targets = _normalize_scenario_targets(
        fundamental,
        currency=(raw_row.get("currency") if raw_row else display_row.get("currency", "USD")),
        fx_to_dkk=(raw_row.get("fx_to_dkk", 1.0) if raw_row else 1.0),
        usd_to_dkk=(raw_row.get("usd_to_dkk", FALLBACK_FX_DKK["USD"]) if raw_row else FALLBACK_FX_DKK["USD"]),
    )
    # Premium web edition does not load or maintain price-target history.
    # Current Bear/Base/Bull targets from the daily cache are sufficient.
    target_age_days, target_age_date_known = None, False
    days_to_earnings = days_until_tv_date(fundamental.get("earnings_next_date"))
    dividend_yield = parse_float(fundamental.get("dividend_yield"), None)
    dividend_frequency = str(fundamental.get("dividend_frequency", "") or "").strip()
    dividend_last_date = fundamental.get("dividend_last_date")
    dividend_upcoming_anchor_date = fundamental.get("dividend_upcoming_anchor_date")
    dividend_schedule_anchor = dividend_last_date or dividend_upcoming_anchor_date
    dividend_months, dividend_month_numbers = dividend_month_schedule(dividend_schedule_anchor, dividend_frequency)
    dividend_payment_dkk = dividend_payment_amount_dkk(
        raw_row.get("value_raw") if raw_row else display_row.get("sort_value_dkk"),
        dividend_yield,
        dividend_frequency,
    )
    quality_score = calculate_quality_score(fundamental)
    structure_score, structure_score_before_penalty, speculation_penalty, structure_size_score, financial_maturity_score = calculate_structure_score(
        fundamental, raw_row, quality_score, robustness, analyst.get("bull")
    )
    structure_layer = structure_layer_from_score(structure_score)
    _book_value, _book_price, market_premium = calculate_book_value_metrics(price, fundamental)
    value_score = value_score_from_premium(market_premium)
    stock_score = None
    if potential_score is not None and trend_strength is not None and robustness is not None and quality_score is not None:
        # Kvalitetsbaseret model:
        # 1) Kvalitet er fundamentet og vægter 40%.
        # 2) Robusthed og Trendstyrke vurderer, om kvaliteten også viser sig
        #    i en stabil og positiv kursadfærd.
        # 3) Analytikerpotentiale × Tillid er kun en 15%-modifikator.
        #
        # Tillid fungerer fortsat som sandsynlighedsfaktor, men kun på
        # analytikerdelen. Ekstreme kursmål kan derfor ikke dominere hele scoren.
        trusted_potential = (
            (potential_score / 100.0)
            * (confidence_score / 100.0)
            * 100.0
        )
        stock_score = (
            0.40 * quality_score
            + 0.25 * robustness
            + 0.20 * trend_strength
            + 0.15 * trusted_potential
        )
        # Ugyldige TradingView-analytikerscenarier straffer ikke aktien:
        # potentialet er allerede beregnet på Base alene. Kort kurshistorik
        # kan fortsat reducere selve Aktiescore, men giver ikke datavarsling.
        if short_history_score_penalty:
            stock_score *= 0.65

    out.update({
        "recommended_weight": "-",
        "approved_buy_weight": "-",
        "shares_delta": "0",
        "analyst_bull_pct": format_plain_pct(analyst.get("bull")),
        "analyst_base_pct": format_plain_pct(analyst.get("base")),
        "analyst_median_pct": format_plain_pct(analyst.get("median")),
        "analyst_bear_pct": format_plain_pct(analyst.get("bear")),
        "analyst_spread_pct": "Ugyldigt" if analyst.get("invalid") else (format_pct(analyst.get("spread")).replace("+", "") if analyst.get("spread") is not None else "-"),
        "confidence_score": format_num(confidence_score, 0),
        "target_age_days": format_target_age_days(target_age_days, target_age_date_known),
        "days_to_earnings": format_days(days_to_earnings),
        "dividend_yield": (format_num(dividend_yield, 2) + "%") if dividend_yield is not None else "-",
        "dividend_frequency": dividend_frequency if dividend_frequency else "-",
        "dividend_last": format_dividend_last_month(dividend_last_date),
        "dividend_months": dividend_months,
        "dividend_payment_dkk": ((format_dkk(dividend_payment_dkk) + " DKK") if dividend_payment_dkk is not None else "-"),
        "dividend_month_numbers": dividend_month_numbers,
        "dividend_last_date_raw": dividend_last_date,
        "dividend_schedule_anchor_raw": dividend_schedule_anchor,
        "trend_strength": format_num(trend_strength, 0) if trend_strength is not None else "-",
        "robustness": format_num(robustness, 0) if robustness is not None else "-",
        "quality_score": format_num(quality_score, 0) if quality_score is not None else "-",
        "stock_score": format_num(stock_score, 1) if stock_score is not None else "-",
        "structure_score": format_num(structure_score, 0),
        "structure_layer": structure_layer,
        "value_score": format_num(value_score, 0),
        "region_score": "-",
        "sector_score": "-",
        "industry_score": "-",
        "region_group": mapped_region(fundamental.get("country", "-")),
        "sector_group": mapped_sector(fundamental.get("sector", "-")),
        "industry_group": normalized_industry(fundamental.get("industry", "-")),
        "market_premium_raw": market_premium,
        "structure_score_before_penalty": structure_score_before_penalty,
        "speculation_penalty_raw": speculation_penalty,
        "structure_market_cap_raw": fundamental.get("market_cap"),
        "structure_currency_raw": (raw_row.get("currency", "USD") if raw_row else display_row.get("currency", "USD")),
        "structure_fx_to_dkk_raw": (raw_row.get("fx_to_dkk", 1.0) if raw_row else 1.0),
        "structure_usd_to_dkk_raw": (raw_row.get("usd_to_dkk", FALLBACK_FX_DKK["USD"]) if raw_row else FALLBACK_FX_DKK["USD"]),
        "structure_quality_raw": quality_score,
        "structure_robustness_raw": robustness,
        "structure_financial_maturity_raw": financial_maturity_score,
        "structure_bull_raw": analyst.get("bull"),
        "bull_target_abs": absolute_targets.get("bull_target"),
        "base_target_abs": absolute_targets.get("base_target"),
        "median_target_abs": absolute_targets.get("median_target"),
        "bear_target_abs": absolute_targets.get("bear_target"),
        "pe": format_num(parse_float(fundamental.get("pe"), None), 1) if parse_float(fundamental.get("pe"), None) is not None else "-",
        "peg": format_num(parse_float(fundamental.get("peg"), None), 2) if parse_float(fundamental.get("peg"), None) is not None else "-",
        "revenue_growth_3y": format_plain_pct(fundamental.get("revenue_growth_3y")),
        "ebit_margin_ttm": format_plain_pct(fundamental.get("ebit_margin_ttm")),
        "roic": format_plain_pct(fundamental.get("roic")),
        "fcf_margin_ttm": format_plain_pct(fundamental.get("fcf_margin_ttm")),
        "fcf_growth_3y": format_plain_pct(fundamental.get("fcf_growth_3y")),
        "analyst_1y_upside_pct": format_plain_pct(analyst_raw),
        "kurs_f2": format_num(kurs_f2, 2),
        "sma50": format_num(raw_row.get("sma50_raw"), 2) if raw_row and raw_row.get("sma50_raw") is not None else "-",
        "sector": fundamental.get("sector", "-") or "-",
        "industry": fundamental.get("industry", "-") or "-",
        "country": fundamental.get("country", "-") or "-",
        "analyst_error": analyst_error or "",
        "data_warning": data_warning,
    })
    sort_map = {
        "recommended_weight": -999999,
        "approved_buy_weight": -999999,
        "shares_delta": 0,
        "analyst_bull_pct": analyst.get("bull") if analyst.get("bull") is not None else -999999,
        "analyst_base_pct": analyst.get("base") if analyst.get("base") is not None else -999999,
        "analyst_median_pct": analyst.get("median") if analyst.get("median") is not None else -999999,
        "analyst_bear_pct": analyst.get("bear") if analyst.get("bear") is not None else -999999,
        "analyst_spread_pct": analyst.get("spread") if analyst.get("spread") is not None and not analyst.get("invalid") else -999999,
        "confidence_score": confidence_score,
        "target_age_days": target_age_days if target_age_days is not None else -999999,
        "days_to_earnings": days_to_earnings if days_to_earnings is not None else -999999,
        "dividend_yield": dividend_yield if dividend_yield is not None else -999999,
        "dividend_frequency": dividend_frequency.casefold() if dividend_frequency else "",
        "dividend_last": (_date_from_tv_value(dividend_last_date).toordinal() if _date_from_tv_value(dividend_last_date) is not None else -999999),
        "dividend_months": (dividend_month_numbers[0] if dividend_month_numbers else -999999),
        "dividend_payment_dkk": dividend_payment_dkk if dividend_payment_dkk is not None else -999999,
        "trend_strength": trend_strength if trend_strength is not None else -999999,
        "robustness": robustness if robustness is not None else -999999,
        "quality_score": quality_score if quality_score is not None else -999999,
        "stock_score": stock_score if stock_score is not None else -999999,
        "structure_score": structure_score,
        "structure_layer": STRUCTURE_LAYER_ORDER.index(structure_layer),
        "value_score": value_score,
        "region_score": -999999,
        "sector_score": -999999,
        "industry_score": -999999,
        "pe": parse_float(fundamental.get("pe"), -999999),
        "peg": parse_float(fundamental.get("peg"), -999999),
        "revenue_growth_3y": parse_float(fundamental.get("revenue_growth_3y"), -999999),
        "ebit_margin_ttm": parse_float(fundamental.get("ebit_margin_ttm"), -999999),
        "roic": parse_float(fundamental.get("roic"), -999999),
        "fcf_margin_ttm": parse_float(fundamental.get("fcf_margin_ttm"), -999999),
        "fcf_growth_3y": parse_float(fundamental.get("fcf_growth_3y"), -999999),
        "analyst_1y_upside_pct": analyst_raw if analyst_raw is not None else -999999,
        "kurs_f2": kurs_f2 if kurs_f2 is not None else -999999,
        "sma50": raw_row.get("sma50_raw") if raw_row and raw_row.get("sma50_raw") is not None else -999999,
        "sector": str(out.get("sector", "")).casefold(),
        "industry": str(out.get("industry", "")).casefold(),
        "country": str(out.get("country", "")).casefold(),
    }
    for k, v in sort_map.items():
        out["sort_" + k] = v
    return out



def update_phase2_summary(summary, data_rows):
    """Udfyld den eksisterende øverste Fase 2-linje med meningsfulde nøgletal.

    Summer bruges for porteføljestørrelser, mens sammenlignelige aktienøgletal
    vises som almindelige gennemsnit af de aktier, der har gyldige data.
    Felter hvor en sum/gennemsnit ville være misvisende, forbliver '-'.
    """
    if not summary or not summary.get("is_summary"):
        return
    rows = [r for r in (data_rows or []) if not r.get("is_summary") and not is_cash_row(r)]

    def valid_values(key):
        vals = []
        for row in rows:
            value = parse_float(row.get("sort_" + key), None)
            if value is not None and value > -999998:
                vals.append(float(value))
        return vals

    def set_avg(key, formatter=lambda v: format_num(v, 1)):
        vals = valid_values(key)
        if vals:
            value = sum(vals) / len(vals)
            summary[key] = formatter(value)
            summary["sort_" + key] = value
        else:
            summary[key] = "-"
            summary["sort_" + key] = -999999

    def set_sum(key, formatter=lambda v: format_num(v, 1)):
        vals = valid_values(key)
        if vals:
            value = sum(vals)
            summary[key] = formatter(value)
            summary["sort_" + key] = value
        else:
            summary[key] = "-"
            summary["sort_" + key] = -999999

    # Summer: hele porteføljens størrelse / planlagte ændring.
    summary["weight"] = format_pct(sum(float(r.get("sort_weight", 0.0) or 0.0) for r in rows)).replace("+", "") if rows else "-"
    summary["sort_weight"] = sum(float(r.get("sort_weight", 0.0) or 0.0) for r in rows)
    set_sum("recommended_weight", lambda v: format_pct(v).replace("+", ""))
    set_sum("shares_delta", lambda v: f"{int(round(v)):+d}" if abs(v) >= 0.5 else "0")
    set_sum("dividend_payment_dkk", format_dkk)

    # Gennemsnit: sammenlignelige procenttal, scorer og fundamentale nøgletal.
    for key in ("analyst_bear_pct", "analyst_base_pct", "analyst_bull_pct", "dividend_yield",
                "revenue_growth_3y", "ebit_margin_ttm", "roic", "fcf_margin_ttm", "fcf_growth_3y"):
        set_avg(key, format_plain_pct)
    for key in ("confidence_score", "trend_strength", "robustness", "quality_score", "stock_score",
                "structure_score", "value_score", "region_score", "sector_score", "industry_score"):
        set_avg(key, lambda v: format_num(v, 1))
    set_avg("pe", lambda v: format_num(v, 1))
    set_avg("peg", lambda v: format_num(v, 2))

    # Datoer, kurser på tværs af valutaer, kategorier og købshukommelse summeres ikke.
    for key in ("approved_buy_weight", "target_position", "target_age_days", "days_to_earnings",
                "dividend_frequency", "dividend_last", "dividend_months", "structure_layer",
                "kurs_f2", "sma50", "sector", "industry", "country"):
        summary[key] = "-"
        summary["sort_" + key] = -999999


def format_large_value(value):
    """Kompakt visning af balanceværdier i selskabets rapporteringsenhed."""
    v = parse_float(value, None)
    if v is None:
        return "-"
    sign = "-" if v < 0 else ""
    a = abs(v)
    if a >= 1_000_000_000_000:
        return f"{sign}{a / 1_000_000_000_000:.2f} bio.".replace(".", ",")
    if a >= 1_000_000_000:
        return f"{sign}{a / 1_000_000_000:.2f} mia.".replace(".", ",")
    if a >= 1_000_000:
        return f"{sign}{a / 1_000_000:.1f} mio.".replace(".", ",")
    if a >= 1_000:
        return f"{sign}{a / 1_000:.1f} t.".replace(".", ",")
    return format_num(v, 0)


def format_factor(value):
    v = parse_float(value, None)
    if v is None:
        return "-"
    return f"{v:.2f}×".replace(".", ",")


def make_phase2b_row(display_row, fundamental=None):
    """Byg Fase 1B – Bogført værdi fra seneste offentliggjorte balance.

    Bogført værdi = Samlede aktiver - Samlede forpligtelser
    Bogført kurs = Bogført værdi / antal udestående aktier
    Præmie = Aktuel kurs / Bogført kurs

    Beregningen svarer til Book Value Per Share og Price-to-Book. Goodwill
    vises som en konkret balanceoplysning, men trækkes ikke fra, fordi denne
    fase bevidst viser den fulde regnskabsmæssige egenkapital.
    """
    fundamental = fundamental or {}
    out = dict(display_row)

    if display_row.get("is_summary"):
        for key in PHASE2B_COLUMN_IDS:
            out.setdefault(key, "")
            out.setdefault("sort_" + key, 0)
        out["name"] = "Fase 1B – Bogført værdi"
        out["weight"] = "100,0%"
        return out

    price = parse_float(display_row.get("price"), None)
    assets = parse_float(fundamental.get("total_assets"), None)
    liabilities = parse_float(fundamental.get("total_liabilities"), None)
    goodwill = parse_float(fundamental.get("goodwill"), None)
    equity_reported = parse_float(fundamental.get("total_equity"), None)
    shares = parse_float(fundamental.get("shares_outstanding"), None)

    # Samme fælles beregning bruges i Fase 1B og til Værdiscore i Fase 2.
    book_value, book_price, premium = calculate_book_value_metrics(price, fundamental)

    negative_book_value = book_value is not None and book_value <= 0
    out.update({
        "intrinsic_tangible_price": (
            "Negativ bogført værdi" if negative_book_value
            else (format_num(book_price, 2) if book_price is not None else "-")
        ),
        "market_premium": (
            "Ikke beregnelig" if negative_book_value
            else format_factor(premium)
        ),
        "total_assets": format_large_value(assets),
        "total_liabilities": format_large_value(liabilities),
        "goodwill": format_large_value(goodwill),
        "shares_outstanding": format_large_value(shares),
        "total_tangible_value": format_large_value(book_value),
        "intrinsic_warning": negative_book_value,
    })

    sort_values = {
        "intrinsic_tangible_price": book_price if book_price is not None else -999999,
        "market_premium": premium if premium is not None else -999999,
        "total_assets": assets if assets is not None else -999999,
        "total_liabilities": liabilities if liabilities is not None else -999999,
        "goodwill": goodwill if goodwill is not None else -999999,
        "shares_outstanding": shares if shares is not None else -999999,
        "total_tangible_value": book_value if book_value is not None else -999999,
    }
    for key, value in sort_values.items():
        out["sort_" + key] = value
    return out

def show_phase2b():
    phase2b_tree.delete(*phase2b_tree.get_children())
    for i, row in enumerate(phase2b_rows):
        values = [row.get(c, "") for c in PHASE2B_COLUMN_IDS]
        if row.get("is_summary"):
            tag = "summary"
        else:
            tag = "even" if i % 2 == 0 else "odd"
        phase2b_tree.insert("", "end", values=values, tags=(tag,))


def sort_phase2b_rows(col):
    global phase2b_rows, phase2b_current_sort, phase2b_descending
    if not phase2b_rows:
        return
    summary = phase2b_rows[0] if phase2b_rows[0].get("is_summary") else None
    data_rows = phase2b_rows[1:] if summary else phase2b_rows[:]
    if phase2b_current_sort == col:
        phase2b_descending = not phase2b_descending
    else:
        phase2b_current_sort = col
        phase2b_descending = False if col in ("rank", "ticker", "name", "currency") else True
    data_rows.sort(key=lambda x: x.get("sort_" + col, ""), reverse=phase2b_descending)
    phase2b_rows = ([summary] if summary else []) + data_rows
    update_phase2b_headers()
    show_phase2b()


def update_phase2b_headers():
    for col_id, title, _width in PHASE2B_COLUMNS:
        arrow = ""
        if col_id == phase2b_current_sort:
            arrow = " ▼" if phase2b_descending else " ▲"
        phase2b_tree.heading(col_id, text=title + arrow, command=lambda c=col_id: sort_phase2b_rows(c))



def phase2_analyst_color(row):
    """Returnér en kontinuerlig Fase 2/Watch list-farve ud fra Bear/Base/Bull.

    Base er hovedmotoren for grøn, Bull supplerer. Negativ Bear reducerer
    grøn styrke og tilfører varm/rød risiko.

    Farven afspejler desuden nærhed til programmets hårde salgsregel:
    Bull skal være mindst 2×|Bear|. Påvirkningen starter før grænsen,
    bliver kraftig omkring |Bear|/Bull = 0,50 og fortsætter med at stige,
    hvis Bear bliver endnu værre. Selve salgsreglen ændres ikke.
    """
    bull = parse_float(row.get("analyst_bull_pct"), None)
    base = parse_float(row.get("analyst_base_pct"), None)
    bear = parse_float(row.get("analyst_bear_pct"), None)
    if bull is None or base is None or bear is None:
        return None

    base_strength = max(0.0, min(1.0, base / 32.0))
    bull_strength = max(0.0, min(1.0, (bull - 18.0) / 52.0))
    bear_bonus = 0.10 * max(0.0, min(1.0, bear / 20.0))
    raw_green = max(0.0, min(1.0,
        0.68 * base_strength + 0.32 * bull_strength + bear_bonus
    ))

    bear_risk = max(0.0, min(1.0, (-bear) / 35.0))
    base_risk = max(0.0, min(1.0, (-base) / 20.0))

    # Kontinuerlig salgsregel-risiko.
    # Start allerede omkring ratio 0,22. Omkring 0,50 er påvirkningen kraftig,
    # men i modsætning til v7.53 fortsætter den videre efter grænsen.
    sell_proximity = 0.0
    sell_overshoot = 0.0
    if bull > 0 and bear < 0:
        ratio = abs(bear) / bull

        # Før-grænse: 0,22 -> 0,50 mappes blødt til 0 -> 1.
        pre = max(0.0, min(1.0, (ratio - 0.22) / 0.28))
        sell_proximity = pre * pre * (3.0 - 2.0 * pre)

        # Efter-grænse: fortsat stigende straf fra 0,50 til 1,00+.
        # 0,50 -> 0, 0,75 -> 0,5, 1,00 -> 1,0.
        sell_overshoot = max(0.0, min(1.0, (ratio - 0.50) / 0.50))

    green_penalty = (
        0.58 * (bear_risk ** 1.25)
        + 0.20 * base_risk
        + 0.50 * sell_proximity
        + 0.28 * sell_overshoot
    )
    green_strength = max(0.0, min(1.0, raw_green * (1.0 - green_penalty)))

    green_visual = green_strength ** 1.20
    green_alpha = 0.0 if green_visual <= 0 else 0.03 + 0.72 * green_visual

    red_alpha = (
        0.24 * bear_risk
        + 0.16 * base_risk
        + 0.40 * sell_proximity
        + 0.22 * sell_overshoot
    )

    green_target = (126, 205, 134)
    red_target = (244, 198, 198)

    r = 255 + (green_target[0] - 255) * green_alpha + (red_target[0] - 255) * red_alpha
    g = 255 + (green_target[1] - 255) * green_alpha + (red_target[1] - 255) * red_alpha
    b = 255 + (green_target[2] - 255) * green_alpha + (red_target[2] - 255) * red_alpha
    rgb = tuple(max(0, min(255, int(round(v)))) for v in (r, g, b))
    return "#%02x%02x%02x" % rgb

def phase2_watch_color_tag(row):
    """Opret dynamisk tag til den fælles kontinuerlige analytikerfarve."""
    color = phase2_analyst_color(row)
    if not color:
        return ""
    tag = "analyst_" + color[1:]
    try:
        phase2_tree.tag_configure(tag, background=color, foreground="black")
    except Exception:
        pass
    return tag

def phase2_buy_opportunity(row):
    """True ved det særlige dybgrønne købssignal i Fase 2.

    Begge betingelser skal være opfyldt samtidigt:
    1) det absolutte Bull-mål er større end 2 × det absolutte Bear-mål,
    2) aktuel kurs er højst Bear + den indstillede procent af spændet
       mellem Bull og Bear (eller lavere).

    Standard er 10 % af (Bull − Bear). Ved Bull=150 og Bear=100 bliver den
    øvre grænse derfor 100 + 10 % × 50 = 105. Grænsen kan ændres via knappen
    ved Kursmålets påvirkning. Ugyldige eller manglende værdier giver intet signal.
    """
    if row.get("data_warning") or row.get("upside_sell"):
        return False
    price = parse_float(row.get("sort_price"), None)
    bull_target = parse_float(row.get("bull_target_abs"), None)
    bear_target = parse_float(row.get("bear_target_abs"), None)
    if price is None or bull_target is None or bear_target is None:
        return False
    if price <= 0 or bull_target <= 0 or bear_target <= 0 or bull_target <= bear_target:
        return False
    window_pct = max(0.0, buy_window_above_bear_pct) / 100.0
    upper = bear_target + window_pct * (bull_target - bear_target)
    return bull_target > 2.0 * bear_target and price <= upper


def target_position_score(row):
    """0-1 score for hvor attraktiv kursen er inde i købsvinduet.

    1,0 ved eller under Bear-målet. Scoren falder glidende mod 0,0 ved den
    øvre købsvinduegrænse, som er Bear + den indstillede procent af
    (Bull − Bear). Dette er en intern delscore og vises ikke i Fase 2.
    """
    price = parse_float(row.get("sort_price"), None)
    bull_target = parse_float(row.get("bull_target_abs"), None)
    bear_target = parse_float(row.get("bear_target_abs"), None)
    if price is None or bull_target is None or bear_target is None or price <= 0 or bear_target <= 0 or bull_target <= bear_target:
        return 0.0
    if price <= bear_target:
        return 1.0
    upper = bear_target + max(0.0, buy_window_above_bear_pct) / 100.0 * (bull_target - bear_target)
    if upper <= bear_target or price >= upper:
        return 0.0
    return clamp((upper - price) / (upper - bear_target), 0.0, 1.0)


def target_potential_score(row):
    """Intern 0-1 mulighedsscore fra Bull (70 %) og Base (30 %).

    Bull-potentiale mættes ved +150 % og Base-potentiale ved +75 %. Det gør
    meget stærke cases i stand til at nå den maksimale faktor, mens mere
    moderate cases får en lavere faktor selv om de befinder sig i købsvinduet.
    """
    bull_pct = parse_float(row.get("analyst_bull_pct"), None)
    base_pct = parse_float(row.get("analyst_base_pct"), None)
    if bull_pct is None or base_pct is None:
        return 0.0
    bull_score = clamp(max(0.0, bull_pct) / 150.0, 0.0, 1.0)
    base_score = clamp(max(0.0, base_pct) / 75.0, 0.0, 1.0)
    return clamp(BUY_WINDOW_BULL_WEIGHT * bull_score + BUY_WINDOW_BASE_WEIGHT * base_score, 0.0, 1.0)


def target_weight_factor(row):
    """Dynamisk købsvinduefaktor med brugerdefineret maksimum.

    Maksimal faktor (standard 5×) er kun et loft. Den faktiske bonus afhænger
    af to interne forhold:
      • 70/30-vægtet Bull/Base-potentiale.
      • Hvor tæt kursen ligger på Bear inden for købsvinduet.

    Prisens nærhed til Bear justerer potentialescore fra 50 % ved vinduets
    yderkant til 100 % ved/under Bear. Skyderen Kursmålets påvirkning skalerer
    hele bonusdelen fra 0 til 100 %. Andre aktiers normale anbefaling ændres ikke.
    """
    if not row.get("buy_opportunity"):
        return 1.0
    potential = target_potential_score(row)
    proximity = target_position_score(row)
    opportunity_strength = clamp(potential * (0.50 + 0.50 * proximity), 0.0, 1.0)
    max_factor = max(1.0, float(buy_window_max_factor))
    return 1.0 + (max_factor - 1.0) * target_influence * opportunity_strength

def minimum_upside_sell_reason(row):
    """Returnér forklaring, hvis aktien bryder de to hårde upside-regler.

    Regler:
    1) Bull 1Y skal være mindst +20 %.
    2) Hvis Bear 1Y er negativ, skal Bull være mindst 2 × |Bear|.

    Manglende/ugyldige analytikerdata udløser ikke automatisk salg; de håndteres
    fortsat af programmets eksisterende datavarsling.
    """
    bull = parse_float(row.get("analyst_bull_pct"), None)
    bear = parse_float(row.get("analyst_bear_pct"), None)
    if bull is None:
        return ""

    reasons = []
    if bull < 20.0:
        reasons.append("Bull under +20 %")
    if bear is not None and bear < 0.0 and bull < 2.0 * abs(bear):
        reasons.append("Bull under 2×|Bear|")
    return " og ".join(reasons)


def apply_recommended_weights(phase2_data_rows, total_portfolio_value=None):
    """Beregn normal Anbefalet %PF og et separat, valgfrit købsvinduetillæg.

    Den normale porteføljefordeling beregnes og normaliseres præcis som før.
    Kursmålets påvirkning ændrer ikke disse normale vægte. Kun aktier i det
    særlige købsvindue kan få en højere midlertidig anbefaling, fra 1× til 5×
    den normale anbefaling. Derfor tvinges andre aktiers anbefaling ikke ned.
    """
    import math
    import statistics

    stock_weight_total = sum(parse_float(row.get("weight"), 0.0) or 0.0 for row in phase2_data_rows)
    region_actual = {category: 0.0 for category in REGION_CATEGORIES}
    sector_actual = {category: 0.0 for category in SECTOR_CATEGORIES}
    industry_actual = {}
    for row in phase2_data_rows:
        normalized_weight = ((parse_float(row.get("weight"), 0.0) or 0.0) / stock_weight_total * 100.0) if stock_weight_total > 0 else 0.0
        region_actual[row.get("region_group", "Andre lande")] = region_actual.get(row.get("region_group", "Andre lande"), 0.0) + normalized_weight
        sector_actual[row.get("sector_group", "Andre sektorer")] = sector_actual.get(row.get("sector_group", "Andre sektorer"), 0.0) + normalized_weight
        industry_name = row.get("industry_group") or normalized_industry(row.get("industry"))
        industry_actual[industry_name] = industry_actual.get(industry_name, 0.0) + normalized_weight

    # Industriscore følger samme sektorbaserede neutrale industrimål som Fase 3.
    industry_targets_dynamic = dynamic_industry_targets(phase2_data_rows)

    raw_scores = []
    for row in phase2_data_rows:
        try:
            stock_score = float(row.get("sort_stock_score", 0.0) or 0.0)
        except Exception:
            stock_score = 0.0
        if stock_score == -999999 or stock_score < 0:
            stock_score = 0.0
        value_score = parse_float(row.get("sort_value_score"), 100.0)
        region_group = row.get("region_group", "Andre lande")
        sector_group = row.get("sector_group", "Andre sektorer")
        region_score = allocation_balance_score(region_actual.get(region_group, 0.0), region_targets.get(region_group, 0.0))
        sector_score = allocation_balance_score(sector_actual.get(sector_group, 0.0), sector_targets.get(sector_group, 0.0))
        industry_name = row.get("industry_group") or normalized_industry(row.get("industry"))
        industry_score = industry_balance_score(industry_actual.get(industry_name, 0.0), industry_target_for(industry_name, industry_targets_dynamic), industry_name)
        value_factor = 1.0 - value_influence * (1.0 - value_score / 100.0)
        region_factor = 1.0 + region_influence * (region_score / 100.0 - 1.0)
        sector_factor = 1.0 + sector_influence * (sector_score / 100.0 - 1.0)
        industry_factor = 1.0 + industry_influence * (industry_score / 100.0 - 1.0)
        adjusted_score = stock_score * value_factor * region_factor * sector_factor * industry_factor
        row.update({
            "region_score": format_num(region_score, 0), "sector_score": format_num(sector_score, 0),
            "industry_score": format_num(industry_score, 0), "sort_region_score": region_score,
            "sort_sector_score": sector_score, "sort_industry_score": industry_score,
            "value_factor_raw": value_factor, "region_factor_raw": region_factor,
            "sector_factor_raw": sector_factor, "industry_factor_raw": industry_factor,
            "adjusted_weight_score_raw": adjusted_score,
        })
        raw_scores.append(adjusted_score)

    positive_scores = [score for score in raw_scores if score > 0]
    if positive_scores:
        center = statistics.median(positive_scores)
        spread = max(positive_scores) - min(positive_scores)
        scale = max(4.0, min(10.0, spread / 6.0 if spread > 0 else 6.0))
    else:
        center, scale = 50.0, 6.0

    weighting_scores = []
    eligible_count = 0
    for row, score in zip(phase2_data_rows, raw_scores):
        sell_reason = minimum_upside_sell_reason(row)
        row["sell_reason"] = sell_reason
        row["upside_sell"] = bool(sell_reason)
        if sell_reason:
            weighting_scores.append(0.0)
            continue
        eligible_count += 1
        if score <= 0:
            weighting_scores.append(0.0)
            continue
        logistic = 1.0 / (1.0 + math.exp(-(score - center) / scale))
        weighting_scores.append(0.10 + 0.90 * logistic)

    total_score = sum(weighting_scores)
    fallback_equal = total_score <= 0 and eligible_count > 0

    for row, weighting_score in zip(phase2_data_rows, weighting_scores):
        # Købsvinduet vurderes efter Sælg-reglen er kendt.
        row["buy_opportunity"] = phase2_buy_opportunity(row)
        if row.get("upside_sell"):
            normal_recommended = 0.0
            recommended = 0.0
            row["recommended_weight"] = f"Sælg – {row['sell_reason']}"
        else:
            if fallback_equal:
                normal_recommended = 100.0 / eligible_count
            elif total_score > 0:
                normal_recommended = weighting_score / total_score * 100.0
            else:
                normal_recommended = 0.0
            factor = target_weight_factor(row)
            recommended = min(100.0, normal_recommended * factor)
            row["target_position_score_raw"] = target_position_score(row)
            row["target_factor_raw"] = factor
            row["normal_recommended_weight_raw"] = normal_recommended
            if row.get("buy_opportunity"):
                row["recommended_weight"] = "Køb – " + format_pct(recommended).replace("+", "")
            else:
                row["recommended_weight"] = format_pct(recommended).replace("+", "")
        row["sort_recommended_weight"] = recommended

    # Registrér først nu købsvindue-hukommelsen, så både Sælg og købssignal er kendt.
    update_buy_window_memory(phase2_data_rows)

    stock_value = sum(float(row.get("sort_value_dkk", 0.0) or 0.0) for row in phase2_data_rows)
    total_value = float(total_portfolio_value) if total_portfolio_value is not None else stock_value
    tolerance_pct_point = 0.05
    for row in phase2_data_rows:
        recommended = float(row.get("sort_recommended_weight", 0.0) or 0.0)
        current_shares = int(round(float(row.get("sort_antal", 0.0) or 0.0)))
        current_weight = float(row.get("sort_weight", 0.0) or 0.0)
        value_dkk = float(row.get("sort_value_dkk", 0.0) or 0.0)
        price_dkk = value_dkk / current_shares if current_shares > 0 else 0.0
        if row.get("upside_sell"):
            delta = -current_shares
        elif total_value <= 0 or price_dkk <= 0:
            delta = 0
        else:
            target_shares_raw = (recommended / 100.0 * total_value) / price_dkk
            lower = max(0, int(target_shares_raw // 1))
            upper = max(0, lower + 1)
            candidates = sorted(set([current_shares, lower, upper]))
            def weight_error(shares):
                return abs(shares * price_dkk / total_value * 100.0 - recommended)
            best_shares = min(candidates, key=lambda shares: (weight_error(shares), abs(shares - current_shares)))
            improvement = abs(current_weight - recommended) - weight_error(best_shares)
            delta = best_shares - current_shares if improvement > tolerance_pct_point else 0
        row["shares_delta"] = f"{delta:+d}" if delta != 0 else "0"
        row["sort_shares_delta"] = delta

def recalculate_value_weighting():
    """Genberegn Værdi-, Region-, Sektor- og Industriscore samt Anbefalet %PF uden datahentning."""
    data_rows = [r for r in phase2_rows if not r.get("is_summary") and not is_cash_row(r)]
    total_portfolio_value = sum(float(r.get("sort_value_dkk", 0.0) or 0.0) for r in phase2_rows if not r.get("is_summary"))
    if not data_rows:
        return
    for row in data_rows:
        premium = row.get("market_premium_raw")
        score = value_score_from_premium(premium)
        row["value_score"] = format_num(score, 0)
        row["sort_value_score"] = score
    apply_recommended_weights(data_rows, total_portfolio_value=total_portfolio_value)
    if phase2_rows and phase2_rows[0].get("is_summary"):
        update_phase2_summary(phase2_rows[0], data_rows)
    show_phase2()


def on_value_influence_change(value):
    global value_influence
    try:
        value_influence = max(0.0, min(1.0, float(value)))
    except Exception:
        return
    if "value_influence_label_var" in globals():
        value_influence_label_var.set(f"{value_influence:.2f}".replace(".", ","))
    save_value_settings()
    recalculate_value_weighting()


def on_region_influence_change(value):
    global region_influence
    try:
        region_influence = clamp(float(value), 0.0, 1.0)
    except Exception:
        return
    if "region_influence_label_var" in globals():
        region_influence_label_var.set(f"{region_influence:.2f}".replace(".", ","))
    save_allocation_settings()
    recalculate_value_weighting()


def on_sector_influence_change(value):
    global sector_influence
    try:
        sector_influence = clamp(float(value), 0.0, 1.0)
    except Exception:
        return
    if "sector_influence_label_var" in globals():
        sector_influence_label_var.set(f"{sector_influence:.2f}".replace(".", ","))
    save_allocation_settings()
    recalculate_value_weighting()


def on_target_influence_change(value):
    global target_influence
    try:
        target_influence = clamp(float(value), 0.0, 1.0)
    except Exception:
        return
    if "target_influence_label_var" in globals():
        target_influence_label_var.set(f"{target_influence:.2f}".replace(".", ","))
    save_allocation_settings()
    recalculate_value_weighting()


def on_industry_influence_change(value):
    global industry_influence
    try:
        industry_influence = clamp(float(value), 0.0, 1.0)
    except Exception:
        return
    if "industry_influence_label_var" in globals():
        industry_influence_label_var.set(f"{industry_influence:.2f}".replace(".", ","))
    save_allocation_settings()
    recalculate_value_weighting()


def open_target_buy_window_settings():
    """Indstil købsvinduets spændandel over Bear og maksimale bonusfaktor."""
    global buy_window_max_factor, buy_window_above_bear_pct
    win = tk.Toplevel(root)
    win.title("Indstil købsvindue")
    win.geometry("620x360")
    win.minsize(560, 330)
    win.transient(root)

    tk.Label(
        win,
        text=("Købsvinduet åbner kun når Bull-målet er større end 2 × Bear-målet. "
              "Her kan du styre hvor stor en procent af spændet Bull − Bear der lægges oven på Bear, "
              "og hvor høj den dynamiske bonusfaktor maksimalt må blive."),
        font=small_font, justify="left", wraplength=570, anchor="w",
    ).pack(fill="x", padx=16, pady=(16, 14))

    form = tk.Frame(win)
    form.pack(fill="x", padx=16)

    tk.Label(form, text="Maksimal bonusfaktor:", font=small_font, width=26, anchor="w").grid(row=0, column=0, sticky="w", pady=7)
    max_factor_var = tk.StringVar(value=format_num(buy_window_max_factor, 1))
    tk.Entry(form, textvariable=max_factor_var, width=10, justify="center", font=small_font).grid(row=0, column=1, sticky="w", pady=7)
    tk.Label(form, text="× normal Anbefalet %PF", font=small_font).grid(row=0, column=2, sticky="w", padx=(8, 0), pady=7)

    tk.Label(form, text="Andel af Bull−Bear spænd:", font=small_font, width=26, anchor="w").grid(row=1, column=0, sticky="w", pady=7)
    above_bear_var = tk.StringVar(value=format_num(buy_window_above_bear_pct, 1))
    tk.Entry(form, textvariable=above_bear_var, width=10, justify="center", font=small_font).grid(row=1, column=1, sticky="w", pady=7)
    tk.Label(form, text="%", font=small_font).grid(row=1, column=2, sticky="w", padx=(8, 0), pady=7)

    tk.Label(
        win,
        text=("Den maksimale faktor bruges ikke automatisk. Programmet beregner internt en glidende faktor "
              "ud fra Bull (70 %), Base (30 %) og hvor tæt kursen ligger på Bear. Derfor får en moderat "
              "case en lavere faktor end en meget stærk case, selv om begge er i købsvinduet."),
        font=small_font, justify="left", wraplength=570, anchor="w",
    ).pack(fill="x", padx=16, pady=(16, 8))

    def reset_defaults():
        max_factor_var.set(format_num(DEFAULT_BUY_WINDOW_MAX_FACTOR, 1))
        above_bear_var.set(format_num(DEFAULT_BUY_WINDOW_ABOVE_BEAR_PCT, 1))

    def save_settings():
        global buy_window_max_factor, buy_window_above_bear_pct
        try:
            max_factor = normalize_number(max_factor_var.get(), None)
            above_bear = normalize_number(above_bear_var.get(), None)
            if max_factor is None or not 1.0 <= max_factor <= 10.0:
                raise ValueError("Maksimal bonusfaktor skal ligge mellem 1,0× og 10,0×.")
            if above_bear is None or not 0.0 <= above_bear <= 50.0:
                raise ValueError("Andelen af Bull−Bear-spændet skal ligge mellem 0 % og 50 %.")
            buy_window_max_factor = float(max_factor)
            buy_window_above_bear_pct = float(above_bear)
            save_allocation_settings()
            update_target_influence_description()
            recalculate_value_weighting()
            win.destroy()
        except Exception as exc:
            messagebox.showerror("Ugyldige indstillinger", str(exc), parent=win)

    buttons = tk.Frame(win)
    buttons.pack(fill="x", padx=16, pady=16)
    tk.Button(buttons, text="Reset til standard", font=small_font, command=reset_defaults).pack(side="left")
    tk.Button(buttons, text="Annuller", font=small_font, command=win.destroy).pack(side="right")
    tk.Button(buttons, text="Gem og anvend", font=small_font, command=save_settings).pack(side="right", padx=(0, 8))


def update_target_influence_description():
    if "target_influence_description_var" in globals():
        target_influence_description_var.set(
            f"0 = ingen · 1 = dynamisk op til {format_num(buy_window_max_factor, 1)}× · "
            f"grænse = Bear + {format_num(buy_window_above_bear_pct, 1)} % af (Bull−Bear)"
        )


def open_industry_settings():
    """Indstil standardmålet pr. industri og eventuelle individuelle undtagelser."""
    global industry_default_target, industry_target_overrides
    win = tk.Toplevel(root)
    win.title("Indstil industrier")
    win.geometry("760x780")
    win.minsize(650, 560)
    win.transient(root)

    tk.Label(
        win,
        text=("Industriscore bruger TradingViews konkrete industri direkte. Standardmålet er en ønsket maksimal/neutral "
              "andel pr. industri og behøver derfor ikke summere til 100 %. En industri under målet løftes, mens koncentration over målet dæmpes."),
        font=small_font, anchor="w", justify="left", wraplength=720,
    ).pack(fill="x", padx=12, pady=(12, 8))

    default_bar = tk.Frame(win)
    default_bar.pack(fill="x", padx=12, pady=(0, 8))
    tk.Label(default_bar, text="Standardmål pr. industri:", font=small_font).pack(side="left")
    default_var = tk.StringVar(value=format_num(industry_default_target, 1))
    tk.Entry(default_bar, textvariable=default_var, font=small_font, width=10, justify="center").pack(side="left", padx=(8, 3))
    tk.Label(default_bar, text="%", font=small_font).pack(side="left")

    outer = tk.Frame(win)
    outer.pack(fill="both", expand=True, padx=12, pady=4)
    canvas = tk.Canvas(outer, highlightthickness=0)
    scroll = ttk.Scrollbar(outer, orient="vertical", command=canvas.yview)
    inner = tk.Frame(canvas)
    inner.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=inner, anchor="nw")
    canvas.configure(yscrollcommand=scroll.set)
    canvas.pack(side="left", fill="both", expand=True)
    scroll.pack(side="right", fill="y")

    current = {normalized_industry(r.get("industry")) for r in phase2_rows if not r.get("is_summary") and not is_cash_row(r)}
    current.discard("Industri ukendt")
    industries = sorted(set(DEFAULT_KNOWN_INDUSTRIES) | set(industry_target_overrides) | current, key=str.casefold)
    vars_by_industry = {}
    tk.Label(inner, text="Industri", font=small_font, width=38, anchor="w").grid(row=0, column=0, padx=5, pady=4, sticky="w")
    tk.Label(inner, text="Individuelt mål %", font=small_font).grid(row=0, column=1, padx=5, pady=4)
    tk.Label(inner, text="(tom = standard)", font=small_font).grid(row=0, column=2, padx=5, pady=4)
    for i, name in enumerate(industries, start=1):
        tk.Label(inner, text=name, font=small_font, width=38, anchor="w").grid(row=i, column=0, padx=5, pady=3, sticky="w")
        value = industry_target_overrides.get(name)
        var = tk.StringVar(value="" if value is None else format_num(value, 1))
        tk.Entry(inner, textvariable=var, font=small_font, width=12, justify="center").grid(row=i, column=1, padx=5, pady=3)
        vars_by_industry[name] = var

    def save_settings():
        global industry_default_target, industry_target_overrides
        try:
            default_value = normalize_number(default_var.get(), None)
            if default_value is None or not 0.1 <= default_value <= 25.0:
                raise ValueError("Standardmålet skal ligge mellem 0,1 % og 25,0 %.")
            overrides = {}
            for name, var in vars_by_industry.items():
                text = var.get().strip()
                if not text:
                    continue
                value = normalize_number(text, None)
                if value is None or not 0.0 <= value <= 25.0:
                    raise ValueError(f"Målet for {name} skal ligge mellem 0,0 % og 25,0 %.")
                overrides[name] = float(value)
            industry_default_target = float(default_value)
            industry_target_overrides = overrides
            save_allocation_settings()
            recalculate_value_weighting()
            win.destroy()
        except Exception as e:
            messagebox.showerror("Ugyldige indstillinger", str(e), parent=win)

    bar = tk.Frame(win)
    bar.pack(fill="x", padx=12, pady=12)
    tk.Button(bar, text="Nulstil standard", font=small_font, command=lambda: default_var.set(format_num(DEFAULT_INDUSTRY_TARGET, 1))).pack(side="left")
    tk.Button(bar, text="Annuller", font=small_font, command=win.destroy).pack(side="right")
    tk.Button(bar, text="Gem og anvend", font=small_font, command=save_settings).pack(side="right", padx=(0, 8))


def open_allocation_settings(kind):
    global region_targets, sector_targets, country_map, sector_map
    is_region = kind == "region"
    categories = REGION_CATEGORIES if is_region else SECTOR_CATEGORIES
    targets = region_targets if is_region else sector_targets
    mapping = country_map if is_region else sector_map
    defaults = DEFAULT_REGION_TARGETS if is_region else DEFAULT_SECTOR_TARGETS
    unknowns = sorted(unknown_country_values if is_region else unknown_sector_values)

    win = tk.Toplevel(root)
    win.title("Indstil regioner" if is_region else "Indstil sektorer")
    win.geometry("760x760")
    win.minsize(650, 560)
    win.transient(root)

    notebook_settings = ttk.Notebook(win)
    notebook_settings.pack(fill="both", expand=True, padx=10, pady=10)
    target_frame = tk.Frame(notebook_settings)
    map_frame = tk.Frame(notebook_settings)
    notebook_settings.add(target_frame, text="Målfordeling")
    notebook_settings.add(map_frame, text="Klassifikation")

    tk.Label(target_frame, text="Målene skal tilsammen give 100 %. Region-/Sektorscoren styrer retningen, mens skyderen styrer styrken.", font=small_font, anchor="w").pack(fill="x", padx=10, pady=10)
    target_entries = {}
    table = tk.Frame(target_frame)
    table.pack(anchor="n", padx=10, pady=5)
    for i, category in enumerate(categories):
        tk.Label(table, text=category, font=small_font, width=24, anchor="w").grid(row=i, column=0, padx=6, pady=4, sticky="w")
        var = tk.StringVar(value=format_num(targets.get(category, 0.0), 1))
        tk.Entry(table, textvariable=var, font=small_font, width=12, justify="center").grid(row=i, column=1, padx=6, pady=4)
        tk.Label(table, text="%", font=small_font).grid(row=i, column=2, sticky="w")
        target_entries[category] = var

    map_outer = tk.Frame(map_frame)
    map_outer.pack(fill="both", expand=True, padx=10, pady=10)
    canvas = tk.Canvas(map_outer, highlightthickness=0)
    scrollbar = ttk.Scrollbar(map_outer, orient="vertical", command=canvas.yview)
    map_inner = tk.Frame(canvas)
    map_inner.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=map_inner, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    all_raw = sorted(set(mapping.keys()) | set(unknowns), key=str.casefold)
    map_vars = {}
    for i, raw in enumerate(all_raw):
        tk.Label(map_inner, text=raw, font=small_font, width=32, anchor="w").grid(row=i, column=0, padx=6, pady=3, sticky="w")
        var = tk.StringVar(value=mapping.get(raw, categories[-1]))
        ttk.Combobox(map_inner, textvariable=var, values=categories, state="readonly", width=25).grid(row=i, column=1, padx=6, pady=3)
        map_vars[raw] = var

    def save_settings():
        global region_targets, sector_targets
        try:
            new_targets = {category: float(normalize_number(var.get(), None)) for category, var in target_entries.items()}
            total = sum(new_targets.values())
            if abs(total - 100.0) > 0.05:
                raise ValueError(f"Målfordelingen giver {format_num(total, 1)} %. Den skal give 100,0 %.")
            if any(v < 0 for v in new_targets.values()):
                raise ValueError("Målfordelinger må ikke være negative.")
            new_map = {raw: var.get() for raw, var in map_vars.items()}
            if is_region:
                region_targets = new_targets
                country_map.update(new_map)
                unknown_country_values.difference_update(new_map.keys())
            else:
                sector_targets = new_targets
                sector_map.update(new_map)
                unknown_sector_values.difference_update(new_map.keys())
            save_allocation_settings()
            # Opdater allerede hentede rækker med den nye klassifikation.
            for row in phase2_rows:
                if row.get("is_summary") or is_cash_row(row):
                    continue
                row["region_group"] = mapped_region(row.get("country"))
                row["sector_group"] = mapped_sector(row.get("sector"))
                row["industry_group"] = normalized_industry(row.get("industry"))
            recalculate_value_weighting()
            if phase3_current_view.startswith("Regioner"):
                show_phase3_regions()
            elif phase3_current_view.startswith("Sektorer"):
                show_phase3_sectors()
            win.destroy()
        except Exception as e:
            messagebox.showerror("Ugyldige indstillinger", str(e), parent=win)

    def reset_targets():
        for category, var in target_entries.items():
            var.set(format_num(defaults.get(category, 0.0), 1))

    bar = tk.Frame(win)
    bar.pack(fill="x", padx=10, pady=(0, 10))
    tk.Button(bar, text="Nulstil mål", font=small_font, command=reset_targets).pack(side="left")
    tk.Button(bar, text="Annuller", font=small_font, command=win.destroy).pack(side="right")
    tk.Button(bar, text="Gem og anvend", font=small_font, command=save_settings).pack(side="right", padx=(0, 8))


def open_value_score_settings():
    win = tk.Toplevel(root)
    win.title("Indstil Værdiscore")
    win.geometry("560x560")
    win.minsize(500, 480)
    win.transient(root)

    tk.Label(
        win,
        text="Præmie og Værdiscore. Programmet interpolerer lineært mellem punkterne.",
        font=small_font,
        anchor="w",
    ).pack(fill="x", padx=12, pady=(12, 8))

    table = tk.Frame(win)
    table.pack(fill="both", expand=True, padx=12)
    tk.Label(table, text="Præmie ×", font=small_font).grid(row=0, column=0, padx=8, pady=4)
    tk.Label(table, text="Værdiscore", font=small_font).grid(row=0, column=1, padx=8, pady=4)

    entries = []
    for i, (premium, score) in enumerate(value_score_points, start=1):
        p_var = tk.StringVar(value=format_num(premium, 2))
        s_var = tk.StringVar(value=format_num(score, 0))
        tk.Entry(table, textvariable=p_var, font=small_font, width=14, justify="center").grid(row=i, column=0, padx=8, pady=3)
        tk.Entry(table, textvariable=s_var, font=small_font, width=14, justify="center").grid(row=i, column=1, padx=8, pady=3)
        entries.append((p_var, s_var))

    def save_entries():
        global value_score_points
        try:
            points = []
            for p_var, s_var in entries:
                premium = normalize_number(p_var.get(), None)
                score = normalize_number(s_var.get(), None)
                if premium is None or score is None:
                    raise ValueError("Alle felter skal indeholde tal.")
                points.append([float(premium), float(score)])
            points.sort(key=lambda x: x[0])
            if any(points[i][0] >= points[i + 1][0] for i in range(len(points) - 1)):
                raise ValueError("Præmierne skal være strengt stigende.")
            if any(not 0.0 <= score <= 100.0 for _, score in points):
                raise ValueError("Værdiscore skal ligge mellem 0 og 100.")
            if any(points[i][1] < points[i + 1][1] for i in range(len(points) - 1)):
                raise ValueError("Værdiscoren skal være faldende eller uændret, når præmien stiger.")
            value_score_points = points
            save_value_settings()
            recalculate_value_weighting()
            win.destroy()
        except Exception as e:
            messagebox.showerror("Ugyldige indstillinger", str(e), parent=win)

    def reset_entries():
        for (p_var, s_var), (premium, score) in zip(entries, DEFAULT_VALUE_SCORE_POINTS):
            p_var.set(format_num(premium, 2))
            s_var.set(format_num(score, 0))

    buttons = tk.Frame(win)
    buttons.pack(fill="x", padx=12, pady=12)
    tk.Button(buttons, text="Nulstil standard", font=small_font, command=reset_entries).pack(side="left")
    tk.Button(buttons, text="Annuller", font=small_font, command=win.destroy).pack(side="right")
    tk.Button(buttons, text="Gem og anvend", font=small_font, command=save_entries).pack(side="right", padx=(0, 8))


def analyst_target_history():
    """Returnér den samlede absolutte kursmålshistorik fra KM-alder-filen."""
    return load_target_age_history()


def target_history_upside(entry, target_field):
    price = parse_float((entry or {}).get("price"), None)
    target = parse_float((entry or {}).get(target_field), None)
    if price is None or price <= 0 or target is None:
        return None
    return (target / price - 1.0) * 100.0


def first_history_upside(entries, target_field):
    """Rekonstruér første gyldige positive 1Y-procent fra mål og dagskurs."""
    for entry in entries or []:
        value = target_history_upside(entry, target_field)
        if value is not None and value > 0:
            return value
    return None

def portfolio_item_for_row(row):
    ex = str(row.get("exchange", "")).upper()
    ti = str(row.get("ticker", "")).upper()
    for item in portfolio:
        if item.get("exchange", "").upper() == ex and item.get("ticker", "").upper() == ti:
            return item
    return None





def format_goal_progress(progress_pct):
    """Vis procent af et oprindeligt 1Y%-mål som tal og grafisk bar.

    100% betyder, at Urealiseret % er lig med det valgte 1Y%-mål ved start.
    Baren fyldes op til 100%, mens tallet gerne må vise mere end 100%.
    """
    if progress_pct is None:
        return "-"
    try:
        value = float(progress_pct)
    except Exception:
        return "-"
    segments = 10
    filled = int(round(clamp(value, 0.0, 100.0) / 100.0 * segments))
    bar = "█" * filled + "░" * (segments - filled)

    # Fast tegnbredde giver ensartet visning ned gennem tabellen:
    # procenttallet højrestilles, og baren har altid samme længde.
    pct_text = f"{value:.0f}%".replace(".", ",")
    return f"{pct_text:>6}  {bar}"


def show_target_history_window(initial_key=None):
    """Vis aktiens samlede historik med kursmål, handler og regnskaber.

    Rullemenuen viser kun aktiens navn i alfabetisk orden. Børs og ticker
    bruges fortsat internt som entydig nøgle, men forstyrrer ikke visningen.
    """
    data = load_target_age_history()
    positions = data.get("positions", {})
    available = []
    for key, entry in positions.items():
        if _entry_has_history_content(entry):
            name = str(entry.get("name", "")).strip() or key
            available.append((name, key))
    available.sort(key=lambda pair: (pair[0].casefold(), pair[1].casefold()))
    if not available:
        messagebox.showinfo("Aktiens historik", "Der findes endnu ingen historik for aktierne.")
        return

    selected_index = 0
    normalized_initial_key = str(initial_key or "").upper().strip()
    if normalized_initial_key:
        selected_index = next(
            (index for index, (_name, key) in enumerate(available) if key.upper() == normalized_initial_key),
            0,
        )

    win = tk.Toplevel(root)
    win.title("Aktiens historik")
    win.geometry("1660x620")
    win.minsize(1200, 460)
    win.transient(root)

    top = tk.Frame(win)
    top.pack(fill="x", padx=10, pady=10)
    tk.Label(top, text="Aktie:", font=small_font).pack(side="left")
    choice = tk.StringVar(value=available[selected_index][0])
    combo = ttk.Combobox(
        top,
        textvariable=choice,
        values=[name for name, _key in available],
        state="readonly",
        width=42,
    )
    combo.current(selected_index)
    combo.set(available[selected_index][0])
    combo.pack(side="left", padx=(8, 12))
    # Sæt værdien igen, når vinduet er oprettet. Det får readonly-comboboxen
    # til visuelt at stå præcis som efter et manuelt valg i rullemenuen.
    win.after_idle(lambda: (combo.current(selected_index), combo.set(available[selected_index][0])))
    info_var = tk.StringVar()
    tk.Label(top, textvariable=info_var, font=small_font, anchor="w").pack(side="left", fill="x", expand=True)

    columns = [
        ("date", "Dato", 105), ("event", "Begivenhed", 390), ("price", "Kurs", 115),
        ("bear", "Bear mål", 105), ("base", "Base mål", 105),
        ("bull", "Bull mål", 105),
        ("bear_pct", "Bear % mål", 125), ("base_pct", "Base % mål", 125),
        ("bull_pct", "Bull % mål", 125),
    ]
    tree_hist = build_tree(win, columns, lambda c: None)

    def render(event=None):
        index = combo.current()
        if index < 0 or index >= len(available):
            index = 0
        _name, key = available[index]
        entry = positions.get(key, {})
        hist = _complete_history_entries(entry.get("history", []))
        earnings = [
            event for event in entry.get("earnings_events", [])
            if isinstance(event, dict)
            and (_date_from_tv_value(event.get("date")) or date.max) < date.today()
        ]
        buy_events = [
            event for event in entry.get("buy_window_events", [])
            if isinstance(event, dict) and _date_from_tv_value(event.get("date")) is not None
        ]
        trade_events = [
            event for event in entry.get("trade_events", [])
            if isinstance(event, dict) and _date_from_tv_value(event.get("date")) is not None
        ]

        # Når et almindeligt køb senere er blevet identificeret som et køb i
        # købsvinduet, vises kun den mere informative købsvindue-række.
        buy_window_keys = {
            (str(event.get("date", "")),
             round(float(event.get("previous_shares", 0.0) or 0.0), 8),
             round(float(event.get("new_shares", 0.0) or 0.0), 8))
            for event in buy_events
        }
        visible_trade_events = []
        for event in trade_events:
            trade_key = (
                str(event.get("date", "")),
                round(float(event.get("previous_shares", 0.0) or 0.0), 8),
                round(float(event.get("new_shares", 0.0) or 0.0), 8),
            )
            if str(event.get("type", "")).lower() == "buy" and trade_key in buy_window_keys:
                continue
            visible_trade_events.append(event)

        next_earnings = _date_from_tv_value(entry.get("next_earnings_date"))
        combined = [(str(point.get("date", "")), 0, "target", point) for point in hist]
        combined += [(str(event.get("date", "")), 1, "buy_window_purchase", event) for event in buy_events]
        combined += [(str(event.get("date", "")), 2, "trade", event) for event in visible_trade_events]
        combined += [(str(event.get("date", "")), 3, "earnings", event) for event in earnings]
        if next_earnings is not None:
            combined.append((next_earnings.isoformat(), 4, "next_earnings", {"date": next_earnings.isoformat()}))
        combined.sort(key=lambda row: (row[0], row[1]))

        tree_hist.delete(*tree_hist.get_children())
        for i, (_date_text, _order, event_type, point) in enumerate(combined):
            if event_type == "buy_window_purchase":
                shares_bought = parse_float(point.get("shares_bought"), None)
                weight_pct = parse_float(point.get("weight_pct"), None)
                event_text = "Køb i købsvindue"
                if shares_bought is not None:
                    event_text += f" · +{format_antal(shares_bought)} akt."
                if weight_pct is not None:
                    event_text += f" · {format_pct(weight_pct).replace('+', '')} PF"
                vals = [
                    point.get("date", "-"), event_text, format_num(point.get("price"), 2),
                    format_num(point.get("bear_target"), 2), format_num(point.get("base_target"), 2),
                    format_num(point.get("bull_target"), 2),
                    format_plain_pct(point.get("bear_pct")),
                    format_plain_pct(point.get("base_pct")),
                    format_plain_pct(point.get("bull_pct")),
                ]
            elif event_type == "trade":
                trade_type = str(point.get("type", "")).lower()
                shares_changed = parse_float(point.get("shares_changed"), None)
                event_text = "Køb" if trade_type == "buy" else "Salg"
                if shares_changed is not None:
                    sign = "+" if trade_type == "buy" else "−"
                    event_text += f" · {sign}{format_antal(shares_changed)} akt."
                vals = [
                    point.get("date", "-"), event_text, format_num(point.get("price"), 2),
                    format_num(point.get("bear_target"), 2), format_num(point.get("base_target"), 2),
                    format_num(point.get("bull_target"), 2),
                    format_plain_pct(point.get("bear_pct")),
                    format_plain_pct(point.get("base_pct")),
                    format_plain_pct(point.get("bull_pct")),
                ]
            elif event_type == "earnings":
                vals = [point.get("date", "-"), "Regnskab", "-", "-", "-", "-", "-", "-", "-"]
            elif event_type == "next_earnings":
                vals = [point.get("date", "-"), "Næste regnskab", "-", "-", "-", "-", "-", "-", "-"]
            else:
                vals = [
                    point.get("date", "-"), "Kursmål", format_num(point.get("price"), 2),
                    format_num(point.get("bear_target"), 2), format_num(point.get("base_target"), 2),
                    format_num(point.get("bull_target"), 2),
                    format_plain_pct(target_history_upside(point, "bear_target")),
                    format_plain_pct(target_history_upside(point, "base_target")),
                    format_plain_pct(target_history_upside(point, "bull_target")),
                ]
            tree_hist.insert("", "end", values=vals, tags=("even" if i % 2 == 0 else "odd",))
        known = "kendt" if entry.get("change_date_known") else "mindst kendt siden første observation"
        next_text = next_earnings.isoformat() if next_earnings is not None else "-"
        info_var.set(
            f"Næste regnskabsdato: {next_text} · "
            f"{len(hist)} kursmålsposter · {len(trade_events) + len(buy_events)} handler · {len(earnings)} tidligere regnskaber · "
            f"Seneste kursmålsændring: {entry.get('last_change_date', '-')} ({known})"
        )

    combo.bind("<<ComboboxSelected>>", render)
    render()


def show_selected_phase2_target_history():
    """Åbn historikken med markeret Fase 2-aktie som forvalg.

    Er ingen gyldig aktierække markeret, åbnes vinduet normalt, hvor den
    alfabetisk første aktie allerede står synligt i rullemenuen.
    """
    selected = phase2_tree.selection()
    if not selected:
        show_target_history_window()
        return

    item_id = selected[0]
    exchange = str(phase2_tree.set(item_id, "exchange") or "").upper().strip()
    ticker = str(phase2_tree.set(item_id, "ticker") or "").upper().strip()
    if not exchange or not ticker or exchange in ("-", CASH_EXCHANGE) or ticker in ("-", CASH_TICKER):
        show_target_history_window()
        return

    key = f"{exchange}:{ticker}"
    data = load_target_age_history()
    entry = data.get("positions", {}).get(key, {})
    if not _entry_has_history_content(entry):
        name = phase2_tree.set(item_id, "name") or ticker
        messagebox.showinfo("Aktiens historik", f"Der findes endnu ingen historik for {name}.")
        return

    show_target_history_window(initial_key=key)



def _latest_complete_target_point_for_key(key):
    """Returnér seneste aktuelle observation, ellers seneste historikpost.

    ``current_snapshot`` opdateres ved hver vellykket normal/forceret hentning,
    også når kursmålene er uændrede. Dermed får Watch list dagens kurs og
    Bull/Base/Bear-procenter uden at kursmålshistorikken fyldes med dagsstøj.
    """
    data = load_target_age_history()
    entry = data.get("positions", {}).get(str(key or "").upper(), {})
    if not isinstance(entry, dict):
        return None, {}
    snapshot = entry.get("current_snapshot")
    if isinstance(snapshot, dict) and _history_point_complete(snapshot):
        return snapshot, entry
    history = _complete_history_entries(entry.get("history", []))
    return (history[-1] if history else None), entry


def _remove_stock_from_json_files(key):
    """Slet en aktie helt fra programmets aktierelaterede JSON-filer."""
    global portfolio
    key = str(key or "").upper().strip()
    if ":" not in key:
        return
    exchange, ticker = key.split(":", 1)

    # Aktiv portefølje / positionshistorik.
    portfolio = [
        item for item in portfolio
        if is_cash_item(item) or position_key(item) != key
    ]
    save_portfolio(portfolio)

    # Permanent aktiekartotek.
    registry = load_stock_registry()
    registry.get("stocks", {}).pop(key, None)
    save_stock_registry(registry)

    # Kursmålshistorik og KM-alder.
    target_data = load_target_age_history()
    target_data.get("positions", {}).pop(key, None)
    save_target_age_history(target_data)

    # Dagens cache. Fjern både fase 1 og fase 2, uanset nøgleformat.
    cache = load_daily_cache()
    for section_name in ("phase1", "phase2"):
        section = cache.get(section_name, {})
        if not isinstance(section, dict):
            continue
        for cache_key in list(section):
            normalized = str(cache_key).upper().strip()
            cached = section.get(cache_key)
            cached_key = position_key(cached) if isinstance(cached, dict) else ""
            if normalized == key or cached_key == key or normalized in (ticker, f"{exchange}:{ticker}"):
                section.pop(cache_key, None)
    save_daily_cache(cache)


def _watchlist_fx_rates():
    """Returnér de bedste tilgængelige FX-kurser uden ekstra netkald.

    Watch list-opdateringen bruger TradingView Scanner til kursmålene, men
    normalisering af ikke-USD kursmål har også brug for valutakurser. Vi
    genbruger derfor dagens allerede hentede FX-cache og supplerer kun med
    programmets eksisterende fallback-værdier. Dermed gør åbning af Watch list
    ikke hovedprogrammets opstart langsommere.
    """
    cache = load_daily_cache()
    cached = cache.get("fx_rates", {}) if isinstance(cache, dict) else {}
    rates = dict(FALLBACK_FX_DKK)
    rates["DKK"] = 1.0
    if isinstance(cached, dict):
        for currency, value in cached.items():
            parsed = parse_float(value, None)
            if parsed is not None and parsed > 0:
                rates[str(currency).upper()] = parsed
    return rates


def open_edit_watchlist_window(parent=None, on_change=None):
    """Redigér Watch list uden at oprette kunstige køb i porteføljen.

    Watch list består af inaktive aktier i det permanente aktiekartotek.
    Nye kandidater gemmes direkte dér med active=False og kommer derfor aldrig
    omkring porteføljen eller handelsloggen.
    """
    parent = parent or root
    win = tk.Toplevel(parent)
    win.title("Rediger Watch list")
    win.geometry("1100x620")
    win.minsize(850, 500)
    win.transient(parent)
    win.grid_rowconfigure(0, weight=0)
    win.grid_rowconfigure(1, weight=1)
    win.grid_rowconfigure(2, weight=0)
    win.grid_columnconfigure(0, weight=1)

    exchange_var = tk.StringVar(value="NASDAQ")
    ticker_var = tk.StringVar()
    name_var = tk.StringVar()

    form = tk.LabelFrame(win, text="Tilføj / opdater potentiel aktie", font=small_font, padx=10, pady=8)
    form.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 8))
    tk.Label(form, text="Børs:", font=small_font).pack(side="left", padx=(0, 4))
    tk.Entry(form, textvariable=exchange_var, font=small_font, width=12).pack(side="left", padx=(0, 10))
    tk.Label(form, text="Ticker:", font=small_font).pack(side="left", padx=(0, 4))
    tk.Entry(form, textvariable=ticker_var, font=small_font, width=14).pack(side="left", padx=(0, 10))
    tk.Label(form, text="Navn:", font=small_font).pack(side="left", padx=(0, 4))
    tk.Entry(form, textvariable=name_var, font=small_font, width=42).pack(side="left", padx=(0, 10))

    frame = tk.Frame(win)
    frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 8))
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    columns = [("exchange", "Børs", 130), ("ticker", "Ticker", 150), ("name", "Navn", 620)]
    tree = ttk.Treeview(frame, columns=[c[0] for c in columns], show="headings")
    for col, title, width in columns:
        tree.heading(col, text=title)
        tree.column(col, width=width, anchor="w" if col == "name" else "center", stretch=(col == "name"))
    scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scroll.set)
    tree.grid(row=0, column=0, sticky="nsew")
    scroll.grid(row=0, column=1, sticky="ns")

    def refresh():
        tree.delete(*tree.get_children())
        for _label, key, entry in stock_registry_choices(include_active=False):
            tree.insert("", "end", iid=key, values=(
                str(entry.get("exchange", "")).upper(),
                str(entry.get("ticker", "")).upper(),
                str(entry.get("name", "")).strip() or str(entry.get("ticker", "")).upper(),
            ))

    def fill_fields(_event=None):
        selected = tree.selection()
        if not selected:
            return
        values = tree.item(selected[0], "values")
        if len(values) >= 3:
            exchange_var.set(values[0])
            ticker_var.set(values[1])
            name_var.set(values[2])

    def add_or_update():
        exchange = exchange_var.get().strip().upper()
        ticker = ticker_var.get().strip().upper()
        name = name_var.get().strip() or ticker
        if not exchange or not ticker:
            messagebox.showinfo("Manglende oplysninger", "Skriv mindst børs og ticker.", parent=win)
            return
        key = f"{exchange}:{ticker}"
        active_keys = {position_key(item) for item in portfolio if not is_cash_item(item)}
        if key in active_keys:
            messagebox.showinfo(
                "Aktien er allerede i porteføljen",
                f"{key} er aktiv i porteføljen og kan derfor ikke samtidig oprettes som Watch list-aktie.",
                parent=win,
            )
            return
        remember_stock({"exchange": exchange, "ticker": ticker, "name": name}, active=False)
        refresh()
        if callable(on_change):
            on_change()
        status_var.set(f"Tilføjet/opdateret direkte i Watch list: {key} – {name}")

    def delete_selected():
        selected = tree.selection()
        if not selected:
            messagebox.showinfo("Ingen valgt", "Vælg først en Watch list-aktie.", parent=win)
            return
        key = str(selected[0]).upper()
        values = tree.item(selected[0], "values")
        name = values[2] if len(values) >= 3 else key
        if not messagebox.askyesno(
            "Slet fra Watch list",
            f"Slet {name} ({key}) helt fra Watch list og aktiens gemte JSON-data?\n\nHandlingen kan ikke fortrydes.",
            parent=win,
        ):
            return
        _remove_stock_from_json_files(key)
        refresh()
        if callable(on_change):
            on_change()
        status_var.set(f"Slettet fra Watch list: {key}")

    tree.bind("<<TreeviewSelect>>", fill_fields)
    buttons = tk.Frame(win)
    buttons.grid(row=2, column=0, sticky="ew", padx=10, pady=(0, 10))
    tk.Button(buttons, text="Tilføj / opdater", font=small_font, command=add_or_update).pack(side="left")
    tk.Button(buttons, text="Slet valgt", font=small_font, command=delete_selected).pack(side="left", padx=(8, 0))
    tk.Label(
        buttons,
        text="Nye aktier oprettes direkte i Watch list og registreres ikke som køb/salg i porteføljen.",
        font=small_font,
        anchor="w",
    ).pack(side="left", padx=(18, 0), fill="x", expand=True)
    tk.Button(buttons, text="Luk", font=small_font, command=win.destroy).pack(side="right")
    refresh()




def _rotation_layer_distance(layer_a, layer_b):
    """Afstand mellem strukturlag i programmets naturlige rækkefølge."""
    try:
        return abs(STRUCTURE_LAYER_ORDER.index(str(layer_a)) - STRUCTURE_LAYER_ORDER.index(str(layer_b)))
    except Exception:
        return 99


def _rotation_role_similarity(candidate, current):
    """0-100 lighed i porteføljerolle.

    Rollematch holdes bevidst rent og bygger kun på faktuelle rollefelter:
    strukturlag 40 %, sektor 25 %, industri 25 % og region 10 %.
    Kvalitet indgår ikke i Rollematch; den vises og vurderes separat i
    rotationsreglen. Nærliggende strukturlag får delvis kredit.
    """
    score = 0.0
    cand_layer = str(candidate.get("structure_layer", ""))
    cur_layer = str(current.get("structure_layer", ""))
    distance = _rotation_layer_distance(cand_layer, cur_layer)
    if distance == 0:
        score += 40.0
    elif distance == 1:
        score += 22.0
    elif distance == 2:
        score += 8.0

    cand_sector = str(candidate.get("sector_group") or mapped_sector(candidate.get("sector", "-")))
    cur_sector = str(current.get("sector_group") or mapped_sector(current.get("sector", "-")))
    if cand_sector == cur_sector:
        score += 25.0

    cand_industry = str(candidate.get("industry_group") or normalized_industry(candidate.get("industry", "-")))
    cur_industry = str(current.get("industry_group") or normalized_industry(current.get("industry", "-")))
    if cand_industry == cur_industry and cand_industry != "Industri ukendt":
        score += 25.0
    elif cand_sector == cur_sector:
        # Samme sektor men anden industri kan stadig være en nært beslægtet rolle.
        score += 7.0

    cand_region = str(candidate.get("region_group") or mapped_region(candidate.get("country", "-")))
    cur_region = str(current.get("region_group") or mapped_region(current.get("country", "-")))
    if cand_region == cur_region:
        score += 10.0

    return clamp(score, 0.0, 100.0)


def _rotation_base_potential(row):
    """Direkte Base-potentiale i procent fra den aktuelle Fase 2-række."""
    return parse_float(row.get("analyst_base_pct"), None)


def _rotation_switch_margins(candidate, current, similarity):
    """Returnér konkrete marginer til de tre synlige Skift-krav.

    Positiv margin betyder, at kravet er opfyldt med den viste reserve.
    Negativ margin fortæller præcist, hvor meget der mangler.

    Skift-krav:
    - Udfordrerens Base-potentiale mindst 20 procentpoint højere.
    - Rollematch mindst 80.
    - Udfordrerens Kvalitet må højst være 10 point lavere.
    """
    candidate_base = _rotation_base_potential(candidate)
    current_base = _rotation_base_potential(current)
    potential_margin = None
    if candidate_base is not None and current_base is not None:
        potential_margin = (candidate_base - current_base) - 20.0

    role_margin = None if similarity is None else float(similarity) - 80.0

    candidate_quality = parse_float(candidate.get("sort_quality_score"), None)
    current_quality = parse_float(current.get("sort_quality_score"), None)
    quality_margin = None
    if (
        candidate_quality is not None and current_quality is not None
        and candidate_quality > -999998 and current_quality > -999998
    ):
        # Kravet er candidate_quality >= current_quality - 10.
        quality_margin = candidate_quality - current_quality + 10.0

    return potential_margin, role_margin, quality_margin


def _rotation_margin_text(value, decimals=0, suffix=""):
    """Vis en Skift-margin med eksplicit +/-, så retningen kan aflæses direkte."""
    v = parse_float(value, None)
    if v is None:
        return "-"
    text = f"{v:+.{int(decimals)}f}".replace(".", ",")
    return text + suffix


def _rotation_decision(candidate, current, similarity):
    """Beslutning ud fra gennemsigtige relative krav; Behold er standard.

    Skift:
      Base-potentiale mindst +20 pp bedre, Rollematch >=80, Kvalitet højst
      10 point lavere, samme strukturlag og ingen kandidat-advarsler.

    Overvej:
      Base-potentiale mindst +10 pp bedre og Rollematch >=70, mens samme
      kvalitets-, strukturlags- og datakrav som ved Skift skal være opfyldt.
    """
    potential_margin, role_margin, quality_margin = _rotation_switch_margins(candidate, current, similarity)
    candidate_sell = bool(minimum_upside_sell_reason(candidate))
    layer_ok = str(candidate.get("structure_layer", "")).strip() == str(current.get("structure_layer", "")).strip()
    quality_ok = quality_margin is not None and quality_margin >= 0.0
    candidate_ok = not candidate_sell and not candidate.get("data_warning")

    strong = (
        potential_margin is not None and potential_margin >= 0.0
        and role_margin is not None and role_margin >= 0.0
        and quality_ok and layer_ok and candidate_ok
    )
    possible = (
        potential_margin is not None and potential_margin >= -10.0
        and role_margin is not None and role_margin >= -10.0
        and quality_ok and layer_ok and candidate_ok
    )

    if strong:
        return "Skift", potential_margin, role_margin, quality_margin
    if possible:
        return "Overvej", potential_margin, role_margin, quality_margin
    return "Behold", potential_margin, role_margin, quality_margin


def _rotation_fx_rates_for_candidate(item, tv):
    """Brug dagens kendte FX først; efterhent kun det nødvendige til kandidaten."""
    cache = load_daily_cache()
    rates = dict(cache.get("fx_rates", {}) if isinstance(cache, dict) else {})
    rates.setdefault("DKK", 1.0)
    currency = currency_for_exchange(item.get("exchange"))
    needed = {currency, "USD"}
    missing = [c for c in needed if c not in rates]
    if missing:
        fetched, _fallback = fetch_fx_rates(tv, missing)
        rates.update(fetched)
    return rates


def _fetch_rotation_candidate(exchange, ticker, name=""):
    """Hent kandidaten med samme kurs-, fundamental- og scoremotor som Fase 2."""
    if TvDatafeed is None or Interval is None:
        raise RuntimeError("tvDatafeed er ikke installeret.")
    item = {
        "exchange": str(exchange or "").upper().strip(),
        "ticker": str(ticker or "").upper().strip(),
        "name": str(name or ticker).strip() or str(ticker),
        "antal": 0.0,
    }
    if not item["exchange"] or not item["ticker"]:
        raise ValueError("Børs og ticker skal udfyldes.")
    tv = TvDatafeed()
    fx_rates = _rotation_fx_rates_for_candidate(item, tv)
    raw = fetch_one(tv, item, fx_rates)
    if raw is None:
        raise RuntimeError(f"Ingen kursdata fundet for {item['exchange']}:{item['ticker']}.")
    fundamental = fetch_fundamental_row_from_tradingview_scanner(item)
    if not fundamental:
        raise RuntimeError(f"Ingen fundamentale TradingView-data fundet for {item['exchange']}:{item['ticker']}.")
    if fundamental.get("name"):
        item["name"] = str(fundamental.get("name"))
        raw["name"] = item["name"]
    display = make_display_row(raw, max(portfolio_total_value_dkk(), 1.0))
    candidate = make_phase2_row(display, raw, fundamental)
    candidate["upside_sell"] = bool(minimum_upside_sell_reason(candidate))
    candidate["buy_opportunity"] = phase2_buy_opportunity(candidate)
    return candidate


def open_rotation_analysis():
    """Fase 2: udfordr den investerede kapital med en ny potentiel aktie."""
    active_rows = [r for r in phase2_rows if not r.get("is_summary") and not is_cash_row(r)]
    if not active_rows:
        messagebox.showinfo("Rotationsanalyse", "Porteføljen skal være opdateret i Fase 2 først.")
        return

    win = tk.Toplevel(root)
    win.title("Rotationsanalyse – udfordr porteføljens kapital")
    # Brug hele skærmens bredde, så også de absolutte kursmål kan ses uden side-scroll.
    screen_width = max(1500, int(win.winfo_screenwidth()))
    screen_height = max(700, int(win.winfo_screenheight()))
    window_height = min(780, max(620, screen_height - 90))
    win.geometry(f"{screen_width}x{window_height}+0+20")
    win.minsize(1500, 620)
    win.transient(root)

    intro = (
        "Formål: Kan en ny aktie anvende den samme kapital bedre end en eksisterende position?  "
        "Behold er standard. Kolonnerne '... til Skift' viser marginen til Skift-kravet: positivt tal = kravet er opfyldt, "
        "negativt tal = så meget mangler. Skift kræver mindst +20 pp bedre Base-potentiale, Rollematch 80, "
        "Kvalitet højst 10 point lavere og samme Strukturlag. Overvej starter ved +10 pp og Rollematch 70."
    )
    tk.Label(win, text=intro, font=small_font, anchor="w", justify="left", wraplength=1680).pack(fill="x", padx=12, pady=(12, 6))

    input_frame = tk.Frame(win)
    input_frame.pack(fill="x", padx=12, pady=(2, 8))
    tk.Label(input_frame, text="Børs:", font=small_font).pack(side="left")
    exchange_var = tk.StringVar(value="NASDAQ")
    tk.Entry(input_frame, textvariable=exchange_var, width=12, font=small_font).pack(side="left", padx=(5, 12))
    tk.Label(input_frame, text="Ticker:", font=small_font).pack(side="left")
    ticker_var = tk.StringVar()
    ticker_entry = tk.Entry(input_frame, textvariable=ticker_var, width=14, font=small_font)
    ticker_entry.pack(side="left", padx=(5, 12))
    status = tk.StringVar(value="Indtast en potentiel aktie og tryk Analyser.")

    candidate_info = tk.StringVar(value="")
    tk.Label(win, textvariable=candidate_info, font=status_font, anchor="w", justify="left").pack(fill="x", padx=12, pady=(0, 6))

    # Kompakt bredde: vinduet bruger hele skærmbredden og kræver ingen vandret scrollbar.
    # Absolutte Kurs/Bear/Base/Bull står samlet umiddelbart før procentmålene.
    columns = [
        ("decision", "Note", 118),
        ("potential_to_switch", "Potentiale til Skift", 120),
        ("role_to_switch", "Rollematch til Skift", 126),
        ("quality_to_switch", "Kvalitet til Skift", 118),
        ("layer", "Strukturlag", 96),
        ("name", "Aktie", 160),
        ("sector", "Sektor", 108),
        ("industry", "Industri", 142),
        ("region", "Region", 100),
        ("price_abs", "Kurs", 68),
        ("bear_abs", "Bear", 68),
        ("base_abs", "Base", 68),
        ("bull_abs", "Bull", 68),
        ("bear", "Bear %", 66),
        ("base", "Base %", 66),
        ("bull", "Bull %", 66),
        ("quality", "Kvalitet", 68),
        ("stock_score", "Aktiescore", 76),
        ("value", "Værdi DKK", 88),
    ]
    numeric_columns = {
        "potential_to_switch", "role_to_switch", "quality_to_switch",
        "price_abs", "bear_abs", "base_abs", "bull_abs",
        "bear", "base", "bull", "quality", "stock_score", "value"
    }
    # Standardvisningen viser de cases, der er tættest på/over Skift-kravet, øverst.
    sort_column = "potential_to_switch"
    sort_descending = True

    table_frame = tk.Frame(win)
    table_frame.pack(fill="both", expand=True, padx=12, pady=(0, 8))
    tree = ttk.Treeview(table_frame, columns=[c[0] for c in columns], show="headings")

    def _sort_value(col_id, value):
        text = str(value or "").strip()
        if col_id in numeric_columns:
            if text in ("", "-"):
                return (1, 0.0)
            cleaned = text.replace("%", "").replace("pp", "").replace("+", "").replace(" ", "").replace(".", "").replace(",", ".")
            try:
                return (0, float(cleaned))
            except (TypeError, ValueError):
                return (1, 0.0)
        return (0, text.casefold())

    def update_headers():
        for col_id, title, _width in columns:
            arrow = ""
            if col_id == sort_column:
                arrow = " ▼" if sort_descending else " ▲"
            tree.heading(col_id, text=title + arrow, command=lambda c=col_id: sort_table(c))

    def sort_table(col_id):
        nonlocal sort_column, sort_descending
        if sort_column == col_id:
            sort_descending = not sort_descending
        else:
            sort_column = col_id
            sort_descending = False
        items = list(tree.get_children(""))
        items.sort(key=lambda item: _sort_value(col_id, tree.set(item, col_id)), reverse=sort_descending)
        for pos, item in enumerate(items):
            tree.move(item, "", pos)
        update_headers()

    for col, title, width in columns:
        anchor = "w" if col in ("decision", "name", "sector", "industry", "region") else "center"
        tree.column(col, width=width, minwidth=60, anchor=anchor, stretch=False)
    update_headers()

    yscroll = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=yscroll.set)
    tree.grid(row=0, column=0, sticky="nsew")
    yscroll.grid(row=0, column=1, sticky="ns")
    table_frame.grid_rowconfigure(0, weight=1)
    table_frame.grid_columnconfigure(0, weight=1)
    tree.tag_configure("challenger", background="#cfe8ff")
    tree.tag_configure("rotate", background="#b8dfb8")
    tree.tag_configure("consider", background="#fff0b8")
    tree.tag_configure("keep", background="#f3f3f3")

    explanation = tk.StringVar(value="")
    tk.Label(win, textvariable=explanation, font=small_font, anchor="w", justify="left", wraplength=1680).pack(fill="x", padx=12, pady=(0, 8))

    button_row = tk.Frame(win)
    button_row.pack(fill="x", padx=12, pady=(0, 12))

    def analyze():
        exchange = exchange_var.get().strip().upper()
        ticker = ticker_var.get().strip().upper()
        if not exchange or not ticker:
            messagebox.showwarning("Rotationsanalyse", "Udfyld både børs og ticker.", parent=win)
            return
        analyze_button.config(state="disabled")
        tree.delete(*tree.get_children())
        candidate_info.set("")
        explanation.set("")
        status.set(f"Henter og analyserer {exchange}:{ticker}...")

        def worker():
            candidate = None
            error = None
            try:
                candidate = _fetch_rotation_candidate(exchange, ticker)
            except Exception as exc:
                error = str(exc)

            def finish():
                analyze_button.config(state="normal")
                if error:
                    status.set("Rotationsanalysen kunne ikke gennemføres.")
                    messagebox.showerror("Rotationsanalyse", error, parent=win)
                    return

                candidate_region = str(candidate.get("region_group") or mapped_region(candidate.get("country", "-")))
                candidate_info.set(
                    f"Udfordrer: {candidate.get('name','-')} ({exchange}:{ticker})  |  "
                    f"{candidate.get('structure_layer','-')}  |  {candidate.get('sector','-')} / {candidate.get('industry','-')}  |  {candidate_region}  |  "
                    f"Bear {candidate.get('analyst_bear_pct','-')}  ·  Base {candidate.get('analyst_base_pct','-')}  ·  Bull {candidate.get('analyst_bull_pct','-')}  |  "
                    f"Kvalitet {candidate.get('quality_score','-')}  ·  Aktiescore {candidate.get('stock_score','-')}"
                )

                # Udfordreren er reference for de relative Skift-marginer. Derfor vises '-' i de tre kravkolonner.
                # Rækken er fortsat normal sortérbar og beholder sin blå farve.
                tree.insert("", "end", values=(
                    "Udfordreren",
                    "-",
                    "-",
                    "-",
                    candidate.get("structure_layer", "-"),
                    candidate.get("name", "-"),
                    candidate.get("sector", "-"),
                    candidate.get("industry", "-"),
                    candidate_region,
                    format_num(candidate.get("sort_price"), 2),
                    format_num(candidate.get("bear_target_abs"), 2),
                    format_num(candidate.get("base_target_abs"), 2),
                    format_num(candidate.get("bull_target_abs"), 2),
                    candidate.get("analyst_bear_pct", "-"),
                    candidate.get("analyst_base_pct", "-"),
                    candidate.get("analyst_bull_pct", "-"),
                    candidate.get("quality_score", "-"),
                    candidate.get("stock_score", "-"),
                    "-",
                ), tags=("challenger",))

                ranked = []
                for current in active_rows:
                    sim = _rotation_role_similarity(candidate, current)
                    decision, potential_margin, role_margin, quality_margin = _rotation_decision(candidate, current, sim)
                    ranked.append((decision, sim, potential_margin, role_margin, quality_margin, current))
                # De 10 mulige modstandere udvælges fortsat primært efter faktisk Rollematch.
                ranked.sort(key=lambda x: (
                    x[1],
                    x[2] if x[2] is not None else -9999,
                    x[4] if x[4] is not None else -9999,
                ), reverse=True)
                ranked = ranked[:10]

                for decision, sim, potential_margin, role_margin, quality_margin, current in ranked:
                    tag = "rotate" if decision == "Skift" else "consider" if decision == "Overvej" else "keep"
                    current_region = str(current.get("region_group") or mapped_region(current.get("country", "-")))
                    tree.insert("", "end", values=(
                        decision,
                        _rotation_margin_text(potential_margin, 1, " pp"),
                        _rotation_margin_text(role_margin, 0),
                        _rotation_margin_text(quality_margin, 0),
                        current.get("structure_layer", "-"),
                        current.get("name", "-"),
                        current.get("sector", "-"),
                        current.get("industry", "-"),
                        current_region,
                        format_num(current.get("sort_price"), 2),
                        format_num(current.get("bear_target_abs"), 2),
                        format_num(current.get("base_target_abs"), 2),
                        format_num(current.get("bull_target_abs"), 2),
                        current.get("analyst_bear_pct", "-"),
                        current.get("analyst_base_pct", "-"),
                        current.get("analyst_bull_pct", "-"),
                        current.get("quality_score", "-"),
                        current.get("stock_score", "-"),
                        current.get("value_dkk", "-"),
                    ), tags=(tag,))

                # Hvis brugeren allerede har valgt en sortering og analyserer igen, bevares den.
                if sort_column is not None:
                    items = list(tree.get_children(""))
                    items.sort(key=lambda item: _sort_value(sort_column, tree.set(item, sort_column)), reverse=sort_descending)
                    for pos, item in enumerate(items):
                        tree.move(item, "", pos)
                    update_headers()

                switch_rows = [x for x in ranked if x[0] == "Skift"]
                if switch_rows:
                    best = switch_rows[0]
                    old = best[5]
                    explanation.set(
                        f"Stærkeste Skift-case: sælg {old.get('name','-')} og anvend som udgangspunkt den frigjorte kapital "
                        f"({old.get('value_dkk','-')} DKK) på {candidate.get('name','-')}. "
                        f"Margin til krav: Potentiale {_rotation_margin_text(best[2],1, ' pp')}, Rollematch {_rotation_margin_text(best[3],0)}, Kvalitet {_rotation_margin_text(best[4],0)}. "
                        "Analysen udfører ingen handel; den udfordrer kun kapitalens nuværende placering."
                    )
                else:
                    explanation.set(
                        "Ingen eksisterende position opfylder alle Skift-krav. De tre 'til Skift'-kolonner viser direkte, "
                        "hvilke krav der allerede er opfyldt (+), og hvor meget der mangler (-)."
                    )
                status.set("Rotationsanalyse færdig. De 10 mest relevante porteføljemodstandere vises; klik på en kolonneoverskrift for at sortere.")
            root.after(0, finish)

        threading.Thread(target=worker, daemon=True).start()

    analyze_button = tk.Button(button_row, text="Analyser", font=status_font, command=analyze)
    analyze_button.pack(side="left")
    tk.Label(button_row, textvariable=status, font=small_font, anchor="w").pack(side="left", padx=(12, 0), fill="x", expand=True)
    tk.Button(button_row, text="Luk", font=small_font, command=win.destroy).pack(side="right")
    ticker_entry.focus_set()

def show_previous_stocks_window():
    """Vis Watch list med beslutningsfarver for mulige genkøb.

    Farverne prioriteres sådan:
    1) Base 1Y forecast under 20 % -> svag rød.
    2) Bull under 2 x den numeriske Bear-værdi -> svag rød uanset forecast.
    3) Base 20-30 % og godkendt Bull/Bear-forhold -> svag gul.
    4) Base 30-40 % og godkendt Bull/Bear-forhold -> svag grøn.
    5) Base mindst 40 % og godkendt Bull/Bear-forhold -> stærk grøn.

    Grænserne er sammenhængende: 20,0 % starter gul, 30,0 % starter
    svag grøn, og 40,0 % starter stærk grøn.
    """
    win = tk.Toplevel(root)
    win.title("Watch list")
    win.geometry("1470x720")
    win.minsize(1050, 520)
    win.transient(root)

    columns = [
        ("exchange", "Børs", 105),
        ("ticker", "Ticker", 105),
        ("name", "Navn", 280),
        ("price", "Kurs", 110),
        ("bear", "Bear", 110),
        ("base", "Base", 110),
        ("bull", "Bull", 110),
        ("bear_pct", "Bear %", 110),
        ("base_pct", "Base %", 110),
        ("bull_pct", "Bull %", 110),
        ("km_age", "KM alder", 90),
    ]

    outer = tk.Frame(win)
    outer.pack(fill="both", expand=True, padx=10, pady=(10, 6))

    # Watch list-sortering. Alle kolonner kan sorteres ved klik på overskriften.
    # Første klik sorterer stigende; næste klik på samme kolonne vender rækkefølgen.
    watch_sort_column = None
    watch_sort_descending = False
    numeric_watch_columns = {"price", "bull", "base", "bear", "bull_pct", "base_pct", "bear_pct", "km_age"}

    def _watch_sort_value(col_id, value):
        text = str(value or "").strip()
        if col_id in numeric_watch_columns:
            if text in ("", "-"):
                return (1, 0.0)
            cleaned = text.replace("%", "").replace("+", "").replace(" ", "").replace(",", ".")
            try:
                return (0, float(cleaned))
            except (TypeError, ValueError):
                return (1, 0.0)
        return (0, text.casefold())

    def update_watch_headers():
        for col_id, title, _width in columns:
            arrow = ""
            if col_id == watch_sort_column:
                arrow = " ▼" if watch_sort_descending else " ▲"
            tree.heading(col_id, text=title + arrow, command=lambda c=col_id: sort_watchlist(c))

    def sort_watchlist(col_id):
        nonlocal watch_sort_column, watch_sort_descending
        if watch_sort_column == col_id:
            watch_sort_descending = not watch_sort_descending
        else:
            watch_sort_column = col_id
            watch_sort_descending = False

        items = list(tree.get_children(""))
        items.sort(
            key=lambda item: _watch_sort_value(col_id, tree.set(item, col_id)),
            reverse=watch_sort_descending,
        )
        for pos, item in enumerate(items):
            tree.move(item, "", pos)
        update_watch_headers()

    tree = build_tree(outer, columns, sort_watchlist)
    update_watch_headers()
    tree.tag_configure("watch_red", background="#f7dddd")
    tree.tag_configure("watch_yellow", background="#fff3c4")
    tree.tag_configure("watch_green", background="#dff3df")
    tree.tag_configure("watch_strong_green", background="#a9dda9")

    row_by_item = {}

    def load_rows():
        tree.delete(*tree.get_children())
        row_by_item.clear()
        choices = stock_registry_choices(include_active=False)
        for index, (_label, key, registry_entry) in enumerate(choices):
            point, history_entry = _latest_complete_target_point_for_key(key)
            point = point or {}
            name = str(registry_entry.get("name", "")).strip() or str(history_entry.get("name", "")).strip() or key
            price = parse_float(point.get("price"), None)
            bull = parse_float(point.get("bull_target"), None)
            base = parse_float(point.get("base_target"), None)
            bear = parse_float(point.get("bear_target"), None)
            bull_pct = target_history_upside(point, "bull_target")
            base_pct = target_history_upside(point, "base_target")
            bear_pct = target_history_upside(point, "bear_target")
            age_source = history_entry.get("last_change_date") if history_entry.get("change_date_known") else history_entry.get("observation_start_date")
            age_date = _date_from_tv_value(age_source)
            age_days = (date.today() - age_date).days if age_date is not None else None
            km_age = format_target_age_days(age_days, bool(history_entry.get("change_date_known")))

            # Beslutningsfarven tager udgangspunkt i Base 1Y forecast.
            # Bull/Bear-forholdet er et overstyrende sikkerhedskrav og bruger
            # Bear numerisk, dvs. den absolutte størrelse også når Bear er negativ.
            if base_pct is None or bull_pct is None or bear_pct is None:
                tag = "even" if index % 2 == 0 else "odd"
            else:
                bull_bear_ok = bull_pct >= 2.0 * abs(bear_pct)
                if base_pct < 20.0 or not bull_bear_ok:
                    tag = "watch_red"
                elif base_pct < 30.0:
                    tag = "watch_yellow"
                elif base_pct < 40.0:
                    tag = "watch_green"
                else:
                    tag = "watch_strong_green"
            item_id = tree.insert("", "end", values=(
                str(registry_entry.get("exchange", "")).upper(),
                str(registry_entry.get("ticker", "")).upper(),
                name,
                format_num(price, 2),
                format_num(bear, 2),
                format_num(base, 2),
                format_num(bull, 2),
                format_plain_pct(bear_pct),
                format_plain_pct(base_pct),
                format_plain_pct(bull_pct),
                km_age,
            ), tags=(tag,))
            row_by_item[item_id] = {
                "key": key,
                "exchange": str(registry_entry.get("exchange", "")).upper(),
                "ticker": str(registry_entry.get("ticker", "")).upper(),
                "name": name,
            }

        # Bevar brugerens valgte sortering efter redigering eller dataopdatering.
        if watch_sort_column is not None:
            items = list(tree.get_children(""))
            items.sort(
                key=lambda item: _watch_sort_value(watch_sort_column, tree.set(item, watch_sort_column)),
                reverse=watch_sort_descending,
            )
            for pos, item in enumerate(items):
                tree.move(item, "", pos)
        update_watch_headers()

    def selected_row():
        selected = tree.selection()
        if not selected:
            messagebox.showinfo("Ingen valgt", "Vælg først en aktie i tabellen.", parent=win)
            return None
        return row_by_item.get(selected[0])

    def delete_all_about_stock():
        row = selected_row()
        if not row:
            return
        if not messagebox.askyesno(
            "Slet alt om aktien",
            f"Er du sikker på, at alt om {row['name']} ({row['key']}) skal slettes fra JSON-filerne?\n\nHandlingen kan ikke fortrydes.",
            parent=win,
        ):
            return
        _remove_stock_from_json_files(row["key"])
        load_rows()
        status_var.set(f"Alt om aktien er slettet fra JSON-filerne: {row['key']}")

    def show_selected_watchlist_target_history():
        row = selected_row()
        if not row:
            return
        data = load_target_age_history()
        entry = data.get("positions", {}).get(row["key"], {})
        if not _entry_has_history_content(entry):
            messagebox.showinfo(
                "Aktiens historik",
                f"Der findes endnu ingen historik for {row['name']}.",
                parent=win,
            )
            return
        show_target_history_window(initial_key=row["key"])

    def rebuy_stock():
        row = selected_row()
        if not row:
            return
        antal = simpledialog.askfloat(
            "Genkøb aktie",
            f"Hvor mange aktier af {row['name']} skal genkøbes?",
            parent=win,
            minvalue=0.0000001,
        )
        if antal is None:
            return
        existing = next((item for item in portfolio if position_key(item) == row["key"]), None)
        if existing:
            existing["antal"] = float(antal)
            existing["name"] = row["name"]
        else:
            portfolio.append({
                "exchange": row["exchange"],
                "ticker": row["ticker"],
                "name": row["name"],
                "antal": float(antal),
            })
        remember_stock({
            "exchange": row["exchange"],
            "ticker": row["ticker"],
            "name": row["name"],
        }, active=True)
        save_portfolio()
        load_rows()
        status_var.set(f"Genkøbt og oprettet i aktiv portefølje: {row['key']} – antal {format_antal(antal)}")

    buttons = tk.Frame(win)
    buttons.pack(fill="x", padx=10, pady=(0, 10))
    tk.Button(buttons, text="Rediger Watch list", font=small_font, command=lambda: open_edit_watchlist_window(win, load_rows)).pack(side="left")
    tk.Button(buttons, text="Slet alt om aktien", font=small_font, command=delete_all_about_stock).pack(side="left", padx=(8, 0))
    tk.Button(buttons, text="Genkøb aktie", font=small_font, command=rebuy_stock).pack(side="left", padx=(8, 0))
    tk.Button(buttons, text="Aktiens historik", font=small_font, command=show_selected_watchlist_target_history).pack(side="left", padx=(8, 0))

    watch_update_button = tk.Button(buttons, text="Opdater Watch list", font=small_font)
    watch_update_button.pack(side="left", padx=(8, 0))
    watch_force_button = tk.Button(buttons, text="Opdater Watch list forceret", font=small_font)
    watch_force_button.pack(side="left", padx=(8, 0))

    tk.Label(
        buttons,
        text=("Svag rød: Base <20 % eller Bull <2×|Bear|  ·  "
              "Svag gul: Base 20-30 %  ·  Svag grøn: Base 30-40 %  ·  "
              "Stærk grøn: Base ≥40 %"),
        font=small_font,
        anchor="w",
    ).pack(side="left", padx=(18, 0), fill="x", expand=True)
    tk.Button(buttons, text="Luk", font=small_font, command=win.destroy).pack(side="right")

    def start_watchlist_update(force_refresh=False, automatic=False):
        watch_update_button.config(state="disabled")
        watch_force_button.config(state="disabled")
        if automatic:
            status_var.set("Watch list åbnet – kontrollerer dagens Watch list-data...")
        else:
            status_var.set("Opdaterer Watch list forceret..." if force_refresh else "Opdaterer Watch list...")

        def worker():
            checked = updated = 0
            error = None
            try:
                checked, updated = update_archived_analyst_history(_watchlist_fx_rates(), force_refresh=force_refresh)
            except Exception as exc:
                error = exc

            def finish():
                if not win.winfo_exists():
                    return
                watch_update_button.config(state="normal")
                watch_force_button.config(state="normal")
                load_rows()
                if error is not None:
                    status_var.set(f"Watch list-opdatering fejlede: {error}")
                elif checked:
                    mode = "Forceret Watch list-opdatering" if force_refresh else "Watch list-opdatering"
                    status_var.set(f"{mode} færdig. Kontrolleret: {checked}, kursmålsændringer: {updated}")
                else:
                    status_var.set("Watch list er allerede opdateret i dag – gemte data genbrugt.")
            root.after(0, finish)

        threading.Thread(target=worker, daemon=True).start()

    watch_update_button.config(command=lambda: start_watchlist_update(False, False))
    watch_force_button.config(command=lambda: start_watchlist_update(True, False))

    # Vis eksisterende data straks. Derefter udføres dagens normale Watch list-
    # opdatering i baggrunden. Hvis den allerede er gennemført i dag, sker der
    # ingen TradingView-hentning. Dermed belastes programstarten ikke.
    load_rows()
    start_watchlist_update(False, True)

def show_selected_phase4_target_history():
    """Åbn historikken med markeret Fase 4-aktie som forvalg.

    Fase 4 viser ikke børsen som kolonne, så den markerede Treeview-række
    kobles tilbage til phase4_rows via ticker og navn. Uden en gyldig
    markering vises første aktie alfabetisk.
    """
    selected = phase4_tree.selection()
    if not selected:
        show_target_history_window()
        return

    item_id = selected[0]
    ticker = str(phase4_tree.set(item_id, "ticker") or "").upper().strip()
    name = str(phase4_tree.set(item_id, "name") or "").strip()
    if not ticker or ticker == "-" or name == "Sum / gennemsnit":
        show_target_history_window()
        return

    matching_row = next(
        (
            row for row in phase4_rows
            if not row.get("is_summary")
            and str(row.get("ticker", "")).upper().strip() == ticker
            and str(row.get("name", "")).strip() == name
        ),
        None,
    )
    if matching_row is None:
        matching_row = next(
            (
                row for row in phase4_rows
                if not row.get("is_summary")
                and str(row.get("ticker", "")).upper().strip() == ticker
            ),
            None,
        )
    if matching_row is None:
        show_target_history_window()
        return

    exchange = str(matching_row.get("exchange", "")).upper().strip()
    key = f"{exchange}:{ticker}" if exchange else ""
    data = load_target_age_history()
    entry = data.get("positions", {}).get(key, {}) if key else {}
    if not _entry_has_history_content(entry):
        messagebox.showinfo("Aktiens historik", f"Der findes endnu ingen historik for {name or ticker}.")
        return

    show_target_history_window(initial_key=key)


def build_phase4_rows():
    global phase4_rows
    history = analyst_target_history()
    out = []
    for r in phase2_rows:
        if r.get("is_summary") or is_cash_row(r):
            continue
        item = portfolio_item_for_row(r) or {}
        gak = parse_float(item.get("gak"), None)
        price = parse_float(r.get("price"), None)
        antal = parse_float(r.get("antal"), 0.0) or 0.0
        fx = 1.0
        native_value = parse_float(r.get("sort_value_dkk"), 0.0) or 0.0
        if price and antal:
            fx = native_value / (price * antal) if price * antal else 1.0
        # Nordnet-importen leverer kun GAK og antal som faste positionsdata.
        # Ureal.% og Ureal. DKK beregnes altid på ny fra programmets aktuelle kurs og valutakurs.
        # Dermed kræves en ny Nordnet-import kun efter køb, salg eller ændring af GAK/antal.
        unrealized_pct = ((price / gak) - 1.0) * 100.0 if gak and price and gak > 0 else None
        unrealized_dkk = (price - gak) * antal * fx if gak and price else None
        analyst_now = parse_float(r.get("analyst_base_pct"), None)
        bull_now = parse_float(r.get("analyst_bull_pct"), None)
        bear_now = parse_float(r.get("analyst_bear_pct"), None)
        key = f"{str(r.get('exchange','')).upper()}:{str(r.get('ticker','')).upper()}"
        position_history = history.get("positions", {}).get(key, {})
        entries = _complete_history_entries(position_history.get("history", [])) if isinstance(position_history, dict) else []

        # Startmål låses til den første gyldige positive historikværdi for hvert
        # scenarie separat. Dermed ignoreres ældre negative/manglende værdier,
        # som kan stamme fra den tidligere fejl i TradingView-valutanormaliseringen.
        analyst_start = first_history_upside(entries, "base_target")
        bull_start = first_history_upside(entries, "bull_target")
        stock_score = parse_float(r.get("stock_score"), None)

        # 100% nås, når Urealiseret % er lig med det respektive 1Y%-mål ved historikkens start.
        # Nul, negative og manglende historikværdier springes over; første positive værdi låses som startmål.
        base_goal_progress = None
        if unrealized_pct is not None and analyst_start is not None and analyst_start > 0:
            base_goal_progress = unrealized_pct / analyst_start * 100.0

        bull_goal_progress = None
        if unrealized_pct is not None and bull_start is not None and bull_start > 0:
            bull_goal_progress = unrealized_pct / bull_start * 100.0

        # Aktuelle mål skal sammenlignes på samme udgangspunkt som Urealiseret %: GAK.
        # Base 1Y% og Bull 1Y% er potentiale FRA DAGENS KURS, så de omregnes først
        # til et samlet kursmål og derefter til samlet afkast fra GAK.
        #
        # Eksempel:
        # GAK=100, kurs=120, aktuel Base 1Y%=30
        # Aktuelt Base-kursmål = 120 * 1,30 = 156
        # Samlet Base-mål fra GAK = 156/100 - 1 = 56%
        # Ved 20% urealiseret er Procent af Basemål = 20/56 = 35,7%.
        current_base_goal_pct = None
        if gak is not None and gak > 0 and price is not None and price > 0 and analyst_now is not None:
            current_base_target_price = price * (1.0 + analyst_now / 100.0)
            current_base_goal_pct = (current_base_target_price / gak - 1.0) * 100.0

        current_bull_goal_pct = None
        if gak is not None and gak > 0 and price is not None and price > 0 and bull_now is not None:
            current_bull_target_price = price * (1.0 + bull_now / 100.0)
            current_bull_goal_pct = (current_bull_target_price / gak - 1.0) * 100.0

        current_base_goal_progress = None
        if unrealized_pct is not None and current_base_goal_pct is not None and current_base_goal_pct > 0:
            current_base_goal_progress = unrealized_pct / current_base_goal_pct * 100.0

        current_bull_goal_progress = None
        if unrealized_pct is not None and current_bull_goal_pct is not None and current_bull_goal_pct > 0:
            current_bull_goal_progress = unrealized_pct / current_bull_goal_pct * 100.0

        row = {
            "rank": r.get("rank", ""), "exchange": r.get("exchange", ""), "ticker": r.get("ticker", ""), "name": r.get("name", ""),
            "antal": r.get("antal", ""), "value_dkk": format_dkk(native_value), "gak": format_num(gak, 2) if gak else "-", "price": r.get("price", "-"),
            "unrealized_pct": format_pct(unrealized_pct) if unrealized_pct is not None else "-",
            "unrealized_dkk": format_dkk(unrealized_dkk) if unrealized_dkk is not None else "-",
            "bull_now": format_pct(bull_now) if bull_now is not None else "-",
            "analyst_now": format_pct(analyst_now) if analyst_now is not None else "-",
            "bear_now": format_pct(bear_now) if bear_now is not None else "-",
            "stock_score": r.get("stock_score", "-"),
            "base_goal_progress": format_goal_progress(base_goal_progress),
            "bull_goal_progress": format_goal_progress(bull_goal_progress),
            "current_base_goal_progress": format_goal_progress(current_base_goal_progress),
            "current_bull_goal_progress": format_goal_progress(current_bull_goal_progress),
            "sort_rank": parse_float(r.get("rank"), 999999), "sort_ticker": str(r.get("ticker", "")).casefold(), "sort_name": str(r.get("name", "")).casefold(),
            "sort_antal": antal, "sort_value_dkk": native_value, "sort_gak": gak if gak is not None else -999999, "sort_price": price if price is not None else -999999,
            "sort_unrealized_pct": unrealized_pct if unrealized_pct is not None else -999999, "sort_unrealized_dkk": unrealized_dkk if unrealized_dkk is not None else -999999,
            "sort_bull_now": bull_now if bull_now is not None else -999999,
            "sort_analyst_now": analyst_now if analyst_now is not None else -999999,
            "sort_bear_now": bear_now if bear_now is not None else -999999,
            "sort_stock_score": stock_score if stock_score is not None else -999999,
            "sort_base_goal_progress": base_goal_progress if base_goal_progress is not None else -999999,
            "sort_bull_goal_progress": bull_goal_progress if bull_goal_progress is not None else -999999,
            "sort_current_base_goal_progress": current_base_goal_progress if current_base_goal_progress is not None else -999999,
            "sort_current_bull_goal_progress": current_bull_goal_progress if current_bull_goal_progress is not None else -999999,
        }
        # Skjult kostværdi i DKK bruges kun til den samlede Ureal.%-beregning.
        row["cost_value_dkk_raw"] = gak * antal * fx if gak and antal else None
        out.append(row)

    def valid_values(sort_key):
        values = []
        for data_row in out:
            value = data_row.get(sort_key, -999999)
            if value not in (None, -999999):
                try:
                    values.append(float(value))
                except Exception:
                    pass
        return values

    # Fast øverste række. Summer bruges, hvor tallene kan lægges meningsfuldt
    # sammen; gennemsnit bruges til scorer, analytikertal og målprocenter.
    total_antal = sum(float(r.get("sort_antal", 0.0) or 0.0) for r in out)
    # Værdi DKK i Sum / gennemsnit skal vise hele porteføljeværdien:
    # aktiepositioner plus Kontanter til rådighed. De øvrige summer/gennemsnit
    # beregnes fortsat kun på aktiepositionerne.
    cash_value_dkk = current_cash_value_dkk()
    total_value_dkk = (
        sum(float(r.get("sort_value_dkk", 0.0) or 0.0) for r in out)
        + cash_value_dkk
    )
    total_unrealized_dkk = sum(
        float(r.get("sort_unrealized_dkk", 0.0) or 0.0)
        for r in out if r.get("sort_unrealized_dkk") != -999999
    )
    total_cost_dkk = sum(
        float(r.get("cost_value_dkk_raw", 0.0) or 0.0)
        for r in out if r.get("cost_value_dkk_raw") is not None
    )
    total_unrealized_pct = total_unrealized_dkk / total_cost_dkk * 100.0 if total_cost_dkk > 0 else None

    def average(sort_key):
        values = valid_values(sort_key)
        return sum(values) / len(values) if values else None

    bull_now_avg = average("sort_bull_now")
    analyst_now_avg = average("sort_analyst_now")
    bear_now_avg = average("sort_bear_now")
    stock_score_avg = average("sort_stock_score")
    base_progress_avg = average("sort_base_goal_progress")
    bull_progress_avg = average("sort_bull_goal_progress")
    current_base_progress_avg = average("sort_current_base_goal_progress")
    current_bull_progress_avg = average("sort_current_bull_goal_progress")

    summary = {
        "rank": "-",
        "ticker": "-",
        "name": "Sum / gennemsnit",
        "antal": format_antal(total_antal) if out else "-",
        "value_dkk": format_dkk(total_value_dkk) if out else "-",
        "gak": "-",
        "price": "-",
        "unrealized_pct": format_pct(total_unrealized_pct) if total_unrealized_pct is not None else "-",
        "unrealized_dkk": format_dkk(total_unrealized_dkk) if out else "-",
        "bull_now": format_pct(bull_now_avg) if bull_now_avg is not None else "-",
        "analyst_now": format_pct(analyst_now_avg) if analyst_now_avg is not None else "-",
        "bear_now": format_pct(bear_now_avg) if bear_now_avg is not None else "-",
        "stock_score": format_num(stock_score_avg, 1) if stock_score_avg is not None else "-",
        "base_goal_progress": format_goal_progress(base_progress_avg),
        "bull_goal_progress": format_goal_progress(bull_progress_avg),
        "current_base_goal_progress": format_goal_progress(current_base_progress_avg),
        "current_bull_goal_progress": format_goal_progress(current_bull_progress_avg),
        "is_summary": True,
    }
    for col in PHASE4_COLUMN_IDS:
        summary.setdefault("sort_" + col, 0)
    # Kontanter vises fortsat som en fast nederste række i Fase 4.
    # Beløbet er samtidig medregnet i Værdi DKK på Sum / gennemsnit-rækken.
    cash_row = None
    if cash_value_dkk > 0:
        cash_row = {col: "-" for col in PHASE4_COLUMN_IDS}
        cash_row.update({
            "rank": "",
            "ticker": "-",
            "name": CASH_NAME,
            "antal": "-",
            "value_dkk": format_dkk(cash_value_dkk),
            "is_cash": True,
        })
        for col in PHASE4_COLUMN_IDS:
            cash_row["sort_" + col] = -999999
        cash_row["sort_name"] = CASH_NAME.casefold()
        cash_row["sort_value_dkk"] = cash_value_dkk

    phase4_rows = ([summary] if out else []) + out + ([cash_row] if cash_row else [])


def _render_phase4_rows():
    phase4_tree.delete(*phase4_tree.get_children())
    data_index = 0
    for r in phase4_rows:
        if r.get("is_summary"):
            tag = "summary"
        elif r.get("is_cash"):
            tag = "even"
        else:
            tag = "even" if data_index % 2 == 0 else "odd"
            data_index += 1
        phase4_tree.insert("", "end", values=[r.get(c, "") for c in PHASE4_COLUMN_IDS], tags=(tag,))


def show_phase4():
    build_phase4_rows()
    _render_phase4_rows()


def sort_phase4_rows(col):
    global phase4_rows, phase4_current_sort, phase4_descending
    if phase4_current_sort == col:
        phase4_descending = not phase4_descending
    else:
        phase4_current_sort = col
        phase4_descending = False if col in ("rank", "ticker", "name") else True

    summary_rows = [r for r in phase4_rows if r.get("is_summary")]
    cash_rows = [r for r in phase4_rows if r.get("is_cash")]
    data_rows = [r for r in phase4_rows if not r.get("is_summary") and not r.get("is_cash")]
    data_rows.sort(key=lambda x: x.get("sort_" + col, ""), reverse=phase4_descending)
    # Summeringsrækken er altid øverst, og kontanter er altid nederst.
    phase4_rows = summary_rows + data_rows + cash_rows
    _render_phase4_rows()


def _csv_value(row, candidates):
    normalized = {re.sub(r"[^a-z0-9æøå]", "", str(k).casefold()): v for k, v in row.items()}
    for candidate in candidates:
        key = re.sub(r"[^a-z0-9æøå]", "", candidate.casefold())
        if key in normalized and str(normalized[key]).strip():
            return normalized[key]
    return None


# Kendte forskelle mellem Nordnets navne og navnene i portefølje_default.json.
# Værdien er altid den entydige nøgle BØRS:TICKER, så Nordnet-data aldrig
# kobles til en løs eller selvstændig aktiepost.
NORDNET_NAME_ALIASES = {
    "applovina": "NASDAQ:APP",
    "bancosantanderadr": "NYSE:SAN",
    "coloplastb": "OMXCOP:COLO_B",
    "asmlholding": "EURONEXT:ASML",
    "novonordiskb": "OMXCOP:NOVO_B",
    "saabb": "OMXSTO:SAAB_B",
    "tencentholdingsltd": "OTC:TCEHY",
    "totalenergies": "NYSE:TTE",
    "freseniusseandcokgaa": "XETR:FRE",
    "schneiderelectricse": "EURONEXT:SU",
    "volkswagenag": "XETR:VOW",
    "strategya": "NASDAQ:MSTR",
    "leidos": "NYSE:LDOS",
}


def _read_nordnet_csv_text(path):
    """Læs Nordnets eksport direkte, også når den er UTF-16 og TAB-separeret."""
    raw = Path(path).read_bytes()
    encodings = []
    if raw.startswith((b"\xff\xfe", b"\xfe\xff")):
        encodings.extend(["utf-16", "utf-16-le", "utf-16-be"])
    encodings.extend(["utf-8-sig", "cp1252", "latin-1"])
    last_error = None
    for encoding in encodings:
        try:
            return raw.decode(encoding), encoding
        except Exception as e:
            last_error = e
    raise ValueError(f"Kunne ikke afkode CSV-filen: {last_error}")


def _normalize_company_name(value):
    txt = str(value or "").casefold().replace("&", " and ")
    txt = re.sub(r"\b(a/s|asa|ab|ag|se|nv|plc|inc|corp|corporation|company|co|kgaa|holdings?|group|adr|class|klasse|ltd)\b", " ", txt)
    txt = re.sub(r"\b[ab]\b", " ", txt)
    return re.sub(r"[^a-z0-9æøå]+", "", txt)


def _portfolio_by_key(key):
    key = str(key or "").upper().strip()
    for item in portfolio:
        if position_key(item) == key:
            return item
    return None


def _find_portfolio_match(ticker, name, currency=None):
    """Find kun en eksisterende porteføljepost og returnér matchmetode.

    Børs+ticker i portefølje_default.json forbliver den faste identitet.
    Der oprettes aldrig nye positioner fra Nordnet-filen.
    """
    ticker = str(ticker or "").strip().upper()
    name = str(name or "").strip()
    currency = str(currency or "").strip().upper()

    if ticker:
        exact = [x for x in portfolio if str(x.get("ticker", "")).upper() == ticker]
        if currency:
            exact_currency = [x for x in exact if currency_for_exchange(x.get("exchange")) == currency]
            if len(exact_currency) == 1:
                return exact_currency[0], "ticker+valuta"
        if len(exact) == 1:
            return exact[0], "ticker"

    alias_key = re.sub(r"[^a-z0-9æøå]", "", name.casefold())
    alias_target = NORDNET_NAME_ALIASES.get(alias_key)
    if alias_target:
        item = _portfolio_by_key(alias_target)
        if item:
            return item, "alias"

    if not name:
        return None, "ingen navn"

    source = _normalize_company_name(name)
    exact_name = [x for x in portfolio if _normalize_company_name(x.get("name", "")) == source]
    if currency:
        exact_currency = [x for x in exact_name if currency_for_exchange(x.get("exchange")) == currency]
        if len(exact_currency) == 1:
            return exact_currency[0], "navn+valuta"
    if len(exact_name) == 1:
        return exact_name[0], "navn"

    from difflib import SequenceMatcher
    scored = []
    for item in portfolio:
        target = _normalize_company_name(item.get("name", ""))
        if not source or not target:
            continue
        ratio = SequenceMatcher(None, source, target).ratio()
        if currency and currency_for_exchange(item.get("exchange")) != currency:
            ratio -= 0.12
        scored.append((ratio, item))
    scored.sort(key=lambda pair: pair[0], reverse=True)
    if scored and scored[0][0] >= 0.78:
        if len(scored) == 1 or scored[0][0] - scored[1][0] >= 0.10:
            return scored[0][1], "fuzzy navn"
    return None, "ikke sikkert match"


def _nordnet_snapshot_from_row(row, source_file):
    """Oversæt alle Nordnet-kolonner til stabile JSON-felter."""
    return {
        "importdato": today_key(),
        "kildefil": Path(source_file).name,
        "navn": str(_csv_value(row, ["Navn", "Instrument", "Værdipapir", "Description"]) or "").strip(),
        "valuta": str(_csv_value(row, ["Valuta", "Currency"]) or "").strip().upper(),
        "antal": normalize_number(_csv_value(row, ["Antal", "Beholdning", "Quantity", "Shares"]), 0.0),
        "gak": normalize_number(_csv_value(row, ["GAK", "Gennemsnitskurs", "Anskaffelseskurs", "Average price", "Købskurs"]), 0.0),
        "i_dag_pct": normalize_number(_csv_value(row, ["I dag %", "I dag", "Today %"]), 0.0),
        "seneste_kurs": normalize_number(_csv_value(row, ["Seneste kurs", "Last price", "Kurs"]), 0.0),
        "belaaningsvaerdi_dkk": normalize_number(_csv_value(row, ["Belåningsværdi DKK", "Belaaningsvaerdi DKK"]), 0.0),
        "vaerdi": normalize_number(_csv_value(row, ["Værdi", "Vaerdi", "Value"]), 0.0),
        "vaerdi_dkk": normalize_number(_csv_value(row, ["Værdi DKK", "Vaerdi DKK", "Value DKK"]), 0.0),
        "urealiseret_afkast_pct": normalize_number(_csv_value(row, ["Ureal.afkast %", "Urealiseret afkast %", "Unrealized return %"]), 0.0),
        "afkast_dkk": normalize_number(_csv_value(row, ["Afkast DKK", "Return DKK"]), 0.0),
    }


def _append_position_snapshot(item, snapshot):
    """Gem ét Nordnet-snapshot pr. dag; en ny import samme dag opdaterer posten."""
    history = item.setdefault("position_history", [])
    compact = {
        "date": snapshot.get("importdato"),
        "antal": snapshot.get("antal"),
        "gak": snapshot.get("gak"),
        "seneste_kurs": snapshot.get("seneste_kurs"),
        "vaerdi_dkk": snapshot.get("vaerdi_dkk"),
        "urealiseret_afkast_pct": snapshot.get("urealiseret_afkast_pct"),
        "afkast_dkk": snapshot.get("afkast_dkk"),
    }
    if history and history[-1].get("date") == compact["date"]:
        history[-1] = compact
    else:
        history.append(compact)



def _xlsx_column_index(cell_reference):
    """Konvertér fx A, Z og AA fra en celleadresse til nulbaseret kolonneindeks."""
    letters = re.match(r"[A-Z]+", str(cell_reference or "").upper())
    if not letters:
        return None
    value = 0
    for ch in letters.group(0):
        value = value * 26 + (ord(ch) - ord("A") + 1)
    return value - 1


def _read_saxo_xlsx_rows(path):
    """Læs Saxos XLSX-eksport uden afhængighed af Excels typografi eller openpyxl."""
    ns_main = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
    ns_rel = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
    ns_pkg = "http://schemas.openxmlformats.org/package/2006/relationships"
    ns = {"a": ns_main, "r": ns_rel}

    with ZipFile(path) as archive:
        shared_strings = []
        if "xl/sharedStrings.xml" in archive.namelist():
            root = ET.fromstring(archive.read("xl/sharedStrings.xml"))
            for item in root.findall(f"{{{ns_main}}}si"):
                shared_strings.append("".join(node.text or "" for node in item.iter(f"{{{ns_main}}}t")))

        workbook = ET.fromstring(archive.read("xl/workbook.xml"))
        rel_root = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
        relations = {
            rel.attrib["Id"]: rel.attrib["Target"]
            for rel in rel_root.findall(f"{{{ns_pkg}}}Relationship")
        }
        sheets = workbook.find("a:sheets", ns)
        if sheets is None or not list(sheets):
            raise ValueError("Saxo-arket indeholder ingen regneark.")
        first_sheet = list(sheets)[0]
        relation_id = first_sheet.attrib.get(f"{{{ns_rel}}}id")
        target = relations.get(relation_id, "worksheets/sheet1.xml").lstrip("/")
        sheet_path = target if target.startswith("xl/") else "xl/" + target
        sheet = ET.fromstring(archive.read(sheet_path))

        matrix = []
        for row_node in sheet.findall(".//a:sheetData/a:row", ns):
            values = {}
            for cell in row_node.findall("a:c", ns):
                col = _xlsx_column_index(cell.attrib.get("r"))
                if col is None:
                    continue
                cell_type = cell.attrib.get("t")
                value_node = cell.find("a:v", ns)
                value = "" if value_node is None else value_node.text or ""
                if cell_type == "s" and value != "":
                    try:
                        value = shared_strings[int(value)]
                    except Exception:
                        pass
                elif cell_type == "inlineStr":
                    value = "".join(node.text or "" for node in cell.iter(f"{{{ns_main}}}t"))
                values[col] = value
            if values:
                width = max(values) + 1
                matrix.append([values.get(i, "") for i in range(width)])

    if not matrix:
        raise ValueError("Saxo-arket er tomt.")
    headers = [str(value).strip() for value in matrix[0]]
    rows = []
    for values in matrix[1:]:
        padded = values + [""] * max(0, len(headers) - len(values))
        row = {headers[i]: padded[i] for i in range(len(headers)) if headers[i]}
        if any(str(value).strip() for value in row.values()):
            rows.append(row)
    return rows, "XLSX"


def _read_saxo_rows(path):
    """Læs Saxos positionsfil som XLSX eller almindelig CSV."""
    suffix = Path(path).suffix.casefold()
    if suffix in (".xlsx", ".xlsm"):
        return _read_saxo_xlsx_rows(path)

    raw, encoding = _read_nordnet_csv_text(path)
    lines = [line for line in raw.splitlines() if line.strip()]
    if not lines:
        raise ValueError("Filen er tom.")
    header = lines[0]
    delimiter_counts = {"\t": header.count("\t"), ";": header.count(";"), ",": header.count(",")}
    delimiter = max(delimiter_counts, key=delimiter_counts.get)
    if delimiter_counts[delimiter] == 0:
        raise ValueError("Kunne ikke genkende kolonneseparatoren i Saxo-filen.")
    return list(csv.DictReader(lines, delimiter=delimiter)), f"{encoding}; {'TAB' if delimiter == chr(9) else delimiter}"


def _saxo_ticker(value):
    """Udtræk ticker fra Saxos format, fx GOOGL:xnas -> GOOGL."""
    symbol = str(value or "").strip().upper()
    if not symbol:
        return ""
    return symbol.split(":", 1)[0].strip()


def _saxo_snapshot_from_row(row, source_file):
    """Oversæt Saxos kolonner til samme faste positionsbegreber som Fase 4 bruger."""
    name = str(_csv_value(row, ["Instrument", "Navn", "Description"]) or "").strip()
    symbol_raw = str(_csv_value(row, ["Symbol", "Ticker"]) or "").strip()
    currency = str(_csv_value(row, ["Valuta", "Currency"]) or "").strip().upper()
    gak = normalize_number(_csv_value(row, ["Kostpris", "Åbningskurs", "GAK", "Average price"]), 0.0, prefer_decimal=True)
    return {
        "importdato": today_key(),
        "kildefil": Path(source_file).name,
        "navn": name,
        "symbol": symbol_raw,
        "ticker": _saxo_ticker(symbol_raw),
        "isin": str(_csv_value(row, ["ISIN"]) or "").strip().upper(),
        "valuta": currency,
        "antal": normalize_number(_csv_value(row, ["Antal", "Quantity", "Shares"]), 0.0, prefer_decimal=True),
        "gak": gak,
        "aabningskurs": normalize_number(_csv_value(row, ["Åbningskurs", "Opening price"]), 0.0, prefer_decimal=True),
        "seneste_kurs": normalize_number(_csv_value(row, ["Aktuel kurs", "Seneste kurs", "Last price"]), 0.0, prefer_decimal=True),
        "vaerdi_dkk": normalize_number(_csv_value(row, ["Markedsværdi (DKK)", "Eksponering (DKK)", "Værdi DKK"]), 0.0, prefer_decimal=True),
        "urealiseret_afkast_pct": normalize_number(_csv_value(row, ["% Total afkast", "Urealiseret afkast %"]), 0.0, prefer_decimal=True),
        "afkast_dkk": normalize_number(_csv_value(row, ["Gevinst/Tab i alt (DKK)", "Gevinst/tab i alt (DKK)", "Afkast DKK"]), 0.0, prefer_decimal=True),
        "i_dag_pct": normalize_number(_csv_value(row, ["% 1D afk.", "I dag %"]), 0.0, prefer_decimal=True),
        "i_dag_dkk": normalize_number(_csv_value(row, ["1-dags gevinst/tab (DKK)"]), 0.0, prefer_decimal=True),
        "status": str(_csv_value(row, ["Status"]) or "").strip(),
        "aktivtype": str(_csv_value(row, ["Aktivtype", "Asset type"]) or "").strip(),
        "konto": str(_csv_value(row, ["Konto", "Account"]) or "").strip(),
        "positions_id": str(_csv_value(row, ["Positions ID", "Position ID"]) or "").strip(),
    }


def import_saxo_csv():
    path = filedialog.askopenfilename(
        title="Vælg Saxo CSV eller XLSX",
        filetypes=[("Saxo filer", "*.xlsx *.xlsm *.csv"), ("Excel filer", "*.xlsx *.xlsm"), ("CSV filer", "*.csv"), ("Alle filer", "*.*")],
    )
    if not path:
        return
    try:
        rows_in_file, file_format = _read_saxo_rows(path)
        found = matched = 0
        match_methods = {}
        unmatched = []

        for row in rows_in_file:
            snapshot = _saxo_snapshot_from_row(row, path)
            name = snapshot["navn"]
            # Spring Saxos summeringsrække og andre ikke-positioner over.
            if snapshot["gak"] <= 0 or snapshot["antal"] <= 0 or not name:
                continue
            if snapshot.get("aktivtype") and snapshot["aktivtype"].casefold() not in ("aktie", "stock", "etf"):
                continue

            found += 1
            item, method = _find_portfolio_match(snapshot["ticker"], name, snapshot["valuta"])
            if not item:
                unmatched.append(f"{name} ({snapshot['ticker'] or 'uden ticker'})")
                continue

            item["gak"] = snapshot["gak"]
            item["antal"] = snapshot["antal"]
            snapshot["matched_to"] = position_key(item)
            snapshot["match_method"] = method
            item["saxo"] = snapshot
            _append_position_snapshot(item, snapshot)
            matched += 1
            match_methods[method] = match_methods.get(method, 0) + 1

        save_portfolio()
        show_phase4()

        method_txt = ", ".join(f"{key}: {value}" for key, value in sorted(match_methods.items())) or "ingen"
        unmatched_txt = ""
        if unmatched:
            preview = "\n".join(f"• {value}" for value in unmatched[:15])
            more = f"\n• ... og {len(unmatched) - 15} flere" if len(unmatched) > 15 else ""
            unmatched_txt = f"\n\nIkke sikkert koblet ({len(unmatched)}):\n{preview}{more}"

        messagebox.showinfo(
            "Saxo CSV importeret",
            f"Saxo-positioner med GAK: {found}\n"
            f"Sikkert koblet til børs+ticker: {matched}\n"
            f"Matchmetoder: {method_txt}\n"
            f"Filformat: {file_format}\n\n"
            f"Kostpris er anvendt som GAK, og antal samt dagens positionssnapshot er gemt i {DEFAULT_PORTFOLIO_FILE.name}.\n"
            f"Ureal.% og Ureal. DKK beregnes fortsat af programmet ud fra den aktuelle kurs.\n"
            f"Ingen nye aktier er oprettet automatisk.{unmatched_txt}",
        )
    except Exception as e:
        messagebox.showerror("Saxo-import fejlede", f"Kunne ikke importere filen.\n\n{e}")


def import_nordnet_csv():
    path = filedialog.askopenfilename(title="Vælg Nordnet CSV", filetypes=[("CSV filer", "*.csv"), ("Alle filer", "*.*")])
    if not path:
        return
    try:
        raw, encoding = _read_nordnet_csv_text(path)
        lines = [line for line in raw.splitlines() if line.strip()]
        if not lines:
            raise ValueError("Filen er tom.")

        header = lines[0]
        delimiter_counts = {"\t": header.count("\t"), ";": header.count(";"), ",": header.count(",")}
        delimiter = max(delimiter_counts, key=delimiter_counts.get)
        if delimiter_counts[delimiter] == 0:
            raise ValueError("Kunne ikke genkende kolonneseparatoren i filen.")

        reader = csv.DictReader(lines, delimiter=delimiter)
        found = matched = 0
        match_methods = {}
        unmatched = []
        for row in reader:
            snapshot = _nordnet_snapshot_from_row(row, path)
            name = snapshot["navn"]
            ticker = str(_csv_value(row, ["Ticker", "Symbol", "Kortnavn", "ISIN"]) or "").strip().upper()
            if snapshot["gak"] <= 0 or not name:
                continue
            found += 1
            item, method = _find_portfolio_match(ticker, name, snapshot["valuta"])
            if not item:
                unmatched.append(name)
                continue

            # Den eksisterende porteføljepost med BØRS:TICKER er master.
            item["gak"] = snapshot["gak"]
            if snapshot["antal"] > 0:
                item["antal"] = snapshot["antal"]
            snapshot["matched_to"] = position_key(item)
            snapshot["match_method"] = method
            item["nordnet"] = snapshot
            _append_position_snapshot(item, snapshot)
            matched += 1
            match_methods[method] = match_methods.get(method, 0) + 1

        save_portfolio()
        show_phase4()

        method_txt = ", ".join(f"{k}: {v}" for k, v in sorted(match_methods.items())) or "ingen"
        unmatched_txt = ""
        if unmatched:
            preview = "\n".join(f"• {x}" for x in unmatched[:15])
            more = f"\n• ... og {len(unmatched)-15} flere" if len(unmatched) > 15 else ""
            unmatched_txt = f"\n\nIkke sikkert koblet ({len(unmatched)}):\n{preview}{more}"
        messagebox.showinfo(
            "Nordnet CSV importeret",
            f"Nordnet-positioner med GAK: {found}\n"
            f"Sikkert koblet til børs+ticker: {matched}\n"
            f"Matchmetoder: {method_txt}\n"
            f"Filformat: {encoding}; separator: {'TAB' if delimiter == chr(9) else delimiter}\n\n"
            f"Alle Nordnet-felter, GAK, antal og dagens positionssnapshot er gemt i {DEFAULT_PORTFOLIO_FILE.name}.\n"
            f"Ingen nye aktier er oprettet automatisk.{unmatched_txt}"
        )
    except Exception as e:
        messagebox.showerror("CSV-import fejlede", f"Kunne ikke importere filen.\n\n{e}")



def refresh_portfolio_box():
    """Hovedvinduet har ikke længere en fast redigeringsliste.
    Funktionen bevares, så import/gem kan opdatere et åbent redigeringsvindue senere hvis ønsket.
    """
    return



def open_edit_window():
    win = tk.Toplevel(root)
    win.title("Rediger portefølje")
    win.geometry("1500x650")
    win.minsize(1200, 520)
    win.transient(root)

    # Brug grid i selve redigeringsvinduet, så knaplinjen altid bliver liggende
    # synligt nederst. Tabellen er den eneste del, der må vokse/krympe.
    win.grid_rowconfigure(0, weight=0)
    win.grid_rowconfigure(1, weight=1)
    win.grid_rowconfigure(2, weight=0)
    win.grid_columnconfigure(0, weight=1)

    edit_exchange_var = tk.StringVar(value="NASDAQ")
    edit_ticker_var = tk.StringVar()
    edit_name_var = tk.StringVar()
    edit_antal_var = tk.StringVar(value="1")

    form = tk.LabelFrame(win, text="Tilføj / opdater position i default-portefølje", font=small_font, padx=10, pady=8)
    form.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 8))

    previous_choices = stock_registry_choices(include_active=False)
    previous_lookup = {label: entry for label, _key, entry in previous_choices}
    previous_var = tk.StringVar()
    tk.Label(form, text="Tidligere aktie:", font=small_font).pack(side="left", padx=(0, 4))
    previous_combo = ttk.Combobox(form, textvariable=previous_var, values=[x[0] for x in previous_choices], width=34)
    previous_combo.pack(side="left", padx=(0, 10))

    tk.Label(form, text="Børs:", font=small_font).pack(side="left", padx=(0, 4))
    tk.Entry(form, textvariable=edit_exchange_var, font=small_font, width=10).pack(side="left", padx=(0, 10))
    tk.Label(form, text="Ticker:", font=small_font).pack(side="left", padx=(0, 4))
    tk.Entry(form, textvariable=edit_ticker_var, font=small_font, width=12).pack(side="left", padx=(0, 10))
    tk.Label(form, text="Navn:", font=small_font).pack(side="left", padx=(0, 4))
    tk.Entry(form, textvariable=edit_name_var, font=small_font, width=34).pack(side="left", padx=(0, 10))
    tk.Label(form, text="Antal:", font=small_font).pack(side="left", padx=(0, 4))
    tk.Entry(form, textvariable=edit_antal_var, font=small_font, width=12).pack(side="left", padx=(0, 10))

    box_frame = tk.Frame(win)
    box_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 8))
    box_frame.grid_rowconfigure(0, weight=1)
    box_frame.grid_columnconfigure(0, weight=1)

    edit_columns = [
        ("exchange", "Børs", 110, "center"),
        ("ticker", "Ticker", 120, "center"),
        ("name", "Navn", 620, "w"),
        ("antal", "Antal", 130, "center"),
    ]
    edit_sort_col = "name"
    edit_sort_descending = False

    edit_box = ttk.Treeview(box_frame, columns=[c[0] for c in edit_columns], show="headings", height=6)

    def edit_sort_value(item, col):
        if col == "antal":
            return normalize_number(item.get("antal", 0), 0.0)
        return str(item.get(col, "")).casefold()

    def update_edit_headers():
        for col, title, _width, _anchor in edit_columns:
            arrow = ""
            if col == edit_sort_col:
                arrow = " ▼" if edit_sort_descending else " ▲"
            edit_box.heading(col, text=title + arrow, command=lambda c=col: sort_edit_box(c))

    def sort_edit_box(col):
        nonlocal edit_sort_col, edit_sort_descending
        if edit_sort_col == col:
            edit_sort_descending = not edit_sort_descending
        else:
            edit_sort_col = col
            edit_sort_descending = False if col in ("exchange", "ticker", "name") else True
        refresh_edit_box()

    for col, title, width, anchor in edit_columns:
        edit_box.heading(col, text=title, command=lambda c=col: sort_edit_box(c))
        edit_box.column(col, width=width, anchor=anchor, stretch=(col == "name"))

    y_scroll_edit = ttk.Scrollbar(box_frame, orient="vertical", command=edit_box.yview)
    edit_box.configure(yscrollcommand=y_scroll_edit.set)
    edit_box.grid(row=0, column=0, sticky="nsew")
    y_scroll_edit.grid(row=0, column=1, sticky="ns")

    def choose_previous_stock(event=None):
        label = previous_var.get().strip()
        entry = previous_lookup.get(label)
        if not entry:
            # Tillad hurtig søgning på navn, ticker, børs eller BØRS:TICKER.
            q = label.casefold()
            matches = [e for l, _k, e in previous_choices if q and q in l.casefold()]
            if len(matches) == 1:
                entry = matches[0]
        if not entry:
            return
        edit_exchange_var.set(str(entry.get("exchange", "")).upper())
        edit_ticker_var.set(str(entry.get("ticker", "")).upper())
        edit_name_var.set(str(entry.get("name", "")))
        edit_antal_var.set("1")

    def filter_previous_choices(event=None):
        q = previous_var.get().casefold().strip()
        values = [label for label, _key, _entry in previous_choices if not q or q in label.casefold()]
        previous_combo["values"] = values

    previous_combo.bind("<<ComboboxSelected>>", choose_previous_stock)
    previous_combo.bind("<KeyRelease>", filter_previous_choices)
    previous_combo.bind("<Return>", choose_previous_stock)

    def refresh_edit_box():
        edit_box.delete(*edit_box.get_children())
        stock_items = [x for x in portfolio if not is_cash_item(x)]
        cash_items = [x for x in portfolio if is_cash_item(x)]
        sorted_items = sorted(
            stock_items,
            key=lambda x: edit_sort_value(x, edit_sort_col),
            reverse=edit_sort_descending,
        ) + cash_items
        for item in sorted_items:
            edit_box.insert("", "end", values=(item["exchange"], item["ticker"], item["name"], format_antal(item["antal"])))
        update_edit_headers()

    def fill_edit_fields(event=None):
        selected = edit_box.selection()
        if not selected:
            return
        values = edit_box.item(selected[0], "values")
        edit_exchange_var.set(values[0])
        edit_ticker_var.set(values[1])
        edit_name_var.set(values[2])
        edit_antal_var.set(str(values[3]).replace(".", "").replace(",", "."))

    def add_or_update_edit_position():
        exchange = edit_exchange_var.get().strip().upper()
        ticker = edit_ticker_var.get().strip().upper()
        name = edit_name_var.get().strip() or ticker
        antal = normalize_number(edit_antal_var.get(), 0.0)
        if exchange == CASH_EXCHANGE and ticker == CASH_TICKER:
            name = CASH_NAME
            antal = max(0.0, antal)
        if not exchange or not ticker:
            messagebox.showinfo("Manglende oplysninger", "Skriv mindst børs og ticker.", parent=win)
            return
        found = False
        for item in portfolio:
            if item["exchange"] == exchange and item["ticker"] == ticker:
                item["name"] = name
                item["antal"] = antal
                found = True
                break
        if not found:
            portfolio.append({"exchange": exchange, "ticker": ticker, "name": name, "antal": antal})
        remember_stock({"exchange": exchange, "ticker": ticker, "name": name}, active=True)
        save_portfolio()
        refresh_edit_box()
        status_var.set(f"Gemt i {DEFAULT_PORTFOLIO_FILE.name}: {exchange}:{ticker} – {name}, antal {format_antal(antal)}")

    def delete_edit_position():
        selected = edit_box.selection()
        if not selected:
            messagebox.showinfo("Ingen valgt", "Vælg en position først.", parent=win)
            return
        values = edit_box.item(selected[0], "values")
        exchange, ticker = values[0], values[1]
        if exchange.upper() == CASH_EXCHANGE and ticker.upper() == CASH_TICKER:
            messagebox.showinfo("Kontantpost bevares", "Kontanter til rådighed skal altid findes. Sæt beløbet til 0 i stedet for at slette rækken.", parent=win)
            return
        if not messagebox.askyesno("Fjern position", f"Fjern {exchange}:{ticker} fra den aktive portefølje?\n\nAktien bevares i kartoteket, og analytikerhistorikken fortsætter.", parent=win):
            return
        global portfolio
        removed = next((x for x in portfolio if x["exchange"] == exchange and x["ticker"] == ticker), None)
        portfolio = [x for x in portfolio if not (x["exchange"] == exchange and x["ticker"] == ticker)]
        if removed:
            remember_stock(removed, active=False)
        save_portfolio()
        refresh_edit_box()
        status_var.set(f"Fjernet fra aktiv portefølje, men bevaret i aktiekartotek: {exchange}:{ticker}")

    edit_box.bind("<<TreeviewSelect>>", fill_edit_fields)

    button_frame = tk.Frame(win)
    button_frame.grid(row=2, column=0, sticky="ew", padx=10, pady=(0, 10))
    button_frame.grid_columnconfigure(3, weight=1)

    tk.Button(button_frame, text="Tilføj / opdater", font=small_font, command=add_or_update_edit_position).grid(row=0, column=0, sticky="w", padx=(0, 8))
    tk.Button(button_frame, text="Fjern valgt", font=small_font, command=delete_edit_position).grid(row=0, column=1, sticky="w", padx=(0, 8))
    tk.Button(button_frame, text="Opdater hovedtabel", font=small_font, command=lambda: start_fetch_thread(False)).grid(row=0, column=2, sticky="w", padx=(0, 8))
    tk.Label(button_frame, text=f"Data gemmes her: {Path.cwd()}", font=small_font, anchor="w").grid(row=0, column=3, sticky="ew", padx=(12, 8))
    tk.Button(button_frame, text="Luk", font=small_font, command=win.destroy).grid(row=0, column=4, sticky="e")

    refresh_edit_box()


def import_portfolio_json():
    path = filedialog.askopenfilename(
        title="Vælg portefølje-JSON",
        filetypes=[("JSON filer", "*.json"), ("Alle filer", "*.*")],
    )
    if not path:
        return
    try:
        imported = load_portfolio_from_file(path)
    except Exception as e:
        messagebox.showerror("Import fejlede", f"Kunne ikke læse porteføljen.\n\nFejl:\n{e}")
        return
    global portfolio
    portfolio = imported
    save_portfolio(portfolio)
    refresh_portfolio_box()
    status_var.set(f"Importeret {len(portfolio)} positioner fra {Path(path).name}. Default-filen er overskrevet; kildefilen er ikke ændret.")


def fetch(force_refresh=False):
    global rows, phase2_rows, phase2b_rows
    if TvDatafeed is None:
        messagebox.showerror(
            "tvDatafeed mangler",
            "Python-modulet tvDatafeed er ikke installeret i dette miljø.\n\nInstaller det fx med:\npip install tvdatafeed",
        )
        return

    cache = load_daily_cache()
    cache.setdefault("fx_rates", {})
    cache.setdefault("phase1", {})
    cache.setdefault("phase2", {})
    cache.setdefault("vix", {})

    if force_refresh:
        # Forceret opdatering ignorerer dagens cache og henter alle data på ny.
        cache = {
            "schema": "PORTEFOLJE_SIMULATOR_DAILY_CACHE_V1",
            "date": today_key(),
            "fx_rates": {},
            "phase1": {},
            "phase2": {},
            "vix": {},
        }
        status_var.set(f"Forceret opdatering: henter alle data på ny for {len(portfolio)} positioner...")
    else:
        status_var.set(f"Klargør dags-cache for {len(portfolio)} positioner...")
    tv = TvDatafeed()

    # VIX genbruges normalt fra dagens cache. En forceret opdatering har tømt
    # cachen ovenfor og henter derfor altid VIX på ny.
    global current_vix_value
    cached_vix = parse_float(cache.get("vix", {}).get("value"), None)
    if cached_vix is not None:
        current_vix_value = cached_vix
    else:
        try:
            status_var.set("Henter VIX fra TradingView...")
            current_vix_value = fetch_vix_value(tv)
            cache["vix"] = {
                "value": current_vix_value,
                "date": today_key(),
                "updated_at": datetime.now().isoformat(timespec="seconds"),
            }
            save_daily_cache(cache)
        except Exception:
            current_vix_value = None
    root.after(0, update_vix_display)

    needed_currencies = [currency_for_exchange(item["exchange"]) for item in portfolio]
    registry_for_fx = load_stock_registry()
    needed_currencies.extend(
        (entry.get("currency") or currency_for_exchange(entry.get("exchange")))
        for entry in registry_for_fx.get("stocks", {}).values() if isinstance(entry, dict)
    )

    # Valutakurser: genbrug dagens cache, hent kun manglende valutaer.
    fx_rates = {"DKK": 1.0}
    fx_fallback = []
    missing_currencies = []
    for currency in sorted(set(needed_currencies)):
        if currency == "DKK":
            fx_rates[currency] = 1.0
            continue
        cached_rate = cache.get("fx_rates", {}).get(currency)
        if not value_is_missing(cached_rate):
            try:
                fx_rates[currency] = float(cached_rate)
                continue
            except Exception:
                pass
        missing_currencies.append(currency)

    if missing_currencies:
        status_var.set("Henter manglende valutakurser til DKK fra TradingView...")
        fetched_fx, fetched_fallback = fetch_fx_rates(tv, missing_currencies)
        fx_rates.update(fetched_fx)
        fx_fallback.extend(fetched_fallback)
        for currency, rate in fetched_fx.items():
            cache["fx_rates"][currency] = rate
        save_daily_cache(cache)

    raw_rows = []
    failed = []
    phase1_cache_hits = 0
    phase1_fetched = 0
    phase1_required = ["price_raw", "sma50_raw", "trend_strength_raw", "robustness_raw", "history_days_raw", "data_date"] + [key + "_raw" for key, _title, _bars in PERIODS]

    for i, item in enumerate(portfolio, start=1):
        key = position_key(item)
        if is_cash_item(item):
            raw_rows.append(make_cash_raw(item))
            continue
        cached = cache.get("phase1", {}).get(key)
        if has_required_fields(cached, phase1_required):
            r = cache_raw_from_item(item, cached, fx_rates)
            if r:
                phase1_cache_hits += 1
                raw_rows.append(r)
                status_var.set(f"Fase 1-cache genbrugt: {key} ({i}/{len(portfolio)})")
                continue

        status_var.set(f"Henter manglende fase 1-data: {item['exchange']}:{item['ticker']} – {item['name']} ({i}/{len(portfolio)})...")
        r = fetch_one(tv, item, fx_rates)
        if r:
            raw_rows.append(r)
            phase1_fetched += 1
            cache["phase1"][key] = dict(r)
            save_daily_cache(cache)
        else:
            failed.append(f"{item['exchange']}:{item['ticker']}")

    total_value = sum(x["value_raw"] for x in raw_rows)
    display_pairs = [(make_display_row(x, total_value), x) for x in raw_rows]
    display_pairs = sorted(
        display_pairs,
        key=lambda pair: (1 if pair[0].get("is_cash") else 0, -pair[0]["sort_weight"]),
    )
    display_rows = []
    phase2_data_rows = []
    phase2b_data_rows = []
    fundamental_failed = []
    analyst_failed = []
    phase2_cache_hits = 0
    phase2_fetched = 0
    phase2_required = ["pe", "peg", "revenue_growth_3y", "ebit_margin_ttm", "kurs_f2", "sector", "industry", "country", "target_high", "target_base", "target_median", "target_low", "quality_schema_v2", "intrinsic_schema_v1", "structure_schema_v1", "calendar_schema_v2", "dividend_schema_v6"]

    # v6.97: dato-fallback hentes én gang i batch for alle aktier, aldrig inde i
    # den enkelte akties felt-probing. Hvis batchen fejler, fortsætter programmet
    # blot med HTML-data/frekvens som før.
    global _dividend_date_batch_cache
    try:
        needs_dividend_batch = force_refresh or any(
            value_is_missing(normalize_phase2_cache(cache.get("phase2", {}).get(position_key(item), {})).get("dividend_schema_v6"))
            for item in portfolio if not is_cash_item(item)
        )
        if needs_dividend_batch:
            status_var.set("Henter udbyttedatoer i batch fra TradingView...")
            _dividend_date_batch_cache = _fetch_dividend_dates_batch(portfolio)
        else:
            _dividend_date_batch_cache = {}
    except Exception:
        _dividend_date_batch_cache = {}

    stock_rank = 0
    cash_phase2_row = None
    for _index, (display_row, raw_row) in enumerate(display_pairs, start=1):
        if raw_row.get("is_cash"):
            display_row["rank"] = ""
            display_row["sort_rank"] = 999999999
            # Kontanter skal kun vises i Fase 2, men indgår i samlet kapital og vægte.
            cash_phase2_row = make_cash_phase2_row(display_row)
            continue

        stock_rank += 1
        rank = stock_rank
        display_row["rank"] = str(rank)
        display_row["sort_rank"] = rank
        display_rows.append(display_row)

        key = position_key(raw_row)
        cached_fundamental = normalize_phase2_cache(cache.get("phase2", {}).get(key, {}))
        missing_fields = [field for field in phase2_required if value_is_missing(cached_fundamental.get(field))]
        fundamental = dict(cached_fundamental)
        analyst_error = ""

        if missing_fields:
            status_var.set(f"Henter manglende fase 2-data: {raw_row['exchange']}:{raw_row['ticker']} ({rank}/{len(display_pairs)}) – mangler {', '.join(missing_fields)}...")
            fetched_any = False

            # Scanner henter PE, PEG, vækst, EBIT-margin, kurs, sektor, industri og land/region samlet.
            scanner_fields = {"pe", "peg", "revenue_growth_3y", "ebit_margin_ttm", "roic", "fcf_margin_ttm", "fcf_growth_3y", "kurs_f2", "sector", "industry", "country", "target_high", "target_base", "target_median", "target_low", "analyst_count", "quality_schema_v2", "market_cap", "structure_schema_v1", "total_assets", "total_liabilities", "goodwill", "total_equity", "shares_outstanding", "intrinsic_schema_v1", "earnings_next_date", "calendar_schema_v3", "dividend_yield"}
            if any(field in missing_fields for field in scanner_fields):
                try:
                    fetched = fetch_fundamental_row_from_tradingview_scanner(raw_row)
                    for k, v in fetched.items():
                        if not value_is_missing(v) and value_is_missing(fundamental.get(k)):
                            fundamental[k] = v
                            fetched_any = True
                    # Marker at den nye kvalitetsdatapakke er forsøgt hentet.
                    # Manglende ROIC/FCF hos enkelte selskaber er gyldigt og skal
                    # ikke udløse gentagne opslag resten af dagen.
                    fundamental["quality_schema_v2"] = 2
                    fundamental["intrinsic_schema_v1"] = 1
                    fundamental["structure_schema_v1"] = 1
                    fundamental["calendar_schema_v3"] = 3
                except Exception:
                    fundamental_failed.append(f"{raw_row['exchange']}:{raw_row['ticker']}")

            # Udbyttefrekvens og seneste historiske udbyttedato ligger på TradingViews
            # dividend-side. Dette opslag er adskilt fra scanneren, fordi en
            # manglende historisk dato er et gyldigt resultat for enkelte papirer. Schema-markøren forhindrer gentagne opslag
            # resten af dagen, også når værdien er '-'.
            if value_is_missing(fundamental.get("dividend_schema_v6")):
                try:
                    dividend_schedule = fetch_tradingview_dividend_schedule(raw_row)
                    for k, v in dividend_schedule.items():
                        if not value_is_missing(v):
                            fundamental[k] = v
                    fundamental["dividend_schema_v6"] = 6
                    fetched_any = True
                except Exception:
                    # Et enkelt webopslag må ikke blokere resten af Fase 2.
                    # Markér forsøget, så samme fejl ikke gentages for hver
                    # genberegning resten af dagen.
                    fundamental["dividend_schema_v6"] = 6
                    fetched_any = True

            # Gammel forecast-scraping bruges kun som nød-fallback, hvis scannerens Base target mangler.
            if value_is_missing(fundamental.get("target_base")) and value_is_missing(fundamental.get("analyst_1y_upside_pct")):
                try:
                    analyst_value, analyst_msg = fetch_tradingview_forecast_upside(raw_row, raw_row.get("price_raw"))
                    if analyst_value:
                        # Gemmes som fallback-upside, ikke target. make_phase2_row bruger kun fallback hvis target_base mangler.
                        fundamental["analyst_1y_upside_pct"] = analyst_value
                        fetched_any = True
                    else:
                        analyst_error = analyst_msg
                        analyst_failed.append(f"{raw_row['exchange']}:{raw_row['ticker']}")
                except Exception as e:
                    analyst_error = str(e)
                    analyst_failed.append(f"{raw_row['exchange']}:{raw_row['ticker']}")

            cache["phase2"][key] = normalize_phase2_cache(fundamental)
            save_daily_cache(cache)
            if fetched_any:
                phase2_fetched += 1
        else:
            phase2_cache_hits += 1
            status_var.set(f"Fase 2-cache genbrugt: {key} ({rank}/{len(display_pairs)})")

        phase2_data_rows.append(make_phase2_row(display_row, raw_row, fundamental, analyst_error))
        phase2b_data_rows.append(make_phase2b_row(display_row, fundamental))

    apply_recommended_weights(phase2_data_rows, total_portfolio_value=total_value)

    summary = make_summary_row(display_rows)
    # Fase 1 viser fortsat kun aktier; summary-værdien korrigeres til samlet kapital inkl. kontanter.
    summary["value_dkk"] = format_dkk(total_value)
    summary["sort_value_dkk"] = total_value
    rows = [summary] + display_rows
    # v0.25: beregn scorerne på den faktiske færdigbyggede DKK-fordeling.
    _apply_builder_allocation_scores_only(phase2_data_rows)
    phase2_rows = [make_phase2_row(summary, None, {})] + phase2_data_rows
    update_phase2_summary(phase2_rows[0], phase2_data_rows)
    if cash_phase2_row is not None:
        phase2_rows.append(cash_phase2_row)
    apply_ai_catalyst_cache_to_phase2_rows()
    phase2b_rows = [make_phase2b_row(summary, {})] + phase2b_data_rows
    root.after(0, show)
    root.after(0, show_phase2)
    root.after(0, show_phase2b)
    root.after(0, show_phase3_structure)
    root.after(0, show_portfolio_structure)
    root.after(0, show_phase4)
    root.after(0, update_vix_display)

    failed_txt = f" | Fejlede: {', '.join(failed)}" if failed else ""
    fx_txt = ""
    if raw_rows:
        used = ", ".join(f"{k}={format_num(v, 4)}" for k, v in sorted(fx_rates.items()) if k in set(x.get("currency") for x in raw_rows))
        fx_txt = f" | FX: {used}"
    fallback_txt = f" | FX fallback: {', '.join(fx_fallback)}" if fx_fallback else ""
    date_txt = ""
    if raw_rows:
        dates = sorted(set(x.get("data_date", "") for x in raw_rows if x.get("data_date")))
        if dates:
            date_txt = f" | Seneste data: {dates[-1]}"
    fundamental_txt = f" | Fase2 fundamental fejl: {len(fundamental_failed)}" if fundamental_failed else ""
    analyst_txt = f" | Analytiker fejl: {len(analyst_failed)}" if analyst_failed else ""
    cache_txt = f" | Cache F1 {phase1_cache_hits}, hentet F1 {phase1_fetched} | Cache F2 {phase2_cache_hits}, hentet F2 {phase2_fetched}"
    mode_txt = "Forceret opdatering færdig" if force_refresh else "Færdig"
    loaded_stock_count = sum(1 for raw_row in raw_rows if not raw_row.get("is_cash"))
    portfolio_stock_count = sum(1 for item in portfolio if not is_cash_item(item))
    status_var.set(f"{mode_txt}. Positioner: {loaded_stock_count}/{portfolio_stock_count} | PF-værdi DKK: {format_num(total_value, 0)}{date_txt}{cache_txt}{fx_txt}{fallback_txt}{failed_txt}{fundamental_txt}{analyst_txt}")


def show():
    tree.delete(*tree.get_children())
    for i, r in enumerate(rows):
        values = [r.get(c, "") for c in COLUMN_IDS]
        tag = "summary" if r.get("is_summary") else ("even" if i % 2 == 0 else "odd")
        tree.insert("", "end", values=values, tags=(tag,))


def format_target_position_indicator(row, slots=15):
    """Vis aktuel kurs som én lodret markør mellem absolut Bear og Bull.

    Indikatoren er altid præcis 15 tegn: prikker i hele intervallet og "|"
    på den position, hvor den aktuelle kurs ligger. Bear er venstre ende og
    Bull højre ende. Kurser uden for intervallet klemmes visuelt til nærmeste
    ende. Der bruges ingen farver eller særskilt Base-markering.
    """
    if row.get("is_summary") or is_cash_row(row):
        return "-"
    bear = parse_float(row.get("bear_target_abs"), None)
    bull = parse_float(row.get("bull_target_abs"), None)
    price = parse_float(row.get("price"), None)
    if bear is None or bull is None or price is None or bull <= bear or slots < 3:
        return "-"

    rel = (price - bear) / (bull - bear)
    rel = max(0.0, min(1.0, rel))
    price_slot = int(round(rel * (slots - 1)))

    chars = ["·"] * slots
    chars[price_slot] = "|"
    return "".join(chars)


def show_phase2():
    apply_ai_catalyst_cache_to_phase2_rows()
    phase2_tree.delete(*phase2_tree.get_children())
    for i, r in enumerate(phase2_rows):
        r["target_position"] = format_target_position_indicator(r)
        values = [r.get(c, "") for c in PHASE2_COLUMN_IDS]
        if r.get("is_summary"):
            tag = "summary"
        elif is_cash_row(r):
            tag = "cash"
        elif r.get("upside_sell"):
            tag = "sell"
        elif r.get("data_warning") or any(
            parse_float(r.get(field), None) is None
            for field in ("analyst_bear_pct", "analyst_base_pct", "analyst_bull_pct")
        ):
            tag = "data_problem"
        elif r.get("buy_opportunity"):
            tag = "buy_opportunity"
        else:
            tag = phase2_watch_color_tag(r) or ("even" if i % 2 == 0 else "odd")
        phase2_tree.insert("", "end", values=values, tags=(tag,))


def sort_rows(col):
    global rows, current_sort, descending
    if not rows:
        return
    summary = rows[0] if rows[0].get("is_summary") else None
    data_rows = rows[1:] if summary else rows[:]
    if current_sort == col:
        descending = not descending
    else:
        current_sort = col
        descending = False if col in ("rank", "exchange", "ticker", "name") else True
    data_rows = sorted(data_rows, key=lambda x: x.get("sort_" + col, ""), reverse=descending)
    rows = ([summary] if summary else []) + data_rows
    update_headers()
    show()


def update_headers():
    for col_id, title, _width in COLUMNS:
        arrow = ""
        if col_id == current_sort:
            arrow = " ▼" if descending else " ▲"
        tree.heading(col_id, text=title + arrow, command=lambda c=col_id: sort_rows(c))


def sort_phase2_rows(col):
    global phase2_rows, phase2_current_sort, phase2_descending
    if not phase2_rows:
        return
    summary = phase2_rows[0] if phase2_rows[0].get("is_summary") else None
    data_rows = phase2_rows[1:] if summary else phase2_rows[:]
    if phase2_current_sort == col:
        phase2_descending = not phase2_descending
    else:
        phase2_current_sort = col
        phase2_descending = False if col in ("rank", "exchange", "ticker", "name", "sector", "industry", "country") else True
    cash_rows = [r for r in data_rows if is_cash_row(r)]
    stock_rows = [r for r in data_rows if not is_cash_row(r)]
    stock_rows = sorted(stock_rows, key=lambda x: x.get("sort_" + col, ""), reverse=phase2_descending)
    phase2_rows = ([summary] if summary else []) + stock_rows + cash_rows
    update_phase2_headers()
    show_phase2()


def update_phase2_headers():
    for col_id, title, _width in PHASE2_COLUMNS:
        arrow = ""
        if col_id == phase2_current_sort:
            arrow = " ▼" if phase2_descending else " ▲"
        phase2_tree.heading(col_id, text=title + arrow, command=lambda c=col_id: sort_phase2_rows(c))


def clean_category(value, fallback="Ukendt"):
    txt = str(value or "").strip()
    if txt == "" or txt == "-":
        return fallback
    return txt


def pe_bucket_label(pe_value):
    pe = parse_float(pe_value, None)
    if pe is None:
        return "PE ukendt"
    for label, low, high in PE_BUCKETS:
        if high is None:
            if pe > low:
                return label
        elif pe >= low and pe < high:
            return label
    if pe < 1:
        return "PE <1 / negativ"
    return "PE ukendt"


def fc1y_bucket_label(fc_value):
    fc = parse_float(fc_value, None)
    if fc is None:
        return "FC1Y ukendt"
    for label, low, high in FC1Y_BUCKETS:
        if low is None:
            if fc < high:
                return label
        elif high is None:
            if fc > low:
                return label
        elif label == "FC1Y 40-50%":
            if fc >= low and fc <= high:
                return label
        elif fc >= low and fc < high:
            return label
    return "FC1Y ukendt"


def weighted_fc1y_for_rows(data_rows, stock_weight_total=None):
    """Beregn analytikertal med dækning målt som andel af aktiedelen.

    Fase 2-vægtene inkluderer kontanter, men alle procentandele i Fase 3
    skal vises uden kontanter. Derfor normaliseres dækningen til 100 % af
    aktiebeholdningen. Selve det vægtede FC1Y-gennemsnit er uændret af
    normaliseringen, fordi både tæller og nævner skaleres ens.
    """
    if stock_weight_total is None:
        stock_weight_total = sum(parse_float(r.get("weight"), 0.0) or 0.0 for r in data_rows)

    weighted_sum = 0.0
    weight_with_fc_raw = 0.0
    fc_values = []
    for r in data_rows:
        fc = parse_float(r.get("analyst_1y_upside_pct"), None)
        if fc is None:
            continue
        weight = parse_float(r.get("weight"), 0.0) or 0.0
        weighted_sum += weight * fc
        weight_with_fc_raw += weight
        fc_values.append(fc)
    weighted_avg = weighted_sum / weight_with_fc_raw if weight_with_fc_raw > 0 else None
    weight_with_fc = (
        weight_with_fc_raw / stock_weight_total * 100.0
        if stock_weight_total and stock_weight_total > 0 else 0.0
    )
    simple_avg = sum(fc_values) / len(fc_values) if fc_values else None
    median_avg = None
    if fc_values:
        sorted_values = sorted(fc_values)
        n = len(sorted_values)
        mid = n // 2
        if n % 2 == 1:
            median_avg = sorted_values[mid]
        else:
            median_avg = (sorted_values[mid - 1] + sorted_values[mid]) / 2.0
    return weighted_avg, simple_avg, median_avg, weight_with_fc, len(fc_values)


def update_phase3_view_buttons():
    """Markér den valgte Fase 3-fordeling som en fysisk nedtrykket knap."""
    buttons = globals().get("phase3_view_buttons", {})
    if not isinstance(buttons, dict):
        return
    title_to_key = {
        "Struktur": "structure",
        "Sektorer i porteføljen": "sectors",
        "Industrier i porteføljen": "industries",
        "PE i porteføljen": "pe",
        "Regioner / lande i porteføljen": "regions",
        "Analytiker analyse": "analyst",
    }
    active_key = title_to_key.get(phase3_current_view, "")
    for key, button in buttons.items():
        try:
            if key == active_key:
                button.configure(relief=tk.SUNKEN, bd=3)
            else:
                button.configure(relief=tk.RAISED, bd=2)
        except Exception:
            pass

def update_phase3_industry_controls():
    """Vis to enkle under-visningsknapper kun når Industrier er valgt."""
    frame = globals().get("phase3_industry_controls")
    if frame is None:
        return
    try:
        if phase3_current_view == "Industrier i porteføljen":
            if not frame.winfo_ismapped():
                frame.pack(fill="x", pady=(0, 6), before=phase3_guidance_label)
        else:
            if frame.winfo_ismapped():
                frame.pack_forget()
    except Exception:
        pass

    for mode, button_name in (("flat", "phase3_industry_flat_button"), ("sector", "phase3_industry_sector_button")):
        button = globals().get(button_name)
        if button is None:
            continue
        try:
            button.configure(
                relief=tk.SUNKEN if phase3_industry_mode == mode else tk.RAISED,
                bd=3 if phase3_industry_mode == mode else 2,
            )
        except Exception:
            pass

def _phase3_industry_sector_rows():
    """Byg 'Efter sektor', så hver sektorrække er præcis summen af de viste industrirækker."""
    data_rows = [r for r in phase2_rows if not r.get("is_summary") and not is_cash_row(r)]
    stock_weight_total = sum(float(r.get("sort_weight", 0.0) or 0.0) for r in data_rows)

    def pf_weight(row):
        raw = float(row.get("sort_weight", 0.0) or 0.0)
        return raw / stock_weight_total * 100.0 if stock_weight_total > 0 else 0.0

    # Saml først aktuelle værdier pr. (sektor, industri).
    grouped = {}
    industries_by_sector = {}
    for row in data_rows:
        sector = row.get("sector_group") or mapped_sector(row.get("sector"))
        industry = row.get("industry_group") or clean_category(row.get("industry"), "Industri ukendt")
        if industry == "Industri ukendt":
            continue

        industries_by_sector.setdefault(sector, set()).add(industry)
        key = (sector, industry)

        weight = pf_weight(row)
        fc = parse_float(row.get("analyst_1y_upside_pct"), None)

        g = grouped.setdefault(key, {
            "weight": 0.0,
            "count": 0,
            "fc_sum": 0.0,
            "fc_weight": 0.0,
        })
        g["weight"] += weight
        g["count"] += 1
        if fc is not None:
            g["fc_sum"] += weight * fc
            g["fc_weight"] += weight

    # Brug præcis de samme anbefalede sektormål som i Fase 3 / Sektorer.
    # Der normaliseres ikke op til 100 % ud fra de sektorer, der tilfældigvis
    # findes i den aktuelle portefølje. Mangler en sektor i porteføljen,
    # forbliver dens anbefalede andel derfor synligt "ubrugt" i industrivisningen.
    fixed_sector_targets = {
        sector: max(0.0, parse_float(sector_targets.get(sector, 0.0), 0.0) or 0.0)
        for sector in industries_by_sector
    }

    rows_out = []

    # Vis sektorer efter aktuel vægt, men beregn sektorrækken ud fra børnene.
    all_relevant_sectors = {
        sector for sector in SECTOR_CATEGORIES
        if (parse_float(sector_targets.get(sector, 0.0), 0.0) or 0.0) > 0.0
    } | set(industries_by_sector)

    sector_order = sorted(
        all_relevant_sectors,
        key=lambda s: (
            -sum(grouped.get((s, i), {}).get("weight", 0.0) for i in industries_by_sector.get(s, set())),
            SECTOR_CATEGORIES.index(s) if s in SECTOR_CATEGORIES else 999,
            s,
        ),
    )

    for sector in sector_order:
        # Alfabetisk rækkefølge bruges også i dynamic_industry_targets,
        # så en evt. afrundingsrest lander på samme industri i begge visninger.
        industries = sorted(industries_by_sector.get(sector, set()))
        sector_target = max(
            0.0,
            parse_float(sector_targets.get(sector, 0.0), 0.0) or 0.0,
        )

        if not industries:
            rows_out.append({
                "category": sector,
                "weight": "0,0%",
                "target_weight": format_pct(sector_target).replace("+", ""),
                "count": "0",
                "weighted_fc1y": "-",
                "recommended_count": "-",
                "sector_count": "-",
                "recommended_sector_count": "-",
                "industry_count": "-",
                "region_count": "-",
                "recommended_fc1y": "-",
                "sort_category": sector.casefold(),
                "sort_weight": 0.0,
                "sort_target_weight": sector_target,
                "sort_count": 0,
                "sort_weighted_fc1y": -999999,
                "sort_recommended_count": -999999,
                "sort_sector_count": -999999,
                "sort_recommended_sector_count": -999999,
                "sort_industry_count": -999999,
                "sort_region_count": -999999,
                "sort_recommended_fc1y": -999999,
                "is_industry_sector_group": True,
            })
            continue

        # Fordel sektorens neutrale mål præcist over de viste industrier.
        # Sidste industri får restdifferencen, så de viste 1-decimalsværdier
        # og sektorens samlede mål hænger sammen uden skjult afrundingsrest.
        raw_per_industry_target = sector_target / len(industries)
        rounded_targets = []
        remaining_target = sector_target
        for idx, _industry in enumerate(industries):
            if idx == len(industries) - 1:
                target_value = remaining_target
            else:
                target_value = round(raw_per_industry_target, 1)
                remaining_target -= target_value
            rounded_targets.append(target_value)

        child_rows = []
        for industry, per_industry_target in zip(industries, rounded_targets):
            g = grouped.get((sector, industry), {})
            fc = (
                g.get("fc_sum", 0.0) / g.get("fc_weight", 1.0)
                if g.get("fc_weight", 0.0) > 0
                else None
            )

            child_rows.append({
                "category": "   ↳ " + industry,
                "weight": format_pct(g.get("weight", 0.0)).replace("+", ""),
                "target_weight": format_pct(per_industry_target).replace("+", ""),
                "count": str(g.get("count", 0)),
                "weighted_fc1y": format_pct(fc) if fc is not None else "-",
                "recommended_count": "-",
                "sector_count": "-",
                "recommended_sector_count": "-",
                "industry_count": "-",
                "region_count": "-",
                "recommended_fc1y": "-",
                "sort_category": industry.casefold(),
                "sort_weight": g.get("weight", 0.0),
                "sort_target_weight": per_industry_target,
                "sort_count": g.get("count", 0),
                "sort_weighted_fc1y": fc if fc is not None else -999999,
                "sort_recommended_count": -999999,
                "sort_sector_count": -999999,
                "sort_recommended_sector_count": -999999,
                "sort_industry_count": -999999,
                "sort_region_count": -999999,
                "sort_recommended_fc1y": -999999,
            })

        # VIGTIGT: sektorrækken dannes nu af summen af de viste industrirækker.
        sector_weight = sum(r["sort_weight"] for r in child_rows)
        sector_target_from_children = round(sum(r["sort_target_weight"] for r in child_rows), 10)
        sector_count = sum(r["sort_count"] for r in child_rows)

        # Vægtet FC1Y for sektoren beregnes fortsat ud fra de underliggende positioner.
        sector_fc_sum = sum(grouped.get((sector, i), {}).get("fc_sum", 0.0) for i in industries)
        sector_fc_weight = sum(grouped.get((sector, i), {}).get("fc_weight", 0.0) for i in industries)
        sector_fc = sector_fc_sum / sector_fc_weight if sector_fc_weight > 0 else None

        rows_out.append({
            "category": sector,
            "weight": format_pct(sector_weight).replace("+", ""),
            "target_weight": format_pct(sector_target_from_children).replace("+", ""),
            "count": str(sector_count),
            "weighted_fc1y": format_pct(sector_fc) if sector_fc is not None else "-",
            "recommended_count": "-",
            "sector_count": "-",
            "recommended_sector_count": "-",
            "industry_count": "-",
            "region_count": "-",
            "recommended_fc1y": "-",
            "sort_category": sector.casefold(),
            "sort_weight": sector_weight,
            "sort_target_weight": sector_target_from_children,
            "sort_count": sector_count,
            "sort_weighted_fc1y": sector_fc if sector_fc is not None else -999999,
            "sort_recommended_count": -999999,
            "sort_sector_count": -999999,
            "sort_recommended_sector_count": -999999,
            "sort_industry_count": -999999,
            "sort_region_count": -999999,
            "sort_recommended_fc1y": -999999,
            "is_industry_sector_group": True,
        })

        rows_out.extend(child_rows)

    # Totalrækken beregnes også direkte fra sektorrækkerne.
    sector_rows = [r for r in rows_out if r.get("is_industry_sector_group")]
    total_weight = sum(r["sort_weight"] for r in sector_rows)
    total_target = sum(r["sort_target_weight"] for r in sector_rows)

    weighted_fc, _mean_fc, _median_fc, _coverage, _fc_count = weighted_fc1y_for_rows(
        data_rows, stock_weight_total
    )
    rows_out.insert(0, {
        "category": "Industrier efter sektor – samlet",
        "weight": format_pct(total_weight).replace("+", ""),
        "target_weight": format_pct(total_target).replace("+", ""),
        "count": str(sum(r["sort_count"] for r in sector_rows)),
        "weighted_fc1y": format_pct(weighted_fc) if weighted_fc is not None else "-",
        "recommended_count": "",
        "sector_count": "-",
        "recommended_sector_count": "-",
        "industry_count": "-",
        "region_count": "-",
        "recommended_fc1y": "-",
        "sort_category": "",
        "sort_weight": total_weight,
        "sort_target_weight": total_target,
        "sort_count": sum(r["sort_count"] for r in sector_rows),
        "sort_weighted_fc1y": weighted_fc if weighted_fc is not None else -999999,
        "sort_recommended_count": -999999,
        "sort_sector_count": -999999,
        "sort_recommended_sector_count": -999999,
        "sort_industry_count": -999999,
        "sort_region_count": -999999,
        "sort_recommended_fc1y": -999999,
        "is_summary": True,
    })
    return rows_out

def show_phase3_industries_by_sector():
    global phase3_rows, phase3_current_view, phase3_industry_mode, phase3_current_sort, phase3_descending
    phase3_current_view = "Industrier i porteføljen"
    phase3_industry_mode = "sector"
    phase3_current_sort = ""
    phase3_descending = False
    update_phase3_view_buttons()
    update_phase3_industry_controls()
    phase3_rows = _phase3_industry_sector_rows()
    update_phase3_headers()
    show_phase3()

def aggregate_phase3(group_func, title, analyst_mode=False, target_func=None, all_categories=None, preserve_category_order=False, structure_mode=False, recommended_fc1y_func=None):
    global phase3_rows, phase3_current_view
    phase3_current_view = title
    update_phase3_view_buttons()
    update_phase3_industry_controls()
    data_rows = [r for r in phase2_rows if not r.get("is_summary") and not is_cash_row(r)]
    stock_weight_total = sum(float(r.get("sort_weight", 0.0) or 0.0) for r in data_rows)

    def phase3_weight(row):
        raw_weight = float(row.get("sort_weight", 0.0) or 0.0)
        return raw_weight / stock_weight_total * 100.0 if stock_weight_total > 0 else 0.0

    total_positions = len(data_rows)
    grouped = {}
    for r in data_rows:
        category = group_func(r)
        weight = phase3_weight(r)
        fc = parse_float(r.get("analyst_1y_upside_pct"), None)
        if category not in grouped:
            grouped[category] = {
                "weight_raw": 0.0, "count_raw": 0,
                "fc_weighted_sum": 0.0, "fc_weight_raw": 0.0,
                "sectors": set(), "industries": set(), "regions": set(),
            }
        group = grouped[category]
        group["weight_raw"] += weight
        group["count_raw"] += 1
        sector_name = r.get("sector_group") or mapped_sector(r.get("sector"))
        industry_name = clean_category(r.get("industry"), "Industri ukendt")
        region_name = r.get("region_group") or mapped_region(r.get("country"))
        if sector_name and sector_name != "Andre sektorer":
            group["sectors"].add(sector_name)
        if industry_name and industry_name != "Industri ukendt":
            group["industries"].add(industry_name)
        if region_name:
            group["regions"].add(region_name)
        if fc is not None:
            group["fc_weighted_sum"] += weight * fc
            group["fc_weight_raw"] += weight

    rows_out = []
    if analyst_mode:
        ordered_categories = [label for label, _low, _high in FC1Y_BUCKETS]
        if any(category not in ordered_categories for category in grouped):
            ordered_categories.append("FC1Y ukendt")
    elif all_categories is not None:
        ordered_categories = list(all_categories)
        extra_categories = [category for category in grouped if category not in ordered_categories]
        ordered_categories.extend(sorted(extra_categories, key=lambda c: grouped[c]["weight_raw"], reverse=True))
    else:
        ordered_categories = sorted(grouped.keys(), key=lambda c: grouped[c]["weight_raw"], reverse=True)

    for category in ordered_categories:
        vals = grouped.get(category, {
            "weight_raw": 0.0, "count_raw": 0, "fc_weighted_sum": 0.0, "fc_weight_raw": 0.0,
            "sectors": set(), "industries": set(), "regions": set(),
        })
        group_fc = vals["fc_weighted_sum"] / vals["fc_weight_raw"] if vals["fc_weight_raw"] > 0 else None
        target_weight = target_func(category) if target_func is not None else None

        layer = structure_layer_from_display(category) if structure_mode else ""
        recommended_count = total_positions * STRUCTURE_RECOMMENDED_POSITION_SHARE.get(layer, 0.0) / 100.0 if structure_mode else None
        recommended_sector_count = STRUCTURE_RECOMMENDED_SECTOR_MIN.get(layer) if structure_mode else None
        sector_count = len(vals["sectors"]) if structure_mode else None
        industry_count = len(vals["industries"]) if structure_mode else None
        region_count = len(vals["regions"]) if structure_mode else None
        recommended_fc1y = recommended_fc1y_func(category) if recommended_fc1y_func is not None else None

        rows_out.append({
            "category": category,
            "weight": format_pct(vals["weight_raw"]).replace("+", ""),
            "target_weight": format_pct(target_weight).replace("+", "") if target_weight is not None else "-",
            "count": str(vals["count_raw"]),
            "recommended_count": str(int(recommended_count + 0.5)) if recommended_count is not None else "-",
            "sector_count": str(sector_count) if sector_count is not None else "-",
            "recommended_sector_count": (f"Min. {recommended_sector_count}" if recommended_sector_count is not None else "-"),
            "industry_count": str(industry_count) if industry_count is not None else "-",
            "region_count": str(region_count) if region_count is not None else "-",
            "weighted_fc1y": format_pct(group_fc) if group_fc is not None else "-",
            "recommended_fc1y": format_pct(recommended_fc1y).replace("+", "") if recommended_fc1y is not None else "-",
            "sort_category": category.casefold(),
            "sort_weight": vals["weight_raw"],
            "sort_target_weight": target_weight if target_weight is not None else -999999,
            "sort_count": vals["count_raw"],
            "sort_recommended_count": recommended_count if recommended_count is not None else -999999,
            "sort_sector_count": sector_count if sector_count is not None else -999999,
            "sort_recommended_sector_count": recommended_sector_count if recommended_sector_count is not None else -999999,
            "sort_industry_count": industry_count if industry_count is not None else -999999,
            "sort_region_count": region_count if region_count is not None else -999999,
            "sort_weighted_fc1y": group_fc if group_fc is not None else -999999,
            "sort_recommended_fc1y": recommended_fc1y if recommended_fc1y is not None else -999999,
        })

    if not analyst_mode and not preserve_category_order:
        rows_out.sort(key=lambda x: x["sort_weight"], reverse=True)

    total_weight = sum(r.get("sort_weight", 0.0) for r in rows_out)
    total_target_weight = sum(r.get("sort_target_weight", 0.0) for r in rows_out if r.get("sort_target_weight", -999999) != -999999)
    total_count = sum(r.get("sort_count", 0) for r in rows_out)
    weighted_fc, mean_fc, median_fc, fc_weight_coverage, fc_count = weighted_fc1y_for_rows(data_rows, stock_weight_total)

    summary = {
        "category": f"{title} – samlet",
        "weight": format_pct(total_weight).replace("+", ""),
        "target_weight": format_pct(total_target_weight).replace("+", "") if target_func is not None else "-",
        "count": str(total_count),
        "recommended_count": "",
        "sector_count": str(len({r.get('sector_group') or mapped_sector(r.get('sector')) for r in data_rows if (r.get('sector_group') or mapped_sector(r.get('sector'))) != 'Andre sektorer'})) if structure_mode else "-",
        "recommended_sector_count": "Min. 11" if structure_mode else "-",
        "industry_count": str(len({clean_category(r.get('industry'), 'Industri ukendt') for r in data_rows if clean_category(r.get('industry'), 'Industri ukendt') != 'Industri ukendt'})) if structure_mode else "-",
        "region_count": str(len({r.get('region_group') or mapped_region(r.get('country')) for r in data_rows})) if structure_mode else "-",
        "weighted_fc1y": format_pct(weighted_fc) if weighted_fc is not None else "-",
        "recommended_fc1y": "-",
        "sort_category": "", "sort_weight": total_weight,
        "sort_target_weight": total_target_weight if target_func is not None else -999999,
        "sort_count": total_count, "sort_recommended_count": -999999,
        "sort_sector_count": -999999, "sort_recommended_sector_count": -999999,
        "sort_industry_count": -999999, "sort_region_count": -999999,
        "sort_weighted_fc1y": weighted_fc if weighted_fc is not None else -999999,
        "sort_recommended_fc1y": -999999, "is_summary": True,
    }

    if analyst_mode:
        common = {
            "target_weight": "-", "recommended_count": "-", "sector_count": "-",
            "recommended_sector_count": "-", "industry_count": "-", "region_count": "-", "recommended_fc1y": "-",
            "sort_target_weight": -999999, "sort_recommended_count": -999999,
            "sort_sector_count": -999999, "sort_recommended_sector_count": -999999,
            "sort_industry_count": -999999, "sort_region_count": -999999, "sort_recommended_fc1y": -999999,
            "is_summary": True,
        }
        mean_row = dict(common, category="FC1Y middelværdi for porteføljen", weight=f"Dækning {format_pct(fc_weight_coverage).replace('+', '')}", count=f"{fc_count}/{total_count}", weighted_fc1y=format_pct(mean_fc) if mean_fc is not None else "-", sort_category="", sort_weight=fc_weight_coverage, sort_count=fc_count, sort_weighted_fc1y=mean_fc if mean_fc is not None else -999999)
        median_row = dict(common, category="FC1Y median for porteføljen", weight=f"Dækning {format_pct(fc_weight_coverage).replace('+', '')}", count=f"{fc_count}/{total_count}", weighted_fc1y=format_pct(median_fc) if median_fc is not None else "-", sort_category="", sort_weight=fc_weight_coverage, sort_count=fc_count, sort_weighted_fc1y=median_fc if median_fc is not None else -999999)
        phase3_rows = [summary, mean_row, median_row] + rows_out if rows_out else []
    else:
        phase3_rows = [summary] + rows_out if rows_out else []

    show_phase3()
    status_var.set(f"Fase 3 viser nu: {title}. Grupper: {len(rows_out)}")


def recalculate_structure_scores():
    """Genberegn Strukturscore og lag fra de allerede hentede Fase 2-data."""
    for row in phase2_rows:
        if row.get("is_summary") or is_cash_row(row):
            continue
        size_score = market_cap_structure_score(
            row.get("structure_market_cap_raw"),
            currency=row.get("structure_currency_raw", "USD"),
            fx_to_dkk=row.get("structure_fx_to_dkk_raw", 1.0),
            usd_to_dkk=row.get("structure_usd_to_dkk_raw", FALLBACK_FX_DKK["USD"]),
        )
        quality = parse_float(row.get("structure_quality_raw"), 50.0)
        robustness = parse_float(row.get("structure_robustness_raw"), 50.0)
        maturity = parse_float(row.get("structure_financial_maturity_raw"), 50.0)
        raw_score = clamp(0.45 * size_score + 0.30 * quality + 0.15 * maturity + 0.10 * robustness)
        penalty = speculation_penalty_from_bull(row.get("structure_bull_raw"))
        score = clamp(raw_score - penalty)
        layer = structure_layer_from_score(score)
        row["structure_score_before_penalty"] = raw_score
        row["speculation_penalty_raw"] = penalty
        row["structure_score"] = format_num(score, 0)
        row["sort_structure_score"] = score
        row["structure_layer"] = layer
        row["sort_structure_layer"] = STRUCTURE_LAYER_ORDER.index(layer)
    show_phase2()
    show_portfolio_structure()


def open_market_cap_settings():
    global market_cap_limits_usd
    win = tk.Toplevel(root)
    win.title("Indstil Market Cap-grænser")
    win.geometry("620x510")
    win.minsize(560, 460)
    win.transient(root)
    tk.Label(win, text="TradingViews Market Cap-kategorier. Beløb angives i mio. USD.", font=small_font, anchor="w").pack(fill="x", padx=12, pady=(12, 8))
    table = tk.Frame(win)
    table.pack(fill="both", expand=True, padx=12)
    tk.Label(table, text="Kategori", font=small_font, width=18, anchor="w").grid(row=0, column=0, padx=6, pady=5)
    tk.Label(table, text="Øvre grænse, mio. USD", font=small_font).grid(row=0, column=1, padx=6, pady=5)
    tk.Label(table, text="Score", font=small_font).grid(row=0, column=2, padx=6, pady=5)
    entries=[]
    for i,(upper,name,score) in enumerate(market_cap_limits_usd, start=1):
        tk.Label(table,text=name,font=small_font,anchor="w").grid(row=i,column=0,padx=6,pady=4,sticky="w")
        upper_var=tk.StringVar(value="" if upper is None else format_num(upper/1_000_000.0,1))
        score_var=tk.StringVar(value=format_num(score,0))
        ent=tk.Entry(table,textvariable=upper_var,width=18,justify="center",font=small_font)
        ent.grid(row=i,column=1,padx=6,pady=4)
        if upper is None:
            ent.configure(state="disabled")
        tk.Entry(table,textvariable=score_var,width=10,justify="center",font=small_font).grid(row=i,column=2,padx=6,pady=4)
        entries.append((upper_var,score_var,name,upper is None))

    def reset_entries():
        for (uvar,svar,_name,is_terminal),(upper,_n,score) in zip(entries,DEFAULT_MARKET_CAP_LIMITS_USD):
            if not is_terminal:
                uvar.set(format_num(upper/1_000_000.0,1))
            svar.set(format_num(score,0))

    def save_entries():
        global market_cap_limits_usd
        try:
            rows=[]
            for uvar,svar,name,is_terminal in entries:
                upper=None if is_terminal else normalize_number(uvar.get(),None)
                if not is_terminal and (upper is None or upper <= 0):
                    raise ValueError("Alle fem Market Cap-grænser skal være positive tal.")
                score=normalize_number(svar.get(),None)
                if score is None or not 0 <= score <= 100:
                    raise ValueError("Alle scorer skal ligge mellem 0 og 100.")
                rows.append([None if is_terminal else float(upper)*1_000_000.0,name,float(score)])
            finite=[r[0] for r in rows if r[0] is not None]
            if any(finite[i] >= finite[i+1] for i in range(len(finite)-1)):
                raise ValueError("Market Cap-grænserne skal være strengt stigende.")
            scores=[r[2] for r in rows]
            if any(scores[i] > scores[i+1] for i in range(len(scores)-1)):
                raise ValueError("Scorerne skal være stigende eller uændrede.")
            market_cap_limits_usd=rows
            save_structure_settings()
            recalculate_structure_scores()
            win.destroy()
        except Exception as exc:
            messagebox.showerror("Ugyldige indstillinger",str(exc),parent=win)

    bar=tk.Frame(win); bar.pack(fill="x",padx=12,pady=12)
    tk.Button(bar,text="Nulstil standard",font=small_font,command=reset_entries).pack(side="left")
    tk.Button(bar,text="Annuller",font=small_font,command=win.destroy).pack(side="right")
    tk.Button(bar,text="Gem og anvend",font=small_font,command=save_entries).pack(side="right",padx=(0,8))


def open_speculation_settings():
    global speculation_penalties
    win = tk.Toplevel(root)
    win.title("Indstil spekulativ straf")
    win.geometry("520x560")
    win.minsize(470, 500)
    win.transient(root)
    tk.Label(win, text="Strukturscoren reduceres kun ved ekstreme Bull-forventninger. Højeste overskredne grænse anvendes.", font=small_font, anchor="w", justify="left", wraplength=485).pack(fill="x", padx=12, pady=(12, 8))
    table=tk.Frame(win); table.pack(fill="both",expand=True,padx=12)
    tk.Label(table,text="Bull over %",font=small_font).grid(row=0,column=0,padx=8,pady=5)
    tk.Label(table,text="Scorestraf",font=small_font).grid(row=0,column=1,padx=8,pady=5)
    entries=[]
    for i,(threshold,penalty) in enumerate(speculation_penalties,start=1):
        tvar=tk.StringVar(value=format_num(threshold,0)); pvar=tk.StringVar(value=format_num(penalty,0))
        tk.Entry(table,textvariable=tvar,width=14,justify="center",font=small_font).grid(row=i,column=0,padx=8,pady=4)
        tk.Entry(table,textvariable=pvar,width=14,justify="center",font=small_font).grid(row=i,column=1,padx=8,pady=4)
        entries.append((tvar,pvar))

    def reset_entries():
        for (tvar,pvar),(threshold,penalty) in zip(entries,DEFAULT_SPECULATION_PENALTIES):
            tvar.set(format_num(threshold,0)); pvar.set(format_num(penalty,0))

    def save_entries():
        global speculation_penalties
        try:
            points=[]
            for tvar,pvar in entries:
                threshold=normalize_number(tvar.get(),None); penalty=normalize_number(pvar.get(),None)
                if threshold is None or penalty is None:
                    raise ValueError("Alle felter skal indeholde tal.")
                if threshold < 0 or penalty < 0 or penalty > 100:
                    raise ValueError("Bull-grænser skal være positive, og straf skal ligge mellem 0 og 100.")
                points.append([float(threshold),float(penalty)])
            points.sort(key=lambda row: row[0])
            if any(points[i][0] >= points[i+1][0] for i in range(len(points)-1)):
                raise ValueError("Bull-grænserne skal være strengt stigende.")
            if any(points[i][1] > points[i+1][1] for i in range(len(points)-1)):
                raise ValueError("Straffen skal være stigende eller uændret.")
            speculation_penalties=points
            save_structure_settings()
            recalculate_structure_scores()
            win.destroy()
        except Exception as exc:
            messagebox.showerror("Ugyldige indstillinger",str(exc),parent=win)

    bar=tk.Frame(win); bar.pack(fill="x",padx=12,pady=12)
    tk.Button(bar,text="Nulstil standard",font=small_font,command=reset_entries).pack(side="left")
    tk.Button(bar,text="Annuller",font=small_font,command=win.destroy).pack(side="right")
    tk.Button(bar,text="Gem og anvend",font=small_font,command=save_entries).pack(side="right",padx=(0,8))


def on_structure_profile_selected(*_args):
    global saved_structure_profile
    profile = structure_profile_var.get()
    if profile in STRUCTURE_PROFILES:
        saved_structure_profile = profile
        save_structure_settings()
    show_portfolio_structure()


def _phase3_target_history_series():
    """Byg den aktuelt byggede porteføljes samlede kursmålstidsserie.

    Kun aktier i den aktuelle Fase 2-portefølje indgår. På hver registreret
    historikdato bruges den senest kendte komplette observation for hver aktie.
    Absolutte mål og faktisk kurs normaliseres til DKK med den aktuelle kendte
    valutakurs (ellers fallback), mens procentmål beregnes direkte fra hvert
    historisk snapshot. Hver akties kursudvikling sættes til 0 % ved dens første
    komplette historikpunkt, hvorefter gennemsnittet bruges som diskret PF-kurve.
    """
    data = load_target_age_history()
    positions = data.get("positions", {}) if isinstance(data, dict) else {}
    active_items = [item for item in portfolio if not is_cash_item(item)]
    if not active_items:
        return []

    fx_rates = {"DKK": 1.0}
    try:
        cache = load_daily_cache()
        for key, value in (cache.get("fx_rates", {}) or {}).items():
            parsed = parse_float(value, None)
            if parsed is not None and parsed > 0:
                fx_rates[str(key).upper()] = float(parsed)
    except Exception:
        pass
    for currency, fallback in FALLBACK_FX_DKK.items():
        fx_rates.setdefault(currency, float(fallback))

    histories = {}
    event_dates = set()
    for item in active_items:
        key = position_key(item)
        entry = positions.get(key, {}) if isinstance(positions, dict) else {}
        complete = _complete_history_entries(entry.get("history", []) if isinstance(entry, dict) else [])
        cleaned = []
        for point in complete:
            try:
                point_date = date.fromisoformat(str(point.get("date", ""))[:10])
            except Exception:
                continue
            if point_date > date.today():
                continue
            row = dict(point)
            row["_date"] = point_date
            cleaned.append(row)
            event_dates.add(point_date)
        cleaned.sort(key=lambda x: x["_date"])
        if cleaned:
            histories[key] = (item, cleaned)

    if not histories or not event_dates:
        return []

    event_dates.add(date.today())
    series = []
    for point_date in sorted(event_dates):
        absolute = {"bear": [], "base": [], "bull": []}
        actual_prices_dkk = []
        percentages = {"bear": [], "base": [], "bull": []}
        portfolio_changes = []
        contributors = 0

        for _key, (item, history) in histories.items():
            latest = None
            for candidate in history:
                if candidate["_date"] <= point_date:
                    latest = candidate
                else:
                    break
            if latest is None:
                continue

            price = parse_float(latest.get("price"), None)
            bear = parse_float(latest.get("bear_target"), None)
            base = parse_float(latest.get("base_target"), None)
            bull = parse_float(latest.get("bull_target"), None)
            if price is None or price <= 0 or any(v is None or v <= 0 for v in (bear, base, bull)):
                continue

            currency = currency_for_exchange(item.get("exchange"))
            fx = fx_rates.get(currency, FALLBACK_FX_DKK.get(currency, 1.0))
            absolute["bear"].append(bear * fx)
            absolute["base"].append(base * fx)
            absolute["bull"].append(bull * fx)
            actual_prices_dkk.append(price * fx)
            percentages["bear"].append((bear / price - 1.0) * 100.0)
            percentages["base"].append((base / price - 1.0) * 100.0)
            percentages["bull"].append((bull / price - 1.0) * 100.0)

            first_price = parse_float(history[0].get("price"), None) if history else None
            if first_price is not None and first_price > 0:
                portfolio_changes.append((price / first_price - 1.0) * 100.0)
            contributors += 1

        if contributors:
            series.append({
                "date": point_date,
                "count": contributors,
                "bear_abs": sum(absolute["bear"]) / len(absolute["bear"]),
                "base_abs": sum(absolute["base"]) / len(absolute["base"]),
                "bull_abs": sum(absolute["bull"]) / len(absolute["bull"]),
                "price_abs": (sum(actual_prices_dkk) / len(actual_prices_dkk)) if actual_prices_dkk else None,
                "bear_pct": sum(percentages["bear"]) / len(percentages["bear"]),
                "base_pct": sum(percentages["base"]) / len(percentages["base"]),
                "bull_pct": sum(percentages["bull"]) / len(percentages["bull"]),
                "portfolio_pct": (sum(portfolio_changes) / len(portfolio_changes)) if portfolio_changes else None,
            })
    return series


def refresh_phase3_target_analysis(event=None):
    """Opdatér begge grafer i Fase 3 -> Kursmålsanalyse samlet."""
    if "phase3_target_abs_canvas" not in globals():
        return
    series = _phase3_target_history_series()
    try:
        _phase3_target_fit_width()
    except Exception:
        pass
    _draw_phase3_target_chart(
        phase3_target_abs_canvas, series,
        ("bear_abs", "base_abs", "bull_abs"),
        "Samlede absolutte kursmål over tid",
        "Gennemsnitligt kursmål (DKK)",
        percent=False,
        overlay_key="price_abs",
        overlay_label="PF",
    )
    _draw_phase3_target_chart(
        phase3_target_pct_canvas, series,
        ("bear_pct", "base_pct", "bull_pct"),
        "Samlede procentuelle kursmål over tid",
        "Gennemsnitligt potentiale (%)",
        percent=True,
        overlay_key="portfolio_pct",
        overlay_label="PF",
    )
    if "phase3_target_status_var" in globals():
        if series:
            phase3_target_status_var.set(
                f"{len(series)} tidsregistreringer fra {series[0]['date'].strftime('%d-%m-%Y')} til {series[-1]['date'].strftime('%d-%m-%Y')}. "
                f"Seneste punkt bygger på {series[-1]['count']} aktier i den byggede portefølje med kendt historik."
            )
        else:
            phase3_target_status_var.set("Ingen komplette kursmålshistorikdata for den byggede portefølje endnu.")


def sort_phase3_rows(col):
    """Sortér den aktuelle Fase 3-visning via kolonneoverskriften.

    Summerings-/analyse-rækker holdes fast øverst. Kategori sorteres alfabetisk,
    mens procent-, antal- og FC1Y-kolonner sorteres numerisk via de eksisterende
    sort_* råværdier.
    """
    global phase3_rows, phase3_current_sort, phase3_descending
    if not phase3_rows:
        return

    if phase3_current_sort == col:
        phase3_descending = not phase3_descending
    else:
        phase3_current_sort = col
        # Samme stil som de øvrige tabeller: tekst starter A-Å,
        # tal starter med højeste værdi øverst.
        phase3_descending = False if col == "category" else True

    fixed_rows = [row for row in phase3_rows if row.get("is_summary")]
    data_rows = [row for row in phase3_rows if not row.get("is_summary")]

    data_rows.sort(
        key=lambda row: row.get("sort_" + col, ""),
        reverse=phase3_descending,
    )
    phase3_rows = fixed_rows + data_rows
    update_phase3_headers()
    show_phase3()



def update_phase3_headers():
    """Vis relevante Fase 3-kolonner og aktiv sortering med ▲/▼."""
    if "phase3_tree" not in globals():
        return
    if phase3_current_view == "Struktur":
        visible = ("category", "weight", "target_weight", "count", "recommended_count", "sector_count", "recommended_sector_count", "industry_count", "region_count", "weighted_fc1y")
    elif phase3_current_view == "Analytiker analyse":
        visible = ("category", "weight", "target_weight", "count", "weighted_fc1y", "recommended_fc1y")
    else:
        visible = ("category", "weight", "target_weight", "count", "weighted_fc1y")
    phase3_tree.configure(displaycolumns=visible)
    for col_id, title, _width in PHASE3_COLUMNS:
        if col_id == "category" and phase3_current_view == "Struktur":
            display_title = "Strukturlag"
        elif col_id == "target_weight" and phase3_current_view == "Industrier i porteføljen":
            display_title = "Neutral anbefalet %PF"
        else:
            display_title = title
        arrow = ""
        if col_id == phase3_current_sort:
            arrow = " ▼" if phase3_descending else " ▲"
        phase3_tree.heading(col_id, text=display_title + arrow, command=lambda c=col_id: sort_phase3_rows(c))
        if col_id == "target_weight":
            if phase3_current_view == "Industrier i porteføljen":
                phase3_tree.column(col_id, width=220, minwidth=220)
            else:
                phase3_tree.column(col_id, width=155, minwidth=120)

    if "phase3_guidance_var" in globals():
        if phase3_current_view == "Struktur":
            data_rows = [r for r in phase2_rows if not r.get("is_summary") and not is_cash_row(r)]
            positions = len(data_rows)
            sectors = {r.get("sector_group") or mapped_sector(r.get("sector")) for r in data_rows}
            sectors.discard("Andre sektorer")
            rec_fundament = int(positions * 0.40 + 0.5)
            rec_growth = int(positions * 0.30 + 0.5)
            rec_accelerator = int(positions * 0.20 + 0.5)
            rec_potential = int(positions * 0.10 + 0.5)
            phase3_guidance_var.set(
                "Porteføljevejledning:\n"
                f"Aktuel portefølje: {positions} positioner og {len(sectors)} forskellige sektorer.\n"
                "Anbefalet antal positioner: minimum 20 og maksimum 50 forskellige aktier.\n"
                "Anbefalet sektorspredning: minimum 11 forskellige sektorer.\n"
                "\n"
                f"Anbefalet antal positioner i hvert strukturlag beregnes ud fra porteføljens aktuelle {positions} positioner. "
                "Fordelingen forudsætter, at porteføljen indeholder mindst 20 positioner.\n"
                f"Fundament: 40 % × {positions} = {rec_fundament} positioner.\n"
                f"Vækst: 30 % × {positions} = {rec_growth} positioner.\n"
                f"Accelerator: 20 % × {positions} = {rec_accelerator} positioner.\n"
                f"Potentiale: 10 % × {positions} = {rec_potential} positioner."
            )
        else:
            phase3_guidance_var.set("")



def show_phase3_sectors():
    aggregate_phase3(
        lambda r: r.get("sector_group") or mapped_sector(r.get("sector")),
        "Sektorer i porteføljen",
        target_func=lambda category: sector_targets.get(category, 0.0),
        all_categories=SECTOR_CATEGORIES,
    )



def show_phase3_industries():
    global phase3_industry_mode, phase3_rows
    phase3_industry_mode = "flat"
    data_rows = [r for r in phase2_rows if not r.get("is_summary") and not is_cash_row(r)]
    targets = dynamic_industry_targets(data_rows)
    aggregate_phase3(
        lambda r: r.get("industry_group") or clean_category(r.get("industry"), "Industri ukendt"),
        "Industrier i porteføljen",
        target_func=lambda category: targets.get(category, 0.0),
    )

    # Sektorer med anbefalet vægt, men uden nogen industri i porteføljen,
    # skal stadig medregnes i den neutrale industrifordeling.
    represented_sectors = {
        r.get("sector_group") or mapped_sector(r.get("sector"))
        for r in data_rows
        if (r.get("industry_group") or clean_category(r.get("industry"), "Industri ukendt")) != "Industri ukendt"
    }
    missing_target = sum(
        max(0.0, parse_float(sector_targets.get(sector, 0.0), 0.0) or 0.0)
        for sector in SECTOR_CATEGORIES
        if sector not in represented_sectors
    )

    if missing_target > 0.000001:
        # Find summary-rækken og indsæt "Andre industrier" lige efter denne.
        row = {
            "category": "Andre industrier",
            "weight": "0,0%",
            "target_weight": format_pct(missing_target).replace("+", ""),
            "count": "0",
            "weighted_fc1y": "-",
            "recommended_count": "-",
            "sector_count": "-",
            "recommended_sector_count": "-",
            "industry_count": "-",
            "region_count": "-",
            "recommended_fc1y": "-",
            "sort_category": "andre industrier",
            "sort_weight": 0.0,
            "sort_target_weight": missing_target,
            "sort_count": 0,
            "sort_weighted_fc1y": -999999,
            "sort_recommended_count": -999999,
            "sort_sector_count": -999999,
            "sort_recommended_sector_count": -999999,
            "sort_industry_count": -999999,
            "sort_region_count": -999999,
            "sort_recommended_fc1y": -999999,
        }
        # Restkategorien vises til sidst efter alle faktiske industrier.
        phase3_rows.append(row)

        # Opdatér totalens neutrale anbefaling til summen af alle rækker.
        if phase3_rows and phase3_rows[0].get("is_summary"):
            total_target = sum(
                r.get("sort_target_weight", 0.0) or 0.0
                for r in phase3_rows[1:]
            )
            phase3_rows[0]["target_weight"] = format_pct(total_target).replace("+", "")
            phase3_rows[0]["sort_target_weight"] = total_target

        show_phase3()



def show_phase3_regions():
    aggregate_phase3(
        lambda r: r.get("region_group") or mapped_region(r.get("country")),
        "Regioner / lande i porteføljen",
        target_func=lambda category: region_targets.get(category, 0.0),
        all_categories=REGION_CATEGORIES,
    )



def show_phase3_pe():
    aggregate_phase3(
        lambda r: pe_bucket_label(r.get("pe")),
        "PE i porteføljen",
        target_func=lambda category: PE_TARGET_WEIGHTS.get(category),
        all_categories=[label for label, _low, _high in PE_BUCKETS],
        preserve_category_order=True,
    )



def show_phase3_analyst():
    aggregate_phase3(
        lambda r: fc1y_bucket_label(r.get("analyst_1y_upside_pct")),
        "Analytiker analyse",
        analyst_mode=True,
        target_func=lambda category: FC1Y_TARGET_WEIGHTS.get(category),
        recommended_fc1y_func=lambda category: FC1Y_RECOMMENDED_LEVELS.get(category),
    )



def show_phase3_structure():
    """Vis strukturfordelingen mod de mål, der faktisk er valgt i Fase 1."""
    global phase3_current_sort, phase3_descending
    try:
        current_settings = collect_builder_settings_from_ui() if "builder_structure_vars" in globals() else load_builder_settings()
        targets = dict(current_settings.get("structure_targets", STRUCTURE_PROFILES["Balanceret"]["targets"]))
    except Exception:
        targets = dict(STRUCTURE_PROFILES["Balanceret"]["targets"])
    phase3_current_sort = "category"
    phase3_descending = False
    aggregate_phase3(
        lambda r: structure_layer_display(r.get("structure_layer") or "Potentiale"),
        "Struktur",
        target_func=lambda category: targets.get(structure_layer_from_display(category), 0.0),
        all_categories=[structure_layer_display(layer) for layer in STRUCTURE_LAYER_ORDER],
        preserve_category_order=True,
        structure_mode=True,
    )




def show_phase3():
    update_phase3_headers()
    phase3_tree.delete(*phase3_tree.get_children())
    for i, r in enumerate(phase3_rows):
        values = [r.get(c, "") for c in PHASE3_COLUMN_IDS]
        if r.get("is_summary"):
            tag = "summary"
        elif r.get("is_industry_sector_group"):
            tag = "industry_sector_group"
        else:
            tag = "even" if i % 2 == 0 else "odd"
        phase3_tree.insert("", "end", values=values, tags=(tag,))



def show_portfolio_structure(*_args):
    """Vis alle aktier grupperet i de fire strukturlag."""
    if "structure_tree" not in globals():
        return
    structure_tree.delete(*structure_tree.get_children())
    profile_name = structure_profile_var.get() if "structure_profile_var" in globals() else "Balanceret"
    profile = STRUCTURE_PROFILES.get(profile_name, STRUCTURE_PROFILES["Balanceret"])
    targets = profile["targets"]
    if "structure_description_var" in globals():
        structure_description_var.set(profile["description"])

    data_rows = [r for r in phase2_rows if not r.get("is_summary") and not is_cash_row(r)]
    # Fase 2-vægtene inkluderer bevidst kontanter. I Porteføljestruktur
    # normaliseres aktierne derimod til 100 %, så lagene kan sammenlignes
    # direkte med Anbefalet lagandel uanset kontantbeholdningens størrelse.
    stock_weight_total = sum(parse_float(r.get("weight"), 0.0) or 0.0 for r in data_rows)

    def structure_weight(row):
        raw_weight = parse_float(row.get("weight"), 0.0) or 0.0
        return raw_weight / stock_weight_total * 100.0 if stock_weight_total > 0 else 0.0

    grouped = {layer: [] for layer in STRUCTURE_LAYER_ORDER}
    for row in data_rows:
        grouped.setdefault(row.get("structure_layer", "Potentiale"), []).append(row)

    for layer in STRUCTURE_LAYER_ORDER:
        layer_rows = grouped.get(layer, [])
        layer_rows.sort(key=lambda r: r.get("sort_structure_score", -999999), reverse=True)
        actual = sum(structure_weight(r) for r in layer_rows)
        target = targets.get(layer, 0.0)
        deviation = actual - target

        parent = structure_tree.insert(
            "", "end",
            values=(
                structure_layer_display(layer), "", "", f"{len(layer_rows)} aktier",
                "", format_pct(actual).replace("+", ""),
                format_pct(target).replace("+", ""), format_pct(deviation),
            ),
            tags=("structure_group",),
            open=True,
        )
        for i, row in enumerate(layer_rows):
            structure_tree.insert(
                parent, "end",
                values=(
                    "", row.get("exchange", ""), row.get("ticker", ""), row.get("name", ""),
                    row.get("structure_score", "-"), format_pct(structure_weight(row)).replace("+", ""), "", "",
                ),
                tags=("even" if i % 2 == 0 else "odd",),
            )

    total_weight = sum(structure_weight(r) for r in data_rows)
    structure_status_var.set(
        f"Samlet aktievægt uden kontanter: {format_pct(total_weight).replace('+', '')}. "
        "Strukturscore: 70-100 Fundament · 56-69 Vækst · 40-55 Accelerator · 0-39 Potentiale."
    )




def _portfolio_profile_distribution(data_rows, field_name, categories=None):
    """Returnér procentfordeling på aktiedelen uden kontanter."""
    stock_weight_total = sum(parse_float(r.get("weight"), 0.0) or 0.0 for r in data_rows)
    result = {category: 0.0 for category in (categories or [])}
    for row in data_rows:
        raw_weight = parse_float(row.get("weight"), 0.0) or 0.0
        normalized = raw_weight / stock_weight_total * 100.0 if stock_weight_total > 0 else 0.0
        category = row.get(field_name)
        if category:
            result[category] = result.get(category, 0.0) + normalized
    return result


def _industry_sector_guess(industry_name):
    """Praktisk kobling mellem TradingViews industri og programmets brede sektorgrupper."""
    name = str(industry_name or "").casefold()
    rules = [
        ("Teknologi", ("software", "semiconductor", "computer", "data processing", "information technology", "electronic component", "electronic production")),
        ("Finans", ("bank", "finance", "insurance", "investment", "financial publishing", "rental/leasing", "mutual funds")),
        ("Sundhed", ("pharmaceutical", "biotechnology", "medical", "health care", "hospital", "nursing")),
        ("Energi", ("oil", "gas production", "integrated oil")),
        ("Materialer", ("metal", "mineral", "steel", "chemical", "forest products", "agricultural commodities")),
        ("Forsyning", ("utilities",)),
        ("Transport", ("transportation", "freight", "courier", "airline")),
        ("Kommunikation", ("telecommunication",)),
        ("Forbrug defensivt", ("beverages", "food retail", "household", "personal care", "consumer sundries")),
        ("Forbrug cyklisk", ("retail", "apparel", "footwear", "motor vehicles", "recreational", "specialty stores", "hotel", "resort", "cruise")),
        ("Industri", ("aerospace", "defense", "machinery", "engineering", "construction", "electrical products", "commercial services", "producer")),
    ]
    for sector, keywords in rules:
        if any(keyword in name for keyword in keywords):
            return sector
    return "Andre sektorer"


def calculate_perfect_stock_profile():
    """Beregn den profil, som bedst udfylder porteføljens største strukturelle mangler."""
    data_rows = [r for r in phase2_rows if not r.get("is_summary") and not is_cash_row(r)]
    if not data_rows:
        return None

    region_actual = _portfolio_profile_distribution(data_rows, "region_group", REGION_CATEGORIES)
    sector_actual = _portfolio_profile_distribution(data_rows, "sector_group", SECTOR_CATEGORIES)
    industry_actual = _portfolio_profile_distribution(data_rows, "industry_group")

    region_rank = sorted(
        ((region_targets.get(name, 0.0) - region_actual.get(name, 0.0), name, region_actual.get(name, 0.0), region_targets.get(name, 0.0))
         for name in REGION_CATEGORIES if region_targets.get(name, 0.0) > 0),
        reverse=True,
    )
    sector_rank = sorted(
        ((sector_targets.get(name, 0.0) - sector_actual.get(name, 0.0), name, sector_actual.get(name, 0.0), sector_targets.get(name, 0.0))
         for name in SECTOR_CATEGORIES if sector_targets.get(name, 0.0) > 0),
        reverse=True,
    )

    best_region = region_rank[0] if region_rank else (0.0, "Andre lande", 0.0, 0.0)
    best_sector = sector_rank[0] if sector_rank else (0.0, "Andre sektorer", 0.0, 0.0)

    # Industrier prioriteres inden for den mest manglende sektor. Alle kendte og allerede
    # observerede industrier kan vælges, så en helt fraværende industri også kan foreslås.
    industry_universe = set(DEFAULT_KNOWN_INDUSTRIES) | set(industry_target_overrides) | set(industry_actual)
    compatible = [name for name in industry_universe if name != "Industri ukendt" and _industry_sector_guess(name) == best_sector[1]]
    if not compatible:
        compatible = [name for name in industry_universe if name != "Industri ukendt"]
    industry_rank = sorted(
        ((industry_target_for(name) - industry_actual.get(name, 0.0), name, industry_actual.get(name, 0.0), industry_target_for(name))
         for name in compatible),
        key=lambda x: (-x[0], x[1].casefold()),
    )

    profile_name = structure_profile_var.get() if "structure_profile_var" in globals() else "Balanceret"
    structure_targets = STRUCTURE_PROFILES.get(profile_name, STRUCTURE_PROFILES["Balanceret"])["targets"]
    stock_weight_total = sum(parse_float(r.get("weight"), 0.0) or 0.0 for r in data_rows)
    structure_actual = {layer: 0.0 for layer in STRUCTURE_LAYER_ORDER}
    for row in data_rows:
        weight = parse_float(row.get("weight"), 0.0) or 0.0
        normalized = weight / stock_weight_total * 100.0 if stock_weight_total > 0 else 0.0
        layer = row.get("structure_layer", "Potentiale")
        structure_actual[layer] = structure_actual.get(layer, 0.0) + normalized
    structure_rank = sorted(
        ((structure_targets.get(layer, 0.0) - structure_actual.get(layer, 0.0), layer,
          structure_actual.get(layer, 0.0), structure_targets.get(layer, 0.0)) for layer in STRUCTURE_LAYER_ORDER),
        reverse=True,
    )
    best_structure = structure_rank[0]

    # Praktiske kvalitetskrav baseres på medianen blandt porteføljens bedste halvdel.
    valid_rows = [r for r in data_rows if parse_float(r.get("sort_stock_score"), None) not in (None, -999999)]
    valid_rows.sort(key=lambda r: parse_float(r.get("sort_stock_score"), 0.0) or 0.0, reverse=True)
    reference_rows = valid_rows[:max(3, len(valid_rows) // 2)] if valid_rows else []

    def median_value(key, fallback):
        import statistics
        values = [parse_float(r.get(key), None) for r in reference_rows]
        values = [v for v in values if v is not None and v != -999999]
        return statistics.median(values) if values else fallback

    return {
        "region": best_region,
        "region_alternatives": region_rank[:3],
        "sector": best_sector,
        "sector_alternatives": sector_rank[:3],
        "industries": industry_rank[:5],
        "structure": best_structure,
        "structure_profile": profile_name,
        "stock_score_min": median_value("sort_stock_score", 35.0),
        "quality_min": median_value("sort_quality_score", 60.0),
        "robustness_min": median_value("sort_robustness", 60.0),
        "trend_min": median_value("sort_trend_strength", 55.0),
        "base_min": max(10.0, median_value("sort_analyst_base_pct", 20.0)),
        "peg_max": max(0.5, median_value("sort_peg", 2.0)),
    }



def _fallback_dividend_months(frequency, last_date_value=None):
    """Vælg en logisk månedsfordeling, når TradingView-data er ufuldstændige.

    Målet er ikke at opfinde et præcist betalingsløfte, men at sikre at hele
    det estimerede årsudbytte bliver placeret i kalenderen:
    - Kendt frekvens + kendt dato bruger den eksisterende rytmeberegning.
    - Kendt frekvens uden dato bruger almindelige kalenderankre.
    - Kendt seneste dato uden frekvens placerer årsbeløbet i den kendte måned.
    - Uden både frekvens og dato fordeles beløbet neutralt over alle 12 måneder.
    """
    parsed_last = _date_from_tv_value(last_date_value)

    if parsed_last is not None and str(frequency or "").strip():
        _label, months = dividend_month_schedule(parsed_last.isoformat(), frequency)
        if months:
            return months

    raw = str(frequency or "").strip().lower()
    if raw in ("uge", "weekly", "måned", "monthly"):
        return list(range(1, 13))
    if raw in ("kvartal", "quarterly"):
        return [3, 6, 9, 12]
    if raw in ("halvår", "semi-annual", "semi-annually", "semiannual"):
        return [6, 12]
    if raw in ("år", "annual", "annually", "yearly"):
        return [parsed_last.month] if parsed_last is not None else [12]

    if parsed_last is not None:
        return [parsed_last.month]

    # "Andet", ukendt frekvens eller helt manglende kalenderdata:
    # neutral fordeling gør årsbeløbet komplet uden at favorisere en bestemt måned.
    return list(range(1, 13))


def _dividend_overview_month_values(row):
    """Returnér 12 DKK-beløb, som tilsammen altid giver hele årsudbyttet."""
    yield_pct = parse_float(row.get("sort_dividend_yield"), None)
    position_value = parse_float(row.get("sort_value_dkk"), None)
    if yield_pct is None or yield_pct <= 0 or position_value is None or position_value < 0:
        return None

    annual = position_value * yield_pct / 100.0
    frequency = row.get("dividend_frequency", "")
    if str(frequency).strip() == "-":
        frequency = ""

    # Brug den rå datostreng fra Fase 2-rækken, hvis den findes. Ved ældre cache
    # kan kun den viste måned være tilgængelig; den håndteres som fallback nedenfor.
    last_date_value = row.get("dividend_last_date_raw") or row.get("dividend_schedule_anchor_raw")
    months = _fallback_dividend_months(frequency, last_date_value)

    # Hvis den rå dato ikke findes, men Fase 2 allerede har beregnet måneder,
    # er disse bedre end en generisk kalender.
    stored_months = row.get("dividend_month_numbers")
    if isinstance(stored_months, (list, tuple)) and stored_months:
        clean = sorted({int(m) for m in stored_months if str(m).isdigit() and 1 <= int(m) <= 12})
        if clean:
            months = clean

    if not months:
        months = list(range(1, 13))

    values = [0.0] * 12
    share = annual / float(len(months))
    for month in months:
        if 1 <= int(month) <= 12:
            values[int(month) - 1] += share

    # Flydende afrunding må aldrig skabe et "forsvundet" restbeløb.
    difference = annual - sum(values)
    if abs(difference) > 1e-9:
        values[int(months[-1]) - 1] += difference
    return values


def _refresh_dividend_data_for_built_portfolio(built_positions, progress_callback=None):
    """Opdatér kun udbyttedata for den konkrete byggede portefølje.

    Identiteten er altid (exchange, ticker). Funktionen indeholder ingen Tk-kald
    og kan derfor trygt køre i en baggrundstråd. progress_callback(stage, current, total, text)
    bruges valgfrit til at informere brugerfladen om fremdriften.
    """
    global _dividend_date_batch_cache

    def progress(stage, current=0, total=0, message=""):
        if callable(progress_callback):
            try:
                progress_callback(stage, current, total, message)
            except Exception:
                pass

    stocks = [normalize_item(x) for x in (built_positions or []) if not is_cash_item(x)]
    total = len(stocks)
    if not stocks:
        return

    progress("start", 0, total, f"Klargør {total} aktier fra den byggede portefølje...")
    cache = load_daily_cache()
    cache.setdefault("phase2", {})

    # Hent aktuelle dividend yields i én/få TradingView-scanner-batches.
    progress("yield", 0, total, "Henter aktuelle udbytteprocenter fra TradingView...")
    scanner_rows = {}
    try:
        scanner_rows = fetch_scanner_rows_batch(stocks) or {}
    except Exception:
        scanner_rows = {}

    # Hent datoankre i batch.
    progress("dates", 0, total, "Henter seneste/kommende udbyttedatoer...")
    try:
        _dividend_date_batch_cache = _fetch_dividend_dates_batch(stocks)
    except Exception:
        _dividend_date_batch_cache = {}

    # Frekvens/seneste dato hentes aktie for aktie fra TradingViews dividendside.
    for index, item in enumerate(stocks, start=1):
        key = position_key(item)
        progress(
            "schedule",
            index,
            total,
            f"Opdaterer udbyttedata {index}/{total} – {key}"
        )

        fundamental = normalize_phase2_cache(cache["phase2"].get(key, {}))

        scanner = scanner_rows.get(key, {}) if isinstance(scanner_rows, dict) else {}
        if isinstance(scanner, dict):
            new_yield = parse_float(scanner.get("dividend_yield"), None)
            if new_yield is not None:
                fundamental["dividend_yield"] = new_yield

        try:
            schedule = fetch_tradingview_dividend_schedule(item)
            if isinstance(schedule, dict):
                for k, v in schedule.items():
                    if not value_is_missing(v):
                        fundamental[k] = v
            fundamental["dividend_schema_v6"] = 6
        except Exception:
            # Behold eksisterende cachedata, hvis TradingView ikke svarer.
            pass

        cache["phase2"][key] = normalize_phase2_cache(fundamental)

    progress("save", total, total, "Gemmer opdaterede udbyttedata...")
    save_daily_cache(cache)
    _dividend_date_batch_cache = {}
    progress("done", total, total, "Udbyttedata er opdateret.")


def _show_dividend_overview_v012_layout(dividend_rows):
    dividend_rows.sort(key=lambda item: item["name"].casefold())
    month_totals = [
        sum(item["months"][index] for item in dividend_rows)
        for index in range(12)
    ]
    annual_total = sum(item["annual"] for item in dividend_rows)
    
    win = tk.Toplevel(root)
    win.title("Udbytteoversigt")
    win.geometry("1580x720")
    win.minsize(1100, 450)
    win.transient(root)
    # Åbn oversigten maksimeret, så alle måneder og årssummen ses bedst muligt.
    try:
        win.state("zoomed")
    except Exception:
        try:
            win.attributes("-zoomed", True)
        except Exception:
            pass
    
    tk.Label(
        win,
        text=(
            "Forventet brutto-udbytte i DKK baseret på aktuel positionsværdi og Udbytte %. "
            "Manglende kalenderdata fordeles efter den mest logiske frekvens/rytme, "
            "så hele årsudbyttet altid er med. Klik på en kolonneoverskrift for at sortere."
        ),
        font=small_font,
        anchor="w",
        justify="left",
    ).pack(fill="x", padx=12, pady=(12, 8))
    
    frame = tk.Frame(win)
    frame.pack(fill="both", expand=True, padx=12, pady=(0, 12))
    
    columns = ["nr", "name"] + [f"m{m}" for m in range(1, 13)] + ["year"]
    tree = ttk.Treeview(frame, columns=columns, show="headings", selectmode="browse")
    ybar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    xbar = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=ybar.set, xscrollcommand=xbar.set)
    
    tree.grid(row=0, column=0, sticky="nsew")
    ybar.grid(row=0, column=1, sticky="ns")
    xbar.grid(row=1, column=0, sticky="ew")
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    
    tree.column("nr", width=55, minwidth=45, anchor="center", stretch=False)
    tree.column("name", width=220, minwidth=150, anchor="w", stretch=False)
    for month in range(1, 13):
        key = f"m{month}"
        tree.column(key, width=92, minwidth=75, anchor="e", stretch=False)
    tree.column("year", width=110, minwidth=90, anchor="e", stretch=False)
    
    # Samlet-rækken bruger samme skriftstørrelse som tabellen, men fremhæves med fed.
    tree.tag_configure(
        "summary",
        font=("Segoe UI", 13, "bold"),
        background="#d9eaf7",
        foreground="#000000",
    )
    
    sort_state = {"column": "name", "descending": False}
    
    def sort_value(item, column):
        if column == "nr":
            # Nr repræsenterer rækkefølgen i den aktuelle visning; ved klik på
            # Nr bruges den alfabetiske grundorden som stabilt udgangspunkt.
            return item["name"].casefold()
        if column == "name":
            return item["name"].casefold()
        if column == "year":
            return float(item["annual"])
        if column.startswith("m"):
            try:
                month_index = int(column[1:]) - 1
                return float(item["months"][month_index])
            except Exception:
                return 0.0
        return item["name"].casefold()
    
    def redraw_table():
        for item_id in tree.get_children(""):
            tree.delete(item_id)
    
        # Summeringen indsættes altid først og påvirkes aldrig af sortering.
        total_values = ["", "Samlet"] + [format_num(v, 0) for v in month_totals] + [format_num(annual_total, 0)]
        tree.insert("", "end", iid="__summary__", values=total_values, tags=("summary",))
    
        ordered = sorted(
            dividend_rows,
            key=lambda item: sort_value(item, sort_state["column"]),
            reverse=sort_state["descending"],
        )
        for index, item in enumerate(ordered, start=1):
            values = [index, item["name"]] + [
                format_num(v, 2) if abs(v) > 0.000001 else "-"
                for v in item["months"]
            ] + [format_num(item["annual"], 2)]
            tree.insert("", "end", values=values)
    
    def sort_by(column):
        if sort_state["column"] == column:
            sort_state["descending"] = not sort_state["descending"]
        else:
            sort_state["column"] = column
            sort_state["descending"] = False
        update_headings()
        redraw_table()
    
    def update_headings():
        titles = {"nr": "Nr", "name": "Aktie", "year": "Året"}
        titles.update({f"m{m}": _danish_month_name(m) for m in range(1, 13)})
        for column in columns:
            arrow = ""
            if column == sort_state["column"]:
                arrow = " ▼" if sort_state["descending"] else " ▲"
            tree.heading(column, text=titles[column] + arrow, command=lambda c=column: sort_by(c))
    
    update_headings()
    redraw_table()
    
    tk.Button(win, text="Luk", font=small_font, command=win.destroy).pack(pady=(0, 12))
    

def open_dividend_overview():
    """Vis udbytte for præcis den portefølje, som aktuelt står i Fase 2.

    Ved klik tages en låst kopi af de viste Fase 2-rækker. Denne kopi er
    sandhedskilden gennem hele opdateringen. Der genindlæses ingen porteføljefil,
    og Fase 2 genopbygges ikke undervejs. Kun udbyttefelterne opdateres for
    de samme exchange+ticker-par.
    """
    locked_rows = []
    for row in phase2_rows:
        if row.get("is_summary") or is_cash_row(row):
            continue
        exchange = str(row.get("exchange", "") or "").strip().upper()
        ticker = str(row.get("ticker", "") or "").strip().upper()
        if not exchange or not ticker:
            continue
        locked_rows.append({
            "exchange": exchange,
            "ticker": ticker,
            "name": str(row.get("name", ticker) or ticker),
            "antal": parse_float(row.get("sort_antal"), parse_float(row.get("antal"), 0.0)) or 0.0,
            "sort_value_dkk": parse_float(row.get("sort_value_dkk"), 0.0) or 0.0,
            "sort_dividend_yield": parse_float(row.get("sort_dividend_yield"), None),
            "dividend_frequency": row.get("dividend_frequency", ""),
            "dividend_last_date_raw": row.get("dividend_last_date_raw"),
            "dividend_schedule_anchor_raw": row.get("dividend_schedule_anchor_raw"),
            "dividend_month_numbers": list(row.get("dividend_month_numbers", []) or []),
        })

    if not locked_rows:
        messagebox.showinfo(
            "Udbytteoversigt",
            "Der står ingen aktier i Fase 2.\n\nByg eller indlæs først en portefølje.",
        )
        return

    locked_keys = [f"{x['exchange']}:{x['ticker']}" for x in locked_rows]
    if len(locked_keys) != len(set(locked_keys)):
        messagebox.showerror(
            "Udbytteoversigt",
            "Den aktuelle Fase 2-portefølje indeholder samme børs+ticker mere end én gang.\n"
            "Udbytteoversigten stoppes, så en position ikke tælles dobbelt.",
        )
        return

    locked_positions = [
        {
            "exchange": row["exchange"],
            "ticker": row["ticker"],
            "name": row["name"],
            "antal": row["antal"],
        }
        for row in locked_rows
    ]

    progress_win = tk.Toplevel(root)
    progress_win.title("Opdaterer udbytteoversigt")
    progress_win.geometry("560x150")
    progress_win.resizable(False, False)
    progress_win.transient(root)
    try:
        progress_win.grab_set()
    except Exception:
        pass

    tk.Label(
        progress_win,
        text="Klargør udbytteoversigt for den aktuelle Fase 2-portefølje",
        font=table_font,
        anchor="w",
    ).pack(fill="x", padx=14, pady=(14, 8))

    progress_text = tk.StringVar(value=f"Låst portefølje: {len(locked_rows)} aktier...")
    tk.Label(
        progress_win,
        textvariable=progress_text,
        font=small_font,
        anchor="w",
        justify="left",
    ).pack(fill="x", padx=14, pady=(0, 8))

    progress_bar = ttk.Progressbar(
        progress_win,
        orient="horizontal",
        mode="determinate",
        maximum=max(1, len(locked_rows)),
        value=0,
    )
    progress_bar.pack(fill="x", padx=14, pady=(0, 14))

    status_var.set(
        f"Udbytteoversigt: låste {len(locked_rows)} aktuelle Fase 2-positioner – opdaterer kun deres udbyttedata..."
    )

    def ui_progress(stage, current, total, message):
        def apply():
            try:
                if progress_win.winfo_exists():
                    progress_text.set(message)
                    if total:
                        progress_bar.configure(maximum=max(1, total))
                        progress_bar["value"] = max(0, min(current, total))
                status_var.set(f"Udbytteoversigt: {message}")
            except Exception:
                pass
        root.after(0, apply)

    def worker():
        try:
            _refresh_dividend_data_for_built_portfolio(
                locked_positions,
                progress_callback=ui_progress,
            )
            root.after(0, finish_success)
        except Exception as exc:
            root.after(0, lambda err=exc: finish_error(err))

    def finish_error(exc):
        try:
            if progress_win.winfo_exists():
                progress_win.destroy()
        except Exception:
            pass
        status_var.set("Udbytteoversigt: fejl under opdatering.")
        messagebox.showerror(
            "Udbytteoversigt",
            f"Udbyttedata kunne ikke klargøres for den aktuelle Fase 2-portefølje.\n\n{exc}",
        )

    def finish_success():
        try:
            progress_text.set("Kobler opdaterede udbyttedata til de låste Fase 2-positioner...")
            progress_bar["value"] = max(1, len(locked_rows))
            status_var.set(
                f"Udbytteoversigt: kobler nye udbyttedata til de samme {len(locked_rows)} positioner..."
            )

            cache = load_daily_cache()
            phase2_cache = cache.get("phase2", {}) if isinstance(cache, dict) else {}

            dividend_rows = []
            for locked in locked_rows:
                key = f"{locked['exchange']}:{locked['ticker']}"
                fundamental = normalize_phase2_cache(phase2_cache.get(key, {}))

                calc_row = dict(locked)

                fresh_yield = parse_float(fundamental.get("dividend_yield"), None)
                if fresh_yield is not None:
                    calc_row["sort_dividend_yield"] = fresh_yield

                fresh_frequency = str(fundamental.get("dividend_frequency", "") or "").strip()
                if fresh_frequency:
                    calc_row["dividend_frequency"] = fresh_frequency

                last_date = fundamental.get("dividend_last_date")
                upcoming_date = fundamental.get("dividend_upcoming_anchor_date")
                if last_date:
                    calc_row["dividend_last_date_raw"] = last_date
                if last_date or upcoming_date:
                    calc_row["dividend_schedule_anchor_raw"] = last_date or upcoming_date
                    _display_months, month_numbers = dividend_month_schedule(
                        calc_row["dividend_schedule_anchor_raw"],
                        calc_row.get("dividend_frequency", ""),
                    )
                    calc_row["dividend_month_numbers"] = month_numbers

                month_values = None
                yield_pct = parse_float(calc_row.get("sort_dividend_yield"), None)
                if yield_pct is not None and yield_pct > 0:
                    month_values = _dividend_overview_month_values(calc_row)
                if month_values is None:
                    month_values = [0.0] * 12

                dividend_rows.append({
                    "name": locked["name"],
                    "months": month_values,
                    "annual": sum(month_values),
                })

            if len(dividend_rows) != len(locked_rows):
                raise RuntimeError(
                    f"Intern afstemningsfejl: Fase 2 havde {len(locked_rows)} aktier, "
                    f"men udbytteoversigten fik {len(dividend_rows)}."
                )

            try:
                if progress_win.winfo_exists():
                    progress_win.destroy()
            except Exception:
                pass

            status_var.set(
                f"Udbytteoversigt klar – præcis {len(dividend_rows)} aktuelle Fase 2-positioner."
            )
            _show_dividend_overview_v012_layout(dividend_rows)

        except Exception as exc:
            finish_error(exc)

    threading.Thread(target=worker, daemon=True).start()


def open_phase2_row_color_explanation():
    """Forklar rækkemarkeringer, købsvindue og godkendt købsvægt i Fase 2."""
    win = tk.Toplevel(root)
    win.title("Forklaring til farve på rækker")
    win.geometry("840x900")
    win.minsize(700, 560)
    win.transient(root)

    # Scrollbart indhold, så hele forklaringen altid kan læses uanset
    # skærmhøjde og Windows' skalering.
    container = tk.Frame(win)
    container.pack(fill="both", expand=True)

    canvas = tk.Canvas(container, highlightthickness=0)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    outer = tk.Frame(canvas, padx=18, pady=16)
    window_id = canvas.create_window((0, 0), window=outer, anchor="nw")

    def update_scrollregion(_event=None):
        canvas.configure(scrollregion=canvas.bbox("all"))

    def fit_width(event):
        canvas.itemconfigure(window_id, width=event.width)

    outer.bind("<Configure>", update_scrollregion)
    canvas.bind("<Configure>", fit_width)

    def on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", on_mousewheel)
    win.bind("<Destroy>", lambda _e: canvas.unbind_all("<MouseWheel>"))

    tk.Label(
        outer,
        text="Forklaring til farver og salgsmarkeringer i Fase 2",
        font=("Segoe UI", 16, "bold"),
        anchor="w",
    ).pack(fill="x")
    tk.Label(
        outer,
        text=("Farverne er hurtige visuelle signaler. Mørkerød Sælg og dybgrøn Køb er egentlige "
              "handlingssignaler i Anbefalet %PF. Lys rød er datavarsling, mens Watch list-farverne "
              "fortsat er visuelle købsvurderinger."),
        font=small_font, justify="left", wraplength=770, anchor="w",
    ).pack(fill="x", pady=(5, 14))

    def add_section(title, color, text, foreground="black"):
        box = tk.LabelFrame(outer, text=title, font=small_font, padx=12, pady=10)
        box.pack(fill="x", pady=(0, 12))
        sample = tk.Label(
            box, text="  Eksempel på rækkefarve  ", font=("Segoe UI", 10, "bold"),
            background=color, foreground=foreground, padx=8, pady=5,
        )
        sample.pack(anchor="w", pady=(0, 8))
        tk.Label(
            box, text=text, font=small_font, justify="left", wraplength=740, anchor="w",
        ).pack(fill="x")

    add_section(
        "Mørkerød – Sælg",
        "#e06666",
        ("Rækken bliver mørkerød, og Anbefalet %PF viser Sælg, når mindst én af de hårde "
         "upside-regler brydes:\n"
         "• Bull 1Y er under +20 %.\n"
         "• Bear 1Y er negativ, og Bull 1Y er mindre end 2 × den numeriske Bear-risiko.\n\n"
         "Formålet er at frasortere positioner, hvor selv det optimistiske scenarie er for lille "
         "i forhold til den mulige nedside. Aktien fjernes fra fordelingen af Anbefalet %PF, "
         "og Aktier+/− viser hele positionen til salg."),
        foreground="white",
    )

    add_section(
        "Lys rød – Datavarsling",
        "#f4cccc",
        ("Rækken bliver lys rød, når analytikernes Bull/Base/Median/Bear-data er tydeligt ugyldige.\n\n"
         "Kort aktiehistorik giver ikke længere denne advarsel. Markeringen betyder ikke automatisk "
         "Sælg og ændrer ikke i sig selv Anbefalet %PF. Manglende eller ugyldige analytikerdata "
         "udløser heller ikke de hårde salgsregler."),
    )

    add_section(
        "Dyb grøn – Køb tæt på Bear-målet",
        "#2e7d32",
        ("Rækken bliver dyb grøn, og Anbefalet %PF viser Køb – xx,x %, når begge betingelser er opfyldt:\n"
         "• Det absolutte Bull-kursmål er større end 2 × det absolutte Bear-kursmål.\n"
         "• Aktuel kurs er højst Bear + den indstillede procent af spændet mellem Bull og Bear, eller ligger endnu lavere.\n\n"
         "Standard er 10 % af spændet (Bull − Bear). Eksempel: Bull = 150 og Bear = 100 giver et spænd på 50. "
         "10 % af spændet er 5, så købsvinduets øvre grænse bliver 100 + 5 = 105. Det er altså ikke længere "
         "10 % oven på selve Bear-målet. Procenten kan ændres via Indstil købsvindue.\n\n"
         "Kursmålets påvirkning gælder KUN i dette købsvindue. Skyder 0 giver den normale Anbefalet %PF. "
         "Skyder 1 bruger en dynamisk faktor med et redigerbart maksimum (standard 5×). Den faktiske faktor "
         "afhænger især af Bull-potentialet (70 %), Base-potentialet (30 %) og hvor tæt kursen er på Bear inden "
         "for det nye Bull−Bear-baserede købsvindue. Maksimal faktor er derfor et loft og ikke en fast multiplikator "
         "for alle købsvindue-aktier. Andre aktiers normale anbefalinger ændres ikke af dette tillæg.\n\n"
         "Maks. godkendt %PF gemmes kun, hvis antal aktier faktisk øges, mens købsvinduet er åbent. "
         "Det faktiske køb gemmes samtidig som 'Køb i købsvindue' i Aktiens historik med dagens kurs, "
         "Bull/Base/Bear og den opnåede %PF. Denne begivenhed er dokumentation og påvirker ikke KM alder. "
         "Når kursen senere stiger ud af vinduet, bevares hukommelsen som forklaring på den opbyggede position. "
         "Godkendelsen slettes ved Sælg-signal eller hvis Bull- eller Bear-kursmålet falder mindst 20 % siden købet."),
        foreground="white",
    )

    add_section(
        "Svag rød – Ikke attraktiv som nyt køb",
        "#f7dddd",
        ("Rækken bliver svagt rød, når Base 1Y er under +20 %, eller når Bull 1Y er mindre "
         "end 2 × den numeriske Bear-værdi. Farven følger Watch listens købsvurdering.\n\n"
         "Den mørkerøde Sælg-markering er fortsat overordnet og uændret. Den svage røde farve "
         "ændrer ikke Anbefalet %PF, Aktier+/− eller salgsreglerne."),
    )

    add_section(
        "Svag gul – Base 1Y fra +20 % til under +30 %",
        "#fff3c4",
        ("Aktien opfylder Bull/Bear-sikkerhedskravet, men Base 1Y ligger mellem +20 % og under +30 %. "
         "Det er et forsigtigt positivt købssignal."),
    )

    add_section(
        "Svag grøn – Base 1Y fra +30 % til under +40 %",
        "#dff3df",
        ("Aktien opfylder Bull/Bear-sikkerhedskravet, og Base 1Y ligger mellem +30 % og under +40 %. "
         "Det er et attraktivt købssignal."),
    )

    add_section(
        "Stærk grøn – Base 1Y mindst +40 %",
        "#a9dda9",
        ("Aktien opfylder Bull/Bear-sikkerhedskravet, og Base 1Y er mindst +40 %. Det er det stærkeste "
         "visuelle købssignal. Ved køb vurderes aktien bevidst på Base %, fordi Base er analytikernes "
         "mest realistiske scenarie. Bull bruges samtidig til at kontrollere, at potentialet er mindst "
         "2 × den numeriske Bear-risiko. Farverne ændrer ingen beregninger."),
    )

    tk.Button(outer, text="Luk", font=small_font, command=win.destroy).pack(anchor="e", pady=(0, 2))


def open_perfect_stock_profile():
    profile = calculate_perfect_stock_profile()
    if profile is None:
        messagebox.showinfo("Perfekt aktieprofil", "Hent først porteføljens data i Fase 2.")
        return

    win = tk.Toplevel(root)
    win.title("Bedste forslag til perfekt aktie i porteføljen")
    win.geometry("790x900")
    win.minsize(680, 820)
    win.transient(root)

    outer = tk.Frame(win, padx=18, pady=16)
    outer.pack(fill="both", expand=True)

    tk.Label(outer, text="Profilen på den aktie porteføljen savner mest", font=("Segoe UI", 16, "bold"), anchor="w").pack(fill="x")
    tk.Label(
        outer,
        text="Forslaget er en profil – ikke en bestemt aktie. Det kombinerer de største undervægte i region, sektor, industri og porteføljestruktur.",
        font=small_font, justify="left", wraplength=740, anchor="w",
    ).pack(fill="x", pady=(4, 14))

    region = profile["region"]
    sector = profile["sector"]
    structure = profile["structure"]
    industries = profile["industries"]

    summary = tk.LabelFrame(outer, text="Bedste samlede profil", font=small_font, padx=14, pady=10)
    summary.pack(fill="x")
    lines = [
        ("Region", region[1], region[2], region[3], region[0]),
        ("Sektor", sector[1], sector[2], sector[3], sector[0]),
        ("Strukturlag", structure[1], structure[2], structure[3], structure[0]),
    ]
    for i, (label, name, actual, target, deficit) in enumerate(lines):
        tk.Label(summary, text=f"{label}:", font=("Segoe UI", 10, "bold"), width=15, anchor="w").grid(row=i, column=0, sticky="w", pady=3)
        tk.Label(summary, text=name, font=small_font, width=25, anchor="w").grid(row=i, column=1, sticky="w", pady=3)
        tk.Label(summary, text=f"Aktuel {format_num(actual, 1)} % · mål {format_num(target, 1)} % · mangel {format_num(deficit, 1)} pp", font=small_font, anchor="w").grid(row=i, column=2, sticky="w", pady=3)

    industry_box = tk.LabelFrame(outer, text="Bedst egnede industrier i den valgte sektor", font=small_font, padx=14, pady=10)
    industry_box.pack(fill="x", pady=(12, 0))
    if industries:
        for i, (deficit, name, actual, target) in enumerate(industries, start=1):
            tk.Label(industry_box, text=f"{i}. {name}", font=small_font, width=38, anchor="w").grid(row=i-1, column=0, sticky="w", pady=2)
            tk.Label(industry_box, text=f"Aktuel {format_num(actual, 1)} % · mål {format_num(target, 1)} % · mangel {format_num(deficit, 1)} pp", font=small_font, anchor="w").grid(row=i-1, column=1, sticky="w", pady=2)
    else:
        tk.Label(industry_box, text="Ingen sikker industri kunne udledes. Brug sektorprofilen som hovedfilter.", font=small_font).pack(anchor="w")

    quality_box = tk.LabelFrame(outer, text="Anbefalet minimumsprofil for selve virksomheden", font=small_font, padx=14, pady=10)
    quality_box.pack(fill="x", pady=(12, 0))
    quality_text = (
        f"Aktiescore omkring {format_num(profile['stock_score_min'], 1)} eller højere\n"
        f"Kvalitet omkring {format_num(profile['quality_min'], 0)} eller højere\n"
        f"Robusthed omkring {format_num(profile['robustness_min'], 0)} eller højere\n"
        f"Trendstyrke omkring {format_num(profile['trend_min'], 0)} eller højere\n"
        f"Base 1Y-potentiale omkring {format_num(profile['base_min'], 1)} % eller højere\n"
        f"PEG helst omkring {format_num(profile['peg_max'], 2)} eller lavere"
    )
    tk.Label(quality_box, text=quality_text, font=small_font, justify="left", anchor="w").pack(fill="x")

    alternatives = tk.LabelFrame(outer, text="Nærmeste alternativer", font=small_font, padx=14, pady=10)
    alternatives.pack(fill="x", pady=(12, 0))
    region_alt = ", ".join(x[1] for x in profile["region_alternatives"])
    sector_alt = ", ".join(x[1] for x in profile["sector_alternatives"])
    tk.Label(alternatives, text=f"Regioner: {region_alt}", font=small_font, anchor="w").pack(fill="x")
    tk.Label(alternatives, text=f"Sektorer: {sector_alt}", font=small_font, anchor="w").pack(fill="x", pady=(4, 0))

    tk.Label(
        outer,
        text=("Fortolkning: Jo større positiv mangel, desto mere hjælper en ny aktie porteføljens balance. "
              "Aktien bør stadig bestå den almindelige kvalitets-, robustheds- og værdivurdering."),
        font=small_font, justify="left", wraplength=740, anchor="w",
    ).pack(fill="x", pady=(12, 0))

    tk.Button(outer, text="Luk", font=small_font, command=win.destroy).pack(side="right", pady=(14, 0))


def open_explanation_window(title, content):
    """Vis en lang, læsevenlig programforklaring i et separat vindue."""
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("1220x850")
    win.minsize(900, 650)
    win.transient(root)

    outer = tk.Frame(win)
    outer.pack(fill="both", expand=True, padx=12, pady=12)
    outer.grid_rowconfigure(0, weight=1)
    outer.grid_columnconfigure(0, weight=1)

    txt = tk.Text(
        outer,
        wrap="word",
        font=("Segoe UI", 11),
        padx=18,
        pady=16,
        spacing1=2,
        spacing2=2,
        spacing3=8,
    )
    scroll = ttk.Scrollbar(outer, orient="vertical", command=txt.yview)
    txt.configure(yscrollcommand=scroll.set)
    txt.grid(row=0, column=0, sticky="nsew")
    scroll.grid(row=0, column=1, sticky="ns")

    txt.tag_configure("title", font=("Segoe UI", 16, "bold"), spacing3=12)
    txt.tag_configure("section", font=("Segoe UI", 13, "bold"), spacing1=12, spacing3=5)
    txt.tag_configure("sub", font=("Segoe UI", 11, "bold"), spacing1=8, spacing3=3)
    txt.insert("1.0", content)

    # Fremhæv overskrifter uden at være afhængig af særlige markdown-komponenter.
    for line_no, line in enumerate(content.splitlines(), start=1):
        stripped = line.strip()
        if line_no == 1:
            txt.tag_add("title", f"{line_no}.0", f"{line_no}.end")
        elif stripped and set(stripped) == {"="}:
            continue
        elif stripped and stripped[0].isdigit() and ". " in stripped[:5]:
            txt.tag_add("section", f"{line_no}.0", f"{line_no}.end")
        elif stripped.endswith(":") and len(stripped) < 80:
            txt.tag_add("sub", f"{line_no}.0", f"{line_no}.end")

    txt.configure(state="disabled")

    close_bar = tk.Frame(win)
    close_bar.pack(fill="x", padx=12, pady=(0, 12))
    tk.Button(close_bar, text="Luk", font=small_font, command=win.destroy).pack(side="right")


def open_program_explanation():
    """Forklar Porteføljebyggerens aktuelle arkitektur og arbejdsgang."""
    explanation = """PROGRAMFORKLARING – PORTEFØLJEBYGGER V0.08

FORMÅL
Porteføljebyggeren konstruerer en ny aktieportefølje ud fra et frit aktieunivers. Målet er at finde en kombination af aktier og positionsstørrelser, der prioriterer forventet afkast og Aktiescore, samtidig med at Strukturlag, Sektor, Industri og Region bruges som styring af risiko og diversifikation.

Programmet er ikke en handelsrobot. Det er en forklarlig optimeringsmotor, hvor brugeren selv bestemmer regler og relative prioriteringer.

============================================================
1. ARBEJDSGANG
============================================================

Fase 0 – Aktieunivers
• Indeholder alle aktier programmet må vælge imellem.
• Import er additiv: nye børs+ticker-kombinationer tilføjes, eksisterende beholdes.
• Grøn række = nødvendige byggedata er klar.
• Rød række = nødvendige data mangler eller symbolet er ubrugeligt.
• OPDATER KURSDATA / MANGLENDE DATA henter kun manglende universdata.
• Opdater alle data forceret genhenter hele universet.

Fase 1 – Byg portefølje
• Angiv samlet porteføljeværdi.
• Angiv minimum positionsstørrelse.
• Angiv maksimum antal aktier.
• Angiv minimum antal aktier pr. sektor.
• Angiv mål for Strukturlag, Sektorer og Regioner. Industri styres som en diversifikationsscore uden en stor måltabel.
• Angiv de relative prioriteringer for Base 1Y, Aktiescore, Strukturlag, Sektor, Industri, Region og Udbytte.
• Tryk BYG PORTEFØLJE for at starte optimeringen.

Fase 1B – Kursudvikling
Viser den færdigbyggede portefølje med aktuel kurs, DKK-værdi, vægt og historiske kursperioder.

Fase 1C – Bogført værdi
Viser bogført værdi, bogført kurs og markedspræmie for den byggede portefølje.

Fase 2 – Aktieanalyse
Viser de detaljerede aktiedata og scorer for de aktier, som optimeringen har valgt.

Fase 3 – Fordelinger
Viser den færdige porteføljes sektor-, industri-, region-, PE-, analytiker- og strukturfordelinger.

============================================================
2. DATAARKITEKTUR
============================================================

aktieunivers.json
Det permanente kandidatunivers. Import af nye JSON-filer gør universet større, medmindre aktier fjernes manuelt.

portefolje_dagsdata_cache.json
Dagens fælles datasnapshot. Fase 0 er master for dataopdateringen. Når universet er grønt, arbejder Porteføljebyggeren på dette snapshot.

portefoljebygger_indstillinger.json
Gemmer Fase 1-regler, målfordelinger og relative prioriteringer.

portefolje_bygget.json
Den senest byggede konkrete portefølje.

VIGTIGT PRINCIP
Efter BYG PORTEFØLJE genhentes data ikke. Fase 1B, 1C, 2 og 3 opbygges direkte fra samme cache, som optimeringen brugte, og programmet åbner automatisk Fase 2. Dermed sammenlignes forskellige byggeforsøg på samme datagrundlag.

============================================================
3. OPTIMERINGENS PRIORITERINGER
============================================================

Bjælkerne i Fase 1 er relative vægte og behøver ikke summere til 100.
Eksempel: 50 / 30 / 15 / 10 / 5 normaliseres internt.

Base 1Y
Fremadskuende analytikerpotentiale. Højere er bedre og dette kan gives størst prioritet.

Aktiescore
Programmets samlede kvalitetsscore, som kombinerer Kvalitet, Robusthed, Trendstyrke og et begrænset troværdigt analytikerpotentiale.

Strukturlag
Matcher porteføljens DKK-vægt mod målene for Fundament, Vækst, Accelerator og Potentiale.

Sektor
Matcher porteføljens DKK-vægt mod de ønskede sektormål.

Region
Matcher porteføljens DKK-vægt mod de ønskede regionsmål.

============================================================
4. ITERATIV BYTTEOPTIMERING
============================================================

Aktievalget følger et enkelt, stabilt princip inspireret af bubble sort:
1. Lav en startportefølje.
2. Prøv én aktie ud og én aktie fra resten af universet ind.
3. Beregn hele porteføljens score igen.
4. Hvis scoren forbedres, behold byttet.
5. Ellers gå tilbage.
6. Gennemgå alle mulige byt.
7. Start forfra.
8. Stop først når en hel gennemgang giver 0 forbedrende byt.

Brugeren kan følge iteration, testnummer, accepterede byt og score i statuslinjen.

============================================================
5. ITERATIV KAPITALOPTIMERING
============================================================

Når de valgte aktier er fundet, optimeres positionsstørrelserne separat:
1. Start fra en neutral kapitalfordeling.
2. Flyt et lille DKK-beløb fra én valgt aktie til en anden.
3. Beregn den samlede DKK-vægtede porteføljescore igen.
4. Behold kun flytningen, hvis scoren forbedres.
5. Gentag til en hel gennemgang giver 0 forbedringer.

Minimum positionsstørrelse er en hård nedre grænse. Der er ikke noget krav om lige store positioner.

Til sidst omsættes de optimerede DKK-mål til hele aktier. En mindre kontantrest kan derfor opstå.

============================================================
6. HVAD TOPBAREN INDEHOLDER
============================================================

Topbaren er bevidst enkel og indeholder kun:
• Programforklaring
• Beregningsforklaring

Dataopdatering foregår kun i Fase 0. Manuel porteføljeimport, Nordnet-import og manuel redigering hører til den gamle Porteføljesimulator og er ikke en del af Porteføljebyggerens normale arbejdsgang.

============================================================
7. BEGRÆNSNINGER
============================================================

• Resultatet afhænger af kvaliteten af TradingView-data og analytikerkursmål.
• Optimeringen er lokal/iterativ og garanterer ikke et matematisk globalt optimum.
• Hele aktier betyder, at målfordelinger og samlet kapital ikke altid kan rammes præcist.
• Lave prioriteringer på Sektor, Industri og Region betyder bevidst, at disse mål kan afvige, hvis Base 1Y og Aktiescore forbedres mere.
• Aktiescore og analytikermål kan ændre sig over tid; en ny Fase 0-opdatering kan derfor skabe en ny optimal portefølje.

KONKLUSION
Porteføljebyggeren søger ikke den pæneste fordeling. Den søger den bedste samlede portefølje efter brugerens egne prioriteringer, mens risikostrukturen stadig holdes under kontrol.
"""
    open_explanation_window("Programforklaring", explanation)

def open_calculation_explanation():
    """Forklar Porteføljebyggerens centrale beregninger og optimeringslogik."""
    explanation = """BEREGNINGSFORKLARING – PORTEFØLJEBYGGER V0.06

============================================================
1. POSITIONSVÆRDI OG VALUTA
============================================================

Positionsværdi DKK = antal × aktuel kurs × valutakurs til DKK

Alle optimerede fordelinger måles på DKK-værdi, så aktier fra forskellige markeder kan sammenlignes korrekt.

============================================================
2. BASE 1Y SOM OPTIMERINGSMÅL
============================================================

Base 1Y er procentvis afstand fra aktuel kurs til TradingViews Base-kursmål:

Base 1Y % = (Base-kursmål / aktuel kurs − 1) × 100

Til den samlede optimeringsscore omregnes Base 1Y til en 0-100 potentialescore med programmets eksisterende S-kurve. Formålet er, at forskellen mellem moderate og gode forecasts betyder meget, mens ekstreme forecasts gradvist mættes og ikke kan dominere ubegrænset.

Den rå DKK-vægtede Base 1Y vises stadig i resultatet, så brugeren kan se det forventede gennemsnit direkte.

============================================================
3. AKTIESCORE
============================================================

Aktiescore beregnes før Porteføljebyggerens optimering og bruges som et selvstændigt 0-100 mål.

Når alle komponenter er tilgængelige:

Aktiescore =
40 % Kvalitet
+ 25 % Robusthed
+ 20 % Trendstyrke
+ 15 % Troværdigt analytikerpotentiale

Troværdigt analytikerpotentiale = Potentialescore × Tillid.

Kvalitet bygger bl.a. på PEG, EBIT-margin, omsætningsvækst, FCF-vækst, FCF-margin og ROIC. Kort kurshistorik kan dæmpe Aktiescoren.

============================================================
4. STRUKTURSCORE OG STRUKTURLAG
============================================================

Strukturscoren klassificerer hver aktie i:
• Fundament: 70+
• Vækst: 56-69,99
• Accelerator: 40-55,99
• Potentiale: under 40

Fase 1 angiver derefter en ønsket DKK-fordeling mellem disse fire lag.

============================================================
5. FORDELINGSMATCH
============================================================

Struktur, Sektor og Region scores hver fra 0 til 100 ved at sammenligne den faktiske DKK-fordeling med målfordelingen. Afvigelsen beregnes som halvdelen af summen af de absolutte procentpointafvigelser mellem alle kategorier.

Matchscore = 100 − samlet fordelingsafvigelse

100 = perfekt match.
Jo større samlet afvigelse, desto lavere score.

Industri scores også 0-100, men uden en fast procentmåltabel. Her måles koncentrationen direkte på TradingViews konkrete industri med en HHI-baseret diversifikationsscore. 100 betyder, at de valgte positioner er fordelt på hver sin industri med minimal koncentration; scoren falder, når flere eller større positioner samles i samme industri. Det forhindrer, at en bred sektor som Industri ser diversificeret ud, selv om porteføljen reelt er koncentreret i fx Aerospace & Defense.

============================================================
6. SAMLET PORTEFØLJESCORE
============================================================

De seks komponenter er:
• Base 1Y-score
• Aktiescore
• Strukturmatch
• Sektormatch
• Industridiversifikation
• Regionsmatch

Brugerens bjælker er relative vægte. De normaliseres automatisk:

Samlet score =
(sum af komponent × valgt vægt) / sum af valgte vægte

Eksempel med 50 / 30 / 15 / 10 / 5:
Summen er 110, så de reelle relative vægte bliver ca. 45,5 %, 27,3 %, 13,6 %, 9,1 % og 4,5 %.

Derfor kan Sektor, Industri og især Region godt afvige mærkbart, hvis et sådant kompromis giver højere Base 1Y og Aktiescore.

============================================================
7. STARTPORTEFØLJE
============================================================

Byggemotoren laver først en stabil startløsning. Hårde minimumskrav pr. sektor håndteres først, hvorefter de stærkeste kandidater efter Base 1Y og Aktiescore fylder de resterende pladser op til Maks. antal aktier.

Maks. antal aktier begrænses også af:
Samlet kapital / minimum positionsstørrelse.

Hvis hårde regler matematisk modsiger hinanden, stopper programmet og forklarer konflikten.

============================================================
8. ITERATIV AKTIEBYTTEOPTIMERING
============================================================

For hver aktie i porteføljen prøves kandidater udenfor porteføljen én ad gangen.

Prøve:
Portefølje B = Portefølje A − aktie X + aktie Y

Hvis:
Score(B) > Score(A) + lille tolerance

beholdes byttet. Ellers tilbageføres det.

Efter en fuld gennemgang startes en ny iteration. Når en hel iteration giver 0 accepterede byt, stopper aktievalget.

Dette er bevidst en enkel lokal søgning: langsommere end avancerede solvere, men stabil, gennemskuelig og let at kontrollere.

============================================================
9. ITERATIV KAPITALOPTIMERING
============================================================

Når aktievalget er færdigt, optimeres kapitalfordelingen på de valgte aktier.

Start: neutral omtrent ligelig DKK-fordeling.
Kapitaltrin: 0,10 % af porteføljen, dog mindst 1.000 DKK.

For hvert donor/modtager-par prøves:
• donor − kapitaltrin
• modtager + kapitaltrin

Minimum positionsstørrelse må aldrig brydes.

Hele porteføljen scores DKK-vægtet igen. Flytningen beholdes kun, hvis scoren forbedres. Der køres nye fulde kapitaliterationer, indtil en hel gennemgang giver 0 forbedringer.

Konsekvens:
Stærke aktier kan naturligt få store positioner, mens aktier, der primært hjælper diversifikation eller har lavere afkastscore, kan ende tæt på minimumskravet.

============================================================
10. HELE AKTIER OG KONTANTREST
============================================================

De kontinuerte DKK-mål kan ikke handles direkte. Derfor omsættes hver position til et helt antal aktier.

Programmet:
• respekterer minimumspositionen
• undgår at overskride samlet kapital
• bruger restkapital på den aktie, hvor én ekstra aktie bringer positionen nærmest dens optimerede DKK-mål
• stopper når en ekstra hel aktie ville gøre løsningen dårligere eller ikke kan købes

Resterende beløb gemmes som kontanter.

============================================================
11. HVORFOR RESULTATET KAN SE SKÆVT UD
============================================================

En optimal løsning efter de valgte vægte behøver ikke se symmetrisk ud.
Hvis Base 1Y og Aktiescore vægtes højt, kan enkelte stærke aktier blive markant større end resten. Hvis Struktur samtidig kan rammes godt uden stort afkaststab, kan den være næsten spot on, mens lavere vægtede Sektor, Industri og Region afviger mere.

Det er ikke i sig selv en fejl. Det er netop kompromiset, som de fem prioriteringsbjælker styrer.

============================================================
12. DATASNAPSHOT OG GENBYGNING
============================================================

Fase 0 henter data. BYG PORTEFØLJE foretager ingen nye netopslag.
Efter bygningen vises Fase 1B/1C/2/3 direkte fra samme dags-cache.

Det betyder, at to byggeforsøg med forskellige prioriteter kan sammenlignes på samme markeds- og analysedata. Først når Fase 0 opdateres igen, ændres datagrundlaget.

KONKLUSION
Porteføljebyggerens kerne er enkel: prøv en lille ændring, behold den kun hvis hele porteføljen bliver bedre, og gentag indtil der ikke længere findes en lokal forbedring.
"""
    open_explanation_window("Beregningsforklaring", explanation)


# ---------------- GUI ----------------
load_value_settings()
load_allocation_settings()
load_vix_settings()
load_structure_settings()



# ---------------------------------------------------------------------------
# Fase 5 – ETF Benchmark
# ---------------------------------------------------------------------------
ETF_MONTH_PERIODS = [(f"pct_{m}m", f"%{m}M", 21 * m) for m in range(1, 13)]
ETF_COLUMNS = [
    ("exchange", "Børs", 85), ("ticker", "Ticker", 85), ("name", "ETF-tema", 300),
    ("price", "Kurs", 90), ("pct_1m", "%1M", 85), ("pct_3m", "%3M", 85),
    ("pct_6m", "%6M", 85), ("trend", "Trend", 95),
    ("acceleration", "Acceleration", 115), ("trend_status", "Udvikling", 105),
    ("holdings_count", "Fundet", 75), ("coverage", "Dækket ETF-vægt", 135),
    ("holdings_updated", "Positioner opdateret", 145),
]
ETF_COLUMN_IDS = [c[0] for c in ETF_COLUMNS]
ETF_HOLDING_COLUMNS = [
    ("rank", "Nr", 55), ("exchange", "Børs", 95), ("ticker", "Ticker", 100),
    ("name", "Selskab", 300),
    ("sector", "Sektor", 175), ("industry", "Industri", 220), ("country", "Land / Region", 165),
    ("bull_pct", "Bull %", 95), ("base_pct", "Base %", 95), ("bear_pct", "Bear %", 95),
    ("weight", "ETF-vægt", 105), ("portfolio_weight", "Min vægt", 105),
    ("portfolio_match", "I min portefølje", 130), ("match_method", "Match", 95),
]
ETF_HOLDING_COLUMN_IDS = [c[0] for c in ETF_HOLDING_COLUMNS]
ETF_ALL_HOLDING_COLUMNS = [
    ("rank", "Nr", 55), ("exchange", "Børs", 95), ("ticker", "Ticker", 100),
    ("name", "Selskab", 300),
    ("sector", "Sektor", 175), ("industry", "Industri", 220), ("country", "Land / Region", 165),
    ("bull_pct", "Bull %", 95), ("base_pct", "Base %", 95), ("bear_pct", "Bear %", 95),
    ("weight", "ETF-vægt", 105), ("portfolio_weight", "Min vægt", 105),
    ("portfolio_match", "I min portefølje", 130), ("etf_name", "ETF", 300),
]
ETF_ALL_HOLDING_COLUMN_IDS = [c[0] for c in ETF_ALL_HOLDING_COLUMNS]
ETF_BENCHMARK_COLUMNS = [
    ("exchange", "Børs", 80), ("ticker", "Ticker", 80), ("name", "ETF-tema", 280),
    ("matches", "Match", 70), ("capital", "Min kapital DKK", 135),
    ("coverage", "ETF-dækning", 110), ("basis", "Datagrundlag", 115),
    ("etf_trend", "ETF trend", 100), ("mine_trend", "Min trend", 100),
    ("difference", "Forskel", 95), ("acceleration", "ETF acceleration", 125),
    ("signal", "Signal", 250),
]
ETF_BENCHMARK_COLUMN_IDS = [c[0] for c in ETF_BENCHMARK_COLUMNS]

# Sorteringstilstand for de tre selvstændige tabeller i Fase 5.
phase5_tree_sort_state = {}


def _phase5_numeric_text(value):
    """Fortolk viste danske tal, procenttal og DKK-beløb til sortering."""
    text = str(value or "").strip()
    if text in ("", "-"):
        return None
    text = text.replace("%", "").replace("DKK", "").replace(" ", "").replace("\u00a0", "")
    # Dansk visning: punktum som tusindtalsseparator og komma som decimaltegn.
    if "," in text:
        text = text.replace(".", "").replace(",", ".")
    elif text.count(".") >= 1:
        parts = text.split(".")
        # 12.345 eller 1.234.567 er heltalsbeløb med tusindtalsseparatorer.
        if len(parts) > 2 or (len(parts) == 2 and len(parts[1]) == 3 and parts[0].lstrip("+-").isdigit()):
            text = "".join(parts)
    try:
        return float(text)
    except Exception:
        return None


def _phase5_sort_value(value, column_id, numeric_columns, date_columns):
    """Returnér en stabil sorteringsnøgle; manglende værdier placeres nederst."""
    text = str(value or "").strip()
    if text in ("", "-"):
        return (1, 0)
    if column_id in numeric_columns:
        number = _phase5_numeric_text(text)
        return (0, number if number is not None else float("-inf"))
    if column_id in date_columns:
        # ISO-dato/-datetime kan sorteres kronologisk som tekst.
        return (0, text)
    return (0, text.casefold())


def configure_phase5_tree_sorting(tree, columns, numeric_columns=(), date_columns=()):
    """Aktivér kliksortering med ▲/▼ på en Fase 5-Treeview."""
    numeric_columns = set(numeric_columns)
    date_columns = set(date_columns)
    titles = {column_id: title for column_id, title, _width in columns}
    tree_key = str(tree)
    phase5_tree_sort_state.setdefault(tree_key, {"column": "", "descending": False})

    def update_headers():
        state = phase5_tree_sort_state[tree_key]
        for column_id, title, _width in columns:
            arrow = ""
            if state["column"] == column_id:
                arrow = " ▼" if state["descending"] else " ▲"
            tree.heading(
                column_id,
                text=title + arrow,
                command=lambda c=column_id: sort_column(c),
            )

    def sort_column(column_id):
        state = phase5_tree_sort_state[tree_key]
        if state["column"] == column_id:
            state["descending"] = not state["descending"]
        else:
            state["column"] = column_id
            # Tekst starter stigende; tal starter faldende, så de største ses først.
            state["descending"] = column_id in numeric_columns

        items = list(tree.get_children(""))
        fixed_items = [
            item_id for item_id in items
            if "fixed_total" in tree.item(item_id, "tags")
        ]
        sortable_items = [item_id for item_id in items if item_id not in fixed_items]
        sortable_items.sort(
            key=lambda item_id: _phase5_sort_value(
                tree.set(item_id, column_id), column_id, numeric_columns, date_columns
            ),
            reverse=state["descending"],
        )
        for index, item_id in enumerate(sortable_items + fixed_items):
            tree.move(item_id, "", index)
        update_headers()

    update_headers()


def _json_load(path, fallback):
    try:
        if Path(path).exists():
            with Path(path).open("r", encoding="utf-8") as f:
                data = json.load(f)
            return data
    except Exception:
        pass
    return fallback


def _json_save(path, data):
    with Path(path).open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_etf_list():
    data = _json_load(ETF_LIST_FILE, [])
    if isinstance(data, dict):
        data = data.get("etfs", [])
    clean=[]
    for row in data if isinstance(data,list) else []:
        if not isinstance(row,dict): continue
        ex=str(row.get("exchange","")).upper().strip(); ti=str(row.get("ticker","")).upper().strip()
        if not ex or not ti: continue
        clean.append({
            "exchange": ex,
            "ticker": ti,
            "name": str(row.get("name", ti)).strip() or ti,
        })
    return clean


def save_etf_list(rows_in):
    _json_save(ETF_LIST_FILE, rows_in)


def load_etf_holdings():
    data=_json_load(ETF_HOLDINGS_FILE,{"schema":"PORTEFOLJE_ETF_HOLDINGS_V1","etfs":{}})
    if not isinstance(data,dict): data={"schema":"PORTEFOLJE_ETF_HOLDINGS_V1","etfs":{}}
    data.setdefault("etfs",{})
    return data


def save_etf_holdings(data):
    data["schema"]="PORTEFOLJE_ETF_HOLDINGS_V1"; data.setdefault("etfs",{})
    _json_save(ETF_HOLDINGS_FILE,data)


def load_etf_settings():
    data=_json_load(ETF_SETTINGS_FILE,{"schema":"PORTEFOLJE_ETF_THEME_SETTINGS_V1","manual_add":{},"manual_remove":{}})
    if not isinstance(data,dict): data={}
    data.setdefault("manual_add",{}); data.setdefault("manual_remove",{}); data["schema"]="PORTEFOLJE_ETF_THEME_SETTINGS_V1"
    return data


def save_etf_settings(data):
    data["schema"]="PORTEFOLJE_ETF_THEME_SETTINGS_V1"; _json_save(ETF_SETTINGS_FILE,data)


def load_etf_cache():
    data=_json_load(ETF_CACHE_FILE,{"schema":"PORTEFOLJE_ETF_CACHE_V1","date":"","etfs":{},"stocks":{},"holding_analyst":{}})
    if not isinstance(data,dict): data={}
    data.setdefault("etfs",{}); data.setdefault("stocks",{}); data.setdefault("holding_analyst",{}); return data


def save_etf_cache(data):
    data["schema"]="PORTEFOLJE_ETF_CACHE_V1"; data["date"]=today_key(); _json_save(ETF_CACHE_FILE,data)


def purge_etf_data(key):
    """Slet alle fase 5-data, der tilhører én ETF-nøgle."""
    key = str(key or "").upper().strip()
    if not key or ":" not in key:
        return

    holdings = load_etf_holdings()
    holdings.setdefault("etfs", {}).pop(key, None)
    save_etf_holdings(holdings)

    settings = load_etf_settings()
    settings.setdefault("manual_add", {}).pop(key, None)
    settings.setdefault("manual_remove", {}).pop(key, None)
    save_etf_settings(settings)

    cache = load_etf_cache()
    cache.setdefault("etfs", {}).pop(key, None)
    # holding_analyst indeholder aktiedata på tværs af ETF'er og må derfor
    # ikke ryddes samlet ved sletning af én ETF. ETF'ens egen benchmarkcache
    # fjernes derimod altid.
    save_etf_cache(cache)


def etf_key(row):
    return f"{str(row.get('exchange','')).upper()}:{str(row.get('ticker','')).upper()}"


def _normalize_company_name(name):
    text=unescape(str(name or "")).upper()
    text=re.sub(r"\b(PLC|INC|CORP|CORPORATION|LTD|LIMITED|SA|SE|AG|NV|ASA|A/S|AB|CO|COMPANY|HOLDINGS?)\b", " ", text)
    return re.sub(r"[^A-Z0-9]+", "", text)


def _extract_holdings_from_tv_html(html):
    """Robust udtræk af TradingViews offentlige ETF-beholdninger.

    TradingViews holdings-side kan levere data på flere måder:
    1) som almindelig JSON i script-tags,
    2) som escaped JSON i sidens HTML,
    3) som den synlige Fund composition-tabel.

    Den tidligere parser krævede symbol, navn og vægt i én helt bestemt
    rækkefølge i samme flade JSON-blok. Det gav tomme resultater, selv om
    TradingView viste positionerne på siden. Denne version gennemgår JSON
    rekursivt og har desuden en tekstbaseret fallback.
    """
    from html import unescape as _html_unescape

    raw = html or ""
    decoded = _html_unescape(raw).replace('\\"', '"').replace('\\u0026', '&')
    candidates = []

    symbol_keys = ("symbol", "ticker", "shortName", "short_name")
    name_keys = ("name", "description", "companyName", "company_name", "longName", "long_name")
    weight_keys = (
        "weight", "weightPercentage", "weight_percentage", "percentage",
        "fundWeight", "fund_weight", "holdingWeight", "holding_weight",
    )
    exchange_keys = ("exchange", "exchangeCode", "exchange_code", "market")

    def add_candidate(symbol, name, weight, exchange=""):
        symbol = str(symbol or "").upper().strip()
        exchange = str(exchange or "").upper().strip()
        name = str(name or "").strip()
        value = parse_float(weight, None)
        if value is None:
            return
        # TradingView kan levere vægt enten som 0,0732 eller 7,32.
        if 0 < value <= 1.0:
            value *= 100.0
        if not (0 < value <= 100.0):
            return
        if ':' in symbol:
            ex_from_symbol, symbol = symbol.split(':', 1)
            exchange = exchange or ex_from_symbol
        symbol = re.sub(r'[^A-Z0-9.\-]', '', symbol)
        exchange = re.sub(r'[^A-Z0-9_\-]', '', exchange)
        if not symbol or len(symbol) > 20 or not name:
            return
        candidates.append({
            "exchange": exchange,
            "ticker": symbol,
            "name": name,
            "weight": float(value),
        })

    def walk_json(value):
        if isinstance(value, dict):
            symbol = next((value.get(k) for k in symbol_keys if value.get(k) not in (None, "")), None)
            name = next((value.get(k) for k in name_keys if value.get(k) not in (None, "")), None)
            weight = next((value.get(k) for k in weight_keys if value.get(k) not in (None, "")), None)
            exchange = next((value.get(k) for k in exchange_keys if value.get(k) not in (None, "")), "")
            if symbol is not None and name is not None and weight is not None:
                add_candidate(symbol, name, weight, exchange)
            for child in value.values():
                walk_json(child)
        elif isinstance(value, list):
            for child in value:
                walk_json(child)

    # 1) Gennemgå JSON i script-tags. Dette håndterer både __NEXT_DATA__ og
    # andre TradingView-stateblokke uden at være afhængig af felternes rækkefølge.
    for script in re.findall(r'<script[^>]*>(.*?)</script>', raw, flags=re.I | re.S):
        text = _html_unescape(script).strip()
        if not text:
            continue
        attempts = [text, text.replace('\\"', '"')]
        for attempt in attempts:
            try:
                walk_json(json.loads(attempt))
                break
            except Exception:
                pass

    # 2) Fleksibel JSON-regex, hvor felterne gerne må stå i forskellig orden.
    # Find små objektlignende tekststykker og udtræk felterne uafhængigt.
    for block in re.findall(r'\{[^{}]{20,1800}\}', decoded, flags=re.S):
        symbol_match = re.search(r'"(?:symbol|ticker|shortName|short_name)"\s*:\s*"([^"]+)"', block, re.I)
        name_match = re.search(r'"(?:name|description|companyName|company_name|longName|long_name)"\s*:\s*"([^"]+)"', block, re.I)
        weight_match = re.search(r'"(?:weight|weightPercentage|weight_percentage|percentage|fundWeight|fund_weight|holdingWeight|holding_weight)"\s*:\s*"?([0-9]+(?:[.][0-9]+)?)', block, re.I)
        exchange_match = re.search(r'"(?:exchange|exchangeCode|exchange_code|market)"\s*:\s*"([^"]+)"', block, re.I)
        if symbol_match and name_match and weight_match:
            add_candidate(
                symbol_match.group(1),
                name_match.group(1),
                weight_match.group(1).replace(',', '.'),
                exchange_match.group(1) if exchange_match else "",
            )

    # 3) Fallback til den synlige tabel. HTML-tags omdannes til linjeskift,
    # så mønstre som NVDA / NVIDIA Corporation / 7.32% kan genkendes.
    visible = re.sub(r'<(?:br|/tr|/td|/div|/span|/a|li|/li)[^>]*>', '\n', decoded, flags=re.I)
    visible = re.sub(r'<[^>]+>', ' ', visible)
    visible = _html_unescape(visible)
    lines = [re.sub(r'\s+', ' ', line).strip() for line in visible.splitlines()]
    lines = [line for line in lines if line]

    for i, line in enumerate(lines):
        pct_match = re.fullmatch(r'([0-9]+(?:[.][0-9]+)?)\s*%', line)
        if not pct_match:
            continue
        # Søg få linjer bagud efter et ticker-lignende felt og et navn.
        window = lines[max(0, i - 6):i]
        ticker = ""
        name_parts = []
        for part in reversed(window):
            compact = re.sub(r'\s+', '', part).upper()
            if not ticker and re.fullmatch(r'[A-Z][A-Z0-9.\-]{0,14}', compact):
                ticker = compact
                continue
            if ticker and len(part) >= 2 and '%' not in part and not re.fullmatch(r'[0-9.]+[KMBT]?', part, re.I):
                name_parts.insert(0, part)
                if len(' '.join(name_parts)) >= 5:
                    break
        if ticker and name_parts:
            add_candidate(ticker, ' '.join(name_parts), pct_match.group(1).replace(',', '.'))

    # Dedup og sorter. Samme ticker kan optræde flere gange i sidens state.
    seen = set()
    out = []
    for row in sorted(candidates, key=lambda x: x['weight'], reverse=True):
        key = (row['ticker'], _normalize_company_name(row['name']))
        if key in seen:
            continue
        seen.add(key)
        out.append(row)
        if len(out) >= 10:
            break
    return out

def fetch_etf_top_holdings(item):
    slug=tradingview_symbol_slug(item)
    if not slug: return []
    urls=[
        f"https://www.tradingview.com/symbols/{slug}/holdings/",
        f"https://www.tradingview.com/symbols/{slug}/analysis/",
        f"https://www.tradingview.com/symbols/{slug}/",
    ]
    for url in urls:
        try:
            rows_found=_extract_holdings_from_tv_html(_read_url_text(url,timeout=20))
            if rows_found: return rows_found
        except Exception:
            continue
    return []


def _holding_name_is_noise(name):
    """True for hjælpefelter fra TradingViews tabel, ikke egentlige selskaber."""
    text = re.sub(r"\s+", " ", unescape(str(name or "")).strip())
    upper = text.upper()
    if not text:
        return True
    if upper in {"MARKET VALUE", "WEIGHT", "SHARES", "HOLDINGS", "FUND COMPOSITION"}:
        return True
    # Eksempler fra TradingView: 57.70 M EUR, 4.2 B USD, EUR AAPL.
    if re.fullmatch(r"[0-9.]+\s*[KMBT]\s*(EUR|USD|GBP|GBX|DKK|SEK|NOK|CHF|JPY|CAD|AUD)?", upper):
        return True
    if re.fullmatch(r"(EUR|USD|GBP|GBX|DKK|SEK|NOK|CHF|JPY|CAD|AUD)\s+[A-Z0-9.\-]+", upper):
        return True
    return False


def _holding_quality(row):
    """Score til valg af den bedste række, når TradingView giver dubletter."""
    exchange = str(row.get("exchange", "")).strip()
    ticker = str(row.get("ticker", "")).strip()
    name = str(row.get("name", "")).strip()
    score = 0
    if exchange:
        score += 4
    if name and not _holding_name_is_noise(name):
        score += 4
    if len(name) >= 5:
        score += 1
    if ticker and not ticker.endswith("."):
        score += 1
    return score


def _clean_etf_holdings(rows):
    """Fjern hjælpefelter, ugyldige rækker og ticker-dubletter."""
    best = {}
    for raw in rows or []:
        if not isinstance(raw, dict):
            continue
        row = dict(raw)
        row["exchange"] = str(row.get("exchange", "")).upper().strip()
        row["ticker"] = re.sub(r"[^A-Z0-9.\-]", "", str(row.get("ticker", "")).upper().strip())
        row["name"] = re.sub(r"\s+", " ", unescape(str(row.get("name", ""))).strip())
        row["weight"] = parse_float(row.get("weight"), None)
        if not row["ticker"] or row["weight"] is None or not (0 < row["weight"] <= 100):
            continue
        if _holding_name_is_noise(row["name"]):
            continue
        # Et selskabsnavn skal indeholde mindst to bogstaver og må ikke blot være tickeren.
        if len(re.findall(r"[A-Za-z]", row["name"])) < 2:
            continue
        key = row["ticker"]
        previous = best.get(key)
        if previous is None or _holding_quality(row) > _holding_quality(previous):
            best[key] = row
    return sorted(best.values(), key=lambda x: float(x.get("weight", 0)), reverse=True)[:10]


def etf_effective_holdings(key):
    data=load_etf_holdings(); base=list((data.get("etfs",{}).get(key,{}) or {}).get("holdings",[]) or [])
    settings=load_etf_settings(); removed={str(x).upper() for x in settings.get("manual_remove",{}).get(key,[])}
    out=[]
    for h in _clean_etf_holdings(base):
        hk=f"{str(h.get('exchange','')).upper()}:{str(h.get('ticker','')).upper()}" if h.get('exchange') else str(h.get('ticker','')).upper()
        if hk in removed or str(h.get('ticker','')).upper() in removed: continue
        row=dict(h); row["source"]="Auto"; out.append(row)
    for h in settings.get("manual_add",{}).get(key,[]):
        if isinstance(h,dict):
            row=dict(h); row["source"]="Manuel"; out.append(row)
    # Manuel tilføjelse vinder over en automatisk dublet med samme ticker.
    dedup={}
    for row in out:
        ti=str(row.get("ticker","")).upper()
        if not ti: continue
        if ti not in dedup or row.get("source")=="Manuel": dedup[ti]=row
    return sorted(dedup.values(), key=lambda x: float(parse_float(x.get("weight"),0.0) or 0.0), reverse=True)


def _portfolio_match_for_holding(holding):
    ti=str(holding.get("ticker","")).upper(); ex=str(holding.get("exchange","")).upper()
    namekey=_normalize_company_name(holding.get("name"))
    for item in portfolio:
        if is_cash_item(item): continue
        if ti and str(item.get("ticker","")).upper()==ti:
            return item,"Ticker"
        if ex and ti and position_key(item)==f"{ex}:{ti}":
            return item,"Børs+ticker"
    if namekey:
        for item in portfolio:
            if is_cash_item(item): continue
            ik=_normalize_company_name(item.get("name"))
            if ik and (ik==namekey or (len(ik)>=7 and (ik in namekey or namekey in ik))):
                return item,"Navn"
    return None,""


def fetch_monthly_history(tv,item,n_bars=280):
    try:
        df=tv.get_hist(symbol=item["ticker"],exchange=item["exchange"],interval=Interval.in_daily,n_bars=n_bars)
        if df is None or df.empty: return None
        return df.dropna(subset=["close"]).copy()
    except Exception:
        return None


def _monthly_values(df):
    return {f"pct_{m}m":pct_change_from_bars(df,21*m) for m in range(1,13)}


def _etf_trend_value(monthly):
    """Nutidig månedlig trend fra 1M, 3M og 6M.

    Længere perioder omregnes til gennemsnitligt månedstempo, så 1M ikke
    sammenlignes direkte med et akkumuleret 6M-afkast.
    """
    p1 = parse_float((monthly or {}).get("pct_1m"), None)
    p3 = parse_float((monthly or {}).get("pct_3m"), None)
    p6 = parse_float((monthly or {}).get("pct_6m"), None)
    values = []
    if p1 is not None: values.append((0.50, p1))
    if p3 is not None: values.append((0.30, p3 / 3.0))
    if p6 is not None: values.append((0.20, p6 / 6.0))
    denom = sum(w for w, _ in values)
    return sum(w * v for w, v in values) / denom if denom > 0 else None


def _etf_acceleration_value(monthly):
    p1 = parse_float((monthly or {}).get("pct_1m"), None)
    p3 = parse_float((monthly or {}).get("pct_3m"), None)
    if p1 is None or p3 is None:
        return None
    return p1 - p3 / 3.0


def _etf_trend_status(trend, acceleration):
    if trend is None:
        return "Ingen data"
    if trend < -1.0:
        return "Negativ"
    if acceleration is None:
        return "Positiv" if trend > 0 else "Stabil"
    if acceleration >= 1.5:
        return "Tiltager"
    if acceleration <= -1.5:
        return "Aftager"
    return "Stabil"


def _etf_basis_label(match_count, coverage):
    coverage = parse_float(coverage, 0.0) or 0.0
    if match_count >= 4 and coverage >= 30.0:
        return "Høj"
    if match_count >= 2 and coverage >= 15.0:
        return "Middel"
    return "Lav"


def _etf_signal(match_count, basis, etf_trend, mine_trend, difference, acceleration):
    if match_count == 0:
        return "Ikke repræsenteret i porteføljen", "neutral"
    if basis == "Lav" or mine_trend is None or etf_trend is None:
        return "For lidt datagrundlag", "neutral"
    if etf_trend < -1.0:
        return "Tema svækkes", "neutral"
    if difference is not None and difference <= -3.0:
        return "ETF trækker fra – undersøg manglende positioner", "warning"
    if difference is not None and difference >= 3.0:
        return "Du fører ETF'en", "positive"
    if acceleration is not None and acceleration >= 1.5 and etf_trend > 0:
        return "Tema accelererer", "attention"
    return "Følger ETF", "normal"


def update_phase5_views():
    if "phase5_etf_tree" in globals(): show_phase5_etfs()
    if "phase5_benchmark_tree" in globals(): show_phase5_benchmark()
    if "phase5_etf_combo" in globals(): refresh_phase5_etf_combo()
    if "phase5_all_holding_tree" in globals(): show_all_etf_holdings()


def update_etf_benchmark(force=False):
    global phase5_etf_rows, phase5_benchmark_rows
    if TvDatafeed is None:
        root.after(0, lambda: messagebox.showerror("tvDatafeed mangler", "Installer tvDatafeed for at hente ETF-data."))
        return
    etfs = load_etf_list()
    if not etfs:
        root.after(0, lambda: messagebox.showinfo("ETF Benchmark", "ETF-listen er tom. Opret eller importer ETF'er først."))
        return

    tv = TvDatafeed()
    cache = load_etf_cache()
    if force:
        cache = {"schema": "PORTEFOLJE_ETF_CACHE_V1", "date": "", "etfs": {}, "stocks": {}, "holding_analyst": {}}
    holdings_data = load_etf_holdings()

    # Hent analytikerkursmål for alle brugbare ETF-positioner i ét samlet
    # TradingView-scannerbatch. Resultaterne gemmes i dags-cachen og genbruges
    # ved skift mellem ETF'er, så tabellen åbner hurtigt.
    all_holdings_by_key = {}
    for etf_item in etfs:
        for holding in etf_effective_holdings(etf_key(etf_item)):
            holding_key = etf_key(holding)
            if holding_key != ":" and holding.get("exchange") and holding.get("ticker"):
                all_holdings_by_key[holding_key] = {
                    "exchange": str(holding.get("exchange", "")).upper(),
                    "ticker": str(holding.get("ticker", "")).upper(),
                    "name": str(holding.get("name", holding.get("ticker", ""))),
                }

    analyst_cache = cache.setdefault("holding_analyst", {})
    required_holding_fields = ("sector", "industry", "country")
    analyst_items = list(all_holdings_by_key.values()) if force or cache.get("date") != today_key() else [
        item for key, item in all_holdings_by_key.items()
        if key not in analyst_cache
        or not isinstance(analyst_cache.get(key), dict)
        or any(value_is_missing(analyst_cache.get(key, {}).get(field)) for field in required_holding_fields)
    ]
    if analyst_items:
        analyst_cache.update(fetch_scanner_rows_batch(analyst_items))
        save_etf_cache(cache)

    etf_rows = []
    analysis_rows = []
    portfolio_values = {
        position_key(r): float(r.get("sort_value_dkk", 0) or 0)
        for r in phase2_rows if not r.get("is_summary") and not is_cash_row(r)
    }

    for idx, item in enumerate(etfs, 1):
        key = etf_key(item)
        root.after(0, lambda i=idx, n=len(etfs), nm=item["name"]: phase5_status_var.set(f"Henter ETF {i}/{n}: {nm}"))
        cached = cache.get("etfs", {}).get(key, {}) if cache.get("date") == today_key() and not force else {}
        vals = cached.get("monthly") if isinstance(cached, dict) else None
        price = cached.get("price") if isinstance(cached, dict) else None
        if not isinstance(vals, dict):
            df = fetch_monthly_history(tv, item)
            vals = _monthly_values(df) if df is not None else {f"pct_{m}m": None for m in range(1, 13)}
            price = float(df["close"].iloc[-1]) if df is not None and not df.empty else None
            cache.setdefault("etfs", {})[key] = {"monthly": vals, "price": price, "updated": datetime.now().isoformat(timespec="seconds")}
            save_etf_cache(cache)

        holding_entry = holdings_data.get("etfs", {}).get(key, {}) or {}
        effective = etf_effective_holdings(key)
        coverage = sum(float(parse_float(h.get("weight"), 0.0) or 0.0) for h in effective)
        etf_trend = _etf_trend_value(vals)
        acceleration = _etf_acceleration_value(vals)
        etf_rows.append({
            "exchange": item["exchange"], "ticker": item["ticker"], "name": item["name"],
            "price": format_num(price, 2),
            "pct_1m": format_pct(vals.get("pct_1m")),
            "pct_3m": format_pct(vals.get("pct_3m")),
            "pct_6m": format_pct(vals.get("pct_6m")),
            "trend": format_pct(etf_trend),
            "acceleration": format_pct(acceleration),
            "trend_status": _etf_trend_status(etf_trend, acceleration),
            "holdings_count": str(len(effective)),
            "coverage": (format_num(coverage, 1) + " %") if effective else "-",
            "holdings_updated": holding_entry.get("updated_at", "-"),
        })

        matched = []
        seen_matches = set()
        for h in effective:
            match, method = _portfolio_match_for_holding(h)
            if match and position_key(match) not in seen_matches:
                matched.append((match, method))
                seen_matches.add(position_key(match))

        components = []
        for match, method in matched:
            skey = position_key(match)
            weight_value = portfolio_values.get(skey, 0.0)
            scached = cache.get("stocks", {}).get(skey, {}) if cache.get("date") == today_key() and not force else {}
            svals = scached.get("monthly") if isinstance(scached, dict) else None
            if not isinstance(svals, dict):
                sdf = fetch_monthly_history(tv, match)
                svals = _monthly_values(sdf) if sdf is not None else {f"pct_{m}m": None for m in range(1, 13)}
                cache.setdefault("stocks", {})[skey] = {"monthly": svals, "updated": datetime.now().isoformat(timespec="seconds")}
                save_etf_cache(cache)
            components.append((weight_value, svals))

        # Min tematrend beregnes først på 1M/3M/6M og derefter med samme model som ETF'en.
        mine_monthly = {}
        for m in (1, 3, 6):
            usable = [(w, v.get(f"pct_{m}m")) for w, v in components if v.get(f"pct_{m}m") is not None]
            denom = sum(w for w, _ in usable)
            if denom <= 0 and usable:
                mine_monthly[f"pct_{m}m"] = sum(v for _, v in usable) / len(usable)
            else:
                mine_monthly[f"pct_{m}m"] = sum(w * v for w, v in usable) / denom if denom > 0 else None
        mine_trend = _etf_trend_value(mine_monthly)
        difference = mine_trend - etf_trend if mine_trend is not None and etf_trend is not None else None
        basis = _etf_basis_label(len(components), coverage)
        signal, signal_tag = _etf_signal(len(components), basis, etf_trend, mine_trend, difference, acceleration)
        capital = sum(portfolio_values.get(position_key(m), 0.0) for m, _ in matched)
        analysis_rows.append({
            "exchange": item["exchange"], "ticker": item["ticker"], "name": item["name"],
            "matches": str(len(components)), "capital": format_dkk(capital),
            "coverage": (format_num(coverage, 1) + " %") if effective else "-",
            "basis": basis,
            "etf_trend": format_pct(etf_trend), "mine_trend": format_pct(mine_trend),
            "difference": format_pct(difference), "acceleration": format_pct(acceleration),
            "signal": signal, "signal_tag": signal_tag,
        })

    phase5_etf_rows = etf_rows
    phase5_benchmark_rows = analysis_rows
    save_etf_cache(cache)
    root.after(0, update_phase5_views)
    root.after(0, lambda: phase5_status_var.set(f"ETF-temaanalyse opdateret: {len(etf_rows)} ETF'er."))


def start_etf_update(force=False,holdings=False):
    phase5_update_button.config(state="disabled"); phase5_force_button.config(state="disabled"); phase5_holdings_button.config(state="disabled")
    def worker():
        try:
            if holdings:
                data=load_etf_holdings(); etfs=load_etf_list(); changed=0
                for i,item in enumerate(etfs,1):
                    root.after(0,lambda i=i,n=len(etfs),nm=item['name']: phase5_status_var.set(f"Henter toppositioner {i}/{n}: {nm}"))
                    found=fetch_etf_top_holdings(item)
                    if found:
                        key=etf_key(item); data.setdefault('etfs',{})[key]={"exchange":item['exchange'],"ticker":item['ticker'],"name":item['name'],"updated_at":datetime.now().isoformat(timespec='seconds'),"holdings":found}; changed+=1
                        save_etf_holdings(data)
                root.after(0, refresh_phase5_etf_combo)
                if changed:
                    root.after(0, lambda: phase5_status_var.set(f"Toppositioner fundet og gemt for {changed}/{len(etfs)} ETF'er."))
                else:
                    root.after(0, lambda: phase5_status_var.set("Ingen toppositioner blev fundet. TradingViews sideformat kunne ikke aflæses."))
            update_etf_benchmark(force=force)
        finally:
            root.after(0,lambda: phase5_update_button.config(state="normal")); root.after(0,lambda: phase5_force_button.config(state="normal")); root.after(0,lambda: phase5_holdings_button.config(state="normal"))
    threading.Thread(target=worker,daemon=True).start()


def show_phase5_etfs():
    phase5_etf_tree.delete(*phase5_etf_tree.get_children())
    for i, row in enumerate(phase5_etf_rows):
        status = row.get("trend_status")
        tag = "attention" if status == "Tiltager" else ("warning" if status in ("Aftager", "Negativ") else ("even" if i % 2 == 0 else "odd"))
        phase5_etf_tree.insert("", "end", values=[row.get(c, "") for c in ETF_COLUMN_IDS], tags=(tag,))


def show_phase5_benchmark():
    phase5_benchmark_tree.delete(*phase5_benchmark_tree.get_children())
    for i, row in enumerate(phase5_benchmark_rows):
        tag = row.get("signal_tag") or ("even" if i % 2 == 0 else "odd")
        phase5_benchmark_tree.insert("", "end", values=[row.get(c, "") for c in ETF_BENCHMARK_COLUMN_IDS], tags=(tag,))


def refresh_phase5_etf_combo():
    """Opdatér ETF-valget uden at miste den valgte ETF."""
    etfs = load_etf_list()
    previous = selected_phase5_etf()
    previous_key = etf_key(previous) if previous else phase5_current_etf_key
    choices = [f"{x['name']} — {etf_key(x)}" for x in etfs]
    phase5_etf_combo['values'] = choices

    selected_index = -1
    if previous_key:
        selected_index = next((i for i, item in enumerate(etfs) if etf_key(item) == previous_key), -1)
    if selected_index < 0 and choices:
        selected_index = 0
    if selected_index >= 0:
        phase5_etf_combo.current(selected_index)
    else:
        phase5_etf_combo.set("")
    show_selected_etf_holdings()


def selected_phase5_etf():
    """Find valgt ETF via den viste entydige BØRS:TICKER-nøgle.

    Comboboxens numeriske indeks kan blive forældet, når ETF-listen genindlæses.
    Derfor bruges teksten efter sidste tankestreg som primær identifikation.
    """
    text = str(phase5_etf_combo.get() or "").strip()
    selected_key = text.rsplit(" — ", 1)[-1].upper().strip() if " — " in text else ""
    etfs = load_etf_list()
    if selected_key:
        for item in etfs:
            if etf_key(item) == selected_key:
                return item
    idx = phase5_etf_combo.current()
    return etfs[idx] if 0 <= idx < len(etfs) else None


def _etf_holding_classification(holding):
    """Returnér Sektor, Industri og Land / Region fra samme TradingView-cache som kursmålene."""
    key = etf_key(holding)
    if key == ":":
        return "-", "-", "-"
    cache = load_etf_cache()
    scanner_row = cache.get("holding_analyst", {}).get(key, {})
    if not isinstance(scanner_row, dict):
        return "-", "-", "-"
    return (
        str(scanner_row.get("sector") or "-"),
        str(scanner_row.get("industry") or "-"),
        str(scanner_row.get("country") or "-"),
    )


def _etf_holding_analyst_percentages(holding):
    """Returnér Bull/Base/Bear 1Y-procenter for en ETF-position fra dags-cachen."""
    key = etf_key(holding)
    if key == ":":
        return None, None, None
    cache = load_etf_cache()
    scanner_row = cache.get("holding_analyst", {}).get(key, {})
    if not isinstance(scanner_row, dict) or not scanner_row:
        return None, None, None
    price = parse_float(scanner_row.get("kurs_f2"), None)
    currency = currency_for_exchange(holding.get("exchange"))
    daily_fx = load_daily_cache().get("fx_rates", {})
    fx_to_dkk = parse_float(daily_fx.get(currency), FALLBACK_FX_DKK.get(currency, 1.0))
    usd_to_dkk = parse_float(daily_fx.get("USD"), FALLBACK_FX_DKK["USD"])
    analyst = analyst_scenario_values(
        scanner_row,
        price,
        currency=currency,
        fx_to_dkk=fx_to_dkk,
        usd_to_dkk=usd_to_dkk,
    )
    return analyst.get("bull"), analyst.get("base"), analyst.get("bear")


def show_selected_etf_holdings(event=None):
    global phase5_current_etf_key
    phase5_holding_tree.delete(*phase5_holding_tree.get_children())
    item = selected_phase5_etf()
    if not item:
        phase5_current_etf_key = ""
        if "phase5_holdings_summary_var" in globals():
            phase5_holdings_summary_var.set("")
        return
    phase5_current_etf_key = etf_key(item)
    holdings = etf_effective_holdings(phase5_current_etf_key)
    if not holdings:
        if "phase5_holdings_summary_var" in globals():
            phase5_holdings_summary_var.set("Ingen brugbare toppositioner er gemt for denne ETF.")
        empty_values = {column_id: "-" for column_id in ETF_HOLDING_COLUMN_IDS}
        empty_values.update({"rank": "", "name": "Ingen toppositioner gemt for denne ETF"})
        phase5_holding_tree.insert('', 'end', values=[empty_values[c] for c in ETF_HOLDING_COLUMN_IDS], tags=('odd',))
        return

    total_portfolio_value = sum(
        float(r.get("sort_value_dkk", 0.0) or 0.0)
        for r in phase2_rows if not r.get("is_summary")
    )
    values_by_key = {
        position_key(r): float(r.get("sort_value_dkk", 0.0) or 0.0)
        for r in phase2_rows if not r.get("is_summary") and not is_cash_row(r)
    }
    matched_count = 0
    matched_capital = 0.0
    total_etf_weight = 0.0
    total_portfolio_weight = 0.0
    analyst_values = {"bull": [], "base": [], "bear": []}

    for i,h in enumerate(holdings,1):
        match,method=_portfolio_match_for_holding(h)
        portfolio_value = values_by_key.get(position_key(match), 0.0) if match else 0.0
        portfolio_weight = portfolio_value / total_portfolio_value * 100.0 if total_portfolio_value > 0 and match else None
        if match:
            matched_count += 1
            matched_capital += portfolio_value
        source = str(h.get('source','Auto'))
        match_text = source if match else "-"
        sector, industry, country = _etf_holding_classification(h)
        bull_pct, base_pct, bear_pct = _etf_holding_analyst_percentages(h)
        etf_weight = parse_float(h.get("weight"), 0.0) or 0.0
        total_etf_weight += etf_weight
        if portfolio_weight is not None:
            total_portfolio_weight += portfolio_weight
        for key_name, value in (("bull", bull_pct), ("base", base_pct), ("bear", bear_pct)):
            if value is not None:
                analyst_values[key_name].append(float(value))
        vals=[
            i,
            h.get('exchange','-') or '-',
            h.get('ticker','-'),
            h.get('name','-'),
            sector,
            industry,
            country,
            format_plain_pct(bull_pct),
            format_plain_pct(base_pct),
            format_plain_pct(bear_pct),
            format_pct(etf_weight).replace('+',''),
            format_pct(portfolio_weight).replace('+','') if portfolio_weight is not None else '-',
            'Ja' if match else 'Nej',
            match_text,
        ]
        phase5_holding_tree.insert('', 'end',values=vals,tags=('summary' if match else ('even' if i%2==0 else 'odd',)))

    def average_or_none(values):
        return sum(values) / len(values) if values else None

    total_values = {column_id: "" for column_id in ETF_HOLDING_COLUMN_IDS}
    total_values.update({
        "name": "Gennemsnit / sum",
        "bull_pct": format_plain_pct(average_or_none(analyst_values["bull"])),
        "base_pct": format_plain_pct(average_or_none(analyst_values["base"])),
        "bear_pct": format_plain_pct(average_or_none(analyst_values["bear"])),
        "weight": format_pct(total_etf_weight).replace("+", ""),
        "portfolio_weight": format_pct(total_portfolio_weight).replace("+", ""),
    })
    phase5_holding_tree.insert(
        "", "end",
        values=[total_values[column_id] for column_id in ETF_HOLDING_COLUMN_IDS],
        tags=("fixed_total",),
    )

    if "phase5_holdings_summary_var" in globals():
        phase5_holdings_summary_var.set(
            f"{len(holdings)} toppositioner · Match: {matched_count}/{len(holdings)} · "
            f"Samlet ETF-vægt: {format_num(total_etf_weight,1)} % · "
            f"Min kapital i match: {format_dkk(matched_capital)} DKK"
        )



def show_all_etf_holdings():
    """Vis alle fundne ETF-positioner samlet, én række pr. ETF-position."""
    phase5_all_holding_tree.delete(*phase5_all_holding_tree.get_children())
    etfs = load_etf_list()
    total_portfolio_value = sum(
        float(r.get("sort_value_dkk", 0.0) or 0.0)
        for r in phase2_rows if not r.get("is_summary")
    )
    values_by_key = {
        position_key(r): float(r.get("sort_value_dkk", 0.0) or 0.0)
        for r in phase2_rows if not r.get("is_summary") and not is_cash_row(r)
    }
    row_number = 0
    matched_count = 0
    total_etf_weight = 0.0
    total_portfolio_weight = 0.0
    analyst_values = {"bull": [], "base": [], "bear": []}

    for etf_item in etfs:
        etf_name = str(etf_item.get("name", etf_item.get("ticker", "-"))).strip() or "-"
        for holding in etf_effective_holdings(etf_key(etf_item)):
            row_number += 1
            match, _method = _portfolio_match_for_holding(holding)
            portfolio_value = values_by_key.get(position_key(match), 0.0) if match else 0.0
            portfolio_weight = (
                portfolio_value / total_portfolio_value * 100.0
                if total_portfolio_value > 0 and match else None
            )
            if match:
                matched_count += 1
            sector, industry, country = _etf_holding_classification(holding)
            bull_pct, base_pct, bear_pct = _etf_holding_analyst_percentages(holding)
            etf_weight = parse_float(holding.get("weight"), 0.0) or 0.0
            total_etf_weight += etf_weight
            if portfolio_weight is not None:
                total_portfolio_weight += portfolio_weight
            for key_name, value in (("bull", bull_pct), ("base", base_pct), ("bear", bear_pct)):
                if value is not None:
                    analyst_values[key_name].append(float(value))

            values = {
                "rank": row_number,
                "exchange": holding.get("exchange", "-") or "-",
                "ticker": holding.get("ticker", "-") or "-",
                "name": holding.get("name", "-") or "-",
                "sector": sector,
                "industry": industry,
                "country": country,
                "bull_pct": format_plain_pct(bull_pct),
                "base_pct": format_plain_pct(base_pct),
                "bear_pct": format_plain_pct(bear_pct),
                "weight": format_pct(etf_weight).replace("+", ""),
                "portfolio_weight": format_pct(portfolio_weight).replace("+", "") if portfolio_weight is not None else "-",
                "portfolio_match": "Ja" if match else "Nej",
                "etf_name": etf_name,
            }
            # Samme beslutningsfarver som i Watch list:
            # rød ved Base under 20 % eller utilstrækkeligt Bull/Bear-forhold,
            # derefter gul, grøn og stærk grøn efter Base-niveauet.
            if base_pct is None or bull_pct is None or bear_pct is None:
                row_tag = "even" if row_number % 2 == 0 else "odd"
            else:
                bull_bear_ok = bull_pct >= 2.0 * abs(bear_pct)
                if base_pct < 20.0 or not bull_bear_ok:
                    row_tag = "watch_red"
                elif base_pct < 30.0:
                    row_tag = "watch_yellow"
                elif base_pct < 40.0:
                    row_tag = "watch_green"
                else:
                    row_tag = "watch_strong_green"

            phase5_all_holding_tree.insert(
                "", "end",
                values=[values[column_id] for column_id in ETF_ALL_HOLDING_COLUMN_IDS],
                tags=(row_tag,),
            )

    if row_number == 0:
        empty_values = {column_id: "-" for column_id in ETF_ALL_HOLDING_COLUMN_IDS}
        empty_values.update({"rank": "", "name": "Ingen ETF-positioner er gemt"})
        phase5_all_holding_tree.insert(
            "", "end",
            values=[empty_values[column_id] for column_id in ETF_ALL_HOLDING_COLUMN_IDS],
            tags=("odd",),
        )
        phase5_all_holdings_summary_var.set("Ingen brugbare ETF-positioner er gemt.")
        return

    def average_or_none(values):
        return sum(values) / len(values) if values else None

    total_values = {column_id: "" for column_id in ETF_ALL_HOLDING_COLUMN_IDS}
    total_values.update({
        "name": "Gennemsnit",
        "bull_pct": format_plain_pct(average_or_none(analyst_values["bull"])),
        "base_pct": format_plain_pct(average_or_none(analyst_values["base"])),
        "bear_pct": format_plain_pct(average_or_none(analyst_values["bear"])),
    })
    phase5_all_holding_tree.insert(
        "", "end",
        values=[total_values[column_id] for column_id in ETF_ALL_HOLDING_COLUMN_IDS],
        tags=("fixed_total",),
    )
    phase5_all_holdings_summary_var.set(
        f"{row_number} fundne positioner fra {len(etfs)} ETF'er · "
        f"Match i porteføljen: {matched_count}/{row_number}"
    )

def edit_etf_list_window():
    win = tk.Toplevel(root)
    win.title("Rediger ETF-liste")
    win.geometry("900x650")
    win.transient(root)

    cols = [("exchange", "Børs", 130), ("ticker", "Ticker", 130), ("name", "Navn", 520)]
    working = [dict(x) for x in load_etf_list()]
    current_sort = None
    sort_descending = False

    # Fast indtastningslinje. Felterne nulstilles ikke efter Tilføj, så fx
    # XETR kan genbruges ved oprettelse af flere ETF'er efter hinanden.
    input_frame = tk.LabelFrame(win, text="Tilføj ETF", font=small_font, padx=10, pady=8)
    input_frame.pack(fill="x", padx=8, pady=(8, 4))
    input_frame.grid_columnconfigure(5, weight=1)

    exchange_var = tk.StringVar()
    ticker_var = tk.StringVar()
    name_var = tk.StringVar()

    tk.Label(input_frame, text="Børs:", font=small_font).grid(row=0, column=0, padx=(0, 5), pady=2, sticky="w")
    exchange_entry = tk.Entry(input_frame, textvariable=exchange_var, font=small_font, width=14)
    exchange_entry.grid(row=0, column=1, padx=(0, 12), pady=2, sticky="w")

    tk.Label(input_frame, text="Ticker:", font=small_font).grid(row=0, column=2, padx=(0, 5), pady=2, sticky="w")
    ticker_entry = tk.Entry(input_frame, textvariable=ticker_var, font=small_font, width=14)
    ticker_entry.grid(row=0, column=3, padx=(0, 12), pady=2, sticky="w")

    tk.Label(input_frame, text="Navn:", font=small_font).grid(row=0, column=4, padx=(0, 5), pady=2, sticky="w")
    name_entry = tk.Entry(input_frame, textvariable=name_var, font=small_font)
    name_entry.grid(row=0, column=5, padx=(0, 10), pady=2, sticky="ew")

    def apply_current_sort():
        if current_sort:
            working.sort(
                key=lambda row: str(row.get(current_sort, "")).casefold(),
                reverse=sort_descending,
            )

    def sort_list(col):
        nonlocal current_sort, sort_descending
        if current_sort == col:
            sort_descending = not sort_descending
        else:
            current_sort = col
            sort_descending = False
        apply_current_sort()
        render()

    tree_edit = build_tree(win, cols, sort_list)

    def update_headers():
        for col_id, title, _width in cols:
            arrow = ""
            if col_id == current_sort:
                arrow = " ▼" if sort_descending else " ▲"
            tree_edit.heading(col_id, text=title + arrow, command=lambda c=col_id: sort_list(c))

    def render():
        tree_edit.delete(*tree_edit.get_children())
        for i, item in enumerate(working):
            tree_edit.insert(
                "", "end", iid=str(i),
                values=[item.get(c, "") for c, _, _ in cols],
                tags=("even" if i % 2 == 0 else "odd",),
            )
        update_headers()

    def add():
        exchange = exchange_var.get().upper().strip()
        ticker = ticker_var.get().upper().strip()
        name = name_var.get().strip()

        if not exchange:
            messagebox.showwarning("Mangler børs", "Angiv børsen, fx XETR.", parent=win)
            exchange_entry.focus_set()
            return
        if not ticker:
            messagebox.showwarning("Mangler ticker", "Angiv ETF'ens ticker.", parent=win)
            ticker_entry.focus_set()
            return
        if not name:
            messagebox.showwarning("Mangler navn", "Angiv ETF'ens navn.", parent=win)
            name_entry.focus_set()
            return

        key = f"{exchange}:{ticker}"

        # Fase 5 har intet permanent ETF-kartotek. Samme børs+ticker betyder
        # derfor altid erstatning: gamle listeposter og eventuelle rester i
        # holdings, manuelle tilpasninger og ETF-cache fjernes først.
        working[:] = [item for item in working if etf_key(item) != key]
        purge_etf_data(key)
        working.append({"exchange": exchange, "ticker": ticker, "name": name})
        save_etf_list(working)
        apply_current_sort()
        render()
        refresh_phase5_etf_combo()
        phase5_status_var.set(f"{name} ({key}) er tilføjet eller overskrevet i ETF-listen.")

    def edit():
        sel = tree_edit.selection()
        if not sel:
            return
        item = working[int(sel[0])]
        name = simpledialog.askstring("Rediger ETF", "Navn:", initialvalue=item["name"], parent=win)
        if name is not None:
            item["name"] = name.strip() or item["ticker"]
            apply_current_sort()
            render()

    def delete():
        sel = tree_edit.selection()
        if not sel:
            return
        item = working.pop(int(sel[0]))
        key = etf_key(item)

        # ETF'en slettes permanent med det samme i hele fase 5. Den gemmes
        # ikke som en tidligere ETF, fordi fase 5 ikke fører analytikerhistorik.
        save_etf_list(working)
        purge_etf_data(key)
        refresh_phase5_etf_combo()
        apply_current_sort()
        render()
        phase5_status_var.set(f"{item.get('name', key)} ({key}) er slettet permanent fra fase 5.")

    def save():
        save_etf_list(working)
        refresh_phase5_etf_combo()
        win.destroy()
        phase5_status_var.set(f"ETF-liste gemt med {len(working)} ETF'er.")

    add_button = tk.Button(input_frame, text="Tilføj", font=small_font, command=add)
    add_button.grid(row=0, column=6, padx=(0, 0), pady=2, sticky="e")

    # Enter i et af felterne tilføjer den indtastede ETF.
    for entry in (exchange_entry, ticker_entry, name_entry):
        entry.bind("<Return>", lambda _event: add())

    bar = tk.Frame(win)
    bar.pack(fill="x", padx=8, pady=8)
    tk.Button(bar, text="Rediger navn", font=small_font, command=edit).pack(side="left")
    tk.Button(bar, text="Slet", font=small_font, command=delete).pack(side="left", padx=6)
    tk.Button(bar, text="Gem", font=small_font, command=save).pack(side="right")
    tk.Button(bar, text="Annuller", font=small_font, command=win.destroy).pack(side="right", padx=6)

    render()
    exchange_entry.focus_set()


def add_manual_etf_member():
    item=selected_phase5_etf()
    if not item:return
    choices=[x for x in portfolio if not is_cash_item(x)]
    if not choices:return
    labels=[f"{x['name']} — {position_key(x)}" for x in choices]
    choice=simpledialog.askstring('Tilføj aktie manuelt','Skriv ticker eller navn fra porteføljen:\n\n'+', '.join(labels[:15]),parent=root)
    if not choice:return
    q=choice.upper().strip(); match=next((x for x in choices if q in x['ticker'].upper() or q in x['name'].upper()),None)
    if not match:return
    settings=load_etf_settings(); key=etf_key(item); arr=settings.setdefault('manual_add',{}).setdefault(key,[])
    if not any(position_key(x)==position_key(match) for x in arr): arr.append({'exchange':match['exchange'],'ticker':match['ticker'],'name':match['name'],'weight':0.0})
    save_etf_settings(settings); show_selected_etf_holdings()


def remove_selected_etf_member():
    item=selected_phase5_etf(); sel=phase5_holding_tree.selection()
    if not item or not sel:return
    vals=phase5_holding_tree.item(sel[0],'values'); ticker=str(vals[2]).upper(); exchange=str(vals[1]).upper(); key=etf_key(item)
    settings=load_etf_settings(); adds=settings.setdefault('manual_add',{}).setdefault(key,[])
    newadds=[x for x in adds if str(x.get('ticker','')).upper()!=ticker]
    if len(newadds)!=len(adds): settings['manual_add'][key]=newadds
    else: settings.setdefault('manual_remove',{}).setdefault(key,[]).append(f'{exchange}:{ticker}' if exchange!='-' else ticker)
    save_etf_settings(settings); show_selected_etf_holdings()


# -----------------------------------------------------------------------------
# Porteføljebygger v0.03 – Aktieunivers og iterativ byggefunktion
# -----------------------------------------------------------------------------

BUILDER_VERSION = "0.20"
BUILDER_SCORE_EPSILON = 0.0001
BUILDER_STATUS_EVERY_TESTS = 40

# v0.31 – responsiv byggestatus. Selve optimeringen kører i en worker-tråd,
# mens GUI-tråden viser seneste trin cirka én gang pr. sekund.
_builder_build_in_progress = False
_builder_build_started_at = 0.0
_builder_progress_text = ""
_builder_progress_last_update = 0.0
_builder_progress_lock = threading.Lock()
_builder_web_progress_hook = None

def _builder_report_progress(text, force=False):
    """Opdatér seneste status og videresend den til web-UI'en, når den er aktiv."""
    global _builder_progress_text, _builder_progress_last_update
    now = time.monotonic()
    should_emit = False
    with _builder_progress_lock:
        if not force and now - _builder_progress_last_update < 0.20:
            return
        _builder_progress_text = str(text)
        _builder_progress_last_update = now
        should_emit = True
    if should_emit:
        hook = globals().get("_builder_web_progress_hook")
        if callable(hook):
            try:
                hook(str(text))
            except Exception:
                pass

def _builder_build_heartbeat():
    """GUI-heartbeat: vis at byggemotoren stadig arbejder, cirka hvert sekund."""
    if not _builder_build_in_progress:
        return
    with _builder_progress_lock:
        text = _builder_progress_text or "Bygger portefølje"
    elapsed = max(0, int(time.monotonic() - _builder_build_started_at))
    dots = "." * (1 + (elapsed % 3))
    try:
        status_var.set(f"{text} | arbejdet i {elapsed} s{dots}")
    except Exception:
        pass
    root.after(1000, _builder_build_heartbeat)

def _builder_set_build_button_state(state):
    try:
        builder_build_button.config(state=state)
    except Exception:
        pass


def _default_builder_settings():
    return {
        "currency": "DKK",
        "portfolio_value_input": 2_000_000.0,
        "minimum_position_input": 20_000.0,
        "portfolio_value_dkk": 2_000_000.0,
        "minimum_position_dkk": 20_000.0,
        "minimum_stocks_per_sector": 3,
        "maximum_stocks": 40,
        # Prioriteringen normaliseres automatisk, så brugeren kan arbejde med
        # intuitive relative vægte uden at summen nødvendigvis er præcis 100.
        "objective_weights": {
            "base_1y": 40.0,
            "stock_score": 30.0,
            "structure": 15.0,
            "sector": 10.0,
            "industry": 7.0,
            "region": 5.0,
            "target_trend": 10.0,
            "dividend": 0.0,
        },
        "use_locked_stocks": True,
        "use_target_trend": True,
        "use_dividend_target": False,
        "dividend_target_pct": 2.0,
        "region_targets": dict(DEFAULT_REGION_TARGETS),
        "sector_targets": dict(DEFAULT_SECTOR_TARGETS),
        "structure_targets": dict(STRUCTURE_PROFILES["Balanceret"]["targets"]),
        # Individuel industripræference: -100 = stærkt fravalg, 0 = neutral,
        # +100 = stærk prioritering. Industri-vægten bestemmer den samlede styrke.
        "industry_preferences": {},
    }


def load_builder_settings():
    data = _default_builder_settings()
    try:
        if BUILDER_SETTINGS_FILE.exists():
            loaded = json.loads(BUILDER_SETTINGS_FILE.read_text(encoding="utf-8"))
            if isinstance(loaded, dict):
                currency = str(loaded.get("currency", data.get("currency", "DKK")) or "DKK").upper().strip()
                data["currency"] = currency if currency in SUPPORTED_PORTFOLIO_CURRENCIES else "DKK"
                data["portfolio_value_input"] = max(1.0, normalize_number(loaded.get("portfolio_value_input", loaded.get("portfolio_value_dkk")), data["portfolio_value_input"]))
                data["minimum_position_input"] = max(0.0, normalize_number(loaded.get("minimum_position_input", loaded.get("minimum_position_dkk")), data["minimum_position_input"]))
                data["portfolio_value_dkk"] = max(1.0, normalize_number(loaded.get("portfolio_value_dkk"), data["portfolio_value_dkk"]))
                data["minimum_position_dkk"] = max(0.0, normalize_number(loaded.get("minimum_position_dkk"), data["minimum_position_dkk"]))
                data["minimum_stocks_per_sector"] = max(0, int(normalize_number(loaded.get("minimum_stocks_per_sector"), data["minimum_stocks_per_sector"])))
                data["maximum_stocks"] = max(1, int(normalize_number(loaded.get("maximum_stocks"), data["maximum_stocks"])))
                data["use_locked_stocks"] = bool(loaded.get("use_locked_stocks", data["use_locked_stocks"]))
                data["use_target_trend"] = bool(loaded.get("use_target_trend", data["use_target_trend"]))
                data["use_dividend_target"] = bool(loaded.get("use_dividend_target", data["use_dividend_target"]))
                data["dividend_target_pct"] = max(0.0, normalize_number(loaded.get("dividend_target_pct"), data["dividend_target_pct"]))
                source_weights = loaded.get("objective_weights", {})
                if isinstance(source_weights, dict):
                    for key in data["objective_weights"]:
                        if key in source_weights:
                            data["objective_weights"][key] = max(0.0, normalize_number(source_weights.get(key), data["objective_weights"][key]))
                for key, cats in (("region_targets", REGION_CATEGORIES), ("sector_targets", SECTOR_CATEGORIES), ("structure_targets", STRUCTURE_LAYER_ORDER)):
                    source = loaded.get(key, {})
                    if isinstance(source, dict):
                        # v0.40: migrér kun de gamle, helt uændrede standarder.
                        # Egne brugerdefinerede sektor-/strukturlagsmål bevares.
                        if key == "sector_targets":
                            old_sector = {
                                cat: max(0.0, normalize_number(source.get(cat), -999999.0))
                                for cat in SECTOR_CATEGORIES
                            }
                            if (
                                all(
                                    abs(old_sector.get(cat, -999999.0) - OLD_DEFAULT_SECTOR_TARGETS.get(cat, 0.0)) < 1e-9
                                    for cat in SECTOR_CATEGORIES
                                )
                                or all(
                                    abs(old_sector.get(cat, -999999.0) - PREVIOUS_DEFAULT_SECTOR_TARGETS.get(cat, 0.0)) < 1e-9
                                    for cat in SECTOR_CATEGORIES
                                )
                            ):
                                source = dict(DEFAULT_SECTOR_TARGETS)
                        elif key == "structure_targets":
                            old_structure_default = {
                                "Fundament": 50.0, "Vækst": 30.0,
                                "Accelerator": 15.0, "Potentiale": 5.0,
                            }
                            old_structure = {
                                cat: max(0.0, normalize_number(source.get(cat), -999999.0))
                                for cat in STRUCTURE_LAYER_ORDER
                            }
                            if all(
                                abs(old_structure.get(cat, -999999.0) - old_structure_default.get(cat, 0.0)) < 1e-9
                                for cat in STRUCTURE_LAYER_ORDER
                            ):
                                source = dict(STRUCTURE_PROFILES["Balanceret"]["targets"])

                        # v0.33: migrér den gamle samlede Norden-andel til de to nye
                        # regioner, men kun hvis den gamle fil endnu ikke allerede
                        # indeholder de nye kategorier. En brugerdefineret Norden-
                        # procent bevares dermed som samme samlede nordiske andel.
                        if key == "region_targets" and "Norden" in source and "Danmark" not in source and "Øvrige Norden" not in source:
                            old_nordic = max(0.0, normalize_number(source.get("Norden"), 10.0))
                            data[key]["Danmark"] = old_nordic / 2.0
                            data[key]["Øvrige Norden"] = old_nordic / 2.0
                        for cat in cats:
                            if cat in source:
                                data[key][cat] = max(0.0, normalize_number(source.get(cat), data[key].get(cat, 0.0)))
                source_industry_preferences = loaded.get("industry_preferences", {})
                if isinstance(source_industry_preferences, dict):
                    data["industry_preferences"] = {
                        str(k): clamp(normalize_number(v, 0.0), -100.0, 100.0)
                        for k, v in source_industry_preferences.items()
                    }
    except Exception:
        pass
    return data


def save_builder_settings(data):
    clean = dict(data or {})
    clean["schema"] = "PORTEFOLJEBYGGER_SETTINGS_V2"
    BUILDER_SETTINGS_FILE.write_text(json.dumps(clean, ensure_ascii=False, indent=2), encoding="utf-8")


def _universe_clean(items):
    seen = set(); out = []
    for item in items or []:
        if not isinstance(item, dict):
            continue
        x = normalize_item(item)
        if is_cash_item(x) or not x.get("exchange") or not x.get("ticker"):
            continue
        key = position_key(x)
        if key in seen:
            continue
        seen.add(key)
        out.append({"exchange": x["exchange"], "ticker": x["ticker"], "name": x.get("name", x["ticker"]), "locked": bool(item.get("locked", False))})
    return out


def _stock_universe_payload(items):
    clean = _universe_clean(items)
    return clean, {"schema": "PORTEFOLJEBYGGER_STOCK_UNIVERSE_V2", "stocks": clean}


def _read_stock_universe_file(path):
    """Læs én universfil uden fallback eller sideeffekter."""
    obj = json.loads(Path(path).read_text(encoding="utf-8"))
    items = obj.get("stocks", obj.get("positions", [])) if isinstance(obj, dict) else obj
    if not isinstance(items, list):
        raise ValueError("Aktieuniversets 'stocks' skal være en liste.")
    return _universe_clean(items)


def _atomic_write_stock_universe(path, payload):
    """Skriv JSON atomisk, så andre tråde aldrig kan læse en halv fil."""
    path = Path(path)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    os.replace(tmp, path)


def load_stock_universe():
    """Indlæs Fase 0-universet uden at kunne destruere det ved en læserace.

    Tidligere betød enhver kortvarig JSON-læsefejl, at funktionen faldt tilbage
    til aktiekartoteket og straks GEMTE fallback-listen som aktieunivers.json.
    Under en samtidig worker-gemning kunne GUI-refresh derfor se en halvskrevet
    fil og permanent reducere fx 384 aktier til de 147, der fandtes i kartoteket.

    Nu gælder:
    - læsning og skrivning er låst,
    - hovedfilen skrives atomisk,
    - seneste gyldige univers holdes i hukommelsen,
    - backup bruges ved reel filskade,
    - fallback til kartotek/portefølje bruges kun, når universfilen slet ikke findes.
    """
    global _stock_universe_last_good
    with _stock_universe_file_lock:
        if STOCK_UNIVERSE_FILE.exists():
            try:
                clean = _read_stock_universe_file(STOCK_UNIVERSE_FILE)
                _stock_universe_last_good = [dict(x) for x in clean]
                return clean
            except Exception:
                # En eksisterende men midlertidigt/varigt ulæselig hovedfil må
                # ALDRIG erstattes med et mindre fallback-univers.
                if _stock_universe_last_good:
                    return [dict(x) for x in _stock_universe_last_good]
                if STOCK_UNIVERSE_BACKUP_FILE.exists():
                    try:
                        clean = _read_stock_universe_file(STOCK_UNIVERSE_BACKUP_FILE)
                        _stock_universe_last_good = [dict(x) for x in clean]
                        return clean
                    except Exception:
                        pass
                raise RuntimeError(
                    "aktieunivers.json findes, men kunne ikke læses. "
                    "Filen er ikke overskrevet; kontrollér aktieunivers.json eller aktieunivers_backup.json."
                )

        # Kun første opstart uden en universfil må bygge et startunivers fra
        # kartoteket/porteføljen.
        items = []
        try:
            registry = load_stock_registry()
            for entry in registry.get("stocks", {}).values():
                if isinstance(entry, dict):
                    items.append(entry)
        except Exception:
            pass
        if not items:
            items = [x for x in portfolio if not is_cash_item(x)]
        clean = _universe_clean(items)
        save_stock_universe(clean)
        return clean


def save_stock_universe(items):
    """Gem universet trådsikkert og atomisk med seneste gyldige fil som backup."""
    global _stock_universe_last_good
    clean, payload = _stock_universe_payload(items)
    with _stock_universe_file_lock:
        # Backup opdateres kun fra en fil, der kan parses som et gyldigt univers.
        # Dermed kopieres en korrupt/halv fil aldrig over en god backup.
        if STOCK_UNIVERSE_FILE.exists():
            try:
                previous = _read_stock_universe_file(STOCK_UNIVERSE_FILE)
                _prev_clean, prev_payload = _stock_universe_payload(previous)
                _atomic_write_stock_universe(STOCK_UNIVERSE_BACKUP_FILE, prev_payload)
            except Exception:
                pass
        _atomic_write_stock_universe(STOCK_UNIVERSE_FILE, payload)
        _stock_universe_last_good = [dict(x) for x in clean]
    return clean


def import_stock_universe_json():
    path = filedialog.askopenfilename(title="Importer aktieunivers", filetypes=[("JSON-filer","*.json"),("Alle filer","*.*")])
    if not path:
        return
    try:
        obj = json.loads(Path(path).read_text(encoding="utf-8"))
        if isinstance(obj, dict) and isinstance(obj.get("stocks"), dict):
            items = list(obj["stocks"].values())
        elif isinstance(obj, dict):
            items = obj.get("stocks", obj.get("positions", []))
        else:
            items = obj
        imported = _universe_clean(items)
        existing = load_stock_universe()
        existing_by_key = {position_key(x): dict(x) for x in existing}
        added = 0
        for item in imported:
            key = position_key(item)
            if key not in existing_by_key:
                existing_by_key[key] = dict(item)
                added += 1
            else:
                new_name = str(item.get("name", "") or "").strip()
                old_name = str(existing_by_key[key].get("name", "") or "").strip()
                if new_name and (not old_name or old_name == existing_by_key[key].get("ticker")) and new_name != old_name:
                    existing_by_key[key]["name"] = new_name
        clean = save_stock_universe(list(existing_by_key.values()))
        refresh_universe_tree()
        if "universe_data_state_var" in globals():
            universe_data_state_var.set("Data skal opdateres efter ændring af aktieuniverset.")
        status_var.set(f"Aktieunivers: {len(imported)} læst | {added} nye tilføjet | {len(clean)} aktier i alt.")
    except Exception as exc:
        messagebox.showerror("Aktieunivers", f"Kunne ikke importere filen.\n\n{exc}")


def add_universe_stock():
    exchange = simpledialog.askstring("Aktieunivers", "Børs (fx NASDAQ, NYSE, XETR):", parent=root)
    if not exchange:
        return
    ticker = simpledialog.askstring("Aktieunivers", "Ticker:", parent=root)
    if not ticker:
        return
    name = simpledialog.askstring("Aktieunivers", "Navn (valgfrit):", parent=root) or ticker
    items = load_stock_universe(); items.append({"exchange":exchange,"ticker":ticker,"name":name})
    save_stock_universe(items); refresh_universe_tree()
    if "universe_data_state_var" in globals():
        universe_data_state_var.set("Data skal opdateres efter ændring af aktieuniverset.")


def remove_universe_stock():
    sel = universe_tree.selection()
    if not sel:
        return
    vals = universe_tree.item(sel[0], "values")
    key = f"{str(vals[1]).upper()}:{str(vals[2]).upper()}"
    save_stock_universe([x for x in load_stock_universe() if position_key(x) != key])
    refresh_universe_tree()
    if "universe_data_state_var" in globals():
        universe_data_state_var.set("Data skal opdateres efter ændring af aktieuniverset.")


def toggle_universe_locked():
    """Skift låsestatus for den/de markerede aktier i Fase 0."""
    sel = universe_tree.selection()
    if not sel:
        messagebox.showinfo("Låste aktier", "Markér mindst én aktie i Fase 0 først.")
        return
    keys = set()
    for iid in sel:
        vals = universe_tree.item(iid, "values")
        if len(vals) >= 3:
            keys.add(f"{str(vals[1]).upper()}:{str(vals[2]).upper()}")
    items = load_stock_universe()
    by_key = {position_key(x): x for x in items}
    # Ved blandet markering låses alle; ellers vendes status samlet.
    all_locked = bool(keys) and all(bool(by_key.get(k, {}).get("locked", False)) for k in keys)
    for k in keys:
        if k in by_key:
            by_key[k]["locked"] = not all_locked
    save_stock_universe(items)
    refresh_universe_tree()
    status_var.set(f"Fase 0: {len(keys)} aktie(r) {'frigivet' if all_locked else 'låst'}.")


def _universe_item_ready(item, cache=None):
    """True når aktien har alle lokale data, som Fase 1 kræver for at kunne optimere."""
    cache = cache or load_daily_cache()
    key = position_key(item)
    cached_raw = cache.get("phase1", {}).get(key, {})
    fundamental = normalize_phase2_cache(cache.get("phase2", {}).get(key, {}))
    return bool(
        cached_raw
        and not value_is_missing(cached_raw.get("price_raw"))
        and not value_is_missing(fundamental.get("target_base"))
        and not value_is_missing(fundamental.get("sector"))
        and not value_is_missing(fundamental.get("industry"))
        and not value_is_missing(fundamental.get("country"))
        and not value_is_missing(fundamental.get("market_cap"))
    )


def _universe_readiness(items=None):
    items = items if items is not None else load_stock_universe()
    cache = load_daily_cache()
    ready_keys = {position_key(x) for x in items if _universe_item_ready(x, cache)}
    missing_keys = [position_key(x) for x in items if position_key(x) not in ready_keys]
    return ready_keys, missing_keys, len(items)


universe_current_sort = "nr"
universe_descending = False

def sort_universe(column):
    """Sortér Fase 0 på valgt kolonne. Gentaget klik vender retningen."""
    global universe_current_sort, universe_descending
    if column == universe_current_sort:
        universe_descending = not universe_descending
    else:
        universe_current_sort = column
        universe_descending = False
    refresh_universe_tree()


def _update_universe_headers():
    """Vis aktiv sortering med pil i Fase 0."""
    if "universe_tree" not in globals():
        return
    titles = {
        "nr": "Nr",
        "exchange": "Børs",
        "ticker": "Ticker",
        "name": "Navn",
        "status": "Status",
        "locked": "Låst",
        "region": "Region",
        "sector": "Sektor",
        "industry": "Industri",
    }
    for col, title in titles.items():
        arrow = ""
        if col == universe_current_sort:
            arrow = " ▼" if universe_descending else " ▲"
        universe_tree.heading(col, text=title + arrow, command=lambda c=col: sort_universe(c))


def _phase0_classification_for_item(x, cache=None):
    """Hent Region, Sektor og Industri fra samme Fase 2-cache som Status/Klar bruger."""
    cache = cache or load_daily_cache()
    key = position_key(x)
    fundamental = normalize_phase2_cache(cache.get("phase2", {}).get(key, {}))

    country = fundamental.get("country")
    sector = fundamental.get("sector")
    industry = fundamental.get("industry")

    # Brug præcis samme land -> region-logik som resten af programmet/byggemotoren.
    region = ""
    if not value_is_missing(country):
        try:
            region = mapped_region(country)
        except Exception:
            region = ""

    # Fallback: Land/Region-data kan i nogle versioner allerede være gemt direkte.
    if not region:
        region = (
            fundamental.get("region")
            or fundamental.get("land_region")
            or fundamental.get("country_region")
            or country
            or ""
        )

    return (
        "" if value_is_missing(region) else str(region),
        "" if value_is_missing(sector) else str(sector),
        "" if value_is_missing(industry) else str(industry),
    )

def refresh_universe_tree():
    if "universe_tree" not in globals():
        return
    universe_tree.delete(*universe_tree.get_children())
    items = load_stock_universe()
    cache = load_daily_cache()
    ready_keys, missing_keys, total = _universe_readiness(items)

    rows_to_show = []
    for original_nr, x in enumerate(items, 1):
        key = position_key(x)
        ready = key in ready_keys
        region, sector, industry = _phase0_classification_for_item(x, cache)
        rows_to_show.append({
            "nr": original_nr,
            "exchange": str(x.get("exchange", "") or ""),
            "ticker": str(x.get("ticker", "") or ""),
            "name": str(x.get("name", "") or ""),
            "status": "Klar" if ready else "Mangler data",
            "locked": "Ja" if bool(x.get("locked", False)) else "Nej",
            "is_locked": bool(x.get("locked", False)),
            "region": region,
            "sector": sector,
            "industry": industry,
            "ready": ready,
        })

    def sort_key(row):
        col = universe_current_sort
        if col == "nr":
            return int(row["nr"])
        return str(row.get(col, "") or "").casefold()

    rows_to_show.sort(key=sort_key, reverse=universe_descending)

    for row in rows_to_show:
        if row["ready"]:
            row_tag = "universe_ready_locked" if row.get("is_locked") else "universe_ready"
        else:
            row_tag = "universe_missing_locked" if row.get("is_locked") else "universe_missing"
        universe_tree.insert(
            "", "end",
            values=(row["nr"], row["exchange"], row["ticker"], row["name"], row["status"], row["locked"], row["region"], row["sector"], row["industry"]),
            tags=(row_tag,),
        )

    _update_universe_headers()

    if "universe_count_var" in globals():
        universe_count_var.set(f"{len(ready_keys)}/{total} aktier klar til porteføljebygning")
    if "universe_data_state_var" in globals():
        if total and len(ready_keys) == total:
            universe_data_state_var.set(f"Alle {total} aktier er korrekt indlæst og klar til Fase 1.")
        elif total:
            universe_data_state_var.set(f"{len(ready_keys)}/{total} aktier er klar. {len(missing_keys)} mangler nødvendige data.")
        else:
            universe_data_state_var.set("Aktieuniverset er tomt.")


def _row_key(row):
    return f"{str(row.get('exchange','')).upper()}:{str(row.get('ticker','')).upper()}"


def _builder_full_scanner_batch(items, batch_size=100):
    """Hent alle scannerfelter, som byggemotoren behøver, i få batch-opslag."""
    result_by_key = {}
    clean_items = [item for item in items if item.get("exchange") and item.get("ticker")]
    mapping = {
        "sector": ("sector",), "industry": ("industry",), "country": ("country",),
        "kurs_f2": ("close",), "market_cap": ("market_cap_basic",),
        "target_high": ("price_target_high",), "target_base": ("price_target_1y",),
        "target_median": ("price_target_median",), "target_low": ("price_target_low",),
        "earnings_next_date": ("earnings_release_next_date",),
        "dividend_yield": ("dividends_yield_current",), "analyst_count": ("number_of_analysts",),
        "revenue_growth_3y": ("total_revenue_3y_growth", "revenue_3y_growth", "total_revenue_cagr_3y", "revenue_cagr_3y", "total_revenue_yoy_growth_ttm", "revenue_yoy_growth_ttm"),
        "ebit_margin_ttm": ("ebit_margin_ttm", "operating_margin_ttm"),
        "roic": ("return_on_invested_capital", "return_on_invested_capital_ttm", "return_on_invested_capital_fq"),
        "fcf_margin_ttm": ("free_cash_flow_margin_ttm", "free_cash_flow_margin"),
        "fcf_growth_3y": ("free_cash_flow_3y_growth", "free_cash_flow_growth_3y", "free_cash_flow_cagr_3y", "free_cash_flow_yoy_growth_ttm"),
        "pe": ("price_earnings_ttm",), "peg": ("price_earnings_growth_ttm",),
        "total_assets": ("total_assets_fq", "total_assets"),
        "total_liabilities": ("total_liabilities_fq", "total_liabilities"),
        "goodwill": ("goodwill_fq", "goodwill"),
        "total_equity": ("total_equity_fq", "total_equity", "total_stockholders_equity_fq", "stockholders_equity_fq"),
        "shares_outstanding": ("total_common_shares_outstanding", "common_shares_outstanding", "total_shares_outstanding", "total_shares_outstanding_fq", "common_stock_shares_outstanding_fq"),
    }
    for start in range(0, len(clean_items), batch_size):
        chunk = clean_items[start:start + batch_size]
        tickers = [f"{str(x['exchange']).upper()}:{str(x['ticker']).upper()}" for x in chunk]
        payload = {"symbols": {"tickers": tickers, "query": {"types": []}}, "columns": TV_FUNDAMENTAL_COLUMNS, "ignore_unknown_fields": True}
        response = None
        for market in ("global", "america"):
            try:
                candidate = _tv_post_json(f"https://scanner.tradingview.com/{market}/scan", payload)
                if candidate.get("data"):
                    response = candidate
                    break
            except Exception:
                continue
        if not response:
            continue
        for result in response.get("data", []):
            symbol = str(result.get("s", "")).upper().strip()
            values = result.get("d") or []
            if not symbol:
                continue
            out = {}
            name = _extract_by_column(TV_FUNDAMENTAL_COLUMNS, values, "description", "name")
            if name:
                out["name"] = str(name).strip()
            for field, cols in mapping.items():
                value = _extract_by_column(TV_FUNDAMENTAL_COLUMNS, values, *cols)
                if value not in (None, ""):
                    out[field] = str(value).strip() if field in ("sector", "industry", "country") else _as_tv_number(value)
            result_by_key[symbol] = out
    return result_by_key


def _builder_set_status(text):
    """Trådsikker statusopdatering."""
    try:
        root.after(0, lambda t=str(text): status_var.set(t))
    except Exception:
        pass


def _builder_update_universe_data_worker(force_refresh=False):
    """Opdatér byggedata for aktieuniverset. Normal = kun manglende; forceret = alle."""
    universe = load_stock_universe()
    if not universe:
        raise RuntimeError("Aktieuniverset er tomt.")
    if TvDatafeed is None:
        raise RuntimeError("Python-modulet tvDatafeed er ikke installeret.")

    cache = load_daily_cache()
    cache.setdefault("fx_rates", {})
    cache.setdefault("phase1", {})
    cache.setdefault("phase2", {})
    tv = TvDatafeed()

    # VIX følger samme cacheprincip som resten af Porteføljebyggeren:
    # normal opdatering henter kun hvis dagens VIX mangler; forceret henter altid på ny.
    try:
        _builder_set_status("Aktieunivers: " + ("henter VIX forceret..." if force_refresh else "kontrollerer dagens VIX..."))
        ensure_vix_for_today(force_refresh=force_refresh, tv=tv)
        # Bevar den netop gemte VIX i workerens lokale cacheobjekt, så senere
        # save_daily_cache(cache) ikke kan overskrive VIX med en ældre kopi.
        cache["vix"] = dict(load_daily_cache().get("vix", {}))
        try:
            root.after(0, update_vix_display)
        except Exception:
            pass
    except Exception:
        # En VIX-fejl må ikke blokere opdateringen af selve aktieuniverset.
        pass

    if force_refresh:
        work_items = list(universe)
    else:
        work_items = [x for x in universe if not _universe_item_ready(x, cache)]
        if not work_items:
            return len(universe), [], len(universe)

    needed = {currency_for_exchange(x.get("exchange")) for x in universe}
    needed.add("USD")
    _builder_set_status("Aktieunivers: henter valutakurser...")
    fx_rates, _fallback = fetch_fx_rates(tv, needed)
    cache["fx_rates"] = fx_rates
    save_daily_cache(cache)

    _builder_set_status(f"Aktieunivers: henter fundamentale data for {len(work_items)} aktier...")
    fundamentals = _builder_full_scanner_batch(work_items)

    total = len(universe)
    for idx, item in enumerate(work_items, 1):
        key = position_key(item)
        _builder_set_status(f"Aktieunivers: henter kursdata {idx}/{len(work_items)} – {key}")
        raw = fetch_one(tv, {**item, "antal": 1}, fx_rates)
        if raw is not None:
            cache["phase1"][key] = dict(raw)

        fundamental = dict(fundamentals.get(key, {}))
        # Batch kan returnere et delvist sæt. Prøv derfor aktien individuelt,
        # hvis et af byggemotorens nødvendige felter mangler.
        required_builder_fields = ("target_base", "sector", "country", "market_cap")
        if not fundamental or any(value_is_missing(fundamental.get(f)) for f in required_builder_fields):
            try:
                individual = fetch_fundamental_row_from_tradingview_scanner(item)
                fundamental.update(normalize_phase2_cache(individual))
            except Exception:
                pass

        if fundamental.get("name"):
            item["name"] = str(fundamental.get("name"))
        merged_fundamental = normalize_phase2_cache(cache.get("phase2", {}).get(key, {}))
        merged_fundamental.update(normalize_phase2_cache(fundamental))
        cache["phase2"][key] = merged_fundamental

        # v0.25: Historikken tilhører aktien – ikke aktieuniversfilen eller en konkret
        # portefølje. Registrér derfor alle komplette kursmål fra hele universet,
        # allerede når Fase 0-data hentes. 2 %-støjfilteret i den eksisterende
        # historikmotor afgør fortsat, om observationen er en reel ændring.
        try:
            observed_price = parse_float((raw or {}).get("price_raw"), None)
            currency = currency_for_exchange(item.get("exchange"))
            absolute_targets = _normalize_scenario_targets(
                merged_fundamental,
                currency=currency,
                fx_to_dkk=fx_rates.get(currency, FALLBACK_FX_DKK.get(currency, 1.0)),
                usd_to_dkk=fx_rates.get("USD", FALLBACK_FX_DKK["USD"]),
            )
            history_stub = {"exchange": item.get("exchange"), "ticker": item.get("ticker"), "name": item.get("name")}
            target_age_days_for_row(history_stub, absolute_targets, observed_price)
            register_earnings_date_for_row(history_stub, merged_fundamental.get("earnings_next_date"))
        except Exception:
            pass

        # Gem efter hver aktie: normal opdatering kan dermed genoptages præcis
        # ved de aktier, der stadig mangler, hvis et opslag fejler eller afbrydes.
        save_daily_cache(cache)
        if idx % 2 == 0:
            try:
                root.after(0, refresh_universe_tree)
            except Exception:
                pass

    save_stock_universe(universe)
    save_daily_cache(cache)
    ready_keys, missing_keys, total = _universe_readiness(universe)
    return len(ready_keys), missing_keys, total


def update_stock_universe_data(force_refresh=False):
    """Fase 0: normal opdatering henter kun manglende data; forceret henter hele universet igen."""
    for name in ("universe_update_button", "universe_force_update_button"):
        try:
            globals()[name].config(state="disabled")
        except Exception:
            pass
    if "universe_data_state_var" in globals():
        universe_data_state_var.set("Opdatering i gang...")
    status_var.set("Aktieunivers: starter " + ("forceret " if force_refresh else "") + "dataopdatering...")

    def worker():
        try:
            updated, failed, total = _builder_update_universe_data_worker(force_refresh=force_refresh)
            def finish():
                for name in ("universe_update_button", "universe_force_update_button"):
                    try:
                        globals()[name].config(state="normal")
                    except Exception:
                        pass
                refresh_universe_tree()
                if failed:
                    text = f"{updated}/{total} aktier klar. {len(failed)} mangler nødvendige data."
                    universe_data_state_var.set(text)
                    status_var.set("Aktieunivers: " + text)
                    messagebox.showwarning(
                        "Aktieunivers",
                        text + "\n\nDe manglende aktier er markeret rødt i Fase 0:\n" + "\n".join(failed[:30])
                    )
                else:
                    text = f"Alle {total} aktier er korrekt indlæst og klar til porteføljebygning."
                    universe_data_state_var.set(text)
                    status_var.set("Aktieunivers: " + text)
            root.after(0, finish)
        except Exception as exc:
            msg = str(exc)
            def fail():
                for name in ("universe_update_button", "universe_force_update_button"):
                    try:
                        globals()[name].config(state="normal")
                    except Exception:
                        pass
                refresh_universe_tree()
                universe_data_state_var.set("Dataopdatering mislykkedes.")
                status_var.set("Aktieunivers: dataopdatering mislykkedes.")
                messagebox.showerror("Aktieunivers", f"Dataopdateringen mislykkedes.\n\n{msg}")
            root.after(0, fail)

    threading.Thread(target=worker, daemon=True).start()


def force_update_stock_universe_data():
    update_stock_universe_data(force_refresh=True)

def _builder_cached_analysis_rows():
    """Lav analyse-rækker KUN fra dagens cache. Der foretages ingen netopslag."""
    universe = load_stock_universe()
    cache = load_daily_cache()
    fx_rates = dict(cache.get("fx_rates", {}))
    analysis_rows = []
    missing = []
    total = len(universe)
    for idx, item in enumerate(universe, 1):
        key = position_key(item)
        cached_raw = cache.get("phase1", {}).get(key, {})
        raw = cache_raw_from_item({**item, "antal": 1}, cached_raw, fx_rates) if cached_raw else None
        fundamental = normalize_phase2_cache(cache.get("phase2", {}).get(key, {}))
        # Disse felter er nødvendige for vores seks optimeringsdimensioner.
        required_ok = (
            raw is not None
            and not value_is_missing(fundamental.get("target_base"))
            and not value_is_missing(fundamental.get("sector"))
            and not value_is_missing(fundamental.get("industry"))
            and not value_is_missing(fundamental.get("country"))
            and not value_is_missing(fundamental.get("market_cap"))
        )
        if not required_ok:
            missing.append(key)
            continue
        display = make_display_row(raw, max(float(raw.get("value_raw", 0.0) or 0.0), 1.0))
        display["rank"] = str(idx)
        display["sort_rank"] = idx
        row = make_phase2_row(display, raw, fundamental, "")
        analysis_rows.append(row)
    return analysis_rows, missing, total


def _builder_candidate_rows():
    rows_local, missing, total = _builder_cached_analysis_rows()
    candidates = []
    for row in rows_local:
        if row.get("is_summary") or is_cash_row(row):
            continue
        price = parse_float(row.get("sort_price"), None)
        currency = str(row.get("currency", "DKK") or "DKK")
        fx = FALLBACK_FX_DKK.get(currency, 1.0)
        try:
            raw_value = float(row.get("sort_value_dkk", 0) or 0)
            shares = float(row.get("sort_antal", 0) or 0)
            if price and shares > 0:
                fx = raw_value / (shares * price)
        except Exception:
            pass
        unit_dkk = price * fx if price and price > 0 else None
        base_1y = parse_float(row.get("analyst_base_pct"), None)
        stock_score = parse_float(row.get("sort_stock_score"), None)
        dividend_yield = max(0.0, parse_float(row.get("sort_dividend_yield"), 0.0) or 0.0)
        layer = str(row.get("structure_layer") or "Potentiale")
        layer = structure_layer_from_display(layer)
        # Premium web builder deliberately does not use price-target history.
        trend_pct, trend_score, trend_known = 0.0, 50.0, False
        candidates.append({
            "row": row,
            "key": _row_key(row),
            "exchange": row.get("exchange"), "ticker": row.get("ticker"), "name": row.get("name"),
            "unit_dkk": unit_dkk,
            "base_1y": base_1y,
            "stock_score": stock_score,
            "target_trend_pct": trend_pct,
            "target_trend_score": trend_score,
            "target_trend_known": trend_known,
            "dividend_yield": dividend_yield,
            "locked": False,
            "sector": mapped_sector(row.get("sector")),
            "industry": normalized_industry(row.get("industry")),
            "region": mapped_region(row.get("country")),
            "layer": layer,
        })
    candidates = [c for c in candidates if c["unit_dkk"] and c["unit_dkk"] > 0 and c["base_1y"] is not None and c["stock_score"] is not None]
    locked_keys = {position_key(x) for x in load_stock_universe() if bool(x.get("locked", False))}
    for c in candidates:
        c["locked"] = c["key"] in locked_keys
    return candidates, missing, total


def _builder_normalize_targets(targets, categories):
    vals = {cat: max(0.0, float(targets.get(cat, 0.0) or 0.0)) for cat in categories}
    total = sum(vals.values())
    if total <= 0:
        return {cat: 0.0 for cat in categories}
    return {cat: value / total * 100.0 for cat, value in vals.items()}


def _builder_distribution_match(selected, field, targets, categories):
    """0-100 match via total variation distance. 100 = perfekt fordeling."""
    if not selected:
        return 0.0
    target = _builder_normalize_targets(targets, categories)
    n = float(len(selected))
    actual = {cat: 0.0 for cat in categories}
    for c in selected:
        value = c.get(field)
        if value in actual:
            actual[value] += 100.0 / n
    deviation = 0.5 * sum(abs(actual.get(cat, 0.0) - target.get(cat, 0.0)) for cat in categories)
    return clamp(100.0 - deviation, 0.0, 100.0)


def _builder_industry_preference_match(selected, settings, position_values=None):
    """0-100 industripræference. 50 er neutral, +100/-100 giver fuldt udslag.

    Ved aktievalg vægtes aktierne ens. Ved kapitaloptimering vægtes præferencen
    efter DKK-positionen, så industribjælkerne påvirker både valg og kapital.
    """
    if not selected:
        return 50.0
    prefs = settings.get("industry_preferences", {}) or {}
    if position_values is None:
        weights = [1.0 / len(selected)] * len(selected)
    else:
        vals = [max(0.0, float(v)) for v in position_values]
        total = sum(vals)
        weights = ([v / total for v in vals] if total > 0 else [1.0 / len(selected)] * len(selected))
    avg_pref = 0.0
    for c, w in zip(selected, weights):
        ind = normalized_industry(c.get("industry"))
        avg_pref += clamp(normalize_number(prefs.get(ind, 0.0), 0.0), -100.0, 100.0) * w
    return clamp(50.0 + 0.5 * avg_pref, 0.0, 100.0)


def _builder_industry_diversity_match(selected):
    """0-100 industridiversifikation ud fra koncentration (HHI).

    100 opnås, når alle valgte aktier ligger i forskellige industrier.
    0 opnås, når alle ligger i samme industri. Dermed kan fx flere meget
    forskellige industrivirksomheder inden for den brede sektor Industri
    tælle som reel diversifikation uden at kræve en stor måltabel.
    """
    if not selected:
        return 0.0
    n = len(selected)
    if n <= 1:
        return 100.0
    counts = {}
    for c in selected:
        ind = normalized_industry(c.get("industry"))
        counts[ind] = counts.get(ind, 0) + 1
    hhi = sum((count / n) ** 2 for count in counts.values())
    min_hhi = 1.0 / n
    if min_hhi >= 1.0:
        return 100.0
    return clamp((1.0 - hhi) / (1.0 - min_hhi) * 100.0, 0.0, 100.0)


def _builder_industry_diversity_match_weighted(selected, position_values):
    """DKK-vægtet industridiversifikation til kapitaloptimeringen."""
    if not selected or not position_values:
        return 0.0
    values = [max(0.0, float(v)) for v in position_values]
    total = sum(values)
    if total <= 0:
        return 0.0
    by_industry = {}
    for c, value in zip(selected, values):
        ind = normalized_industry(c.get("industry"))
        by_industry[ind] = by_industry.get(ind, 0.0) + value / total
    hhi = sum(weight ** 2 for weight in by_industry.values())
    # Den teoretisk laveste HHI for n positioner er 1/n. Det gør skalaen
    # sammenlignelig med den uvægtede score og giver 100 ved lige store
    # positioner i hver sin industri.
    n = len(selected)
    min_hhi = 1.0 / n if n > 0 else 1.0
    if min_hhi >= 1.0:
        return 100.0
    return clamp((1.0 - hhi) / (1.0 - min_hhi) * 100.0, 0.0, 100.0)


def _builder_base_score(base_pct):
    """Eksisterende S-kurve gør Base 1Y sammenlignelig med 0-100 Aktiescore."""
    return nonlinear_potential_curve(base_pct if base_pct is not None else 0.0)


def _builder_dividend_score(yield_pct, settings):
    """0-100 målopfyldelse. Målet belønnes frem til 100; overskydende yield giver ikke ekstra score."""
    if not settings.get("use_dividend_target", False):
        return 100.0
    target = max(0.0, float(settings.get("dividend_target_pct", 0.0) or 0.0))
    if target <= 0:
        return 100.0
    return clamp(float(yield_pct or 0.0) / target * 100.0, 0.0, 100.0)


def _builder_portfolio_metrics(selected, settings):
    if not selected:
        return {"score": 0.0, "base_score": 0.0, "base_1y": 0.0, "stock_score": 0.0, "structure": 0.0, "sector": 0.0, "industry": 0.0, "region": 0.0}
    base_scores = [_builder_base_score(c.get("base_1y")) for c in selected]
    base_raw = [float(c.get("base_1y", 0.0) or 0.0) for c in selected]
    stocks = [float(c.get("stock_score", 0.0) or 0.0) for c in selected]
    structure_match = _builder_distribution_match(selected, "layer", settings["structure_targets"], STRUCTURE_LAYER_ORDER)
    sector_match = _builder_distribution_match(selected, "sector", settings["sector_targets"], SECTOR_CATEGORIES)
    industry_match = _builder_industry_preference_match(selected, settings)
    region_match = _builder_distribution_match(selected, "region", settings["region_targets"], REGION_CATEGORIES)
    target_trend = sum(float(c.get("target_trend_score", 50.0) or 50.0) for c in selected) / len(selected)
    target_trend_pct = sum(float(c.get("target_trend_pct", 0.0) or 0.0) for c in selected) / len(selected)
    dividend_yield = sum(float(c.get("dividend_yield", 0.0) or 0.0) for c in selected) / len(selected)
    dividend_match = _builder_dividend_score(dividend_yield, settings)
    components = {
        "base_1y": sum(base_scores) / len(base_scores),
        "stock_score": sum(stocks) / len(stocks),
        "structure": structure_match,
        "sector": sector_match,
        "industry": industry_match,
        "region": region_match,
        "target_trend": target_trend,
        "dividend": dividend_match,
    }
    weights = settings.get("objective_weights", {})
    def effective_weight(k):
        if k == "dividend" and not settings.get("use_dividend_target", False):
            return 0.0
        if k == "target_trend" and not settings.get("use_target_trend", False):
            return 0.0
        return max(0.0, float(weights.get(k, 0.0) or 0.0))
    weight_sum = sum(effective_weight(k) for k in components)
    if weight_sum <= 0:
        weight_sum = 1.0
    score = sum(components[k] * effective_weight(k) for k in components) / weight_sum
    return {
        "score": score,
        "base_score": components["base_1y"],
        "base_1y": sum(base_raw) / len(base_raw),
        "stock_score": components["stock_score"],
        "structure": structure_match,
        "sector": sector_match,
        "industry": industry_match,
        "region": region_match,
        "target_trend": target_trend,
        "target_trend_pct": target_trend_pct,
        "dividend": dividend_match,
        "dividend_yield": dividend_yield,
    }


def _builder_min_sector_rule_ok(selected, settings):
    minimum = int(settings.get("minimum_stocks_per_sector", 0) or 0)
    if minimum <= 0:
        return True
    targets = settings.get("sector_targets", {})
    for sector, target in targets.items():
        if float(target or 0.0) <= 0:
            continue
        available = sum(1 for c in _builder_current_candidates_context if c.get("sector") == sector)
        required = min(minimum, available)
        if required <= 0:
            continue
        actual = sum(1 for c in selected if c.get("sector") == sector)
        if actual < required:
            return False
    return True


_builder_current_candidates_context = []


def _builder_initial_selection(candidates, settings, max_positions):
    """Stabil start: minimum pr. sektor først, derefter Base 1Y + Aktiescore."""
    selected = []
    keys = set()
    weights = settings.get("objective_weights", {})
    base_w = max(0.0, float(weights.get("base_1y", 0.0) or 0.0))
    stock_w = max(0.0, float(weights.get("stock_score", 0.0) or 0.0))
    industry_w = max(0.0, float(weights.get("industry", 0.0) or 0.0))
    target_trend_w = max(0.0, float(weights.get("target_trend", 0.0) or 0.0)) if settings.get("use_target_trend", False) else 0.0
    prefs = settings.get("industry_preferences", {}) or {}
    denom = base_w + stock_w + industry_w + target_trend_w or 1.0
    for c in candidates:
        ind_pref = clamp(normalize_number(prefs.get(normalized_industry(c.get("industry")), 0.0), 0.0), -100.0, 100.0)
        ind_score = 50.0 + 0.5 * ind_pref
        c["individual_start_score"] = (
            _builder_base_score(c.get("base_1y")) * base_w
            + float(c.get("stock_score", 0.0) or 0.0) * stock_w
            + ind_score * industry_w
            + float(c.get("target_trend_score", 50.0) or 50.0) * target_trend_w
        ) / denom
    ranked = sorted(candidates, key=lambda c: (c["individual_start_score"], c.get("base_1y", -999999)), reverse=True)

    def add(c):
        if c["key"] not in keys and len(selected) < max_positions:
            selected.append(c); keys.add(c["key"])

    # Låste aktier får første plads i startporteføljen og kan ikke senere byttes ud.
    if settings.get("use_locked_stocks", True):
        for c in ranked:
            if c.get("locked"):
                add(c)

    minimum = int(settings.get("minimum_stocks_per_sector", 0) or 0)
    if minimum > 0:
        for sector, target in sorted(settings["sector_targets"].items(), key=lambda x: x[1], reverse=True):
            if target <= 0:
                continue
            pool = [c for c in ranked if c["sector"] == sector]
            for c in pool[:min(minimum, len(pool))]:
                add(c)

    for c in ranked:
        add(c)
        if len(selected) >= max_positions:
            break
    return selected


def _builder_iterative_swap_optimize(selected, candidates, settings):
    """Bubble-sort-inspireret lokal søgning: behold kun forbedrende 1-for-1-byt."""
    selected = list(selected)
    total_swaps = 0
    pass_no = 0
    current = _builder_portfolio_metrics(selected, settings)
    while True:
        pass_no += 1
        swaps_this_pass = 0
        tests = 0
        selected_keys = {c["key"] for c in selected}
        outside = [c for c in candidates if c["key"] not in selected_keys]
        possible = max(1, len(selected) * len(outside))
        _builder_report_progress(f"Aktieoptimering – iteration {pass_no}: starter {possible} mulige byt | score {current['score']:.2f}", force=True)

        # En fuld gennemgang svarer til bubble-sort-pass. Når et byt accepteres,
        # fortsætter vi systematisk; ny komplet pass starter bagefter.
        for i in range(len(selected)):
            old = selected[i]
            if settings.get("use_locked_stocks", True) and old.get("locked"):
                continue
            # Outside beregnes igen, fordi tidligere accepterede byt ændrer medlemskabet.
            selected_keys = {c["key"] for c in selected}
            outside_now = [c for c in candidates if c["key"] not in selected_keys]
            for incoming in outside_now:
                tests += 1
                trial = list(selected)
                trial[i] = incoming
                if not _builder_min_sector_rule_ok(trial, settings):
                    continue
                trial_metrics = _builder_portfolio_metrics(trial, settings)
                if trial_metrics["score"] > current["score"] + BUILDER_SCORE_EPSILON:
                    before = current["score"]
                    selected = trial
                    current = trial_metrics
                    swaps_this_pass += 1
                    total_swaps += 1
                    _builder_report_progress(
                        f"Aktieoptimering – iteration {pass_no}: forbedring {old['ticker']} → {incoming['ticker']} | "
                        f"{before:.2f} → {current['score']:.2f}", force=True
                    )
                    old = incoming
                elif tests % BUILDER_STATUS_EVERY_TESTS == 0:
                    _builder_report_progress(f"Aktieoptimering – iteration {pass_no}: tester byt {tests}/{possible} | score {current['score']:.2f}")

        _builder_report_progress(f"Aktieoptimering – iteration {pass_no} færdig: {swaps_this_pass} forbedrende byt | score {current['score']:.2f}", force=True)
        if swaps_this_pass == 0:
            break
    return selected, current, pass_no, total_swaps


def _builder_distribution_match_weighted(selected, position_values, field, targets, categories):
    """0-100 fordelingsmatch baseret på DKK-vægte i stedet for antal aktier."""
    if not selected:
        return 0.0
    total_value = sum(max(0.0, float(v)) for v in position_values)
    if total_value <= 0:
        return 0.0
    target = _builder_normalize_targets(targets, categories)
    actual = {cat: 0.0 for cat in categories}
    for c, value in zip(selected, position_values):
        category = c.get(field)
        if category in actual:
            actual[category] += max(0.0, float(value)) / total_value * 100.0
    deviation = 0.5 * sum(abs(actual.get(cat, 0.0) - target.get(cat, 0.0)) for cat in categories)
    return clamp(100.0 - deviation, 0.0, 100.0)


def _builder_portfolio_metrics_weighted(selected, position_values, settings):
    """Samme seks optimeringsmål som aktievalget, men vægtet efter DKK-positionerne."""
    if not selected or not position_values:
        return {"score":0.0,"base_score":0.0,"base_1y":0.0,"stock_score":0.0,"structure":0.0,"sector":0.0,"industry":0.0,"region":0.0}
    values = [max(0.0, float(v)) for v in position_values]
    total = sum(values)
    if total <= 0:
        return {"score":0.0,"base_score":0.0,"base_1y":0.0,"stock_score":0.0,"structure":0.0,"sector":0.0,"industry":0.0,"region":0.0}
    weights_dkk = [v / total for v in values]
    base_score = sum(_builder_base_score(c.get("base_1y")) * w for c,w in zip(selected,weights_dkk))
    base_raw = sum(float(c.get("base_1y",0.0) or 0.0) * w for c,w in zip(selected,weights_dkk))
    stock_score = sum(float(c.get("stock_score",0.0) or 0.0) * w for c,w in zip(selected,weights_dkk))
    structure_match = _builder_distribution_match_weighted(selected, values, "layer", settings["structure_targets"], STRUCTURE_LAYER_ORDER)
    sector_match = _builder_distribution_match_weighted(selected, values, "sector", settings["sector_targets"], SECTOR_CATEGORIES)
    industry_match = _builder_industry_preference_match(selected, settings, values)
    region_match = _builder_distribution_match_weighted(selected, values, "region", settings["region_targets"], REGION_CATEGORIES)
    target_trend = sum(float(c.get("target_trend_score",50.0) or 50.0) * w for c,w in zip(selected,weights_dkk))
    target_trend_pct = sum(float(c.get("target_trend_pct",0.0) or 0.0) * w for c,w in zip(selected,weights_dkk))
    dividend_yield = sum(float(c.get("dividend_yield",0.0) or 0.0) * w for c,w in zip(selected,weights_dkk))
    dividend_match = _builder_dividend_score(dividend_yield, settings)
    components={"base_1y":base_score,"stock_score":stock_score,"structure":structure_match,"sector":sector_match,"industry":industry_match,"region":region_match,"target_trend":target_trend,"dividend":dividend_match}
    objective=settings.get("objective_weights",{})
    def effective_weight(k):
        if k == "dividend" and not settings.get("use_dividend_target", False):
            return 0.0
        if k == "target_trend" and not settings.get("use_target_trend", False):
            return 0.0
        return max(0.0,float(objective.get(k,0.0) or 0.0))
    weight_sum=sum(effective_weight(k) for k in components) or 1.0
    score=sum(components[k]*effective_weight(k) for k in components)/weight_sum
    return {"score":score,"base_score":base_score,"base_1y":base_raw,"stock_score":stock_score,"structure":structure_match,"sector":sector_match,"industry":industry_match,"region":region_match,"target_trend":target_trend,"target_trend_pct":target_trend_pct,"dividend":dividend_match,"dividend_yield":dividend_yield}


def _builder_iterative_capital_optimize(selected, settings):
    """Bubble-sort-princip for kapital: flyt ét fast DKK-trin og behold kun forbedringer.

    Starten er ligelig alene som neutral starttilstand. Derefter er der intet krav om
    lige positioner. Minimum positionsstørrelse er den eneste nedre DKK-grænse.
    """
    target_value=float(settings["portfolio_value_dkk"])
    minimum=max(0.0,float(settings["minimum_position_dkk"]))
    n=len(selected)
    if n<=0:
        return [], _builder_portfolio_metrics_weighted([],[],settings), 0, 0, 0.0
    if minimum*n > target_value + 1e-9:
        raise ValueError("Minimumspositionerne kan ikke rummes inden for den samlede porteføljeværdi.")

    values=[target_value/n for _ in selected]
    # 0,10% af porteføljen, dog mindst 1.000 DKK. Det er fintmasket nok til
    # fordelingen, men stadig hurtigt selv ved mange fulde gennemgange.
    step=max(1000.0, target_value*0.001)
    current=_builder_portfolio_metrics_weighted(selected,values,settings)
    pass_no=0
    total_moves=0
    while True:
        pass_no += 1
        moves_this_pass=0
        tests=0
        possible=max(1,n*(n-1))
        _builder_report_progress(f"Kapitaloptimering – iteration {pass_no}: starter {possible} flytninger | score {current['score']:.2f}", force=True)
        for donor in range(n):
            for receiver in range(n):
                if donor == receiver:
                    continue
                tests += 1
                if values[donor] - step < minimum - 1e-9:
                    continue
                trial=list(values)
                trial[donor]-=step
                trial[receiver]+=step
                trial_metrics=_builder_portfolio_metrics_weighted(selected,trial,settings)
                if trial_metrics["score"] > current["score"] + BUILDER_SCORE_EPSILON:
                    before=current["score"]
                    values=trial
                    current=trial_metrics
                    moves_this_pass += 1
                    total_moves += 1
                    _builder_report_progress(
                        f"Kapitaloptimering – iteration {pass_no}: {format_dkk(step)} DKK {selected[donor]['ticker']} → {selected[receiver]['ticker']} | "
                        f"{before:.2f} → {current['score']:.2f}", force=True
                    )
                elif tests % BUILDER_STATUS_EVERY_TESTS == 0:
                    _builder_report_progress(f"Kapitaloptimering – iteration {pass_no}: tester {tests}/{possible} | score {current['score']:.2f}")
        _builder_report_progress(f"Kapitaloptimering – iteration {pass_no} færdig: {moves_this_pass} forbedringer | score {current['score']:.2f}", force=True)
        if moves_this_pass == 0:
            break
    return values,current,pass_no,total_moves,step


def _builder_values_to_whole_shares(selected, desired_values, settings):
    """Omsæt optimerede DKK-mål til hele aktier og brug restkapitalen intelligent."""
    import math
    target_value=float(settings["portfolio_value_dkk"])
    minimum=max(0.0,float(settings["minimum_position_dkk"]))
    built=[]
    invested=0.0
    for c,desired in zip(selected,desired_values):
        unit=float(c["unit_dkk"])
        min_shares=max(1,int(math.ceil(minimum/unit))) if minimum>0 else 1
        shares=max(min_shares,int(float(desired)//unit))
        value=shares*unit
        built.append({"exchange":c["exchange"],"ticker":c["ticker"],"name":c["name"],"antal":shares,"_unit":unit,"_desired":float(desired),"_candidate":c,"_min_shares":min_shares})
        invested += value

    # Hvis afrunding/minimum giver overskridelse, fjern aktier hvor det gør mindst
    # skade på afstanden til det optimerede DKK-mål.
    while invested > target_value + 1e-6:
        choices=[x for x in built if x["antal"] > x["_min_shares"]]
        if not choices:
            raise ValueError("The optimized minimum positions cannot fit within the selected portfolio value.")
        item=min(choices,key=lambda x: abs((x["antal"]-1)*x["_unit"]-x["_desired"]) - abs(x["antal"]*x["_unit"]-x["_desired"]))
        item["antal"]-=1
        invested-=item["_unit"]

    # Restkapital: tilføj én hel aktie dér hvor den bringer den faktiske
    # kapitalfordeling tættest på de optimerede DKK-mål.
    while True:
        affordable=[x for x in built if invested+x["_unit"] <= target_value+1e-9]
        if not affordable:
            break
        best=min(affordable,key=lambda x: abs((x["antal"]+1)*x["_unit"]-x["_desired"]) - abs(x["antal"]*x["_unit"]-x["_desired"]))
        # Stop hvis selv den bedste ekstra aktie bevæger positionen længere væk
        # fra det optimerede mål; så er restbeløbet reelle kontanter pga. hele aktier.
        before=abs(best["antal"]*best["_unit"]-best["_desired"])
        after=abs((best["antal"]+1)*best["_unit"]-best["_desired"])
        if after > before + 1e-9:
            break
        best["antal"]+=1
        invested+=best["_unit"]

    cash=max(0.0,target_value-invested)
    return built,invested,cash


def _apply_builder_allocation_scores_only(data_rows):
    """Udfyld Region/Sektor/Industriscore uden at ændre byggemotorens positionsstørrelser."""
    if not data_rows:
        return
    stock_weight_total = sum(parse_float(row.get("weight"), 0.0) or 0.0 for row in data_rows)
    region_actual = {category: 0.0 for category in REGION_CATEGORIES}
    sector_actual = {category: 0.0 for category in SECTOR_CATEGORIES}
    industry_actual = {}
    for row in data_rows:
        normalized_weight = ((parse_float(row.get("weight"), 0.0) or 0.0) / stock_weight_total * 100.0) if stock_weight_total > 0 else 0.0
        rg = row.get("region_group", "Andre lande")
        sg = row.get("sector_group", "Andre sektorer")
        ig = row.get("industry_group") or normalized_industry(row.get("industry"))
        region_actual[rg] = region_actual.get(rg, 0.0) + normalized_weight
        sector_actual[sg] = sector_actual.get(sg, 0.0) + normalized_weight
        industry_actual[ig] = industry_actual.get(ig, 0.0) + normalized_weight
    industry_targets_dynamic = dynamic_industry_targets(data_rows)
    for row in data_rows:
        rg = row.get("region_group", "Andre lande")
        sg = row.get("sector_group", "Andre sektorer")
        ig = row.get("industry_group") or normalized_industry(row.get("industry"))
        rs = allocation_balance_score(region_actual.get(rg, 0.0), region_targets.get(rg, 0.0))
        ss = allocation_balance_score(sector_actual.get(sg, 0.0), sector_targets.get(sg, 0.0))
        ins = industry_balance_score(industry_actual.get(ig, 0.0), industry_target_for(ig, industry_targets_dynamic), ig)
        row.update({
            "region_score": format_num(rs, 0), "sort_region_score": rs,
            "sector_score": format_num(ss, 0), "sort_sector_score": ss,
            "industry_score": format_num(ins, 0), "sort_industry_score": ins,
        })


def refresh_built_portfolio_from_cache():
    """Genopbyg Fase 1B/1C/2/3 fra Fase 0-cachen uden netværksopslag."""
    global rows, phase2_rows, phase2b_rows
    cache = load_daily_cache()
    fx_rates = dict(cache.get("fx_rates", {}))
    fx_rates.setdefault("DKK", 1.0)

    raw_rows = []
    missing_phase1 = []
    for item in portfolio:
        if is_cash_item(item):
            raw_rows.append(make_cash_raw(item))
            continue
        key = position_key(item)
        cached = cache.get("phase1", {}).get(key, {})
        raw = cache_raw_from_item(item, cached, fx_rates) if cached else None
        if raw is None:
            missing_phase1.append(key)
            continue
        raw_rows.append(raw)

    if missing_phase1:
        raise ValueError(
            "Den byggede portefølje mangler Fase 0-kursdata for: "
            + ", ".join(missing_phase1[:20])
            + (" ..." if len(missing_phase1) > 20 else "")
        )

    total_value = sum(float(x.get("value_raw", 0.0) or 0.0) for x in raw_rows)
    display_pairs = [(make_display_row(x, total_value), x) for x in raw_rows]
    display_pairs.sort(key=lambda pair: (1 if pair[0].get("is_cash") else 0, -pair[0].get("sort_weight", 0.0)))

    display_rows = []
    phase2_data_rows = []
    phase2b_data_rows = []
    cash_phase2_row = None
    stock_rank = 0

    for display_row, raw_row in display_pairs:
        if raw_row.get("is_cash"):
            display_row["rank"] = ""
            display_row["sort_rank"] = 999999999
            cash_phase2_row = make_cash_phase2_row(display_row)
            continue

        stock_rank += 1
        display_row["rank"] = str(stock_rank)
        display_row["sort_rank"] = stock_rank
        display_rows.append(display_row)

        key = position_key(raw_row)
        fundamental = normalize_phase2_cache(cache.get("phase2", {}).get(key, {}))
        phase2_data_rows.append(make_phase2_row(display_row, raw_row, fundamental, ""))
        phase2b_data_rows.append(make_phase2b_row(display_row, fundamental))

    summary = make_summary_row(display_rows)
    summary["value_dkk"] = format_dkk(total_value)
    summary["sort_value_dkk"] = total_value
    rows = [summary] + display_rows

    # Fase 2-scorerne skal afspejle den konkrete byggede porteføljes fordeling.
    _apply_builder_allocation_scores_only(phase2_data_rows)
    phase2_rows = [make_phase2_row(summary, None, {})] + phase2_data_rows
    update_phase2_summary(phase2_rows[0], phase2_data_rows)
    if cash_phase2_row is not None:
        phase2_rows.append(cash_phase2_row)
    apply_ai_catalyst_cache_to_phase2_rows()

    phase2b_rows = [make_phase2b_row(summary, {})] + phase2b_data_rows

    show()
    show_phase2()
    show_phase2b()
    show_phase3_structure()
    show_portfolio_structure()
    update_vix_display()

    return stock_rank, total_value


# ===== Porteføljebygger v0.43: Webordre, valuta og samlet JSON-kundeoutput =====
_current_web_order = None
_current_web_order_path = ""

WEB_SECTOR_MAP = {
    "Technology": "Teknologi", "Financials": "Finans", "Healthcare": "Sundhed",
    "Industrials": "Industri", "Consumer Cyclical": "Forbrug cyklisk",
    "Consumer Defensive": "Forbrug defensivt", "Energy": "Energi", "Materials": "Materialer",
    "Utilities": "Forsyning", "Transportation": "Transport", "Communication": "Kommunikation",
    "Other sectors": "Andre sektorer",
}
WEB_REGION_MAP = {
    "USA": "USA", "Canada": "Canada", "Denmark": "Danmark", "Other Nordics": "Øvrige Norden",
    "Europe": "Europa", "Japan": "Japan", "China / Hong Kong": "Kina / Hongkong",
    "Other Asia": "Øvrige Asien", "Emerging Markets": "Emerging Markets", "Other countries": "Andre lande",
}
WEB_STRUCTURE_MAP = {"Fundamental": "Fundament", "Growth": "Vækst", "Accelerator": "Accelerator", "Potential": "Potentiale"}
WEB_PRIORITY_ALIASES = {
    # Aktuelt APB-webformat bruger de læsbare engelske navne.
    # De gamle snake_case-navne beholdes som fallback, så tidligere testordrer stadig kan indlæses.
    "base_1y": ("Base 1Y", "base_1y"),
    "stock_score": ("Stock score", "stock_score", "Aktiescore"),
    "structure": ("Structure layer", "structure_layer", "Strukturlag", "structure"),
    "sector": ("Sectors", "sectors", "Sektorer", "sector"),
    "industry": ("Industry", "industry", "Industri"),
    "region": ("Regions", "regions", "Regioner", "region"),
    "target_trend": ("Price target trend", "price_target_trend", "Kursmålstrend", "target_trend"),
    "dividend": ("Dividend", "dividend", "Udbytte"),
}

def _builder_currency_rate_to_dkk(currency):
    currency = str(currency or "DKK").upper().strip()
    if currency == "DKK":
        return 1.0
    try:
        cache = load_daily_cache()
        rate = parse_float((cache.get("fx_rates", {}) or {}).get(currency), None)
        if rate and rate > 0:
            return float(rate)
    except Exception:
        pass
    return float(FALLBACK_FX_DKK.get(currency, 1.0) or 1.0)

def _portfolio_currency_from_dkk(value_dkk, currency):
    rate = _builder_currency_rate_to_dkk(currency)
    return float(value_dkk or 0.0) / rate if rate > 0 else float(value_dkk or 0.0)

def _safe_filename_part(value, fallback="order"):
    value = str(value or "").strip()
    if "@" in value:
        value = value.split("@", 1)[0]
    value = re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("._-")
    return value[:80] or fallback

def _web_order_reference(order, source_path=""):
    server = order.get("server", {}) if isinstance(order, dict) else {}
    number = str(server.get("order_number", "") or order.get("order_number", "") or "").strip()
    if number:
        return number
    stem = Path(source_path).stem if source_path else ""
    if stem.upper().startswith("APB-"):
        return stem
    email = str(order.get("email", "") or "")
    received = str(server.get("received_at", "") or "")[:10].replace("-", "")
    return f"{_safe_filename_part(email, 'APB')}_{received or date.today().strftime('%Y%m%d')}"

def _load_saved_web_order_context():
    global _current_web_order, _current_web_order_path
    try:
        if WEB_ORDER_CONTEXT_FILE.exists():
            obj = json.loads(WEB_ORDER_CONTEXT_FILE.read_text(encoding="utf-8"))
            if isinstance(obj, dict) and obj.get("type") == "apb_order":
                _current_web_order = obj
                _current_web_order_path = str(obj.get("_desktop_source_path", "") or "")
                return obj
    except Exception:
        pass
    return None

def _save_web_order_context(order, source_path=""):
    global _current_web_order, _current_web_order_path
    clean = dict(order or {})
    clean["_desktop_source_path"] = str(source_path or "")
    _current_web_order = clean
    _current_web_order_path = str(source_path or "")
    WEB_ORDER_CONTEXT_FILE.write_text(json.dumps(clean, ensure_ascii=False, indent=2), encoding="utf-8")

def _clear_web_order_context():
    global _current_web_order, _current_web_order_path
    _current_web_order = None
    _current_web_order_path = ""
    try:
        if WEB_ORDER_CONTEXT_FILE.exists():
            WEB_ORDER_CONTEXT_FILE.unlink()
    except Exception:
        pass
    if "builder_order_info_var" in globals():
        builder_order_info_var.set("Egen portefølje – ingen webordre indlæst.")
    if "customer_output_context_var" in globals():
        customer_output_context_var.set("Ingen webordre indlæst. JSON-resultat kræver en webordre med ID og adgangskode.")

def _web_order_submitted_text(order=None):
    order = order or _current_web_order
    if not isinstance(order, dict):
        return ""
    server = order.get("server", {}) or {}
    shown = str(server.get("submitted_at_display", "") or "").strip()
    if shown:
        return shown
    raw = str(server.get("received_at", "") or "").strip()
    if raw:
        try:
            dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
            return dt.strftime("%d-%m-%Y %H:%M")
        except Exception:
            return raw
    return ""

def _validate_current_web_order(order):
    """Valider de felter den aktuelle APB-webapp forventes at sende."""
    if not isinstance(order, dict) or order.get("type") != "apb_order":
        raise ValueError("Filen er ikke en Alpha Portfolio Builder webordre (type = apb_order).")
    required_sections = (
        "basic_rules", "priorities", "sectors", "industry_preferences",
        "regions", "structure_layers", "price_target_trend", "dividend", "server",
    )
    missing = [name for name in required_sections if not isinstance(order.get(name), dict)]
    if missing:
        raise ValueError("Webordren mangler følgende sektion(er): " + ", ".join(missing))
    basic = order.get("basic_rules", {})
    for field in ("currency", "portfolio_value", "minimum_position", "minimum_stocks_per_sector", "maximum_number_of_stocks"):
        if field not in basic:
            raise ValueError(f"Webordren mangler basic_rules.{field}")
    return True

def _web_order_info_text(order=None, source_path=""):
    order = order or _current_web_order
    if not isinstance(order, dict):
        return "Egen portefølje – ingen webordre indlæst."
    ref = _web_order_reference(order, source_path or _current_web_order_path)
    name = str(order.get("name", "") or "").strip()
    email = str(order.get("email", "") or "").strip()
    currency = str((order.get("basic_rules", {}) or {}).get("currency", "DKK") or "DKK")
    server = order.get("server", {}) or {}
    status = str(server.get("status_display", "") or server.get("status", "") or "").strip()
    submitted = _web_order_submitted_text(order)
    who = name or email or "kunde"
    parts = [f"Webordre: {ref}", who, currency]
    if name and email:
        parts.append(email)
    if submitted:
        parts.append(submitted)
    if status:
        parts.append(status)
    return " · ".join(parts)

def _priority_from_web(source, internal_key, default=0.0):
    for alias in WEB_PRIORITY_ALIASES.get(internal_key, (internal_key,)):
        if alias in source:
            return max(0.0, normalize_number(source.get(alias), default))
    return default

def _update_builder_currency_labels(*_args):
    currency = builder_currency_var.get() if "builder_currency_var" in globals() else "DKK"
    if "builder_portfolio_value_label_var" in globals():
        builder_portfolio_value_label_var.set(f"Samlet porteføljeværdi {currency}")
    if "builder_min_position_label_var" in globals():
        builder_min_position_label_var.set(f"Minimum positionsstørrelse {currency}")

def _apply_web_order_to_builder_ui(order, source_path=""):
    _validate_current_web_order(order)
    basic = order.get("basic_rules", {}) or {}
    currency = str(basic.get("currency", "DKK") or "DKK").upper().strip()
    if currency not in SUPPORTED_PORTFOLIO_CURRENCIES:
        raise ValueError(f"Valutaen {currency} understøttes ikke. Brug DKK, EUR eller USD.")
    builder_currency_var.set(currency)
    builder_portfolio_value_var.set(format_num(normalize_number(basic.get("portfolio_value"), 0.0), 0))
    builder_min_position_var.set(format_num(normalize_number(basic.get("minimum_position"), 0.0), 0))
    builder_min_sector_count_var.set(str(max(0, int(normalize_number(basic.get("minimum_stocks_per_sector"), 0)))))
    builder_max_stocks_var.set(str(max(1, int(normalize_number(basic.get("maximum_number_of_stocks"), 1)))))
    builder_use_locked_var.set(False)
    priorities = order.get("priorities", {}) or {}
    for key, var in builder_objective_vars.items():
        var.set(_priority_from_web(priorities, key, var.get()))
    for web_name, value in (order.get("sectors", {}) or {}).items():
        target = WEB_SECTOR_MAP.get(str(web_name), str(web_name))
        if target in builder_sector_vars:
            builder_sector_vars[target].set(format_num(normalize_number(value, 0.0), 1))
    for web_name, value in (order.get("regions", {}) or {}).items():
        target = WEB_REGION_MAP.get(str(web_name), str(web_name))
        if target in builder_region_vars:
            builder_region_vars[target].set(format_num(normalize_number(value, 0.0), 1))
    for web_name, value in (order.get("structure_layers", {}) or {}).items():
        target = WEB_STRUCTURE_MAP.get(str(web_name), str(web_name))
        if target in builder_structure_vars:
            builder_structure_vars[target].set(format_num(normalize_number(value, 0.0), 1))
    missing_industries = []
    for name, value in (order.get("industry_preferences", {}) or {}).items():
        if name in builder_industry_preference_vars:
            builder_industry_preference_vars[name].set(clamp(normalize_number(value, 0.0), -100.0, 100.0))
        elif abs(normalize_number(value, 0.0)) > 1e-9:
            missing_industries.append(name)
    target_trend = order.get("price_target_trend", {}) or {}
    builder_use_target_trend_var.set(bool(target_trend.get("enabled", True)))
    dividend = order.get("dividend", {}) or {}
    builder_use_dividend_var.set(bool(dividend.get("enabled", False)))
    builder_dividend_target_var.set(format_num(normalize_number(dividend.get("portfolio_target_pct"), 2.0), 1))
    _save_web_order_context(order, source_path)
    _update_builder_currency_labels()
    if "builder_order_info_var" in globals():
        builder_order_info_var.set(_web_order_info_text(order, source_path))
    if "customer_output_context_var" in globals():
        customer_output_context_var.set(_web_order_info_text(order, source_path))
    settings = collect_builder_settings_from_ui()
    settings["web_order_reference"] = _web_order_reference(order, source_path)
    settings["web_order_email"] = str(order.get("email", "") or "")
    settings["web_order_name"] = str(order.get("name", "") or "")
    settings["web_order_submitted"] = _web_order_submitted_text(order)
    settings["web_order_status"] = str((order.get("server", {}) or {}).get("status_display", "") or (order.get("server", {}) or {}).get("status", "") or "")
    save_builder_settings(settings)
    return missing_industries

def import_web_order_json():
    path = filedialog.askopenfilename(title="Importer Alpha Portfolio Builder webordre", filetypes=[("APB webordre JSON", "*.json"), ("Alle filer", "*.*")])
    if not path:
        return
    try:
        order = json.loads(Path(path).read_text(encoding="utf-8"))
        missing = _apply_web_order_to_builder_ui(order, path)
        ref = _web_order_reference(order, path)
        submitted = _web_order_submitted_text(order)
        customer = str(order.get("name", "") or "").strip()
        email = str(order.get("email", "") or "").strip()
        msg = f"Webordre {ref} er indlæst i Fase 1. Alle kendte webfelter er overført."
        if customer:
            msg += f"\nKunde: {customer}"
        if email:
            msg += f"\nEmail: {email}"
        if submitted:
            msg += f"\nIndsendt: {submitted}"
        if missing:
            msg += "\n\nIkke-neutrale industrier uden match i Fase 1:\n" + "\n".join(missing[:15])
        messagebox.showinfo("Webordre indlæst", msg)
        status_var.set(_web_order_info_text(order, path))
    except Exception as exc:
        messagebox.showerror("Importer webordre", f"Webordren kunne ikke indlæses.\n\n{exc}")

def _customer_output_identity():
    """Fast filidentitet for det samlede SIMGROVA-resultat."""
    order = _current_web_order if isinstance(_current_web_order, dict) else {}
    ref = _web_order_reference(order, _current_web_order_path) if order else "Egen_portefolje"
    base = _safe_filename_part(ref, "APB_result")
    return base, order, ref


def _json_safe_number(value, digits=None):
    v = parse_float(value, None)
    if v is None:
        return None
    v = float(v)
    if digits is None:
        return v
    return round(v, int(digits))


def _customer_phase2_rows_json():
    """Kundeegnede Fase 2-data. Kun direkte/afledte portefølje- og markedsdata – ingen interne scorer."""
    currency = (_current_web_order or {}).get("basic_rules", {}).get("currency") if isinstance(_current_web_order, dict) else None
    if not currency:
        currency = builder_currency_var.get() if "builder_currency_var" in globals() else "DKK"
    currency = str(currency or "DKK").upper()

    result = []
    for row in phase2_rows:
        if row.get("is_summary") or is_cash_row(row):
            continue
        value_currency = _portfolio_currency_from_dkk(row.get("sort_value_dkk", 0.0), currency)
        result.append({
            "exchange": str(row.get("exchange", "") or ""),
            "ticker": str(row.get("ticker", "") or ""),
            "name": str(row.get("name", "") or ""),
            "trading_currency": str(row.get("currency", "") or ""),
            "current_price": _json_safe_number(row.get("sort_price", row.get("price")), 6),
            "shares": _json_safe_number(row.get("sort_antal", row.get("antal")), 6),
            "position_value": round(float(value_currency or 0.0), 2),
            "portfolio_weight_pct": _json_safe_number(row.get("weight"), 4),
            "change_1d_pct": _json_safe_number(row.get("pct_1d"), 4),
            "sector": str(row.get("sector", "") or ""),
            "industry": str(row.get("industry", "") or ""),
            "country_region": str(row.get("country", "") or ""),
            "structure_layer": str(row.get("structure_layer", "") or ""),
            "bear_target": _json_safe_number(row.get("bear_target_abs"), 6),
            "base_target": _json_safe_number(row.get("base_target_abs"), 6),
            "bull_target": _json_safe_number(row.get("bull_target_abs"), 6),
            "bear_1y_pct": _json_safe_number(row.get("analyst_bear_pct"), 4),
            "base_1y_pct": _json_safe_number(row.get("analyst_base_pct"), 4),
            "bull_1y_pct": _json_safe_number(row.get("analyst_bull_pct"), 4),
            "days_to_earnings": _json_safe_number(row.get("days_to_earnings"), 0),
            "dividend_yield_pct": _json_safe_number(row.get("dividend_yield"), 4),
            "pe": _json_safe_number(row.get("pe"), 4),
            "peg": _json_safe_number(row.get("peg"), 4),
            "revenue_growth_3y_pct": _json_safe_number(row.get("revenue_growth_3y"), 4),
            "ebit_margin_ttm_pct": _json_safe_number(row.get("ebit_margin_ttm"), 4),
            "roic_pct": _json_safe_number(row.get("roic"), 4),
            "fcf_margin_pct": _json_safe_number(row.get("fcf_margin_ttm"), 4),
            "fcf_growth_3y_pct": _json_safe_number(row.get("fcf_growth_3y"), 4),
            "sma50": _json_safe_number(row.get("sma50"), 6),
        })
    return result, currency


def _phase3_distribution_for_customer_json(kind):
    """Samme kundeegnede fordelinger som Fase 3-visningen, uden scorefelter."""
    rows = [r for r in phase2_rows if not r.get("is_summary") and not is_cash_row(r)]
    stock_total = sum(parse_float(r.get("weight"), 0.0) or 0.0 for r in rows)
    settings = load_builder_settings()

    def w(r):
        return (parse_float(r.get("weight"), 0.0) or 0.0) / stock_total * 100.0 if stock_total else 0.0

    groups = {}
    for r in rows:
        if kind == "Sectors":
            cat = r.get("sector_group") or mapped_sector(r.get("sector"))
        elif kind == "Industries":
            cat = r.get("industry_group") or normalized_industry(r.get("industry"))
        elif kind == "Regions":
            cat = r.get("region_group") or mapped_region(r.get("country"))
        elif kind == "Structure layers":
            cat = r.get("structure_layer") or "Potentiale"
        elif kind == "PE distribution":
            cat = pe_bucket_label(r.get("pe"))
        else:
            cat = fc1y_bucket_label(r.get("analyst_1y_upside_pct"))
        g = groups.setdefault(str(cat), [0.0, 0, 0.0])
        ww = w(r)
        g[0] += ww
        g[1] += 1
        g[2] += ww * (parse_float(r.get("analyst_base_pct"), 0.0) or 0.0)

    sector_targets_json = settings.get("sector_targets", {}) or {}
    region_targets_json = settings.get("region_targets", {}) or {}
    structure_targets_json = settings.get("structure_targets", {}) or {}
    industry_targets_json = dynamic_industry_targets(rows) if kind == "Industries" else {}

    if kind == "Sectors":
        ordered = list(SECTOR_CATEGORIES) + [x for x in groups if x not in SECTOR_CATEGORIES]
    elif kind == "Regions":
        ordered = list(REGION_CATEGORIES) + [x for x in groups if x not in REGION_CATEGORIES]
    elif kind == "Structure layers":
        ordered = list(STRUCTURE_LAYER_ORDER)
    elif kind == "PE distribution":
        ordered = [label for label, _low, _high in PE_BUCKETS]
    elif kind == "Analyst distribution":
        ordered = [label for label, _low, _high in FC1Y_BUCKETS]
        if "FC1Y ukendt" in groups:
            ordered.append("FC1Y ukendt")
    else:
        ordered = sorted(groups, key=lambda x: groups[x][0], reverse=True)

    result = []
    for cat in ordered:
        weight, count, weighted = groups.get(cat, [0.0, 0, 0.0])
        target = None
        if kind == "Sectors":
            target = parse_float(sector_targets_json.get(cat), 0.0)
        elif kind == "Regions":
            target = parse_float(region_targets_json.get(cat), 0.0)
        elif kind == "Structure layers":
            target = parse_float(structure_targets_json.get(cat), 0.0)
        elif kind == "Industries":
            target = parse_float(industry_targets_json.get(cat), 0.0)
        elif kind == "PE distribution":
            target = PE_TARGET_WEIGHTS.get(cat)
        elif kind == "Analyst distribution":
            target = FC1Y_TARGET_WEIGHTS.get(cat)
        result.append({
            "category": str(cat),
            "portfolio_weight_pct": round(float(weight), 4),
            "positions": int(count),
            "average_base_1y_pct": None if not weight else round(float(weighted / weight), 4),
            "recommended_pct": None if target is None else round(float(target), 4),
            "deviation_pp": None if target is None else round(float(weight - target), 4),
        })

    if kind == "Industries":
        represented_sectors = {
            r.get("sector_group") or mapped_sector(r.get("sector"))
            for r in rows
            if (r.get("industry_group") or normalized_industry(r.get("industry"))) != "Industri ukendt"
        }
        missing_target = sum(
            max(0.0, parse_float(sector_targets_json.get(sector, 0.0), 0.0) or 0.0)
            for sector in SECTOR_CATEGORIES
            if sector not in represented_sectors
        )
        if missing_target > 0.000001:
            result.append({
                "category": "Andre industrier",
                "portfolio_weight_pct": 0.0,
                "positions": 0,
                "average_base_1y_pct": None,
                "recommended_pct": round(float(missing_target), 4),
                "deviation_pp": round(float(-missing_target), 4),
            })

    if kind not in ("Structure layers", "PE distribution", "Analyst distribution"):
        special = [r for r in result if r["category"] == "Andre industrier"]
        normal = [r for r in result if r["category"] != "Andre industrier"]
        normal.sort(key=lambda x: x["portfolio_weight_pct"], reverse=True)
        result = normal + special
    return result


def _customer_target_history_json():
    try:
        series = _phase3_target_history_series()
    except Exception:
        return []
    result = []
    for row in series:
        d = row.get("date")
        ds = d.isoformat() if hasattr(d, "isoformat") else str(d or "")
        result.append({
            "date": ds,
            "bear_pct": _json_safe_number(row.get("bear_pct"), 4),
            "base_pct": _json_safe_number(row.get("base_pct"), 4),
            "bull_pct": _json_safe_number(row.get("bull_pct"), 4),
            "portfolio_pct": _json_safe_number(row.get("portfolio_pct"), 4),
            "bear_dkk": _json_safe_number(row.get("bear_abs"), 4),
            "base_dkk": _json_safe_number(row.get("base_abs"), 4),
            "bull_dkk": _json_safe_number(row.get("bull_abs"), 4),
            "portfolio_dkk": _json_safe_number(row.get("price_abs"), 4),
        })
    return result


def _built_portfolio_customer_json(currency):
    positions = []
    cash_amount = 0.0
    for item in (portfolio or []):
        if is_cash_item(item):
            cash_amount = float(parse_float(item.get("antal"), 0.0) or 0.0)
            continue
        positions.append({
            "exchange": str(item.get("exchange", "") or ""),
            "ticker": str(item.get("ticker", "") or ""),
            "name": str(item.get("name", "") or ""),
            "shares": _json_safe_number(item.get("antal"), 6),
        })
    cash_in_currency = _portfolio_currency_from_dkk(cash_amount, currency)
    return positions, {
        "currency": currency,
        "amount": round(float(cash_in_currency or 0.0), 2),
        "amount_dkk": round(float(cash_amount or 0.0), 2),
    }


def build_customer_result_json():
    if not phase2_rows:
        raise ValueError("Fase 2 indeholder ingen portefølje. Byg porteføljen først.")
    order = _current_web_order if isinstance(_current_web_order, dict) else {}
    if not order:
        raise ValueError("Indlæs først den webordre, som resultatet skal knyttes til.")
    _validate_current_web_order(order)

    result_access = order.get("result_access", {}) if isinstance(order.get("result_access"), dict) else {}
    user_id = str(result_access.get("user_id", "") or "").strip()
    access_code = str(result_access.get("access_code", "") or "").strip()
    if not user_id or not access_code:
        raise ValueError("Webordren mangler result_access.user_id eller result_access.access_code.")

    server = order.get("server", {}) if isinstance(order.get("server"), dict) else {}
    order_number = str(server.get("order_number", "") or order.get("order_number", "") or "").strip()
    if not order_number:
        order_number = _web_order_reference(order, _current_web_order_path)

    phase2_data, currency = _customer_phase2_rows_json()
    built_positions, cash = _built_portfolio_customer_json(currency)

    # Original input bevares uændret bortset fra desktopens private hjælpefelt.
    original_input = {k: v for k, v in order.items() if k != "_desktop_source_path"}

    return {
        "type": "apb_result",
        "schema_version": "0.43",
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "user_id": user_id,
        "access_code": access_code,
        "order_number": order_number,
        "customer": {
            "name": str(order.get("name", "") or ""),
            "skool_username": str(order.get("skool_username", "") or ""),
            "email": str(order.get("email", "") or ""),
        },
        "original_input": original_input,
        "portfolio": {
            "currency": currency,
            "positions": built_positions,
            "cash": cash,
            "position_count": len(built_positions),
        },
        "phase2": {
            "description": "Customer-facing portfolio and market/fundamental data. Internal Alpha scores are excluded.",
            "positions": phase2_data,
        },
        "phase3": {
            "sectors": _phase3_distribution_for_customer_json("Sectors"),
            "industries": _phase3_distribution_for_customer_json("Industries"),
            "regions": _phase3_distribution_for_customer_json("Regions"),
            "structure_layers": _phase3_distribution_for_customer_json("Structure layers"),
            "pe_distribution": _phase3_distribution_for_customer_json("PE distribution"),
            "analyst_base_distribution": _phase3_distribution_for_customer_json("Analyst distribution"),
            "price_target_history": _customer_target_history_json(),
        },
    }


def generate_customer_result_json(path=None):
    base, _order, _ref = _customer_output_identity()
    if path is None:
        CUSTOMER_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        path = CUSTOMER_OUTPUT_DIR / f"{base}_Result.json"
    payload = build_customer_result_json()
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return Path(path)


def generate_customer_output_json():
    try:
        path = generate_customer_result_json()
        if "customer_output_status_var" in globals():
            customer_output_status_var.set(f"Genereret: {path.name}")
        messagebox.showinfo(
            "Kundeoutput",
            f"Samlet JSON-resultat er genereret til SIMGROVA:\n{path}\n\n"
            "Filen indeholder webordrens ID/kode, ordredata, byggede portefølje, kontanter samt kundeegnede Fase 2- og Fase 3-data."
        )
    except Exception as exc:
        messagebox.showerror("Kundeoutput", f"JSON-output kunne ikke genereres.\n\n{exc}")


# Desktop web-order context load disabled in web edition.

def build_portfolio_from_rules():
    """Start Porteføljebyggeren responsivt og vis løbende status under hele arbejdet."""
    global _builder_build_in_progress, _builder_build_started_at

    if _builder_build_in_progress:
        status_var.set("Byg portefølje: en optimering kører allerede.")
        return

    # Tkinter-variabler må kun læses i GUI-tråden. Alt tungt arbejde sker bagefter
    # i worker-tråden på denne frosne kopi af indstillingerne.
    try:
        settings = collect_builder_settings_from_ui()
        save_builder_settings(settings)
    except Exception as exc:
        messagebox.showerror("Byg portefølje", f"Indstillingerne kunne ikke læses.\n\n{exc}")
        return

    _builder_build_in_progress = True
    _builder_build_started_at = time.monotonic()
    _builder_set_build_button_state("disabled")
    _builder_report_progress("Forbereder aktieunivers og kontrollerer byggedata", force=True)
    status_var.set("Forbereder aktieunivers og kontrollerer byggedata...")
    root.after(1000, _builder_build_heartbeat)

    def finish_error(message, warning=False):
        global _builder_build_in_progress
        _builder_build_in_progress = False
        _builder_set_build_button_state("normal")
        status_var.set("Byg portefølje: afbrudt.")
        if warning:
            messagebox.showwarning("Byg portefølje", message)
        else:
            messagebox.showerror("Byg portefølje", f"Porteføljen kunne ikke bygges.\n\n{message}")

    def finish_success(payload):
        global portfolio, _builder_build_in_progress, _builder_current_candidates_context
        global sector_targets, region_targets
        try:
            # Fase 3 skal vise præcis de anbefalede fordelinger, som netop blev
            # brugt til at bygge porteføljen.
            sector_targets = dict(settings.get("sector_targets", DEFAULT_SECTOR_TARGETS))
            region_targets = dict(settings.get("region_targets", DEFAULT_REGION_TARGETS))
            _builder_report_progress("Gemmer den byggede portefølje og opdaterer visninger", force=True)
            status_var.set("Gemmer den byggede portefølje og opdaterer Fase 2...")

            result = payload["result"]
            portfolio = ensure_cash_position(result)
            _builder_current_candidates_context = payload["candidates"]

            BUILT_PORTFOLIO_FILE.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
            save_phase2_portfolio_snapshot(portfolio)
            save_portfolio(portfolio)

            summary = payload["summary"]
            if "builder_result_var" in globals():
                builder_result_var.set(summary)

            refresh_built_portfolio_from_cache()
            notebook.select(phase2_frame)  # Fase 2 vises direkte fra samme Fase 0-cache

            status_var.set(
                f"Optimering færdig – {len(result)-1} aktier | {summary} | "
                f"investeret {format_dkk(payload['invested'])} DKK | visninger opdateret fra Fase 0-cache"
            )
        except Exception as exc:
            messagebox.showerror(
                "Byg portefølje",
                "Porteføljen blev beregnet, men afsluttende lagring/visning fejlede.\n\n" + str(exc),
            )
            status_var.set("Byg portefølje: beregning færdig, men afsluttende opdatering fejlede.")
        finally:
            _builder_build_in_progress = False
            _builder_set_build_button_state("normal")

    def worker():
        global _builder_current_candidates_context
        try:
            _builder_report_progress("Forbereder aktieunivers og kontrollerer byggedata", force=True)
            candidates, missing, universe_total = _builder_candidate_rows()
            if missing or len(candidates) < universe_total:
                unavailable = max(len(missing), universe_total - len(candidates))
                msg = (
                    f"Aktieuniversets byggedata er ikke komplette.\n\n"
                    f"Univers: {universe_total} aktier\nBrugbare kandidater: {len(candidates)}\nManglende/ubrugbare: {unavailable}\n\n"
                    "Gå til Fase 0 og tryk 'OPDATER KURSDATA / MANGLENDE DATA' først."
                )
                root.after(0, lambda m=msg: finish_error(m, warning=True))
                return
            if not candidates:
                root.after(0, lambda: finish_error("Der findes ingen brugbare kandidater i aktieuniverset.", warning=True))
                return

            target_value = settings["portfolio_value_dkk"]
            minimum_value = settings["minimum_position_dkk"]
            max_by_capital = max(1, int(target_value // minimum_value)) if minimum_value > 0 else len(candidates)
            max_positions = min(int(settings["maximum_stocks"]), len(candidates), max_by_capital)
            locked_candidates = [c for c in candidates if c.get("locked")] if settings.get("use_locked_stocks", True) else []
            if len(locked_candidates) > max_positions:
                raise ValueError(
                    f"Der er {len(locked_candidates)} låste aktier, men porteføljen kan højst rumme {max_positions}. "
                    "Frigiv aktier eller øg maksimum."
                )
            if max_positions < 1:
                raise ValueError("Indstillingerne giver plads til 0 aktier.")

            # Samme kontekst som før v0.31: minimumsreglen bruger hele kandidatlisten
            # under hvert 1-for-1-byt. Den sættes før optimeringen starter.
            _builder_current_candidates_context = candidates

            min_per_sector = int(settings.get("minimum_stocks_per_sector", 0) or 0)
            if min_per_sector > 0:
                hard_minimum_total = 0
                for sector, target in settings["sector_targets"].items():
                    if float(target or 0.0) <= 0:
                        continue
                    available = sum(1 for c in candidates if c.get("sector") == sector)
                    hard_minimum_total += min(min_per_sector, available)
                if hard_minimum_total > max_positions:
                    raise ValueError(
                        f"Minimumsreglen kræver mindst {hard_minimum_total} aktier på tværs af sektorerne, "
                        f"men Maks. antal aktier er {max_positions}. Hæv maksimum eller sænk minimum pr. sektor."
                    )

            _builder_report_progress(
                f"Bygger startportefølje – {len(candidates)} kandidater, maks. {max_positions} aktier",
                force=True,
            )
            selected = _builder_initial_selection(candidates, settings, max_positions)
            if len(selected) < max_positions:
                max_positions = len(selected)

            initial_metrics = _builder_portfolio_metrics(selected, settings)
            _builder_report_progress(
                f"Startportefølje klar – {len(selected)} aktier | score {initial_metrics['score']:.2f}. Starter aktieoptimering",
                force=True,
            )

            selected, selection_metrics, passes, total_swaps = _builder_iterative_swap_optimize(selected, candidates, settings)

            _builder_report_progress(
                f"Aktievalg færdigt – score {selection_metrics['score']:.2f}. Starter kapitaloptimering",
                force=True,
            )
            desired_values, final_metrics, capital_passes, capital_moves, capital_step = _builder_iterative_capital_optimize(selected, settings)

            _builder_report_progress("Afrunder til hele aktier og beregner endelig porteføljescore", force=True)
            built, invested, cash = _builder_values_to_whole_shares(selected, desired_values, settings)

            actual_values = [float(x["antal"]) * float(x["_unit"]) for x in built]
            final_metrics = _builder_portfolio_metrics_weighted(selected, actual_values, settings)

            result = [{k: v for k, v in x.items() if not k.startswith("_")} for x in built]
            result.append({"exchange": CASH_EXCHANGE, "ticker": CASH_TICKER, "name": CASH_NAME, "antal": cash})

            summary = (
                f"Score {final_metrics['score']:.2f} | Base 1Y {final_metrics['base_1y']:.1f}% | "
                f"Aktiescore {final_metrics['stock_score']:.1f} | Udbytte {final_metrics.get('dividend_yield',0.0):.2f}% "
                f"(mål {settings.get('dividend_target_pct',0.0):.2f}%) | Struktur {final_metrics['structure']:.1f} | "
                f"Sektor {final_metrics['sector']:.1f} | Industri {final_metrics['industry']:.1f} | Region {final_metrics['region']:.1f} | "
                f"Kursmålstrend {final_metrics.get('target_trend_pct',0.0):+.1f}% | "
                f"Aktievalg {passes} iterationer / {total_swaps} byt | "
                f"Kapital {capital_passes} iterationer / {capital_moves} flytninger"
            )

            _builder_report_progress("Optimering færdig – klargør resultat og visninger", force=True)
            payload = {
                "result": result,
                "invested": invested,
                "summary": summary,
                "candidates": candidates,
            }
            root.after(0, lambda p=payload: finish_success(p))
        except Exception as exc:
            msg = str(exc)
            root.after(0, lambda m=msg: finish_error(m, warning=False))

    threading.Thread(target=worker, daemon=True, name="PortefoljebyggerWorker").start()

def collect_builder_settings_from_ui():
    base = load_builder_settings()
    currency = str(builder_currency_var.get() if "builder_currency_var" in globals() else base.get("currency", "DKK")).upper().strip()
    if currency not in SUPPORTED_PORTFOLIO_CURRENCIES:
        currency = "DKK"
    rate = _builder_currency_rate_to_dkk(currency)
    input_value = max(1.0, normalize_number(builder_portfolio_value_var.get(), base.get("portfolio_value_input", base["portfolio_value_dkk"])))
    input_min = max(0.0, normalize_number(builder_min_position_var.get(), base.get("minimum_position_input", base["minimum_position_dkk"])))
    base["currency"] = currency
    base["portfolio_value_input"] = input_value
    base["minimum_position_input"] = input_min
    base["portfolio_value_dkk"] = input_value * rate
    base["minimum_position_dkk"] = input_min * rate
    base["minimum_stocks_per_sector"] = max(0, int(normalize_number(builder_min_sector_count_var.get(), base["minimum_stocks_per_sector"])))
    base["maximum_stocks"] = max(1, int(normalize_number(builder_max_stocks_var.get(), base["maximum_stocks"])))
    base["use_locked_stocks"] = bool(builder_use_locked_var.get())
    base["use_target_trend"] = bool(builder_use_target_trend_var.get())
    base["use_dividend_target"] = bool(builder_use_dividend_var.get())
    base["dividend_target_pct"] = max(0.0, normalize_number(builder_dividend_target_var.get(), base.get("dividend_target_pct", 2.0)))
    for key, var in builder_objective_vars.items():
        base["objective_weights"][key] = max(0.0, normalize_number(var.get(), base["objective_weights"].get(key, 0.0)))
    for cat,var in builder_region_vars.items():
        base["region_targets"][cat] = max(0.0, normalize_number(var.get(),0.0))
    for cat,var in builder_sector_vars.items():
        base["sector_targets"][cat] = max(0.0, normalize_number(var.get(),0.0))
    for cat,var in builder_structure_vars.items():
        base["structure_targets"][cat] = max(0.0, normalize_number(var.get(),0.0))
    base["industry_preferences"] = {
        cat: clamp(normalize_number(var.get(), 0.0), -100.0, 100.0)
        for cat, var in builder_industry_preference_vars.items()
    }
    return base


# ===== Porteføljebygger v0.25: historikgrafer og Fase 0-data =====
def _draw_phase3_target_chart(canvas, series, value_keys, title, y_label, percent=False, overlay_key=None, overlay_label=None):
    """Tegn en kompakt, responsiv tidsseriegraf direkte i Tkinter Canvas."""
    canvas.delete("all")
    width = max(760, canvas.winfo_width())
    height = max(280, canvas.winfo_height())
    left, right, top, bottom = 76, 28, 44, 58
    plot_w = max(100, width - left - right)
    plot_h = max(100, height - top - bottom)

    canvas.create_text(width / 2, 18, text=title, font=("Segoe UI", 12, "bold"), fill="#202020")
    if not series:
        canvas.create_text(width / 2, height / 2, text="Ingen komplette kursmålshistorikdata for den aktive portefølje.", font=("Segoe UI", 11), fill="#555555")
        return

    values = []
    for key in value_keys:
        values.extend(float(row[key]) for row in series if row.get(key) is not None)
    if overlay_key:
        values.extend(float(row[overlay_key]) for row in series if row.get(overlay_key) is not None)
    if not values:
        return
    ymin, ymax = min(values), max(values)
    if ymin == ymax:
        pad = max(1.0, abs(ymin) * 0.1)
    else:
        pad = (ymax - ymin) * 0.10
    ymin -= pad
    ymax += pad
    if percent and ymin > 0:
        ymin = min(0.0, ymin)

    # X-aksen er kategorisk: hver registreret dato får præcis samme afstand
    # til næste datapunkt. Kalenderafstand (fx 1 dag vs. 20 dage) påvirker
    # dermed ikke grafens bredde eller den visuelle afstand mellem punkterne.
    point_count = len(series)
    index_by_date = {row["date"]: index for index, row in enumerate(series)}

    def x_for(d):
        index = index_by_date.get(d, 0)
        if point_count <= 1:
            return left + 14.5
        # Fast kategorisk afstand: ca. 1/3 af v7.38's 88 px.
        return left + index * 29.0

    def y_for(v):
        return top + (ymax - float(v)) / max(1e-12, ymax - ymin) * plot_h

    # Vandrette gitterlinjer og Y-akse.
    for i in range(6):
        frac = i / 5.0
        y = top + frac * plot_h
        val = ymax - frac * (ymax - ymin)
        canvas.create_line(left, y, width - right, y, fill="#e5e5e5")
        if percent:
            label = f"{val:.1f}%"
        else:
            label = f"{val:,.0f}".replace(",", ".")
        canvas.create_text(left - 8, y, text=label, anchor="e", font=("Segoe UI", 9), fill="#444444")

    canvas.create_line(left, top, left, height - bottom, fill="#777777")
    canvas.create_line(left, height - bottom, width - right, height - bottom, fill="#777777")

    # Hver registreret dato vises som sit eget, jævnt placerede datapunkt.
    # Den vandrette scrollbar gør, at alle datoer kan vises uden at blive
    # presset sammen eller få kalenderafstand til at styre bredden.
    for idx, row in enumerate(series):
        x = x_for(row["date"])
        canvas.create_line(x, height - bottom, x, height - bottom + 5, fill="#777777")
        canvas.create_text(x, height - bottom + 18, text=row["date"].strftime("%d-%m-%Y"), angle=30, anchor="n", font=("Segoe UI", 8), fill="#444444")

    # Fast Bear/Base/Bull-farvekode.
    colors = ["#c94c4c", "#2f6db0", "#3f8f4f"]
    labels = ["Bear", "Base", "Bull"]
    for key, color, label in zip(value_keys, colors, labels):
        coords = []
        for row in series:
            value = row.get(key)
            if value is None:
                continue
            coords.extend([x_for(row["date"]), y_for(value)])
        if len(coords) >= 4:
            canvas.create_line(*coords, fill=color, width=2.4, smooth=False)
        elif len(coords) == 2:
            x, y = coords
            canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill=color, outline=color)
        for row in series:
            value = row.get(key)
            if value is not None:
                x, y = x_for(row["date"]), y_for(value)
                canvas.create_oval(x - 2.5, y - 2.5, x + 2.5, y + 2.5, fill=color, outline=color)

    # Diskret porteføljekurve i procentgrafen. Den skal være en visuel
    # reference og derfor svagere end Bear/Base/Bull.
    if overlay_key:
        overlay_color = "#8a8a8a"
        overlay_coords = []
        for row in series:
            value = row.get(overlay_key)
            if value is None:
                continue
            overlay_coords.extend([x_for(row["date"]), y_for(value)])
        if len(overlay_coords) >= 4:
            canvas.create_line(*overlay_coords, fill=overlay_color, width=1.4, dash=(5, 4), smooth=False)
        elif len(overlay_coords) == 2:
            x, y = overlay_coords
            canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill=overlay_color, outline=overlay_color)
        for row in series:
            value = row.get(overlay_key)
            if value is not None:
                x, y = x_for(row["date"]), y_for(value)
                canvas.create_oval(x - 1.7, y - 1.7, x + 1.7, y + 1.7, fill=overlay_color, outline=overlay_color)

    # Legend og aksetitler.
    legend_items = list(zip(colors, labels))
    if overlay_key and overlay_label:
        legend_items.append(("#8a8a8a", overlay_label))
    legend_x = width - right - (300 if len(legend_items) > 3 else 210)
    legend_step = 72 if len(legend_items) <= 3 else 92
    for i, (color, label) in enumerate(legend_items):
        x = legend_x + i * legend_step
        if overlay_key and overlay_label and label == overlay_label:
            canvas.create_line(x, 31, x + 22, 31, fill=color, width=1.4, dash=(5, 4))
        else:
            canvas.create_line(x, 31, x + 22, 31, fill=color, width=3)
        canvas.create_text(x + 27, 31, text=label, anchor="w", font=("Segoe UI", 9), fill="#333333")
    canvas.create_text(18, top + plot_h / 2, text=y_label, angle=90, font=("Segoe UI", 9, "bold"), fill="#333333")
    canvas.create_text(left + plot_w / 2, height - 10, text="Dato", font=("Segoe UI", 9, "bold"), fill="#333333")

    # v7.44 – Hover-tooltip. Når musen er tæt på et datapunkt på en af
    # kurverne, vises én samlet boks for datoen med alle relevante værdier.
    # Boksen tegnes som Canvas-elementer og fjernes straks igen, når musen
    # forlader datapunktet/grafen. Dermed forbliver grafen ren i normal brug.
    hover_points = []
    for row in series:
        x = x_for(row["date"])
        point_values = []
        for key, label in zip(value_keys, labels):
            value = row.get(key)
            if value is not None:
                point_values.append((key, label, float(value), x, y_for(value)))
                hover_points.append((x, y_for(value), row))
        if overlay_key:
            value = row.get(overlay_key)
            if value is not None:
                hover_points.append((x, y_for(value), row))

    def clear_tooltip(event=None):
        canvas.delete("chart_tooltip")

    def show_tooltip(event):
        # Kræv reel nærhed til et synligt datapunkt – ikke blot samme dato/X.
        nearest = None
        nearest_dist2 = 10.0 ** 2
        for px, py, row in hover_points:
            dist2 = (event.x - px) ** 2 + (event.y - py) ** 2
            if dist2 <= nearest_dist2:
                nearest_dist2 = dist2
                nearest = row
        if nearest is None:
            clear_tooltip()
            return

        lines = [nearest["date"].strftime("%d-%m-%Y")]
        for key, label in zip(value_keys, labels):
            value = nearest.get(key)
            if value is None:
                continue
            if percent:
                value_text = f"{float(value):+.1f} %".replace(".", ",")
            else:
                value_text = format_num(value, 2)
            lines.append(f"{label}: {value_text}")
        if overlay_key and overlay_label:
            value = nearest.get(overlay_key)
            if value is not None:
                if percent:
                    value_text = f"{float(value):+.1f} %".replace(".", ",")
                else:
                    value_text = format_num(value, 2)
                lines.append(f"{overlay_label}: {value_text}")

        clear_tooltip()
        tooltip_text = "\n".join(lines)
        # Placér først boksen lidt til højre/ned for markøren. Hvis den ellers
        # ville gå uden for Canvas, flyttes den til venstre/op.
        tx = event.x + 14
        ty = event.y + 14
        text_id = canvas.create_text(
            tx + 8, ty + 6, text=tooltip_text, anchor="nw",
            font=("Segoe UI", 9), fill="#202020", tags="chart_tooltip"
        )
        bbox = canvas.bbox(text_id)
        if not bbox:
            return
        x1, y1, x2, y2 = bbox
        box_w = x2 - x1 + 16
        box_h = y2 - y1 + 12
        if x2 + 8 > width:
            tx = max(4, event.x - box_w - 14)
        if y2 + 8 > height:
            ty = max(4, event.y - box_h - 14)
        canvas.coords(text_id, tx + 8, ty + 6)
        bbox = canvas.bbox(text_id)
        x1, y1, x2, y2 = bbox
        rect_id = canvas.create_rectangle(
            x1 - 7, y1 - 5, x2 + 7, y2 + 5,
            fill="#fffff4", outline="#8a8a8a", width=1, tags="chart_tooltip"
        )
        canvas.tag_lower(rect_id, text_id)

    canvas.bind("<Motion>", show_tooltip)
    canvas.bind("<Leave>", clear_tooltip)

def _single_stock_target_history_series(key, entry=None):
    """Byg Bear/Base/Bull-tidsserie for én aktie i dens egen handelsvaluta.

    Historiske kursmålsposter bruges direkte. Dagens current_snapshot tilføjes,
    når det er komplet, så grafen kan føres frem til seneste observerede kurs.
    Den diskrete kurskurve normaliseres til 0 % ved første komplette snapshot.
    """
    if entry is None:
        data = load_target_age_history()
        entry = data.get("positions", {}).get(str(key or "").upper(), {})
    if not isinstance(entry, dict):
        return []

    points_by_date = {}
    for point in _complete_history_entries(entry.get("history", [])):
        try:
            point_date = date.fromisoformat(str(point.get("date", ""))[:10])
        except Exception:
            continue
        if point_date <= date.today():
            row = dict(point)
            row["_date"] = point_date
            points_by_date[point_date] = row

    snapshot = entry.get("current_snapshot")
    if isinstance(snapshot, dict) and _history_point_complete(snapshot):
        try:
            snapshot_date = date.fromisoformat(str(snapshot.get("date", today_key()))[:10])
        except Exception:
            snapshot_date = date.today()
        if snapshot_date <= date.today():
            row = dict(snapshot)
            row["_date"] = snapshot_date
            points_by_date[snapshot_date] = row

    points = [points_by_date[d] for d in sorted(points_by_date)]
    if not points:
        return []

    first_price = parse_float(points[0].get("price"), None)
    series = []
    for point in points:
        price = parse_float(point.get("price"), None)
        bear = parse_float(point.get("bear_target"), None)
        base = parse_float(point.get("base_target"), None)
        bull = parse_float(point.get("bull_target"), None)
        if price is None or price <= 0 or any(v is None or v <= 0 for v in (bear, base, bull)):
            continue
        series.append({
            "date": point["_date"],
            "count": 1,
            "bear_abs": bear,
            "base_abs": base,
            "bull_abs": bull,
            "price_abs": price,
            "bear_pct": (bear / price - 1.0) * 100.0,
            "base_pct": (base / price - 1.0) * 100.0,
            "bull_pct": (bull / price - 1.0) * 100.0,
            "stock_pct": ((price / first_price - 1.0) * 100.0) if first_price is not None and first_price > 0 else None,
        })
    return series

def show_target_history_window(initial_key=None):
    """Vis aktiens samlede historik med kursmål, handler og regnskaber.

    Rullemenuen viser kun aktiens navn i alfabetisk orden. Børs og ticker
    bruges fortsat internt som entydig nøgle, men forstyrrer ikke visningen.
    """
    data = load_target_age_history()
    positions = data.get("positions", {})
    available = []
    for key, entry in positions.items():
        if _entry_has_history_content(entry):
            name = str(entry.get("name", "")).strip() or key
            available.append((name, key))
    available.sort(key=lambda pair: (pair[0].casefold(), pair[1].casefold()))
    if not available:
        messagebox.showinfo("Aktiens historik", "Der findes endnu ingen historik for aktierne.")
        return

    selected_index = 0
    normalized_initial_key = str(initial_key or "").upper().strip()
    if normalized_initial_key:
        selected_index = next(
            (index for index, (_name, key) in enumerate(available) if key.upper() == normalized_initial_key),
            0,
        )

    win = tk.Toplevel(root)
    win.title("Aktiens historik")
    win.geometry("1660x920")
    win.minsize(1200, 700)
    win.transient(root)
    # Historik + to grafer kræver god lodret plads. Åbn derfor maksimeret
    # på Windows og tilsvarende platforme; geometri ovenfor er fallback.
    try:
        win.state("zoomed")
    except Exception:
        try:
            win.attributes("-zoomed", True)
        except Exception:
            pass

    top = tk.Frame(win)
    top.pack(fill="x", padx=10, pady=10)
    tk.Label(top, text="Aktie:", font=small_font).pack(side="left")
    choice = tk.StringVar(value=available[selected_index][0])
    combo = ttk.Combobox(
        top,
        textvariable=choice,
        values=[name for name, _key in available],
        state="readonly",
        width=42,
    )
    combo.current(selected_index)
    combo.set(available[selected_index][0])
    combo.pack(side="left", padx=(8, 12))
    # Sæt værdien igen, når vinduet er oprettet. Det får readonly-comboboxen
    # til visuelt at stå præcis som efter et manuelt valg i rullemenuen.
    win.after_idle(lambda: (combo.current(selected_index), combo.set(available[selected_index][0])))
    info_var = tk.StringVar()
    tk.Label(top, textvariable=info_var, font=small_font, anchor="w").pack(side="left", fill="x", expand=True)

    columns = [
        ("date", "Dato", 105), ("event", "Begivenhed", 390), ("price", "Kurs", 115),
        ("bear", "Bear mål", 105), ("base", "Base mål", 105),
        ("bull", "Bull mål", 105),
        ("bear_pct", "Bear % mål", 125), ("base_pct", "Base % mål", 125),
        ("bull_pct", "Bull % mål", 125),
    ]
    # Historikken bevares øverst, men får en kontrolleret højde, så de to
    # nye grafer kan stå umiddelbart efter tabellen i det maksimerede vindue.
    history_table_frame = tk.Frame(win, height=300)
    history_table_frame.pack(fill="x", padx=0, pady=0)
    history_table_frame.pack_propagate(False)
    tree_hist = build_tree(history_table_frame, columns, lambda c: None)

    graph_status_var = tk.StringVar(value="")
    stock_abs_canvas = tk.Canvas(win, height=300, background="#ffffff", highlightthickness=1, highlightbackground="#d0d0d0")
    stock_abs_canvas.pack(fill="x", expand=False, padx=10, pady=(8, 6))
    stock_pct_canvas = tk.Canvas(win, height=300, background="#ffffff", highlightthickness=1, highlightbackground="#d0d0d0")
    stock_pct_canvas.pack(fill="x", expand=False, padx=10, pady=(0, 6))
    tk.Label(win, textvariable=graph_status_var, font=small_font, anchor="w").pack(fill="x", padx=10, pady=(0, 8))

    def render(event=None):
        index = combo.current()
        if index < 0 or index >= len(available):
            index = 0
        _name, key = available[index]
        entry = positions.get(key, {})
        hist = _complete_history_entries(entry.get("history", []))
        earnings = [
            event for event in entry.get("earnings_events", [])
            if isinstance(event, dict)
            and (_date_from_tv_value(event.get("date")) or date.max) < date.today()
        ]
        # Porteføljebyggeren arbejder ikke med handler. Eventuelle gamle
        # handelsbegivenheder i en eksisterende historikfil ignoreres derfor
        # bevidst i denne visning.
        buy_events = []
        trade_events = []
        visible_trade_events = []

        next_earnings = _date_from_tv_value(entry.get("next_earnings_date"))
        combined = [(str(point.get("date", "")), 0, "target", point) for point in hist]
        combined += [(str(event.get("date", "")), 1, "buy_window_purchase", event) for event in buy_events]
        combined += [(str(event.get("date", "")), 2, "trade", event) for event in visible_trade_events]
        combined += [(str(event.get("date", "")), 3, "earnings", event) for event in earnings]
        if next_earnings is not None:
            combined.append((next_earnings.isoformat(), 4, "next_earnings", {"date": next_earnings.isoformat()}))
        combined.sort(key=lambda row: (row[0], row[1]))

        tree_hist.delete(*tree_hist.get_children())
        for i, (_date_text, _order, event_type, point) in enumerate(combined):
            if event_type == "buy_window_purchase":
                shares_bought = parse_float(point.get("shares_bought"), None)
                weight_pct = parse_float(point.get("weight_pct"), None)
                event_text = "Køb i købsvindue"
                if shares_bought is not None:
                    event_text += f" · +{format_antal(shares_bought)} akt."
                if weight_pct is not None:
                    event_text += f" · {format_pct(weight_pct).replace('+', '')} PF"
                vals = [
                    point.get("date", "-"), event_text, format_num(point.get("price"), 2),
                    format_num(point.get("bear_target"), 2), format_num(point.get("base_target"), 2),
                    format_num(point.get("bull_target"), 2),
                    format_plain_pct(point.get("bear_pct")),
                    format_plain_pct(point.get("base_pct")),
                    format_plain_pct(point.get("bull_pct")),
                ]
            elif event_type == "trade":
                trade_type = str(point.get("type", "")).lower()
                shares_changed = parse_float(point.get("shares_changed"), None)
                event_text = "Køb" if trade_type == "buy" else "Salg"
                if shares_changed is not None:
                    sign = "+" if trade_type == "buy" else "−"
                    event_text += f" · {sign}{format_antal(shares_changed)} akt."
                vals = [
                    point.get("date", "-"), event_text, format_num(point.get("price"), 2),
                    format_num(point.get("bear_target"), 2), format_num(point.get("base_target"), 2),
                    format_num(point.get("bull_target"), 2),
                    format_plain_pct(point.get("bear_pct")),
                    format_plain_pct(point.get("base_pct")),
                    format_plain_pct(point.get("bull_pct")),
                ]
            elif event_type == "earnings":
                vals = [point.get("date", "-"), "Regnskab", "-", "-", "-", "-", "-", "-", "-"]
            elif event_type == "next_earnings":
                vals = [point.get("date", "-"), "Næste regnskab", "-", "-", "-", "-", "-", "-", "-"]
            else:
                vals = [
                    point.get("date", "-"), "Kursmål", format_num(point.get("price"), 2),
                    format_num(point.get("bear_target"), 2), format_num(point.get("base_target"), 2),
                    format_num(point.get("bull_target"), 2),
                    format_plain_pct(target_history_upside(point, "bear_target")),
                    format_plain_pct(target_history_upside(point, "base_target")),
                    format_plain_pct(target_history_upside(point, "bull_target")),
                ]
            tree_hist.insert("", "end", values=vals, tags=("even" if i % 2 == 0 else "odd",))
        known = "kendt" if entry.get("change_date_known") else "mindst kendt siden første observation"
        next_text = next_earnings.isoformat() if next_earnings is not None else "-"
        info_var.set(
            f"Næste regnskabsdato: {next_text} · "
            f"{len(hist)} kursmålsposter · {len(earnings)} tidligere regnskaber · "
            f"Seneste kursmålsændring: {entry.get('last_change_date', '-')} ({known})"
        )

        # De to grafer bruger samme visuelle logik som Fase 3, men kun den
        # valgte akties egne historiske snapshots. Absolutte mål står derfor
        # i aktiens handelsvaluta; procentgrafens svage 'Kurs'-kurve starter 0 %.
        stock_series = _single_stock_target_history_series(key, entry)
        exchange = str(entry.get("exchange", key.split(":", 1)[0] if ":" in key else ""))
        currency = currency_for_exchange(exchange)
        stock_name = str(entry.get("name", _name)).strip() or _name
        _draw_phase3_target_chart(
            stock_abs_canvas, stock_series,
            ("bear_abs", "base_abs", "bull_abs"),
            f"Absolutte kursmål over tid – {stock_name}",
            f"Kursmål ({currency})",
            percent=False,
            overlay_key="price_abs",
            overlay_label="Kurs",
        )
        _draw_phase3_target_chart(
            stock_pct_canvas, stock_series,
            ("bear_pct", "base_pct", "bull_pct"),
            f"Procentuelle kursmål over tid – {stock_name}",
            "Potentiale (%)",
            percent=True,
            overlay_key="stock_pct",
            overlay_label="Kurs",
        )
        if stock_series:
            graph_status_var.set(
                f"{len(stock_series)} grafpunkter fra {stock_series[0]['date'].strftime('%d-%m-%Y')} "
                f"til {stock_series[-1]['date'].strftime('%d-%m-%Y')} · Kursudvikling starter ved 0 %."
            )
        else:
            graph_status_var.set("Ingen komplette kursmålsposter til grafer for den valgte aktie endnu.")

    combo.bind("<<ComboboxSelected>>", render)
    stock_abs_canvas.bind("<Configure>", lambda event: render())
    stock_pct_canvas.bind("<Configure>", lambda event: render())
    render()


def _phase0_analysis_row_for_item(x, cache=None):
    cache = cache or load_daily_cache()
    key = position_key(x)
    raw_cached = cache.get("phase1", {}).get(key, {})
    fx_rates = dict(cache.get("fx_rates", {})); fx_rates.setdefault("DKK", 1.0)
    raw = cache_raw_from_item({**x, "antal": 1}, raw_cached, fx_rates) if raw_cached else None
    fundamental = normalize_phase2_cache(cache.get("phase2", {}).get(key, {}))
    if raw is None:
        return None, fundamental
    display = make_display_row(raw, max(float(raw.get("value_raw", 0.0) or 0.0), 1.0))
    row = make_phase2_row(display, raw, fundamental, "")
    return row, fundamental

def show_selected_phase0_target_history():
    selected = universe_tree.selection() if "universe_tree" in globals() else ()
    if not selected:
        show_target_history_window()
        return
    vals = universe_tree.item(selected[0], "values")
    if len(vals) < 3:
        show_target_history_window(); return
    key = f"{str(vals[1]).upper()}:{str(vals[2]).upper()}"
    data = load_target_age_history()
    entry = data.get("positions", {}).get(key, {})
    if not _entry_has_history_content(entry):
        messagebox.showinfo("Aktiens historik", f"Der findes endnu ikke tolkbar historik for {vals[3] if len(vals)>3 else key}.")
        return
    show_target_history_window(initial_key=key)

def _update_universe_headers():
    if "universe_tree" not in globals():
        return
    titles = {col:title for col,title,_width in universe_cols}
    for col, title in titles.items():
        arrow = ""
        if col == universe_current_sort:
            arrow = " ▼" if universe_descending else " ▲"
        universe_tree.heading(col, text=title + arrow, command=lambda c=col: sort_universe(c))

def refresh_universe_tree():
    global _phase0_preview_mode, _phase0_preview_history
    if "universe_tree" not in globals():
        return
    universe_tree.delete(*universe_tree.get_children())
    items = load_stock_universe()
    cache = load_daily_cache()
    # Historikken indlæses én gang pr. refresh. Samtidig sættes preview-mode,
    # så make_phase2_row ikke registrerer historik/regnskab under ren visning.
    try:
        _phase0_preview_history = load_target_age_history()
    except Exception:
        _phase0_preview_history = {"positions": {}}
    _phase0_preview_mode = True
    ready_keys, missing_keys, total = _universe_readiness(items)
    rows_to_show=[]
    for original_nr,x in enumerate(items,1):
        key=position_key(x); ready=key in ready_keys
        region,sector,industry=_phase0_classification_for_item(x,cache)
        analysis,fundamental=_phase0_analysis_row_for_item(x,cache)
        trend_pct, _trend_score, trend_known = _builder_target_trend_for_key(key, _phase0_preview_history)
        def av(field, sort=False):
            if not analysis: return None if sort else ""
            return analysis.get(("sort_" if sort else "")+field, "")
        row={
            "nr":original_nr,"exchange":str(x.get("exchange","") or ""),"ticker":str(x.get("ticker","") or ""),"name":str(x.get("name","") or ""),
            "status":"Klar" if ready else "Mangler data","locked":"Ja" if bool(x.get("locked",False)) else "Nej","is_locked":bool(x.get("locked",False)),
            "region":region,"sector":sector,"industry":industry,"ready":ready,
            "price": av("price"), "bear_pct": av("analyst_bear_pct"), "base_pct": av("analyst_base_pct"), "bull_pct": av("analyst_bull_pct"),
            "_analyst_bear_pct": av("analyst_bear_pct", True), "_analyst_base_pct": av("analyst_base_pct", True), "_analyst_bull_pct": av("analyst_bull_pct", True),
            "_data_warning": bool(analysis.get("data_warning")) if analysis else False,
            "_upside_sell": bool(analysis.get("upside_sell")) if analysis else False,
            "_buy_opportunity": bool(analysis.get("buy_opportunity")) if analysis else False,
            "target_trend": (format_plain_pct(trend_pct) if trend_known else "Neutral"),
            "dividend_yield": av("dividend_yield"), "stock_score": av("stock_score"), "quality_score": av("quality_score"),
            "confidence_score": av("confidence_score"), "trend_strength": av("trend_strength"), "robustness": av("robustness"),
            "structure_score": av("structure_score"), "structure_layer": av("structure_layer"), "value_score": av("value_score"),
            "pe": av("pe"), "peg": av("peg"), "revenue_growth_3y": av("revenue_growth_3y"), "ebit_margin_ttm": av("ebit_margin_ttm"),
            "roic": av("roic"), "fcf_margin_ttm": av("fcf_margin_ttm"), "fcf_growth_3y": av("fcf_growth_3y"),
            "market_cap": format_num(parse_float(fundamental.get("market_cap"),None),0) if not value_is_missing(fundamental.get("market_cap")) else "",
            "_target_trend_num": trend_pct if trend_known else 0.0,
        }
        rows_to_show.append(row)
    numeric_cols={"nr","price","bear_pct","base_pct","bull_pct","target_trend","dividend_yield","stock_score","quality_score","confidence_score","trend_strength","robustness","structure_score","value_score","pe","peg","revenue_growth_3y","ebit_margin_ttm","roic","fcf_margin_ttm","fcf_growth_3y","market_cap"}
    def sort_key(row):
        col=universe_current_sort
        if col=="nr": return int(row["nr"])
        if col=="target_trend": return float(row.get("_target_trend_num",0.0))
        if col in numeric_cols:
            v=parse_float(row.get(col),None)
            return -1e99 if v is None else float(v)
        return str(row.get(col,"") or "").casefold()
    rows_to_show.sort(key=sort_key,reverse=universe_descending)
    col_ids=[c[0] for c in universe_cols]
    for i, row in enumerate(rows_to_show):
        # Fase 0-prioritet: låsestatus står altid over analytikerfarven.
        # Uden komplette indlæste data gives ingen analytisk farve.
        if row.get("is_locked"):
            tag = "universe_locked"
        elif not row.get("ready"):
            tag = "universe_neutral_even" if i % 2 == 0 else "universe_neutral_odd"
        elif row.get("_upside_sell"):
            tag = "sell"
        elif row.get("_data_warning") or any(
            parse_float(row.get(field), None) is None
            for field in ("_analyst_bear_pct", "_analyst_base_pct", "_analyst_bull_pct")
        ):
            tag = "data_problem"
        elif row.get("_buy_opportunity"):
            tag = "buy_opportunity"
        else:
            color = phase2_analyst_color({
                "analyst_bear_pct": row.get("_analyst_bear_pct"),
                "analyst_base_pct": row.get("_analyst_base_pct"),
                "analyst_bull_pct": row.get("_analyst_bull_pct"),
            })
            if color:
                tag = "universe_analyst_" + color[1:]
                universe_tree.tag_configure(tag, background=color, foreground="black")
            else:
                tag = "universe_neutral_even" if i % 2 == 0 else "universe_neutral_odd"
        universe_tree.insert("","end",values=tuple(row.get(c,"") for c in col_ids),tags=(tag,))
    _phase0_preview_mode = False
    _update_universe_headers()
    if "universe_count_var" in globals(): universe_count_var.set(f"{len(ready_keys)}/{total} aktier klar til porteføljebygning")
    if "universe_data_state_var" in globals():
        if total and len(ready_keys)==total: universe_data_state_var.set(f"Alle {total} aktier er korrekt indlæst og klar til Fase 1.")
        elif total: universe_data_state_var.set(f"{len(ready_keys)}/{total} aktier er klar. {len(missing_keys)} mangler nødvendige data.")
        else: universe_data_state_var.set("Aktieuniverset er tomt.")




# ============================================================================
# APB ALL-IN-ONE WEB EDITION v0.8
# Proof of concept: input -> existing desktop engine -> immediate web result.
# No user database is required. Persistent server data is JSON/file based.
# ============================================================================
import base64
import copy
import io
import secrets
import hashlib
import hmac
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Alpha Portfolio Builder", page_icon="📈", layout="wide")
st.markdown("""
<style>
:root { --apb-blue:#1565c0; --apb-blue-dark:#0d47a1; --apb-soft:#f5f8fc; }
.block-container {padding-top:1.6rem!important; padding-bottom:2.2rem!important; max-width:1500px!important;}
h1 {font-size:2.05rem!important; margin-bottom:.1rem!important;}
h2,h3 {letter-spacing:-.01em;}
div[data-testid="stVerticalBlock"] {gap:.7rem;}
.apb-card {border:1px solid rgba(21,101,192,.16);border-radius:14px;padding:14px 16px;background:linear-gradient(180deg,#fff 0%,#f8fbff 100%);min-height:88px;box-shadow:0 2px 10px rgba(15,23,42,.035)}
.apb-kicker {font-size:.73rem;color:#64748b;text-transform:uppercase;letter-spacing:.055em;margin-bottom:3px}
.apb-big {font-size:1.42rem;font-weight:700;line-height:1.25;color:#0f172a}
.apb-subtle {color:#64748b;font-size:.84rem;margin-top:2px}
.apb-welcome {padding:14px 16px;border-radius:14px;background:#f7faff;border:1px solid #dbeafe;color:#334155;margin:.2rem 0 .8rem 0}
.apb-userline {font-size:.86rem;color:#64748b;text-align:right;padding-top:.35rem}
.apb-login-title {font-size:1.15rem;font-weight:700;color:#0f172a;margin:0 0 .18rem 0;}
.apb-login-subtitle {font-size:.93rem;color:#64748b;margin:0 0 .55rem 0;}
.apb-login-gap {height:1.15rem;}
/* Keep Streamlit controls inside the APB blue visual system. */
input[type="radio"] {accent-color:var(--apb-blue)!important;}
.stRadio [data-baseweb="radio"] input:checked + div {background-color:var(--apb-blue)!important;border-color:var(--apb-blue)!important;}
.stRadio [data-baseweb="radio"] input:checked ~ div {border-color:var(--apb-blue)!important;}
.stButton > button[kind="primary"] {background:var(--apb-blue)!important;border-color:var(--apb-blue)!important;color:white!important;font-weight:650!important;border-radius:9px!important;min-height:2.65rem!important;}
.stButton > button[kind="primary"]:hover {background:var(--apb-blue-dark)!important;border-color:var(--apb-blue-dark)!important;}
.stButton > button {border-radius:9px!important;}
div[data-testid="stProgress"] > div > div > div > div {background-color:var(--apb-blue)!important;}
div[data-baseweb="input"] > div, div[data-baseweb="select"] > div {border-radius:9px!important;}
[data-testid="stDataFrame"] {border-radius:12px;overflow:hidden;}

.apb-pdf-open {
    display:inline-block;
    background:#1565c0 !important;
    color:#fff !important;
    text-decoration:none !important;
    font-weight:700;
    padding:.62rem 1.05rem;
    border:1px solid #1565c0;
    border-radius:8px;
}
.apb-pdf-open:hover {
    background:#0d47a1 !important;
    border-color:#0d47a1 !important;
    color:#fff !important;
}

/* Product-like shell: hide Streamlit's own top-right actions. */
[data-testid="stToolbar"],
[data-testid="stHeaderActionElements"],
#MainMenu {visibility:hidden !important; display:none !important;}
header[data-testid="stHeader"] {background:transparent !important;}

/* Stronger radio override for current Streamlit/BaseWeb versions. */
div[data-testid="stRadio"] input[type="radio"] {accent-color:#1565c0 !important;}
div[data-testid="stRadio"] label[data-baseweb="radio"] input:checked + div {
    background-color:#1565c0 !important;
    border-color:#1565c0 !important;
}
div[data-testid="stRadio"] label[data-baseweb="radio"] input:checked + div > div {
    background-color:#1565c0 !important;
}
.apb-head-logo {padding-top:.65rem; padding-bottom:.15rem;}

:root, .stApp, [data-testid="stAppViewContainer"] { --primary-color:#1565c0 !important; }
div[data-testid="stRadio"] input[type="radio"] { accent-color:#1565c0 !important; }
div[data-testid="stRadio"] [role="radio"][aria-checked="true"] > div:first-child,
div[data-testid="stRadio"] label[data-baseweb="radio"] input:checked + div,
div[data-testid="stRadio"] label[data-baseweb="radio"] input:checked ~ div:first-of-type {
    background-color:#1565c0 !important;
    border-color:#1565c0 !important;
}
div[data-testid="stRadio"] [aria-checked="true"] svg {
    fill:#1565c0 !important;
    color:#1565c0 !important;
}
div[data-testid="stDownloadButton"] button,
button[kind="primary"],
button[data-testid="stBaseButton-primary"] {
    background-color:#1565c0 !important;
    border-color:#1565c0 !important;
    color:#fff !important;
}
div[data-testid="stDownloadButton"] button:hover,
button[kind="primary"]:hover,
button[data-testid="stBaseButton-primary"]:hover {
    background-color:#0d47a1 !important;
    border-color:#0d47a1 !important;
    color:#fff !important;
}



/* Basic money fields: yesterday's formatted text input + inline step controls. */
div[data-testid="stColumn"]:has([class*="st-key-portfolio_value_input"]),
div[data-testid="stColumn"]:has([class*="st-key-minimum_position_input"]) {
    position: relative !important;
}

/* Leave room inside the text field for the two controls. */
[class*="st-key-portfolio_value_input"] input,
[class*="st-key-minimum_position_input"] input {
    padding-right: 4.6rem !important;
}

/* Place the +/- widget wrappers over the right side of the text field. */
[class*="st-key-portfolio_value_input_minus"],
[class*="st-key-minimum_position_input_minus"] {
    position: absolute !important;
    right: 2.35rem !important;
    top: 1.72rem !important;
    z-index: 20 !important;
    width: 2rem !important;
}
[class*="st-key-portfolio_value_input_plus"],
[class*="st-key-minimum_position_input_plus"] {
    position: absolute !important;
    right: 0.25rem !important;
    top: 1.72rem !important;
    z-index: 20 !important;
    width: 2rem !important;
}

/* Make the overlaid controls look like Streamlit's native number-input steppers. */
[class*="st-key-portfolio_value_input_minus"] button,
[class*="st-key-portfolio_value_input_plus"] button,
[class*="st-key-minimum_position_input_minus"] button,
[class*="st-key-minimum_position_input_plus"] button {
    width: 2rem !important;
    min-width: 2rem !important;
    height: 2.35rem !important;
    min-height: 2.35rem !important;
    padding: 0 !important;
    margin: 0 !important;
    border: 0 !important;
    border-radius: 0 !important;
    background: transparent !important;
    color: #31333f !important;
    box-shadow: none !important;
    font-size: 1rem !important;
}

/* Hover highlights only while the pointer is over the control. */
[class*="st-key-portfolio_value_input_minus"] button:hover,
[class*="st-key-portfolio_value_input_plus"] button:hover,
[class*="st-key-minimum_position_input_minus"] button:hover,
[class*="st-key-minimum_position_input_plus"] button:hover {
    background: #1565c0 !important;
    color: #ffffff !important;
}

/* Do not visually remember the last clicked button. */
[class*="st-key-portfolio_value_input_minus"] button:focus:not(:hover),
[class*="st-key-portfolio_value_input_plus"] button:focus:not(:hover),
[class*="st-key-minimum_position_input_minus"] button:focus:not(:hover),
[class*="st-key-minimum_position_input_plus"] button:focus:not(:hover),
[class*="st-key-portfolio_value_input_minus"] button:active:not(:hover),
[class*="st-key-portfolio_value_input_plus"] button:active:not(:hover),
[class*="st-key-minimum_position_input_minus"] button:active:not(:hover),
[class*="st-key-minimum_position_input_plus"] button:active:not(:hover) {
    background: transparent !important;
    color: #31333f !important;
    box-shadow: none !important;
    outline: none !important;
}

/* Native number-input steppers: hover may highlight, but the last click must not stay selected. */
div[data-testid="stNumberInput"] button:focus:not(:hover),
div[data-testid="stNumberInput"] button:active:not(:hover) {
    background:transparent !important;
    box-shadow:none !important;
    outline:none !important;
}

.apb-account-card {
    margin-top:.55rem;
    margin-bottom:.45rem;
    padding:.58rem .72rem;
    border:1px solid rgba(21,101,192,.16);
    border-radius:12px;
    background:#ffffff;
    box-shadow:0 3px 12px rgba(20,55,90,.05);
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:.65rem;
}
.apb-account-name {
    font-size:.96rem;
    font-weight:700;
    color:#1f2937;
    line-height:1.15;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
}
.apb-account-tier {
    display:inline-block;
    flex:0 0 auto;
    padding:.12rem .48rem;
    border-radius:999px;
    background:#eaf3ff;
    color:#1565c0;
    font-size:.75rem;
    font-weight:700;
    letter-spacing:.01em;
}
</style>
""", unsafe_allow_html=True)

COVER_IMAGE_B64 = """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"""
LOGO_IMAGE_B64 = """iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAIAAABMXPacAABLU0lEQVR42n29ebxlVXUnvtba59zhDfWqKKqgmEehGGRQQAYF5xln7URjq3HIpB2j6fzSGdokn3SnY9rEaDQkatSOJhjnBpwVxQFFFAUBwWIoCqjx1Zvufffes9f69h97n3P2Off5Qz5Y79V7996zhzV813d9F6sqETExEYiImAkAVV8TEalqnufhz4888ujN37/l5h/cesdddz/40COHFg+vDkajSQEzwOIrEDMzERFARIhfEKj6fyGi8F8GiDn8FgGIbxx+Kfw8V/8BiKvPBRAzUL6bWfxxYpgRh4ciIhABAIGYCUQMImEC4gcGyoemcikIVH1Zvle9HkQgEu518vnZmc2bF044bsc5O8+8+PEXPOGSi04++aTwI8WkECciEh4nfjAiIlRry8RcbkD1rfj64TtmlmUZEQ2H69ddd8MnPvW5m777/f1795P3xI6yjJwjJ8QSfoOJEDeg9aocPwW31pTjM3P9vGEtwkuAwCTU2M5qhcDhe/E7qH4M1cLFR6Gw1hxfMP4FhQ2IP4XqBFbvVS84wJS8fvhbgMzIe1JPUGK3edvWix9//ste/IIXvfDqrVuPIKKiKJxz6WlOV5jSDUi+G/9sqlmej0ajf/7Ah9/zvn+69647iYQ6M9LpsEhYAiCeq/i7zHFBmKk+2vHRwg8lRzteB6b0G1xdm+qYUPMnmiuL1lonV5mILDmAFHcU1aqGe4Zqy8pjg3ojyxtZvwUsbB6zcPkE4VWsmNB4najYcfwpb/j1V//Ob79p25FHeq/MJHFlWv9suAHMZiYsLPzlr3zt9//gj3/64x+Rm3GzM0xkZgYwMbGEMxMWqDqIwSw0l6965LABUq5O8yPVW1VuEsrzzdUFSzegcURp+h9ufj+aEZSmrH6deC3qXQAB8QAB9ds1bDMIBLLKshGIGSLCzH40osnacSee8ufv+KPXvubXiMh770SmnplYVbl5qNQsy7KiKP6/P3rHu/73uwmSzc+bmZkxM+IecfV8HAx6+HDCpaWjZCW5PNfE4U7UD9b4MNUJqLekcXW5XLlyjSj5MyfPkfxNslUovwyvAq7sWL23nKx1uW+Gyi7F1Q6fHwChcitUWjkiYmEnrlgfUjF4xa/86vv+4e+O2LK5KIrMOWpaezbV9NCE1T9w8NArfuXV3/jql9zcNiJSNRJODjtzZayZ4zfDtSg3uVr8cOaThebK7CeLyw1vV16l2vRXXhyU2uly9esfAoHTn09/q96AKtZA3PPSrHN7dxseOJq72tOg/KtoqJhq20VEwizCfvXgzrMf+8n/+PhZO8+o9qBeDC03oDr7D+15+DnPf+kdt/04XzjS+wL1M3PLHKd2v1xyJmYYiJmDb+DyitTvyc17GL5gJBerfTm4XGjm2isyt6xQvQQtMwXUvh1GPGWKo1lHGSZhw1dGckzKw4f4UdB838pwAVmeFytL248+6obrP/u4C89r7UHtA8xMXHbw4MGrnva8O3/6k3zTEYUvmCR8aiZGeZargCWGgMSVdW+tWhnNCAAixJ0oA6F4MlEFPOHFJH769ppT84tkV+KJtvgDCN61cZar9U3sRrLHdZSJMtSixFE1LVJpx5o2qzKy4S+tDhIIWZb7wer2o7Z942tfOGvnGd575yQ+cDBBBgRH8bRnv/Db37gx37S1KMbMEj1tdKpM3Ljb5cJx+b/yIJc+qTRQXBre6KWpOumo7U+MkVvXpTxH4OrioIxr0Xid+rwTYFx7GlDDRKFtYVIbFX0rGllE41DXiUXTjJY3rPbPSHMIl2V+dfm0Mx9z87e/vmXLZgDCTERSvZ5z7q3/9U++/Y2v5Atbi2JSmVGuAsjyDZufvbLoqbNkal2H6uZw4qJR7gRz6Z0lyRtSt8Hc9tigZqbUMHIiVZyd/KHyK0LlNodgB0lSUj5oHTc3rWXr46WnJ75e/ZHDAWUmYu99Nr/wi7vveO0bfkdEylSCWNVMNcuz62/40vOe+8JsbrOaVkEacxXVcPWKVH/i8BdSO1XmKnZjlIe9ZZqIy9ifa7fMydFJ3DDKIDsNW8sQqrE8aEapjRip8bfVebcq+yWkv1vZ+pYLISJrv0UjNUOd5Zafu/rb8HNZlhWr+6/55w++8fWv8SFH894z8/pw/bEXPfH+X+yS3oyqpueFp4xMI/1sbBIxMSQecpSJGFMaenINTsT8Obrqam1Le119BjQiE2YAlcXn2oKBq3tqtkHO1rDm4c82lZ1VJ6DKA1o7UXmu5M6UG1AaOVDimtKEjpnJT7YcsfmOH9+8ffs2AGJmIvK+f/rgfXff7mbmwuqHf8IfwPUlx5QtbNkGlO8XYmFm4dQ5V8429WmNGLz06iJVrNs0OUyAIyOz+ohxnfHFlebEuG2Qf6IV/lZHJOIoSWDWylvTbDF1CfWrcbQV9Y4l6JLBpNs7tHf3X7/r70XEDJJl2crK6t++5xruzMO0YbbL7JlLL8qo7APXB4mlTLBKi5OancS2Tn3k6k/cNFHVDUxTgfglvL/mf7xpx9HbuPDMqY+p3Xt959IXmcbUpha0PgpAffe4kfeBuca64lLEm1hmBdF2lNeTwYz4HTFV7ix88EP/Z+/efXmeCTN/5nPXPfrAva7XN2s7nfrLekka7ohTV0lEUj8tqutIRtW9bXlN5jqyRQkAVGa6mZ86YQzWL7v4rF9/4xUvefb5GI5cJu2jjSRt5mbYOh0oV1c1eWpOE+82SBa3gevHQfuGRSfAtTsun6WKc12nu3Joz7Wf/EyMgj7+iU8xu9p0NJIZ1NGGCNI4IBioZoKPdoSUZEuwYBzAzCwREeIa7poCDMoHRmK2gD/8zafBDv7Or13S37qg6SXY4IxzGl9S84v0OCGFKxrHrvkLaO1Qci2oNPTVL5Z/BqdHFSAClKlz7X982szkgQd3f+/7P0RnNkA9TMHFNd4SXN7q8AMhkivRZU5xxOozIUnYSFIbQTQdGnHiBbnxxNFCwInTwfiiS3c++2nHFYuHz7jguFe88BJbGWaOmayZOdRPWh/kxCTylEnkKdioPBagaf87bR7qKL1MjNC0qk2c0QzozPz4tp/+/Of3yrdu+s7qwYOS50iiwDTE4/ogAqVPDuh4yxtVrhvlhUgNMTixy5TicQ2IiEIyXFY96h8WJqM/eNNTXZ9VGeOVt73hSZ25GfXK1aWtVhnlB0i3hFublAAGiTdu2I222+bkmtfVnmSxUb40ozYCxGjsEDFLno9Wlm/81rflu9/7QR3zceU7OA1vAjTM0YwgOfLJcY7ZgNS3ogXzR0NvZVxvyQdOkqbGJsXVd8I6WH/shadc/axTdHm1k5FfG51zwVHPf84FurruhMiMa2gMSDK/1iFJzUIK8VfnlCuksWmDEncHEUaAj9J7EsNxVOEYJ6ehzrRRJQn83Zt/ILffeTexS31XXbeqXowYoXQYE1lwO7RLo45wF4RZ6visnZFOJc6NTUJ9RcJyCWNib331JXl3pN6YQTDyw7e94cmum5tpCEG4cpJ1Js5tSxPPJ+ptBqY2CmkxMvWz4piZdWUSQJPUWpceQlphS11x4iQWB0jyu+6+R/Y8vJecS0qgU2ahtqKleUFVQkpxhSkLSe3grhUANeI+rjYXSZYEApyIH45PP+eElz//TFsdOAFMhdWvDS+97NinP/Wxfm3duXCvLInK0zeaqlEyT8HalZ23KuOrvUY4U0K6NraRf+UrznrfHz+RJ5NG8NSAJyrDQC3Utk7t8uyRR/fJ8vIyOVcXOVuRJbeXrrZPIUtoYGexRtlwXwAZatMJQuNFI1CMRqCSwqvEQhj5t77m8pktKAolKFnBBJgSr7/9TVeyuJAbMxPDGGBOwuVw4Rm/vHDGTSg0iYzK++Qc26jQ1eKKJ5zwhWue9a9/fcnW3sBGFsu9rVynNoQ0VepNn0+WVtdkOBqTkyTR3Tjoal7LJIFsX8F2wScJn1FWoqpNishtw2mm2StMCH59fPxpR73y6tNsecUxkykTkXlh+JX1pzzx+CsuP6NYW3cuCfcScKb0N7zBTQXS2DnZojoIdo6tMH94dPrJR3z4nU/92nuf+LSzcltc2/XIOqXRF5KbV582JNB6A8gLizkZj6XwWhbYygWNdoaan6xxqBIIFgmhowHOJBQHTkFQljJrBNowS/VRI9oDEcZw8luvvHTTVvVjFVIiA5RgTGaq3NG3vf6JZKAKQYq/a1QX38lQfdTyKJi17D4DKfzhhAH4w+tHLPT/4r9edvMHn/qfn7pltLK6vA4R3r84nIK1qYUQNq4BtYKaGI9K5SgSe5dgn0jvVaPsNW3aaYPPgnakXb1SCzEu3w6ow39h9uPJ9hO3vf4lj7HlFRHAlACGEQxmTqAra8995qkXXnRasbbupMTXOPnMLKXJrKCBVjjAzaMPcSzCfnnkSN7wny/8wUef+cevOraH4fLyRJw4JvJ+78F1Iqkhn1BjbhzzJFBsEQoSmEjKbLS6F1yj77U7iHcCLY9aIZ2NxLKVgtS42Aaofl28qZxTjUKIEAaj17/8oiOPRjEqOBh6+OgnTclUi0nW92/79ctQWB1Hpnh8wz1G2kDTyaEGN4Vd5nQw0bXiec8+4zsfed4//cFZx88VS4fWDewcwcAE73Xf4nrEZdNaDjXz8PKR0c5E6hQpq4xWyj0rT2z5RSxJJiA41yQT3uAScCw4pieu5SsqSBtlJF4zHmLsphO/sGPrb77sTFtdE8mCKYcxixAZMZHBMdnhlRc/57Szzzvxzrsfzvtdjey6BvLa8Dpt4CFW210mfuRtWJx/4XF/8hvnv/jyI7C+urx/mZmzjAlWGbrh2PYdGpFwShJA/ZaJe69AvZQCgxp3lybERq0Qpjod05BlE1NMnSraJY1pkCjNSJnTGKkiHIiwrY1+7UUXHHdC5kcqZDAfASUYwQdDxFBfaG9W3/Lqx2GkzCnij5rFRinSl9avjAhZJgD84vDY7fN//5fP+O6Hn/HiKxYGi0trgyLLxAkxABigpp5hg+FkabWgTFCdWrSA3MQbg1pUHeKqHg6hpFybZI6oyh3BYzJTA+NFtZ11naSZPLa9axWcAU1QFI28gwEmMEO99rcuvOVXzsZghQlkWm0Pw2CAGZkn9UJmy8u/8oLTTjpj+2R9LNyGnVEjVJZwGxByWmbyS+v9PH/7f7nq1k+88M2vOMaNlgdL6+JYpM56yIBAjiIcXhkvDwpyUqOvDVvQ3OYU1kOr+EFCrbItT59z3gAbqZkx1IJ0piu0NIXztqFJbhOnnLCtjl76nLNPP7VbDMYcC+VGMDIFtDy8RjAh8xPMb5bf+pXzsO5ZWiXMmLA0M6+4Rbo6sqG+6Orzvv/vL3nn7+3c3hmsH1wFsWNEFgUBpqbeTAGo90J6cHk8GGpkJqYnktNovVGUrpIKUMpRjKQ24kaYymi40VaNgNN6KHMLBAU2SHaYEn40c5OrykhsUlmuVcvmer/7q2djfYVYuArYzWK8CGUYm4XvCxuW1l734rOOPvEIPyoaKCsBraMAA8BAh+XKJ551/Yde9ul3XnLu8TTaf3hSmHME8zCFKQCYkhnUm/fqvXpl6L6DazRREZ4qyqcMhIYN4PJscRkQhWBBpvGYNIJI1oQjF7yiGNbBaMMXcZpDhLdIMwNshN03gFI4YV1Zf97Td154zpxfHbnyHBJAZAQlGGAhJCWAfCGAn+jW7fLrLz3X1sYiKSyBGkysaATM5G3Htvn/+dZLnvP0rcTwY5QrDpjBFCCoh8HMQw0g8958QfB7D62Toc5mmGt6VAs9pVYQyGl+SARpHu+SMt+CImrCHdCiNKWBHpoAW01gSN0DkiioidzUbAXjXuf3fvV8Gq+CJRTUuHKkFk6lMhGgZJ6IYMZQLC296cWnbd6xyU+KChxFyoxDkpt13IN7D1/+4vdcdfVHrr3u3vXxuL/Q6eVsvghXxNSbmamGr2BmBgMYePTAsEWjnLrx09WcaUiWiOC4M0eUvlDCxy+rzDVJpapftzidLc9RAUScAjsJst8s2ZRVZoCQCfnV0VVPOv1PXn+6X1lzThqM81h9MiJmMq7gUlPSohgXRxzV27Nv9IPv7clnO8E+xRMq7Wp63DOWB+8/+Mkv/uQ/vnzPaKjbFtzCjFMNJshMLTSeADAzAGro5fQf39p728/XpZejCdymVAmU1Aq0Sz9JD0S9UnW5Rpr0JzR5Vc0gtwWFco15N7pJku2pktHGJtUgHgxGLG9/1bnsVy0cdhhqdMHItCQtK7QgVSrXi4mxsvaWl54+e+ScL7S87tQEcDklFzGzm51x/U2/eGj0B+/65ruu3dWfyXzhYWHpy9DVQgwEU/VqB1Y8kTSDda6SpjaI1iqMce0Uq5JTSFuajPmNmfct9qcQN2unoWZJLSeeXkyj0io3Ih8QwZxjXRtf/IRTnnXxlsnhgWOQGawEdmBkPubAWgTgE+qhnkxDTjAZTh5zcvcVzznZ1iaZk7RQylUTQLyyoS4tRgLOsjxf2Hrk777ynGJ9FG+LGUWXELbDoEqgibdDyxOSOnioG7EqMiTQ5PQ1eBdVub4Ck7nRI5YU9oiTGn3iJ2v8Mk2gGikIphIvVDX2BrMpeEsuu78U/+UVO52tegs2SSk42wrURAznYRaX3oxUyZRUAejy6ptfdGJ3U1e9tigQaCNUTOKIneSZH/s3vOK8M0/sDtaNQ6AUPb+pV+/V1AzGTOuj4uCKJ8ewko/1S4x88uRpitAoSgttfGEa9f9m50OFljUjTm7mHU1ItFnjR5MvFJFIx2xro53nn/DCSzePl9ZcVtJvEayNJ6t2ncksLn34A5TMQGDz66uj80/svuApJ+rqxEnr/ZNmOVSHUHRkR51w9Nv/087R0kBKhAdmpuq9OkfdjArvYcaw1WGxtOYTC8TUBI9bqA+SLKxFImOCoAJqwY3MNp61KeIpGovcvFw83XCxQX4Qf6/EjeP6G5FhYr/7n86dyQeFEpnBQBZiNQtGn8wTGZHWrxi8gnqoRzExVTD54dqbX3y8m83NSsZgHZtx0osDACKCsf3h688/an6yPlYuU97gcnPH9z+6dvuDy1tm3fq4IOjycLI61NixwpJAzFyiZ5wymrimIjdLgYFIRQloiNpt8Yb1mCboV5dfG0ufptNJVYjrmh9iRJ+cTGHW4fiknUe/7IpN64urwgQzCq2vtRNWQMnMvI9nXw1qMJiaqTc/MVUGVtcml56SP/Pyo8MlSJhGJRxUkhacc34weexFx7/xOTvWDg+csKnGllvAe52byf763+66+g++/dXbDmydz8zr8tBGE2NuoC41gByyWK74Aemxk8QQxsBD6hyCQVMRfuJm6viK0SQwpbXh+tJwQsHBRp6jUS1iJozxmy85fUtnbaJCFhB/D9XoBFWJmAymPu9mHHDR4NJVLexHeCpTEOl49JYXHM9dV9ZdKv+DJhoIYvdXv/24ng0KpRj5AGSmZptm85tue/TzNz26us4v/++3fPire446wh08tEYF0qi2EaVH6krl+etmhhSsrBAmaXLRwA1PSy0QDS2LwymTsJXiWQ2jtsEfNL40YyEdFUefsvXVT9sxWF6TGGAg2igzDkA0YGrO8T2PjMeFMRQw0oLIGAaEPNbDVAjLa5Mn7exddclRujZx0miRjFgwII51afSyF5717At7y8sjxwTTcJ/CezHZX3z055MJ5XnHqPP29/7sLz9x30ClTINTQmrrLZAue70+XPX2ljSLDfjJAE2R91JABdzEXdNQ25JtwkaoXCO5iz8pzBj5X3/hGUfPDMdeGMoEmAUEsjxWSgZhUum99Dc+/sN7Vrif+ckkRoim8f4DBkMwW6PBbz//GHIcYQw0rr8wMCo2H7Pwzt8+d7yyQkyAVtdzUuimWfn0jQ9888eLrjdTQMjlnM/+xb889KcfeYh6XUXKfOFGa0Gkd8RUs3luk0w2dMjUhFDmuidkyhQlOQSXTBc0c9SQ4FoD/U+NVfn6NYQSC9HQiV84ZtNrn759bXlQ0resgp4Qu7pIvc829T735Z/dftfDH/r0T9nFENbUBxtlpqEmbN47xsrQP+Xs7kXnb9WBF6kKewFDhTDb0P/5my8+cctouO4lXHOzgH06oeXV8Z9/dBe7LrGwZCAHl0m/f+Aw2EnD/aIZl1DS4ZQav424OlK6I3Bc2wQvqX6VN0joGoWIGlaTZpl3uuMx6fNnQii7D4pXPvf0kzetr48ttAsSS8y/yMh8aGYRRjHWv/rgLSLZtZ+/9e57x52uU++ZOawavJr3phoMiBpyP/6dq49JGXPR92bsV8ZPfOrpv/m8o1YPrTphgEw1JLyTwi/MuPd9ateuPeuu27HQ0iSO2IEyyTMioVpAgaYat1Jdi0a/QDterLex6tThDeGlhKw4xfBHnRBUMhFJhNpIQdDCroVJCz+zbf4Nz9y+trzKwgHjLJGA2JMAqPe+s3n2+m88cOtPHspm5teH47//+I9lpmemwcIAMKiVDi5WTlYnTz/LnX32gg5VqjxIGIXNbJ55/+9fRKsH1SjmuwQz9Wqz/c7Pdh3+u08/KJ2+gYkFLMRC7CDOyAUIAFPde42WprqllOmXcHuC+a1Y5q2UKiVDYiMOeH2gapp3KKW3SW/cdAw1PCCOMZi85Oknnn0UDUfK0NIYmgTaRPlWwjCPv/nQ94k7IOF89mOfu+2hR4puh81rzYmBVbEfA77wHV1/w9OPJK8s5Zsy6VrxjrdcfPbRo9WBChQwVVMFkRi4l9Of/MvP14bEmUOgvYZ/JbLqq3aRtFWrdcJLeg4zN6CAymiH5ZAGeNyWTJmGczgpdHAT0qwa6WMPP9Don6IpcIKZrPD5pv4bn71j7fBhEheS2Rj3a8xvgz/uzve/cuOu79yy283MeuOs11tZWr3mUz9z87OmSjASAWDFGOqJjAmqCrN9B9efehqdfOqsHyoTOcf+8OBpzzrjbS85ZvnAsghH8F8NqkWhR8zn137twRu+dyDr98LxL0nLLlqeZBnS3rl262Szo3fjbk9UUMSUsEVtr7lqQm41BJVFAG7sbyPixkauorwNImxrxbOvOv68Hbo6DCF/OIoBebfoiolgSuT+5sM/Is5DM7caczbzz5+47cBB38k5pq1mYCECfKGFN/W+KNYGxWBp9SUX5AwIk42KI45ZuOZtjy0WDxg7mIE4JL5myBz2H1j5kw/ew1kXJeUbVVtSyeFB7EGvEHLCBlTs0jij2VtZ9zaDAGn3i7RETNICd+rLfykXC036lbWb++pUG6Yms53fvvqEyfISB8MVAAkoQavwzRS9+e5NNz/49e/vdjNzRkLsjMT1+/v3HvrI9fd1Fmb9pAjVK1BkbcFUCz9aHw8Go70Hh8f21/OOwWCFvf+/X3nKwnB1MGGoem/eB9gn+N4//dBde/Z7180t9qVI6v/SWL/NJ2gVX8tjj6A2MM2fqIvyoF/SIUTcaL1GUGdpe/R2l1bKjWi0TyaNHRBhG0yuunTHRcfaytAzQvZfBQKx3x9qMOUsf9dHf2zmJBOIIxESBzC7/vuv/cnKqmXsATNVeG9qBnivo9FkbW18eHm8b3H83i8e9ApdHrz5TZe8/Akzhw6tOcfqPUxVC1NfTIqF2ezzN+7+yJf3u35PreqilYZJqTOYCtqRjZj33GI61EFIEs9T0jCeMmZ/SVNnO6xFLf7TgINazXJIO47LCofBlDL3xueeNFlZQvgYSf0DsBB6erX+XPeWHz1y3bcekNk5tWCFhVmMRPoz9+3a94mv756b7xWTAtBw9ovxZDgcra6OF5eL0ch/4MbFXQczW59c+dSdf/O6U5Ye2Rs0GsLBD5CnOD5waPD2a37OWS/2myQrh5rWWv4rwuIonobaS7eZQlyRR7jRlFYxNKmB6TTUEKYqX+k9tLoLMmXl/7J/OM2xIcK6Nr74omOuPF1W1sYiXIKIZSpNYuHGmUm3++6P3eE9iRPULWbxmVny93z89oHPhBQGM/W+GI8nw8FkcXlSjIuPfuvQLbs8E445adtH/vgCv7jHG0PLmpcZFIW3+Z780Qfu3n3AXDeLoWeD0diITcCCyQRFgckY4wmKAkUBP4EvaAPy5S8/zERZ2aUuU5aIGKCgOcfTBJNY8az0dprCITxV18QUiV3e+NzjZbgEyeoW+MgLgAkYMNjsbPdndx/61Nd+wf1Zs0ZNkZjNWPr9n97x6A3f3/+CCzoHD49J/WRUDAfjxaV1Pyo+efPil346yXq9LO9+/H9ddaw7eHiozGRqoc5oZuNCj5hz1375gU9882A2M6tGJA5RRSO1OFVNyTh3my64FJwRWcDVQ3c+TNcfvEsHy7W8Ak+VWJBm0MiopcCBsvE4/LpF3i/xBt0G3Cr/tzTnOGH+JPsjQjYozjj3yKeeIYcX17NuFwG7cRT+nwGoMrF67RzZf/+1t41GPtuUKVK2QNh9JsmI3Hs/cedzH3cJdDAZF2uDyaGliU78dT869PHvruUzs8XIrvmfT7/yxNG+veuZEw2plxkMhbd+193/0PIffmiXdPpWtrmltOL4YJXigMH1up2dT/Gr3jkCAPVMCHjt5NEHdW2pPLiou/YqDnUiTcHEGTcot8wNqJISVSqkFiiRrZHGj1VUO26p0SAth8Hr6593Qq9YW2dXYnhEFi8iYCBW0/5Mdt/u1Y/dsIu7c2YN9YFS0kEMkP7MTbc88u2frV14FBZXR8urI/KTL/9k8Z+/sZr3Z4qBf8d/e9rrrsj3PXzIZU5VY9rsVdWIhc3/1t/feWhV3KyzUsCl5PBwiqrXLB1mP1j1g4IclQm4EsAuA6xtaEqwqCq1JS0JwfK0VZAqDleL+lC3vgONDpOkMxgJ3kANVmxZv7FhcfwZ25933tzS8rpzEsR5mCBkXEqOAfATPzvf/8Bn7l1aHWfdHE3lhrJvkUEsmYPims//wswWDw/EFzfdufL3XzjsOr1iWLz+dZf+6Yu37duzX5yYjwWGgBcV3rbMyjv+5a7v3rWWzXTryCdK2nASXrSxHGESkQj6M7EIM0tZzg/gOdBgxVK7XSzkAY1O/Iq0m1a7mkoadX9Y3c3MLQ56u9W7SsRMhDGxX3vGjk1YmSiZWinyyhGOISaQGXU6smf/8F8+fw/nfbV6uZsdwMzMCuHuzPXf2n37w+OFjl1/66H/8dkD3Jsv1icveenj3vumkw7ueZjEmVcNpF41M4wmunWh87Ev3v/+6x7N+jNKwuKqTluqZJLK6KCRBYkICFqUBRxDrFErmVLzviT9ThZBz2QrBXWMDrT6koCNGLbNPjTQBip3jR68mhPHTDoutp6w6UWPn108uOKclMmlAGXdBUbMvvALC/2PXXfv3oMD1+uWSq4yfVNDLOxyNx4Wn7xp//ce9P/rs/vhun44efozzvvQW3eu7n20gEBNQ5nFoKqjcTE/k93ys/1v/+dd0ulZjezLhtpr4ajFJIaZwCUTQBnGkTIcLxYxEZRb4Bc3BC+rGnlWy2CVlB7ClKZG7buR0FQsiMmV/R6gdrkeDecMiJAf+lc87dijs+EBc91a4NiYJcb/ZsSc53JwVa/51L2c9Q2MCMjUjrGKA0IMohDuzX74ht2FsfQ2+eHoiVee/e9/emFx4KGJEYcaV+wHMG/odrJDi+tveNedg0nmelkEnBuiBkhlG5HS/YgIUPVmxsIUeZJWlhM56QZptsgyM7WlTGVD7LnuTqrbVzEF0pUgUVmAancfEpptMNCJzmybecVlW1YOD9gJiM1I1UAc6+6mpjYZTzbNdz/51Qfvf3RFet2IiLVlt1Dyx2MrN7l8ZDm73A+LS5/02E+84/E4tCc2dhhUTdW08N4bAWz6hr/5yQP7NOvlWkX9rYbyJqiQCB8xAFJjKFsBnZh6U4UVgR9Wy6W0igR1kb7mPktL+aAi8k5BrEzTDeUVWTMp9aXVrrQ9xgljUFx95Y6T+uvDiQUsCCixeFRfkhMMxnbNp+5m6QWzsAH5GCklmIkE7PL+rB/qpVec+ak/O98t7V4bKcFUzXszM/Oqpqq6qSdvfc9PvnPXWjbT8xZci1SatE1SFNp0tMpnmrIW8EW4AVCvvlBfVCvcFE9Fys5KSTsZymCSKzSTmTe+QxsVfWJ4RaVya5M1XZXsGeqRLfReedW21cOHXJaVctjEIqbGROKEBGq2ZfPMZ7798E9/sejmtii4VOBDwsGuPpuhDA0yR8Xhtauedv7H/+gcd/ihwYQY6k0BUu9DBuUN2zd33vGhu/7jO4vS7Xsldg6hbzZ2z5aZSyBAcgURIh7WSibYjNQj2GEzMo0HLZIzNhAnbfQRVZlwGcukpK1od7j8X7PPeAMELrkxIGYytIIAJ+xXxk999slnbSkO7NVuz3EsSQbJNOa6pxie5X2f/gVJNwR7VSrEFcsi5kQ1wpI5LhbXnvu8c/7l7Tv9gQcGXoShaiH2MDMieKXtm7N3/dvd7/m/e6gzt6WnRrw0CbJqST9EYGs552bnAQa0rF0ABBQTqA+IN8wzk0X2ajhPmOLxbCi7Ulnm2glz0osNpmZj6TTlEU0psDq1rqgBDe1MU3A/e/VVRw4OL3GWwYwDYcpCtdcxCwBf+C1b+t++7eDNtx+QmYWyHtKoKNdtNYhFBSEqFoevetVF733TsWuP3D9Rx6wl0hOXZqI4anPnHz+76y8/sYfymdnMX34Clsb8rQeNnVS6+CCwCBXr/eMfO3vuMyZLB4iIsxyqmIzAMvjpF3QyIgN8AdXI14MxB3KfC3cikUahVKe8dM8VNyS0GpfKiI1SSptU0ipsNtGLiqPKDQpd0MkRIVsbP+Gioy842lYGReAelOFzqPiaeh9CIJdn//DJu4mygNBhuskp6RUQYRj86uT33nzZ+16/Y/mh3WMN7J6IdQZoelTotoXsms/u+uP/8wB3ZnsZLj0B/V72mKPckXNRQIcTySkCSNxkMNCJV4VfH+l4FIt0FQXaFOZhRezY8QV8YX4yJcxeC4nSBl3UNcW0ljxKaBYV0pl2oLUjkcRJcLs9pErqHP/nJx/pV1cgYl6Ngn0IYnYUroH3Njub37Zr7au37Jf+jIKnRDobExayTGx97Izf/RdP/bMXzh3YvVspY5Aq1Jv6eAkKb9s2uX/63P1//K8PUN7viF5xgh21kHfzbPumzhWnOPKWzjiINS8tWIvoALQg9RRqPVySvLwn8wTjwFhFmRAkujjcEM5Bgi9RxVsUauocleklOEUAUdUbQU3eVcwoynA+fY3Ie2HYcHLO+dsvPUlW1iaZSMzXib1FGk54d1Wbme1+4HO/8MqSBdw/6cRvhs9O4JfWdxyz9VN/e9VrLhw/+tCjYKfeezXvvao3VVU1whGz/L+v3fUn//oA5/2uw+UnYMeWbKbrtm3Kut3sslOzLfME3wQ9SwsMLcgX4RlVCzNftofU5AuoJ/MMYw4aCmip0rS7VoG0yiit/sdEdrSthUON5i4q9ZOpkt5oTDmoLgcTGV79lO0yWNVagpxD54/6yhjR7Ex+78PDz3zzEe7OqDVKIlUcHFS5hckfXn/ik0798t9f9oStiw8/vChZjlDcmhTeB5zHM9lCn//0wz//m8/s4c5Mx+FJJ9NxWzv9bmfLXL55Lut1syM3ZVee0YGHlFTL8KxmBPXkJ2E8CczCZpQPGttlquac0DSIOg9o12abXPK6pU6aHaNpy+pGIH5Lx6lyJ5jioJYBrQ39CactPOlUOXR46IRBUDOzwKK1mF0we2/zCzMfvmH3cORdJ4uluzb2wC4TG010ZG/5zSdc+4enbVp+4ODSyGWZeq9qpqGJBQru93JS/1vvvuNDXznA+UxP7Mmn8rFb8tl+vn2hs2Uun+/n831HLM84u9OfjSe7GkkC9VaMQ+rMviA/JvVJ2z1IC9ICFonypqreozJBqXpY0kmRyG1EClbWouowVVOJUu346lpZMhymBZNOAUEAM1lhv/qUo7qj1QFJBpiChUv9Him7gtHtyO4Do3/7ykPcmYnyjSmtLjT3Cful9aNP2PzO37vw+WfR/j17CpNMOGRb0NDESIW3zfOy7+Dgze+969b71jnvzuV2xcl89OZ8ppdtnc/nZ7J+1+WZyx3y3B234K48U794y8jNZWoVXwoB4SEOUabWCxONryIwISOh0ZpyT1M+E+lkm/pyZLHtsGaXJIOIOEmQwalqVqX33KJoV1sTtfHHfutx/eec21tdWhQnZuA4P6q+OaETYtuR/Y98ZvfS6iSb76ulPVJMBCfiC29rk+c896z/8fpTjvZ7H35glOW5wAepZVNTVTMDy9b5/Ns/2f/7H9z16JK5vLPQ8Vc9prN51s313ObZbL7vZruu23WdTPJcnEihuPqC3ld+OkrmYIVPphSKzKngRDJLqR5FEDIDEBRTskGl70UNW3IdqVgWrGrAtNIRTnVClsT4oLQDD8muNBrDETnP5Ef6sifv2GTD/QXyPCSNIo4BY3ahZ52EXMaHB/4jX9zNWc8s6fIAiNg59iujmc2zf/Tmi173pJnBvt0HCmTOqS/CO4WQc1xoJ5P5Hj76xQf/4to9hYnL836mzzqrO9vP5vtuvu/mZ7KZrpvpuW7HZRlnjp3wqLCdO/KLHtO/+c6J64uVyDnUw5QoEk/L4SBWml+LrWpkZYUcic3kVjmmHqKQiK5TXRHjqJQFrsZsxSldKQjMSbrYKlO3CqdEUI+5bb0XXDizdHgx5mJOhAxwIYFkcUawwo7YPHPtt/Y/fGDdzS1YzWQxcU4L9SvFEy4/4X/+xllnzS3vvf8hyfPMSYDtwgVSVa+2aSZbXhn/93+5/3O3LHHedRmZYjRRydyW2Xx+xs30svl+1u26Xsd1cnYSWubJZQK1lzy+f/Ndk+rImQHqy25ADW2alg4xCU44VFFDbTz2ECaQUSpjk7Bz0vg6S8ZMcDtJ2EABJ8V5pmijCWjkHPs1/7xnHHWUG+2dIM8FIDUix1BjlqgvxSyOxyYfuP5Bdt0g0xTeQYT9yqi30Hv7m857w1M2+QO7H91rWZaFDvbYimAovBLR5pnsez879Gcf333/fu+6fQMZsTj4sexe0svP6A4L3jyX9Tqu25E8kyyPwTATu4wGI3/xyZ0zT8rvfqBwPafMMLMAtAFkygE0TPHeqJ0T+hjKHosoJtoYdcHVxJtgadIBPAxpNFAnanycgL1tKGNaeKettGyqyOfzFz5ubmlxwMJUlrqobEAEgWDe6+b5/Gs/PnjPQ2vS64ZROs6JqfnlyWWXHX/d3176O1fwyu49a2NkwkGyxDTweTAuLHfkSP/2U/e/9t277j9grtcxEogDi5GQy259cIwsO2LOzfTcbD/r97JeN+tkLstEhEXYCZNIBn3xxXMljsBknqywYgwtoi2KVZcyyI7XwmK6GqEPbXC2KnF45jaVrtzHrJx3M9VRjQ0AiGifOFr/5qSFOgN3jv1K8eSn7ThlE/bts07u6tAXJE4qwhIZyLkPXrebuBNKfczil8ebts/9/pvPedWlXX9o76OPaNbJWEu4GkREXg2gzTNyx/2rf3ntgz++b53zjogohKJeDYHI5W4wnNz2iH/JBbOrI/S7Thw7kYitxZYSyhwvDexJp+Yf2i77FpXFKLSAWwGS6GxZyLSWeVWNPhdlOYS4StOi+diQdtss8QpXHaNJM1hpqSJfAVS6+6n5mpzorVRpnim4Jy+/ZG5lcbU0fKHiGwkJYfO8x6b5/Lt3Lv/w58vS6zCLjb0Oiuc+99Tr33nBay8olnY/sjaBy5z6UrTBoKrjse9l6Gb4p+sfeuXf3PPj+yau1yMOzH3HVRe8CEiIs+tuXcrnZjbNZnnH5Zm4jMVFdhuIg/hZoTSX2QseP4uxhh5N+DFUYd4C4l/anMhdMjUNIETZ14fYKMjUkA1Pw1OuWyfjL2V12FNN7OCkMh8CKHBCeuBm8ENJSBQbvnRYPP7CLWdutv17i7wjAIGFYKYsmZTUH1azbr/70S/dJ+JExK9NTjh163973RnPPtOt7du3d5lc5kjVR66/BaaisC30+af3r/71px+59RcDyjrSFUUg71f1LImwOMx18kf2DW5+0D9n58zh1SJONyWO+lel8WDmQyv+KWdkH/+2rA1UzFu0PFNyVbG3WckUEkdLVsZ/w9o4t8Sjk03JmhAnGnNoa/577KxtjisLeVnp8FF3f5Hwy5+waX15lYRBpB6QIDJrqkTsyGDQ2Znstl8s3XT7ipmw4Y2vOfd3nrV9bnRo3wMD1+kwQwuNDS1mhaoqbZpxa+v2v2949MNfP+Q9uW7XSCxSSCSOt4g3O9jJUHOVa7+1/+rHnc6rY2LHJQyr0YRAFd5oUthRm/kpZ/U+d9MyL5hpQVq0tGdgVgMtMAqab4ZSzK6twV8PIZoSEgrvnU0JSdRa00krZos3Wteduak6K0I69Gc8Zu6i42Vxr2YdByOL8D0xs4EEMKNC7bhjNv3Zv945ngyuuPys333JMedvw/Lehw+yuG4nXOsIlKqpodcRl+Ortx547w377ts7oTyXrmhVTI+6+sIsqIsaoUIF6fR+ctehHzxw/PlH5itDrW0rEYg19iKQCK8M9LmP7V3/ozVVFS1gnsURuNTeTVWPNE4LEopCCdwSZKuWMBEpKmv9FdqftToiyxIKbyyPkgI99WC2Zv5teOllW/zq0DgeMXHkwtQCZufIDEQ023U3/+zADx/Sv/y9S65+7Kyuru3ZPen2cufI1FQthMcTb5mThVl33yODf7h+7xd/tELsXK9rEKuH1kg1ywWoRmvW3CHJMpqM//0bj176mhOWVlddFlpxjIgqSYKwtKsjnLY9u/zM3jfvHGfzXmN7BcfBqdEaWCluBBCRaqhsp5rJ3KzjYsNSLhECFtTUgONGGb/WQuRp6jsa6igQJh3r0cf1LjuRlg5N2DkgiLyTqnGoywuripltmnOTvPf+3z3jzM30yO6DLs87HYnNRkwEUiI1bOrz+shf84UDH/rKgbV1km6HiEubUzJ5SsqiiCOXM1H0rjAyD8usGHHeufFHiz9/znFHdWQw0dhMHDTowvwOgImEsbw8ev55/W/eNTQtmISsKsIJoLHaGgE4z8RMVvrQuKnBGiMOHeNq4motXF95UaYMCebSEOJtkp8YaLTX1FuQiOIx0Vhf9IRt2Xg8UcoZoanNACtMhIicFeQcmLG2ruccmY+Gg4f2UqeTcWwNJgsKNYROLjM5f/Mnh//hhn33PDKmrON6YignTZXswXL1BX4ye9r5buvJ5EcimRFDCyLWtYODe27K8nwyHHz2B4fe9swti4+sZZmDwXs1sPcWlaLMCDi8qo85snPOyd079o46Mx2AQRLmMYf4rUKKOPSztYu9yYTq2kZzOvk1dRFZPaiVa8CnUsFuKgbVc0em0l8wkU1s07bOVad1Di2tgEXVQMJcRe9MDBGGR5ZxMS4WJ+oy55ypV3FCxsLkzVh4YdY9uHf9H7/w6Bd+tEKUZb2uggzx4FddAgiTQksFZen0QWLc8WbQgpld3g0zF4yYXefz3zv4a088ouvIg9TMQN4HEI+ISRVeYcyTsX/uuf07dk/QJaOMBGyCUiu9ZExbHOxVb4ElMmCR5soAN+iZaDEjsiaQVvoAbkOjJTFnSgGyJGGLkI79s67aPIvxvgKdnIyZDQWICSzhslvYK+/ZOc4cqVcwhVZFYkwMs30mwse+sfeaLx1YGZh0OsSi1dRJEWIpE/pIVkxaqMAuJz8hFs66cbiPZCGZcr3u4oHhV25feem53UcWJ0G8vJzcBdXgCUDA0gAX7tBjjtRHlybSBVGGekJjKACGFE6r4a2l27VpqbdIn02EptPxO9LoZWoIdifIxLQ7SZpguey4627KnnFm5/DSugjHpAmkaoU39bE8Fq55qOUVRXCAZgY1eLXNM+4XD6//9vt3vfPTj66MxPU6YDF2YBd71cnFUZzs6pJZqZwGyRAIPMxBXh1VRVMciMl1rr3p0IhzBry3cO/VYmdU+MwgnnhQMX766cDYM3yEIkrCTzzs5hFlzQKpO+rZJVVcMNI5dUjJ9dUaywal+pQfmfZfpKOeag0xIiInhHV90mM3Hdm11VEAKSksq5mF39Hg91gMbGA1GIVVoELhiDoOH/763l9/764f7Rq5bo+zkNlmXBKnqlE2qGh9DTa5lAQH5piXKpknLcJTG4nrd++/f/j9+8YzXfGKiA8Sx2ZAi4V3ET488JedzPNzqpPwIh7QRECzGj1Ran2G5LKlhDqlQAZqSZyxNAXO0pbSZBByq7BJ6U0CEdTIzbjnnN1bXFx3mVOlkNoEjCR2Yik0SjmQqmlR0cRtriuHVsdv+/AD771+3wSZdDsaicpSjngUIgFxnBKeBj/iiBMd/1KxpmIMwqyeESWORD7x3cWskwc0O4DMqqalPpeB1DCc8FxmTz5DMCpCGBEV0moyglagJFdG3hRoWQukh5abi1fWhNMeFiQK6K3yfIp0J25YmDDSC0/rHtsvVkYaaLCloBUZKPo5kFd4hQ+kHYIqJoVu7vN3715+0z8+eMu9I9ftllxBB4rdhwjkuDAlGMBkjGKCYhz/naxDi/q5/ITVM5ThI1pgCoovYhDudX7ws6V79vu5nqiamZki/q1BDWrhWuDAsn/iSZx3LcgVR/JM3aNi1ZiPsmvRklSr0RCEttQzV3hP1pSoSWPS1vQhqv1xU80AADl69rn9xaV1CyG/sIW4TUMTObNxBZWAQSUGeMS8+/fvLl7z5YMkuet2QmbLZUNoCb+WnxjIZjblC9tLvgUTIC4rBsvFyiFignoEqQJmjmwGhfrSZwnYZZnzQ/7cj9fe+pS5g8vrmWMiMpAqqRGIojcGrRfYvkkvOF5+sMu7GVZUZJ0oaolqqlpQd4yxDze5ENw48OmyAhGKSObpojG1nH9ZIYaT4w8d6Zmn9k7fKg8/qt1uFvjqZBpQRmLOJPhEFWYIZ8IKEHi+L393w97/e8uq5B0SUSoHTLZ6Y4NAEQv8KN96YveUS2y0yqE115Tznu25fbK0n1jgCw5qrhGpDzfcONKPhUXMHPc7X79t+Vcumu048uWiezVD9FuBXGvA0kCffLK75T6LgWqjU9pgVhatrD1eD82B6q2zXDMRIy2lNYKWqW3IShyj6hpE2XNDRETPPndmsDomERi8wWsky3ilKOIAqDevqmrjwqtZJ6e/+tyj//eW1azbhUjQgAEHYQZHJAgiMamUOwsJ2/qKjQY2Gupw1Q9X/dphm4xD2BO5aVpQeHsLAYxHohJqJJJnw5Xi63cPF+byibew+ogcyfiv90rA8rqdsIUes4NtrEJay4XXzdKNuRANalpzcAKqvphKURmpXlDdbMQbqIAmM+5Kkhyi1OHEdhzd2XkkL64VRFSEPgiQRmwcoS2uKAKPFaFPqJ/TX3/u0Zt+Nsh6PU8CduX0ZwkTccuedK4D3bISW+X9MTpkCdyKiFX6cdDShflaW7RCx0RYBBDq5NfdujLwzBRXv4xEY/wW/pAxDUfFk05CZKIn887KtUZM0FARAzGlnk4bOWauNeOmabZtfie16Cel9xcib884Z8aPJ96oUJr46MS07Hk30MRboVZEwiyOmM/e99VDN98zynp9hTA7jgFPtBJpPsm1TIlQBFwIpvCTuFTFGDHQ5HLp0xBIUc5VKoUjCSyum+/bO7nlvtFcVyZFRJLVSpmPQFsVVrPltcnpW3T7ZtjEmLTVOYoYF1tj9admWaTCpZWZjfkJGtVLNNrz8Et77MOZ1IltOTK78FjetzQJUYSFOCcqkJC3oEFDAJvxWGnLnPvX7yx94/a1rNvVRBGglKSKDKxSfSFRq4rNKkLqg2Q9hVAnSLmWUnNl5TZUaCOrsDHgJag7sKMsu+4nayYCQJW8xgJNECn2apNCDVzAqeKJJzEVvuTe1q123NQGrXmfjQmVdTE8bXAMbiDjpgp+wp2b6hRMG1ADClDoE0/rYTL2RkFIRZgLBYidEDRMgyEhMZD3OGohu+nnq5+6ecl1e1pDaZKOEoMZ6aRcL4kUHXHs8uBmUYzJfEi7yHzSFEEAAlmThVFN3IAmStXxnhmxdPM7d49+sb/Y3qe1UdArIzUKhRoNdDdiYl4a0ZnbaLaPgYIbIki2gfrDBvJxDTFVpAPZyjC0LR9dQXeMpkpH8vbmqTcvF52QLa6MmcUrmOJIc28wUBZmqDNBSL31O7JvafLP3zgsWW4U52qHHpiSFiBQ35nf2j12p5mvC0ku05WD64/+IpTCYd7Ul6ePCJ7Ml/PzjMwzKUNC3bbs4EswsnLsLjsm5S/dPnjjFbNLQ89EXqFgK5HwmK4Do4lt7vPjj3PfvFclR1nQUUqniCWMoYZcQ13R5A15EpK2tlQ97i28IsXg4lIJYayXntqdy2w4iXbGzAofCLLwHoWamkWoB9zL+H1fOzQqMnJZ0JYLhxE1rE8E4/4CzWxFNofOJupspu5m6mwm6cbJgyEj9RMK4Y2fmE4iTZsDmdBQin2jVl6nBmpU5nfczb5/3/jgEBnDa6gQhLNfEgCMCk9eaWloZ28zl6lFQgE4HWkQfYCRWdNQox4Imja8JixPQTU0r8yUk/gVG6o5MZMZuS5deqI7sFREnMfgLd5cr+ZVvZpXqNHEY8us3PDTlfv2q+vmQRCD4ypwHWOFBTKP8QB+ZOOhjQe2vmbrq1aMo5s1hZ8EFe9AGyH1qMeBRmdYMsWTuLB8ouAHSATkJHOTIb5973i+58IGmJFqDLWC6/BGxDRSmu1g5zZCYXVQUzneUhG3NdQETWwzwT2TwJjrw1/PKuJ0Ms8GjBZgYo89IZ/NdGVsIPJm3gIzUipB1mBMC2/dnPceGl7/k4F0YtMvBw3OYIIikaS8BxW/I8pHW9JoRQSNrhUe3puqhQEOJdGDou9FGD0W46J6hieVaupMzEZCubvx7sHIM4G8xpMUAQklr1XUzysjO/+YKCtFsYPA2i0YjKlZwHW7KKUjI6tMNg2CuO7L4420ExPSsuCKUztLa14iql5iuWV9IsTyCvKG2cw++cO1QrMqxIT62O+gBayAD62HJVddi7jKWkAnsAI2iUfELPwwfIj0FVZUoGxQPySLaurxv9BK5qLRzcAMctJxhw7rrQ9NZvvOx0vMauQVPoizh5wGtja2I2bsuC0MjyAinvh5NLS521rZ9dK3lEEBZNzy2byBIl1S8WFhtpGedmx21Cw9fMhE2IJUKMgITkiEyUyJXJ4DtKkndzw0/NkjJt1exCayTr6wgyWr431x8ONieW9AGeELaCEiFpvHANWyebmCd0p6SNJrDhhVjFooGcWwilu1JEQ/LCBjErnx5+vn7pgLbLuS608G0lgkMBiEaVLY+Tuw5xAi+AMQW81iaMzr2Uj0MxUOKL1B1v6d9vzZcj4QGl1Kl57oDq+ODVVmVPGvJVQgRYTUiClju/72IUlOzMQOgLiOzB8FCgx1hC2x9RUcfiTWZv3EfEEiFCmkdXsIQGQeWtR1balGNHDJ0dRyPgElMC9Tw8JWrcciHXlgX3HfwWL7DC2PqDJBRiExjhplDKyMcNwCb5mzw+MytrdmtaoJ3tSwGqreO2rOfSbhdLbFhnPhOR0lTFbY0UfKiVt4ed3ioGQDIVaQNdJthMBqmO/y7btHew6zdDIjqepTKIY2Hth4zcYDm6zb+opNBtE9mcFPyMI0hkkwRzCNeYuZ+SLoWgKKONrWYooLi5PFSqwYaI6tgXKzHlL2mPN3d41zxwGSA5ECvoRFFRGcCG953g4mD44D/VCGACBsqCPJ0wIDlAjIS5ZlCRF3wwlkdVcNE5Hi8pO762NvIGbyPpyXILlPBLaIJiJwsG68d0wur+eCsoTqaNXVFqOayMVmmIcWpfUPiMKEzMd2HPPl+lrU1TVfZ5lxnkys1tXDr9KhFSWMXC2HkXDOt+8pDg/RcWXlDuUEpTi/jRTIhIcTnLKV+z1ALWnnrUb21QWs1mRxak/UICLKXCb9XjdexiqQaLbnIamRqcfCAp22BStDH8qqARhXQ1Va8goFvFE/p7seHj58mCR3oErnMAFt4kL7hhOGQQv4STkZJpEgQZkBBqUkDe5aqzAUiIMOS8do5e/SBnIitRViFucndOvuSTdjH1a8zmComicGgzfqZdi5DShMOCnIpKpgrfJtG1arF7nb7cjCwiZSbWi2NkfdVyLhIVK7+HhRXxRKVDKerYz9q1gwJJDO9Du7CnJZi/uOsMTVSTcP81G1NQ4rLMoOIR//EIsq4Xc96vgyjjkpn7fqFdXqllRCmASKwFFVLSitEJgoz364pyg0Ek0UZSRMdQs0CE54ecw7j3IuM9Ogrq+N6RCUEga5NV6kkVypLWyak+OOPYa8D/0iLaEalIpIVCZf3T6dfgQfHioRqUE4posWEdCApcB76wg9slQ8GI4/u5BzRZo1AD8mXxr30OxpPnzSkrLsgxhDvCimVC0xLAAScZ6nJtpUZd9E7JVASNB9VUMPiUI1bSbh1TjJZGUV9+z33YwLb2YoFN5iK1R4Oq8ovI4K6zt/woLCgxsN0mkpd4NBSKije2YW8v7YY3bIWWc+hkjTYc3c5MXV9JVCH3+c62c28uQYmYCBTMgJMSN3FP6cOe7k0s/pBw8WRI4lgTlLzfZGGskMKEARsQnHHEYMClNi6g8GYtdAemPjtuO6y1livlbVbEXY5Yk0bTqPyKqx1cRCTm59qNjUl25O/Zw29Wi+SzM59TKayWkmp9kO9TP0nHnTS44lx9Yc/hVHodZC27W0S819TpqCi507z8guu/TiD/7TB+tor+xvQk2WJhYxgHM+es4ODczM1ieUCQOkgDCJsBpEiIjNKBd6cA33HBLuduHySvE3ouHiGGBxkasUyQ1E/U0UlfNALi9bXoUAyvuUdZkQK/XSjaNUQcQCl9PcVopS68wuJ6phCXKOOsJclf+yuq5iSixMefDM3JU9K8W3dvn5rqiJY6jBGxVW5bShhs9EnAm6vWxYCLcI5Cw1VtEeXo2GbCvxpRc/nu+5597zL7lyOBhxJg3yeqVaX2tQQqAJlgFOs+qSPhpllAByVY23JHRWEu1ozlNLpNIq5Zhapi4Og2Iwx6GSTXZMoidhZfRdJzFlQUYCvFhzFkrGeVlgK8H9wiJi2pj4lyiWVF9maStFvXCcqkW3xnJGWh3DrNft/Oj7N8rpp536+AvP52JN4oSJui8etQYxB0lXI2dB1ZkF7IwFHDviwkzAKH7kHDuXallyOs6vJmiklPoQElYt4ai1Cuvxd5jWRS45k1Zmg1KPMk4IUlzuUz1pqMEAqUqf7LpOcpacXIddhyVn6VD4joQvcwr/VpzDekRsOnmzWbxKlSLECRfDC84/98wzzxBifsVLXwQUAX9PCYxNmlA9cb6WcaplRKvxtFVhn8HcbDFHYy5zQz1katRZIjbXEGsrHR1XzBxD2c2bRDtNUlMDL6uaW1Ip+HhmOXDlQvOgopx+EJAucAz5QBXqNjU0FiXmmhzlBIiuJ61g8rKXvJCZ2cwOHjp05jkXHz58mLPMyrFJqQ4Bt7poAvBTSWq1Z7VxQgJDyStJwcF0qlVNtpjqNuYmFXW6S6T2W5zOlG2zmRq6ywnBNubvrRJK0j1BCZSAFKFJW903mJ3Qljmq2wIIxMKkOjc3+/M7btmxY4d477cdeeRv/cbrMFkVl8VZJaBERLESi0jHaZfyua2usdJ6MNdC82hpejQmSk79uR47Y8mZtQ3EupDKuFcFMkwJ9VBDxDTpVeemji0CnZYTPkCqJDoFr6HW9gFa8zQaG1LtMRPBuQyTlde+5lU7duwoioK998y8tLR09vmX7tu7l/OumTFVPQKSPjeXgoKtYQRV3pe0JoRzJ5yIJicHMQkJ0SKRpZ1SqZTLBq2ZBPuldwWtESyc6iw2MtWU9tcaSFR96OCluX0FyxNZK1rxxi9XnmZmUt20MP+z276/Y8fRZibCrKpHHHHEO//qz1GsOZEa+kkKY6Xud21mK+kibmOpKAtPJXe+cgW1zlD1g1berWqqbtBR30hpEFNDK9uWo8FqBcqqTvVNa7CPKdUOq1VDp+4NIuBaiW0kEmL1nWNq9lpzE4cGCHAus8nyn/3pHx5zzA5VFQnTW4lMLcuzl//qa//j3z6az28riqKK2EAt2crE7LZkkZOIMr2SzI1pi3XBpooCy99PYddm+1OrpoG2hW10eU5VZMsG6FLxpTGjKCINDSdUoZW2YTBZq6E3OfulYUPqLirDm+W5Hxx82rOv/vL1nw6rT8ysIZUHQLy6snL5lU+/8/Y7stlN3heVAWlQQ9syLLXUK1OqZ8OV5Ep1/Wt1yLIEjIQTVqIglcBOopKDSjOeKmH3clQgtzt/uGUlmiJSDVWS6q5bcx4buDVTsxJQqmw/NwhXpcmlhv52clBclun64Jhjd/zge9865pgdpioi9bwFFgFs85bNn/30vx99zA4/WMnyPFHp5+pIMLX0CsDUFDqgekwBp07W0nY15uZogVKurm71ryb+MBKVtbZkIDW6Vmo/Twk+hMbwiOmiFdJsMkb0CXKMJLzdaLRCjeJzIzZLXtxlmY7W5+dnPvupa4899hgtV5/rgReAc1IUxemnnfqFGz6347gdfm05z/NGtjk1WiPRqATzBjXMlrnmRDEtqcptOJQMlZ1CPSUNxKm6bJV+N4b3lfh5gm8BTVrnVLxYOzckhyvmMcGbTRPFW9EnB52BtnQbZ1mu68O52d5nPv3Jiy56XFEUTmo1Wkl31jlXFMX55537za9/5Zzzzi1W97ssY+YNotvp7huqs7QGt3yjbrMNBByZqu7TaqAPkJijRm9JQxsyKXk0m9WBhl4hNsbnk4+LjZ4wmr+yAb8KOuoQJZnu3hwiz5LlHb926LjjdnzlK1946lOuLCZF5lyDFdHa1sy5oihOP/3Um2786q++6jV+7ZCNx3me8wYhIBpigM1bmsyST3kyoDRkm7pRqE47qBF7c3tuLrciPbQb3VqzKDbSH0/xGU5o5CnHIRHlRN2ekhirDaxC2Issy+G9X9339Gc+87vfvvEJFz++mBQuc63rI9NHO8sy7/3mzQsf+z8f+tjH//Wkk44vVg/YpHAuC1I/qT4TJ/gpqmwoeqLSOlWat7Wg3NQ0vkaCVgb4FXyNKZpHbS3KoLBpfDmdi9yK9ivCVlUynhbqJDTl+tNzTw3GPBpInYi4LIOaXzu4dfPcu/723V/64nXHH3+sL4osc9MM0hgFbWCDAQAuyxYXD7/7Pe/7wAc//MhD9xNl1JmRPOcyNwE1uvk49stxQ+u4GhOGRjE8lcxOJ5QiIfOhQTKOpqCZAZY94FPj6hoK2o2ZHk1tw+bod671CluzZTcwAjUexkyAFgVNhkTF5iOPefUr/9PvvfUtJ554fJjbJCU/tTnri5MNaGGuFISpNLjixcXFT3/m85/45Gd+8MMfLx88RGREjrKMnEuFKtucsCQQBE3NFK3haCTheqQF17OCME0r+P+b2seJFkn9ZOG7zGhgfNymIyc5DjYenNDcAjNSJVVCQcQzmxced965L3rh81/2shcfd+yxRFQUhXOON5QQCo9sVQMJN0jU5WgQIjM1qyKi++6777s3/+D73//hHXfevXv3Q4tLK4PhelFWlRPMIgWyytibOXLxInTc3oD2qANK5EOa9j5dnOR1WtWPNOSvDKVtMFAhGY3Wkoif+lBlzsWcOdfvdbdsnj92x9E7z3zMEy5+/OWXXbpz55nx7BYFi4gIVUpYNPUxmf8f7j4An0WkFWwAAAAASUVORK5CYII="""

STRUCTURE_PYRAMID_B64 = """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0TmicuTkz3nNnvOaPecke85o95yZ7zkz3nJnvOTPecme85M95yR7zkz3nJHvOSPecke85o95zR7zmj3nJHvOSPecge85I95yR7zkz3nNHvOTPecke85I95yR7zkz3nJnvOTPec0Tmj3nJnvOSPec0e85M95yR7zkz3nNnvOSPecme85M95zZ7znj3nIHvMMBvdD+zia8JrGH1dgnCiNpXaU2lNpTaU2ldpTaU2lNpTaU2lNpTaU2lNpXaU2lNpTaU2lNpTaU2lNpXaV2ldpTaU2lNpTaU2lNpTaV2lNpTaU2lNpTaU2ldpXaU2lNpTaU2lNpTaU2lNpTaU2lNpTaU2ldpTaU2lNpTaV2lNpXaU2lNpXaV2ldpXaV2lNpTaU2lNpXaB2lekEPrCfaHv8A/wAbn84H2+twSQ+tVKlSpUqVK7FSpUqVKlSpXYqVKlSpUqVKldipUrsVKlSpUqVKlSpUqVKlSpUqVKlSpUqVK7SpUqVK7FSpXYqVKlSpUqV/8zf/2gAMAwEAAgADAAAAEPPLPPPPPPNPPPPPPPPPPPPPPPPPPPPPHPPPPPNPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPKPPPPPPPPPPPPPPPPPPLPPPPPPtt+PPPPsPPPOFPPLPPOPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPJfDhNDwe9royIybrYcl6OPPPPPOPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPLKRrVTO1PsSwQ6YW7M57ksHPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPNPONPMOOPPPPPPOPPPONPPOPNPONPPPNI9cMNNPOPONPPNPONPPPPPPPPPPPPPPPPPPPOzCo/wBKqbnb78sfoP8Ayu/xZ6mSjehmB3erEmphEpkEc1pRY9WHBXWj2h3888888o8888888ccM88M8s88ccs8MsMcs88c8sE8sscscM8s8M84s888ss88cM+8M8M8c888888s88888888888888888888088888888888884ve88888888888c888888888888888888888888888888888888888888888888888888jBzi8888888c888888888888888888888088888888888888888888888888888888884aZl7088s888888888888888880888888888888888888888888888888888888888888/2LC5t8888888888888888888888888888888888889+0wx0+8888888888888888888oLeOBojc8888888888888888888888888888888888v7lkqjIz8848888888888888808WGWx/pJt8888888888888888888888888888s888888oZpcUp0w0c6meOOOGuOGKe+uWoXm+jjVOIV8888888888888888888c8888888c88888rmk7SOlR4O88888888888888843B8nHsB8wT088888888888888888888888888s88c8888Ec8es888888888888848888i/+fOF4eeKLR8888s8880c88888888888888888888888888888888888888888888888z9puGnpoQ0xd088888888s8888888888888884888888888888888888888888s88888s7SUxFZtPNz3Lf888888888888848888888888888888888888888888888888888888rcejz7T3Tnv/KVHX888880488888888888888888s8888888888888888888888888888NLpV5h3A/BhRBtzv8888888s88888888888888888888884DjQ34r/f188888888888808zvrNbnHbRNZXQwV4888888888888888888888888888889AGEWShPqeq5Vx37z9/wDefbu8McYOTerRK7IrqFCtPPPPPPPPPPPHPPPPNPPPPPPPPPPPKxUfzydPPPHfPPPPPPPPPLzP86cR0aFxyZ3DljAPXfPPPPPPPPPPPPPPPPPPPPPPPPPPPLhVFye1PPPPPPPPPPPPPLDeohmnICxV+6pePunMOLHvPNPPPLPPLPPPPPPPPPPPLPPPPPPPPPPPPPPPPPPPPPPPPPEQpw68cVUAxX7i37g9XfUp/PPPPPPPPOPPPPPPPLPPPPPPPPPPPPPPPPPPPPPPPPPPPPJyST396DWccVJ2v/07WaAVdG/PPPPPPPLPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPOLBidkv6xn3w0tjCLyvXZ40XNvPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPLPPPPPIjKVXqRbXQe4ik0ixas7fWlSBs/PPPPPPPPPPPPPPPPPPPPPPPPKT/ud4tfPPPPPPPPPPO5Do7REcdTTSgh63kynRRKodbVFPPPPPPPPPPPPPPPPPPKPPPPPOcq5vVD/PPN/PPPPPOY4pm8XfccU6dIMFbJODXxhA4/cHPPPPPPPPPPPPPPPPPPPPPPPPOwZ2fyrddPDWz37972TTTQkzz8y7+ak5YerJj08HLno6wjPPPPPPPPPPPPPPPPPPPPPPPLjxD/YaU7vPPPPPPE0GPEPXIjCdSWI1MwbY/APfYXhnr/LfLPPPPPPPPPPPPPPPOPPPPPPPPPPPPPNPPPPPPOxPjvoDDJFLhXVtj/F4VjGVWVKvoENXXPPPPPPPPPPPPPPPPLPPPPPPPPPPPPPPPPPPPODfDOELkvkirLtK+nvAMBCUu+zy11EEOnNPPPPPOPPPPPPPPPPPPPPPPPPPPPNPPPPPPPLQhaJqMiAs+70BJwy86x2N45xx3OAWex5cvPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPOC4mcfEIOMMPNHMMGPAlilBDDNKDGrz43x9vPPPPPPPPPPPPPPPPPPPPPOc9U8efFbfPPGtmMHFTZXdaEMQXfEOI58KcTTWfaUcUs5/foPPPPPPPPPPNPPPPPPPPPPLH8onf25fvPLBnOZURTTUcU4dcQxnwLeeycx2cWnbT08IAgs1PPPPPPPPPPPPPPPPPPPKxeawzm6D4ETYZTTGsMAtoDePsMLMYt8v53MMMMNWMBXadTTa+NPPPPPPPLPPPPPPPPPPPvfz7vz/PPPJYw0TT43LOsMMDNLDDGIZCzzbDPIARMNKESQQXwm/NPPPPPPPPPPPPPPPPPPPPPPPPPPOO3f9+fT/f4QBCPQQRKQic1PecVYQAfGAAAIAQPDkdPPPPPPPPPPPPPPPPPPPPPPPPPPOMRWvNJTcNKFYRQQSTDTQUAIEHAWSTRTZTQQQSRRSyC9PPPPPPPPPPPPPPPPPPPPPPPPPKFHGyww07w/URUdzWYQUUT/AH1FlG33VXGUUlE01++srtTzzzzzzzzzzzzzzzzzzzzzzzzzxxAQAQABBDCBAAACADDDCBDDDBDDDCDDDBADBCAQCizzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzxzzzzzzzzzzzzzzzzzzzzzzzzzzzzjzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzxzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz//EACwRAAMAAAQDBgcBAQAAAAAAAAABESExQWEQUZEgQFBxsfAwgaHB0eHxYHD/2gAIAQMBAT8Q/wA60zCTIXs3tOMPGEdgQ3uK02JhoTraE9d0E2VMBCtRMbQis2kN24sC2BnRVzE7ZrQeFTUbNxYCaOibYjHr4i1VQk7WJI9hJRpHUNxuokuAjeKGI9RJkbINsbJ1COYiNtQhQ6qLj5DZOojaaYk0oUeX+AaqjEksF4GyzIo8ytCbheRWJulYszErG8CsrKysrHjCwrKVlaK2UT5jzxEylb4N4YGWBccytlZcYJ4CKymiMisxKXEySKV8G8Btid/2DMbExb98zEWtk/fL/BpXEIU2bF/j5fkQ9cmK8/2MaP8AwWEvI3f6z6ccC8M3n+/X/ApjxZlwr3eOU2zM7XgiwutkKFEn5NfSi0mtjUwfBAkWDcul5Uds9DCLE2l8u6204vBeWr+fvPjkany16LESluvbDD5nMPN5fr08vBPq/sxbZo3VsNJZKK9RrqoiSXmmjuCYlpQ8xJkUUwbSSerQiriYsUm5hhcRXHthPBYLn9rywFnJeDIcW9aSbpUywkleV7olLlm/IWkRLg/qb5fv0HGWbla1mfUc/lP64fkSmgxjtGa8veHgtK8+FKXjLF0Z5bcnT+cP84f5w/yh/lD/ACh/lD/KH+UP8of5Q/yh/lD/ACh/nCxDE90f2epgxqP7IeGxIUoqM3m28Ep5+eCYwOrZdZJLrOXtDcDqP7L3z4ZA1F918/Ua8CfDEzXBsQu54C6nm9EQeyRNJr1Obw25xYfTG+YiLrY9skPJYpPfm/Tzy44X/Yeq+/8APB53RAVWxCM9d3r75cGBkrSfPHlvvoqWtbkkk4ubdlmOLwpEmtszeWucxyyEHOYv5/rsaxGWz098hzXGsPGrC8FgvPV/LL+cXLjxJo3v5EiTzP3psJjrybdrKXt9j+3TxnWx9tissFh252H1NTwNFj6rR+LozCTfJtYfLmX7D1L9h6l+w9S/YepfsPUv2HqX7D1L9h6l+w9S/YepfsPU9z8hnA2ubbw+fUfi2e5M/wAfHy3Nl+O/sZJmxFmY15jZJG7Ink9xwMTvJ4YZ05oVNNPDAZWmGLVxS8iTyfnkPkyaSmOGOvkcvysuM5wXmrHS49PisaIWvXr59luKsestZtkUJaOcxfvQR7FLR4dLV6GFXaVv1aeYxo+/IWiwqJLimslGnsidDVdfVIR4c7jjjy5QQ28G02WLuepbTTrUzw6GN+pivJwZrRpLPHDeHyjLcMpZzgtSKRJdEPbkp8OSSQSRTUhywWXn+u01qs3l79CLxPo1qtfmISFELjqp7yGS+w2WOL58loSHz18+1y4efn++/NwpSiZeyjbST+GoZjEnIXazwwTDPFfsQRFNc/mLC688R9CzJaIhRmTqnvIwtC9ppyGOOYu/QhCE7hzMeXl++29jLB9vxwjalyEdOCEP0B7NR2+dCz8v14ixejXyEklF8D+hSacdPwhEmS7UGiRjH6dPLw9GP3ixf4N43DfN1G6bpvm+bhuI3TdN1G6b5um6bqN1G+YpYMV+B+HRRmzeN43jeN43jeN43jeN43jeN43jeN43jeN43jeMGea8NQlY9zdmlLwpS8HJUxCrEpSlL2JITTVXelPfQWalY/Qz8chM11hnY6z5lWRSOfKlTk+Jdz8G8LwVbiE1AxTKcKXhS8Lwti70p76jZJwnmVmY2/URsYuT5DmLgs/P2xxeCWjmGs7DtJs+2hobbdfClKUpS8KUy4eBxihtxEx5l7d4NUgpCd5eBSlLwpeL9BsDYGwNgbA2BgzJFLwvC8aUQ1YCy6rFceCGEniLE+9TKKUpS9rGOT71CEIQhPg5Hmy8bxpSl4R6KF3D8HqmUfV/kycF4XhS8aUxvXwduYlPRoUpeFLwpSlF1kxJeMGS4xJJRjUazEC5ON43jeOZ5PwdaJ4m86G66G46G46G46G46G46G66G46G66G66G66G46G46G46G46G46G66G46G86G46G+6G46G86G46G86G86G86M3nRm86ECurwVbshDG5XMr5lfMr5lfMr5lfMr5lfMr5lfMr5lfMr5lfMr5lcyvmV8yvmV8yuZXMrmV8yvmbhXzNw3BICEq8Es+p8dpEoxixCGqhpEnxoUXS7s9mYZKbt2hMwTef0E210vlyJTTISNpJsfsYaa5UanI84ObNqhImU+87CGuMZtrwnYnwFIMa9IziZhHrSESUufanYhCEHo0BK117qhjGDdjRlL0a64jSRNqqMzl5PoIbZfqJEj2G6+dI560aJr3jexg7JEIQhOEIQhCEIIXveRDiUZF/ITA1v6CdQhCEIQhCEIQhDHmT9e6spSlKXgyrBOf6E5voTm+gyWrIQhCEIQhCEIQhC5BkrkyQzofbQYmbJFPmIQhCEIQhCEIQWBibzXdYQnCE7LcVY14hCEIQhCEIQhCENcI9giB1QEIQhCEIQhCEIQhj+gu/STqQhCEIQhCEIQhCEFg6haQolKUQ8cSEIQhCEIQhCEIQhiHNd9eAzMmbJsmybJsmybJsmybJsmybJsmybJsmybJsmybJsmybJsmybJsmybJsmybJsmybJsiwiF32EIQhCEJ8MAJwTuAAAhCf8AXf/EACsRAAIBAwMBCAMBAQEAAAAAAAABESExYRBBkVEgMEBQcdHh8IGhscFgcP/aAAgBAgEBPxD/AJ1tg24aav2YfaTNN+cOmpOBqXlDQVBpJscEY0s3GlYrJEk5aENxCk2JUikomi4LC0jQie4oNzsJSlqRKSNxEYWW8xaEMQgNBN0KaUCZAIp0DbOQpKYwa2Y0sgpohK1DQOmwpJpioLCWUFBkahQQI0MnIiVH/wAAm2lDGl+Roal1IiaFhCY0pSI2aEk2GlA0LEQuhCsxKrIEIgQISFSSJqQnQiliEhIyEtiJ2GqQhWoNdSAkkzDQlWo1NblliCsQIpI1Ww0thoQomDcXIVhpLYgskiWPQQ20hIknsNR5/PmKeqFy7/8ABuhU1ZFZ23E5/wCCo27/AJrVF1/wK3MOa2rUJsJQm/kiF2C/htJS9WicCElCVtu8LM4fnWyih4mS38lT5KsbdCkO2o/ZaiiOrHUluiGpZVogTdY6/ZY7bt9F4Rbw225emNlFrBFDqJtOUIXu8qjVWTYR1Lj5I6lx8kdS4+SOpcfJHUuPkjqXHyR1Lj5I6lx8kdS4+SOpcfJHUuPkjqXHyR1Lj5I6lx8kdS4+RLe/18lJVkPdwsJqsSSUISgtdlpe7PyNOGQrDgsFECSHAybEkO/gaSrvRatpS2UFjYbSSx7aT7FTXXk8vwjaSljH6IwyNgurKm6BEit2GLQQkrzqJQ1aj3MQJN2Ehk37W8/HnKWMMdt3bGTQpCebsQl0uonX89D6kvY+pL2PqS9j6kvY+pL2PqS9j6kvY+pL2PqS9j6kvY+pL2PqS9hhX0solX8dRebSruUXv+BuXL71UqiJdij9/wA+PQjayGVmkAkbJpJTLVGsClIajZqrm0G604JpqsMV0mrhOKN9Eya4vS/p/ohOU0zTpVRt6nW4mJik9JGRLpvFKbT3qEljWrZRenz2Um3CFSq3ZL/qvtuxWlSXSaKape4krUt1Vr1iH/St3+HYjRqWuo/T4EJK8cxuiSMbRRp1blNZdCXlQhQulm6jwi7RSlOvWRiSlpNI6KLbEC01BzavOOo4lcmqo/VSQxSx2pXEn51RFbzE9JHNZzLb5Yqtuf13cACQADuSWVRrd6fPajjSz1+/0k7oUlOkOqUdUTYlj1Rz9vsLgutVl0ounV73I4tden2mkditNbPT48clLglAmIHDtFhBtW7u2Wi7W9I1gghKpraj+EMdTcuqt+MDu4lMUICxKq92StSNR8Mlbeh/57kawQX+0JVl+NTgQhckqMfAVHor+vwRpBBBBA3UX990QSKsezHB1WP3kIVaT7/hBBBBBBNPo7evyLzBD99l6jNm13rGkagHsvOpGjDFVRUc6o2RpHYY6uIQrdv6+XsjCOwvcyODI4MjgyODI4MjgyODI4MjgyODI4MjgyODI4MjgyODI4MjgyODI4IUOw/8YvLuuTM7kzuTI5MzkzOTM5MzkzOTM5MzkzOTM5MzkzOTM5MzkzOTM5MzkzOTK5Mrkrq68tU5hj37EdyhlNQJRWW+zGsD1hkkrxSWMSVRUuVsJ++DLvH5HKDZ97CX93dQQQNaFc33thLsuhBBBBBBGsil+PFJYw0ThQnerMjmGq/8GIc039R1VSJkf1SOw/SbtpewzaXpBGkEEEEEEDainUhxV1E0GLVK5BBBBGkaQOUmwhCeJSlwbiRISbGmtCk41doMAwDAMAwDAKEstIIIIIIIIIGFKEJ1kpZsIIbhdBpHLIj93LfyIIIIII7NY2fiU47Csgbk6BQcjc9xYbvSCCCCCCNIIELkT05hewn7lo/b9yzVBHYgjWq7+TtwVfbsQQQQQQRoiMhBoUZHwkkoY4HuQnQQRrGkawQXWz8nWgXMbML4Mb4MbMb4Mb4Mb4Mb4Mb4ML4Mb4MbMb4Mb4MbMbMbMb4MLML4MLMLMLMLMLML4MLMLMLMDHIJbyVTvMQNghEIhEIhEIhEEIhEIoUKEIhEIhEIhEIhEIhEIhEIhEIhD0491xeSQOtbv2hLQLuL6fsp19P0ISWnv/8AS9/DWkn7EqdAzN3BUcCst91PQbA6SmI6w6kkYVJphDZJtrSJvSbbCa2nF49X96idKVMTG9LiCjVTv7cE5sIvxE9hydu/oIRJZd85tOsCEOOSzoLeEucUDmXeF3zxYY1z+Faldhs1EpkhKV0+FAqwjacq9JqbIrNb7/oiTWz9DecE5c7+4kRSya5n3ErZaN7cjQyu0+FHYr7u+/8A0T+/+sk5TApttd/frP5v6j9dfzvJ168L+eFVWJaiVRiydHSd9bmRz8GRz8GRz8FMKNZJ7Mkk6TrGO6FN2umN7suImvuUN5si+lE9xJJOkk6Wazt4ROCRLJZJLJfZYySEqX89ie6nXbo7/ftSbJLg47kkk6STrJOs6SSS+7YaacPx0j6FiSSSSSSdJJJJJJ0kkcNQykg+g2QlioTpJPakknSex0qf98aktJiihCyYXJhcmByYXJgcmFyY3JgcmByYXJicmByYnJgcmJyYnJicmByYHJicmByYXJicmByYXJgcmFyYHJhcmByYHJicmByYnJjcmByYHJgcjWpXI1D8an5OAAAAAAT/AOu//8QAKxABAAIBAgQFBQEBAQEAAAAAAQARITFBEFFhcSAwgZHwQKHB0fGxUOFg/9oACAEBAAE/EPJ3+gvyTXw7+dr4N5fi2mp5+nh2/wDgD6F4X5Z5D52/k7+G/o68Z49vGfXPlZ8rTzD6B8g4XwfFfk54v0F8L8rfh2+l38B9M8TyNfLvUNQtrYDdWgN1itOUwF1vF9A9WF0DQAnQaPcqKmvilKYQ2RwwIGwEGgFCtzykTUCr2hZIVZaW5QNCKyV4a8DLKSHliFum2BsGQOoQySnxV4vTytJfl7fQv0Bf1F+Vt5FiKrOtM9LQ95MeBGw8K6axfpLQ1yLO9CJ3pzFeq4GyVmdPaG+mWIBWWkVKuQaQVQXC3g6IhXSQyJsw7ImlS92rj1gAaDBkheyoIbFILNGnqGAl7wQoVmrAVeWWRghDPUijrVQYCqAq6qEdaSDQo5ADNt2PJyhnHEth1ON4JbFqbaFQ0HAcXaAvNR3nEZATAveIqGhQ4CpWRNCaXVJcCjNUgplKWjhcFmLjkizMAsIynImZJ4GXYg94yNw2LJqlim+j0mUF/MwygOUoG3UByTdPxmdIYSzsI+8e5irsNRYBvucoeDAUawCXrZ3JbUDdCz/Yww+xdkyNap9YY416SLMeZVBrCpxoCHYU94Uu4pQIW14U5NNSmd4rELdvaA5As9oWMYBzvSJMBb4VtFFfZHsZQXvlFrvmDQpSK5aHvvSDyua5vzt/+Nt9I+bt4NfGtGI9q1GPAuSsnI0egd4x12j1jWjJds9o6gofQAXm2E5ZNoUNMqLFpyy+8ca2VbHJr0IU5ShzUSVCsO6FOIgA6feI5YynycSq2UTokNNavrQPRYM9bKig7o4BeCmJtVD1BLgfY7yt8ua8XiqowB0CVxavaCTHRIlc1SIQLFvdp1VbfkJdWyIh0EffMHUy4GtGg66rEcV1+E7V1oPfnHyIU7ZldqL0DQixE+LRTS81OzUwBDI7CXPgOTK30hJKALYbF4tRjXGGbJk05m0svo42lGLBHAcOdjMyrW81Vw+x7oBMUq0BL6IfaXuAFzYH1fvQFqHC0LQfSg7sJ0ZIbGA2oaAVpH6OOaVaBdwJ3TSUHopuVj8wYTTMsWUZoEwar0hohokUYKvROUVg9B8G+RbvCMKREwxaoqs5ssNqgAV9Rt9Dt5L5m3Hb69llbXUzNGclt5rGYyv0FNyxAwaZKaJaudEAJQgtbrG1y2uAaBgOltejBLQoGqNLuS0YNYBVrYVqYjsxKaRTum7KFT2SBh6Vh0UjkVjW8QymBxRQpstXW1x74kLb2PTC9Bj21juQBRpoRcZYFari5GVyvUDWVulR6iIabOp0SLGS9NrRDNDrGzUwaCwtM+kyUeAoK1vTqQOiCXVooTGDBrbLW7SsbfioFHzrHssYYEj3ZD15QfJSXUpRwFyVnOYEWBI7VG3pkG+W8DGDQCgCfINmI6xOXqG3gLuAHT1mPPhRTc2U2AHvDGnaVZQrbE67z4BH/Y0G196Js7gJ0UzJC03NTvf2RIApsi1B5Xg7oOnk+gVtA68xgTWGVFtUnqDN6DA5B2UAqA2olKUbWgtym6ORpqoTF5hQZxVVpnR6wxUnYUlY1G22id5Q05/X35VeHaV4zx7eUa/Ut1fdC2SOXi6nTF1TusakdvQspdOyQWJ6IWgECtlCIGg2GtnDAxIbApdha6c4A0gKUBRZcFSCxVg2GzZ+zvBFkZfzlqPtCyyixSrItWqurESBlgulVmMaixg9FnsGo9OBEHoZHRahMABQBQR1sVhNQqUucNQDuoghChprzi21tPnR1XMjmHfCw1U5Zhot1DopTUDIUImqOSAKNS4CgErVAFvtKyQcmmiJkTZMxKqbFx2w+8FjZc+iwuuXrNIr1BknUmBYk2WZUXpDbgVwK6mcI4seUSul2wckW+1RYMcS8IcXolca0pXa4tiszJ4Glfctq+UHfpnuCr7uvrBtvRrHk8xNkyRugbxLoYPvcyle6VPmOB6tsHq9NJBKwqsyyn4IRpQppiVzBdYPm+0Wvm6r2YPvcW+nEWSlPA9W3lNNDwafRbeCvFfg2leZt/2L8O3CpvwvhXjYSrlpklg1M2OKCtN4qMw5sUgVWmLxVsoCvE/Q15Nedr5V+KvJspz63nllfgYuZi9ANVeUBs5+xCxHlxqV1NIBzV0gYDADYjo8fYNOtWGtdZUuGYHRaAFNAXu8dZSbxtalB1eNyNK2jXrDWrxfgrhjhXDfgxZaAo9RY5G2kIvlZxLj0tCAc1dIVYgiNiO/CuG/G74OBVoOcFqlkA6JLj4ZobXtbNPPjB7JLvwnIo6yzoL1XlwNIpyXtdnJrRlnGonygwUFoG+JfCuFk1leIxXwABpVbnKH1ywUTnlmeA1QHuS8TEqaS5UC0FkA5q6QEBRYjYkUAALV2IAV6QDmJr4TCxTgc1dIWFhRYnMYfLUKCaoateff0a4EyNI1q2zBGtKk3EZbyZ9ItuwAoMowAZVH1RLqq0OmjDCYwCQOke6GepBiCN3eTNatS+0hMeo6D3hjJOpBFcobzi9YRa34E5EuAHKw+9tIPY7m4xv+IC12AN1cEQH5HI0OQ4LzV5hGPrhAVDAbrLh7oCdjuWWMrmBFGqw623W41Ud6Ldh75uUkUnmgTd0ChpcR3c2jlrNWy92BZzzTqYbIjfKoQ2OVwWnYN06wyHWVLTBywq+XRfS6jO5umUXbzsLpY1NSthCp130Mc5in7l3qdNHUS5eApe4NlM1tCoLHLt20wANsu55puKU9a3JmRrVik+QU5xdRa5MWIZF5bHYrM2WqPIu7g0HtFRcEjDUHNRi6ckArUHNVeqEFPgF9UBkZO1zL7Tc1C8FuhqxFlGVAB4VSXtMECIEu4g40XXKdSr5Isg2sbYeDdclxIyLsBePY9JaWlEhZsm+lS8chYYRLRVQycLMARebA1qtld4h6DqRoch57XDpZiFaWwalGrAoQSBFDwjSdIKFlR81r9oHMMHCIrEDZXdWLWoCANX8C8HOI9CJxmj4RK6MuEWRgNescs4umNMnRUiLUFU24iRINrvHSFVXOD7mGCaJqWVLWc8BNso5iNfaURfYcyNwAqCykUtt0XZjYxFzD5ChZeXQINLhihMFqlGRj1jqjhTnrmrrswsYNg1QTmAimsEo1cmtK6OsfzOAMmzmXFa3EGEYNJdew7wLFMyXeXB9URj6zd849T7IN6YBN0N05QHrbeWp0vzIgQUWmr5jXPE58YjsFmv3ivKQqTIR5I4YrVlxT3Se1yqfoYzbW4Cq6wLEx/TBMOpncmXba4jk1Dd3K5QNxI67NF8plost60PkM+kQtPkBRSuAC7dCLVC2JZsa04ip1BuDTdmoNEfyKKpnQRtTQEvYEdnUobjrAOeBysnyD0uXXZYKablmzmKlqWFg1rFGw4Z0YwrgUCCusFGRh5XHJhQsoWtdrh2KzLN9NR0AxnVvSpQ0QAAWt2HvB3HIxYRVu5oXpcRNZAgZd6xpnMHTeWmhuzK0c5zBuEQBTCYKsA1YjQAoLKDCYYdvT/rBtsZ0K3ZgFGc3dBC2z0ievhB15S/Kqb8iMpjHOAQ2AJBdjjBnrFelBFBosP4YmhApG1zYtrg1ExQXhRlMWvU0jgQV1fQPtFCDDi4DObX1i7tmWgmb97I8ZnQNqF1Al5dC4OSfWqPBdSNhzFmOsCDBhit11HobMACxyraMmTKRVUQpbqiXR0SwQFqpzC0RwbqghF0FAYBmzmzMSmOK6IaqRlVI5W0YFOVcgqwGU2OUOAnK0GgN8ENmzSOthQF/aoVGqdgIZW0e0zKopCFRkbHKI9iph6LQhfMamuXwZBTZ7zfYC+VouOzwM/EZSB23mO7aCkUchz2Y3A0LoNCTCWg7w1i5qgJbjO8dYZp/0R3slnjTl0nqSIYJcZhl7P2qC1GVstKMiSr6kvFdIF2SZrWUCwFm1BKROW8vzVwzwD39YX7hrQJGTlZ6xEWxtSser7s0Y20E+vpd4XsrXRLCop54xLpAR4gB2LLhkggFoEVH/AGElIhrP5ZYxAJCuCyCNoIVg8hb94SuxazKitWsvLEQZNa5UMEBkXgb4GEJopX0FD9KmMCgLAFRoGaxcpqsauw5NrrswGL/KGjpkntqusTtgoI2dYcXObotYKiXyzDCSunLOebiWi1bQyK0HGCwa+mZiZlELtALfB1GYBrlxRZHkTAfR3IJ+ZZMhkyAAR2JAIZra3yygovqwkwpyIBnLzJICoYYUnOPPat6l3Lei5hK1bvYPtl58mEJh6W+0cXQhMC02a5letWDQO06xN25h9ocUQi4WLjK35QCV2johWg7o5BL/AHCLBgcmKuUzSkrVETuc4znEu1RqNUHLWEPnLiJGKbH3hrwAqxWm16+sxz+bZGEXnvc5qMBkydGrL5zUCeYJtWrzlHeDgq3ULtjvcsHdwGYmTcT3lOtkqzAVhuXlKu0xulH/ACWSbHYFD1ZqITCXQ0C1VgI5pNHvQ64JxtaaygG4aSwp5DLbq6mkeM6Jdg0xseknZUFurrNtRMpBIcjPWMuYq2A06Gse/wDuGBxXsuucFiOg5GEBQ6c8zLhlkGCClqdBL15VDQFNnNQxCW7VFKjSs+sdSv8A1vcDaw7MQLo/1h8FqaLhroOl86iUEZrRaOtasHYhNXUVDCmE5zLwgdyGU0Q0q9dJzLyQY0UKmMy9HKI4AWtMy+GedCsiWtXmIqmDkMoikASaTZauBZWifbDC+nahAqymlIMGJvQWbBm6jDPk6cNvov8ANRfvMVW0Apt3QAirW0FMkuVALUAW94ExRUoSqxVTexVCjgkAdYBfeLFVhxU6OaFH2nRrWBfvKLuswLAB2jQjUQp2hiVBl3QBnhTQAgRQY5TSwY0xpCjAYgBdBnWNyw2U4gcq0Cj2mixBQU7QAiWPOdB8AB7QApRVVVQAUYIGgTw0LfWJxJqJZAkgMAGIAFAVpVRrSoAugLiURLHCMKaMAAqUZwZgBUAuJgHWBnvznSiCWSjlKVVFcqgQqiuURADhEsYLAGACggUUBUQkUUiYqUuzcE9oaAGK02jfulGncCN6uzrmGCpXlGaBPvCpQFFGNIUYAipGkgU7MUsS7jYAnJJUzhS6AF84inJEqCQsaA7AANiaN0XzjQpJ1HSBPaABVUbSyXi2gLiITQoNdpkFBTeVGcWWDUDVms5j1q2FkAqgUVptM4gsIMvrFgLEgLfWUZUXpwpKOqpb35wJGizTEobUWbxYW0lCz1mkoyovnUuooW0kFnrEuublJq2FEFQ1baBcN8SheAvOIYgNTQz3m8aqAkANA0qFBQAQ1JzSKKrpTcHgDQCgiwbHRBZ6xCAI4Rzcp8BgAxG5EwosfSBUAFKKNI0mFZQa7QSgJ1IglUJ1laUrZQaiDVg03n/mbefXlbfT19U+Hfwb/QX52/h18enkbeXfDabfX7cXK9SYXy7we6NVhfLv5+3nb8d//na8pxGrU19NocaX4XZ5yhq5fp+IcPR6S4h/xdf+Np4tvrH6hURUrJUc/gxo6vSKgMBiphKQRwzSUhK50e4auxzim/i3/wCjf/DeD/wd+D4GBAU04C1Zawc/b0d3V6sZcLZSot3/AENOoQJh4d0WQfBt4tv+Znw78N/Fv5Z4rz49OO8eOn0enm3FU0a4Y2/NS3oHOXGDw0dWuu+v4kO/O3/6O3kb+PfyK8V+Zpwv6LTj34rM5uIdUwHVcSzUPUOx0NDocL4XHcEh1BsYfAehsf0OiQfrHyMTaaeA4aeM/wDid/AyogDeYMcaT7Md7mkvwDUUbpFXGl+d3OUez9Dv4dvLz4d/Dr9dv9FjifRY8Fcb4HjVSqkVHlTPaM96md1eq2viuoCq1HaMeEldfzYU9R5wfK9eOn1FfXHDb6vX6Hbw7eQwGAFU0BusVdr7Yv3LPtyjLhmEvhlZcgSI4e9r6mp1OsHQR6xCxIeT6f8AK08WvnWGGoGK15GWT+M7XfIQPvAPCl3Px2gFlDRsFui1g5DKgQNzEs4uIc9wVNK0YM6sQSQtVRoBzmovJYVaVDZed6e0BC2hvyZN2HSKItsN1Q19/oH6hUTHvYQ55Xqx2GLnicDDfzlHNdA6sOGufvBYPQZoAGv+ChB+kMkUBeV5yzpHw+rLrb7ps6PSKz6rT/i9/IEnen3SgBQEq3apWKI2Fndem3usAOa3pDiUqxLuBQVnFrDzlO7oGXarWdE19JRzMXBShNOZeujHlnetuuqd62u+txbLoiMmFHDhO8ypYutoCaN6peL0IBhKrJEKq6E5nrFYsVawqd1U6rCC1ixRAaA3XrpKrotRTVIHXIN9Yr1CC2AIOljPh+X6WpXGuO3HHkMtVu+7Wx1Wg7xttSNjoDoFHEYF6QkjWQZty+3P2XDyHYZXNdV6s00jhBCikvRV/wACYJSyNXSzZ6JY9GMZvTV6K6jZBx4NPptf+Lt47qbs0e6XpfZQpm6uOxJWsAGhlLEeVylFkVqChTnIZaAlsa4NQu7DCr7lQARQeQ1fSW9OFI92q25XaPj7C20d2S60ckRkOcFdIuN9eKsqN8ZitwGFgRhu7ybRKGtCh0nfTltcUC4LGo526rljeAidE6yHLr+P/wAdUTOWop8AZeqcpcuGYlEToQljcA9dXkd4MwQKgGgG0YewDkaBnXAdJdFANOutyIOuiRbDzgZSW2p/IX14LmAO83SrT0Fdw5y4l8Hjt51/S6eTp59+DaG0Q6lwAKqIbRJWNVBcclTRVeQRFROiF+8RUD3LjoBWlVMBQojZS1IC4UQA6FTBGbAL7wPQG1YmAoxwzKlRGVxGq0D1UIfzYvYZS2a6mekpaYK7JJVa8JMh/BKkyZZfDJkCJUkNZIXSSo8EmTJ1RxkyvVeCXLk6H42JMhdJJ1UFVHiCVS6yGyQJB8je09DV6EVGpryNq92ZgkFaKHJ6GYZ4HVfjOdi7YfODrrqdVlhFyvrVdauhFzrZcKp4MSSlDGmAOcAuo6zQfQt9ILVKvV3ly6gEpgopQ2J1GKOGNbA17DJ3eUH/AODvggKeghGkak6ypuxAOauAgNgCI2JNpdsCD3cEZU0Fu64gdgKq0AarA4YsYboO8u0G5WK4YPNXSBBBEsTeYCBHxQonlVxdCRin0s1eksjqNFFVaQchQuDiVF8IUtJ1Oo0+kpC3iEbBXVc61nMZ7J/PS/8AWn8JP4Sfzk/lJ/CT+En8tP5SfwU/no8/9EOReify0/lp/LT+Wn8pP5Sfz0/np/LT+En8JP5yfz0/lp/PTm+2jjRByCpmThDR399KOh1lpNiKaKDMrr783QgYRVCX10yzV2nktafe4NODBTEtTQHNlytn/BOtY6BzjFi8NDUjsL+6fZYCaj2/5230+g6DDLgfS/QmEKzNMXor3pjLg6AKQiglrQOIrVDDLYWATGzZpF1EsyguhWouTXON4SdbQtVlSgxoswhLoXQI430h2jZG1Qayt7Y6dnGXk/UCebRBFmAEtaBZYi4LaDcMFKmLxTCgWZ0thoFTAkuMv0g/Um6SsAZVVV0h3759c3sWhFfqFZZU05FwaHCgXSHUcgFbG63NMb6SyqlLk6mbqZNay/qnxXFNAQUHPww6vSKbYJZvNDMJV5avYLfSCBiCLzW3VcveWtJ08s0O136TGUDHl1D1a9OLUwLVaA5wrplRY+Trv21bS4vC5d9ZZVCEs6C7mr05wf8AsX4NvIrHFugq/wAxdB6UuqF7Iz6Q4uz1ZU1YulKb1iDc1R7ts00FLxCRtStbx7UBvpFbB7VhLp7lClFj0IUGwZWZQToKroCK7GbpAp2WmvOB8GGPVFRYJyMJ+Sb63rqyCh6jD/lrtCVRyBXtGoTe5ee0TjHekoejHPPYL+pfI6UkVEyYghmYM6jgJZLB/kIxYqDSwYRwDY8TlijRqPfwH1rCGOp0AtYbyixsfc3eqy5tEZRawPRNJmZMisr6xcArlYoNt6s0gB9VHKWebs76OdS2I1pzmvy1H/IyyEqpA5GV1o9dY2ly/Bcvx1L1ceofeoC4kG4wfMJXk7/X7+J4aeRXAsLMPOjdGhHMNKaewoPtFls1KYxmQQCFCBCmLKhhBbaS1spzl3KOOhNfJeD5uvlKiaMIKOmr19XQOcc8LhCObTp5iDKK03TlroRpqRZZzDDagICF2SUNRovMV+Jm3uw0gWaWXzMu4jbiLqXXrfpMBAO8trvavujLly4suXLmvgJdnX19HrHZHjf0G/8AxHwb+Cpjzd+GPq9/IuMyR65pXAd38yxkHMLy6Gh0JfBrC25q0vYVtbrOas8mVIjtQDcavBgwazchKxcKbgLDm52gMjCLK2rSBBrZoKtV2meAKLhs5TrRXQIMuXLl8bi8jw7DYwTgFLYx7mnRIP8AyL+g2+n1+t24V4XiVVxwxxpL0e6Ll8LlMKEFUFtW9IES7OTWVsrbWheeUXq2gwod2Hb/ACX/ADA2nWN8hG0gil9SOK32G1Gi9+zHeLmXLly4suLw0lPWZlxo+tq7nKO9YeDb6NzNvqt/qjx39WzTgsIlLh5Uz2jPepYqqrqra+G4UK0I5g1L4EuXL43Fly4VvNBAWuTX3Az1GD/0dZv9a+Tj6TbwMcgBarQHOPyfSF+5Z7Vyly5cuXxuXL43Lly5cvjcYtEsX3NfU1O3WAvBoASxPSD4NuF8Nv8AqazfxbfVV5e/jWI4IsJZ0n3Y7DFupNdpTyZnlM8pnkzPJmeTG+TM8mZ5MzyZnkzPJlPKZ5MzyZTyZnlM8mA8mI8odpbZNQVN5ufUfZOUV+ft4dvOvzz/AIWfHp9DvwqLKz1pzeQdVxDW88zaKDDRjlLjwMeLFhFnwL8z4B+Z8Q/M+bfnj86V/C+8+RfmfMPzPnX5nwL8z5H+Y/Lv9j83/wBnyb8zPCLxhJlqcTJC3Msrd5MdLXdnc9HEu/J38vbzq8nv49vKJv468eh4MfW6SiGeV3/h9P8AXpKPE+G5fG5cuXL8V1LPIrt7PqfcOcRXm7eGv+hXh1/4G3hWoVEcO/d2NZaiKNq6rzly/BfgvxM34MPExIIobE1HnASTQzbm7OsGzhp4NvE//DOkPFt9DcdCrRLZuj8zf1f5Xla+AOG3lXw3mEajom3oftceNYOPod/Bf/FrjoRmnJQCq63euNOF8K4OlxDZd4vQawRlSunC5vB/xyrPEZXnPmKUVAdD3ffT3434LlzXiFtc8EuReaS36besLUjcJ7FEAJtwNUT1Z3xfeCX5QCZPvLZho6nY7xKl8b4suXL4amiAv0X009oOP+Hv5l+HfyXSy6c3Y96g83bqNq+6/SWFaUTWmE73CwVVLAa1bb6V0iIMb8F16sM89opLJePHTAqffrKhDYGjpZz19pzlID+nclZd4Nsms0W69C7rtHswDpT+j1I+uqFaGDLV3cdl+iyVmnQzitYNU4hQNkutxvlL+gtPW1nncCme/Fv0osyypU9KhXTojpfOPVELGg5Vecdo8k0lKu+k1PP28G/hWWSCTpNxqVybHoRfBcvgcLjnU0NVgDFbVocj9w9Swxu3z+aynO1fjHtLP0IRMhqlK5tBVzreOAOqHAdOf3gP2Y6fqbPUhtVKYyPN1/2VXC5cuXLlweAzJ0mfceolFhk6MPI7+V3+h08m/oGU2dByg0Hqj2goZ0PclbIwS8gZUKPb7xLEOcW1nbrcS/TuBWO+R7RjMwNap3zm+lTXElIF3YwOb60wftLyPS69YaFK2XIOK7MCW5xqInaY9yWdxTfJgD2N5iGJ0FQFlaczN7ytVWw7egvfWFtYVLc56I6wstca8LTvWiSy7ccrBYvLkE3SPJKiUzHl7+a1ZMq32ejXu9ONy5cvhcuXCmGNg6L7nd/zvMe82zmp1L17XmXsFiyycmsaPPPg7GhDGnaWlJhNE1I9JTV1r2R1ezDvIx8W+pfKI5Fo2T5YzKqmHk2ZcuXLly+F8Fy5rgKzs/k194r8jfyL8zp59ebp4NCqgqdmAIrWbskX1lau2q+8aqosRtoPvUVzYCJYy+5+rt7R7V8X3awEDGgNPeGQXQAe0VDnNAf5NGrianvKKSpVRdd4S0HDU9500eh95vzOkPtNFnABe7Kh6LcOlqA/eUxG1sXKtD0gY397P6mYvyZ/W8Gv62C/uz+tn97w6FlI/uzHG/rZ/Wz+/wDB800P+7DXbqnb2jFBWVu6ehq9omV6jVXV8d8SMlVYuWpfa4oamNucX6H4horwL1BkupmOV7s0gkzBr+QrCDXLbrpC6hwJnPK3TfrCOWtFHPqDBGfdbT2f943Lly5cuXLlxX5ANk0YKgmDt6n5OiQfKqV4PXy8eCvrUvRSArWjnDhlagAdWb1pSWDVDcyTaDjQUgrQzu8pYwiwLVaAl+nzaPYYTGVYgmqGrUM5iLZAQg6Kaly/FXAM6iNEZjZ0ZD1xbPWb6y+8vrM+DPgub6+C5c2mnAsCy7lLf1f4S4svhfC+F8LgsXhOiv0S9OmlzNWPQiIoF5WNVruscSm+IEQyxVR0FtiUUd0/39PeAxDkojY6Pv2hOY/bZFiOYvaIzyfeqfeLLlxZcWXLly5cuUdZi/T4A9+kXkHkb+Pbh1/4TSFSoa7fVI3Yp+FgMQk+Ev32L3besWmxAbWsAzuXWJV17csFMBu1g5tQrFxQDT1QOLZYzknOmeRMNBfJWyucCatFc5bcqu2YlItiTTdY7rus1H9UuWq4AGVXAGVl43Am8qlIa5Vz8D4Dz68a6yypAmtfgB3ly5cuXL4HC5fAfi6w+zkKVWMkV9NpSZrNDtfAKJYS0oWvtBiJ6ipapeL9pSqIFgDaTbHGc94VIRNCq0MPSFhfKLLl8L43Lly4tlRBw3fqPgPUg+Xp5OPp9ptL4nF8aeCNdSNgXjMoFO37cgC7jqzBVNEF0HXDylpW9z7IgjDYreFgNFGiIrZnMYTWjiqwaFpljSJnIaADKwnpEqxTq1Fo6g6wuBgQqVpqCU8oPBasVXVJ2UJCGtApJCNK1W9C3jE/71MTq6iXh8GfPvymFMKo0A1ZfuJY2dD892MXLl4ly5cuXLlwzFUDE6q/9gEHUuq/SQzFJXoRHS/1BwGNUb6JrLlN5OitNg5deGEtoXA5rgn7ENVI4wS+Fy5cuXLly5fAf2jC3dfU1O0CycBojowfpr4Gv0+/jrhmXKlY1gEtcVu7Earu1tFg2usu6ruqqvNmqGMS5lvAqX9PXjVTSkRzb8jX0IuIPG+Fy5cuXLmEN16NzWPsuKqlJDo09T8Sm0dZfC4sMzr4DZ2npr7TKMu0NHq59IsvhcuXFly5cOA8GhJN2+/0Oez0g48rXw19Ca+DP1230evlsz1Bjctj1Zd+ZOv62ly5cuDLiy5cuXLlw1lVMWC9A3NunaBvqR26vV19ZcuXiLLhBLVIWDvns95eSsK0OQdAxLly5eJcWXL43Llwjy0n6Ho6escPVVutx6jiGePbxPDPnkeGn123/D2iqUNxsjTc9tO9y5cuXL4XL4XwuXwuXLly5fG5fC5cuXLiy5cuXL4jBirSS0uOR6MdwhJfifq9vpfTwZ8WeD5On0a1DLZg67+gz7RW21V3d5fhvwXwqVL8VcL43F8F8XhfC5fC2JRFQ2JqPOMkaI5N+zrBxDxZ+l38e30B4u/ln0pxWBm5o9wbJ103c+0Xr8zpH55/k+OfifPfxPnv4nz38TN8j2nyj8T4T+J8o/E+U/iHyH/J8w/EfjP+T5T+J8J/E+E/ifIfxPln4nwH8T5R+J8o/E+EfiUfI+0+A/iPwD/J8g/Eo+B9p8o/E+U/ifAfxPlP4nwn8T5H+J8r/EPmP+T4j+JZ8P7RH4P2h8h/yC/D+0ScfD6Qj2rbS8aNn7LEaXL+r28D4nwbebr5enDX6LPiUppG/Q3Gea/YZQz72LP5MA/dn9LP6Wf08P8A00/p5/VT+7n93P6ef08/p5/Tz+jn9FLf25/dT+qj/wCrn93P7Kf00/pp/Rz+mn9PH/0s/rZ/Sz+lj/6WH/pZ/az+9n9fH/1sf/Uz+pn9zP7mZ/yYkxd3xL+rTK6dxo+nOaPMvyteN58V+XfhfDXgfHfGvOfKXEVurytXkHVcRUrxDQ5B0CjgS5cuXLly5cuXxuXLly5cuXL8Ky5fCyXLlxZceFxYsuaoE7ZR7/4PuEMqcbcdGGngrwbcHjr4a+lz5b4KmnkbfR14d+CqUmZ2noHo+70lwZcuXL4XLly5cuXLly5cuXL43LlxMWoHWNV1dk99IsByBSJszEWXGXLly5cWXLiy4suYZl22Xdy1/Id2WePf6Lfzd/E/RV4Dzb8lagEpyTd/g1e0dghU1V1Zcvgcbly5cvhcuXLly+Fy5cuXLhMaqgZYtsQ4QbPvJuUABpEebC3oqvtUWXLly5cWXLl4iy5cWXLiyv3PLJ+NuzMYp53FhXZgzWXL+o3+pQiqDNxS7ClIeoU+koADSrK5JqPfx2XVl8oKdRQSrULdtGYT6dmKX6+zkfsP2CLjhcuEvhcWXLly5cuXLly5cuXLly5c+2s43V2IJhZE9fQNjYlfulp2xMgOoTKXLly8y4suXLly5cWXLlxgPQUE6aJ7Mdwlx5fbzT6xclpRppexUvtMS7WqBbGaGxBGp0oa05WlY5Rg6KkB3AwVbiO9VQtZ1bZfKirZ2QlpzR1OdZOUZDa3FLoKrNJ6S64rasC9KrVD1l28SYqqADkPeGx4vbOTrse8zF5mFhPW8RFgFlAtCEyXrWksfplxNCJthzvPXQ7vKOmCiXL43Ll8GXLly5fBcuXLly+Fy4Nw5ZrL6HNfxqwUKhihpuuwcto2A8Jh/Xo335QoIJqg29Ry5Rq7OFy5cuXFly5cuLFly5cuXNcWnU1OsIkcb0H2Jn3ix5R9Jt4NvN38CWKSheF7BC+8UnlhlSm0GSzaIgAm2hY5ydoCgFyna5GpKGtlAfUUggpzbAsVfNUKjIJNRugH+H1lAqsrULX+sBQFBOyC/YPeJT7t0CuZ9GH2BTIFhilfJkVffhfm3x346QMrjtg1Zf8A20+38O68Fy5cvgMuXFly5cuXLl8Fy5cGXLg3OYy2Z7e/fTvAg9KNf9kEubrs93M9NDrHxwstD7LCnCC8J+ZSqTJsy7I8Lly5cuXFiy5cZcuXwuNVFB8rY9TPa4CFN9ofQPj28+5r5WkAggjhGPz02jL0IRWiwW1dgGN33l88qFuzbvWsWKm6rzzOT1IcMdEe0U16RA1DI1NHEq/p6mTU57sVDR2Zeee0GKlLqTkolneWMLz8gGdrmpjrYlmr0eh5FmO36Ep5aIIvejB2WPZ9pd7Ptw957+09/afNJ7+09H2nzTh6S9RFmKUO3wX0jbhcuXL4ly4suXFl8Fy5cuXBjMdZzp9s6l0PWf2UY/2x0hISZH/c+w94kYMXoDkGx0JpHM/2DCw0iFmJT4GuLL4FlxeC5cuXFl5ly5cuXLlxVsiDXOme7/EXHf63t9BtwqNBPZKuBUvbhfFYPf2mJWJcu48NpQ+JpoI2X0sIJaleh3JTb0xKq1d/3xfaMHtOyQXQ4kiRXcBAujCUgjeMSxKBqTpY5VZZ6jnl/G0uXLly5cuXiXLly5cuXLly5cHgBvA6ypXH9919Lh7Xp94LL6VKxRoKHrdW+h6wayv/AHd31hCZq9U6NbQNz7D9RQNntkZkek3J8I3xi5fEuXwXLiy8y5cuXLly+BPLkc9j1D71KsI88M1+tPDfn3x/uJEaTFhK5jFxWTvCEfKLegAjgrNMyM8zTa12LspM9VYihaCwAVaQi6KQMIktES6RRil3jVXlW42unWJOulACl5wYcxIa50oUtgZBms4BlnyxsAUS6VgtLaL0hcDmKs6bPSNALUwFUXJBuSFhdc2qYts0ZSTY/wCq6gUJauriPzG2OweuooxWsACHMZbMneql34N/Fjw3KSOV9HDTd9jHdZocFy5cuXLly5cuXLly4MuXLlweRCyLd7OfaID40/cJYchc3vZiLmsH/wCRef3EEamTfCkQZnfliaHYjtH8jfLlxZcuXLly5cuLLly4suXLl8BaiqvPX1dHrFZwrw35G3kb+dfHbybH5CN0Z4qt29sGdcaoqw1YQ6ZSAOoVrK+o6GdHWHRd/rgoZ0Z0sqGfWGZW7JuTA05zCwagbQ3ozCswPIaNAFeNWGLCLBvsIngWdOoQpp9UYU0IWhM6a8pWVVIMsGqMLzOsDLf56W6KvDRtMt2MYxsKlKYalxR/Sx34OR3VQ047+I8S1AGraXmPsDPtFalXm6svhcvhcuXLly5cuXLly5cuXLnXPUy9iJ1D48o9u1SL7xxANprLmpVGkroBSo1d32JtPgJzn3//AEml2I6kfxt8WXLlxZcuXLly5cuXL43Lly4qYMew2MDQQodv8n2SDZ4jxvhPpDTyl0grLLp58KWSwLWWLBhQij11iTBZCx9Jp3+AFORyiQEN2BhvWFDekIHNjfrBoNRDL3ljQW20asDiDQFBEpLAtZYta2Ci05dpt/Gq+zSXjTlUUVpiUyorLLp5+espHJ6x0hsPnbPqZ7VL4Lly+C5cuXwXFl+AXxLlwcAuje9QlbvvKyFiveqcAJ0YqXwzGXzcODru/wATS7R1I6+NnFzLly5cuXwuXLly5cXMuXLly5cuVtdC640l66vSXE1/5/b65SvrmiHOmvXQ9Y+iXLly5cuXLly5cuLLly5cvguXLqKKQYzK1fgIhomwIxm/0nYfMxaMw3cWPuQtHaLkl3ys+Cy5cuLLgy5cWXLjLly5cWXLlwSszIjT11fZfcYPC/8Ap7ePHkHkMMai7YC2BSp9nx6B91ly5cuXLly5cvguXLly5cuXLgy5cWEEMQpphitD8+kVcqrQF6tBrFb0V4RdasxFOD8+kKuwKAwaAGAj+hjUA0LS4t0189ovhz9U6sQIgq0vq1mXpgPIfxBVUI2q2rGLly5cvMuXLuLLly4suXLly5cvhcsQ10N2691n35wDAhYmROZ9Dv5u3gr6evBv520WJcavVfLX8704LLhLlwZcuXL4XLly5cuXL4XLl8Ll8NovC+FQa4M8GXFly5cvjcZfBeN8bize4Vx2mubMe7HZIsfX9+OIeUHDfydvoljiC6g7B3Yur9BlfXTY6Exfgfufzn7n8Z+5/OfufCPzP5z9yr9T9z+C/cP/ABn7n8B+4/8AnP3P5z9z+c/c/jf3P4r9z+c/c/jP3H/yH7gn6n7n8Z+47fsv3P5D9z+U/cP/ABn7j/5z9z+U/c/jP3P4z9z+c/c/jP3PhH5lf6n7n8R+5Z+p+58o/M/jP3P5z9z+U/cyfifuP/jP3P5L9x/8l+4f+K/c/lP3D/wX7mH8T9x+Uf7H5h/sP/EfuPwj/Z8w/Mf/ADX7h/4j9x/81+5/PfuH/gP3P4r9y39D9yt1fT+4rj7f9xiy1YF2EzuY9oDlIGmkvZ6w49/+Lf0KeesoJToVVg3GNTQ6xd8T7z5Z+YF8T7yz4n3nwT8z4J+Y/JP9nyT8w+Cf7KvifeK/M+8+SfmfJPzLvifePyT/AGfBPzPkn5h88/2PwT/Yl8T7y74n3h8k/wBnyz8x+Cf7Pkn5h8E/2fJPzH4p/sA+J958k/M+CfmfHPzPgn5nxz8yv5H3nxj8z45+YfBP9nzz8z5p+Ytq3w5yj4n3nwT8wo+J7z5J+Z8k/M+SfmfJPzD4p/sfkn+z5p+Yp8T7z4Z+Z8k/Ms+J94H5n3j8k/2PyT/ZR8T7xb4n3gXxPvKfyPeF+E2qqb/MKdnnCSa/VvkPk34t+Gfo1iV7jIcqZ7RnvUs5VV1VtZfDXhcuXLly5cuXwXLlwZfG5cuXLiy5cuXLgy5fAZcuXL4XLly5cvguXcuXLly5cuXLl3wRkeHUGxgvha2z9jc6JDhp9Ht5VfS6fRMNORUUAar0jhKrXI/cs9qNoMuXBly5cuXB4Lly5cuXLl+AXxLly4suWQnqgMB5pgd5kgpTo5rQdSXLly5cviXLly5cuXLly5fBcuXLly4sWXLlwhsBS40O3m3ROUuOv0+3m/75NSvp7iomHa8Dm/Tuyuw85eZfBfEuXL4LlxeC5cuXLly5cuXLl8Fy46wdzUP3XfB7qh7wDGqta6Jp6HrDpUsW36HuoDtK3Y+RbesFdqCU9A4fUO8cUVqxfsLXvAC0Do3wXLl8Fy5cuXLly5cuXLl8Fy5cupcuXLlxp1yMxoy05/JBT1OsVn/KIP7NEwDm+8M6KeKoFvQuCLjaesobnC4g0XPQa085b+s22AavfWGTDcsNyIC7OFL1LnrLAtmJS2FxpxlxWz3iDKwPQ1A2vaf6ffOqjl41lqOKdWtA6rQdWOtrOw6B0Cj0ly5fEGXLly5cuMXL8YFwfCFxm6ZZB0Aa21ekE4TIixBftsp/bD1YhK4GO4DD1uakxfQHQ6GJgI5hKcnZOjiDgrGDvrw+idoaGNrn22PvFiXdd/1iLLNt4qC7C44L4L4Lly5cvguXLly4suXLly5cuXL4XNqcrf8A9GB1IN9WnIWJ6Qf+Dr5OIbwnOhQnI5yGucaYgRZEGCoo5DXlCK11tABWM6Nb0hFsIAW2Ko5B06zCActEB0W4o0vogZ/sPKKgssp76QEQYjFoGDvpnTvLJz2ERaU6KzOowh5ARGOoYGsvQi8sUNu6SFAU5DNkuvzxQwKByLuqvugLvgcMFity81VZ5Qyb4G7RVXgzjlHmDxbWgCrKGmRJc5G1qWOGNfZClgB2M3k1vTFc2VflEs0HGHNh5MpBz8XvEojJVaBxVj0G+70gy+JcuD4QuXLlzDiXGLly5cviXwXfFrNxAprENCtosuWwjp0iBgNaCo+N5JcuXLgy5fBcuXLl+AXLly+C5fBcuXcuYQsZq67n3TZ0ekV8NuL9Ft9Hc1jbqpk+zLK61d6xWxEwZB2VYRrTEoqORLdnXktK7kCU9AuqjXe5T2D+waNrwi9agFtqZI4R1y9tYcBCZQNXVjOdjiJCmdVBWNKpLy0qEnGQCysz1PeN4+g3OHuQo8QFGA1zQll9YrDhRYYt33r9JW3rXsOJuGcekD77OZLL2SF1BirVYU0R34phZkF2AxWoU5uVmspduCWF62QsJi5k1WIX6J4lxCU5Ebpj0C126xp4HrUbV6qy5cuLLly5cvguXLl8Cy5cuXLly5cuXLl8Dt/DMnLIWXwXswBaroBziStUDTwDdzz0OcNOVCyyjVnSVv8AhcUD86S4vBcuDLiy+C5fBcuXLly5cvguXLly5cuUIkTazZ6JY9GO/vxzpL1GyGnG/Hr4N/L386+FDrNJrMcpjSpSpXSASiYJRgBMciPaJbMoSyNcjhXg0lBH2cG4z+8MdAly5cuXLl8F8S5fEWZS5cuXL4Lly5cuXLhkLYOJOu8qN5Y3Vc3/AFWaqIq7A1uY+Sp8psc2xsdXDaJv/wBj/r05woQLl1QvrHz/ACS5cuXL4Lly5cuXLl8L4Lly4suXLly5cuXLiNWsJYpwdhjuEuPK04eviv6ctmIAa6m96TIlhwVvwslEMUnBrRy8oH1YPq1bWzjpcRItNqILTmF+sdrB164GtNaxgeYMuFSvU/SAXQ4spr1jRt1KmSg2jnbGIcwivlrZZM4CNURT6MjuS6qhem0dqIQOdHvt07vKKbFBLly5cviXLly5fBcuLLly5cuXLly5cuXLlwAdCmd1T7iWGhLyLj7/AHy6I7lRczAWBlfvNu0EEppFLX+TZfTEO1b6c27urZ68rVqlVtVtXncC4KTdHXlPdgkV3DoX+xly5cuXLl8Fy5cuXLly5fC5cuDLlwZcuXLlwmhBEpE0TrCOYzcpjsGe9m0Gzze/gz4r+hYXfJRXojytRHoKL2ih0OWWDRZYAFYhOyOGyX9LQhrL7tBUBmtnwgU8zP8AsSA00Dlc6Q72xXkc1uwEbsGOLLQtkGgS65tZmVBJMTbTJpit5ZLGshdTVUJRVR+dAcMQWWLqwbQqUWd5Dc+uLlLXpHeNbE4eKB5BvmYcDrWzwqVZeG9xiwLCou1AaXRbKc33ZXV92V1fdlHN92V1feJW77sOQiLAFrLMEsun/R6rG0uXLly5cuXLl1wXLly5cuXLly5cuXwXLly4s+62Oh/EbTkNan3cPrLeRDUg0j1GHrqjSj5pvC/0fPU3db4dL3jgPo2pvwSMc+6aI5RWA9D/AFfvLq1c8m191ly5cuXLly5fEuXwXLly5cuXLly5cWXLly5cZZAD5Jx3rPa4CQBLEbGX523kb8NPHt5AFFvdb2EGl+8zwCtNF3XjMyAQN8YLlwBoFIUKZzjlaxQAemkRJZUjGewCTWOI9X3tjEunIjZKPd5jqgJoc827sINHCKugX9pTKJ06eoxVVVQjaNU713gMaNkKoYwbShobM41lXd5NQqmgKdW24V7MgSzXZo52GaY8mojZMKx7vW1dDml5ly5cuXLlxZcuXLly5cuXLly5cuXLly5cuXLlzCHv/BrqLs4dF5TX/MvQ9L7HO7L6cLmEX4yBpTVmymDpbvAgJ2MNP9VvVOUuXLly5cuXLly5fBcvguXLly5cuXLly5cuXLlwal/TISzor1ZdIVw+r34M2mfL28s46nFaJzC0qXwPdr0uWmo55cuhodAly5cuXLly5cuXLl8Lly5cuXLly5cuXLly5cuXLgkto0LRI0oRUwaJOq3NtHaOHNk3zkfsG1mll+0ZggAWryDdlZAU3jl8fXlMJO4yNoXP9mmqQXULUtqu6y5cuXLly5cuXLly5cuXLly5cuXLiy5cuXLly5cuXlt+3C4XufepQfznVz67PUYM24b+d14bf8frKCBaAWWKK9A9zFwZcuXLly5cuXLly5cuXLly5cWXL4XLly5cuXLly5bXcVJ820ZhFGxTd/tOOTtElrLxD1/cdesqIuHFO7se3vMj0KL7B19XuiYpOEtVXVl3wuXLly5cuXLly4MvEuXwuXLly5cuXBly5cuXLly5rka101eto6nNLjxaeKvFp/yFRBPS/lGZ7RnvRvEpVU5VbV5vC5cuXLly5cuXLl8Liy5fC5cvhcuXLly5cuXLly5cMRY+2PZNfUIntGw0ejXvaNnhcvhcuXLly5cuXLlxZfG+Fy5cuXwuXLly+Fy5c1Go2A2MC4att/Y3OiQb8e3k6+Lb6jfylxLlABarQRHWwOyXPrZ7VLly5cuXLly5cuXLly5cuXLly5fC5cuXLly5cuXLly5cuXxuXLly+Ny5cuXLly5cuXLly5cuXLly+Fy5cuXwviGRtCo0O26u5ylh1l+Y+Hb6TTT6MG26VCu17WWX1g1sOzWG8lxquKP1Qv8A1Qr4ZZhkfxvCccMcPDjj+ND+VCn9UD/xoPgsYY8eJhlH8qH8L9of+V+0F/T+0o4pZR/Ch/K84k+8cMMo+4IIo4/nQJxT+qH8yH8aH8LgWfyvEWcMMeM+rnfyv2lX6oWTP43Aov0mZ+MePJ8Icq4ZYJIsMNJe6YWEd3RBQnC2GBe8VwfpT/gPDcMBdHtFbPadJ7TofaPL+06f2l232gO32jyPtDl/aY9PtOn9pRt9p0HtOh9p0PtL9vtMun2nT+0q2+06X2nQ+0OR9p0vtOl9p0/tOj9p0ftOi9p0ntOk9ocr7TpfadN7TpfaDbPadD7TpfadN7ToPadB7TpfadL7TpPaPKe0wafadD7TofadD7TpfaHJe06f2nQ+0u2+06X2nQ+06X2nQ+06X2nQe06H2nQe06H2nS+06f2nQ+0D2+0eV9p0ftDlPadJ7TpPaYtPtOh9p0PtOk9ocv7Q5H2nIPaAyh7SoIIfT4+i38xiS2NnSJ5SvKV5cFeUryj0yvKV5SvKV5SvKV5QPKJ5SvKdsryleUrylOUpylOUryleU7J2ztleUBylOUryieU7ZXlK8p2RPKdk7JXlK8pXlKcpTlKcpTlK8odE7ZXlK8pXlK8pTlK8pXlKcp2yvKV5SvKV5SnKV5SnKV5SvKU5TtleUrylOUpylOUpylOUDekolJAh5T5R5O/0+3CpXgdeP28NPI/9s7fA6+L/AG+K9OHHyf8A7fH/AF4a8ftlfBuzxfp4u1leP28YJX0u/k15FeRv5NcKzK4VKlQJUrhUrhUqVKlSpUqVKlSpUqVwqVKlSpUqVKlSpUqVKlSpUqVKlSpUqVKlSpUqVKlSpUrhUqVKlcKlcK+uryn6vb6Dbza8+voq8uvqNeN/RP8Awq8W/wD8hX0G3jrzzxbx+orzN/Hvx3+i2+hr6e/MuXmb/T7eEl8b8F8bm3g28i8+DfxbeG+JL434N/Bv4787bjfhvhc//9k="""

WEB_SECTOR_TO_ENGINE = {
    "Technology":"Teknologi", "Financials":"Finans", "Healthcare":"Sundhed", "Industrials":"Industri",
    "Consumer Cyclical":"Forbrug cyklisk", "Consumer Defensive":"Forbrug defensivt", "Energy":"Energi",
    "Materials":"Materialer", "Utilities":"Forsyning", "Transportation":"Transport",
    "Communication":"Kommunikation", "Other sectors":"Andre sektorer",
}
WEB_REGION_TO_ENGINE = {
    "USA":"USA", "Canada":"Canada", "Denmark":"Danmark", "Other Nordics":"Øvrige Norden", "Europe":"Europa",
    "Japan":"Japan", "China / Hong Kong":"Kina / Hongkong", "Other Asia":"Øvrige Asien",
    "Emerging Markets":"Emerging Markets", "Other countries":"Andre lande",
}
WEB_STRUCTURE_TO_ENGINE = {"Fundamental":"Fundament", "Growth":"Vækst", "Accelerator":"Accelerator", "Potential":"Potentiale"}

ENGINE_STRUCTURE_TO_DISPLAY = {
    "Fundament":"Fundamental", "Fundamental":"Fundamental",
    "Vækst":"Growth", "Growth":"Growth",
    "Accelerator":"Accelerator",
    "Potentiale":"Potential", "Potential":"Potential",
}
ENGINE_SECTOR_TO_DISPLAY = {
    "Teknologi":"Technology", "Technology":"Technology",
    "Finans":"Financials", "Financials":"Financials",
    "Sundhed":"Healthcare", "Healthcare":"Healthcare",
    "Industri":"Industrials", "Industrials":"Industrials",
    "Forbrug cyklisk":"Consumer Cyclical", "Consumer Cyclical":"Consumer Cyclical",
    "Forbrug defensivt":"Consumer Defensive", "Consumer Defensive":"Consumer Defensive",
    "Energi":"Energy", "Energy":"Energy",
    "Materialer":"Materials", "Materials":"Materials",
    "Forsyning":"Utilities", "Utilities":"Utilities",
    "Transport":"Transportation", "Transportation":"Transportation",
    "Kommunikation":"Communication", "Communication":"Communication",
    "Andre sektorer":"Other sectors", "Other sectors":"Other sectors",
    "Ukendt sektor":"Unknown sector", "Unknown sector":"Unknown sector",
}
ENGINE_REGION_TO_DISPLAY = {
    "USA":"USA", "Canada":"Canada",
    "Danmark":"Denmark", "Denmark":"Denmark",
    "Øvrige Norden":"Other Nordics", "Other Nordics":"Other Nordics",
    "Europa":"Europe", "Europe":"Europe",
    "Japan":"Japan",
    "Kina / Hongkong":"China / Hong Kong", "China / Hong Kong":"China / Hong Kong",
    "Øvrige Asien":"Other Asia", "Other Asia":"Other Asia",
    "Emerging Markets":"Emerging Markets",
    "Andre lande":"Other countries", "Other countries":"Other countries",
    "Ukendt region":"Unknown region", "Unknown region":"Unknown region",
}
def _display_structure(value):
    s=str(value or "")
    return ENGINE_STRUCTURE_TO_DISPLAY.get(s,s)
def _display_sector(value):
    s=str(value or "")
    return ENGINE_SECTOR_TO_DISPLAY.get(s,s)
def _display_region(value):
    s=str(value or "")
    return ENGINE_REGION_TO_DISPLAY.get(s,s)
def _display_category(value, kind):
    if kind=="structure_layers": return _display_structure(value)
    if kind=="sectors": return _display_sector(value)
    if kind=="regions": return _display_region(value)
    return str(value or "")
def _clip_pdf_text(value,max_chars):
    s=str(value or "")
    return s if len(s)<=max_chars else s[:max(1,max_chars-3)].rstrip()+"..."
def _user_facing_error(exc):
    msg=str(exc or "").strip()
    translations={
        "Minimumspositionerne kan ikke rummes inden for den samlede porteføljeværdi.":
            "The minimum positions cannot fit within the selected portfolio value.",
        "Aktieuniverset er tomt.":"The stock universe is empty.",
        "Aktieuniversets 'stocks' skal være en liste.":"The stock-universe file is invalid.",
    }
    if msg in translations: return translations[msg]
    if msg.startswith("Den byggede portefølje mangler Fase 0-kursdata for:"):
        return "The built portfolio is missing required market data for: "+msg.split(":",1)[1].strip()
    if re.search(r"[æøåÆØÅ]|\b(portefølje|aktier|aktie|mangler|samlede|kursdata|valutaen|understøttes)\b",msg,re.I):
        return "The portfolio could not be built with the selected settings. Please adjust the settings and try again."
    return msg
def _user_facing_progress(message):
    msg=str(message or "")
    low=msg.lower()
    if "aktieoptimering" in low: return "Optimising stock selection..."
    if "kapitaloptimering" in low: return "Optimising capital allocation..."
    if "hele aktier" in low or "afrunder" in low: return "Converting allocation to whole shares..."
    if "startportefølje" in low: return "Creating the starting portfolio..."
    if "optimering færdig" in low or "klargør resultat" in low: return "Finalising portfolio results..."
    if "gemmer" in low or "opdaterer visninger" in low: return "Preparing your portfolio report..."
    if re.search(r"[æøåÆØÅ]|\b(aktier|portefølje|bygger|færdig|indlæser|beregner)\b",msg,re.I):
        return "Building your portfolio..."
    return msg

SIMPLE_PROFILES = {
    "Balanced": {"Fundament":60.0,"Vækst":25.0,"Accelerator":10.0,"Potentiale":5.0},
    "Growth": {"Fundament":40.0,"Vækst":35.0,"Accelerator":20.0,"Potentiale":5.0},
    "High growth": {"Fundament":25.0,"Vækst":35.0,"Accelerator":30.0,"Potentiale":10.0},
}

STRUCTURE_TARGET_PROFILES = {
    "Balanced": {"Fundamental":60.0,"Growth":25.0,"Accelerator":10.0,"Potential":5.0},
    "Defensive": {"Fundamental":75.0,"Growth":20.0,"Accelerator":4.0,"Potential":1.0},
    "Quality growth": {"Fundamental":50.0,"Growth":35.0,"Accelerator":12.0,"Potential":3.0},
    "Growth": {"Fundamental":40.0,"Growth":35.0,"Accelerator":20.0,"Potential":5.0},
    "High growth": {"Fundamental":25.0,"Growth":35.0,"Accelerator":30.0,"Potential":10.0},
}

SECTOR_TARGET_PROFILES = {
    "Balanced": {"Technology":35.0,"Financials":9.0,"Healthcare":15.0,"Industrials":6.0,"Consumer Cyclical":10.0,"Consumer Defensive":5.0,"Energy":6.0,"Materials":6.0,"Utilities":3.0,"Transportation":2.0,"Communication":3.0,"Other sectors":0.0},
    "Broad diversification": {"Technology":20.0,"Financials":12.0,"Healthcare":15.0,"Industrials":12.0,"Consumer Cyclical":10.0,"Consumer Defensive":8.0,"Energy":7.0,"Materials":5.0,"Utilities":4.0,"Transportation":2.0,"Communication":5.0,"Other sectors":0.0},
    "Technology growth": {"Technology":45.0,"Financials":7.0,"Healthcare":13.0,"Industrials":6.0,"Consumer Cyclical":10.0,"Consumer Defensive":4.0,"Energy":4.0,"Materials":3.0,"Utilities":2.0,"Transportation":1.0,"Communication":5.0,"Other sectors":0.0},
    "Defensive": {"Technology":20.0,"Financials":10.0,"Healthcare":20.0,"Industrials":10.0,"Consumer Cyclical":5.0,"Consumer Defensive":15.0,"Energy":5.0,"Materials":4.0,"Utilities":6.0,"Transportation":2.0,"Communication":3.0,"Other sectors":0.0},
    "Cyclical / industrial": {"Technology":20.0,"Financials":12.0,"Healthcare":8.0,"Industrials":20.0,"Consumer Cyclical":15.0,"Consumer Defensive":5.0,"Energy":8.0,"Materials":6.0,"Utilities":2.0,"Transportation":3.0,"Communication":1.0,"Other sectors":0.0},
}

REGION_TARGET_PROFILES = {
    "Global balanced": {"USA":45.0,"Canada":5.0,"Denmark":5.0,"Other Nordics":5.0,"Europe":20.0,"Japan":5.0,"China / Hong Kong":4.0,"Other Asia":6.0,"Emerging Markets":3.0,"Other countries":2.0},
    "US tilt": {"USA":65.0,"Canada":4.0,"Denmark":3.0,"Other Nordics":3.0,"Europe":10.0,"Japan":4.0,"China / Hong Kong":3.0,"Other Asia":4.0,"Emerging Markets":2.0,"Other countries":2.0},
    "Europe / Nordics tilt": {"USA":25.0,"Canada":3.0,"Denmark":10.0,"Other Nordics":10.0,"Europe":35.0,"Japan":5.0,"China / Hong Kong":2.0,"Other Asia":4.0,"Emerging Markets":3.0,"Other countries":3.0},
    "Asia tilt": {"USA":30.0,"Canada":3.0,"Denmark":3.0,"Other Nordics":3.0,"Europe":15.0,"Japan":12.0,"China / Hong Kong":10.0,"Other Asia":15.0,"Emerging Markets":6.0,"Other countries":3.0},
    "Global ex-US tilt": {"USA":25.0,"Canada":5.0,"Denmark":5.0,"Other Nordics":5.0,"Europe":25.0,"Japan":8.0,"China / Hong Kong":7.0,"Other Asia":10.0,"Emerging Markets":7.0,"Other countries":3.0},
}

INDUSTRY_PREFERENCE_PROFILES = {
    "Neutral": {},
    "AI & software": {"Packaged Software":70.0,"Internet Software/Services":60.0,"Information Technology Services":45.0,"Data Processing Services":35.0},
    "Semiconductors": {"Semiconductors":80.0,"Electronic Production Equipment":55.0,"Electronic Components":35.0},
    "Industrial automation": {"Industrial Machinery":70.0,"Electrical Products":55.0,"Engineering & Construction":35.0,"Trucks/Construction/Farm Machinery":30.0},
    "Defense & aerospace": {"Aerospace & Defense":80.0,"Electronic Production Equipment":30.0},
    "Healthcare & biotech": {"Biotechnology":70.0,"Pharmaceuticals: Major":60.0,"Medical Specialties":45.0,"Managed Health Care":25.0},
    "Financial quality": {"Major Banks":50.0,"Property/Casualty Insurance":50.0,"Insurance Brokers/Services":45.0,"Investment Managers":35.0},
    "Energy & utilities": {"Integrated Oil":50.0,"Oil & Gas Production":65.0,"Electric Utilities":35.0},
    "Consumer": {"Internet Retail":55.0,"Specialty Stores":40.0,"Beverages: Non-Alcoholic":40.0,"Household/Personal Care":35.0,"Food Retail":30.0},
    "Real estate & infrastructure": {"Real Estate Investment Trusts":60.0,"Real Estate Development":45.0,"Engineering & Construction":35.0},
}
INDUSTRY_WEB_OPTIONS = sorted({name for profile in INDUSTRY_PREFERENCE_PROFILES.values() for name in profile})

DISCLAIMER = (
    "Alpha Portfolio Builder is a decision-support and educational tool — not financial, investment, tax or legal advice. "
    "The model uses market data, analyst estimates and programmed assumptions that can be delayed, incomplete or wrong, "
    "and the software is continuously developed and may contain errors. Use APB at your own risk, verify important information independently, "
    "and make investment decisions based on your own situation, judgement and risk tolerance. Past performance and model outputs do not guarantee future results."
)


def _apply_web_profile(prefix, selected_name, profiles, high_priority_key=None, auto_high_priority=False, all_keys=None):
    """Apply a preset on first use and whenever the dropdown changes.

    Existing user-edited values are preserved on ordinary reruns. The extra
    missing-key check prevents Streamlit's number inputs from starting at 0
    simply because the default dropdown profile has never been actively changed.
    """
    marker=f"_{prefix}_profile_applied"

    # ``Custom setup`` is a state/label, not a preset. Selecting it manually must
    # never overwrite the percentages the user is already working with.
    if str(selected_name)=="Custom setup":
        st.session_state[marker]="Custom setup"
        return

    selected=dict(profiles.get(selected_name,{}) or {})
    if all_keys is not None:
        keys=list(all_keys)
    else:
        keys=[]
        for profile_values in profiles.values():
            for key in (profile_values or {}):
                if key not in keys:
                    keys.append(key)

    missing_any=any(f"{prefix}_{key}" not in st.session_state for key in keys)
    if st.session_state.get(marker)==selected_name and not missing_any:
        return

    for key in keys:
        st.session_state[f"{prefix}_{key}"]=float(selected.get(key,0.0))
    if high_priority_key and auto_high_priority:
        st.session_state[high_priority_key]=(str(selected_name)!="Neutral")
    st.session_state[marker]=selected_name


def _keep_target_section_open(section_name):
    """Keep the active target expander open after a preset dropdown change."""
    st.session_state["_open_target_section"]=section_name


def _allocation_profile_dropdown_changed(prefix, profiles, section_name):
    """Apply the visible dropdown selection before the next expander heading is rendered.

    Streamlit callbacks run before the script reruns. Applying the preset here keeps
    the section heading, dropdown and actual percentages synchronized on the very
    first rerun after a selection. Choosing Custom setup remains non-destructive.
    """
    widget_key=_allocation_profile_widget_key(prefix)
    if widget_key:
        selected_name=st.session_state.get(widget_key)
        _apply_web_profile(prefix,selected_name,profiles)
    st.session_state["_open_target_section"]=section_name


def _ensure_web_profile_defaults(prefix, default_name, profiles, high_priority_key=None, auto_high_priority=False, all_keys=None):
    """Seed every preset-controlled field before its widget is created."""
    marker=f"_{prefix}_profile_applied"
    if all_keys is not None:
        keys=list(all_keys)
    else:
        keys=[]
        for profile_values in profiles.values():
            for key in (profile_values or {}):
                if key not in keys:
                    keys.append(key)
    selected=dict(profiles.get(default_name,{}) or {})
    for key in keys:
        st.session_state.setdefault(f"{prefix}_{key}",float(selected.get(key,0.0)))
    st.session_state.setdefault(marker,default_name)
    if high_priority_key:
        st.session_state.setdefault(
            high_priority_key,
            bool(auto_high_priority and str(default_name)!="Neutral"),
        )


def _allocation_keys(prefix, profiles):
    """Return allocation keys in stable display order."""
    keys=[]
    for profile_values in profiles.values():
        for key in (profile_values or {}):
            if key not in keys:
                keys.append(key)
    return keys


def _round_allocation_to_tenths(values, fixed_key, target=100.0):
    """Round automatic values to 0.1 while keeping the user-edited value fixed."""
    result={k:round(max(0.0,min(100.0,float(v))),1) for k,v in values.items()}
    fixed=round(max(0.0,min(100.0,float(result.get(fixed_key,0.0)))),1)
    result[fixed_key]=fixed
    others=[k for k in result if k!=fixed_key]
    if not others:
        return result
    diff=round(target-sum(result.values()),1)
    # Apply any rounding residue in 0.1 pp steps to the largest eligible values.
    guard=0
    while abs(diff)>=0.05 and guard<5000:
        guard+=1
        step=0.1 if diff>0 else -0.1
        eligible=[k for k in others if (step>0 and result[k]<100.0-1e-9) or (step<0 and result[k]>0.0+1e-9)]
        if not eligible:
            break
        k=max(eligible,key=lambda name: result[name])
        result[k]=round(result[k]+step,1)
        diff=round(target-sum(result.values()),1)
    return result


def _rebalance_100(prefix, keys, changed_key):
    """Streamlit callback: preserve the edited field and rebalance all other fields to 100%."""
    # Changing an allocation can also change the expander heading from a preset
    # name to ``Custom setup``. Because Streamlit treats a changed expander label
    # as a new widget, explicitly keep the section open for that rerun. Once the
    # heading has changed, the widget identity is stable again and the user can
    # collapse it normally.
    section_by_prefix={"str":"structure","sec":"sector","reg":"region"}
    section_name=section_by_prefix.get(prefix)
    if section_name:
        st.session_state["_open_target_section"]=section_name

    if not st.session_state.get(f"{prefix}_auto_balance",True):
        profile_map={"str":STRUCTURE_TARGET_PROFILES,"sec":SECTOR_TARGET_PROFILES,"reg":REGION_TARGET_PROFILES}
        if prefix in profile_map:
            _sync_allocation_profile_selection(prefix,profile_map[prefix])
        return
    changed_state_key=f"{prefix}_{changed_key}"
    changed=round(max(0.0,min(100.0,float(st.session_state.get(changed_state_key,0.0) or 0.0))),1)
    st.session_state[changed_state_key]=changed
    others=[k for k in keys if k!=changed_key]
    if not others:
        return
    target_other=max(0.0,100.0-changed)
    current={k:max(0.0,float(st.session_state.get(f"{prefix}_{k}",0.0) or 0.0)) for k in others}
    method=st.session_state.get(f"{prefix}_balance_method","Proportional")

    if method=="Equal":
        # Equal percentage-point adjustment. If a value reaches 0 while reducing,
        # the remaining difference is redistributed across the values still able to move.
        vals=dict(current)
        delta=target_other-sum(vals.values())
        active=set(others)
        guard=0
        while abs(delta)>1e-9 and active and guard<100:
            guard+=1
            share=delta/len(active)
            hit=[]
            for k in list(active):
                new=vals[k]+share
                if new<0.0:
                    vals[k]=0.0; hit.append(k)
                elif new>100.0:
                    vals[k]=100.0; hit.append(k)
                else:
                    vals[k]=new
            for k in hit:
                active.discard(k)
            new_delta=target_other-sum(vals.values())
            if not hit:
                delta=new_delta
                break
            delta=new_delta
        raw={changed_key:changed,**vals}
    else:
        total=sum(current.values())
        if total>1e-12:
            vals={k:(current[k]/total)*target_other for k in others}
        else:
            each=target_other/len(others)
            vals={k:each for k in others}
        raw={changed_key:changed,**vals}

    rounded=_round_allocation_to_tenths(raw,changed_key,100.0)
    for k,v in rounded.items():
        st.session_state[f"{prefix}_{k}"]=v

    profile_map={"str":STRUCTURE_TARGET_PROFILES,"sec":SECTOR_TARGET_PROFILES,"reg":REGION_TARGET_PROFILES}
    if prefix in profile_map:
        _sync_allocation_profile_selection(prefix,profile_map[prefix])


def _allocation_slider_changed(prefix, keys, changed_key):
    """Slider callback: copy the slider value to the canonical percentage field, then reuse the normal 100% rebalance logic."""
    slider_key=f"{prefix}_{changed_key}_slider"
    field_key=f"{prefix}_{changed_key}"
    value=round(max(0.0,min(100.0,float(st.session_state.get(slider_key,0.0) or 0.0))),1)
    st.session_state[field_key]=value
    _rebalance_100(prefix,keys,changed_key)


def _allocation_value_input(prefix, keys, item):
    """Render a precise number field plus a quick drag slider, kept in sync through one canonical allocation value."""
    field_key=f"{prefix}_{item}"
    slider_key=f"{field_key}_slider"

    st.number_input(
        f"{item} (%)",
        min_value=0.0,
        max_value=100.0,
        step=0.1,
        format="%.1f",
        key=field_key,
        on_change=_rebalance_100,
        args=(prefix,keys,item),
    )

    # The percentage field is canonical. Refresh the slider mirror before it is
    # instantiated on every rerun, so edits to any one value immediately show
    # the rebalanced values on all the other sliders as well.
    st.session_state[slider_key]=float(st.session_state.get(field_key,0.0) or 0.0)
    st.slider(
        f"Adjust {item}",
        min_value=0.0,
        max_value=100.0,
        step=1.0,
        key=slider_key,
        label_visibility="collapsed",
        on_change=_allocation_slider_changed,
        args=(prefix,keys,item),
        help=f"Drag to adjust {item} quickly. With automatic adjustment enabled, the other values are redistributed at the same time so the total remains 100%.",
    )


def _matching_industry_profile(profiles, tol=1e-6):
    """Return the matching Industry preset name, otherwise Custom setup."""
    for name, values in profiles.items():
        if name == "Custom setup":
            continue
        if all(abs(float(st.session_state.get(f"ind_{k}", 0.0) or 0.0) - float(values.get(k, 0.0) or 0.0)) <= tol
               for k in INDUSTRY_WEB_OPTIONS):
            return name
    return "Custom setup"


def _sync_industry_profile_selection(profiles):
    """Keep the Industry dropdown aligned with the actual manual values."""
    name=_matching_industry_profile(profiles)
    st.session_state["industry_profile"]=name
    return name


def _industry_profile_dropdown_changed(profiles):
    """Apply an Industry preset before rerender; Custom setup itself is non-destructive."""
    selected=st.session_state.get("industry_profile")
    if selected and selected != "Custom setup":
        _apply_web_profile(
            "ind",
            selected,
            profiles,
            high_priority_key="industry_high_priority",
            auto_high_priority=True,
            all_keys=INDUSTRY_WEB_OPTIONS,
        )
    st.session_state["_open_target_section"]="industry"


def _industry_value_changed(item, profiles):
    """Manual Industry edits make the dropdown reflect the actual setup."""
    _sync_industry_profile_selection(profiles)
    st.session_state["_open_target_section"]="industry"


def _industry_slider_changed(item, profiles):
    """Slider callback: copy the Industry slider value and sync preset/Custom setup."""
    slider_key=f"ind_{item}_slider"
    field_key=f"ind_{item}"
    value=max(-100.0,min(100.0,float(st.session_state.get(slider_key,0.0) or 0.0)))
    st.session_state[field_key]=value
    _sync_industry_profile_selection(profiles)
    st.session_state["_open_target_section"]="industry"


def _industry_preference_input(item, profiles):
    """Render an industry preference number field and synchronized quick-adjust slider."""
    field_key=f"ind_{item}"
    slider_key=f"{field_key}_slider"

    st.number_input(
        item,
        min_value=-100.0,
        max_value=100.0,
        step=5.0,
        format="%.0f",
        key=field_key,
        help="0 = neutral, positive = prefer, negative = avoid/reduce preference.",
        on_change=_industry_value_changed,
        args=(item,profiles),
    )

    # The number field remains canonical; mirror it into the slider on each rerun.
    st.session_state[slider_key]=float(st.session_state.get(field_key,0.0) or 0.0)
    st.slider(
        f"Adjust {item}",
        min_value=-100.0,
        max_value=100.0,
        step=5.0,
        key=slider_key,
        label_visibility="collapsed",
        on_change=_industry_slider_changed,
        args=(item,profiles),
        help=f"Drag to adjust the preference for {item}. 0 is neutral; positive values favour it and negative values reduce its preference.",
    )


def _normalize_allocation_100(prefix, keys):
    """Immediately normalize the full current allocation proportionally to exactly 100.0%."""
    values={k:max(0.0,float(st.session_state.get(f"{prefix}_{k}",0.0) or 0.0)) for k in keys}
    if not values:
        return
    total=sum(values.values())
    if total>1e-12:
        raw={k:(v/total)*100.0 for k,v in values.items()}
    else:
        each=100.0/len(values)
        raw={k:each for k in values}

    # Round to one decimal and place any 0.1 pp rounding residue on the largest value.
    rounded={k:round(v,1) for k,v in raw.items()}
    diff=round(100.0-sum(rounded.values()),1)
    guard=0
    while abs(diff)>=0.05 and guard<5000:
        guard+=1
        step=0.1 if diff>0 else -0.1
        eligible=[k for k in keys if (step>0 and rounded[k]<100.0-1e-9) or (step<0 and rounded[k]>0.0+1e-9)]
        if not eligible:
            break
        k=max(eligible,key=lambda name: rounded[name])
        rounded[k]=round(rounded[k]+step,1)
        diff=round(100.0-sum(rounded.values()),1)

    for k,v in rounded.items():
        st.session_state[f"{prefix}_{k}"]=v

    profile_map={"str":STRUCTURE_TARGET_PROFILES,"sec":SECTOR_TARGET_PROFILES,"reg":REGION_TARGET_PROFILES}
    if prefix in profile_map:
        _sync_allocation_profile_selection(prefix,profile_map[prefix])


def _auto_balance_toggled(prefix, keys):
    """Checkbox callback: turning auto-balance on immediately fixes the current allocation proportionally."""
    if st.session_state.get(f"{prefix}_auto_balance",False):
        # Switching the feature on always starts from a neutral proportional normalization.
        st.session_state[f"{prefix}_balance_method"]="Proportional"
        _normalize_allocation_100(prefix,keys)


def _allocation_total(prefix, profiles):
    """Return the displayed total for a required 100% allocation."""
    keys=_allocation_keys(prefix,profiles)
    return round(sum(float(st.session_state.get(f"{prefix}_{k}",0.0) or 0.0) for k in keys),1)


def _matching_allocation_profile(prefix, profiles, tolerance=0.05):
    """Return the preset whose complete value combination matches the current allocation.

    If the user has changed one or more values so the allocation no longer matches
    any ready-made preset, return ``Custom setup``. This is intentionally based on
    the values themselves rather than the dropdown selection.
    """
    keys=_allocation_keys(prefix,profiles)
    current={k:float(st.session_state.get(f"{prefix}_{k}",0.0) or 0.0) for k in keys}
    for profile_name,profile_values in profiles.items():
        if all(abs(current[k]-float((profile_values or {}).get(k,0.0)))<tolerance for k in keys):
            return profile_name
    return "Custom setup"


def _allocation_profile_widget_key(prefix):
    """Map allocation prefixes to their visible preset dropdown session-state keys."""
    return {"str":"structure_profile","sec":"sector_profile","reg":"region_profile"}.get(prefix)


def _sync_allocation_profile_selection(prefix, profiles):
    """Keep the preset dropdown aligned with the percentages currently on screen."""
    widget_key=_allocation_profile_widget_key(prefix)
    if not widget_key:
        return
    match=_matching_allocation_profile(prefix,profiles)
    st.session_state[widget_key]=match
    # Mark the displayed state as already accounted for. In particular, this
    # prevents ``Custom setup`` from being interpreted as a preset to apply.
    st.session_state[f"_{prefix}_profile_applied"]=match


def _profile_options(profiles):
    """Preset names plus a non-destructive Custom setup choice."""
    return list(profiles)+["Custom setup"]


def _invalid_required_allocations():
    """Return required 100% distributions that are not exactly 100.0%."""
    checks=[
        ("Structure layers","str",STRUCTURE_TARGET_PROFILES),
        ("Sector targets","sec",SECTOR_TARGET_PROFILES),
        ("Region targets","reg",REGION_TARGET_PROFILES),
    ]
    invalid=[]
    for label,prefix,profiles in checks:
        total=_allocation_total(prefix,profiles)
        if abs(total-100.0)>=0.05:
            invalid.append((label,total))
    return invalid


def _allocation_controls(prefix, profiles):
    """Render common controls/status for distributions that must total 100%."""
    keys=_allocation_keys(prefix,profiles)
    auto=st.checkbox(
        "Adjust other values automatically",
        value=True,
        key=f"{prefix}_auto_balance",
        help="Keeps the value you edit and adjusts the other values so the total remains 100%. Turning this on also immediately normalizes the current distribution to 100% proportionally.",
        on_change=_auto_balance_toggled,
        args=(prefix,keys),
    )
    if auto:
        st.radio(
            "Automatic distribution",
            ["Proportional","Equal"],
            horizontal=True,
            key=f"{prefix}_balance_method",
            help="Proportional preserves the relative weighting of the other values. Equal changes the other values by the same percentage-point amount where possible.",
        )
    else:
        total=sum(float(st.session_state.get(f"{prefix}_{k}",0.0) or 0.0) for k in keys)
        diff=round(100.0-total,1)
        if abs(diff)<0.05:
            st.success("Distributed: 100.0%")
        elif diff>0:
            st.info(f"Distributed: {total:.1f}% · {diff:.1f}% remains to be distributed")
        else:
            st.warning(f"Distributed: {total:.1f}% · {abs(diff):.1f}% must be removed")
    return keys


def _show_structure_pyramid(width=460, caption=True):
    if not STRUCTURE_PYRAMID_B64:
        return
    _,mid,_=st.columns([1.1,1.8,1.1])
    with mid:
        st.markdown(
            f'<img src="data:image/jpeg;base64,{STRUCTURE_PYRAMID_B64}" style="max-width:{int(width)}px;width:100%;height:auto;display:block;margin:0.15rem auto 0.1rem auto">',
            unsafe_allow_html=True,
        )
        if caption:
            st.caption("Structure layers set the portfolio's core risk architecture. More weight higher in the pyramid increases expected variability and risk.")


def _render_disclaimer():
    st.caption("Important: "+DISCLAIMER)


def _img(b64, width=680):
    if not b64: return ""
    return f'<img src="data:image/webp;base64,{b64}" style="max-width:{width}px;width:100%;height:auto;display:block;margin:auto">'

def _card(label,value,sub=""):
    st.markdown(f'<div class="apb-card"><div class="apb-kicker">{label}</div><div class="apb-big">{value}</div><div class="apb-subtle">{sub}</div></div>', unsafe_allow_html=True)

def _fmt(v,n=1):
    """Friendly European display: thousands dot, decimal comma."""
    try:
        raw=f"{float(v):,.{n}f}"
        return raw.replace(",","X").replace(".",",").replace("X",".")
    except Exception:
        return "–"

def _money(v):
    return _fmt(v,0)

def _parse_eu_number(value, default=0.0):
    """Parse friendly European input such as 100.000, 1.000.000 or 100.000,50."""
    try:
        s=str(value or "").strip().replace(" ","")
        if not s:
            return float(default)

        # European decimal comma: dots are thousands separators.
        if "," in s:
            s=s.replace(".","").replace(",",".")

        elif "." in s:
            parts=s.split(".")
            signless_first=parts[0].lstrip("+-")

            # Treat one or more dot-separated 3-digit groups as thousands
            # separators: 1.000, 20.000, 1.000.000, 10.000.000, etc.
            if (
                signless_first.isdigit()
                and all(part.isdigit() and len(part)==3 for part in parts[1:])
            ):
                s="".join(parts)

        return float(s)
    except Exception:
        return float(default)


def _format_eu_integer_input(value, default=0):
    number = int(round(_parse_eu_number(value, default)))
    return f"{number:,}".replace(",", ".")

def _normalize_money_widget(key, default):
    st.session_state[key] = _format_eu_integer_input(st.session_state.get(key, default), default)


def _sync_basic_number_to_slider(number_key, slider_key, maximum, integer=True, money=False):
    raw=st.session_state.get(number_key,0)
    value=_parse_eu_number(raw,0.0) if money else _safe(raw,0.0)
    value=max(0.0,min(float(maximum),value))
    if integer:
        value=int(round(value))
    st.session_state[slider_key]=value
    if money:
        st.session_state[number_key]=_format_eu_integer_input(value,0)


def _sync_basic_slider_to_number(slider_key, number_key, integer=True, money=False):
    value=_safe(st.session_state.get(slider_key,0),0.0)
    value=int(round(value)) if integer else float(value)
    st.session_state[number_key]=_format_eu_integer_input(value,0) if money else value


def _basic_number_with_slider(label,key,maximum,step,help_text,money=False):
    slider_key=f"{key}_slider"
    if key not in st.session_state:
        st.session_state[key]="0" if money else 0
    if slider_key not in st.session_state:
        raw=st.session_state.get(key,0)
        parsed=_parse_eu_number(raw,0.0) if money else _safe(raw,0.0)
        st.session_state[slider_key]=int(round(parsed))
    if money:
        st.text_input(
            label,key=key,help=help_text,
            on_change=_sync_basic_number_to_slider,args=(key,slider_key,maximum,True,True),
        )
    else:
        st.number_input(
            label,min_value=0,max_value=int(maximum),step=int(step),key=key,
            help=help_text,
            on_change=_sync_basic_number_to_slider,args=(key,slider_key,maximum,True,False),
        )
    st.slider(
        f"{label} slider",min_value=0,max_value=int(maximum),step=int(step),key=slider_key,
        label_visibility="collapsed",
        on_change=_sync_basic_slider_to_number,args=(slider_key,key,True,money),
    )

def _sync_dividend_number_to_slider():
    st.session_state["dividend_target_slider"]=float(_safe(st.session_state.get("dividend_target_pct",3.0),3.0))
    st.session_state["_open_dividend_once"]=True


def _sync_dividend_slider_to_number():
    st.session_state["dividend_target_pct"]=float(_safe(st.session_state.get("dividend_target_slider",3.0),3.0))
    st.session_state["_open_dividend_once"]=True


def _keep_dividend_open_once():
    st.session_state["_open_dividend_once"]=True


def _pct(v,n=1):
    try: return f"{float(v):.{n}f}%".replace(".",",")
    except Exception: return "–"

def _safe(v,default=0.0):
    try:
        if v is None or v == "": return default
        return float(v)
    except: return default


def order_to_settings(order):
    """Translate the existing web-input schema directly into the existing desktop builder settings."""
    _validate_current_web_order(order)
    s = _default_builder_settings()
    basic = order.get("basic_rules", {}) or {}
    currency = str(basic.get("currency","DKK") or "DKK").upper()
    rate = _builder_currency_rate_to_dkk(currency)
    s["currency"] = currency
    s["portfolio_value_input"] = max(1.0, _safe(basic.get("portfolio_value"), 100000.0))
    s["minimum_position_input"] = max(0.0, _safe(basic.get("minimum_position"), 5000.0))
    s["portfolio_value_dkk"] = s["portfolio_value_input"] * rate
    s["minimum_position_dkk"] = s["minimum_position_input"] * rate
    s["minimum_stocks_per_sector"] = max(0, int(_safe(basic.get("minimum_stocks_per_sector"), 0)))
    s["maximum_stocks"] = max(1, int(_safe(basic.get("maximum_number_of_stocks"), 15)))
    s["use_locked_stocks"] = False

    priorities = order.get("priorities", {}) or {}
    for k, aliases in WEB_PRIORITY_ALIASES.items():
        for alias in aliases:
            if alias in priorities:
                s["objective_weights"][k] = max(0.0, _safe(priorities.get(alias), s["objective_weights"].get(k,0)))
                break

    for web,val in (order.get("sectors",{}) or {}).items():
        eng=WEB_SECTOR_TO_ENGINE.get(str(web),str(web))
        if eng in s["sector_targets"]: s["sector_targets"][eng]=max(0.0,_safe(val))
    for web,val in (order.get("regions",{}) or {}).items():
        eng=WEB_REGION_TO_ENGINE.get(str(web),str(web))
        if eng in s["region_targets"]: s["region_targets"][eng]=max(0.0,_safe(val))
    for web,val in (order.get("structure_layers",{}) or {}).items():
        eng=WEB_STRUCTURE_TO_ENGINE.get(str(web),str(web))
        if eng in s["structure_targets"]: s["structure_targets"][eng]=max(0.0,_safe(val))

    s["industry_preferences"] = {str(k): clamp(_safe(v),-100.0,100.0) for k,v in (order.get("industry_preferences",{}) or {}).items()}
    # Premium web builder: price-target history/trend is intentionally disabled.
    s["use_target_trend"] = False
    s["objective_weights"]["target_trend"] = 0.0
    d = order.get("dividend",{}) or {}
    s["use_dividend_target"] = bool(d.get("enabled",False))
    s["dividend_target_pct"] = max(0.0,_safe(d.get("target_pct"),2.0))
    return s


def run_engine(order, progress=None):
    """Exact desktop optimisation chain, with web progress reporting."""
    global _builder_current_candidates_context, _builder_web_progress_hook
    settings = order_to_settings(order)
    previous_hook = _builder_web_progress_hook
    _builder_web_progress_hook = progress
    if progress: progress("Reading stock universe and cached analysis data…")
    candidates, missing, universe_total = _builder_candidate_rows()
    if not candidates:
        raise ValueError("No usable candidates were found. Upload/populate aktieunivers.json and portefolje_dagsdata_cache.json first.")
    if missing:
        raise ValueError(f"Stock universe data are incomplete: {len(candidates)} usable of {universe_total}; {len(missing)} missing/invalid.")

    target_value=settings["portfolio_value_dkk"]
    minimum=settings["minimum_position_dkk"]
    max_by_capital=max(1,int(target_value//minimum)) if minimum>0 else len(candidates)
    max_positions=min(int(settings["maximum_stocks"]),len(candidates),max_by_capital)
    _builder_current_candidates_context=candidates

    min_per_sector=int(settings.get("minimum_stocks_per_sector",0) or 0)
    if min_per_sector>0:
        hard=0
        for sector,target in settings["sector_targets"].items():
            if float(target or 0)<=0: continue
            available=sum(1 for c in candidates if c.get("sector")==sector)
            hard += min(min_per_sector, available)
        if hard>max_positions:
            raise ValueError(f"Sector minimum requires at least {hard} stocks, but maximum is {max_positions}.")

    if progress: progress(f"Creating start portfolio from {len(candidates)} candidates…")
    selected=_builder_initial_selection(candidates,settings,max_positions)
    if progress: progress("Optimising stock selection…")
    selected,selection_metrics,passes,swaps=_builder_iterative_swap_optimize(selected,candidates,settings)
    if progress: progress("Optimising capital allocation…")
    desired,final_metrics,capital_passes,capital_moves,capital_step=_builder_iterative_capital_optimize(selected,settings)
    if progress: progress("Converting allocation to whole shares…")
    built,invested,cash_dkk=_builder_values_to_whole_shares(selected,desired,settings)
    actual_values=[float(x["antal"])*float(x["_unit"]) for x in built]
    final_metrics=_builder_portfolio_metrics_weighted(selected,actual_values,settings)

    # Build customer-facing result directly from the candidate rows used by the engine.
    currency=settings["currency"]
    rate=_builder_currency_rate_to_dkk(currency)
    total_dkk=invested+cash_dkk
    phase2=[]
    result_positions=[]
    for x,c,val_dkk in zip(built,selected,actual_values):
        row=c["row"]
        weight=(val_dkk/total_dkk*100.0) if total_dkk else 0.0
        pos_value=val_dkk/rate if rate else val_dkk
        phase2.append({
            "exchange":str(x.get("exchange","") or ""),"ticker":str(x.get("ticker","") or ""),"name":str(x.get("name","") or ""),
            "trading_currency":str(row.get("currency","") or ""),"current_price":parse_float(row.get("sort_price",row.get("price")),None),
            "shares":float(x.get("antal",0) or 0),"position_value":round(pos_value,2),"portfolio_weight_pct":round(weight,4),
            "change_1d_pct":parse_float(row.get("pct_1d"),None),"sector":str(row.get("sector","") or ""),
            "industry":str(row.get("industry","") or ""),"country_region":str(row.get("country","") or ""),
            "structure_layer":str(row.get("structure_layer",c.get("layer","") or "")),
            "bear_target":parse_float(row.get("bear_target_abs"),None),"base_target":parse_float(row.get("base_target_abs"),None),"bull_target":parse_float(row.get("bull_target_abs"),None),
            "bear_1y_pct":parse_float(row.get("analyst_bear_pct"),None),"base_1y_pct":parse_float(row.get("analyst_base_pct"),None),"bull_1y_pct":parse_float(row.get("analyst_bull_pct"),None),
            "days_to_earnings":parse_float(row.get("days_to_earnings"),None),"dividend_yield_pct":parse_float(row.get("dividend_yield"),None),
            "pe":parse_float(row.get("pe"),None),"peg":parse_float(row.get("peg"),None),"revenue_growth_3y_pct":parse_float(row.get("revenue_growth_3y"),None),
            "ebit_margin_ttm_pct":parse_float(row.get("ebit_margin_ttm"),None),"roic_pct":parse_float(row.get("roic"),None),
            "fcf_margin_pct":parse_float(row.get("fcf_margin_ttm"),None),"fcf_growth_3y_pct":parse_float(row.get("fcf_growth_3y"),None),"sma50":parse_float(row.get("sma50"),None),
        })
        result_positions.append({"exchange":x.get("exchange"),"ticker":x.get("ticker"),"name":x.get("name"),"shares":float(x.get("antal",0) or 0)})

    def dist(field, targets=None, transform=lambda z:z):
        groups=defaultdict(lambda:{"w":0.0,"n":0,"base_num":0.0})
        for p in phase2:
            cat=str(transform(p.get(field) or "Unknown"))
            w=_safe(p.get("portfolio_weight_pct"))
            groups[cat]["w"]+=w; groups[cat]["n"]+=1; groups[cat]["base_num"]+=w*_safe(p.get("base_1y_pct"))
        keys=list(groups)
        if targets:
            keys=list(targets)+[k for k in keys if k not in targets]
        out=[]
        for k in keys:
            g=groups.get(k,{"w":0.0,"n":0,"base_num":0.0}); target=None if targets is None else _safe(targets.get(k))
            out.append({"category":k,"portfolio_weight_pct":round(g["w"],4),"positions":g["n"],
                        "average_base_1y_pct":None if not g["w"] else round(g["base_num"]/g["w"],4),
                        "recommended_pct":target,"deviation_pp":None if target is None else round(g["w"]-target,4)})
        return sorted(out,key=lambda r:r["portfolio_weight_pct"],reverse=True)

    sector_targets=settings["sector_targets"]
    region_targets=settings["region_targets"]
    structure_targets=settings["structure_targets"]
    phase3={
        "sectors":dist("sector",sector_targets,lambda z:mapped_sector(z)),
        "industries":dist("industry",None,lambda z:normalized_industry(z)),
        "regions":dist("country_region",region_targets,lambda z:mapped_region(z)),
        "structure_layers":dist("structure_layer",structure_targets,lambda z:structure_layer_from_display(z)),
        "pe_distribution":[],"analyst_base_distribution":[],"price_target_history":[],
    }
    access=order.get("result_access",{}) or {}
    server=order.get("server",{}) or {}
    return {
        "type":"apb_result","schema_version":"web-0.1","generated_at":datetime.now().astimezone().isoformat(timespec="seconds"),
        "user_id":str(access.get("user_id","") or ""),"access_code":str(access.get("access_code","") or ""),
        "order_number":str(server.get("order_number","") or f"APB-{secrets.token_hex(4).upper()}"),
        "customer":{"name":str(order.get("name","") or ""),"skool_username":str(order.get("skool_username","") or ""),"email":str(order.get("email","") or "")},
        "original_input":copy.deepcopy(order),
        "portfolio":{"currency":currency,"positions":result_positions,"cash":{"currency":currency,"amount":round(cash_dkk/rate if rate else cash_dkk,2),"amount_dkk":round(cash_dkk,2)},"position_count":len(result_positions)},
        "phase2":{"description":"Customer-facing portfolio data generated directly by the web engine.","positions":phase2},
        "phase3":phase3,
        "engine":{"score":round(final_metrics.get("score",0),4),"base_1y":round(final_metrics.get("base_1y",0),4),"weighted_dividend_yield_pct":round(final_metrics.get("dividend_yield",0),4),"selection_passes":passes,"swaps":swaps,"capital_passes":capital_passes,"capital_moves":capital_moves},
    }


def _current_display_username():
    """Return the user's display spelling while keeping the internal auth key stable."""
    key=str(st.session_state.get("auth_user","") or "")
    if not key or key=="admin":
        return key
    try:
        entry=_load_users().get("users",{}).get(key,{})
        return str(entry.get("display_name",key) or key)
    except Exception:
        return key


def make_order_from_ui(mode="simple"):
    # Session-state values are generated by the widgets below.
    currency=st.session_state.get("currency","Select")
    value=_parse_eu_number(st.session_state.get("portfolio_value_input",0),0.0)
    minpos=_parse_eu_number(st.session_state.get("minimum_position_input",0),0.0)
    maxstocks=int(_safe(st.session_state.get("maximum_stocks",0),0))
    minsector=int(st.session_state.get("minimum_sector",0))

    if mode=="simple":
        profile=st.session_state.get("simple_profile","Balanced")
        structure=SIMPLE_PROFILES.get(profile,SIMPLE_PROFILES["Balanced"])
        structure_web={"Fundamental":structure["Fundament"],"Growth":structure["Vækst"],"Accelerator":structure["Accelerator"],"Potential":structure["Potentiale"]}
        sectors=dict(SECTOR_TARGET_PROFILES["Balanced"])
        regions=dict(REGION_TARGET_PROFILES["Global balanced"])
        industry_preferences={}
        structure_high=sector_high=region_high=industry_high=False
        dividend_enabled=False
        dividend_high=True
        dividend_target=3.0
    else:
        structure_web={k:float(st.session_state.get(f"str_{k}",v)) for k,v in STRUCTURE_TARGET_PROFILES["Balanced"].items()}
        sectors={k:float(st.session_state.get(f"sec_{k}",v)) for k,v in SECTOR_TARGET_PROFILES["Balanced"].items()}
        regions={k:float(st.session_state.get(f"reg_{k}",v)) for k,v in REGION_TARGET_PROFILES["Global balanced"].items()}
        industry_preferences={k:float(st.session_state.get(f"ind_{k}",0.0)) for k in INDUSTRY_WEB_OPTIONS}
        industry_preferences={k:v for k,v in industry_preferences.items() if abs(v)>1e-9}
        structure_high=bool(st.session_state.get("structure_high_priority",False))
        sector_high=bool(st.session_state.get("sector_high_priority",False))
        region_high=bool(st.session_state.get("region_high_priority",False))
        industry_high=bool(st.session_state.get("industry_high_priority",False))
        dividend_enabled=bool(st.session_state.get("dividend_enabled",False))
        dividend_high=bool(st.session_state.get("dividend_high_priority",True))
        dividend_target=max(0.0,_safe(st.session_state.get("dividend_target_pct",3.0),3.0))

    return {
        "type":"apb_order","schema_version":"web-0.2","name":_current_display_username(),"skool_username":_current_display_username(),"email":"",
        "basic_rules":{"currency":currency,"portfolio_value":value,"minimum_position":minpos,"minimum_stocks_per_sector":minsector,"maximum_number_of_stocks":maxstocks},
        "priorities":{
            "Base 1Y":40.0,
            "Stock score":30.0,
            "Structure layer":250.0 if structure_high else 15.0,
            "Sectors":250.0 if sector_high else 10.0,
            "Industry":250.0 if industry_high else 7.0,
            "Regions":250.0 if region_high else 5.0,
            "Price target trend":0.0,
            "Dividend":250.0 if (dividend_enabled and dividend_high) else (10.0 if dividend_enabled else 0.0),
        },
        "sectors":sectors,"industry_preferences":industry_preferences,"regions":regions,"structure_layers":structure_web,
        "price_target_trend":{"enabled":False},"dividend":{"enabled":dividend_enabled,"target_pct":dividend_target,"high_priority":dividend_high},
        "result_access":{"user_id":"SESSION","access_code":"SESSION"},
        "server":{"order_number":f"APB-{datetime.now().strftime('%Y%m%d-%H%M%S')}","status":"built"},
    }


def _configured_admin_password():
    try:
        value = str(st.secrets.get("APB_ADMIN_PASSWORD", "") or "")
    except Exception:
        value = ""
    return value or str(os.environ.get("APB_ADMIN_PASSWORD", "") or "")


SIMGROVA_STORAGE_URL = "https://simgrova.dk/apb_api/storage.php"
REMOTE_ENGINE_FILES = {
    "aktieunivers.json",
    "portefolje_dagsdata_cache.json",
}
TIER_BUILD_LIMITS = {"Standard":5, "Premium":25, "VIP":100}


def _configured_apb_secret():
    try:
        value = str(st.secrets.get("APB_SECRET", "") or "")
    except Exception:
        value = ""
    return value or str(os.environ.get("APB_SECRET", "") or "")


def _simgrova_request(payload, timeout=30):
    secret=_configured_apb_secret()
    if not secret:
        raise RuntimeError("APB_SECRET is not configured in Streamlit secrets.")

    body=json.dumps(payload,ensure_ascii=False,separators=(",",":")).encode("utf-8")
    req=Request(
        SIMGROVA_STORAGE_URL,
        data=body,
        headers={
            "Content-Type":"application/json; charset=utf-8",
            "Accept":"application/json",
            "X-APB-SECRET":secret,
        },
        method="POST",
    )
    try:
        with urlopen(req,timeout=timeout) as response:
            raw=response.read()
            status=int(getattr(response,"status",200) or 200)
    except Exception as exc:
        # urllib raises HTTPError for 4xx/5xx; retain any useful API response.
        try:
            raw=exc.read()
            status=int(getattr(exc,"code",500) or 500)
            result=json.loads(raw.decode("utf-8"))
            detail=result.get("error") if isinstance(result,dict) else None
            err=RuntimeError(detail or f"SIMGROVA storage returned HTTP {status}.")
            setattr(err,"status_code",status)
            setattr(err,"payload",result if isinstance(result,dict) else {})
            raise err
        except RuntimeError:
            raise
        except Exception:
            raise RuntimeError(f"SIMGROVA storage could not be reached: {exc}") from exc

    try:
        result=json.loads(raw.decode("utf-8"))
    except Exception as exc:
        raise RuntimeError("SIMGROVA storage returned invalid JSON.") from exc

    if status!=200 or not isinstance(result,dict) or result.get("ok") is not True:
        detail=result.get("error") if isinstance(result,dict) else None
        err=RuntimeError(detail or f"SIMGROVA storage returned HTTP {status}.")
        setattr(err,"status_code",status)
        setattr(err,"payload",result if isinstance(result,dict) else {})
        raise err
    return result


def _remote_storage_request(action, filename, data=None, timeout=30):
    filename=str(filename or "").strip()
    if filename not in REMOTE_ENGINE_FILES:
        raise ValueError("Unsupported remote engine filename.")
    payload={"action":str(action),"filename":filename}
    if action=="write":
        payload["data"]=data
    return _simgrova_request(payload,timeout=timeout)


def _remote_save_engine_json(filename, obj):
    return _remote_storage_request("write",filename,obj,timeout=40)


def _remote_load_engine_json(filename):
    result=_remote_storage_request("read",filename,timeout=30)
    if "data" not in result:
        raise RuntimeError("SIMGROVA storage response did not contain file data.")
    return result["data"],result


def _atomic_local_json_write(path, obj):
    path=Path(path)
    tmp=path.with_name(path.name+".tmp")
    tmp.write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding="utf-8")
    tmp.replace(path)


def _restore_missing_engine_files_from_simgrova():
    """Restore only missing local engine files. Normal builds keep using local files."""
    restored=[]
    errors=[]
    for filename in sorted(REMOTE_ENGINE_FILES):
        local=Path.cwd()/filename
        if local.exists():
            continue
        try:
            obj,meta=_remote_load_engine_json(filename)
            _atomic_local_json_write(local,obj)
            restored.append(filename)
        except Exception as exc:
            errors.append((filename,str(exc)))
    return restored,errors


def _customer_month_key():
    return datetime.now().astimezone().strftime("%Y-%m")


def _tier_build_limit(tier):
    return int(TIER_BUILD_LIMITS.get(str(tier or "Standard"),1))


def _effective_build_usage(entry):
    entry=entry if isinstance(entry,dict) else {}
    month=_customer_month_key()
    used=int(entry.get("builds_used",0) or 0) if str(entry.get("build_month","") or "")==month else 0
    limit=_tier_build_limit(entry.get("tier","Standard"))
    return used,limit,month


def _format_admin_datetime(value):
    """Readable admin display; keep the stored ISO timestamp unchanged."""
    raw=str(value or "").strip()
    if not raw:
        return "–"
    try:
        dt=datetime.fromisoformat(raw.replace("Z","+00:00"))
        return dt.strftime("%d %b %Y · %H:%M")
    except Exception:
        return raw


def _remote_customers_read():
    result=_simgrova_request({"action":"customers_read"},timeout=25)
    data=result.get("data",{}) if isinstance(result,dict) else {}
    if not isinstance(data,dict) or not isinstance(data.get("users"),dict):
        data={"schema":"APB_CUSTOMERS_V1","users":{}}
    return data,bool(result.get("exists",False))


def _remote_customers_initialize(data):
    return _simgrova_request({"action":"customers_initialize","data":data},timeout=30)


def _remote_customer_create(key,entry):
    return _simgrova_request({"action":"customer_create","key":key,"entry":entry},timeout=30)


def _remote_customer_update(key,patch):
    return _simgrova_request({"action":"customer_update","key":key,"patch":patch},timeout=30)


def _remote_customer_delete(key):
    return _simgrova_request({"action":"customer_delete","key":key},timeout=30)


def _remote_customer_record_login(key):
    return _simgrova_request({"action":"customer_record_login","key":key},timeout=20)


def _remote_customer_record_build(key):
    return _simgrova_request({"action":"customer_record_build","key":key},timeout=30)


USERS_FILE = Path.cwd() / "apb_users.json"
USER_DATA_DIR = Path.cwd() / "apb_user_data"


def _load_local_users_cache():
    base={"schema":"APB_CUSTOMERS_V1","users":{}}
    try:
        if USERS_FILE.exists():
            data=json.loads(USERS_FILE.read_text(encoding="utf-8"))
            if isinstance(data,dict) and isinstance(data.get("users"),dict):
                base.update(data)
    except Exception:
        pass
    return base


def _save_local_users_cache(data):
    data=dict(data or {})
    data["schema"]="APB_CUSTOMERS_V1"
    data.setdefault("users",{})
    _atomic_local_json_write(USERS_FILE,data)


def _load_users(require_remote=False):
    """SIMGROVA customers.json is master; local apb_users.json is only a cache/fallback."""
    try:
        data,exists=_remote_customers_read()
        if not exists:
            local=_load_local_users_cache()
            if local.get("users"):
                init=_remote_customers_initialize(local)
                data=init.get("data",local)
            else:
                init=_remote_customers_initialize({"schema":"APB_CUSTOMERS_V1","users":{}})
                data=init.get("data",{"schema":"APB_CUSTOMERS_V1","users":{}})
        _save_local_users_cache(data)
        return data
    except Exception:
        if require_remote:
            raise
        return _load_local_users_cache()


def _save_users(data):
    """Compatibility helper. Customer edits should use the atomic remote actions below."""
    _save_local_users_cache(data)


def _refresh_users_cache_from_payload(result):
    data=(result or {}).get("data") if isinstance(result,dict) else None
    if isinstance(data,dict) and isinstance(data.get("users"),dict):
        _save_local_users_cache(data)
        return data
    return None

def _hash_password(password, salt_hex=None):
    salt=bytes.fromhex(salt_hex) if salt_hex else secrets.token_bytes(16)
    digest=hashlib.pbkdf2_hmac("sha256",str(password).encode("utf-8"),salt,180000)
    return salt.hex(),digest.hex()


def _verify_password(password, entry):
    try:
        salt=str(entry.get("salt","")); expected=str(entry.get("password_hash",""))
        _,actual=_hash_password(password,salt)
        return bool(expected) and hmac.compare_digest(actual,expected)
    except Exception:
        return False


def _safe_username(value):
    """Normalize a username without destroying Danish/Unicode letters.

    Letters and digits from Unicode are preserved (so Jørgen/Søren/Åge work),
    spaces and unsupported punctuation are converted to underscores.
    """
    text=unicodedata.normalize("NFKC",str(value or "")).strip()
    out=[]
    for ch in text:
        if ch.isalnum() or ch in "_.-":
            out.append(ch)
        elif ch.isspace():
            out.append("_")
        else:
            out.append("_")
    value=re.sub(r"_+","_","".join(out)).strip("_")
    return value[:64]


def _username_identity(value):
    """Case-insensitive identity used for duplicate checks and login."""
    return unicodedata.normalize("NFKC",_safe_username(value)).casefold()


def _find_user_key(users, entered_username):
    wanted=_username_identity(entered_username)
    if not wanted:
        return None
    for key,entry in (users or {}).items():
        display=(entry or {}).get("display_name",key) if isinstance(entry,dict) else key
        if _username_identity(key)==wanted or _username_identity(display)==wanted:
            return key
    return None


def _record_login(username):
    try:
        result=_remote_customer_record_login(username)
        _refresh_users_cache_from_payload(result)
    except Exception:
        # A login remains usable if the counter write alone fails.
        pass


def _save_premium_user_data(username, order, result):
    """Keep the latest result locally; build entitlement itself is stored in customers.json."""
    username=_safe_username(username)
    if not username:
        return
    USER_DATA_DIR.mkdir(exist_ok=True)
    payload={
        "schema":"APB_USER_DATA_V1",
        "username":username,
        "saved_at":datetime.now().astimezone().isoformat(timespec="seconds"),
        "latest_order":order,
        "latest_result":result
    }
    tmp=USER_DATA_DIR/(username+".tmp")
    dest=USER_DATA_DIR/(username+".json")
    tmp.write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding="utf-8")
    tmp.replace(dest)


def login_screen():
    if COVER_IMAGE_B64:
        _,mid,_=st.columns([1.7,3.6,1.7])
        with mid:
            st.markdown(_img(COVER_IMAGE_B64,600),unsafe_allow_html=True)
    st.markdown('<div class="apb-login-gap"></div>',unsafe_allow_html=True)

    left,mid,right=st.columns([1.35,1.5,1.35])
    with mid:
        with st.container(border=True):
            st.markdown(
                '<div class="apb-login-title">Welcome to Alpha Portfolio Builder</div>'
                '<div class="apb-login-subtitle">Sign in to access your portfolio builder.</div>',
                unsafe_allow_html=True,
            )
            # Give the browser genuinely new login inputs after a logout. Streamlit's
            # normal rerun otherwise reuses the same widget identities, which can prevent
            # browser password-manager/autofill suggestions from appearing again.
            login_nonce=int(st.session_state.get("login_nonce",0) or 0)
            username=st.text_input("Username",key=f"login_username_{login_nonce}")
            password=st.text_input("Password",type="password",key=f"login_password_{login_nonce}")

            # Browser password managers can visually autofill Streamlit inputs without
            # firing the DOM input/change events that Streamlit needs to update its
            # server-side widget state. The small hidden component below watches the
            # actual parent-page login inputs and re-dispatches those events whenever
            # autofill changes their DOM values. This is especially important after
            # an in-app logout, where no full browser navigation occurs.
            components.html(
                r"""
<script>
(function () {
  function syncLoginFields() {
    try {
      const win = window.parent;
      const doc = win.document;
      const user = doc.querySelector('input[aria-label="Username"]');
      const pass = doc.querySelector('input[aria-label="Password"]');
      if (!win.__apbAutofillSynced) {
        win.__apbAutofillSynced = { username: "", password: "" };
      }

      [[user, "username"], [pass, "password"]].forEach(function (pair) {
        const el = pair[0];
        const key = pair[1];
        if (!el) return;
        const value = el.value || "";
        // Ignore normal empty fields. Only a real value needs autofill repair.
        if (!value || win.__apbAutofillSynced[key] === value) return;
        win.__apbAutofillSynced[key] = value;

        // Re-emit the browser-filled value through the events Streamlit listens for.
        el.dispatchEvent(new Event("input", { bubbles: true }));
        el.dispatchEvent(new Event("change", { bubbles: true }));
      });
    } catch (e) {}
  }

  // Password managers may fill immediately or a few seconds after a selection.
  // Polling avoids permanent event listeners on Streamlit's parent document.
  let runs = 0;
  const timer = setInterval(function () {
    syncLoginFields();
    runs += 1;
    if (runs >= 150) clearInterval(timer);
  }, 200);
})();
</script>
                """,
                height=0,
            )

            if st.button("LOG IN",type="primary",use_container_width=True):
                entered=str(username or "").strip()

                # Hidden admin route: only the reserved username Admin invokes it.
                if entered.casefold()=="admin":
                    configured=_configured_admin_password()
                    if configured and hmac.compare_digest(password,configured):
                        st.session_state.auth_user="admin"
                        st.session_state.auth_tier="Admin"
                        st.session_state.pop("_open_target_section",None)
                        st.rerun()
                    st.error(
                        "Login unsuccessful. Please check your username and password. "
                        "If you still can’t access APB, send a message in the Skool community and we’ll help you."
                    )
                else:
                    users=_load_users(require_remote=True).get("users",{})
                    key=_find_user_key(users,entered)
                    entry=users.get(key) if key is not None else None
                    if (
                        not isinstance(entry,dict)
                        or not bool(entry.get("active",True))
                        or not _verify_password(password,entry)
                    ):
                        st.error(
                            "Login unsuccessful. Please check your username and password. "
                            "If you still can’t access APB, send a message in the Skool community and we’ll help you."
                        )
                    else:
                        _record_login(key)
                        st.session_state.auth_user=key
                        st.session_state.auth_tier=str(entry.get("tier","Standard"))
                        st.session_state.pop("_open_target_section",None)
                        st.rerun()

            st.divider()
            st.markdown("**Alpha Portfolio Builder Community**")
            st.caption(
                "Visit the Skool community for access information, updates, guides and discussions."
            )
            st.link_button(
                "OPEN COMMUNITY →",
                "https://www.skool.com/alpha-portfolio-builder-8372/about",
                use_container_width=True,
            )

    _render_disclaimer()


def _build_portfolio_pdf(result):
    """Create a customer-facing APB portfolio report with explanatory context and risk disclaimer."""
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4, landscape
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.pdfbase.pdfmetrics import stringWidth
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak

    portfolio=result.get("portfolio",{}) or {}
    phase2=result.get("phase2",{}) or {}
    phase3=result.get("phase3",{}) or {}
    positions=phase2.get("positions",[]) or []
    ccy=portfolio.get("currency","DKK")
    cash=_safe((portfolio.get("cash",{}) or {}).get("amount"))
    total=sum(_safe(x.get("position_value")) for x in positions)+cash
    invested=sum(_safe(x.get("position_value")) for x in positions)
    weighted=lambda field: (sum(_safe(x.get("position_value"))*_safe(x.get(field)) for x in positions)/invested) if invested else None

    buf=io.BytesIO()
    doc=SimpleDocTemplate(buf,pagesize=landscape(A4),rightMargin=12*mm,leftMargin=12*mm,topMargin=12*mm,bottomMargin=17*mm,
                          title="Alpha Portfolio Builder - Portfolio Report")
    styles=getSampleStyleSheet()
    title=ParagraphStyle('APBTitle',parent=styles['Title'],fontName='Helvetica-Bold',fontSize=22,leading=26,textColor=colors.HexColor('#0b2545'),spaceAfter=4*mm)
    sub=ParagraphStyle('APBSub',parent=styles['Normal'],fontSize=9,leading=12,textColor=colors.HexColor('#52606d'))
    body=ParagraphStyle('APBBody',parent=styles['Normal'],fontSize=8.5,leading=12,textColor=colors.HexColor('#334155'),spaceAfter=2*mm)
    h2=ParagraphStyle('APBH2',parent=styles['Heading2'],fontName='Helvetica-Bold',fontSize=13,textColor=colors.HexColor('#0b2545'),spaceBefore=3*mm,spaceAfter=2*mm)
    small=ParagraphStyle('APBSmall',parent=styles['Normal'],fontSize=7.2,leading=9.5,textColor=colors.HexColor('#52606d'))

    story=[Paragraph('ALPHA PORTFOLIO BUILDER',title),Paragraph('Portfolio Report',styles['Heading2'])]
    order=result.get('order_number') or ''
    created=result.get('created_at') or result.get('generated_at') or datetime.now().strftime('%Y-%m-%d %H:%M')
    story += [Paragraph(f"{order} &nbsp;&nbsp; | &nbsp;&nbsp; Generated: {created}",sub),Spacer(1,2*mm)]
    story.append(Paragraph(
        "APB builds a model portfolio by balancing portfolio structure, diversification and company-level analysis. "
        "The output is a starting point for your own judgement — not a recommendation to buy or sell any security.", body
    ))

    summary=[
        ['Portfolio value',f"{_money(total)} {ccy}",'Positions',str(len(positions)),'Engine score',_fmt((result.get('engine',{}) or {}).get('score'),1)],
        ['Cash',f"{_money(cash)} {ccy}",'Currency',str(ccy),'',''],
        ['Weighted Bear 1Y',_pct(weighted('bear_1y_pct'),1),'Weighted Base 1Y',_pct(weighted('base_1y_pct'),1),'Weighted Bull 1Y',_pct(weighted('bull_1y_pct'),1)],
        ['Weighted dividend yield',_pct(weighted('dividend_yield_pct'),2),'Dividend target',(_pct(((result.get('original_input',{}) or {}).get('dividend',{}) or {}).get('target_pct'),1) if ((result.get('original_input',{}) or {}).get('dividend',{}) or {}).get('enabled') else 'Off'),'Dividend priority',(('High' if ((result.get('original_input',{}) or {}).get('dividend',{}) or {}).get('high_priority') else 'Normal') if ((result.get('original_input',{}) or {}).get('dividend',{}) or {}).get('enabled') else '–')],
    ]
    t=Table(summary,colWidths=[42*mm,24*mm,42*mm,24*mm,42*mm,24*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),colors.HexColor('#f5f8fc')),
        ('BOX',(0,0),(-1,-1),0.5,colors.HexColor('#c9d7e8')),
        ('INNERGRID',(0,0),(-1,-1),0.25,colors.HexColor('#dce5ef')),
        ('FONTNAME',(0,0),(-1,-1),'Helvetica'),
        ('FONTNAME',(0,0),(0,-1),'Helvetica-Bold'),
        ('FONTNAME',(2,0),(2,-1),'Helvetica-Bold'),
        ('FONTNAME',(4,0),(4,-1),'Helvetica-Bold'),
        ('FONTSIZE',(0,0),(-1,-1),8.5),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,-1),5),
        ('BOTTOMPADDING',(0,0),(-1,-1),5),
    ]))
    story += [t,Spacer(1,4*mm),Paragraph('Built portfolio',h2),Paragraph('Positions are shown by model portfolio weight. Bear, Base and Bull are analyst 1-year scenarios used as inputs — not guaranteed outcomes.',small)]

    headers=['#','Name','Ticker','Exchange','Shares',f'Value ({ccy})','%PF','Structure','Sector','Dividend %','Bear 1Y','Base 1Y','Bull 1Y']
    data=[headers]
    for i,x in enumerate(sorted(positions,key=lambda z:_safe(z.get('portfolio_weight_pct')),reverse=True),1):
        data.append([i,_clip_pdf_text(x.get('name'),28),str(x.get('ticker') or ''),str(x.get('exchange') or ''),_fmt(x.get('shares'),0),_money(x.get('position_value')),_pct(x.get('portfolio_weight_pct'),1),_display_structure(x.get('structure_layer')),_clip_pdf_text(_display_sector(x.get('sector')),20),_pct(x.get('dividend_yield_pct'),2),_pct(x.get('bear_1y_pct'),1),_pct(x.get('base_1y_pct'),1),_pct(x.get('bull_1y_pct'),1)])
    widths=[7,31,15,17,12,21,12,22,25,17,16,16,16]
    pt=Table(data,repeatRows=1,colWidths=[w*mm for w in widths])
    pt.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#0b4f9c')),('TEXTCOLOR',(0,0),(-1,0),colors.white),('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('FONTNAME',(0,1),(-1,-1),'Helvetica'),('FONTSIZE',(0,0),(-1,-1),7),('GRID',(0,0),(-1,-1),0.25,colors.HexColor('#d7e0ea')),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f7f9fc')]),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('ALIGN',(0,0),(0,-1),'CENTER'),('ALIGN',(4,1),(6,-1),'RIGHT'),('ALIGN',(9,1),(12,-1),'RIGHT'),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4)]))
    story.append(pt)


    def distribution(title_text,key,explanation):
        rows=phase3.get(key,[]) or []
        if not rows: return
        story.append(Paragraph(title_text,h2))
        story.append(Paragraph(explanation,small))
        d=[['Category','Actual %','Target %','Deviation pp','Positions']]
        for r in rows:
            d.append([
                _display_category(r.get('category'),key),
                _pct(r.get('portfolio_weight_pct'),1),
                _pct(r.get('recommended_pct'),1),
                (f"{_fmt(r.get('deviation_pp'),1)} pp" if r.get('deviation_pp') is not None else "–"),
                str(r.get('positions') or '')
            ])
        natural_widths=[]
        for col_idx in range(len(d[0])):
            widest=0.0
            for row_idx,row in enumerate(d):
                value=str(row[col_idx] if col_idx < len(row) else "")
                font="Helvetica-Bold" if row_idx==0 else "Helvetica"
                widest=max(widest,stringWidth(value,font,8))
            natural_widths.append(widest + 16)
        min_widths=[42*mm,20*mm,20*mm,24*mm,20*mm]
        max_widths=[68*mm,34*mm,34*mm,38*mm,30*mm]
        smart_widths=[max(min_widths[i],min(natural_widths[i],max_widths[i])) for i in range(len(natural_widths))]
        tt=Table(d,repeatRows=1,colWidths=smart_widths,hAlign='LEFT')
        tt.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#eaf2fb')),('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('FONTSIZE',(0,0),(-1,-1),8),('GRID',(0,0),(-1,-1),0.25,colors.HexColor('#d7e0ea')),('ALIGN',(1,1),(-1,-1),'RIGHT'),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4)]))

        story.append(tt)
        story.append(Spacer(1,4*mm))

    # Keep page 1 focused on the portfolio itself. Allocation analysis starts on page 2.
    story.append(PageBreak())
    distribution('Structure layers','structure_layers','Actual allocation compared with the selected targets.')
    distribution('Sector allocation','sectors','Sector targets guide diversification without forcing the engine to ignore company quality and available opportunities.')
    distribution('Regional allocation','regions','Regional targets help control geographic concentration. High-priority settings, when used, intentionally give these targets much greater influence.')
    story += [Spacer(1,4*mm),Paragraph('<b>Important disclaimer</b>',small),Paragraph(DISCLAIMER,small)]

    def footer(canvas,doc_obj):
        canvas.saveState()
        canvas.setFont('Helvetica',6.2)
        canvas.setFillColor(colors.HexColor('#667085'))
        footer_text='APB decision-support tool — use at your own risk. Verify important data independently. Page %d' % doc_obj.page
        canvas.drawString(12*mm,7*mm,footer_text)
        canvas.restoreState()

    doc.build(story,onFirstPage=footer,onLaterPages=footer)
    return buf.getvalue()



def _compact_result_dataframe(df, hide_index=True, max_height=None):
    """Show result tables with content-driven column widths instead of stretching them."""
    df=pd.DataFrame(df).copy()
    configs={}
    for col in df.columns:
        values=[str(col)]
        values.extend(str(v) for v in df[col].fillna("").astype(str).tolist())
        longest=max((len(v) for v in values),default=len(str(col)))
        px=max(64,min(300,22+longest*7))
        configs[col]=st.column_config.Column(str(col),width=px)
    kwargs={
        "hide_index":hide_index,
        "use_container_width":False,
        "column_config":configs,
    }
    if max_height is not None:
        kwargs["height"]=max_height
    st.dataframe(df,**kwargs)

def show_result(result):
    portfolio=result.get("portfolio",{}); phase2=result.get("phase2",{}); phase3=result.get("phase3",{}); positions=phase2.get("positions",[]); ccy=portfolio.get("currency","DKK")
    st.success("Portfolio built successfully.")
    st.caption("The portfolio below is the engine's best fit to your selected structure and diversification targets within the available stock universe. Treat it as a decision-support starting point, not an automatic investment instruction.")

    # Make the report available immediately, before the user scrolls through the result.
    try:
        pdf_bytes=_build_portfolio_pdf(result)
        st.download_button(
            "DOWNLOAD PORTFOLIO PDF",
            pdf_bytes,
            file_name=f"{result.get('order_number','APB')}_Portfolio.pdf",
            mime="application/pdf",
            type="primary",
        )
    except Exception as exc:
        st.warning(f"PDF report could not be created: {exc}")

    total=sum(_safe(p.get("position_value")) for p in positions)+_safe(portfolio.get("cash",{}).get("amount"))
    denom=sum(_safe(p.get("position_value")) for p in positions)
    weighted=lambda field: (sum(_safe(p.get("position_value"))*_safe(p.get(field)) for p in positions)/denom) if denom else None
    c1,c2,c3=st.columns(3)
    with c1:_card("Portfolio value",f"{_money(total)} {ccy}",f"{len(positions)} positions")
    with c2:_card("Cash",f"{_money(portfolio.get('cash',{}).get('amount'))} {ccy}","Uninvested balance")
    with c3:_card("Engine score",_fmt(result.get("engine",{}).get("score"),1),"Portfolio optimisation")
    st.write("")
    s1,s2,s3,s4=st.columns(4)
    with s1:_card("Weighted Bear 1Y",_pct(weighted("bear_1y_pct"),1),"Analyst bear case")
    with s2:_card("Weighted Base 1Y",_pct(weighted("base_1y_pct"),1),"Analyst base case")
    with s3:_card("Weighted Bull 1Y",_pct(weighted("bull_1y_pct"),1),"Analyst bull case")
    with s4:_card("Weighted dividend yield",_pct(weighted("dividend_yield_pct"),2),"Portfolio-weighted annual yield")
    st.write("")
    st.subheader("Built portfolio")
    st.caption("Bear, Base and Bull show analyst 1-year scenarios used by APB. Structure is the model-assigned risk layer for each position.")
    rows=[]
    sorted_positions=sorted(positions,key=lambda x:_safe(x.get("portfolio_weight_pct")),reverse=True)
    for position_no,p in enumerate(sorted_positions,start=1):
        rows.append({"#":position_no,"Name":p.get("name"),"Ticker":p.get("ticker"),"Exchange":p.get("exchange"),"Shares":_fmt(p.get("shares"),0),"Value":f"{_money(p.get('position_value'))} {ccy}","%PF":_pct(p.get("portfolio_weight_pct"),1),"Structure":_display_structure(p.get("structure_layer")),"Sector":_display_sector(p.get("sector")),"Dividend %":_pct(p.get("dividend_yield_pct"),2),"Bear 1Y":_pct(p.get("bear_1y_pct"),1),"Base 1Y":_pct(p.get("base_1y_pct"),1),"Bull 1Y":_pct(p.get("bull_1y_pct"),1)})
    st.dataframe(pd.DataFrame(rows),use_container_width=True,height=38+35*max(1,len(rows)),hide_index=True)
    tabs=st.tabs(["Structure","Sectors","Regions","Input / Results"])
    explanations={
        "structure_layers":"Structure layers are the portfolio's risk architecture. The target mix is especially important because it determines how much of the portfolio is allocated to lower- versus higher-risk company profiles.",
        "sectors":"Sector targets control concentration across the economy. They guide the optimiser while still allowing stronger individual companies to compete for weight.",
        "regions":"Regional targets control geographic concentration. Actual allocations can differ when the available stock universe or higher-priority constraints make an exact match unattractive or impossible.",
    }
    for tab,key,label in [(tabs[0],"structure_layers","Structure layers"),(tabs[1],"sectors","Sectors"),(tabs[2],"regions","Regions")]:
        with tab:
            st.caption(explanations[key])
            data=phase3.get(key,[])
            if data:
                df=pd.DataFrame(data)[["category","portfolio_weight_pct","recommended_pct","deviation_pp","positions"]].copy()
                df["category"]=df["category"].map(lambda value:_display_category(value,key))
                for col in ("portfolio_weight_pct","recommended_pct","deviation_pp"):
                    df[col]=pd.to_numeric(df[col],errors="coerce").round(1)
                df.columns=[label,"Actual %","Target %","Deviation pp","Positions"]
                _compact_result_dataframe(df,hide_index=True)
    with tabs[3]:
        original=result.get("original_input",{}) or {}
        basic=original.get("basic_rules",{}) or {}
        st.caption("This page records the main inputs used for the build and a few high-level outputs, so the result can be understood and reproduced later.")
        st.markdown("**Input settings**")
        input_rows=[
            {"Setting":"Currency","Value":str(basic.get("currency",ccy) or ccy)},
            {"Setting":"Capital available for portfolio build","Value":f"{_money(basic.get('portfolio_value'))} {ccy}"},
            {"Setting":"Minimum value per stock position","Value":f"{_money(basic.get('minimum_position'))} {ccy}"},
            {"Setting":"Number of different stocks","Value":_fmt(basic.get("maximum_number_of_stocks"),0)},
            {"Setting":"Minimum stocks per sector","Value":_fmt(basic.get("minimum_stocks_per_sector"),0)},
            {"Setting":"Dividend preference","Value":("On" if (original.get("dividend",{}) or {}).get("enabled") else "Off")},
            {"Setting":"Dividend target","Value":(_pct((original.get("dividend",{}) or {}).get("target_pct"),1) if (original.get("dividend",{}) or {}).get("enabled") else "–")},
            {"Setting":"Dividend priority","Value":("High" if (original.get("dividend",{}) or {}).get("high_priority") else "Normal") if (original.get("dividend",{}) or {}).get("enabled") else "–"},
        ]
        _compact_result_dataframe(pd.DataFrame(input_rows),hide_index=True)

        st.markdown("**Build results**")
        result_rows=[
            {"Result":"Positions","Value":str(len(positions))},
            {"Result":"Cash","Value":f"{_money(portfolio.get('cash',{}).get('amount'))} {ccy}"},
            {"Result":"Weighted Bear 1Y","Value":_pct(weighted("bear_1y_pct"),1)},
            {"Result":"Weighted Base 1Y","Value":_pct(weighted("base_1y_pct"),1)},
            {"Result":"Weighted Bull 1Y","Value":_pct(weighted("bull_1y_pct"),1)},
            {"Result":"Weighted dividend yield","Value":_pct(weighted("dividend_yield_pct"),2)},
            {"Result":"Engine score","Value":_fmt(result.get("engine",{}).get("score"),1)},
            {"Result":"Build ID","Value":str(result.get("order_number","") or "")},
        ]
        _compact_result_dataframe(pd.DataFrame(result_rows),hide_index=True)
    _render_disclaimer()


def admin_panel():
    st.subheader("Administration")
    user_tab,data_tab=st.tabs(["Users","Engine data"])
    with user_tab:
        users_data=_load_users(require_remote=True); users=users_data.setdefault("users",{})
        st.caption("Create test accounts and see who has logged in or built a portfolio.")
        with st.expander("Create user",expanded=not bool(users)):
            nonce=int(st.session_state.get("create_user_nonce",0) or 0)
            a,b,c=st.columns(3)
            with a: new_user=st.text_input("Username",key=f"new_user_{nonce}")
            with b: new_tier=st.selectbox("Tier",["Standard","Premium","VIP"],key=f"new_tier_{nonce}")
            with c: new_pw=st.text_input("Password",type="password",key=f"new_pw_{nonce}")
            if st.button("Create user",type="primary",key=f"create_user_button_{nonce}"):
                display_name=_safe_username(new_user)
                existing_key=_find_user_key(users,display_name)
                if not display_name or len(new_pw)<4:
                    st.error("Use a username and a password of at least 4 characters.")
                elif existing_key is not None:
                    st.error("Username already exists.")
                else:
                    # Store a stable case-folded key, but keep the user's spelling for display.
                    key=_username_identity(display_name)
                    salt,digest=_hash_password(new_pw)
                    entry={
                        "display_name":display_name,
                        "tier":new_tier,
                        "active":True,
                        "salt":salt,
                        "password_hash":digest,
                        "created_at":datetime.now().astimezone().isoformat(timespec="seconds"),
                        "last_login":"",
                        "login_count":0,
                        "last_build":"",
                        "has_saved_data":False,
                        "build_month":"",
                        "builds_used":0,
                        "total_builds":0,
                    }
                    try:
                        remote=_remote_customer_create(key,entry)
                        _refresh_users_cache_from_payload(remote)
                        st.session_state.create_user_nonce=nonce+1
                        st.session_state.create_user_flash=f"Created {display_name} ({new_tier})."
                        st.rerun()
                    except Exception as exc:
                        st.error(f"Customer could not be saved at SIMGROVA: {exc}")
        flash=st.session_state.pop("create_user_flash",None)
        if flash:
            st.success(flash)
        if users:
            rows=[]
            ordered_keys=sorted(users,key=lambda k:str((users.get(k) or {}).get("display_name",k)).casefold())
            for name in ordered_keys:
                e=users[name]
                display_name=e.get("display_name",name)
                used,limit,_month=_effective_build_usage(e)
                rows.append({
                    "Username":display_name,
                    "Tier":e.get("tier"),
                    "Builds this month":f"{used} / {limit}",
                    "Total builds":int(e.get("total_builds",0) or 0),
                    "Active":bool(e.get("active",True)),
                    "Logins":int(e.get("login_count",0) or 0),
                    "Last login":_format_admin_datetime(e.get("last_login","")),
                    "Last build":_format_admin_datetime(e.get("last_build","")),
                })
            st.dataframe(pd.DataFrame(rows),use_container_width=True,hide_index=True)
            labels={k:str((users.get(k) or {}).get("display_name",k)) for k in ordered_keys}
            chosen=st.selectbox("Manage user",[None]+ordered_keys,format_func=lambda k:"–" if k is None else labels.get(k,k),key="manage_user")
            if chosen is not None:
                e=users[chosen]; c1,c2,c3=st.columns(3)
                with c1: tier=st.selectbox("Tier",["Standard","Premium","VIP"],index={"Standard":0,"Premium":1,"VIP":2}.get(str(e.get("tier","Standard")),0),key="manage_tier")
                with c2: active=st.checkbox("Active",value=bool(e.get("active",True)),key="manage_active")
                with c3: reset_pw=st.text_input("New password (optional)",type="password",key="manage_pw")
                if st.button("Save user"):
                    patch={"tier":tier,"active":active}
                    if reset_pw:
                        salt,digest=_hash_password(reset_pw)
                        patch["salt"]=salt
                        patch["password_hash"]=digest
                    try:
                        remote=_remote_customer_update(chosen,patch)
                        _refresh_users_cache_from_payload(remote)
                        st.success("User updated.")
                        st.rerun()
                    except Exception as exc:
                        st.error(f"Customer could not be updated at SIMGROVA: {exc}")

                st.divider()
                st.markdown("**Delete user**")
                st.caption(
                    "Permanently removes the user and the stored login/build history from customers.json."
                )
                confirm_delete=st.checkbox(
                    f"Confirm permanent deletion of {labels.get(chosen,chosen)}",
                    key=f"confirm_delete_{chosen}",
                )
                if st.button(
                    "DELETE USER",
                    type="secondary",
                    disabled=not confirm_delete,
                    key=f"delete_user_{chosen}",
                ):
                    try:
                        remote=_remote_customer_delete(chosen)
                        _refresh_users_cache_from_payload(remote)
                        # Remove any local cached result file for the deleted user as well.
                        try:
                            cached=USER_DATA_DIR/(str(chosen)+".json")
                            if cached.exists():
                                cached.unlink()
                        except Exception:
                            pass
                        st.success(f"Deleted {labels.get(chosen,chosen)}.")
                        st.rerun()
                    except Exception as exc:
                        st.error(f"Customer could not be deleted at SIMGROVA: {exc}")
    with data_tab:
        st.caption(
            "Engine files are used locally for fast builds and backed up persistently at SIMGROVA. "
            "Builder users cannot upload files. Maximum 10 MB each."
        )
        targets=[("Stock universe","aktieunivers.json"),("Daily analysis cache","portefolje_dagsdata_cache.json")]
        for label,fn in targets:
            col1,col2=st.columns([3,1])
            with col1:
                up=st.file_uploader(label,type=["json"],key=f"up_{fn}")
            with col2:
                p=Path.cwd()/fn
                st.caption(f"{'✓ Local' if p.exists() else '– Local'}")
                st.caption(fn)

            if up is not None:
                try:
                    raw=up.getvalue()
                    if len(raw)>10*1024*1024:
                        raise ValueError("File is larger than the 10 MB admin upload limit.")
                    obj=json.loads(raw.decode("utf-8"))

                    # Local active copy first: builds remain fast and immediately usable.
                    _atomic_local_json_write(Path.cwd()/fn,obj)

                    # Persistent SIMGROVA backup/master copy.
                    try:
                        remote=_remote_save_engine_json(fn,obj)
                        st.success(
                            f"Saved {fn} locally and at SIMGROVA "
                            f"({int(remote.get('size_bytes',0) or 0):,} bytes)."
                        )
                    except Exception as remote_exc:
                        st.warning(
                            f"{fn} was saved locally, but the SIMGROVA backup failed: {remote_exc}"
                        )
                except Exception as exc:
                    st.error(f"Invalid JSON: {exc}")

        st.divider()
        if st.button("TEST / RESTORE FROM SIMGROVA"):
            restored,errors=_restore_missing_engine_files_from_simgrova()
            if restored:
                st.success("Restored: "+", ".join(restored))
            elif not errors:
                st.info("Both local engine files already exist. Nothing needed restoring.")
            for filename,error in errors:
                st.warning(f"{filename}: {error}")




def _basic_money_step(storage_key, delta):
    """Adjust a formatted whole-money field while keeping European thousands separators."""
    value = int(round(_parse_eu_number(st.session_state.get(storage_key, "0"), 0)))
    value = max(0, value + int(delta))
    st.session_state[storage_key] = _format_eu_integer_input(value, 0)


def _basic_money_field(label, storage_key, step, help_text):
    """Formatted money text input with compact inline +/- controls."""
    if storage_key not in st.session_state:
        st.session_state[storage_key] = "0"

    st.text_input(
        label,
        key=storage_key,
        help=help_text,
        on_change=_normalize_money_widget,
        args=(storage_key, 0),
    )
    # Buttons are rendered normally but CSS positions them inside the field,
    # matching the compact controls of Streamlit's native number_input.
    st.button(
        "−",
        key=f"{storage_key}_minus",
        on_click=_basic_money_step,
        args=(storage_key, -int(step)),
    )
    st.button(
        "+",
        key=f"{storage_key}_plus",
        on_click=_basic_money_step,
        args=(storage_key, int(step)),
    )


def render_builder():
    if st.session_state.get("result_data") is not None:
        if st.button("← Build another portfolio"):
            st.session_state.result_data=None
            st.session_state["_open_target_section"]=None
            st.session_state.pop("_open_dividend_once",None)
            st.rerun()
        show_result(st.session_state.result_data)
        return

    if COVER_IMAGE_B64:
        _,mid,_=st.columns([1.5,4,1.5])
        with mid: st.markdown(_img(COVER_IMAGE_B64,660),unsafe_allow_html=True)
    st.subheader("Build your portfolio")
    st.caption("Set the capital available for the portfolio, the number of different stocks and the portfolio's risk/diversification targets. APB then searches the available universe for the strongest overall fit.")

    if not st.session_state.get("_basic_rules_v018_initialized",False):
        st.session_state["currency"]="Select"
        st.session_state["portfolio_value_input"]="0"
        st.session_state["minimum_position_input"]="0"
        st.session_state["maximum_stocks"]=0
        st.session_state["_basic_rules_v018_initialized"]=True

    # A confirmed automatic reduction is applied before the number_input widget
    # is instantiated. Streamlit does not allow changing a widget's session-state
    # value after that widget has already been rendered in the same run.
    deferred_stock_count=st.session_state.pop("_apply_reduced_stock_count",None)
    if deferred_stock_count is not None:
        st.session_state["maximum_stocks"]=max(1,int(_safe(deferred_stock_count,1)))

    # First-use basic rules deliberately start unselected/at zero so a portfolio
    # cannot be built accidentally from hidden defaults. Numeric fields and sliders
    # are synchronized in both directions.
    if st.session_state.get("currency") not in ("Select","DKK","EUR","USD"):
        st.session_state["currency"]="Select"

    top1,top2,top3,top4=st.columns([0.75,1.8,1.8,1.55])
    with top1:
        st.selectbox(
            "Currency",
            ["Select","DKK","EUR","USD"],
            index=0,
            key="currency",
            help="Select the currency used for all portfolio amounts and in the final report.",
        )
    selected_currency=st.session_state.get("currency") or "Select"
    currency_label=selected_currency if selected_currency in SUPPORTED_PORTFOLIO_CURRENCIES else "currency"
    with top2:
        _basic_money_field(
            f"Capital available ({currency_label})",
            "portfolio_value_input",
            10_000,
            "The total amount APB may use when constructing the portfolio.",
        )
    with top3:
        _basic_money_field(
            f"Minimum per stock ({currency_label})",
            "minimum_position_input",
            1_000,
            "The smallest amount APB may allocate to one stock position.",
        )
    with top4:
        st.number_input(
            "Number of different stocks (typical 10–50)",
            min_value=0,
            step=1,
            key="maximum_stocks",
            help="APB builds the portfolio using this number of different stocks, provided the selected rules can be satisfied. 10–50 is a typical range, not a limit.",
        )

    st.info("The profiles below are ready-made starting points. Choose a preset, then change any individual value if you want. High priority gives that target group much more influence in the optimisation.")

    # Seed the selected default profiles before Streamlit creates the number inputs.
    # This guarantees meaningful targets even when the user never touches a dropdown.
    _ensure_web_profile_defaults("str","Balanced",STRUCTURE_TARGET_PROFILES,high_priority_key="structure_high_priority")
    _ensure_web_profile_defaults("sec","Balanced",SECTOR_TARGET_PROFILES,high_priority_key="sector_high_priority")
    _ensure_web_profile_defaults("reg","Global balanced",REGION_TARGET_PROFILES,high_priority_key="region_high_priority")
    _ensure_web_profile_defaults(
        "ind","Neutral",INDUSTRY_PREFERENCE_PROFILES,
        high_priority_key="industry_high_priority",
        auto_high_priority=True,
        all_keys=INDUSTRY_WEB_OPTIONS,
    )

    structure_heading=f"Structure layers | {st.session_state.get('structure_profile', _matching_allocation_profile('str',STRUCTURE_TARGET_PROFILES))}"
    with st.expander(structure_heading,expanded=(st.session_state.get("_open_target_section")=="structure")):
        st.caption("This is the portfolio's main risk architecture and therefore one of the most important choices in APB. The four targets should normally total 100%.")
        structure_profile=st.selectbox("Structure profile",_profile_options(STRUCTURE_TARGET_PROFILES),index=0,key="structure_profile",on_change=_allocation_profile_dropdown_changed,args=("str",STRUCTURE_TARGET_PROFILES,"structure"))
        _apply_web_profile("str",structure_profile,STRUCTURE_TARGET_PROFILES)
        st.checkbox("High priority",key="structure_high_priority",help="Give the selected structure-layer targets substantially more influence. Use only when matching the risk architecture is more important than the normal balance of APB signals.")
        structure_keys=_allocation_controls("str",STRUCTURE_TARGET_PROFILES)
        cols=st.columns(4)
        for col,(k,v) in zip(cols,STRUCTURE_TARGET_PROFILES["Balanced"].items()):
            with col:
                _allocation_value_input("str",structure_keys,k)
        _show_structure_pyramid(width=455,caption=False)

    sector_heading=f"Sector targets | {st.session_state.get('sector_profile', _matching_allocation_profile('sec',SECTOR_TARGET_PROFILES))}"
    with st.expander(sector_heading,expanded=(st.session_state.get("_open_target_section")=="sector")):
        st.caption("Sector targets shape economic diversification. Presets are starting points; every percentage remains editable.")
        sector_profile=st.selectbox("Sector profile",_profile_options(SECTOR_TARGET_PROFILES),index=0,key="sector_profile",on_change=_allocation_profile_dropdown_changed,args=("sec",SECTOR_TARGET_PROFILES,"sector"))
        _apply_web_profile("sec",sector_profile,SECTOR_TARGET_PROFILES)
        st.checkbox("High priority",key="sector_high_priority",help="Give sector targets substantially more influence than under normal APB balancing.")
        st.number_input(
            "Minimum stocks in each active sector (normally choose 0 or 1)",
            min_value=0,
            max_value=10,
            value=0,
            step=1,
            key="minimum_sector",
            help=(
                "Optional diversification rule. 0 lets APB decide freely. "
                "If you choose 1, a portfolio of roughly 15 stocks or more is recommended, "
                "otherwise there may be too few positions to cover the active sectors sensibly."
            ),
        )
        sector_keys=_allocation_controls("sec",SECTOR_TARGET_PROFILES)
        cols=st.columns(3)
        for i,(k,v) in enumerate(SECTOR_TARGET_PROFILES["Balanced"].items()):
            with cols[i%3]:
                _allocation_value_input("sec",sector_keys,k)

    region_heading=f"Region targets | {st.session_state.get('region_profile', _matching_allocation_profile('reg',REGION_TARGET_PROFILES))}"
    with st.expander(region_heading,expanded=(st.session_state.get("_open_target_section")=="region")):
        st.caption("Regional targets manage geographic concentration. They normally sum to 100%, but the optimiser may deviate when the stock universe or stronger constraints require it.")
        region_profile=st.selectbox("Region profile",_profile_options(REGION_TARGET_PROFILES),index=0,key="region_profile",on_change=_allocation_profile_dropdown_changed,args=("reg",REGION_TARGET_PROFILES,"region"))
        _apply_web_profile("reg",region_profile,REGION_TARGET_PROFILES)
        st.checkbox("High priority",key="region_high_priority",help="Give regional targets much more influence in the optimisation. Leave unchecked for normal APB balancing.")
        region_keys=_allocation_controls("reg",REGION_TARGET_PROFILES)
        cols=st.columns(3)
        for i,(k,v) in enumerate(REGION_TARGET_PROFILES["Global balanced"].items()):
            with cols[i%3]:
                _allocation_value_input("reg",region_keys,k)

    if "industry_profile" not in st.session_state:
        st.session_state["industry_profile"]=_matching_industry_profile(INDUSTRY_PREFERENCE_PROFILES)
    industry_heading=f"Industry preferences | {st.session_state.get('industry_profile', _matching_industry_profile(INDUSTRY_PREFERENCE_PROFILES))}"
    with st.expander(industry_heading,expanded=(st.session_state.get("_open_target_section")=="industry")):
        st.caption("Industries are softer preferences rather than a 100% allocation. Zero is neutral; positive values favour an industry and negative values reduce its preference. A non-neutral preset automatically switches High priority on, but you can change it afterwards.")
        industry_profile_options=list(INDUSTRY_PREFERENCE_PROFILES.keys())
        if "Custom setup" not in industry_profile_options:
            industry_profile_options.append("Custom setup")
        industry_profile=st.selectbox(
            "Industry preset",
            industry_profile_options,
            key="industry_profile",
            on_change=_industry_profile_dropdown_changed,
            args=(INDUSTRY_PREFERENCE_PROFILES,),
        )
        st.checkbox("High priority",key="industry_high_priority",help="When selected, industry preferences receive substantially more influence in stock selection. You can switch this off even after choosing a non-neutral preset.")
        cols=st.columns(3)
        for i,k in enumerate(INDUSTRY_WEB_OPTIONS):
            with cols[i%3]:
                _industry_preference_input(k,INDUSTRY_PREFERENCE_PROFILES)

    if "dividend_enabled" not in st.session_state:
        st.session_state["dividend_enabled"]=False
    if "dividend_high_priority" not in st.session_state:
        st.session_state["dividend_high_priority"]=True
    if "dividend_target_pct" not in st.session_state:
        st.session_state["dividend_target_pct"]=3.0
    if "dividend_target_slider" not in st.session_state:
        st.session_state["dividend_target_slider"]=float(st.session_state.get("dividend_target_pct",3.0))
    dividend_heading=f"Dividend | {'On' if st.session_state.get('dividend_enabled',False) else 'Off'}"
    dividend_force_open=bool(st.session_state.pop("_open_dividend_once",False))
    with st.expander(dividend_heading,expanded=dividend_force_open):
        st.caption("Dividend is optional. When enabled, APB favours portfolios whose weighted dividend yield reaches the selected target while still balancing the other portfolio rules.")
        st.checkbox("Include dividend preference",key="dividend_enabled",on_change=_keep_dividend_open_once)
        dividend_on=bool(st.session_state.get("dividend_enabled",False))
        st.checkbox(
            "High priority",key="dividend_high_priority",disabled=not dividend_on,
            help="Default is High priority. Switch this off if dividend should influence the build more gently.",
            on_change=_keep_dividend_open_once,
        )
        st.number_input(
            "Target dividend yield (%)",min_value=0.0,max_value=15.0,step=0.1,
            key="dividend_target_pct",disabled=not dividend_on,
            help="Portfolio-level target based on weighted dividend yield. Default is 3.0% when dividend preference is enabled.",
            on_change=_sync_dividend_number_to_slider,
        )
        st.slider(
            "Dividend target slider",min_value=0.0,max_value=15.0,step=0.1,
            key="dividend_target_slider",disabled=not dividend_on,label_visibility="collapsed",
            on_change=_sync_dividend_slider_to_number,
        )

    st.caption("Tip: targets are guidance to the optimiser, not guarantees. Tight constraints can conflict with each other, especially in smaller portfolios or a limited stock universe.")

    quota_blocked=False
    quota_used=0
    quota_limit=0
    quota_month=_customer_month_key()
    if st.session_state.get("auth_tier") in ("Standard","Premium","VIP"):
        try:
            live_users=_load_users(require_remote=True).get("users",{})
            live_entry=live_users.get(st.session_state.get("auth_user",""),{})
            quota_used,quota_limit,quota_month=_effective_build_usage(live_entry)
            quota_blocked=quota_used>=quota_limit
            next_month=(datetime.now().astimezone().replace(day=1)+timedelta(days=32)).replace(day=1)
            if quota_blocked:
                st.warning(f"Portfolio builds this month: {quota_used} / {quota_limit} — Monthly limit reached. Resets {next_month.strftime('%B 1')}.")
            else:
                st.info(f"Portfolio builds this month: {quota_used} / {quota_limit}")
        except Exception:
            quota_blocked=True
            st.warning("Build availability could not be verified at the moment. Please try again shortly.")

    # If the selected number of stocks and minimum position consume all (or more)
    # available capital, APB can reduce the stock count by 20% and continue.
    pending_reduction=st.session_state.get("_stock_count_reduction_prompt")
    if isinstance(pending_reduction,dict):
        old_count=max(1,int(_safe(pending_reduction.get("stock_count"),1)))
        new_count=max(1,int(_safe(pending_reduction.get("reduced_stock_count"),max(1,int(old_count*0.8)))))
        req=_safe(pending_reduction.get("required_capital"),0.0)
        cap=_safe(pending_reduction.get("capital"),0.0)
        cur=str(pending_reduction.get("currency") or st.session_state.get("currency",""))
        st.warning(
            "The selected settings leave too little room for portfolio optimisation.\n\n"
            f"{old_count} stocks × minimum per stock requires {_money(req)} {cur} "
            f"of the available {_money(cap)} {cur}.\n\n"
            f"Build portfolio anyway? The number of stocks will automatically be reduced by 20% "
            f"from {old_count} to {new_count} to give the optimiser more flexibility."
        )
        cancel_col,build_anyway_col=st.columns([1,2])
        with cancel_col:
            if st.button("CANCEL",use_container_width=True,key="cancel_stock_count_reduction"):
                st.session_state.pop("_stock_count_reduction_prompt",None)
                st.rerun()
        with build_anyway_col:
            if st.button("BUILD PORTFOLIO ANYWAY",type="primary",use_container_width=True,key="confirm_stock_count_reduction"):
                st.session_state["_apply_reduced_stock_count"]=new_count
                st.session_state["_build_after_stock_reduction"]=True
                st.session_state.pop("_stock_count_reduction_prompt",None)
                st.rerun()

    build_button_clicked=st.button("BUILD PORTFOLIO",type="primary",use_container_width=True,disabled=quota_blocked)
    continue_after_reduction=bool(st.session_state.pop("_build_after_stock_reduction",False))
    build_requested=bool(build_button_clicked or continue_after_reduction)

    if build_requested:
        basic_errors=[]
        currency=st.session_state.get("currency","Select")
        capital=_parse_eu_number(st.session_state.get("portfolio_value_input",0),0.0)
        minimum_position=_parse_eu_number(st.session_state.get("minimum_position_input",0),0.0)
        stock_count=int(_safe(st.session_state.get("maximum_stocks",0),0))
        if currency not in SUPPORTED_PORTFOLIO_CURRENCIES:
            basic_errors.append("Select a portfolio currency.")
        if capital<=0:
            basic_errors.append("Capital available must be greater than 0.")
        if minimum_position<=0:
            basic_errors.append("Minimum per stock must be greater than 0.")
        if stock_count<=0:
            basic_errors.append("Number of different stocks must be greater than 0.")
        if capital>0 and minimum_position>capital:
            basic_errors.append("Minimum per stock cannot be greater than the total capital available.")
        if basic_errors:
            st.error("Portfolio cannot be built yet:\n\n"+"\n".join(f"• {x}" for x in basic_errors))
            st.stop()

        # Equality is intentionally included: if every requested position receives
        # exactly the minimum, the optimiser has no capital left to distribute.
        if capital>0 and minimum_position>0 and stock_count>0 and minimum_position*stock_count>=capital:
            reduced_stock_count=max(1,int(stock_count*0.8))
            if reduced_stock_count>=stock_count and stock_count>1:
                reduced_stock_count=stock_count-1
            st.session_state["_stock_count_reduction_prompt"]={
                "stock_count":stock_count,
                "reduced_stock_count":reduced_stock_count,
                "required_capital":minimum_position*stock_count,
                "capital":capital,
                "currency":currency,
            }
            st.rerun()

        invalid_allocations=_invalid_required_allocations()
        if invalid_allocations:
            lines=[]
            for label,total in invalid_allocations:
                diff=round(100.0-total,1)
                if diff>0:
                    action=f"{diff:.1f}% remains to be distributed"
                else:
                    action=f"{abs(diff):.1f}% must be removed"
                lines.append(f"• {label}: {total:.1f}% — {action}")
            st.error(
                "Portfolio cannot be built yet. The following distributions must total 100.0%:\n\n"
                + "\n".join(lines)
            )
            st.stop()

        order=make_order_from_ui("advanced")
        status=st.empty(); detail=st.empty(); bar=st.progress(2)
        state={"p":2,"last":time.monotonic()}
        status.info("Preparing the portfolio build…")
        detail.caption("Reading your settings and preparing the optimisation engine.")
        time.sleep(0.35)

        def progress(msg):
            lower=str(msg).lower()
            if "reading" in lower: base=7
            elif "start portfolio" in lower or "creating" in lower: base=14
            elif "aktieoptimering" in lower or "stock selection" in lower or "optimising stock" in lower: base=24
            elif "kapitaloptimering" in lower or "capital allocation" in lower or "optimising capital" in lower: base=58
            elif "whole shares" in lower or "converting" in lower: base=82
            else: base=state["p"]
            state["p"]=max(state["p"],min(86,base+1))
            status.info("Building your portfolio…")
            detail.caption(_user_facing_progress(msg))
            bar.progress(int(state["p"]))

        try:
            result=run_engine(order,progress)

            # Deliberate user-experience buffer: the real optimiser usually needs only a few seconds.
            # These staged checks provide stable feedback and preserve room for future engine growth.
            finishing_steps=[
                (88,"Checking target balance across structure layers…"),
                (91,"Reviewing sector and regional concentration…"),
                (94,"Testing whole-share allocation and position limits…"),
                (97,"Preparing portfolio tables and report data…"),
                (99,"Final quality check…"),
            ]
            status.info("Finalising your portfolio…")
            for pct_value,message in finishing_steps:
                detail.caption(message)
                bar.progress(pct_value)
                time.sleep(1.0)

            if st.session_state.get("auth_tier") in ("Standard","Premium","VIP"):
                try:
                    quota_result=_remote_customer_record_build(st.session_state.get("auth_user",""))
                    _refresh_users_cache_from_payload(quota_result)
                except Exception as quota_exc:
                    payload=getattr(quota_exc,"payload",{}) or {}
                    if "limit" in payload:
                        raise RuntimeError(f"Monthly build limit reached ({payload.get('used',0)} / {payload.get('limit',0)}).")
                    raise RuntimeError("The portfolio was calculated, but the build could not be registered securely. Please try again.") from quota_exc
                _save_premium_user_data(st.session_state.get("auth_user",""),order,result)

            bar.progress(100); status.success("Portfolio ready"); detail.caption("Build complete — opening your portfolio.")
            time.sleep(0.25)
            st.session_state.result_data=result
            st.rerun()
        except Exception as exc:
            bar.empty(); status.empty(); detail.empty(); st.error(_user_facing_error(exc))
        finally:
            globals()["_builder_web_progress_hook"]=None
    _render_disclaimer()


# ----------------------------- APP SHELL ------------------------------------
for key,default in (("result_data",None),("auth_user",None),("auth_tier",None),("admin_page","Users"),("login_nonce",0)):
    if key not in st.session_state: st.session_state[key]=default

if not st.session_state.auth_user:
    login_screen(); st.stop()

head1,head2=st.columns([7.8,2.2])
with head1:
    st.title("Alpha Portfolio Builder")
    st.caption("Fast, guided portfolio construction powered by the APB engine")
with head2:
    if LOGO_IMAGE_B64:
        st.markdown('<div class="apb-head-logo">',unsafe_allow_html=True)
        st.markdown(_img(LOGO_IMAGE_B64,68),unsafe_allow_html=True)
        st.markdown('</div>',unsafe_allow_html=True)
    st.markdown(
        f'<div class="apb-account-card">'
        f'<div class="apb-account-name">{_current_display_username()}</div>'
        f'<span class="apb-account-tier">{st.session_state.auth_tier}</span>'
        f'</div>',
        unsafe_allow_html=True,
    )
    if st.button("Log out",use_container_width=True):
        # Remove the current login widgets and create fresh widget identities for the
        # login screen. This gives the browser password manager a new autofill target.
        login_nonce=int(st.session_state.get("login_nonce",0) or 0)
        st.session_state.pop(f"login_username_{login_nonce}",None)
        st.session_state.pop(f"login_password_{login_nonce}",None)
        st.session_state["login_nonce"]=login_nonce+1
        for k in ("auth_user","auth_tier","result_data"): st.session_state[k]=None
        st.session_state.pop("_open_target_section",None)
        st.rerun()

if not st.session_state.get("_engine_restore_checked",False):
    # Local files are the fast working copy. SIMGROVA is contacted only if one is missing,
    # e.g. after a Streamlit redeploy/restart.
    _restore_missing_engine_files_from_simgrova()
    st.session_state["_engine_restore_checked"]=True

if st.session_state.auth_tier=="Admin":
    view=st.radio("",["Administration","Portfolio builder"],horizontal=True,label_visibility="collapsed")
    if view=="Administration": admin_panel()
    else: render_builder()
else:
    render_builder()