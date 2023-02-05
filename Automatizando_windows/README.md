# Autonatizando o Windows

Script referente ao [meu artigo no Linkedin](https://www.linkedin.com/pulse/scripts-prontos-automatizando-o-windows-jo%C3%A3o-pedro-louren%C3%A7o-affonso/) sobre comandos do Windows para facilitar tarefas simples.

```bash
@echo OFF

echo  > NOME.bat

rem  abrindo o notepad
start notepad meu_arquivo.txt

rem  Abre o navegador padrão do computador no link especificado
start "" https://www.youtube.com/watch?v=dQw4w9WgXcQ

rem Internet Explorar / Microsoft Edge (Por que eles são muito diferentes...) 

start iexplore https://www.youtube.com/watch?v=dQw4w9WgXcQ

rem Firefox

start firefox https://www.youtube.com/watch?v=dQw4w9WgXcQ

rem Google Chrome

start chrome https://www.youtube.com/watch?v=dQw4w9WgXcQ

rem Abrindo Outlook

start outlook

rem Esperando 30 segundos

timeout 30

rem abrindo sites no Chrome

start chrome https://g1.globo.com
start chrome https://bbc.com
start chrome https://www.linkedin.com/feed/

rem executando scripts em outras línguas

python PATH\script.py

python PATH\outro_script.py "input do outro_script.py"

php PATH\script.php >> arquivo_de_saida.txt

PATH\outro_script_bat.bat

# Executando o ssh em outras máquinas
ssh -i chave1.pem usuario1@189.189.200.200 "df -h"

ssh -i chave2.pem usuario2@189.189.200.201 "sh meu_bash.sh"

ssh -i chave3.pem usuario3@189.189.200.202 "sh meu_bash.sh | grep 'padrão desejado'"

ssh -i chave4.pem usuario4@189.189.200.203 "sh meu_bash.sh" >> arquivo_para_registro.log

ssh -i chave5.pem usuario5@189.189.200.204 "ssh -i chave6.pem usuario@189.189.200.205 'sh meu_bash.sh'"

rem impede que a janela seja fechada, assim, você pode visualizar os outputs dos seus comandos
pause 
```
