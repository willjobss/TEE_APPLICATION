#include "HASH_sha256.h"
#include <stdio.h>
int main(){
    
    char *check="de1fbd7960fccc33593378a21ff11096893147dd827b574e3eea18caf4559093";//预留的代码
    char *fp = "C:\\Users\\adminn\\Desktop\\python\\ui.py";
    char * read=malloc(sizeof(char)*100);
    read = sha1Hash(1,fp);
    printf("%s\n",read);
    if (!strcmp(read,check)) 
    {
        printf("pass");
        system("python C:\\Users\\adminn\\Desktop\\python\\ui.py");
    }
    else
    {
        printf("fail");
    }
    
    free(read);
    return 0;
}