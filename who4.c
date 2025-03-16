//who3를 수정하여 오리지널 who커맨드와 출력을 일치시킨다.  
//localtime과  strftime 함수를 포매팅 타임을 위해 확인해라?
//who2를 수정하여 버퍼 기능을 주가한다.

#include <stdio.h>
#include <sys/types.h>
#include <utmp.h>
#include <fcntl.h>
#include <stdlib.h>
#include <time.h>

#define SHOWHOST

int utmp_open(char *);
void utmp_close();

void show_info(struct utmp *utbufp)
{
    printf("%-12.12s", utbufp->ut_name);
    printf(" ");
    printf("%-12.12s", utbufp->ut_line);
    printf(" ");
    printf("%-12.12ld", utbufp->ut_time);
    printf(" ");
#ifdef SHOWHOST
    printf("(%s)", utbufp->ut_host);
#endif
    printf("\n");
}

// void show_info(struct utmp *)


void showtime(time_t);

int main()
{
    struct utmp *utbufp,
                *utmp_next();
    
    if(utmp_open(  UTMP_FILE  ) == -1){
            perror(UTMP_FILE);
            exit(1);
    }
    
    while((utbufp = utmp_next()  ) != ((struct utmp *) NULL))
        show_info(utbufp);

    utmp_close();

    return 0;
}