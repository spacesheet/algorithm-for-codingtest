import java.util.Scanner;

public class Fibonacci {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
				fibonacci= new int[N+1];
				fibo(N);
        for (int i = 1; i <= N; i++) {
            System.out.print(fibonacci[i]+" ");
        }
    }
    static int[]fibonacci;
    static int fibo(int n){
        if(fibonacci[n]>0) return fibonacci[n];  //메모이제이션 핵심!
        if(n==1||n==2) return fibonacci[n]=1;;
        return fibonacci[n]=fibo(n-2)+fibo(n-1);
    }
}