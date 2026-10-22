#include<bits/stdc++.h>
using namespace std;
int main(){
 int n,k;
 cin>>n>>k;
 vector<long long>a(n);
 long long l=0,r=0;
 for(auto&x:a)
 cin>>x,l=max(l,x),r+=x;
 while(l<r)
 {
  long long m=(l+r)/2,s=0;
  int c=1;
  for(auto x:a)if(s+x>m)c++,s=x;else s+=x;
  c<=k?r=m:l=m+1;
 }
 cout<<l;
}