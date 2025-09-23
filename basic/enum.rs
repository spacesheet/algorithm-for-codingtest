enum Color {
    Red,
    Green,
    Blue,
}

enum Message {
    Quit,
    Move { x: i32, y:i32 },
    Write(String),
}

fn main() {
    let color = Color::Red;

    match color {
        Color::Red => println!("빨간색"),
        Color::Green => println!("초록색"),
        Color::Blue => println!("파란색"),
    }

    let msg = Message::Write(String::from("안녕"));
    match msg {
        Message::Quit => println!("종료"),
        Message::Move { x, y } => println!("이동: ({}, {})", x, y),
        Message::Write(text) => println!("메시지: {}", text),
    }

    let mv = Message::Move { x: 10, y: 20 };
    match mv {
        Message::Quit => println!("종료"),
        Message::Move { x, y } => println!("이동: ({}, {})", x, y),
        Message::Write(text) => println!("메시지: {}", text),
    }
}
