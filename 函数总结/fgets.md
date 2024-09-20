# fgets

`fgets` 是 C 语言中用于从文件流中读取一行字符串的函数，定义在 `stdio.h` 头文件中。它通常用于从标准输入（如键盘）或文件中读取数据。

### 函数原型

```c
char *fgets(char *str, int n, FILE *stream);
```

### 参数

- **`str`**：指向一个字符数组的指针，读取的字符串将存储在这里。
- **`n`**：要读取的最大字符数（包括结束的 `\0` 字符）。
- **`stream`**：指向输入流的指针，可以是 `stdin`（标准输入）或其他文件指针。

### 返回值

- 成功时，返回 `str` 的指针。
- 如果遇到文件结束符（EOF）或发生错误，返回 `NULL`。

### 使用示例

```c
#include <stdio.h>

int main() {
    char buffer[100];

    printf("Please enter a line of text:\n");
    if (fgets(buffer, sizeof(buffer), stdin) != NULL) {
        printf("You entered: %s", buffer);
    } else {
        printf("Error reading input.\n");
    }

    return 0;
}
```

### 注意事项

1. **行末换行符**：`fgets` 会读取行末的换行符（如果存在），并将其存储在 `str` 中。如果读取的字符串长度达到 `n-1`，则不会读取换行符。
2. **字符串结束**：`fgets` 会在读取的字符串末尾自动添加 `\0` 字符，确保字符串正确结束。
3. **缓冲区溢出**：确保提供给 `fgets` 的字符数组足够大，以容纳读取的字符串和结束的 `\0` 字符。
4. **错误处理**：在使用 `fgets` 时，建议检查返回值，以便处理可能的读取错误或 EOF。

### 总结

`fgets` 是一个安全且方便的函数，用于从输入流中读取字符串。它能够处理换行符并确保字符串以 `\0` 结束，适合用于读取用户输入或文件内容。使用时要注意缓冲区的大小和返回值的检查。
