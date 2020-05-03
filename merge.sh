INDIR=`readlink -f $1`

for i in $(seq 1 22)
do
	echo Working on Chr: $i
	sort -n -m $INDIR/*/*.$i.start.fwd $INDIR/*/*.$i.start.rev > $INDIR/merge.$i
done
