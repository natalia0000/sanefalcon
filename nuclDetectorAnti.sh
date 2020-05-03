export SCRIPT_NUCDEC=/home/nzukova/SANEFALCON/Sanef/nuclDetector.py

export SCRIPT_PYTHON=/usr/bin/python2

export INDIR=`readlink -f $1`

for CHROM in $(seq 22 -1 1)
do
	$SCRIPT_PYTHON $SCRIPT_NUCDEC $INDIR/anti.$CHROM $INDIR/nucl_ex3.$CHROM
done

