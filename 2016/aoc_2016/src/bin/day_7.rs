fn is_abba(inp: &str) -> bool{
    if inp.len() == 4{
        if inp.chars().nth(0) == inp.chars().nth(3) && inp.chars().nth(1) == inp.chars().nth(2){
            if inp.chars().nth(0) != inp.chars().nth(1){
                return true;
            }
        }
    }
    false
}
fn contains_abba(inp: &str) -> bool{
    if inp.len()<=4{
        return is_abba(&inp);
    }
    for i in 0..inp.len()-3{
        if is_abba(&inp[i..i+4]){
            return true;
        }
    }
    false
}
fn part_one(){
    let file_contents = std::fs::read_to_string("/Users/2024oliverbindewald/Documents/Code/AOC/2016/Day7/Input.txt").expect("failed to read files");
    let mut valid_ids = 0;
    for i in file_contents.lines(){
        let line: Vec<&str> = i.split(|x| x == '[' || x == ']').collect();
        let mut odd = false;
        let mut even = false;
        for j in 0..line.len(){
            if contains_abba(line[j]){
                if j%2 == 0{
                    even = true;
                }else{
                    odd = true;
                }
            }
        }
        if even && !odd{
            valid_ids += 1;
        }
    }
    println!("{:?}", valid_ids);
}
fn detect_aba_bab(line: Vec<&str>) -> (Vec<&str>, Vec<&str>){
    let mut aba: Vec<&str> = vec![];
    let mut bab: Vec<&str> = vec![];
    for i in 0..line.len(){
        let ch: Vec<char> = line[i].chars().collect();
        for j in 1..ch.len()-1{
            if ch[j-1] == ch[j+1] && ch[j] != ch[j+1]{
                if i%2 == 0 {
                    aba.push(&line[i][j-1..j+2]);
                }else{
                    bab.push(&line[i][j-1..j+2]);
                }
            }
        }
    }
    (aba,bab)
}
fn part_two(){
    let file_contents = std::fs::read_to_string("/Users/2024oliverbindewald/Documents/Code/AOC/2016/Day7/Input.txt").expect("failed to read files");
    let mut valid_ids = 0;
    for i in file_contents.lines(){
        let line: Vec<&str> = i.split(|x| x == '[' || x == ']').collect();
        let (aba, bab) = detect_aba_bab(line);
        let mut valid = false;
        for j in aba{
            for k in &bab{
                if j.chars().nth(0) == k.chars().nth(1) && j.chars().nth(1) == k.chars().nth(0){
                    valid = true;
                }
            }
        }
        if valid{
            valid_ids += 1;
        }
        //println!("{:?} {:?}", aba, bab);
    }    
    println!("{:?}", valid_ids);
}
fn main() {    
    part_one();
    part_two();
}