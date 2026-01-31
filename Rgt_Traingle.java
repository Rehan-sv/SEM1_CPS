class Rgt_Traingle{
    public static void main(String[] args) {
        int rows = 4;

        for (int i = 1; i <= rows; i++) {   // Outer loop = rows
            for (int j = 1; j <= i; j++) {  // Inner loop = numbers per row
                System.out.print(j);
            }
            System.out.println(); 
        }
    }
}
