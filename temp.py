#include <iostream>
using namespace std;

int main () {
double Celsius;
double farenheit;
string temp = "°F";
cout << "What is the Celsius temperature value?" << endl;
cin >> Celsius;
double result = Celsius * 9;
double result_2 = result / 5;
double Farenheit = result_2 + 32;
cout << Farenheit << temp << endl;
}