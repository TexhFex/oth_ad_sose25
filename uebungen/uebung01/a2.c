#include <stdio.h>
#include <stdbool.h>


void sieb_von_eratosthenes(int k, bool isPrime[])
{
    for (int i = 0; i <= k; i++) {
        if(i>= 2){
            isPrime[i] = true;
        }
    }

    for (int i = 2; i * i <= k; i++) {
        if (isPrime[i]) {
            for (int j = i * i; j <= k; j += i) {
                isPrime[j] = false;
            }
        }
    }
}

int main(void)
{
    int k;
    printf("k: ");
    scanf("%d", &k);

    bool isPrime[100001];

    sieb_von_eratosthenes(k, isPrime);

    for (int i = 2; i <= k; i++) {
        if (isPrime[i]) {
            printf("%d ", i);
        }
    }
    return 0;
}
