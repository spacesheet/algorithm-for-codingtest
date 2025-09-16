package Simulation;

public class 이진변환반복하기 {
    public int[] solution(String s) {
    int[] answer = new int[2];  // 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수
 
    while(s.length() > 1) { // while()을 활용해서 입력받은 문자열 s의 길이가 1이 될 때까지 반복합니다.
 
      int cntOne = 0; // 1의 개수를 세어줄 int형 변수
      for(int i=0; i<s.length(); i++) {
 
        if(s.charAt(i) == '0') answer[1]++;
        else cntOne++;
      } // for()을 s의 길이만큼 돌립니다. 조건문을 활용해서 첫 번째 문자부터 0인지 확인합니다.
        // 만약 0이면 answer[1]++를 하고 그렇지 않으면 cntOne++를 합니다. (이진수라서 0이 아니면 무조건 1이기 때문)
 
      s = Integer.toBinaryString(cntOne); // 위에서 계산해둔 1의 개수를 toBinaryString()를 사용해서 이진수로 변경하고 s에 넣어둡니다.
                                          // 예시 1번에 따르면 1의 개수가 총 6개라서 cntOne이 6이 되어있고, 이를 이진수로 변경하면 110이 됩니다.
      answer[0]++; // 이렇게 이진수로 변환할 때마다 answer[0]++
    }
 
    return answer; // 이진 변환 횟수와 제거한 0의 개수를 확인할 수 있고 이를 리턴
  }
}
