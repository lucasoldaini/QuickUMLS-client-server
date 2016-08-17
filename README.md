# QuickUMLS-client-server

On server: 

```bash
$ bash start start_server.sh
```

On client

```python
from quickumls_client import get_quick_umls_client

cl = get_quick_umls_client(host='server.address', port=4645)
cl.match('lyme disease)
```
