fn main() {
    const SALT: &str = "ahsbgdzn";
    let mut index: u32 = 0;
    let mut hashes: Vec<Vec<char>> = Vec::new();
    let mut keys: u32 = 0;
    let mut last_key: u32 = 0;
    for i in 0..1001 {hashes.push(search_quint(stretch(format!("{}{}",SALT,i)))); }
    while keys < 64 {
        let trip = hashes[0][0];
        if trip != '*' {
            'search_q: for i in 1..1001 {
                for k in 1..hashes[i].len() {
                    if hashes[i][k] == trip {
                        keys += 1;
                        last_key = index;
                        println!("{:?}", index);
                        break 'search_q;
                    }
                }
            }
        }
        hashes.remove(0);
        index += 1;
        hashes.push(search_quint(stretch(format!("{}{}",SALT,index+1001))));   
    }
    println!("{}", last_key);
}
fn stretch(inp: String) -> String {
    let mut md = format!("{:X}", md5::compute(inp)).to_lowercase();
    for i in 0..2016 {
        md = format!("{:X}", md5::compute(md)).to_lowercase();
    }
    md
}
fn search_quint(inp: String) -> Vec<char> {
    let mut out: Vec<char> = Vec::new();
    let chars: Vec<char> = inp.chars().collect();
    out.push(search_tripolets(inp.clone()));
    for i in 0..inp.len()-4 {
        if chars[i..i+5] == [chars[i];5] {
            out.push(chars[i]);
        }
    }
    out.push('-');
    out
}
fn search_tripolets(inp: String) -> char {
    let mut out = '*';
    let chars: Vec<char> = inp.chars().collect();
    for i in 0..inp.len()-2 {
        if chars[i..i+3] == [chars[i];3] { out = chars[i]; break;}
    }
    out
}