fn main() {
    let now = std::time::Instant::now();

    let starting_code: String = String::from("10010000000110000");
    let length: usize = 272;
    let mut checksum: String = generate_checksum(fill_disc(starting_code, length));
    while checksum.len()%2 == 0 {
        checksum = generate_checksum(checksum);
    }
    println!("{}", checksum);
    //assert_eq!(fill_disc(String::from("1011"), 19), String::from("1011000100101110010"));
    //println!("{}", fill_disc(String::from("0"), 50));

    let elapsed_time = now.elapsed();
    println!("Runtime: {:?}", elapsed_time);
}
fn step_up(inp: String) -> String {
    let a: &str = &inp;
    let mut b: String = String::new();
    for i in inp.chars().rev(){
        if i == '0'{
            b.push('1');
        }else{
            b.push('0');
        }
    }
    format!("{}{}{}", a, '0', b)
}
fn fill_disc(inp: String, disc_size: usize) -> String{
    let mut working = inp;
    while working.len()<disc_size{
        working = step_up(working);
    }
    String::from(&working[0..disc_size])
}
fn generate_checksum(disc: String) -> String{
    let mut out: String = String::new();
    for i in 0..disc.len()/2{
        out = format!("{}{}", out, ((disc.as_str().chars().nth(i*2).unwrap() == disc.as_str().chars().nth(i*2+1).unwrap()) as i8).to_string());
    }
    out
}