# 我是一个快乐的沙漏

## 代码实现：第二版，9/13 18：31版

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void middle(char symbol[], int stringlength) {
    char temp[stringlength + 1];
    int index = 0;
    for (int i = 0; i < stringlength; i += 2) {
        temp[index++] = symbol[i];
    }
    for (int i = stringlength - (stringlength % 2 == 0 ? 1 : 2); i > 0; i -= 2) {
        temp[index++] = symbol[i];
    }
    temp[index] = '\0';
    strcpy(symbol, temp);
}

int hourglass(int time, int downstar) {
    if (time < 0) {
        exit(0);
    } else if (time > 16) {
        printf("您输入的时间已经超过16，请重新输入：");
        scanf("%d", &time);
        hourglass(time, 0);
    }

    int upblock = 16 - time;
    int rows[] = {7, 5, 3, 1};
    printf("---------\n");
    for (int i = 0; i < 4; i++) {
        char symbol[rows[i]];
        for (int j = 0; j < rows[i]; j++) {
            if (upblock > 0) {
                symbol[j] = ' ';
                upblock--;
            } else {
                symbol[j] = '*';
            }
        }
        middle(symbol, rows[i]);
        for (int space = (7 - rows[i]) / 2; space > 0; space--) {
            printf(" ");
        }
        printf("\\");
        printf("%s/\n", symbol);
    }

    int downblock = 16 - downstar;
    for (int i = 3; i >= 0; i--) {
        char symbol[rows[i]];
        for (int j = 0; j < rows[i]; j++) {
            if (downblock > 0) {
                symbol[j] = ' ';
                downblock--;
            } else {
                symbol[j] = '*';
            }
        }
        middle(symbol, rows[i]);
        for (int space = (7 - rows[i]) / 2; space > 0; space--) {
            printf(" ");
        }
        printf("/");
        printf("%s\\\n", symbol);

    }
    printf("---------\n");
    sleep(1);
    system("clear");
    hourglass(time - 1, downstar + 1);

    return 0;
}

int main() {
    int time;
    printf("请输入你要计算的秒数，范围在1~16：");
    scanf("%d", &time);
    hourglass(time, 0);
    return 0;
}
```

## 输出示例

```
---------
\       /
 \*****/
  \***/
   \*/
   / \
  /   \
 /     \
/*******\
---------
```

## 代码实现：exe打包版

```c
//此版本用GPT4修改，因为scanf的安全性问题不能打包exe
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void middle(char symbol[], int stringlength) {
    char temp[stringlength + 1];
    int index = 0;
    for (int i = 0; i < stringlength; i += 2) {
        temp[index++] = symbol[i];
    }
    for (int i = stringlength - (stringlength % 2 == 0 ? 1 : 2); i > 0; i -= 2) {
        temp[index++] = symbol[i];
    }
    temp[index] = '\0';
    strcpy(symbol, temp);
}

int hourglass(int time, int downstar) {
    if (time < 0) {
        return 0;
    } else if (time > 16) {
        printf("您输入的时间已经超过16，请重新输入：");
        if (scanf("%d", &time) != 1) {
            printf("输入无效，请输入一个整数。\n");
            return -1;  // 错误处理，返回非零值表示失败
        }
        return hourglass(time, 0);
    }

    int upblock = 16 - time;
    int rows[] = {7, 5, 3, 1};
    printf("---------\n");
    for (int i = 0; i < 4; i++) {
        char symbol[rows[i]];
        for (int j = 0; j < rows[i]; j++) {
            if (upblock > 0) {
                symbol[j] = ' ';
                upblock--;
            } else {
                symbol[j] = '*';
            }
        }
        middle(symbol, rows[i]);
        for (int space = (7 - rows[i]) / 2; space > 0; space--) {
            printf(" ");
        }
        printf("\\");
        printf("%s/\n", symbol);
    }

    int downblock = 16 - downstar;
    for (int i = 3; i >= 0; i--) {
        char symbol[rows[i]];
        for (int j = 0; j < rows[i]; j++) {
            if (downblock > 0) {
                symbol[j] = ' ';
                downblock--;
            } else {
                symbol[j] = '*';
            }
        }
        middle(symbol, rows[i]);
        for (int space = (7 - rows[i]) / 2; space > 0; space--) {
            printf(" ");
        }
        printf("/");
        printf("%s\\\n", symbol);
    }
    printf("---------\n");

    sleep(1);
    // 处理 system 函数返回值
    if (system("clear") == -1) {
        printf("清屏命令执行失败。\n");
        return -1;  // 错误处理
    }

    return hourglass(time - 1, downstar + 1);
}

int main() {
    int time;
    printf("请输入你要计算的秒数，范围在1~16：");
    // 处理 scanf 返回值
    if (scanf("%d", &time) != 1) {
        printf("输入无效，请输入一个整数。\n");
        return 1;  // 返回错误代码
    }

    if (time < 1 || time > 16) {
        printf("输入的秒数超出范围，请输入1到16之间的值。\n");
        return 1;  // 返回错误代码
    }

    // 调用 hourglass 函数
    if (hourglass(time, 0) != 0) {
        printf("程序执行中发生错误。\n");
        return 1;  // 返回错误代码
    }

    return 0;
}
```

## 代码实现：第一版

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void middle(char symbol[], int stringlength) {
    char temp[stringlength + 1];
    int index = 0;
    for (int i = 0; i < stringlength; i += 2) {
        temp[index++] = symbol[i];
    }
    for (int i = stringlength - (stringlength % 2 == 0 ? 1 : 2); i > 0; i -= 2) {
        temp[index++] = symbol[i];
    }
    temp[index] = '\0';
    strcpy(symbol, temp);
}

int hourglass(int time, int downstar) {
    if (time < 0) {
        exit(0);
    } else if (time > 16) {
        printf("您输入的时间已经超过16，请重新输入：");
        scanf("%d", &time);
        hourglass(time, 0);
    }

    int upblock = 16 - time;
    int rows[] = {7, 5, 3, 1};

    for (int i = 0; i < 4; i++) {
        char symbol[rows[i]];
        for (int j = 0; j < rows[i]; j++) {
            if (upblock > 0) {
                symbol[j] = '-';
                upblock--;
            } else {
                symbol[j] = '*';
            }
        }
        middle(symbol, rows[i]);
        for (int space = (7 - rows[i]) / 2; space > 0; space--) {
            printf(" ");
        }
        printf("%s\n", symbol);
    }

    int downblock = 16 - downstar;
    for (int i = 3; i >= 0; i--) {
        char symbol[rows[i]];
        for (int j = 0; j < rows[i]; j++) {
            if (downblock > 0) {
                symbol[j] = '-';
                downblock--;
            } else {
                symbol[j] = '*';
            }
        }
        middle(symbol, rows[i]);
        for (int space = (7 - rows[i]) / 2; space > 0; space--) {
            printf(" ");
        }
        printf("%s\n", symbol);
    }

    sleep(1);
    system("clear");
    hourglass(time - 1, downstar + 1);

    return 0;
}

int main() {
    int time;
    printf("请输入你要计算的秒数，范围在1~16：");
    scanf("%d", &time);
    hourglass(time, 0);
    return 0;
}
```

## 输出示例

```
---*---
 *****
  ***
   *
   -
  ---
 -----
-******
```

## 视频演示

[点击代码运行演示](https://ex.dreamor.top/tmp/hourglass.mp4)


## 提示

由于使用的是Replit上的Linux系统，所以清屏函数在Windows系统上可能有所不同。

## 总结与收获

Middle函数部分借用了GPT-4的能力，并且认为GPT-4的代码能力实际超过4o（API版本），Claud代码能力尚未测试，因为太贵。

此代码仍有不完美的地方，主要是懒得打印边框了。而且这个代码认识到我自己好菜（bushi），总之也算是拖拖拉拉完成了，也是可以睡觉去了。此代码让我认识到GPT-4o的代码强度完全不如4，另外，Openai似乎在今天（9月13号）出了一个o1，进行数学计算和程序推理，我准备过今天引入我的网站试试:)。不过总体来讲真的如果让我一个人写我肯定只能写个屎山，总之就这样了，你可以试着运行一下我这个代码:)P.S.突然感觉Gemini好菜。

个人感觉真的这种题肯定超过900分了，因为我做900分一般最长也就一个小时（包括我那读不懂的题干），而这个代码我做了5-7个小时:(

最后，人生苦短，我用Python，真的不想学C了啊啊啊啊！
