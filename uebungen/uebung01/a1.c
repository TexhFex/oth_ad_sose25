#include <stdio.h>
#include <stdlib.h>

int iterative(int a, int b) {
    int r;
    do {
        r = a % b;
        a = b;
        b = r;
    } while (b != 0);

    return a;
}

int recursive(int a, int b) {
    if (b == 0)
        return a;
    return recursive(b, a % b);
}


int kgV_func(int a, int b) {
    int val = iterative(a, b);
    return (abs(a * b) / val);
}

int main(void) {
    // Werte sind: a, b, a*b, ggT(a,b). kgV(a,b)
    for (int a = 30; a <= 40; a++) {
        for (int b = 30; b <= 40; b++) {
            int product = a * b;
            int it = iterative(a, b);
            int kgV = kgV_func(a, b);
            printf("%d %d %d %d %d\n",
                   a, b, product, it, kgV);
        }
    }
    return 0;
}