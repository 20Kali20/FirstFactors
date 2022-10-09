//Kalina Dzierzak
#include <iostream>
#include <vector>
#include <numeric>
#include <cmath>

using namespace std;

class Factor
{
    public:
        int FirstFactor;
        int Count;

        Factor(int firstFactor, int count) : FirstFactor(firstFactor), Count(count) {}
};

int main()
{
    cout << "Enter number: ";
    int num;
    cin >> num;
    int num_2 = num;

    vector<Factor> factors;

    int i = 2;
    int y = 1;
    while(i <= num)
    {
        if (num % i == 0)
        {
            if (y == 1)
            {
                factors.push_back(Factor(i, 1));
            }
            else
            {
                (factors.back()).Count++;
            }
            num = num / i;
            y++;
        }

        else
        {
            i++;
            y = 1;
        }
    }

    int countOfDivisors = 1;
    for(auto it = factors.begin(); it != factors.end(); ++it)
    {
        countOfDivisors *= (it->Count + 1);
    }

    vector<int> divisors;
    int z = 1;
    int a = 1;
    while (a <= ceil(float(countOfDivisors)/2.0f))
    {
        if (num_2 % z == 0)
        {
            divisors.push_back(z);
            if(z != num_2/z)
            {
                divisors.push_back(num_2 / z);
            }
            a++;
        }
        z++;
    }

    cout << "Count of divisors = " << countOfDivisors << endl;

    cout << "Divisors = ";
    for(auto it = divisors.begin(); it != divisors.end(); ++it)
    {
        cout << *it << " ";
    }
    cout << endl;

    for(auto it = factors.begin(); it != factors.end(); ++it)
    {
        cout << it->FirstFactor;
        if (it->Count > 1) cout << "^" << it->Count;
        cout << " ";
    }
    cout << endl;

    cout << "[ ";
    for(auto it = factors.begin(); it != factors.end(); ++it)
    {
        cout << "[" << it->FirstFactor << ", " << it->Count << "] ";
    }
    cout << "]" << endl;
}