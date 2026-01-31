package sort;
import java.util.Scanner;

public class sort_using_for_loop {
    public static void main(String[] args) {
        Scanner data = new Scanner(System.in);

        System.out.print("Enter number 1: ");
        int largest = data.nextInt();

        for (int i = 2; i <= 3; i++) {
            System.out.print("Enter number " + i + ": ");
            int num = data.nextInt();

            if (num > largest) {
                largest = num;
            }
        }

        System.out.println("Largest number is: " + largest);
    }
}
