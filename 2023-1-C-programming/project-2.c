#include <stdio.h>
#include <string.h>
char menu(void);
void sort_ascName(char Name[][10], int ID[], int Score[]);
void sort_ascID(char Name[][10], int ID[], int Score[]); 
void sort_descScore(char Name[][10], int ID[], int Score[]);
void search_Name(char Name[][10], int ID[], int Score[]); 

#define SIZE 20

int main(void)
{
	char request;

	char inputName[20][10]={"Sophia", "Olivia", "Riley", "Emma", "Ava", "Isabella", "Aria", "Amelia", "Mia", "Liam", "Noah", "Jackson", "Aiden", "Elijah", "Grayson", "Lucas", "Oliver", "Caden", "Mateo", "David"};
	int inputID[20]={20220001, 20220010, 20220002, 20220015, 20220009, 20220014, 20220020, 20220005, 20220016, 20220008, 20220012, 20220004, 20220018, 20220017, 20220003, 20220013, 20220007, 20220019, 20220011, 20220006};
	int inputScore[20]={98,96,88,77,82,93,84,79,90,80,89,99,78,83,92,71,72,68,95,76};

	while (1)
	{
		request=menu();
		
		if (request=='1')
			sort_ascName(inputName,inputID,inputScore);
		else if (request=='2')
			sort_ascID(inputName,inputID,inputScore);
		else if (request=='3')
			sort_descScore(inputName,inputID,inputScore);
		else if (request=='4')
			search_Name(inputName,inputID,inputScore);
		else if (request=='5')
			break;
	}

	return 0;
}
void sort_ascName(char Name[][10], int ID[], int Score[])
{
	char tempChar[10];
	int tempInt;

	for (int i=1; i<SIZE; i++)
	{
		for (int j=0; j<SIZE-i; j++)
		{
			if (strcmp(Name[j],Name[j+1])>0)
			{
				strcpy(tempChar, Name[j]);
				strcpy(Name[j], Name[j+1]);
				strcpy(Name[j+1], tempChar);

				tempInt=ID[j];
				ID[j]=ID[j+1];
				ID[j+1]=tempInt;

				tempInt=Score[j];
				Score[j]=Score[j+1];
				Score[j+1]=tempInt;
			}
		}
	}
	printf("------------------------------------------\n");
	printf("%-15s %-15s %-15s\n","이름","학번","점수");
	for (int i=0; i<SIZE; i++)
		printf("%-15s %-15d %-15d\n", Name[i], ID[i], Score[i]);
	printf("------------------------------------------\n");

	return;
}
				
void sort_ascID(char Name[][10], int ID[], int Score[])
{
	char tempChar[10];
    int tempInt;

    for (int i=1; i<SIZE; i++)
    {
        for (int j=0; j<SIZE-i; j++)
        {
            if (ID[j]>ID[j+1])
            {
                strcpy(tempChar, Name[j]);
                strcpy(Name[j], Name[j+1]);
                strcpy(Name[j+1], tempChar);

                tempInt=ID[j];
                ID[j]=ID[j+1];
                ID[j+1]=tempInt;

                tempInt=Score[j];
                Score[j]=Score[j+1];
                Score[j+1]=tempInt;
            }
        }
    }
	printf("------------------------------------------\n");
    printf("%-15s %-15s %-15s\n","이름","학번","점수");
    for (int i=0; i<SIZE; i++)
        printf("%-15s %-15d %-15d\n", Name[i], ID[i], Score[i]);
	printf("------------------------------------------\n");

    return;
}
void sort_descScore(char Name[][10], int ID[], int Score[])
{
	char tempChar[10];
    int tempInt;

    for (int i=1; i<SIZE; i++)
    {
        for (int j=0; j<SIZE-i; j++)
        {
            if (Score[j]<Score[j+1])
            {
                strcpy(tempChar, Name[j]);
                strcpy(Name[j], Name[j+1]);
                strcpy(Name[j+1], tempChar);

                tempInt=ID[j];
                ID[j]=ID[j+1];
                ID[j+1]=tempInt;

                tempInt=Score[j];
                Score[j]=Score[j+1];
                Score[j+1]=tempInt;
            }
        }
    }
	printf("------------------------------------------\n");
    printf("%-15s %-15s %-15s\n","이름","학번","점수");
    for (int i=0; i<SIZE; i++)
        printf("%-15s %-15d %-15d\n", Name[i], ID[i], Score[i]);
	printf("------------------------------------------\n");

    return;
}
void search_Name(char Name[][10], int ID[], int Score[])
{
	char SearchName[10];
	int i;
	while (1)
	{	
		printf("이름을 입력하세요: ");
		scanf("%s", SearchName);
		getchar();
		for (i=0; i<SIZE; i++)
		{
			if (strcmp(Name[i],SearchName)==0)
			{
				printf("------------------------------------------\n");
				printf("%-15s %-15s %-15s\n","이름","학번","점수");
    			printf("%-15s %-15d %-15d\n",Name[i], ID[i], Score[i]);
				printf("------------------------------------------\n");
				break;
			}
		}
		if (i!=SIZE)
			break;
			
	}
	return;
}
char menu(void)
{
	char input_num;
	char input_ent;

	printf("\nMENU\n");
	printf("------------------------------------------\n");
	printf("1. 이름 오름차순 출력\n"
			"2. 학번 오름차순 출력\n"
			"3. 점수 내림차순 출력\n"
			"4. 이름 검색\n"
			"5. 종료\n");
	printf("------------------------------------------\n");
	while (1)
	{
		printf("번호를 선택하세요: ");
		input_num=getchar();
		input_ent=getchar();
		if ((input_num=='1' || input_num=='2' || input_num=='3' || input_num=='4' || input_num=='5') && (input_ent=='\n'))
			break;
		else
			while (input_ent!='\n')
				input_ent=getchar();
	}

	return input_num;
}
