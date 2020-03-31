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

- **Eenvoudige integratie:** de op gegevens gerichte benadering die door DDS wordt gebruikt, maakt de definitie mogelijk van gemeenschappelijke en uitbreidbare gegevensmodellen voor naadloze interoperabiliteit van informatietechnologie (IT) / operationele technologie (OT). De losse en anonieme abstractie van het delen van gegevens verbergt de connectiviteit en topologiedetails van applicaties volledig.

- **Prestatie-efficiëntie en schaalbaarheid:** DDS-implementaties kunnen punt-tot-punt latenties bereiken die zo laag zijn als 30 µsec. en doorvoer van enkele miljoenen berichten per seconde. Het maakt gebruik van een zeer efficiënt draadprotocol, inhouds- en tijdgebaseerde filtering. Als ze op de juiste manier zijn ontworpen, kunnen op DDS gebaseerde systemen een bijna lineaire schaalbaarheid bereiken.

- **Geavanceerde beveiliging:** de OMG DDS-beveiligingsspecificatie definieert een uitgebreide beveiligingsmodel- en Service Plugin Interface (SPI) -architectuur voor compatibele DDS-implementaties. DDS biedt gestandaardiseerde authenticatie, encryptie, toegangscontrole en logging mogelijkheden om end-to-end beveiligde data connectiviteit in een IoT-systeem mogelijk te maken.

- **Open standaard:** de OMG DDS middleware-specificatie is een volwassen, bewezen standaard die openstaat voor deelname door zowel leveranciers als gebruikers. Het maakt end-to-end interoperabiliteit van leveranciers mogelijk en vereenvoudigt de ontwikkeling en integratie van IoT-systemen door middel van volledig open, toekomstbestendige API's zonder vendor lock -n.

- **QoS-enabled:** Met een uitgebreide set QoS-beleid kan DDS alle aspecten van de gegevensdistributie besturen, zoals tijdigheid, verkeersprioritering, betrouwbaarheid en gebruik van bronnen.

- **Schaalbare detectie:** voor grootschalige dynamische systemen biedt DDS automatische detectie die plug-and-play-functionaliteit biedt om systeemintegratie en orkestratie te vereenvoudigen.

- **Toepasbaarheid:** DDS kan peer-to-peer-, apparaat-naar-apparaat-, apparaat-naar-cloud- en cloud-naar-cloud-communicatie transparant behandelen. Implementaties zijn beschikbaar voor embedded, mobiele, web-, enterprise- en cloud-applicaties.

## Hoe DDS integreren?

In de eerste plaats is het belangtrijk voor systeemarchitecten of ontwikkelaars om te bepalen welke gegevens moeten worden verzonden tussen applicaties binnen het gedistribueerde systeem. Dit wordt het conceptuele datamodel dat aan datastromen wordt toegewezen.

In de eerste fase is het belangrijk om te focussen op de gegevens die moeten worden verzonden in plaats van op het mechanisme voor verzending. Als het systeem bijvoorbeeld een vloot van legervrachtwagens controleert, is het belangrijk om te overwegen welke gegevens belangrijk zijn om te bewaken over dit wagenpark? Mogelijk moet het systeem bijvoorbeeld de posities, manifesten, oliepeilen en onderhoudsinformatie van de vrachtwagens bewaken. Het definiëren van de gegevens die moeten worden verzonden, moet worden gedaan voordat de gegevens worden toegewezen aan berichten of middlewaretechnologieën.

De volgende stap is om van dit conceptuele datamodel naar een model toe te wijzen dat rekening houdt met de netwerkproblemen van wanneer, waar en hoe de data moeten worden verzonden. Om dit te doen, moet de systeemarchitect netwerkgegevensstromen ontwerpen op basis van de structuur van die gegevens en hun leveringskenmerken.

### DDS best practices

Bij het toewijzen van een conceptueel gegevensmodel naar een netwerkgegevensmodel moeten de volgende beste praktijken in overweging worden genomen:

#### - Maak een netwerkgegevensmodel op basis van gerelateerde gegevens en bezorgingskenmerken

#### - gebruik getypte data

#### - Gebruik keyed data

## Waar gebruiken ze DDS?

DDDS word vooral door grote bedrijven gebruikt omdat het ook specifiek voor die markt ontworpen is. Momenteel gebruiken bedrijven zoals NASA en AUDI het om hun machines of simulaties te voorzien van gegevens

## Bronnen

[DDS foundation](https://www.dds-foundation.org/what-is-dds-3/)
[DDS Foundation - Why](https://www.dds-foundation.org/why-choose-dds/)
[Wikipedia - DDS](https://en.wikipedia.org/wiki/Data_Distribution_Service)
[Wikipedia - Machine-To-Machine](https://en.wikipedia.org/wiki/Machine_to_machine)
[Military embedded - best practices](http://mil-embedded.com/articles/data-centric-real-world-distributed-systems/)

[Object Management Group]: <https://www.omg.org/index.htm>
