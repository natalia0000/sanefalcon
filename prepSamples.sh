INDIR=$1
OUTDIR=$2
mkdir $OUTDIR

export DIR_FETALFRAC=/home/nzukova/SANEFALCON/Sanef
export SCRIPT_RETRO=$DIR_FETALFRAC/retro.py

export DIR_SCRIPTS=/usr/bin
export SCRIPT_PYTHON=$DIR_SCRIPTS/python2
export SCRIPT_SAMTOOLS=$DIR_SCRIPTS/samtools/bin/samtools

for SAMPLE in `find $INDIR -name "*.bam"`
do
	SHORT=`echo $SAMPLE | rev | cut -d"/" -f1 | rev`
	OUTFILE="$OUTDIR/${SHORT//".dedup.bam"/}"
	echo "IN:$SAMPLE, OUT:$OUTFILE"
	
	for ARG_TASKID in `seq 1 22` # or "X"
		do
			$SCRIPT_SAMTOOLS index $SAMPLE
			$SCRIPT_SAMTOOLS view \
			$SAMPLE \
			chr$ARG_TASKID \
			-F 20 -q 1 | \
			$SCRIPT_PYTHON $SCRIPT_RETRO| \
					awk '{print $4}' \
					    > $OUTFILE.$ARG_TASKID.start.fwd &

			$SCRIPT_SAMTOOLS view \
			$SAMPLE \
			chr$ARG_TASKID \
			-f 16 -F 4 -q 1 | \
			$SCRIPT_PYTHON $SCRIPT_RETRO | \
					awk '{print ($4 + length($10) - 1)}' \
					    > $OUTFILE.$ARG_TASKID.start.rev
		
		done
done
