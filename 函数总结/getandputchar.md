# getchar和putchar

`getchar` 和 `putchar` 是 C 语言中用于字符输入和输出的基本函数，分别用于从标准输入读取单个字符和向标准输出写入单个字符。

### getchar

#### 函数原型

```c
int getchar(void);
```

#### 返回值

- 返回读取的字符（以 `int` 类型返回，以便能够返回 `EOF`），如果发生错误或到达文件结束符（EOF），则返回 `EOF`。

#### 使用示例

```c
#include <stdio.h>

int main() {
    int ch;

    printf("Please enter a character: ");
    ch = getchar();  // 读取一个字符

    printf("You entered: ");
    putchar(ch);     // 输出读取的字符
    putchar('\n');   // 输出换行符

    return 0;
}
```

### putchar

#### 函数原型

```c
int putchar(int char);
```

#### 参数

- **`char`**：要写入的字符，作为 `int` 类型传入。

#### 返回值

- 返回写入的字符，如果发生错误，则返回 `EOF`。

#### 使用示例

在上述示例中，`putchar` 用于输出读取的字符。

### 注意事项

1. **缓冲区**：`getchar` 和 `putchar` 都是基于标准输入输出流的，它们会受到输入输出缓冲区的影响。
2. **字符处理**：`getchar` 读取的是单个字符，可能包括换行符（当用户按下 Enter 键时），而 `putchar` 仅输出一个字符。
3. **返回值检查**：在实际使用中，建议检查 `getchar` 和 `putchar` 的返回值，以处理可能的错误或 EOF。

### 总结

`getchar` 和 `putchar` 是简单而有效的字符输入输出函数，适合用于处理单个字符的情况。它们是 C 语言中进行基本字符处理的基础函数。
