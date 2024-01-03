#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NAME 101
#define FALSE 0
#define TRUE 1

const int years[5]={2017,2018,2019,2020,2021};

typedef struct membersInfomation{
    char* firstName;
    char* lastName;
    int memberNumber;
    int yearJoined;
    int feesPaid[5];
    int note; //in case the year joined is later than 2017
}structMI;

void clearBuffer(void){ //Tool_1
    while(getc(stdin)!='\n');
}
void testMemory(void* testP){ //Tool_2
    if(NULL==testP){
        printf("\n\n***** OUT OF MEMORY *****\n\n\n");
        exit(1);
    }
}

int addMember(structMI*); //F_1
void removeMember(int,structMI**,int,structMI**); //F_2
void updateMember(structMI*); //F_3
void printMember(structMI*); //F_4
void printRegister(int,structMI**); //F_5
int searchMember(int,int,int,int*,structMI**); //F_6
void end(int*,int,structMI**,int,structMI**); //F_7

void mainMenu(int* selectionP){ //F_menu
    *selectionP=0;
    printf(
    "1  Add a new member\n"
    "2  Remove a member\n"
    "3  Update member\n"
    "4  Print member\n"
    "5  Print register\n"
    "6  Search\n"
    "7  End\n\n"
    "Select > ");
    scanf("%d",selectionP);
        clearBuffer();
    printf("\n");
}

int main(void){
    int i;
    int aNumber;
    int chosenOne;
    int selection;
    int searchSelection;
    int searchResult;
    int* numberArray=(int*)calloc(1,sizeof(int));//free
        testMemory(numberArray);
    structMI** mainP=(structMI**)malloc(3*sizeof(structMI*));//free
        testMemory(mainP);
    structMI** binP=(structMI**)malloc(1*sizeof(structMI*));//free
        testMemory(binP);
    int bin=0;
    int n=0;
    int freeSlots=3;

    while(1){
        mainMenu(&selection);
        switch(selection){
            case 1:
                if(0==freeSlots){
                    printf("*** REGISTER IS FULL, ALLOCATING MORE MEMORY ***\n\n");
                    freeSlots=3;
                    mainP=(structMI**)realloc(mainP,(n+3)*sizeof(structMI*));
                        testMemory(mainP);
                }
                *(mainP+n)=(structMI*)calloc(1,sizeof(structMI));//free
                    testMemory(*(mainP+n));
                if(TRUE==addMember(*(mainP+n))){
                    ++n;
                    printf("Free slots %d\n\n",--freeSlots);
                }
                break;
            case 2:
                printf("Give member number to remove > ");
                scanf("%d",&aNumber);
                    clearBuffer();
                printf("\n");
                numberArray=(int*)realloc(numberArray,(n+1)*sizeof(int));
                    testMemory(numberArray);
                memset(numberArray,0,(n+1)*sizeof(int));
                searchResult=searchMember(3,aNumber,n,numberArray,mainP);
                chosenOne=-1;
                if(0==searchResult)
                    printf("Not found, cannot remove data!\n\n");
                else{
                    if(1<searchResult){
                        for(i=0;i<searchResult;i++){
                            printf("#%d:\n",i+1);
                            printMember(*(mainP+*(numberArray+i)));
                        }
                        printf("Select > ");
                        scanf("%d",&chosenOne);
                            clearBuffer();
                        printf("\n");
                        if(1<=chosenOne && i>=chosenOne)
                            chosenOne=*(numberArray+chosenOne-1);
                        else
                            printf("*** INVALID SELECTION ***\n\n");
                    }
                    else if(1==searchResult)
                        chosenOne=*numberArray;
                    if(-1!=chosenOne)
                        removeMember(bin,binP,chosenOne,mainP);
                }
                break;
            case 3:
                printf("Give member number to update > ");
                scanf("%d",&aNumber);
                    clearBuffer();
                printf("\n");
                numberArray=(int*)realloc(numberArray,(n+1)*sizeof(int));
                    testMemory(numberArray);
                memset(numberArray,0,(n+1)*sizeof(int));
                searchResult=searchMember(3,aNumber,n,numberArray,mainP);
                chosenOne=-1;
                if(0==searchResult)
                    printf("Not found, cannot update data!\n\n");
                else{
                    if(1<searchResult){
                        for(i=0;i<searchResult;i++){
                            printf("#%d:\n",i+1);
                            printMember(*(mainP+*(numberArray+i)));
                        }
                        printf("Select > ");
                        scanf("%d",&chosenOne);
                            clearBuffer();
                        printf("\n");
                        if(1<=chosenOne && i>=chosenOne)
                            chosenOne=*(numberArray+chosenOne-1);
                        else
                            printf("*** INVALID SELECTION ***\n\n");
                    }
                    else if(1==searchResult)
                        chosenOne=*numberArray;
                    if(-1!=chosenOne)
                        updateMember(*(mainP+chosenOne));
                }
                break;
            case 4:
                printf("Give member number to print > ");
                scanf("%d",&aNumber);
                    clearBuffer();
                printf("\n");
                numberArray=(int*)realloc(numberArray,(n+1)*sizeof(int));
                    testMemory(numberArray);
                memset(numberArray,0,(n+1)*sizeof(int));
                searchResult=searchMember(3,aNumber,n,numberArray,mainP);
                printf("***************************\n\n");
                if(0==searchResult)
                    printf("Not found, cannot print data!\n\n");
                else{
                    for(i=0;i<searchResult;i++)
                        printMember(*(mainP+*(numberArray+i)));
                }
                printf("***************************\n\n");
                break;
            case 5:
                printRegister(n,mainP);
                break;
            case 6:
                searchSelection=0;
                printf(
                "1 Search by first name\n"
                "2 Search by last name\n"
                "3 Search by member number\n"
                "4 Search by year joined\n"
                "5 Search by unpaid fees\n\n"
                "Select > ");
                scanf("%d",&searchSelection);
                    clearBuffer();
                printf("\n");
                if(3==searchSelection){
                    printf("Give the member number > ");
                    scanf("%d",&aNumber);
                        clearBuffer();
                    printf("\n");
                }
                numberArray=(int*)realloc(numberArray,(n+1)*sizeof(int));
                    testMemory(numberArray);
                memset(numberArray,0,(n+1)*sizeof(int));
                searchResult=searchMember(searchSelection,aNumber,n,numberArray,mainP);
                if(0==searchResult)
                    printf("Not found!\n\n");
                else{
                    for(i=0;i<searchResult;i++)
                        printMember(*(mainP+*(numberArray+i)));
                }
                break;
            case 7:
                end(numberArray,bin,binP,n,mainP);
                break;
            default:
                printf("*** INVALID SELECTION ***\n\n");
                break;
        }
    }
    return 0;
}

int addMember(structMI* addP){ //F_1
    int result=FALSE;
    char name[NAME]={0};
    char* spaceP;
    int i;

    printf("Give the first and last name > ");
    fgets(name,NAME,stdin);
    if(name[strlen(name)-1]=='\n')
        name[strlen(name)-1]=0;
    else
        clearBuffer();

    spaceP=strchr(name,' ');
    if(NULL==spaceP){
        printf("\nPlease give a space!\n\n");
        result=FALSE;
    }
    else{
        char tempC=*spaceP;
        *spaceP=0; //*spaceP='\0';
        addP->firstName=(char*)calloc(strlen(name)+1,sizeof(char));//free
            testMemory(addP->firstName);
        strcpy(addP->firstName,name);
        *spaceP=tempC;
        addP->lastName=(char*)calloc(strlen(spaceP)+1,sizeof(char));//free
            testMemory(addP->lastName);
        strcpy(addP->lastName,spaceP+1);

        printf("Give member number > ");
        scanf("%d",&addP->memberNumber);
            clearBuffer();
        printf("Give year joined > ");
        scanf("%d",&addP->yearJoined);
            clearBuffer();

        if(years[0]<addP->yearJoined)
            addP->note=addP->yearJoined-years[0];
        else
            addP->note=0;
        for(i=0;i<addP->note;i++)
            addP->feesPaid[i]=0;
        for(i=addP->note;i<5;i++){
            printf("Give fee paid for year %d > ",years[i]);
            scanf("%d",&addP->feesPaid[i]);
                clearBuffer();
        }
        printf("\n");
        result=TRUE;
    }
    return result;
}
void removeMember(int bin,structMI** binP,int chosenOne,structMI** mainP){ //F_2
    binP=(structMI**)realloc(binP,(bin+1)*sizeof(structMI*));
        testMemory(binP);
    *(binP+bin)=*(mainP+chosenOne);
    ++bin;
    *(mainP+chosenOne)=NULL;
    printf("Removed successfully!\n\n");
}
void updateMember(structMI* updateP){ //F_3
    int updateSelection=0;
    printf(
    "1 Change first name\n"
    "2 Change last name\n"
    "3 Change member number\n"
    "4 Change year joined\n"
    "5 Change member fees paid\n\n"
    "Select > ");
    scanf("%d",&updateSelection);
        clearBuffer();
    printf("\n");

    int i;
    int yearSelection;
    char name[NAME]={0};
    switch(updateSelection){
        case 1:
            printf("Give new first name > ");
            fgets(name,NAME,stdin);
            printf("\n");
            if(name[strlen(name)-1]=='\n')
                name[strlen(name)-1]=0;
            else
                clearBuffer();
            strcpy(updateP->firstName,name);
            printf("Updated successfully!\n\n");
            break;
        case 2:
            printf("Give new last name > ");
            fgets(name,NAME,stdin);
            printf("\n");
            if(name[strlen(name)-1]=='\n')
                name[strlen(name)-1]=0;
            else
                clearBuffer();
            strcpy(updateP->lastName,name);
            printf("Updated successfully!\n\n");
            break;
        case 3:
            printf("Give new member number > ");
            scanf("%d",&updateP->memberNumber);
                clearBuffer();
            printf("\n");
            printf("Updated successfully!\n\n");
            break;
        case 4:
            printf("Give new year joined > ");
            scanf("%d",&updateP->yearJoined);
                clearBuffer();
            printf("\n");
            if(years[0]<updateP->yearJoined)
                updateP->note=updateP->yearJoined-years[0];
            else
                updateP->note=0;
            printf("Updated successfully!\n\n");
            break;
        case 5:
            for(i=0;i<5;i++){
                printf("#%d:\n",i+1);
                printf("Year:     %d\n",years[i]);
                printf("Fee paid: %d\n\n",updateP->feesPaid[i]);
            }
            printf("Select > ");
            scanf("%d",&yearSelection);
                clearBuffer();
            printf("\n");
            switch(yearSelection){
                case 1 ...5:
                    --yearSelection;
                    printf("Give new fee paid for year %d > ",years[yearSelection]);
                    scanf("%d",&updateP->feesPaid[yearSelection]);
                        clearBuffer();
                    printf("\n");
                    printf("Updated successfully!\n\n");
                    break;
                default:
                    printf("*** INVALID SELECTION ***\n\n");
                    break;
            }
            break;
        default:
            printf("*** INVALID SELECTION ***\n\n");
            break;
    }
}
void printMember(structMI* printP){ //F_4
    printf("First name: %s\n",printP->firstName);
    printf("Last name:  %s\n",printP->lastName);
    printf("Member num: %d\n",printP->memberNumber);
    printf("Joined:     %d\n\n",printP->yearJoined);
}
void printRegister(int n,structMI** mainP){ //F_5
    printf("***************************\n\n");
    int i;
    for(i=0;i<n;i++)
        if(NULL!=*(mainP+i))
            printMember(*(mainP+i));
    printf("***************************\n\n");
}
int searchMember(int searchSelection,int aNumber,int n,int* numberArray,structMI** mainP){ //F_6
    int i,j;
    int result=0;
    char name[NAME]={0};
    switch(searchSelection){
        case 1:
            printf("Give the first name > ");
            fgets(name,NAME,stdin);
            printf("\n");
            if(name[strlen(name)-1]=='\n')
                name[strlen(name)-1]=0;
            else
                clearBuffer();
            for(i=0;i<n;i++){
                if(NULL!=*(mainP+i))
                    if(0==strcmp(name,(*(mainP+i))->firstName)){
                        *(numberArray+result)=i;
                        ++result;
                    }
            }
            break;
        case 2:
            printf("Give the last name > ");
            fgets(name,NAME,stdin);
            printf("\n");
            if(name[strlen(name)-1]=='\n')
                name[strlen(name)-1]=0;
            else
                clearBuffer();
            for(i=0;i<n;i++){
                if(NULL!=*(mainP+i))
                    if(0==strcmp(name,(*(mainP+i))->lastName)){
                        *(numberArray+result)=i;
                        ++result;
                    }
            }
            break;
        case 3:
            for(i=0;i<n;i++){
                if(NULL!=*(mainP+i))
                    if(aNumber==(*(mainP+i))->memberNumber){
                        *(numberArray+result)=i;
                        ++result;
                    }
            }
            break;
        case 4:
            printf("Give the year joined > ");
            scanf("%d",&aNumber);
                clearBuffer();
            printf("\n");
            for(i=0;i<n;i++){
                if(NULL!=*(mainP+i))
                    if(aNumber==(*(mainP+i))->yearJoined){
                        *(numberArray+result)=i;
                        ++result;
                    }
            }
            break;
        case 5:
            for(i=0;i<n;i++)
                if(NULL!=*(mainP+i))
                    for(j=(*(mainP+i))->note;j<5;j++)
                        if(0==(*(mainP+i))->feesPaid[j]){
                            *(numberArray+result)=i;
                            ++result;
                            break;
                        }
            break;
        default:
            printf("*** INVALID SELECTION ***\n\n");
            result=-1;
            break;
    }
    return result;
}
void end(int* numberArray,int bin,structMI** binP,int n,structMI** mainP){ //F_7
    printf("*** ENDING PROGRAM ***\n\n\n");
    int i;
    for(i=0;i<bin;i++){
        free((*(binP+i))->firstName);
        free((*(binP+i))->lastName);
        free(*(binP+i));
    }
    free(binP);
    for(i=0;i<n;i++){
        if(NULL!=*(mainP+i)){
            free((*(mainP+i))->firstName);
            free((*(mainP+i))->lastName);
        }
        free(*(mainP+i));
    }
    free(mainP);
    free(numberArray);
    exit(0);
}
