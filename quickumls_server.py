try:
    from QuickUMLS.quickumls import QuickUMLS
    from MinimalServer import run_server
except ImportError:
    from .QuickUMLS.quickumls import QuickUMLS
    from .MinimalServer import run_server

from argparse import ArgumentParser


def run_quickumls_server(opts):
    matcher = QuickUMLS(
        quickumls_fp=opts.quickumls_fp,
        threshold=opts.threshold,
        similarity_name=opts.similarity_name,
        window=opts.window,
        min_match_length=opts.min_match_length,
        verbose=opts.verbose
    )

    run_server(matcher, host=opts.host, port=opts.port, buffersize=4096)


if __name__ == '__main__':
    ap = ArgumentParser()
    ap.add_argument('-f', '--quickumls-fp', default='cache/QuickUMLS')
    ap.add_argument('-H', '--host', default='localhost')
    ap.add_argument('-P', '--port', default=4645, type=int)
    ap.add_argument('-t', '--threshold', default=0.8, type=float)
    ap.add_argument('-s', '--similarity_name', default='jaccard')
    ap.add_argument('-w', '--window', default=5, type=int)
    ap.add_argument('-l', '--min-match-length', default=3, type=int)
    ap.add_argument('-v', '--verbose', action='store_true')
    opts = ap.parse_args()
    run_quickumls_server(opts)
