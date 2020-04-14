//Time Conversion
//https://www.hackerrank.com/challenges/time-conversion/problem

#include <bits/stdc++.h>

using namespace std;

string timeConversion(string s) {

    if(s[8] == 'P')
    {
        if((s[0]!='1') || (s[1]!='2'))
        {
            int firstHour = int(s[0]) + 1;
            s[0] = char(firstHour);

            int secondHour = 0;
            if(s[1] == '8')
                secondHour = 0;
            else if(s[1] == '9')
                secondHour = 1;
            else
            {
                secondHour = (int(s[1])+2);
            }

            s[1] = char(secondHour);
        }

    }
    else if((s[8] == 'A') && (s[0]=='1') && (s[1]=='2'))
    {
        s[0] = '0';
        s[1] = '0';
    }
    s.erase(s.size()-2, 2);
    return s;

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = timeConversion(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
