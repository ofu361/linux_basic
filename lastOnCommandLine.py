"""
Um herauszufinden, was zuletzt auf deinem Linux-System passiert ist, gibt es mehrere Befehle und Logdateien, 
die dir helfen können. Hier sind einige nützliche Linux-Befehle:

1. `dmesg`: Der Befehl `dmesg` zeigt Kernel-Nachrichten an, die während des Bootvorgangs und während der 
Laufzeit erzeugt wurden. Du kannst es verwenden, um nach Hardwareproblemen oder Kernel-Fehlermeldungen zu suchen.
    dmesg
    ```
2. **`journalctl`:** Dieser Befehl gibt die Systemprotokolle aus, einschließlich Systemd-Protokolle und 
Kernel-Meldungen. Du kannst es verwenden, um Systemereignisse zu überprüfen.
    ```
    journalctl
    ```
    Um nur die Meldungen der letzten Stunden oder Minuten anzuzeigen, kannst du den `-S`- oder `-n`-Parameter 
verwenden:
    ```
    journalctl -n 50  # Zeigt die letzten 50 Zeilen an
    journalctl -S "2022-01-20 12:00:00"  # Zeigt Meldungen seit einem bestimmten Zeitpunkt an
    ```
3. **`last`:** Der Befehl `last` zeigt die Anmeldungen und Abmeldungen von Benutzern an.
    ```
    last
    ```
4. **`who`:** Dieser Befehl zeigt aktuell angemeldete Benutzer an.
    ```
    who
    ```
5. **`uptime`:** Der Befehl `uptime` gibt an, wie lange dein System aktiv ist und wie viel Last es hat.
    ```
    uptime
    ```
6. **`cat /var/log/syslog`:** Die Datei `/var/log/syslog` enthält allgemeine Systemprotokolle. 
Du kannst sie mit `cat` oder `less` anzeigen.

    cat /var/log/syslog

Diese Befehle sollten dir eine gute Übersicht über die letzten Ereignisse auf deinem Linux-System geben. Je nach Distribution und Konfiguration können die genauen Dateipfade variieren. Du kannst auch spezifischere Logdateien in den Verzeichnissen `/var/log` überprüfen, um mehr Informationen zu erhalten.
"""
print(index)
