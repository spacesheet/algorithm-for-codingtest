fn main() {
    // option 타입
    let some_number = Some(5);
    let _no_number: Option<i32> = None;

    match some_number {
        Some(value) => println!("값이 있음: {}", value),
        None => println!("값이 없음"),
    }

    // result 타입
    let result = divide(10, 2);
    match result {
        Ok(value) => println!("결과: {}", value),
        Err(error) => println!("오류: {}", error),
    }
}

fn divide(a: i32, b: i32) -> Result<i32, String> {
    if b == 0 {
        Err(String::from("0으로 나눌 수 없습니다"))
    } else {
        Ok(a / b)
    }

}
