class Solution {
public:
    vector<int> twoSum(vector<int>& v, int target) {
        for(int i=0;i<v.size();i++)
        {
            for(int j=i+1;j<v.size();j++)
            {
                if(v[i]+v[j]==target)
                {
                    vector <int> num;
                    num.push_back(i);
                    num.push_back(j);
                    return num;
                }
            }
        }
        return vector <int>();
    }
};