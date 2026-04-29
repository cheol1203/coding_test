package d1;

import java.util.Scanner;

public class c2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T;
        T=sc.nextInt();
		/*
		   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
		*/

        for(int test_case = 1; test_case <= T; test_case++)
        {
            //30
            int third_num = test_case / 100;  //0
            int second_num = (test_case % 100) / 10;  // 3
            int first_num = (test_case % 100) % 10;  //0

            int count = 0;
            if(third_num % 3 == 0 & third_num != 0){
                count++;
            }
            if(second_num % 3 == 0 & second_num != 0){
                count++;
            }
            if(first_num % 3 == 0 & first_num != 0){
                count++;
            }



            if(count>0){
                for(int i =0; i<count; i++){
                    System.out.print("-");
                }
            }else{
                System.out.print(test_case);
            }

            if(test_case != T){
                System.out.print(" ");
            }

            /////////////////////////////////////////////////////////////////////////////////////////////
			/*
				 이 부분에 여러분의 알고리즘 구현이 들어갑니다.
			 */
            /////////////////////////////////////////////////////////////////////////////////////////////

        }
    }
}
