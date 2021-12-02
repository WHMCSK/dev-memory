# mysql常用

### 临时关闭安全更新

记得用完之后一定要SET SQL_SAFE_UPDATES = 1;

```
SET SQL_SAFE_UPDATES = 0;
update mckt.todo set iteration = 'iteration1';
SET SQL_SAFE_UPDATES = 1;
```