#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <bitset>
#include <string>
using namespace std;

char pfm[5][5];
int order[25] = {24, 23, 22, 21, 20, 15, 10, 5, 0, 1, 2, 3, 4, 9, 14, 19, 18, 17, 16, 11, 6, 7, 8, 13, 12};
string pfck, pt, ptm, knr = "" ;
int rfck, lv, i, j ;
bitset<26> b ;

void print()
{
    for(int i = 0; i < 5; i++)
    {
        for(int j = 0; j < 5; j++)
            cout << pfm[i][j] << " " ;
        cout << "\n" ;
    }
}

void ChangeMatrix()
{
    string str = "", str2 = "" ;
    for(int i = 0; i < 25; i++)
        str += pfm[i/5][i%5];
    char rf[rfck][25];
    int c = 0 ;
    bool flag = false ;
    for(int i = 0; i < rfck; i++)
    {
        for(int j = 0; j < 25; j++)
            rf[i][j] = '*' ;
    }
    if(rfck > 1)
    {
        int r = 0, c = 0 ;
        for(int i = 0; i < 25; i++)
        {
            if(r == 0 || r == rfck-1)
                flag = !flag ;
            rf[r][c++] = str[i];
            if(flag)
                r++ ;
            else
                r-- ;
        }
    }
    else
    {
        for(int i = 0; i < 25; i++)
            rf[0][i] = str[i];
    }
    for(int i = 0; i < rfck; i++)
    {
        for(int j = 0; j < 25; j++)
        {
            if(rf[i][j] != '*')
                str2 += rf[i][j];
        }
    }
    for(int i = 0; i < 25; i++)
        pfm[order[i]/5][order[i]%5] = str2[i];
}

void encrypt(char c1, char c2)
{
    int i1 = 0, i2 = 0, j1 = 0, j2 = 0 ;
    for(int i = 0; i < 5; i++)
    {
        for(int j = 0; j < 5; j++)
        {
            if(pfm[i][j] == c1)
            {
                i1 = i ;
                j1 = j ;
                break ;
            }
        }
    }
    for(int i = 0; i < 5; i++)
    {
        for(int j = 0; j < 5; j++)
        {
            if(pfm[i][j] == c2)
            {
                i2 = i ;
                j2 = j ;
                break ;
            }
        }
    }
    if(i1 == i2)
        cout << pfm[i1][(j1+1)%5] << pfm[i2][(j2+1)%5];
    else if(j1 == j2)
        cout << pfm[(i1+1)%5][j1] << pfm[(i2+1)%5][j2];
    else
        cout << pfm[i1][j2] << pfm[i2][j1];
}

int main() {
    cin >> rfck >> pfck >> lv >> pt ;
    transform(pfck.begin(), pfck.end(), pfck.begin(), ::toupper);
    transform(pt.begin(), pt.end(), pt.begin(), ::toupper);
    b.reset();
    for(i = 0; i < pfck.length(); i++)
    {
        if(!b[pfck[i]-'A'])
        {
            knr += pfck[i];
            b.set(pfck[i]-'A');
        }
    }
    for(i = 0; i < knr.length(); i++)
        pfm[order[i]/5][order[i]%5] = knr[i];
    if(b['J'-'A'])
    {
        replace(pt.begin(), pt.end(), 'I', 'J');
        for(; i < 25; i++)
        {
            while(b[j])
            {
                j++ ;
            }
            if('A'+j == 'I' )
                j++ ;
            if('A'+j == 'J')
                j++ ;
            while(b[j])
            {
                j++ ;
            }
            pfm[order[i]/5][order[i]%5] = (char)('A'+(j++));
        }
    }
    else
    {
        replace(pt.begin(), pt.end(), 'J', 'I');
        for(; i < 25; i++)
        {
            while(b[j])
            {
                j++ ;
            }
            if('A'+j == 'J')
                j++ ;
            while(b[j])
            {
                j++ ;
            }
            pfm[order[i]/5][order[i]%5] = (char)('A'+(j++));
        }
    }
    for(int i = 0; i < lv; i++)
        ChangeMatrix();
    print();
    for(int i = 0; i < pt.length(); i++)
    {
        ptm += pt[i];
        if(pt[i] == pt[i+1])
        {
            if(pt[i] == 'Z')
                ptm += 'Y' ;
            else
                ptm += 'Z' ;
        }
    }
    if(ptm.length()&1)
    {
        if(ptm[ptm.length()-1] == 'Z')
            ptm += 'Y' ;
        else
            ptm += 'Z' ;
    }
    for(int i = 0; i < ptm.length(); i += 2)
        encrypt(ptm[i], ptm[i+1]);
    return 0;
}

