

查看GPU：
```
import subprocess
try:
    subprocess.run("nvidia-smi", shell=True)
except Exception as e:
    print(e)
```