#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int k11, k21, k12, k22 ;
    string pt ;
    cin >> k11 >> k21 >> k12 >> k22 >> pt ;
    if(pt.size()&1)
        pt += 'X' ;
    for(int i = 0; i < pt.size(); i += 2)
        cout << (char)(((((pt[i]-'A')*k11)%26+((pt[i+1]-'A')*k21)%26)%26)+'a') << (char)(((((pt[i]-'A')*k12)%26+((pt[i+1]-'A')*k22)%26)%26)+'a');
    return 0;
}

