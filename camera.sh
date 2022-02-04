
OUTPUT='log.out'
INPUT='log.in'

echo ':sunglasses: 正常に起動しました :sunglasses:' > $INPUT

while true
do
    python3 main.py < $INPUT > $OUTPUT 2>&1
    cp $OUTPUT $INPUT
    echo ':sunglasses: エラーが発生しました :sunglasses:' >> $INPUT
    sleep 3s
done

