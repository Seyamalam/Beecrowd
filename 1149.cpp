#include <cstdio>
int main() {
    int resposta = 0, a, n = -1;
    scanf("%d", &a);
    while (n <= 0) scanf("%d", &n);
    while (n--) {
        resposta += a;
        a++;
    }
    printf("%d\n", resposta);
    return 0;
}
