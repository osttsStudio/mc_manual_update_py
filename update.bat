taskkill /F /IM update.exe
timeout /T 2
mkdir bg
move .minecraft\background.png .\bg\
move .minecraft\config.ini .\
move .minecraft\update.exe .\