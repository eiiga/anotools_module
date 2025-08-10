import static util.RecursiveMultidimensionalArraysUtil.printArray;

public class RecursiveMultidimensionalArraysMain {

  public static void main(String[] args) {
    // 1次元配列
    int[] array1D = {
        1, 2, 3
    };

    // 2次元配列
    int[][] array2D = {
        {1, 2, 3},
        {4, 5, 6}
    };

    // 3次元配列
    int[][][] array3D = {
        {{1, 2}, {3, 4}},
        {{5, 6}, {7, 8}}
    };

    // 4次元配列
    int[][][][] array4D = {
        {
            {{1, 2}, {3, 4}},
            {{5, 6}, {7, 8}}
        },
        {
            {{9, 10}, {11, 12}},
            {{13, 14}, {15, 16}}
        }
    };

    // 多次元配列（不規則な多次元）
    Object jagged = new Object[]{
        new int[]{1, 2, 3},
        new Object[]{
            new int[]{4, 5},
            new int[][]{{6}, {7, 8}}
        },
        9
    };

    System.out.println("=== 1次元 ===");
    printArray(array1D);

    System.out.println("\n=== 2次元 ===");
    printArray(array2D);

    System.out.println("\n=== 3次元 ===");
    printArray(array3D);

    System.out.println("\n=== 4次元 ===");
    printArray(array4D);

    System.out.println("\n=== 多次元 ===");
    printArray(jagged);
  }
}
