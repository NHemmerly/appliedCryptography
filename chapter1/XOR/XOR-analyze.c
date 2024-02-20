#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    FILE *fi, *fi2;
    int c;
    int d;
    long offset = strtol(argv[1], NULL, 10);
    int sameByte = 0;
    int byteLength = 0;


    if ((fi = fopen(argv[2], "rb")) != NULL) {
        if ((fi2 = fopen(argv[3], "rb")) != NULL) {
            fseek(fi2, offset, SEEK_SET);
            while ((c = getc(fi)) != EOF) 
            {
                d = getc(fi2);
                /*if (d != EOF) {
                    fseek(fi2, 1, SEEK_CUR);
                } else{
                    fseek(fi2, 0, SEEK_SET);
                }*/
                c ^= d;
                if (c == 0) {
                    sameByte++;
                }
                byteLength++;
            }
            fclose(fi2);
        }
        fclose(fi);
    }
    printf("offset: %li\n", offset);
    printf("byteLength: %d\n numberOfSame: %d\n", byteLength, sameByte);

}