fn main() {
    // 불변 변수 immutable variables 런타임 바인딩
    let x = 5;
    
    // 가변 변수 mutable variables
    let mut y = 10;
    y = 20;

    // 상수 constant
    const MAX_SIZE: u32 = 4294967295;

    // 상수 literal 컴파일 시점에 값이 결정됨
    let x = 42;
    // x = 43 (x) 재할당 불가
    // let count = get_count(); (x) 런타임 때 값이 결정됨
}
