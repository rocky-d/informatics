package datastructure;

import rockyutil.Examination;

import java.util.Random;

class UnionFindSets {

    int[] array;

    UnionFindSets() {
        int n = 100;
        this.array = new int[n];
        for (int i = 0; i < n; i++) {
            this.array[i] = i;
        }
    }

    UnionFindSets(int[] array) {
        this.array = array;
    }

    UnionFindSets(int n) {
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

    public static void main(String[] args) {
        int n = 1000000;
        int m = 20000000;
        int[][] inputArray = new int[m][2];
        Random random = new Random(19891213);
        UnionFindSets unionFindSets = new UnionFindSets(n);

        Examination.start();
        for (int i = 0; i < m; i++) {
            inputArray[i][0] = random.nextInt(n);
            inputArray[i][1] = random.nextInt(n);
        }
        Examination.end();
        System.out.println("Input Done!");

        Examination.start();
        for (int i = 0; i < m; i++) {
            union(unionFindSets.array, inputArray[i][0], inputArray[i][1]);
        }
        Examination.end();
        System.out.println("Union Done!");
    }
}