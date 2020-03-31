# DDS

Voor het vak **Internet of things** pleeg ik een onderzoek rond het concept DDS. Hieronder kan u mijn bevindingen terugvinden.

## Wat is DDS?

DDS staat voor **Data Distribution Sevice**. Het is een middleware-protocol en API-standaard voor gegevensgerichte machine-to-machine connectiviteit dat is uitgevonden door de [Object Management Group].

Data Distribution Sevice integreert de componenten van een systeem samen en biedt dataconnectiviteit met lage latency, extreme betrouwbaarheid en een schaalbare architectuur dat een die zakelijke en bedrijfskritieke Internet of Things-toepassingen nodig hebben.

DDS is uniek op gegevens gericht, wat ideaal is voor het industriële internet der dingen. De meeste middleware werkt door informatie tussen applicaties en systemen te verzenden. Datacentriciteit zorgt ervoor dat alle berichten de contextuele informatie bevatten die een applicatie nodig heeft om de ontvangen data te begrijpen.

De essentie van datacentriciteit is dat DDS weet welke gegevens het opslaat en bepaalt hoe die gegevens worden gedeeld. Programmeurs die traditionele berichtgerichte middleware gebruiken, moeten code schrijven die berichten verzendt. Programmeurs die op gegevens gerichte middleware schrijven, schrijven code die aangeeft hoe en wanneer gegevens moeten worden gedeeld en vervolgens rechtstreeks gegevenswaarden kunnen delen. In plaats van al deze complexiteit in de applicatie code te beheren, implementeert DDS direct de gecontroleerde, beheerde en veilige gegevensuitwisseling.

DDS ziet conceptueel een lokale opslag van gegevens die de 'wereldwijde gegevensruimte' wordt genoemd. Voor de applicatie ziet de globale gegevensruimte eruit als lokaal geheugen dat toegankelijk is via een API. De programmeur schrijft naar wat voor hem lijkt op zijn lokale opslag. In werkelijkheid verzendt DDS berichten om de juiste winkels op externe knooppunten bij te werken. het programma leest uit wat lijkt op een lokale winkel.

Alles bij elkaar geven de lokale winkels applicaties de illusie dat ze toegang hebben tot de volledige wereldwijde gegevensruimte. Dit is slechts een illusie. Er is geen wereldwijde plaats waar alle gegevens leven. Elke applicatie slaat lokaal alleen op wat het nodig heeft en alleen zolang het nodig is. DDS houdt zich bezig met data in beweging. De wereldwijde dataruimte is een virtueel concept dat eigenlijk slechts een verzameling lokale winkels is. Elke applicatie, in bijna elke taal die op elk systeem draait, ziet het lokale geheugen in zijn optimale native formaat. De wereldwijde gegevensruimte deelt gegevens tussen embedded, mobiele en cloudapplicaties over elk transport, ongeacht taal of systeem, en met extreem lage latentie.

### Wat is middleware?

Middleware word ook wel Machine To Machine of connectivity framework genoemd. het is een softwarelaag tussen het besturingssysteem en de applicaties. Met als doel om het makkelijker te maken om tussen verschillende componenten van een systeem te cummuniceren en gegevens te delen. Dit zowel via kabel of draadloos. Het vereenvoudigt de ontwikkeling van gedistribueerde systemen. Hierdoor kunnen softwareontwikkelaars zich concentreren op het specifieke doel van hun applicaties in plaats van bezig te zijn met de mechanica van het doorgeven van informatie en data tussen applicaties en systemen.

## Waarom DDS?

Waarom zou een developper de Data Distribution Service nu gebruiken?

De OMG DDS-standaard is geoptimaliseerd voor hoogwaardige, zeer schaalbare Industrial Internet of Things (IoT) en grootschalige Consumer IoT-toepassingsomgevingen die realtime datacommunicatie-uitwisseling vereisen.

Het helpt gebruikers om in realtime grote hoeveelheden informatie die door het apparaat gegenereed zijn te verwerken op een betrouwbare en veilig manier. Dit zorgt ervoor dat het mogelijk is om op een kost efficiente manier slimmere beslissingen, nieuwe services, extra inkomstenstromen mogelijk maakt. Het vereenvoudigd de ontwikkeling, implementatie en het beheer van IoT-toepassingen.

### DDS zorgt voor:

- **Eenvoudige integratie:** de op gegevens gerichte benadering die door DDS wordt gebruikt, maakt de definitie mogelijk van gemeenschappelijke en uitbreidbare gegevensmodellen voor naadloze interoperabiliteit van informatietechnologie / operationele technologie. De losse en anonieme abstractie van het delen van gegevens verbergt de connectiviteit en topologiedetails van applicaties volledig.

- **Prestatie-efficiëntie en schaalbaarheid:** de punt-tot-punt latenties die te bereiken zijn met DDS-implementaties kunnen zo laag zijn als 30 µsec. Hierdoor is het mogelijk om miljoenen berichten per seconde door te sturen. Het maakt gebruik van een zeer efficiënt draadprotocol, inhouds- en tijdgebaseerde filtering. Het is zelfs mogelijk om bijna lineaire schaalbaarheid te bereiken mits de applicatie hier goed genoeg voor is ontworpen.

- **Geavanceerde beveiliging:** De OMG DDS-beveiligingsspecificatie gebruikt een uitgebreid beveiligingsmodel- en Service Plugin Interface -architectuur voor compatibele DDS-implementaties. Het is mogelijk om end-to-end beveiligde data connectiviteit in een IoT-systeem te gebruiken door de gestandaardiseerde authenticatie, toegangscontrole en encryptie die DDS biedt.

- **Open standaard:** de OMG DDS middleware-specificatie is een bewezen standaard die openstaat voor deelname door zowel leveranciers als gebruikers. Het maakt end-to-end interoperabiliteit van leveranciers mogelijk en vereenvoudigt de ontwikkeling en integratie van IoT-systemen door middel van volledig open, toekomstbestendige API's zonder vendor lock -n.

- **QoS-enabled:** Door gebruik te maken van een uitgebreid QoS-beleid kan DDS alle aspecten van de gegevensdistributie besturen, zoals verkeersprioritering, betrouwbaarheid, stiptheid, en gebruik van andere bronnen.

- **Schaalbare detectie:** Voor grootschalige dynamische systemen biedt DDS automatische detectie die plug-and-play-functionaliteit biedt om systeemintegratie en utalisatie te vereenvoudigen.

- **Toepasbaarheid:** DDS kan peer-to-peer-, apparaat-naar-apparaat-, apparaat-naar-cloud- en cloud-naar-cloud-communicatie transparant behandelen. Implementaties zijn beschikbaar voor embedded, mobiele, web-, enterprise- en cloud-applicaties.

## Hoe DDS integreren?

In de eerste plaats is het belangtrijk voor systeemarchitecten of ontwikkelaars om te bepalen welke gegevens moeten worden verzonden tussen applicaties binnen het gedistribueerde systeem. Dit wordt het conceptuele datamodel dat aan datastromen wordt toegewezen.

In de eerste fase is het belangrijk om te focussen op de gegevens die moeten worden verzonden in plaats van op het mechanisme voor verzending. Als het systeem bijvoorbeeld een vloot van legervrachtwagens controleert, is het belangrijk om te overwegen welke gegevens belangrijk zijn om te bewaken over dit wagenpark? Mogelijk moet het systeem bijvoorbeeld de posities, manifesten, oliepeilen en onderhoudsinformatie van de vrachtwagens bewaken. Het definiëren van de gegevens die moeten worden verzonden, moet worden gedaan voordat de gegevens worden toegewezen aan berichten of middlewaretechnologieën.

De volgende stap is om van dit conceptuele datamodel naar een model toe te wijzen dat rekening houdt met de netwerkproblemen van wanneer, waar en hoe de data moeten worden verzonden. Om dit te doen, moet de systeemarchitect netwerkgegevensstromen ontwerpen op basis van de structuur van die gegevens en hun leveringskenmerken.

### DDS best practices

Bij het toewijzen van een conceptueel gegevensmodel naar een netwerkgegevensmodel moeten de volgende beste practices gebruikt worden:

#### - Maak een netwerkgegevensmodel op basis van gerelateerde gegevens en bezorgingskenmerken

Om toekomstige schaalbaarheid en prestaties te garanderen moet een programmeur gegevensitems groeperen die logisch gerelateerd zijn en vergelijkbare leveringskenmerken hebben in een netwerkdatamodel.

Wanneer programmeurs alles in 1 gegevensstroom hebben gestopt en niet hebben nagedacht over het gegevensmodel dan kunnen er zich problemen voordoen.
Dit zou kunnen betekenen dat alle gegevens tegelijkertijd zouden worden verzonden. Dit kan werken met een beperkte hoeveelheid gegevens, maar zelfs op kleine schaal gebruikt het onnodige bandbreedte en CPU-capaciteit. uiteindelijk zal dit het verwerken van gegevens zo goed als onmogelijk maken. Door een gegevensmodel vooraf aan te maken kan de programmeur schaalbaarheidsproblemen en prestatieproblemen langs de lijn voorkomen.

#### - Gebruik getypte data

Het kan zeer nuttig zijn om gegevens een daadwerkelijke structuur of type geven in plaats van binaire gegevens over het netwerk te verzenden. Een reden hiervoor is dat de middleware de detectie en distributie van type-informatie gaat verwerken.

wanneer gegevens getypt zijn kan men automatisch andere applicaties en diensten aansluiten, zoals datavisualisatie-tools of gedistribueerde logging-tools. Hierdoor kunnen ontwikkelaars en systeemintegrators op maat gemaakte tools aansluiten om gegevens te visualiseren, gegevens op te nemen, realtime gegevens te vertalen naar een relationele database of om aanvullende functies uit te voeren op de gegevens die niet van tevoren bekend zijn.

door het gebruik van getypte gegevens kunnen er meer mogelijkheden voorkomen dan oorsprongkelijk bedoeld was. Er kunnen nieuwe applicaties worden ontwikkeld die gegevens choreograferen, aggregeren, splitsen of bemiddelen zonder dat u zich zorgen hoeft te maken over details op protocolniveau. Het helpt om systemen op een efficientere manier to onderhouden en upgraden aangezien de gegevens op een goed georganiseerde manieren kunnen worden gewijzigd.

Wanner dit niet wordt gedaan zal de applicatieontwikkelaar de logica moeten schrijven om de gegevens van en naar een netwerkformulier te converteren, de vereiste programmeertalen te ondersteunen en om met het eindbestaan ​​om te gaan. Dit voegt extra logica en complicaties toe die moet worden geschreven, getest en onderhouden.  Dit kan ervoor zorgen dat de uiteindelijke kosten van het ontwikkelen en upgraden van het systeem verhogen.

#### - Gebruik keyed data

Als meerdere real-world objecten in een systeem worden weergegeven moet de systeemarchitect sleutelvelden gebruiken om de middleware te informeren wat die objecten zijn. Sleutelvelden zijn velden in een gegevenstype die een unieke identificatie vormen van een real-world object. Als gegevens zijn gecodeerd zal de middleware herkennen dat elke unieke waarde van sleutelvelden een uniek real-world object vertegenwoordigt. Als meerdere real-world objecten in een systeem worden weergegeven moet de systeemarchitect sleutelvelden gebruiken om de middleware te informeren wat die objecten zijn. Sleutelvelden zijn velden in uw gegevenstype die een unieke identificatie vormen van een real-world object. Als gegevens zijn gecodeerd zal de middleware herkennen dat elke unieke waarde van sleutelvelden een uniek real-world object vertegenwoordigt.

De middelware kan op deze manier bijvoorbeeld informatie over de levenscyclus van objecten bijhouden. Het kan ook levenscyclusinformatie bijhouden over de vraag of deze instantie al dan niet in leven is.

als de programmeur geen sleutelwaarden aanmaakt zal de middleware niet begrijpen dat er meerdere objecten worden weergegeven. Dit kan leiden tot het probleem dat de applicatieontwikkelaar logica schrijft die dupliceert wat er al in de middleware zit om levenscycli van objecten te detecteren, vertraagde updates van objecten te detecteren en om failover tussen updates over een object te bieden. Als de middleware niet weet dat de applicatie meerdere objecten vertegenwoordigt kan deze bovendien geen afzonderlijke logische wachtrij per object aanhouden. Dit zorgt ervoor dat de applicatie langere wachtrijen heeft om ervoor te zorgen dat updates niet verloren gaan voor een bepaald object.

## Waar gebruiken ze DDS?

DDDS word vooral door grote bedrijven gebruikt omdat het ook specifiek voor die markt ontworpen is. Momenteel gebruiken bedrijven zoals NASA en AUDI het om hun machines of simulaties te voorzien van gegevens

## Bronnen

[DDS foundation](https://www.dds-foundation.org/what-is-dds-3/)
[DDS Foundation - Why](https://www.dds-foundation.org/why-choose-dds/)
[Wikipedia - DDS](https://en.wikipedia.org/wiki/Data_Distribution_Service)
[Wikipedia - Machine-To-Machine](https://en.wikipedia.org/wiki/Machine_to_machine)
[Military embedded - best practices](http://mil-embedded.com/articles/data-centric-real-world-distributed-systems/)

[Object Management Group]: <https://www.omg.org/index.htm>
