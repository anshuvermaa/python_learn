#include<bits/stdc++.h>
using namespace std;

int main()
{
    long long t;
    cin>>t;
    while (t--)
    {
        string s;
        cin>>s;
        long long min=s[0]-'0';
        if(s.length()==2) cout<<s[1]<<endl;
        else{
            for (long long i = 0; i < s.length(); i++)
        {
            long long num=s[i]-'0';
            if(num<min) min=num;
        }
        cout<<min<<"\n";
        }

    }
    
    return 0;
}