#include<bits/stdc++.h>;
using namespace std;
int main(){
 int n,q,x;cin>>n;vector<long long>a(n),p(n+1);
 for(auto&v:a)cin>>v;
 sort(a.begin(),a.end());
 for(int i=0;i<n;i++)p[i+1]=p[i]+a[i];
 cin>>q;
 while(q--){cin>>x;int k=upper_bound(a.begin(),a.end(),x)-a.begin();cout<<k<<" "<<p[k]<<"\n";}
}