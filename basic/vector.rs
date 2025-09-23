fn main() {
    // 벡터 생성
    let mut v = Vec::new();
    v.push(1);
    v.push(2);

    // 매크로
    let v2 = vec![1, 2, 3, 4, 5];

    for i in &v2 {
        println!("값: {}", i);
    }

    // 인덱스로 접근
    if let Some(third) = v2.get(2) {
        println!("세 번째 요소: {}", third);
    }
}
