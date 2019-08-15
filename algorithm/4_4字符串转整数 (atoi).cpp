class Solution {
public:
    int myAtoi(string str) {
        const int maxint=0x7fffffff;
        const int minint=0x80000000;
        const long long max=0x100000000;
        long long ans=0;
        bool flag=false;
        int st=0;
		
        while(st<str.length()&&str[st]==' '){
            st++;
        }
		
        if(st<str.length()&&str[st]=='+'){
            st++;
        }else{
            if(st<str.length()&&str[st]=='-'){
                flag=true;
                st++;
            }
        }
		
        for(int i=st;i<str.length();i++){
            if(str[i]<='9'&&str[i]>='0'){
                ans=ans*10+str[i]-'0';
                if(ans>maxint) ans=max;
            }else{
                break;
            }
        }
        if(flag) ans=-ans;
        if(ans>maxint) ans=maxint;
        if(ans<minint) ans=minint;
        
        return ans;
        
    }
};

