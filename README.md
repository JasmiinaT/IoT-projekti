Tämä repositorio on IoT-perusteet ryhmätyötä varten. Ryhmätyön tavoite on suunnitella ja valmistaa lämpömittari Raspberry Picoa hyväksi käyttäen.

Ryhmän jäsenet:
Jasmiina Tauriainen,
Joonatan Konttila,
Jari Nordsten,
Joel Puolakanaho


***** Lämpömittari *****

Lämpömittaria alettiin tekemään Raspberry Picon ja NTC thermistorin avulla. Referenssinä toimi DS18B20 digitaalinen lämpömittari, joka liitettiin järjestelmään.


***** Backend *****

Repositoriosta löydän kolme koodia backendiä varten:

  Backend.py

  Yleismalli backendistä. Tämä muodostaa Picoon wifi- yhteyden, antaa ohjelmarungon sensori- dataa varten ja lähettää datan Thingspeakiin.

  Sensori.py

  Erillinen tiedosto lämpötilasensoreiden koodista. Tästä löytyy mm. omat aliohjelmat analogiselle ja digitaliselle lämpötilasensorille. 

  BackendWithSensors.py
  
  Varsinainen backend- koodi jossa yhdistyvät Backend.py sekä Sensori.py.

***** Frontend *****

Frontendia varten löytyy kolme tiedostoa:

  Index.html

  Verkkosivun pohja.

  gchart.js

  Määrittelee verkkosivun toiminnallisuudet: sivustolla molemmille antureille lämpötilamittarit esittämään sen hetkistä lämpötilaa. Lisäksi graafi esittämään lämpötiloja edellisen tunnin ajalta. Sivu päivittyy     automaattisesti minuutin välein.

  styles.css

  Verkkosivun muotoilu.
