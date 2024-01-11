#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#define pri_blank printf("               ") //15
enum wday {Sun, Mon, Tue, Wed, Thu, Fri, Sat};
struct cal_info{
	int y_num;
	int m_num;
	int d_cnt;
	int mthd_cnt;
	enum wday fst; };
struct sch{
	_Bool tf;
	char *schd;};
int yun_dcnt(int year);
int mth_dcnt(int year, int mth);
void print_cal(struct cal_info *, struct sch *);
void sch_input(struct sch (*)[], int);
int main(void){
	enum wday wday;
	struct cal_info cal;
	struct cal_info *pcal;
	pcal=&cal;

	printf("년을 입력하세요: ");
	scanf("%d",&pcal->y_num);
	printf("월을 입력하세요: ");
	scanf("%d",&pcal->m_num);
	pcal->mthd_cnt=mth_dcnt(pcal->y_num,pcal->m_num);
	struct sch sch[(*pcal).mthd_cnt];
	struct sch (*psch)[(*pcal).mthd_cnt];
	psch=&sch;
	for (int i=0;i<pcal->mthd_cnt;i++){
		sch[i].tf=0;
		sch[i].schd=NULL; }
	
	pcal->d_cnt=0;
	for (int i=1;i<pcal->y_num;i++)
		pcal->d_cnt += yun_dcnt(i);
	for (int i=1;i<pcal->m_num;i++)
		pcal->d_cnt += mth_dcnt(pcal->y_num,i);
	pcal->fst=(pcal->d_cnt +1)%7;
	
	int sel;
	system("clear");
	while (1) {
		print_cal(pcal,sch);
		while (1){
			printf("메뉴를 입력하세요: ");
			scanf("%d",&sel);
			if (sel/5==0) break; }
		if (sel==4) break;
		else if (sel==1){
			int day;
			while (1){
				printf("날짜를 입력하세요: ");
				scanf("%d",&day);
				if (day>=0 && day<=pcal->mthd_cnt){
					if (day==0) break;
					else if (sch[day-1].tf==0) break;}}
			if (day==0) ;
			else {
				sch_input(psch,day);
			}
		}
		else if (sel==2){
			int day;
            while (1){
                printf("날짜를 입력하세요: ");
                scanf("%d",&day);
                if (day>=0 && day<=pcal->mthd_cnt){
                    if (day==0) break;
                    else if (sch[day-1].tf) break;}}
			sch[day-1].tf=0;
			sch[day-1].schd=NULL;
		}
		else if (sel==3){
			int day;
            while (1){
                printf("날짜를 입력하세요: ");
                scanf("%d",&day);
                if (day>=0 && day<=pcal->mthd_cnt){
                    if (day==0) break;
                    else if (sch[day-1].tf) break;}}
			if (day)
				printf("%d년 %d월 %d일 일정은 %s입니다.\n",pcal->y_num,pcal->m_num,day,sch[day-1].schd);

		}
		sleep(3);
		system("clear");
	}
	for (int i=0;i<pcal->mthd_cnt;i++)
		free(sch[i].schd);
	return 0;
}
int yun_dcnt(int year){
	if (year%400==0) return 366;
	else if (year%100==0) return 365;
	else if (year%4==0) return 366;
	return 365; }
int mth_dcnt(int year, int mth){
	if (mth==2){
		if (yun_dcnt(year)==365)
			return 28;
		else
			return 29; }
	else if (mth<8){
		if (mth%2)
			return 31;
		else return 30;}
	else {
		if (mth%2)
			return 30;
		else return 31;}}
void print_cal(struct cal_info *pcal, struct sch *sch){
	printf("\n\n");
	pri_blank;
	pri_blank;
	printf("%4d년 %d월\n",pcal->y_num, pcal->m_num);
	pri_blank;
	printf("   Sun   Mon   Tue   Wed   Thu   Fri   Sat\n");
	pri_blank;
	int cnt=pcal->fst;
	for (int i=1;i<=pcal->fst;i++)
		printf("      ");
	for (int i=1;i<=pcal->mthd_cnt;i++){
		if (sch[i-1].tf){
			if (i<10)
				printf("    *%d",i);
			else
				printf("   *%d",i);}
		else
			printf("%6d",i);
		cnt++;
		if (cnt%7==0){
			printf("\n");
			pri_blank;}}
	for (int i=0;i<5;i++)
		printf("\n");
	printf("1. 일정 입력         2. 일정 삭제         3. 일정 확인         4. 종료\n");
}
void sch_input(struct sch (*sch)[], int day){
	char temp[100];
	printf("일정을 입력하세요: ");
	getchar();
	scanf("%[^\n]",temp);
	getchar();
	
	(*sch)[day-1].schd=(char *)calloc(strlen(temp)+1,sizeof(char));
	strcpy((*sch)[day-1].schd, temp);
	(*sch)[day-1].tf=1;
	return;
}
