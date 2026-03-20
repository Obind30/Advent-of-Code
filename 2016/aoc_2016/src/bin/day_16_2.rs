use std::iter::FromIterator;
fn main() {
    let now = std::time::Instant::now();

    println!("{:?}", checksum(fill_disc(35651584, String::from("10010000000110000"))));

    let elapsed_time = now.elapsed();
    println!("Runtime: {:?}", elapsed_time);
}
fn generate_dragon_curve(n: usize) -> Vec<char> {
    let mut curve: Vec<char> = vec!['0'; n];
    let mut i:f32 = 2.0;
    let mut starting_pos = 2;
    let mut adder = 3;
    while ((n as f32/i).round() as i32 )/2>0{
        //println!("{} {}", n as f32/i, ((n as f32/i).round() as i32)/2);
        for j in 0..((n as f32/i).round() as i32)/2{
            curve[starting_pos+((i as usize)*2*j as usize)] = '1';
        }
        starting_pos += adder;
        adder = adder * 2;
        i = i*2.0;
    } 
    curve
}
fn fill_disc(n: usize, innie: String) -> Vec<char> {
    let mut out: Vec<char> = Vec::new();
    let a: Vec<char> = innie.chars().collect();
    let mut b: Vec<char> = Vec::new();
    for i in a.iter().rev(){
        if i == &'0'{
            b.push('1');
        }else{
            b.push('0');
        }
    }
    let len_ini = a.len();
    let runs = n/(2*(len_ini+1));
    let dragon = generate_dragon_curve(2*(runs+1));
    for i in 0..runs+1{
        out.extend(&a);
        out.push(dragon[i*2]);
        out.extend(&b);
        out.push(dragon[i*2+1]);
    }
    Vec::from_iter(out[0..n].iter().cloned())
    //out//pan down to appropriate size
}
fn checksum(innie: Vec<char>) -> String {
    let mut out = innie;
    while out.len()%2 == 0 {
        let mut temp: Vec<char> = Vec::new();
        for i in  0..out.len()/2 {
            if out[i*2] == out[i*2+1]{
                temp.push('1');
            } else {
                temp.push('0');
            }
        }
        out = temp;
    }
    out.into_iter().collect::<String>()
}