UMLS_PATH="$HOME/irlab/datasets/umls-2015ab/installation/META"
QUICKUMLS_DEST="cache/QuickUMLS"
SERVER_PORT=4645
SERVER_THRESHOLD=0.9

if [ ! -d $QUICKUMLS_DEST ]; then
    cd QuickUMLS
    bash setup_simstring.sh 3
    python3 install.py $UMLS_PATH "../$QUICKUMLS_DEST"
    cd ..
fi

python3 quickumls_server.py -P $SERVER_PORT -f $QUICKUMLS_DEST -t $SERVER_THRESHOLD -H 0.0.0.0 -v

