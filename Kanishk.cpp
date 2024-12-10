#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int k;
        cin >> k;
        vector<int> v(k);
        unordered_map<int, int> d;
        for (int i = 0; i < k; ++i) {
            cin >> v[i+1];
            d[v[i]]++;
        }
        if (d[1] > 0 && d[k - 2] > 0) {
            cout << 1 << " " << k - 2 << endl;
            continue;
        }
        bool f = false;
        for (int i = 2; i * i <= k - 2; ++i) {
            if ((k - 2) % i == 0) {
                int a = i, b = (k - 2) / i;
                if (a == b) {
                    if (d[a] > 1) {
                        cout << a << " " << a << endl;
                        f = true;
                        break;
                    }
                } else if (d[a] > 0 && d[b] > 0) {
                    cout << a << " " << b << endl;
                    f = true;
                    break;
                }
            }
        if (!f) cout << "No valid factors" << endl;
    }
    return 0;
}
