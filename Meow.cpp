#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include "meow_hash_x64_aesni.h"

static void PrintHash(meow_u128 Hash)
{
    printf("    %08X-%08X-%08X-%08X\n",
        MeowU32From(Hash, 3),
        MeowU32From(Hash, 2),
        MeowU32From(Hash, 1),
        MeowU32From(Hash, 0));
}

int main()
{
    size_t size = 128;
    meow_u128 HashA;
    HashA = _mm_loadu_si128((__m128i*)"20220610");
    char Message[] = "202000260118";
    meow_u8* seed = (meow_u8*)malloc(size);
    for (int i = 0; i <= 1000000; i++)
    {
        char input[] = "";
        MeowExpandSeed(128, input, seed);
        int Size = 8;
        meow_u128 HashB = MeowHash(seed, Size, Message);
        int HashesMatch = MeowHashesAreEqual(HashA, HashB);
        if (HashesMatch)
        {
            printf("seed:%p",(const char*)seed);
            break;
        }
    }
    free(seed);
    return 0;
}