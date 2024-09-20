# strlen

`strlen` 是 C 语言中用于计算字符串长度的函数，定义在 `string.h` 头文件中。

### 函数原型

```c
size_t strlen(const char *str);
```

### 参数

- **`str`**：指向以 null 结尾的字符串的指针。这个字符串应该是有效的，并且以 `\0`（空字符）结束。

### 返回值

- 返回字符串 `str` 的长度（不包括结束的 `\0` 字符），类型为 `size_t`。

### 使用示例

```c
#include <stdio.h>
#include <string.h>

int main() {
    const char *myString = "Hello, World!";
    size_t length = strlen(myString);
    
    printf("The length of the string is: %zu\n", length);  // 输出: 13
    return 0;
}
```

### 注意事项

1. **以 null 结尾**：`strlen` 计算长度时依赖于字符串以 `\0` 结尾。如果传入的字符串没有以 `\0` 结尾，可能会导致未定义行为。
2. **性能考虑**：`strlen` 函数的时间复杂度为 \(O(n)\)，其中 \(n\) 是字符串的长度，因为它需要遍历整个字符串以找到结束的 `\0` 字符。
3. **返回类型**：返回类型为 `size_t`，这是一种无符号整数类型，适合表示内存大小或对象的长度。

### 总结

`strlen` 是一个基本且常用的函数，用于获取字符串的长度。在使用时，确保字符串是有效的，并以 null 结尾，以避免潜在的错误。
