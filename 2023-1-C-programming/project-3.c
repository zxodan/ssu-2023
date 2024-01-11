#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int rand_func(void);
int match_func(char, char);
int main(void)
{
	char choice, com;
	char keep='y';
	int match, attack;

	srand(time(NULL));
	while (keep == 'y') // 게임 전체 루프
	{
		printf("\n\n묵(O)찌(X)빠(#) 게임을 시작합니다.\n\n");
		while (1) // 선 정하기
		{
			printf("선을 정하기 위해 먼저 가위 바위 보를 선택하세요 : ");
			scanf("%c",&choice);
			getchar();
			
			com=rand_func();
			printf("당신은 %c를 냈고 컴퓨터는 %c를 냈습니다.\n", choice, com);
			
			match=match_func(choice,com);
			if (match==0)
				printf("당신과 컴퓨터가 비겼습니다.\n\n");
			else if (match == 1)
			{
				printf("당신의 공격 차례입니다.\n\n");
				attack=1;
				break;
			}
			else if (match == 2)
			{
				printf("컴퓨터의 공격 차례입니다.\n\n");
				attack=2;
				break;
			}
		}
		while (1) // 게임
		{
			printf("묵찌빠를 선택하세요 : ");
			scanf("%c",&choice);
			getchar();
			com=rand_func();
			printf("당신은 %c를 냈고 컴퓨터는 %c를 냈습니다.\n", choice, com);

			match=match_func(choice, com);
			if (match==1)
			{
				printf("당신의 공격 차례입니다.\n\n");
				attack=1;
			}
			else if (match==2)
			{
				printf("컴퓨터의 공격 차례입니다.\n\n");
				attack=2;
			}
			else if (match==0)
			{
				if (attack==1)
				{
					printf("당신이 이겼습니다.\n\n");
					break;
				}
				else if (attack==2)
				{
					printf("컴퓨터가 이겼습니다.\n\n");
					break;
				}
			}
		}
		printf("계속 하시겠습니까? ");
		scanf("%c",&keep);
		getchar();
	}

	return 0;
}
int rand_func(void)
{
	int x;
	while (x!='#' && x!='O' && x!='X')
		x=rand()%89;
	return x;
}
int match_func(char you, char com)
{
	int score; // you win s:=1, com win s:=2, 무승부 s:=0
	if (you == com)
		score=0;
	else if (you == '#')
	{
		if (com == 'O')
			score=1;
		else if (com == 'X')
			score=2;
	}
	else if (you == 'O')
	{
		if (com == 'X')
			score=1;
		else if (com == '#')
			score=2;
	}
	else if (you == 'X')
	{
		if (com=='O')
			score=2;
		else if (com=='#')
			score=1;
	}
	return score;
}
