# 熟悉spark

进入spark-shell
```
/opt/spark/bin/spark-shell
```

Try the following command, which should return 1,000,000,000:
```
spark.range(1000 * 1000 * 1000).count()
```