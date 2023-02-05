#!/bin/sh

# executa comando para todas as linhas de um arquivo
while read line:
 x=`cat $line | wc -l`;
 echo "$line - $x"; 
done < arquivo.txt;

# continua executando até que uma condição específica seja atingida
num=`ls -l diretorio_qualquer | wc -l`;
while [[ $num -le 200 ]]; do
 sleep 10;
 num=`ls -l diretorio_qualquer | wc -l`;
done;

echo "ALERTA!!!!"
