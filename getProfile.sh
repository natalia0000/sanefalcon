export SCRIPT_GETPRO=/home/nzukova/SANEFALCON/Sanef/getProfile.py

export SCRIPT_PYTHON=python2

export INDIR=`readlink -f $1`
export NUCLDIR=`readlink -f $2`
export OUTDIR=`readlink -f $3`

mkdir $OUTDIR

for SAMPLE in `find $INDIR -name "*.1.start.fwd"`
do
	export SIMPLE=${SAMPLE//.1.start.fwd/}
	export SIMPLER=`echo $SIMPLE | rev | cut -d"/" -f1 | rev`
	for CHROM in $(seq 1 22 ) 
	do
		$SCRIPT_PYTHON $SCRIPT_GETPRO $NUCLDIR/nucl_ex3.$CHROM $SIMPLE.$CHROM.start.fwd 0 $OUTDIR/$SIMPLER.$CHROM.fwd 
		$SCRIPT_PYTHON $SCRIPT_GETPRO $NUCLDIR/nucl_ex3.$CHROM $SIMPLE.$CHROM.start.rev 1 $OUTDIR/$SIMPLER.$CHROM.rev

		$SCRIPT_PYTHON $SCRIPT_GETPRO $NUCLDIR/nucl_ex3.$CHROM $SIMPLE.$CHROM.start.fwd 1 $OUTDIR/$SIMPLER.$CHROM.ifwd 
		$SCRIPT_PYTHON $SCRIPT_GETPRO $NUCLDIR/nucl_ex3.$CHROM $SIMPLE.$CHROM.start.rev 0 $OUTDIR/$SIMPLER.$CHROM.irev
	done
done
