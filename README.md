# harvesting_asteroids_python_pygame

Perehdyttyäni Helsingin yliopiston avoimen yliopiston tarjoaman "Ohjelmoinnin
perusteet- ja jatkokurssi Python:illa"-opintojakson materiaaliin, päätin tehdä
uuden Python-version aiemmasta 'asteroids_JavaFX'-sovelluksestani. Uudessa
versiossa kehitin vielä edelleen muutamia vanhan version ominaisuuksia, ja
'pygame'-kirjastoa oli varsin luontevaa käyttää, sen lievästä epävakaudesta
huolimatta, ainakin tämän tyyppiseen peliin, eikä vähiten siksi, että 'pygame'
antaa ohjelmoijan käyttöön 'sprite'-moduulin tarjoaman 'Sprite'-luokan. Suurin
käytännön ero vanhan ja uuden version välillä on ehkä se, että vanhassa Java-
versiossa asteroidit generoidaan ajonaikaisesti, kun taas tässä uudemmassa Python-
versiossa asteroidit generoidaan ja tallennetaan valmiiksi käytettävissä olevaksi
resurssiksi ennen jokaisen uuden pelivuoron alkua. Tämä ratkaisu johtuu siitä,
että Python on suoritukseltaan hitaampi kuin Java.

---

After going through the materials of the course "Fundamentals and Advanced Course
in Programming with Python" offered by the Open University of Helsinki, I decided
to create a new version of my previous 'asteroids_JavaFX' application using Python.
In this new version, I further developed some of the features from the old version,
and I found it quite suitable to use the 'pygame' library, especially for this type
of game. One notable advantage of 'pygame', despite the slight instability, is its
'sprite' module, which provides the 'Sprite' class to manage graphical objects.
Perhaps the greatest practical difference between the old and the new version lies
in the fact that in the old Java version, asteroids were generated dynamically
at runtime, whereas in this newer Python version, the asteroids are generated
and stored as a resource before the start of each new game round. This solution
is due to the fact that Python's execution speed is slower compared to Java.
