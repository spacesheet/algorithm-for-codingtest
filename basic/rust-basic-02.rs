fn main() {
    // 정수형 int가 32비트 차지
    let age: i32 = -2147483648;

    // 실수형 부호1 / 지수11 / 가수52비트
    let price: f64 = 29.99; // +-10^308 부동소수점(유효자릿수 약15-17), 근사값

    // 불린형
    let is_active: bool = true;

    // 문자열
    let letter: char = 'A';

    // 문자열
    let string_data_of_binary: &str = "홍길동"; // static
    /**
     * 단순 배열 포인터 = 주소값 (x)
     * fat pointer (o) 
     */

    struct StrRef_stack {
        ptr: *const u8, // 단순 배열 포인터
        len: usize, // 바이트 길이
    }

    /**
     * String vs array of chars
     * 문자열은 UTF-8 로 된 일련의 바이트, 문자의 배열이 아님
     * Unicode 글자가 배열
     */

    let s: &str = "홍길동";
    // Unicode array [237, 153, 141, 234, 184, 184, 235, 143, 153]
    // 9 bytes

    /**
     * [234, 184, 184]
     * 0xEA  0xB8 0xB8
     *     다름   같음
     */

    /**
     * '길'의 UTF-8 인코딩 과정
     *  1. '길'의 유니코드 코드포인트 찾기
     *  2. UTF-8 3바이트 패턴으로 분할 (16비트 = 4 + 6 + 6)
     *  3. UTF-8 바이트 구성 (첫 바이트: 몇 바이트 문자, 후속 바이트: 모두 10으로 시작, 연속 바이트)
     */

    let owned_string_heap: String = String::from("소유된 문자열");

    struct String_stack {
        ptr: *mut u8, // 힙 메모리 주소, 실제 문자열 데이터
        len: usize, // 현재 길이
        capacity: usize, // 할당된 용량
    }

    // Rust's 소유권 system
    // 소유권 이동이 기본이며, 명시적으로 &을 써야 참조

    fn take_string_call_by_value(s: String) { } // 소유권 이동
    let my_string = String::from("test");
    take_string_call_by_value(my_string); // my_string 재사용 불가

    fn borrow_string_call_by_ref(s: &String) { } // 빌려오기, &명시적 참조
    let my_string = String::from("test");
    borrow_string_call_by_ref(&my_string); // my_string 사용 가능, &명시적 참조
}
