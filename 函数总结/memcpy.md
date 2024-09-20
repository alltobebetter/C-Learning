# memcpy

`memcpy` 是 C 语言中用于内存拷贝的函数，定义在 `string.h` 头文件中。它的主要功能是将一块内存区域的内容复制到另一块内存区域。

### 函数原型

```c
void *memcpy(void *dest, const void *src, size_t n);
```

### 参数

- **`dest`**：指向目标内存区域的指针，拷贝的内容将存放在这里。
- **`src`**：指向源内存区域的指针，从这里复制内容。
- **`n`**：要拷贝的字节数。

### 返回值

- 返回指向目标内存区域 `dest` 的指针。

### 使用示例

```c
#include <stdio.h>
#include <string.h>

int main() {
    char src[] = "Hello, World!";
    char dest[20];  // 确保目标数组足够大以容纳拷贝的内容

    memcpy(dest, src, strlen(src) + 1);  // 包括 null 字符
    printf("Copied string: %s\n", dest);  // 输出: Hello, World!

    return 0;
}
```

### 注意事项

1. **重叠内存**：`memcpy` 不适合处理重叠的内存区域。如果源和目标内存区域重叠，使用 `memmove` 函数更为安全，因为 `memmove` 处理了重叠的情况。
2. **没有边界检查**：`memcpy` 不会检查目标缓冲区的大小。确保目标区域足够大以容纳要拷贝的数据，避免缓冲区溢出。
3. **返回值**：虽然返回值是 `dest` 的指针，但通常不需要使用这个返回值。

### 总结

`memcpy` 是一个高效的内存拷贝函数，适合用于复制原始内存数据。使用时要特别注意内存区域的重叠和目标缓冲区的大小，以避免潜在的错误和安全问题。
