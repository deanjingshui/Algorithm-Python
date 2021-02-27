#include <iostream>
#include <vector>
#include <algorithm>  // std::sort
using namespace std;

class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) 
    {
        int ret = 0;
        int i = 0;
        int j = 0;
        int g_len = g.size();
        int s_len = s.size();
        
        sort(g.begin(), g.end(), greater<int>());
        sort(s.begin(), s.end(), greater<int>());
        
        while (i<g_len && j<s_len)
        {
            if (g[i]<=s[j])
            {
                ret += 1;
                i += 1;
                j += 1;
            }
            else
            {
                i += 1;
            }
        }
        return ret;
    }
};


int main()
{
    vector<int> g = {1, 2, 3};
    vector<int> s = {1, 1};
    int ret;

    Solution my_sol;
    ret = my_sol.findContentChildren(g, s);

    cout << "result is: " << ret << endl;

    return 0;
}