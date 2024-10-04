# C Answer

**1. 奇偶判断:**

```c
#include <stdio.h>

int main() {
  int num;
  scanf("%d", &num); // 读取输入的整数

  if (num % 2 == 0) { // 使用模运算符判断是否能被2整除
    printf("Even\n"); // 如果余数为0，则为偶数
  } else {
    printf("Odd\n"); // 否则为奇数
  }

  return 0;
}
```

**2. 最大值:**

```c
#include <stdio.h>

int main() {
  int a, b, c;
  scanf("%d %d %d", &a, &b, &c); // 读取三个整数

  int max = a; // 假设a为最大值

  if (b > max) { // 如果b大于当前最大值
    max = b;     // 更新最大值为b
  }
  if (c > max) { // 如果c大于当前最大值
    max = c;     // 更新最大值为c
  }

  printf("%d\n", max); // 输出最大值

  return 0;
}
```

**3. 求和:**

```c
#include <stdio.h>

int main() {
  int n, sum = 0;
  scanf("%d", &n); // 读取输入的正整数

  for (int i = 1; i <= n; i++) { // 循环从1到n
    sum += i; // 累加每个数字到sum
  }

  printf("%d\n", sum); // 输出总和

  return 0;
}
```

**4. 阶乘:**

```c
#include <stdio.h>

int main() {
  int n, factorial = 1;
  scanf("%d", &n); // 读取输入的非负整数

  for (int i = 1; i <= n; i++) { // 循环从1到n
    factorial *= i; // 累乘每个数字到factorial
  }

  printf("%d\n", factorial); // 输出阶乘结果

  return 0;
}
```

**5. 斐波那契数列:**

```c
#include <stdio.h>

int main() {
  int n;
  scanf("%d", &n); // 读取输入的非负整数

  int a = 0, b = 1; // 初始化前两项

  for (int i = 0; i < n; i++) {
    printf("%d ", a); // 输出当前项

    int next = a + b; // 计算下一项
    a = b;          // 更新前一项
    b = next;       // 更新后一项
  }

  printf("\n");

  return 0;
}
```

**6. 数组反转:**

```c
#include <stdio.h>

int main() {
  int n;
  scanf("%d", &n); // 读取数组大小

  int arr[n];
  for (int i = 0; i < n; i++) {
    scanf("%d", &arr[i]); // 读取数组元素
  }

  for (int i = n - 1; i >= 0; i--) { // 从最后一个元素开始循环
    printf("%d ", arr[i]); // 输出当前元素
  }

  printf("\n");

  return 0;
}
```

**7. 字符串回文判断:**

```c
#include <stdio.h>
#include <string.h>

int main() {
  char str[100];
  scanf("%s", str); // 读取字符串

  int len = strlen(str); // 获取字符串长度
  int isPalindrome = 1; // 假设是回文串

  for (int i = 0; i < len / 2; i++) { // 只需比较一半的字符
    if (str[i] != str[len - i - 1]) { // 如果对应字符不相等
      isPalindrome = 0; // 不是回文串
      break;             // 退出循环
    }
  }

  if (isPalindrome) {
    printf("Yes\n");
  } else {
    printf("No\n");
  }

  return 0;
}
```

**8. 二分查找:**

```c
#include <stdio.h>

int main() {
  int n, target;
  scanf("%d %d", &n, &target); // 读取数组大小和目标元素

  int arr[n];
  for (int i = 0; i < n; i++) {
    scanf("%d", &arr[i]); // 读取数组元素
  }

  int left = 0, right = n - 1; // 初始化左右边界

  while (left <= right) {
    int mid = left + (right - left) / 2; // 计算中间位置

    if (arr[mid] == target) { // 如果找到目标元素
      printf("Found at index %d\n", mid);
      return 0;
    } else if (arr[mid] < target) { // 如果目标元素在右边
      left = mid + 1; // 更新左边界
    } else { // 如果目标元素在左边
      right = mid - 1; // 更新右边界
    }
  }

  printf("Not found\n"); // 如果循环结束仍未找到

  return 0;
}
```

**9. 矩阵转置:**

```c
#include <stdio.h>

int main() {
  int m, n;
  scanf("%d %d", &m, &n); // 读取矩阵的行数和列数

  int matrix[m][n];
  for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
      scanf("%d", &matrix[i][j]); // 读取矩阵元素
    }
  }

  for (int j = 0; j < n; j++) {
    for (int i = 0; i < m; i++) {
      printf("%d ", matrix[i][j]); // 输出转置后的元素
    }
    printf("\n");
  }

  return 0;
}
```

**10. 简单排序 (冒泡排序):**

```c
#include <stdio.h>

int main() {
  int n;
  scanf("%d", &n); // 读取数组大小

  int arr[n];
  for (int i = 0; i < n; i++) {
    scanf("%d", &arr[i]); // 读取数组元素
  }

  for (int i = 0; i < n - 1; i++) { // 外层循环控制比较轮数
    for (int j = 0; j < n - i - 1; j++) { // 内层循环比较相邻元素
      if (arr[j] > arr[j + 1]) { // 如果顺序错误
        int temp = arr[j];       // 交换两个元素
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }

  for (int i = 0; i < n; i++) {
    printf("%d ", arr[i]); // 输出排序后的数组
  }

  printf("\n");

  return 0;
}
```
