//#include <bits/stdc++.h>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

/*
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

string timeConversion(string s)
{
    int hh = stoi(s.substr(0, 2));
    int mm = stoi(s.substr(3, 2));
    int ss = stoi(s.substr(6, 2));
    string ampm = s.substr(8, 2);
    if (ampm == "AM" || ampm == "am")
    {
        if (hh == 12)
        {
            hh = 0; // e.g. 12:00:00AM becomes 00:00:00
        }
    }
    else if (ampm == "PM" || ampm == "pm")
    {
        if (hh < 12)
        {
            hh += 12; // e.g. 01:00:00PM becomes 13:00:00
        }
    }

    int size = std::snprintf(nullptr, 0, "%2d:%2d:%2d", hh, mm, ss);
    // fill in eight chars '\0' (this holds the date in 24h format)
    string output(8, '\0');
    sprintf(&output[0], "%02d:%02d:%02d", hh, mm, ss);
    return output;
}
 
int main()
{
    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        string s;
        cin >> s;
        string result = timeConversion(s);
        cout << result << "\n";
    }

    return 0;
}
