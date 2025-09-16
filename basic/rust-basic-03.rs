fn main() {
    let result = add(-2147483648, 2147483647);
    println!("result: {}", result);

    greet("world!");
}

// 매개변수와 반환값이 있는 함수 function
fn add(a: i32, b: i32) -> i32 {
    a + b // return 없어도 마지막 표현식이 반환값
}

// 반환값이 없는 함수 procedure
fn greet(name: &str) {
    println!("hello, {}!", name)
}
