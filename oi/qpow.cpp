#include <iostream>
using namespace std;
typedef long long LL;
const LL MOD = 2e9 + 7;

LL qpow(LL a, LL b) {
    LL res = 1;
    while (b) {
        if (b & 1) res = res * a % MOD;
        a = a * a % MOD;
        b >>= 1;
    }
    return res;
}