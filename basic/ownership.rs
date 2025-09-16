///  소유권 모델
///  각 메모리 블록은 정확히 하나의 소유자를 가짐
///  소유자가 스코프를 벗어나면 메모리 자동 해제
///  컴파일 타임에 메모리 안정성 보장
/// 
///  런타임 오버헤드 없음
///  메모리 누수와 댕글링 포인터 방지
///  동시성 안정성 보장
/// 
///  cf) GC: 메모리 관리 실수 방지, 복잡한 데이터 구조 구현 용이, 런타임 오버헤드(CPU와 메모리) 
 

fn main() {
    // 문자열 소유권 이동
    let s1 = String::from("hello");
    let s2 = s1;  // s1의 소유권이 s2로 이동
    // println!("{}", s1);  // s1은 더 이상 유효하지 않음
    println!("{}", s2);
    
    // 참조 (borrowing)
    let s3 = String::from("world");
    let len = calculate_length(&s3);  // 참조로 전달
    println!("'{}'의 길이는 {}입니다", s3, len);  // s3 사용 가능
}

fn calculate_length(s: &String) -> usize {
    s.len()
}
