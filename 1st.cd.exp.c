#include<stdio.h>
#include<conio.h>
#include<ctype.h>
#include<string.h>

void main(){
  FILE *fi, *fo, *fop, *fk;
  int flag=0, i=1;
  char c,a[15],ch[15],file[20];
  char name[20];
  char rollno[15];
  printf("Enter name: ");
  scanf("%s",name);
  printf("Enter rollno: ");
  scanf("%s",rollno);
  printf("\n Enter the FileName: ");
  scanf("%s",&file);
  fi=fopen(file,"r");
  fo=fopen("lexemes.c","w");
  fop=fopen("o.c","r");
  fk=fopen("k.c","r");
  c=getc(fi);
  while(!feof(fi)){
       if(isalpha(c)||isdigit(c)||(c=='['||c==']'||c=='.'==1))
                       fputc(c,fo);
       else{
              if(c=='\n')
                      fprintf(fo,"\t$\t");
              else
                      fprintf(fo,"\t%c\t",c);
       }
       c=getc(fi);
   }
   fclose(fi);
   fclose(fo);
   fi=fopen("lexemes.c","r");
   printf("\nName of the student: %s",name);
   printf("\nRollNo of the student: %s",rollno);
   printf("\nLexical Analysis");
   fscanf(fi,"%s",a);
   printf("\nLine:%d\n",i++);
   while(!feof(fi)){
             if(strcmp(a,"$")==0){
                   printf("\nLine:%d\n",i++);
                   fscanf(fi,"%s",a);
             }
             fscanf(fop,"%s",ch);
             while(!feof(fop)){
                 if(strcmp(ch,a)==0){
                       fscanf(fop,"%s",ch);
                       printf("\t\t%s\t:\t%s\n",a,ch);
                       flag=1;
                 }
                 fscanf(fop,"%s",ch);
             }
             rewind(fop);
             fscanf(fk,"%s",ch);
             while(!feof(fk)){
                     if(strcmp(ch,a)==0){
                              fscanf(fk,"%k",ch);
                              printf("\t\t%s\t:\tKeywords\n",a); //
                              flag=1;
                     }
                     fscanf(fk,"%s",ch);
             }
             rewind(fk);
             if(flag==0){
                        if(isdigit(a[0]))
                            printf("\t\t%s\t:\tConstant\n",a);
                        else
                             printf("\t\t%s\t:\tidentifier\n",a);
             }
             flag=0;
             fscanf(fi,"%s",a);
    }
getch();
}
 