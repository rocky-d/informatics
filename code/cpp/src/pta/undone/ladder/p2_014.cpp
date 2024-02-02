#include <bits/stdc++.h>
using namespace std;

const int N_MAX = 100000;

int n, nums[N_MAX];

int main() {
    cin >> n;
    for (int i = 0; i < n; i += 1) {
        cin >> nums[i];
    }

    int q_heads[N_MAX], q_tails[N_MAX], queues[N_MAX][N_MAX], queues_len, queues_len_max, waiting;
    queues_len = 0;
    queues_len_max = 0;
    waiting = n;
    for (int i = 0; i < n; i += 1) {
        if (waiting == nums[i]) {
            waiting -= 1;
            bool loopelse1 = true;
            while (1 <= waiting) {
                bool loopelse2 = true;
                for (int j = 0; j < queues_len; j += 1) {
                    if (waiting == queues[j][q_heads[j]]) {
                        if (1 == (q_tails[j] - q_heads[j] + N_MAX) % N_MAX) {
                            queues_len -= 1;
                            for (int k = q_heads[queues_len]; k != q_tails[queues_len]; k = (1 + k) % N_MAX) {
                                queues[j][k] = queues[queues_len][k];
                            }
                            q_heads[j] = q_heads[queues_len];
                            q_tails[j] = q_tails[queues_len];
                        } else {
                            q_heads[j] = (1 + q_heads[j]) % N_MAX;
                        }
                        waiting -= 1;
                        loopelse2 = false;
                        break;
                    }
                } if (loopelse2) {
                    loopelse1 = false;
                    break;
                }
            } if (loopelse1) {
                break;
            }
        } else {
            bool loopelse1 = true;
            for (int j = 0; j < queues_len; j += 1) {
                if (nums[i] < queues[j][q_tails[j] - 1]) {
                    queues[j][q_tails[j]] = nums[i];
                    q_tails[j] = (1 + q_tails[j]) % N_MAX;
                    loopelse1 = false;
                    break;
                }
            } if (loopelse1) {
                q_heads[queues_len] = 0;
                q_tails[queues_len] = 0;
                queues[queues_len][q_tails[queues_len]] = nums[i];
                q_tails[queues_len] = (1 + q_tails[queues_len]) % N_MAX;
                queues_len += 1;
                if (queues_len_max < queues_len) {
                    queues_len_max = queues_len;
                }
            }
        }
    }
    cout << 1 + queues_len_max << endl;
    return 0;
}
