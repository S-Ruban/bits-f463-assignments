#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int char_to_hex(char c)
{
    int ans = c & 0x0f ;
    if(c >= 'a' && c <= 'f')
        ans += 0x09 ;
    return ans ;
}

char hex_to_char(int x)
{
    int ans = x + 0x30 ;
    if(x >= 0x0a && x <= 0x0f)
        ans += 0x27 ;
    return ans ;
}

int main() {
    string str ;
    cin >> str ;
    int pre[str.length()], post[str.length()];
    pre[0] = char_to_hex(str[0]);
    for(int i = 1; i < str.length(); i++)
        pre[i] = pre[i-1] ^ char_to_hex(str[i]);
    post[str.length()-1] = char_to_hex(str[str.length()-1]);
    for(int i = str.length()-2; i >= 0; i--)
        post[i] = post[i+1] ^ char_to_hex(str[i]);
    for(int i = 0; i < str.length(); i++)
        cout << hex_to_char(pre[i]);
    for(int i = 1; i < str.length(); i++)
        cout << hex_to_char(post[i]);
    return 0;
}

