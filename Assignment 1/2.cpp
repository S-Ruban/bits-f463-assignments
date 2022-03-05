#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int eea(int a, int b, int& x, int& y)
{
    int gcd ;
    if(b)
    {
        int x1, y1 ;
        gcd = eea(b, a%b, x1, y1);
        x = y1 ;
        y = x1 - (a/b)*y1 ;
    }
    else
    {
        x = 1 ;
        y = 0 ;
        return a ;
    }
    return gcd ;
}

int lincong(int a, int b)
{
    a = a%26 ;
    b = b%26 ;
    int u = 0, v = 0, d = eea(a, 26, u, v);
    if(b % d)
    {
        cout << "no" ;
        exit(0);
    }
    return (((u*(b/d))%26)+26)%26 ;
}

int main() {
    string ct, pt, d1, d2 ;
    int k11, k12, k21, k22, det ;
    cin >> ct >> d1 >> d2 ;
    if(ct.size()&1)
        ct += 'x' ;
    k11 = lincong(27, (((4*(d1[0]-'a')-7*(d2[0]-'a'))%26)+26)%26);
    k21 = lincong(7, ((((d1[0]-'a')-19*k11)%26)+26)%26);
    k12 = lincong(27, (((4*(d1[1]-'a')-7*(d2[1]-'a'))%26)+26)%26);
    k22 = lincong(7, ((((d1[1]-'a')-19*k12)%26)+26)%26);
    det = k11*k22 - k12*k21 ;
    k12 *= -1 ;
    k21 *= -1 ;
    k11 = k11 + k22 ;
    k22 = k11 - k22 ;
    k11 = k11 - k22 ;
    if((!det) || (!(det%2) || !(det%13)))
    {
        cout << "no" ;
        exit(0);
    }
    if(det < 0)
    {
        k11 *= -1 ;
        k12 *= -1 ;
        k21 *= -1 ;
        k22 *= -1 ;
        det *= -1 ;
    }
    for(int i = 0; i < ct.size()-1; i += 2)
    {
        pt += (char)(((int)((ct[i])-'a')*((((k11*lincong(((det%26)+26)%26,1))%26)+26)%26) + (int)(ct[i+1]-'a')*(((((((k21%26)+26)%26)*lincong(((det%26)+26)%26,1))%26)+26)%26))%26 + 'a');
        pt += (char)(((int)((ct[i])-'a')*(((((((k12%26)+26)%26)*lincong(((det%26)+26)%26,1))%26)+26)%26) + (int)(ct[i+1]-'a')*((((k22*lincong(((det%26)+26)%26,1))%26)+26)%26))%26 + 'a');
    }
    for(int i = 0; i < ct.size()-1; i++)
        cout << pt[i];
    if(pt[pt.size()-1] != 'x')
        cout << pt[pt.size()-1];
    return 0;
}

