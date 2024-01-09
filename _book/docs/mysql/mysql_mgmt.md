# Mysql管理

## 查询表的大小

mysql中，可用“concat(round(sum(DATA_LENGTH/1024/1024),2),'M')”语句配合“where table_schema='数据库名称' AND table_name='表名称'”语句查询表的大小。

通过sql语句查询整个数据库的容量，或是单独查看表所占容量。

1. 要查询表所占的容量，就是把表的数据和索引加起来就可以了

```
select sum(DATA_LENGTH)+sum(INDEX_LENGTH) from information_schema.tables where table_schema='数据库名称';
```
上面获取的结果是以字节为单位的，可以通过%1024在%1024的到M为单位的结果。


2. 查询所有的数据大小

```
select concat(round(sum(DATA_LENGTH/1024/1024),2),'M') from tables;
```

3. 查询某个表的数据大小

```
select concat(round(sum(DATA_LENGTH/1024/1024),2),'M') from tables where table_schema='数据库名称' AND table_name='表名称';
```

在mysql中有一个information_schema数据库，这个数据库中装的是mysql的元数据，包括数据库信息、数据库中表的信息等。所以要想查询数据库占用磁盘的空间大小可以通过对information_schema数据库进行操作。

information_schema中的表主要有：

　　schemata表：这个表里面主要是存储在mysql中的所有的数据库的信息

　　tables表：这个表里存储了所有数据库中的表的信息，包括每个表有多少个列等信息。

　　columns表：这个表存储了所有表中的表字段信息。

　　statistics表：存储了表中索引的信息。

　　user_privileges表：存储了用户的权限信息。

　　schema_privileges表：存储了数据库权限。

　　table_privileges表：存储了表的权限。

　　column_privileges表：存储了列的权限信息。

　　character_sets表：存储了mysql可以用的字符集的信息。

　　collations表：提供各个字符集的对照信息。

　　collation_character_set_applicability表：相当于collations表和character_sets表的前两个字段的一个对比，记录了字符集之间的对照信息。

　　table_constraints表：这个表主要是用于记录表的描述存在约束的表和约束类型。

　　key_column_usage表：记录具有约束的列。

　　routines表：记录了存储过程和函数的信息，不包含自定义的过程或函数信息。

　　views表：记录了视图信息，需要有show view权限。

　　triggers表：存储了触发器的信息，需要有super权限。