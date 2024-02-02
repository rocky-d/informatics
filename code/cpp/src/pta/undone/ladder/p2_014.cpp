#include <bits/stdc++.h>

using namespace std;

const int N_MAX = 100000;

int n, nums[N_MAX];

int que_heads[N_MAX], que_tails[N_MAX], ques[N_MAX][N_MAX], ques_len, ques_len_max, waiting;
bool loopelse1, loopelse2;

int main() {
    cin >> n;
    for (int i = 0; i < n; i += 1) {
        cin >> nums[i];
    }

    ques_len = 0;
    ques_len_max = 0;
    waiting = n;
    for (int i = 0; i < n; i += 1) {
        if (waiting == nums[i]) {
            waiting -= 1;
            loopelse1 = true;
            while (1 <= waiting) {
                loopelse2 = true;
                for (int j = 0; j < ques_len; j += 1) {
                    if (waiting == ques[j][que_heads[j]]) {
                        if (1 == (que_tails[j] - que_heads[j] + N_MAX) % N_MAX) {
                            ques_len -= 1;
                            for (int k = que_heads[ques_len]; k != que_tails[ques_len]; k = (1 + k) % N_MAX) {
                                ques[j][k] = ques[ques_len][k];
                            }
                            que_heads[j] = que_heads[ques_len];
                            que_tails[j] = que_tails[ques_len];
                        } else {
                            que_heads[j] = (1 + que_heads[j]) % N_MAX;
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
            loopelse1 = true;
            for (int j = 0; j < ques_len; j += 1) {
                if (nums[i] < ques[j][que_tails[j] - 1]) {
                    ques[j][que_tails[j]] = nums[i];
                    que_tails[j] = (1 + que_tails[j]) % N_MAX;
                    loopelse1 = false;
                    break;
                }
            } if (loopelse1) {
                que_heads[ques_len] = 0;
                que_tails[ques_len] = 0;
                ques[ques_len][que_tails[ques_len]] = nums[i];
                que_tails[ques_len] = (1 + que_tails[ques_len]) % N_MAX;
                ques_len += 1;
                if (ques_len_max < ques_len) {
                    ques_len_max = ques_len;
                }
            }
        }
    }
    cout << 1 + ques_len_max << endl;
    return 0;
}
