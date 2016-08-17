# QuickUMLS-client-server

On server:

```bash
$ bash start start_server.sh
```

On client

```python
from quickumls_client import get_quickumls_client

cl = get_quickumls_client(host='server.address', port=4645)
cl.match('lyme disease')
```
