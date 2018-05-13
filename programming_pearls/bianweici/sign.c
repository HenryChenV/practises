#include<stdio.h>
#include <stdlib.h>
#include <string.h>
#include "base.h"

int charcomp(char *x, char *y) { return *x - *y; }

int main(void)
{
    char word[WORDMAX], sig[WORDMAX];
    while (scanf("%s", word) != EOF) {
        strcpy(sig, word);
        qsort(sig, strlen(sig), sizeof(char), (int (* _Nonnull)(const void *, const void *))(charcomp));
        printf("%s %s\n", sig, word);
    }
    return 0;
}
