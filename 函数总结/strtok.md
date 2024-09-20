# strtok

`strtok` 是 C 语言中用于分割字符串的函数，定义在 `string.h` 头文件中。它的主要功能是将一个字符串分割成多个子字符串，通常是基于特定的分隔符。

### 函数原型

```c
char *strtok(char *str, const char *delim);
```

### 参数

- **`str`**：要分割的字符串。在第一次调用时，这个参数应该是要处理的字符串。后续的调用应将其设置为 `NULL`。
- **`delim`**：包含分隔符的字符串。`strtok` 将根据这些字符来分割 `str`。

### 返回值

- 返回指向下一个子字符串的指针。如果没有更多的子字符串可供提取，则返回 `NULL`。

### 使用示例

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "Hello, World! Welcome to C programming.";
    const char *delim = " ,.!";  // 分隔符: 空格、逗号、句号和感叹号
    char *token;

    // 第一次调用 strtok
    token = strtok(str, delim);
    while (token != NULL) {
        printf("%s\n", token);  // 打印每个子字符串
        token = strtok(NULL, delim);  // 后续调用
    }

    return 0;
}
```

### 注意事项

1. **原地修改**：`strtok` 会在原字符串中用 `\0` 替换分隔符，因此原字符串会被修改。
2. **线程不安全**：由于 `strtok` 使用静态变量来存储状态，因此在多线程环境中使用时可能会导致问题。可以使用 `strtok_r` 来实现线程安全的分割。
3. **连续分隔符**：如果有多个连续的分隔符，`strtok` 会返回空字符串作为子字符串。

### 总结

`strtok` 是一个方便的函数，用于将字符串分割成多个部分，适合处理以特定字符分隔的文本数据。使用时要注意对原字符串的修改和线程安全问题。
