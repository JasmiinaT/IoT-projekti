#### Tämä repositorio on IoT;n ja sulautettujen järjestelmien-perusteet kurssin ryhmätyötä varten. Ryhmätyön tavoite on suunnitella ja valmistaa lämpömittari Raspberry Picoa hyväksi käyttäen.

Ryhmän jäsenet:
- Jasmiina Tauriainen
-  Joonatan Konttila
-  Jari Nordsten
-  Joel Puolakanaho

#

### Lämpömittari

_Lämpömittaria alettiin tekemään Raspberry Picon ja NTC thermistorin avulla. Referenssinä toimi DS18B20 digitaalinen lämpömittari, joka liitettiin järjestelmään._



***** Backend *****

_Repositoriosta löydän kolme koodia backendiä varten:_

  - Backend.py

       _Yleismalli backendistä. Tämä muodostaa Picoon wifi- yhteyden, antaa ohjelmarungon sensori- dataa varten ja lähettää datan Thingspeakiin._

  - Sensori.py

       _Erillinen tiedosto lämpötilasensoreiden koodista. Tästä löytyy mm. omat aliohjelmat analogiselle ja digitaliselle lämpötilasensorille._

  - BackendWithSensors.py
  
       _Varsinainen backend- koodi jossa yhdistyvät Backend.py sekä Sensori.py._

***** Frontend *****

_Frontendia varten löytyy kolme tiedostoa:_

  - Index.html

       _Verkkosivun pohja._

  - gchart.js

       _Määrittelee verkkosivun toiminnallisuudet: sivustolla molemmille antureille lämpötilamittarit esittämään sen hetkistä lämpötilaa. Lisäksi graafi esittämään lämpötiloja edellisen tunnin ajalta. Sivu päivittyy     automaattisesti minuutin välein._

  - styles.css

       _Verkkosivun muotoilu._
