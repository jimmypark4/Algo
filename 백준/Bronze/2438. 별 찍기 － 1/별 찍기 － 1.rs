use std::io::stdin;

fn main() {
    let mut input = String::new();
    stdin().read_line(&mut input).expect(" 1");

    let n: i32 = input.trim().parse().expect("Error");
    for i in 1..(n+1){
        for j in  0..i{
            print!("*");
        }
        println!("");
    }


}
