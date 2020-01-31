# Tietokantasovellusharjoitus

<https://tsoha-laskutus.herokuapp.com/>

Yksinkertainen laskutussovellus kappaletavarakauppaan. Sovelluksessa on tuoterekisteri, asiakasrekisteri ja tietysti laskurekisteri. Lasku on aina yhdelle asiakkalle, mutta siinä voi olla monta riviä. Rivit ovat omassa taulussaan. Laskulla ei voi olla rivejä tuoterekisterin ulkopuolelta.

Ilman kirjautumista voi katsoa vain tuotehinnastoa. Käyttäjätunnukset *erkki* ja *paavo* toimivat ja niiden salasana on *sala*

Tuoterekisterissä on tuoteryhmä-kenttä yhteenvetoraportointia varten. Esimerkiksi asiakaskohtainen raportointi tuoteryhmittäin edellyttää useamman taulun yhteiskäyttöä ja summaamista.

Jokaisella käyttäjällä tulee olemaan omat asiakkaansa eivätkä käyttäjät näe toistensa asiakkaita. Sama koskee laskuja.

Käyttäjät voivat katsoa, lisätä, poistaa ja muokata tuotteita, omia laskujaan ja omia asiakkaitaan. Katso lisää: <https://github.com/riihikallio/tsoha/blob/master/documentation/user_stories.md>

![Kaavio](https://github.com/riihikallio/tsoha/blob/master/documentation/kaavio.png)
