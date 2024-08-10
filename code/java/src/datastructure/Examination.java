package datastructure;

public class Examination {
    public static long concurrentTime1 = Long.MAX_VALUE;
    public static long concurrentTime2 = Long.MIN_VALUE;
    public static long concurrentMemory1 = Long.MAX_VALUE;
    public static long concurrentMemory2 = Long.MIN_VALUE;

    public static long getConcurrentTime1() {
        return concurrentTime1;
    }

    public static void setConcurrentTime1(long concurrentTime1) {
        Examination.concurrentTime1 = concurrentTime1;
    }

    public static long getConcurrentTime2() {
        return concurrentTime2;
    }

    public static void setConcurrentTime2(long concurrentTime2) {
        Examination.concurrentTime2 = concurrentTime2;
    }

    public static long getConcurrentMemory1() {
        return concurrentMemory1;
    }

    public static void setConcurrentMemory1(long concurrentMemory1) {
        Examination.concurrentMemory1 = concurrentMemory1;
    }

    public static long getConcurrentMemory2() {
        return concurrentMemory2;
    }

    public static void setConcurrentMemory2(long concurrentMemory2) {
        Examination.concurrentMemory2 = concurrentMemory2;
    }

    public static void start() {
        Runtime runtime = Runtime.getRuntime();
        concurrentMemory1 = runtime.totalMemory() - runtime.freeMemory();

        concurrentTime1 = System.nanoTime();
    }

    public static void end() {
        concurrentTime2 = System.nanoTime();

        Runtime runtime = Runtime.getRuntime();
        concurrentMemory2 = runtime.totalMemory() - runtime.freeMemory();

        // 计算start和end之间的代码执行期间所耗时间(ms)与内存(M)。
        // 1毫秒(ms) = 1000微秒(us) = 1000 000纳秒(ns)
        // 1MB = 1 * 2^20 Byte = 1024 * 1024 Byte;

//        String time = String.valueOf((double) (concurrentTime2 - concurrentTime1) / 1000000);
//        String memory = String.valueOf((double) (concurrentMemory2 - concurrentMemory1) / 1024);
//        System.out.println("Time：" + time.substring(0, time.equals("0.0") ? 1 : (time.indexOf(".") + 4)) + " ms, Memory：" + memory.substring(0, memory.equals("0.0") ? 1 : (memory.indexOf(".") + 4)) + " KB");
        System.out.println("Time: " + (concurrentTime2 - concurrentTime1) / 1000000.0D + " ms");
        System.out.println("Memory: " + (concurrentMemory2 - concurrentMemory1) / 1024.0D + " KB");
        concurrentTime1 = Long.MAX_VALUE;
        concurrentTime2 = Long.MIN_VALUE;
        concurrentMemory1 = Long.MAX_VALUE;
        concurrentMemory2 = Long.MIN_VALUE;
    }

    public static void main(String[] args) {
        start();
        int x = 0;
        for (int i = 0; i < 555413255; ++i) {
            for (int j = 0; j < 24103434; ++j) {
                ++x;
            }
            x %= 10007;
        }
        end();
        System.out.println(x);
    }
}