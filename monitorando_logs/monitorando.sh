#!/bin/sh

last_count=`cat last.txt`

current_count=`cat arquivo_de.log | grep "[0-9]\|[a-z]\|[A-Z]" | wc -l | tee last.txt`;

new_lines=$((current_count - last_count));

last_byte_size=`cat lastbytesize.txt`;
bytes_size=`ls -l arquivo_de.log | awk '{print $5}' | tee lastbytesize.txt`;

new_bytes=$((bytes_size - last_byte_size));

# Perceba que primeiro apagamos o conteúdo original do arquivo: ">" e então começamos a anexar elementos: ">>"

echo "# TYPE new_lines gauge" > /path/counter.prom;
echo "new_lines $new_lines" >> /path/counter.prom;

echo "# TYPE new_bytes gauge" >> /path/counter.prom;
echo "new_bytes $new_bytes" >> /path/counter.prom;

echo "# TYPE total_size gauge" >> /path/counter.prom;
echo "total_size $bytes_size" >> /path/counter.prom;

echo "# TYPE total_lines gauge" >> /path/counter.prom;
echo "total_lines $current_count" >> /path/counter.prom;
