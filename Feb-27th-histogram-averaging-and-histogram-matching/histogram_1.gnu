set terminal pngcairo  transparent enhanced font "arial,10" fontscale 1.0 size 600, 400
set output 'histogram.2.png'
set style fill solid 1.0 border lt -1
set key fixed right top vertical Right noreverse noenhanced autotitle nobox
set style increment default
set style histogram clustered gap 1 title textcolor lt -1
set datafile missing '-'
set style data histograms
set xtics border in scale 0,0 nomirror rotate by -45  autojustify
set xtics  norangelimit
set xtics   ()
set title "A typical disctribution of a dark image"
set xrange [ * : * ] noreverse writeback
set yrange [ * : * ] noreverse writeback
plot 'histogram_1.dat' using 2:xtic(1) title 'frequency of pixel range'
