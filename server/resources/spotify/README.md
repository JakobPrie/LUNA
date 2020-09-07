# Spotify Steuerung durch LUNA

## Einrichtung:

1. Registriere dich als Spotify-Entwickler und erstelle im [Dashboard](https://developer.spotify.com/dashboard/applications) eine neue App.
2. Trage in der App die Redirect-URL _https://oskar.pw/_ ein.
3. Trage im _spotify_-Modul UND in der Datei `get-spotify-auth.py` in diesem Ordner an den entsprechenden Stellen deinen **Benutzernamen**, deine **Client-ID** (der in 1. erstellten App) und dein **Client-Secret** ein.
4. Du musst einmalig manuell auf einem Gerät mit grafischer Oberfläche und Webbrowser den Zugriff der in 1. erstellten App auf deinen Spotify-Account genehmigen. Anschließend wird der Token automatisch erneuert.
  * Führe dazu das Skript `get-spotify-auth.py` aus. Dies musst nicht unbedingt auf dem LUNA-Server geschehen; du musst nur später die generierte Datei _spotify-auth_ in diesen Ordner (`server/resources/spotify`) kopieren.
  * Es öffnet sich ein Webbrowser. Dort genehmigst du den Zugriff. Anschließend erhältst du einen _Refresh-Token_, den du im Eingabeprompt des Skripts einfügst.
  * Nun wird automatisch der _acces_token_ abgefragt und in der Datei _spotify-auth_ gespeichert sowie zur Kontrolle ausgegeben.
  * Stelle sicher, dass die Datei `spotify-auth` in diesem Ordner liegt.

#### FERTIG
Du kannst nun die Wiedergabe steuern sowie Lieder und Playlists abspielen.

**Beachte jedoch, dass bereits ein Abspielgerät aktiv ist**. Ansonsten gibt LUNA einen entsprechenden Hinweis aus.

## Raspberry Pi als Spotify Client
Du kannst Spotify auch auf einem Raspberry Pi nutzen, der als LUNA-Raumclient fungiert.
Installiere dazu _raspotify_ mit `curl -sL https://dtcooper.github.io/raspotify/install.sh | sh` nach [dieser](https://github.com/dtcooper/raspotify) Anleitung.
Nun kannst du den Client in der Spotify-App auswählen und anschließend LUNA zur Steuerung nutzen.

AQAaVc1WDgih9Ufm7w4spIlFWvfr71kOhqIoxFeXTNoeiWt0GNk8kk4PV6VqQQuSo9fX0mGcfjR5rCY-I1F3LtV2JpIUkYTtETkC30Fub8E4pgg-9p3VxnVR-hMDjsKVEJ0Su25pyEPft-hoy-Chm1nM4ZyZb0a9vquC8Y7THWmcHjn-k69yh8Ff8DybTUWRA79WJz9uW9TGuxjn6UhjBpQbVOzitiNmA32cGix_SJrzB3t17CHAqc0wJqh4GAIMGD2w5C1QgP2ct51eu8rxJmSCLBnE33VWC4VRVM_BlRdedHxQ1-RXDMdIPTbZNEEYd2U