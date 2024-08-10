package luogu.contest.c20230730njit;

import java.util.*;

class QC {
    static int n, target, numsSize;
    static List<Integer> nums;
    static int res = 0;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        target = scanner.nextInt();
        nums = new ArrayList<>(n);
        int tmp;
        for (int i = 0; i < n; i++) {
            tmp = scanner.nextInt();
            if (tmp < target) {
                nums.add(tmp);
            } else if (tmp == target) {
                ++res;
            }
        }
        scanner.close();
        nums.sort(Comparator.comparingInt(x -> x));
        numsSize = nums.size();
    }

    static void dfs(int sum, int start) {
        if (target == sum) {
            ++res;
        } else if (target > sum) {
            int last = -1;
            for (int i = start + 1; i < numsSize; i++) {
                if (last != nums.get(i)) {
                    dfs(sum + nums.get(i), i);
                    last = nums.get(i);
                }
            }
        }
    }

    public static void main(String[] args) {
        input();
        Deque<int[]> queue;
        int[] vertex;
        int last = -1, lastDfs;
        for (int i = 0; i < numsSize; i++) {
            if (last != nums.get(i)) {
//                dfs(nums.get(i), i);

                queue = new ArrayDeque<>(n);
                queue.push(new int[]{nums.get(i), i});
                while (!queue.isEmpty()) {
                    vertex = queue.pop();
                    if (target == vertex[0]) {
                        ++res;
                    } else if (target > vertex[0]) {
                        lastDfs = -1;
                        for (int j = vertex[1] + 1; j < numsSize; j++) {
                            if (lastDfs != nums.get(j)) {
                                queue.push(new int[]{vertex[0] + nums.get(j), j});
                                lastDfs = nums.get(j);
                            }
                        }
                    }
                }

                last = nums.get(i);
            }
        }
        System.out.println(res);
    }
}