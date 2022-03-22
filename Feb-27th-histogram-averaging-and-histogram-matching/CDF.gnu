set terminal pngcairo  transparent enhanced font "arial,10" fontscale 1.0 size 600, 400 
set output 'cdf.1.png'
#set output 'cdf.2.png'
set key left box
set style increment default
set samples 200
set title "CDF"
set title font ",20" norotate
set xrange [* : *] noreverse writeback
plot [0:255] x * (510.0 - x)/3.72 title "P(r)" with dots
# plot [0:255] x*68.6 title "P(r)" with dots
