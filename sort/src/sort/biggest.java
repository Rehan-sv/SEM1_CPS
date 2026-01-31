package sort;
import java.util.Scanner;
public class biggest {
	public static void main (String[] args) {
		Scanner data = new Scanner(System.in);
        System.out.print("Enter first number: ");
        int a = data.nextInt();

        System.out.print("Enter second number: ");
        int b = data.nextInt();

        System.out.print("Enter third number: ");
        int c = data.nextInt();
        if (a>=b && a>=c) {
            System.out.println("Biggest number is: " + a);
        } else if (b >= a && b >= c) {
            System.out.println("Biggest number is: " + b);
        } else {
            System.out.println("Biggest number is: " + c);
        }
        
        }
	}
