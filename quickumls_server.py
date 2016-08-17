from QuickUMLS.quickumls import QuickUMLS
from argparse import ArgumentParser
from MinimalServer import run_server

def run_quickumls_server(opts):

    matcher = QuickUMLS(
        quickumls_fp=opts.quickumls_fp,
        threshold=opts.threshold,
        similarity_name=opts.similarity_name,
        window=opts.window)

    run_server(matcher, host=opts.host, port=opts.port,
               pickle_protocol=2, buffersize=4096)

if __name__ == '__main__':
    ap = ArgumentParser()
    ap.add_argument('-f', '--quickumls-fp', default='cache/QuickUMLS')
    ap.add_argument('-H', '--host', default='localhost')
    ap.add_argument('-P', '--port', default=4645, type=int)
    ap.add_argument('-t', '--threshold', default=0.8, type=float)
    ap.add_argument('-s', '--similarity_name', default='jaccard')
    ap.add_argument('-w', '--window', default=5, type=int)
    opts = ap.parse_args()
    run_quickqumls_server(opts)


