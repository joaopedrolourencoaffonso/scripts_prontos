#!/bin/sh

for dir in AM-12 ES-87 MG MG-2 MT-01 RJ RJ-12 RJ-3 RS-12 RS-3 RS-12 ES-77 TO MG-20 MT-11 RJ-6 AC-12 PA-3 PA-12 GO-3; do
 total=`ls -l /path_para_o_diretorio/$dir | wc -l`;
 echo "$dir - $total"
done;

# Exportando para um CSV
for dir in AM-12 ES-87 MG MG-2 MT-01 RJ RJ-12 RJ-3 RS-12 RS-3 RS-12 ES-77 TO MG-20 MT-11 RJ-6 AC-12 PA-3 PA-12 GO-3; do
 total=`ls -l /path_para_o_diretorio/$dir | wc -l`;
 echo "$dir , $total"
done >> arquivo.csv;

# Loop for dentro de outro loop for
for data in 20221203 20221204 20221205 20221206 20221207; do
 for dir in AM-12 ES-87 MG MG-2 MT-01 RJ RJ-12 RJ-3 RS-12 RS-3 RS-12 ES-77 TO MG-20 MT-11 RJ-6 AC-12 PA-3 PA-12 GO-3; do
  total=`ls -l /path_para_o_diretorio/$dir | grep $data | wc -l`;
  echo "$data - $dir - $total"
 done;
done;

# Loop for para range de números
for i in {1..20}; do
  x=`cat arquivo.log.$i | wc -l`;
  echo "arquivo.log.$i , $x";
done;

# Loop for para range de números com passo específico
for i in {10..200..10}; do
  x=`cat arquivo.log.$i | wc -l`;
  echo "arquivo.log.$i , $x";
done;
