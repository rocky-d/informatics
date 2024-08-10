package onlinejudge.luogu.solved;

import java.util.Scanner;

class P1551 {
    static int N, M, P;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        N = scanner.nextInt();
        M = scanner.nextInt();
        P = scanner.nextInt();
        DisjointSetUnion dsu = new DisjointSetUnion(N + 1);
        for (int i = 0; i < M; ++i) {
            DisjointSetUnion.union(dsu.array, scanner.nextInt(), scanner.nextInt());
        }
        for (int i = 0; i < P; ++i) {
            System.out.println(DisjointSetUnion.isSameHead(dsu.array, scanner.nextInt(), scanner.nextInt()) ? "Yes" : "No");
        }
    }

    public static void main(String[] args) {
        input();
    }

    static class DisjointSetUnion {
        int[] array;

        DisjointSetUnion(int n) {
            this.array = new int[n];
            for (int i = 0; i < n; i++) {
                this.array[i] = i;
            }
        }

        static int findHead(int[] arr, int node) {
            return node == arr[node] ? node : (arr[node] = findHead(arr, arr[node]));
        }

        static void union(int[] arr, int a, int b) {
            arr[findHead(arr, a)] = findHead(arr, b);
        }

        static boolean isSameHead(int[] arr, int a, int b) {
            return findHead(arr, a) == findHead(arr, b);
        }
    }
}

