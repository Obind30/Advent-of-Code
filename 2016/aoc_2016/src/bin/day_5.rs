use md5::{Md5, Digest};
use hex::ToHex;
fn md5_hash(inp: &str)-> String{
    let mut hasher = Md5::new();
    hasher.update(inp);
    let result = hasher.finalize();
    let out = result.encode_hex::<String>();
    out
}
fn part_one(){
    let inp = "uqwqemis";
    let mut password = String::new();
    let mut i = 0;
    while password.len()<8{
        let new = inp.to_owned() + &i.to_string();
        let hash = md5_hash(&new);
        if hash[0..5] == "00000"[..]{
            password = password + &hash.chars().nth(5).unwrap().to_string();
        }
        //println!("{:?}",i);
        i += 1;
    }
    println!("{}",password);
}
fn part_two(){
    let inp = "uqwqemis";
    let mut password = [' ';8];
    let mut i = 0;
    let mut added = 0;
    while added<8{
        let new = inp.to_owned() + &i.to_string();
        let hash = md5_hash(&new);
        //println!("{:?}", hash);
        if hash[0..5] == "00000"[..]{
            //password = password + &hash.chars().nth(5).unwrap().to_string();
            if (hash.chars().nth(5).unwrap() as u8) < 97{
                let insert_index = hash.chars().nth(5).unwrap().to_digit(10).unwrap();
                if insert_index<8{
                    if password[insert_index as usize] == ' ' {
                        password[insert_index as usize] = hash.chars().nth(6).unwrap();
                        added += 1;
                    }
                }
            }
        }
        i += 1;
    }
    println!("{:?}",password);
}
fn main(){
    part_one();
    part_two();
}