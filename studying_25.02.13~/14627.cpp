#include <iostream>
#include <vector>
using namespace std;

int s, c;
vector<long long> lengths;

bool check(long long mid) {
    long long cnt = 0;
    for (long long len : lengths) {
        cnt += len / mid;
    }
    return cnt >= c;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> s >> c;

    long long left = 0, right = 1e9 + 1;
    for (int i = 0; i < s; i++) {
        long long x; cin >> x;
        lengths.push_back(x);
    }

    while (left + 1 < right) {
        long long mid = (left + right) / 2;
        if (check(mid)) left = mid;
        else right = mid;
    }

    // 이걸로 하면 실패
    long long ans = 0;
    if (left) {
        for (long long len : lengths) {
            ans += len % left;
        }
    } else {
        for (long long len : lengths) {
            ans += len;
        }
    }
    
    // 이걸로 하면 통과
    // long long sum = 0;
    // for (long long len : lengths) {
    //     sum += len;
    // }
    // long long ans = sum - left * c;
    
    cout << ans;
}