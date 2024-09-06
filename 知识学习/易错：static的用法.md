#

在 C 语言中，`static` 关键字有多种用途，主要用于控制变量和函数的存储持续性和可见性。下面是 `static` 的几种常见用法及其详细说明。

### 1. 静态局部变量

当在函数内部声明一个变量为 `static` 时，该变量的生命周期将延续至程序结束，而不仅仅是函数调用期间。每次调用该函数时，该变量的值会保持不变。

**示例：**

```c
#include <stdio.h>

void counter() {
    static int count = 0; // 静态局部变量
    count++;
    printf("Count: %d\n", count);
}

int main() {
    counter(); // 输出: Count: 1
    counter(); // 输出: Count: 2
    counter(); // 输出: Count: 3
    return 0;
}
```

### 2. 静态全局变量

当在文件级别（全局作用域）声明一个变量为 `static` 时，该变量的作用域限制在该文件内，其他文件无法访问。

**示例：**

```c
// file1.c
#include <stdio.h>

static int globalVar = 10; // 静态全局变量

void display() {
    printf("Global Variable: %d\n", globalVar);
}

// file2.c
#include <stdio.h>

extern int globalVar; // 这将无法编译，因为 globalVar 是静态的

int main() {
    display();
    return 0;
}
```

### 3. 静态函数

当一个函数被声明为 `static` 时，它的作用域仅限于定义它的文件，其他文件无法调用该函数。

**示例：**

```c
// file1.c
#include <stdio.h>

static void helperFunction() { // 静态函数
    printf("This is a static function.\n");
}

void publicFunction() {
    helperFunction(); // 可以在同一文件中调用
}

// file2.c
#include <stdio.h>

extern void publicFunction();

int main() {
    publicFunction(); // 这将有效
    // helperFunction(); // 这将无法编译，因为 helperFunction 是静态的
    return 0;
}
```

### 总结

- **静态局部变量**：在函数内部使用，生命周期持续到程序结束，值在多次调用中保持。
- **静态全局变量**：在文件级别使用，作用域限制在定义它的文件内。
- **静态函数**：在文件级别使用，作用域限制在定义它的文件内，其他文件无法调用。

使用 `static` 可以有效地控制变量和函数的作用域与生命周期，帮助避免命名冲突和不必要的全局状态。
