#include <iostream>

using namespace std;

int gcd(int num1, int num2) {
    if (num2 == 0)
        return num1;
    else
        return gcd(num2, num1 % num2);
}

class Frac {
    int bunja;
    int bunmo;
    bool isDivided;
public:
    Frac(int bunja, int bunmo) {
        if (bunja == 0) {
            this->bunja = bunja;
            this->bunmo = 1;

            isDivided = (bunmo == 1) ? false : true;
        }
        else {
            this->bunja = bunja / gcd(bunja, bunmo);
            this->bunmo = bunmo / gcd(bunja, bunmo);

            isDivided = (this->bunja == bunja) ? false : true;
        }
    }

    int getBunmo() {
        return bunmo;
    }

    bool getIsDivided() {
        return isDivided;
    }

    friend int operator>=(Frac f1, Frac f2) {
        return f1.bunja * f2.bunmo >= f1.bunmo * f2.bunja;
    }

    void printFrac() {
        cout << bunja << " / " << bunmo << endl;
    }
};

int main() {
    int P, Q;
    cin >> P >> Q;

    Frac confirmFrac(P, Q);

    int count = 2;
    for (int bunmo = 2; bunmo <= confirmFrac.getBunmo(); bunmo++) {
        for (int bunja = 1; bunja <= bunmo - 1; bunja++) {
            Frac temp(bunja, bunmo);
            if (not temp.getIsDivided()) {
                Frac checkFrac(1, temp.getBunmo());
                if (checkFrac >= confirmFrac) {
                    count++;
                }
            }
        }
    }

    cout << count << endl;

    return 0;
}