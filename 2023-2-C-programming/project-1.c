#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
struct card{
	char shape;
	char num[3];};
_Bool dup(struct card mycard[]);
_Bool royal_straight_flush(struct card mycard[]);
_Bool back_straight_flush(struct card mycard[]);
_Bool straight_flush(struct card mycard[]);
_Bool four_card(struct card mycard[]);
_Bool full_house(struct card mycard[]);
_Bool flush(struct card mycard[]);
_Bool mountain(struct card mycard[]);
_Bool back_straight(struct card mycard[]);
_Bool straight(struct card mycard[]);
_Bool triple(struct card mycard[]);
_Bool two_pair(struct card mycard[]);
_Bool one_pair(struct card mycard[]);
int main(void){
	struct card mycard[5];
	int select;
	printf("1. 직접 입력          2. 랜덤 생성\n\n");
	srand(time(NULL));	
	while (1){
		printf("번호를 입력하세요 : ");
		scanf("%d",&select);
		getchar();
		//1번 메뉴 선택
		if (select==1){
			//1번 메뉴 내용
			printf("\n5개의 카드 정보를 입력하세요.\n");
			for (int i=0;i<5;i++){
				printf("%d번 카드 무늬와 숫자 : ",i+1);
				scanf("%c %s",&mycard[i].shape,mycard[i].num);
		   		getchar();	}
			if (royal_straight_flush(mycard))
				printf("\n결과 : 로얄 스트레이트 플러쉬(로티플)\n");
			else if (back_straight_flush(mycard))
				printf("\n결과 : 백 스트레이트 플러쉬\n");
			else if (straight_flush(mycard))
				printf("\n결과 : 스트레이트 플러쉬(스티플)\n");
			else if (four_card(mycard))
				printf("\n결과 : 포카드(포카)\n");
			else if (full_house(mycard))
				printf("\n결과 : 풀하우스\n");
			else if (flush(mycard))
				printf("\n결과 : 플러쉬\n");
			else if (mountain(mycard))
				printf("\n결과 : 마운틴\n");
			else if (back_straight(mycard))
				printf("\n결과 : 백스트레이트\n");
			else if (straight(mycard))
				printf("\n결과 : 스트레이트\n");
			else if (triple(mycard))
				printf("\n결과 : 트리플\n");
			else if (two_pair(mycard))
				printf("\n결과 : 투 페어\n");
			else if (one_pair(mycard))
				printf("\n결과 : 원 페어\n");
			else
				printf("\n결과 : 노 페어\n");
		}
		//2번 메뉴 선택
		else if (select==2){
			//2번 메뉴 내용
			char shape[4]={'S','D','H','C'};
			char num[13][3]={"2","3","4","5","6","7","8","9","10","J","Q","K","A"};
			int select;
			int cnt=0;
			printf("\n");
			printf("1. royal_straight_flush        2. back_straight_flush\n");
			printf("3. straight_flush              4. four_card\n");
			printf("5. full_house                  6. flush\n");
			printf("7. mountain                    8. back_straight\n");
			printf("9. straight                    10. triple\n");
			printf("11. two_pair                   12. one_pair\n");
			printf("\n\n무슨 족보를 생성할까요? ");
			scanf("%d",&select);
			getchar();
			//랜덤 생성
			while(1){
				for (int i=0; i<5; i++){
					mycard[i].shape=shape[rand()%4];
					strcpy(mycard[i].num,num[rand()%13]);
				}
				cnt++;
				// select 조건문
				if (select==1 && royal_straight_flush(mycard)==true)
					break;
				else if (select==2 && back_straight_flush(mycard)==true)
					break;
				else if (select==3 && straight_flush(mycard)==true)
					break;
				else if (select==4 && four_card(mycard)==true)
					break;
				else if (select==5 && full_house(mycard)==true)
					break;
				else if (select==6 && flush(mycard)==true)
					break;
				else if (select==7 && mountain(mycard)==true)
					break;
				else if (select==8 && back_straight(mycard)==true)
					break;
				else if (select==9 && straight(mycard)==true)
					break;
				else if (select==10 && triple(mycard)==true)
					break;
				else if (select==11 && two_pair(mycard)==true)
					break;
				else if (select==12 && one_pair(mycard)==true)
					break;
				else
					;
			}// 랜덤 루프 종료
			printf("생성된 카드 :");
			for (int i=0;i<5;i++){
				printf(" %c",mycard[i].shape);
				printf(" %s",mycard[i].num);
			}
			printf("\n%d번 족보를 생성하기 위한 카드 생성 시도 : %d번\n",select,cnt);
		}
		else if (select==3)
			break; //전체루프 종료
		printf("===============================================================\n");
		printf("1. 직접 입력          2. 랜덤 생성          3. 종료\n\n");
	}//전체루프 종료
}
_Bool dup(struct card mycard[]){
	for (int i=0;i<5;i++){
		for (int k=0;k<5;k++){
			if (i==k)
				break;
			else if (mycard[i].shape==mycard[k].shape && strcmp(mycard[i].num,mycard[k].num)==0)
				return true;}
	}
	return 0;
}
_Bool royal_straight_flush(struct card mycard[]){
	char shp=mycard[0].shape, num[5][3]={"10","J","Q","K","A"};
	int cmp[5]={0};
	if (!(mycard[1].shape==shp && mycard[2].shape==shp && mycard[3].shape==shp && mycard[4].shape==shp))
		return false;
	for (int i=0;i<5;i++){
		for (int k=0;k<5;k++){
			if (strcmp(num[k],mycard[i].num)==0){
				cmp[k]=1;
				break;}
		}
	}
	int cnt=0;
	for (int i=0;i<5;i++)
		if (cmp[i]==1)
			cnt++;
	if (cnt==5)
		return true;
	else 
		return false;
}
_Bool back_straight_flush(struct card mycard[]){
	char shp=mycard[0].shape, num[5][3]={"A","2","3","4","5"};
	int cmp[5]={0};
	if (!(mycard[1].shape==shp && mycard[2].shape==shp && mycard[3].shape==shp && mycard[4].shape==shp))
		return false;
	for (int i=0;i<5;i++){
		for (int k=0;k<5;k++){
			if (strcmp(num[k],mycard[i].num)==0){
				cmp[k]=1;
				break;}
		}
	}
	int cnt=0;
	for (int i=0;i<5;i++)
		if (cmp[i]==1)
			cnt++;
	if (cnt==5)
		return true;
	else 
		return false;
}
_Bool straight_flush(struct card mycard[]){
	if (royal_straight_flush(mycard))
		return false;
	else if (back_straight_flush(mycard))
		return false;
	char shp=mycard[0].shape, num[13][3]={"A","2","3","4","5","6","7","8","9","10","J","Q","K"};
	int cmp[13]={0};
	if (!(mycard[1].shape==shp && mycard[2].shape==shp && mycard[3].shape==shp && mycard[4].shape==shp))
		return false;
	for (int i=0;i<5;i++){
		for (int k=0;k<13;k++){
			if (strcmp(num[k],mycard[i].num)==0){
				cmp[k]=1;
				break; }
		}
	}
	int cnt=0;
	for (int i=0;i<13;i++){
		if (cmp[i]==1)
			cnt++;
		else if (cnt==5)
			return true;
		else if (cmp[i]==0)
			cnt=0;}
	return false;
}
_Bool four_card(struct card mycard[]){
	int cnt[13]={0};
	char num[13][3]={"A","2","3","4","5","6","7","8","9","10","J","Q","K"};
	if (dup(mycard))
		return false;
	for (int i=0;i<5;i++){
		for (int k=0;k<13;k++){
			if (strcmp(num[k],mycard[i].num)==0){
				cnt[k]++;
				break;}
		}
	}
	for (int i=0;i<13;i++)
		if (cnt[i]==4)
			return true;
	return false;
}	
_Bool full_house(struct card mycard[]){
	if (dup(mycard))
		return false;
	int cnt[13]={0};
	char num[13][3]={"A","2","3","4","5","6","7","8","9","10","J","Q","K"};
	for (int i=0;i<5;i++){
		for (int k=0;k<13;k++){
			if (strcmp(num[k],mycard[i].num)==0){
				cnt[k]++;
				break;}
		}
	}
	for (int i=0;i<13;i++){
		if (cnt[i]==3){
			for (int k=0;k<13;k++){
				if (cnt[k]==2)
					return true;}}}		
	return false;
}
_Bool flush(struct card mycard[]){
	if (dup(mycard))
		return false;
	else if (royal_straight_flush(mycard))
		return false;
	else if (back_straight_flush(mycard))
		return false;
	else if (straight_flush(mycard))
		return false;
	int cnt=0;
	for (int i=1;i<5;i++){
		if (mycard[0].shape==mycard[i].shape)
			cnt++;}
	if (cnt==4)
		return true;
	else
		return false;
}
_Bool mountain(struct card mycard[]){
	char num[5][3]={"10","J","Q","K","A"};
	if (royal_straight_flush(mycard))
		return false;
	int cmp[5]={0};
	for (int i=0;i<5;i++){
		for (int k=0;k<5;k++){
			if (strcmp(num[k],mycard[i].num)==0){
				cmp[k]=1;
				break;}
		}
	}
	int cnt=0;
	for (int i=0;i<5;i++)
		if (cmp[i]==1)
			cnt++;
	if (cnt==5)
		return true;
	else 
		return false;
}
_Bool back_straight(struct card mycard[]){
	if (back_straight_flush(mycard))
		return false;
	char num[5][3]={"A","2","3","4","5"};
	int cmp[5]={0};
	for (int i=0;i<5;i++){
		for (int k=0;k<5;k++){
			if (strcmp(num[k],mycard[i].num)==0){
				cmp[k]=1;
				break;}
		}
	}
	int cnt=0;
	for (int i=0;i<5;i++)
		if (cmp[i]==1)
			cnt++;
	if (cnt==5)
		return true;
	else 
		return false;
}
_Bool straight(struct card mycard[]){
	if (royal_straight_flush(mycard))
		return false;
	else if (back_straight_flush(mycard))
		return false;
	else if (straight_flush(mycard))
		return false;
	char num[13][3]={"A","2","3","4","5","6","7","8","9","10","J","Q","K"};
	int cmp[13]={0};
	for (int i=0;i<5;i++){
		for (int k=0;k<13;k++){
			if (strcmp(num[k],mycard[i].num)==0){
				cmp[k]=1;
				break; }
		}
	}
	int cnt=0;
	for (int i=0;i<13;i++){
		if (cmp[i]==1)
			cnt++;
		else if (cnt==5)
			return true;
		else if (cmp[i]==0)
			cnt=0;}
	return false;
}
_Bool triple(struct card mycard[]){
	if (dup(mycard))
		return false;
	else if (full_house(mycard))
		return false;
	int cnt[13]={0};
	char num[13][3]={"A","2","3","4","5","6","7","8","9","10","J","Q","K"};
	for (int i=0;i<5;i++){
		for (int k=0;k<13;k++){
			if (strcmp(num[k],mycard[i].num)==0){
				cnt[k]++;
				break;}
		}
	}
	for (int i=0;i<13;i++)
		if (cnt[i]==3)
			return true;
	return false;
}
_Bool two_pair(struct card mycard[]){
	if (dup(mycard))
		return false;
	int cnt[13]={0};
	char num[13][3]={"A","2","3","4","5","6","7","8","9","10","J","Q","K"};
	for (int i=0;i<5;i++){
		for (int k=0;k<13;k++){
			if (strcmp(num[k],mycard[i].num)==0){
				cnt[k]++;
				break;}
		}
	}
	for (int i=0;i<13;i++){
		if (cnt[i]==2){
			for (int k=0;k<13;k++){
				if (i!=k && cnt[k]==2)
					return true;}}}
	return false;
}
_Bool one_pair(struct card mycard[]){
	if (dup(mycard))
		return false;
	else if (full_house(mycard))
		return false;
	else if (two_pair(mycard))
		return false;
	int cnt[13]={0};
	char num[13][3]={"A","2","3","4","5","6","7","8","9","10","J","Q","K"};
	for (int i=0;i<5;i++){
		for (int k=0;k<13;k++){
			if (strcmp(num[k],mycard[i].num)==0){
				cnt[k]++;
				break;}
		}
	}
	for (int i=0;i<13;i++)
		if (cnt[i]==2)
			return true;
	return false;
}
