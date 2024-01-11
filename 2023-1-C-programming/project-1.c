/*

30자리 수 덧셈
(공백 무시, 배열 사용 금지)

a + b =c

 */
#include <stdio.h>
int chtoi(char x, int y)   // char to int
{
    if ((int)x>=48 && (int)x<=57)
        y=(int)x-48;
    else
        y=0;
    return y;
}
int main(void)
{
	char a1, a2, a3, a4, a5, a6, a7, a8, a9, a10;
	char a11, a12, a13, a14, a15, a16, a17, a18, a19, a20;
	char a21, a22, a23, a24, a25, a26, a27, a28, a29, a30;
	char x;
	char op;
	char b1, b2, b3, b4, b5, b6, b7, b8, b9, b10;
	char b11, b12, b13, b14, b15, b16, b17, b18, b19, b20;
	char b21, b22, b23, b24, b25, b26, b27, b28, b29, b30;
	char keep;
	char input;

	int ai1, ai2, ai3, ai4, ai5, ai6, ai7, ai8, ai9, ai10;
	int ai11, ai12, ai13, ai14, ai15, ai16, ai17, ai18, ai19, ai20;
	int ai21, ai22, ai23, ai24, ai25, ai26, ai27, ai28, ai29, ai30;

	int bi1, bi2, bi3, bi4, bi5, bi6, bi7, bi8, bi9, bi10;
	int bi11, bi12, bi13, bi14, bi15, bi16, bi17, bi18, bi19, bi20;
	int bi21, bi22, bi23, bi24, bi25, bi26, bi27, bi28, bi29, bi30;

	int c1, c2, c3, c4, c5, c6, c7, c8, c9, c10;
	int c11, c12, c13, c14, c15, c16, c17, c18, c19, c20;
	int c21, c22, c23, c24, c25, c26, c27, c28, c29, c30;
	int cr=0;  //carry
	int y=0;
	int w=1;
	int rp1=0, rp2=0;

	while (w)
	{
		//변수 초기화
		a1='0', a2='0', a3='0', a4='0', a5='0', a6='0', a7='0', a8='0', a9='0', a10='0';
		a11='0', a12='0', a13='0', a14='0', a15='0', a16='0', a17='0', a18='0', a19='0', a20='0';
		a21='0', a22='0', a23='0', a24='0', a25='0', a26='0', a27='0', a28='0', a29='0', a30='0';
		b1='0', b2='0', b3='0', b4='0', b5='0', b6='0', b7='0', b8='0', b9='0', b10='0';
		b11='0', b12='0', b13='0', b14='0', b15='0', b16='0', b17='0', b18='0', b19='0', b20='0';
		b21='0', b22='0', b23='0', b24='0', b25='0', b26='0', b27='0', b28='0', b29='0', b30='0';
		ai1=0, ai2=0, ai3=0, ai4=0, ai5=0, ai6=0, ai7=0, ai8=0, ai9=0, ai10=0;
		ai11=0, ai12=0, ai13=0, ai14=0, ai15=0, ai16=0, ai17=0, ai18=0, ai19=0, ai20=0;
		ai21=0, ai22=0, ai23=0, ai24=0, ai25=0, ai26=0, ai27=0, ai28=0, ai29=0, ai30=0;
		bi1=0, bi2=0, bi3=0, bi4=0, bi5=0, bi6=0, bi7=0, bi8=0, bi9=0, bi10=0;
		bi11=0, bi12=0, bi13=0, bi14=0, bi15=0, bi16=0, bi17=0, bi18=0, bi19=0, bi20=0;
		bi21=0, bi22=0, bi23=0, bi24=0, bi25=0, bi26=0, bi27=0, bi28=0, bi29=0, bi30=0;
		c1=0, c2=0, c3=0, c4=0, c5=0, c6=0, c7=0, c8=0, c9=0, c10=0;
		c11=0, c12=0, c13=0, c14=0, c15=0, c16=0, c17=0, c18=0, c19=0, c20=0;
		c21=0, c22=0, c23=0, c24=0, c25=0, c26=0, c27=0, c28=0, c29=0, c30=0;
	
		rp1=0, rp2=0;	
		// 첫 번째 정수, 연산자 입력
		printf("수식 : ");
		while (1)
		{
			x=getchar();

			if (x==' ')
				;
			else if (x>='0' && x<='9')
			{
				a1=a2;
				a2=a3;
				a3=a4;
				a4=a5;
				a5=a6;
				a6=a7;
				a7=a8;
				a8=a9;
				a9=a10;
				a10=a11;
				a11=a12;
				a12=a13;
				a13=a14;
				a14=a15;
				a15=a16;
				a16=a17;
				a17=a18;
				a18=a19;
				a19=a20;
				a20=a21;
				a21=a22;
				a22=a23;
				a23=a24;
				a24=a25;
				a25=a26;
				a26=a27;
				a27=a28;
				a28=a29;
				a29=a30;
				a30=x;
				rp1++;
			}
			else 
			{
				op=x;
				break;
			}	
		}
		// 두 번째 정수 입력
		while (1)
		{
			x=getchar();
			if (x==' ')
				;
			else if (x>='0' && x<='9')
			{
				b1=b2;
				b2=b3;
				b3=b4;
				b4=b5;
				b5=b6;
				b6=b7;
				b7=b8;
				b8=b9;
				b9=b10;
				b10=b11;
				b11=b12;
				b12=b13;
				b13=b14;
				b14=b15;
				b15=b16;
				b16=b17;
				b17=b18;
				b18=b19;
				b19=b20;
				b20=b21;
				b21=b22;
				b22=b23;
				b23=b24;
				b24=b25;
				b25=b26;
				b26=b27;
				b27=b28;
				b28=b29;
				b29=b30;
				b30=x;
				rp2++;
			}
			else if (x=='\n')
				break;
			else
				break;
		}

		//문자 -> 정수
		ai1=chtoi(a1,ai1);
    	ai2=chtoi(a2,ai2);
    	ai3=chtoi(a3,ai3);
    	ai4=chtoi(a4,ai4);
    	ai5=chtoi(a5,ai5);
		ai6=chtoi(a6,ai6);
    	ai7=chtoi(a7,ai7);
    	ai8=chtoi(a8,ai8);
    	ai9=chtoi(a9,ai9);
    	ai10=chtoi(a10,ai10);
		ai11=chtoi(a11,ai11);
		ai12=chtoi(a12,ai12);
		ai13=chtoi(a13,ai13);
		ai14=chtoi(a14,ai14);
    	ai15=chtoi(a15,ai15);
    	ai16=chtoi(a16,ai16);
    	ai17=chtoi(a17,ai17);
    	ai18=chtoi(a18,ai18);
    	ai19=chtoi(a19,ai19);
    	ai20=chtoi(a20,ai20);
    	ai21=chtoi(a21,ai21);
    	ai22=chtoi(a22,ai22);
    	ai23=chtoi(a23,ai23);
    	ai24=chtoi(a24,ai24);
    	ai25=chtoi(a25,ai25);
    	ai26=chtoi(a26,ai26);
    	ai27=chtoi(a27,ai27);
    	ai28=chtoi(a28,ai28);
    	ai29=chtoi(a29,ai29);
    	ai30=chtoi(a30,ai30);

		bi1=chtoi(b1,bi1);
    	bi2=chtoi(b2,bi2);
    	bi3=chtoi(b3,bi3);
    	bi4=chtoi(b4,bi4);
    	bi5=chtoi(b5,bi5);
		bi6=chtoi(b6,bi6);
    	bi7=chtoi(b7,bi7);
    	bi8=chtoi(b8,bi8);
    	bi9=chtoi(b9,bi9);
    	bi10=chtoi(b10,bi10);
		bi11=chtoi(b11,bi11);
		bi12=chtoi(b12,bi12);
		bi13=chtoi(b13,bi13);
		bi14=chtoi(b14,bi14);
    	bi15=chtoi(b15,bi15);
    	bi16=chtoi(b16,bi16);
    	bi17=chtoi(b17,bi17);
    	bi18=chtoi(b18,bi18);
    	bi19=chtoi(b19,bi19);
    	bi20=chtoi(b20,bi20);
    	bi21=chtoi(b21,bi21);
    	bi22=chtoi(b22,bi22);
    	bi23=chtoi(b23,bi23);
    	bi24=chtoi(b24,bi24);
    	bi25=chtoi(b25,bi25);
    	bi26=chtoi(b26,bi26);
    	bi27=chtoi(b27,bi27);
    	bi28=chtoi(b28,bi28);
    	bi29=chtoi(b29,bi29);
    	bi30=chtoi(b30,bi30);
	
		//연산
		y=ai30+bi30+cr;
		c30=y%10;
		cr=y/10;
	
		y=ai29+bi29+cr;
		c29=y%10;
		cr=y/10;
		
		y=ai28+bi28+cr;
		c28=y%10;
		cr=y/10;
	
		y=ai27+bi27+cr;
		c27=y%10;
		cr=y/10;
		
		y=ai26+bi26+cr;
		c26=y%10;
		cr=y/10;
	
		y=ai25+bi25+cr;
		c25=y%10;
		cr=y/10;
	
		y=ai24+bi24+cr;
		c24=y%10;
		cr=y/10;
		
		y=ai23+bi23+cr;
		c23=y%10;
		cr=y/10;
	
		y=ai22+bi22+cr;
		c22=y%10;
		cr=y/10;
		
		y=ai21+bi21+cr;
		c21=y%10;
		cr=y/10;
		
		y=ai20+bi20+cr;
		c20=y%10;
		cr=y/10;
	
		y=ai19+bi19+cr;
		c19=y%10;
		cr=y/10;
		
		y=ai18+bi18+cr;
		c18=y%10;
		cr=y/10;
	
		y=ai17+bi17+cr;
		c17=y%10;
		cr=y/10;
		
		y=ai16+bi16+cr;
		c16=y%10;
		cr=y/10;
	
		y=ai15+bi15+cr;
		c15=y%10;
		cr=y/10;
	
		y=ai14+bi14+cr;
		c14=y%10;
		cr=y/10;
		
		y=ai13+bi13+cr;
		c13=y%10;
		cr=y/10;
	
		y=ai12+bi12+cr;
		c12=y%10;
		cr=y/10;
		
		y=ai11+bi11+cr;
		c11=y%10;
		cr=y/10;
	
		y=ai10+bi10+cr;
		c10=y%10;
		cr=y/10;
	
		y=ai9+bi9+cr;
		c9=y%10;
		cr=y/10;
		
		y=ai8+bi8+cr;
		c8=y%10;
		cr=y/10;
	
		y=ai7+bi7+cr;
		c7=y%10;
		cr=y/10;
		
		y=ai6+bi6+cr;
		c6=y%10;
		cr=y/10;
	
		y=ai5+bi5+cr;
		c5=y%10;
		cr=y/10;
	
		y=ai4+bi4+cr;
		c4=y%10;
		cr=y/10;
		
		y=ai3+bi3+cr;
		c3=y%10;
		cr=y/10;
	
		y=ai2+bi2+cr;
		c2=y%10;
		cr=y/10;
		
		y=ai1+bi1+cr;
		c1=y%10;
		cr=y/10;
		
		

		//출력
		if (cr==1)
			printf("결과 : 오버플로우가 발생했습니다.\n");
		else if (rp1>=31 || rp2>=31)
			printf("결과 : 오버플로우가 발생했습니다.\n");
		else if	(op=='+')
		{
			printf("결과 : ");
			printf("%d%d%d,",c1,c2,c3);
			printf("%d%d%d,",c4,c5,c6);
			printf("%d%d%d,",c7,c8,c9);
			printf("%d%d%d,",c10,c11,c12);
			printf("%d%d%d,",c13,c14,c15);
			printf("%d%d%d,",c16,c17,c18);
			printf("%d%d%d,",c19,c20,c21);
			printf("%d%d%d,",c22,c23,c24);
			printf("%d%d%d,",c25,c26,c27);
			printf("%d%d%d\n",c28,c29,c30);
		}	
		else 
			printf("결과 : 잘못된 연산자입니다.\n");
		do
		{
			printf("계속 하시겠습니까? ");
			scanf("%c",&keep);
			input=getchar();
			if (input!='\n')
			{
				do
					input=getchar();
				while (input!='\n');
				keep='a';
			}
			else (input=='\n')
				;
		}
		while (keep!='y' && keep!='n');
		
		if (keep=='y')
			w=1;
		else if (keep=='n')
			w=0;

	}
	return 0;
}
