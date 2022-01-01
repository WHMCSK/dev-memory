# go语言和java语言加密解密对比

## Golang两种方法实现MD5加密

```
package main

import (
    "crypto/md5"
    "fmt"
    "io"
)

func main() {
    str := "123456"
    //方法一
    data := []byte(str)
    has := md5.Sum(data)
    md5str1 := fmt.Sprintf("%x", has) //将[]byte转成16进制
    fmt.Println(md5str1)   
    //方法二
    w := md5.New()
    io.WriteString(w, str)
    //将str写入到w中
    md5str2 := fmt.Sprintf("%x", w.Sum(nil))

    fmt.Println(md5str2)





//结果
//e10adc3949ba59abbe56e057f20f883e
//e10adc3949ba59abbe56e057f20f883e
}
```

## java实现MD5加密

```
/*
 * Copyright (c) 2021.  武汉美宸时科科技有限公司 www.fashiontech.top
 */

package top.fashiontech.device.biz;

import org.apache.commons.codec.digest.DigestUtils;

public class OperationApplication {
    public static void main(String[] args) {
        System.out.println("-----------------ooooo-------" + DigestUtils.md5Hex("123456"));
    }
}

//结果
//e10adc3949ba59abbe56e057f20f883e
//e10adc3949ba59abbe56e057f20f883e
```