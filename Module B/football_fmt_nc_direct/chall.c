
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void win() {
    system("cat flag.txt");
}

void ask() {
    char name[128];
    puts("⚽ Welcome to the Football MVP survey!");
    puts("Who is your favorite player?");
    fgets(name, 256, stdin);
    printf(name);  // форматная уязвимость
    puts("Thanks for voting!");  // хотим перенаправить сюда вызов win()
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    ask();
    return 0;
}
