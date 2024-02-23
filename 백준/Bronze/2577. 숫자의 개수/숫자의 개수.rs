use std::io::stdin;

fn main() {
    let mut result = 1;
    for _ in 0..3{
        let mut input = String::new();
        stdin().read_line(&mut input).expect(" 1");
        let n: i32 = input.trim().parse().expect("Error");
        result = n * result;
    }
    // println!("{result}");

    let mut vec_result = vec![0;10];

    while result > 0 {
        let num =( result%10) as usize;
        result /= 10;

        vec_result[num] += 1;

    }
    for i in &vec_result{
        println!("{i}");
    }
}
