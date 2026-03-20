fn part_one(){
    let file_contents = std::fs::read_to_string("/Users/2024oliverbindewald/Documents/Code/AOC/2016/Day4/Input.txt").expect("failed to read file");
    let lines: Vec<&str> = file_contents.lines().collect();
    let mut valid_codes = 0;
    for i in lines{
        let ind = i.find('[').unwrap();
        let key = &i[ind+1..ind+6];
        let mut actual_key = String::new();
        let mut alaphabet_counts = [0; 26];
        let sect_id: i32 = (&i[i.len()-10..ind]).parse().expect("failed to parse section id");
        for j in i[0..i.len()-11].chars(){
            let uni = (j as i32)-97;
            if uni >= 0{
                alaphabet_counts[uni as usize] += 1;
            }
        }
        let mut max = 0;
        let mut max_ind = 0;
        let mut used = vec![];
        for _j in 0..5{
            for k in 0..alaphabet_counts.len(){
                if alaphabet_counts[k] > max && !used.contains(&k){
                    max = alaphabet_counts[k];
                    max_ind = k;
                }
            }
            used.push(max_ind);
            let to_ut = vec![(max_ind+97) as u8];
            let to_add = String::from_utf8(to_ut).unwrap();
            actual_key = actual_key+&to_add;
            max = 0;
        }
        if key == actual_key{
            valid_codes += sect_id; 
        }
    }
    println!("{}",valid_codes);
}
fn part_two(){
    let file_contents = std::fs::read_to_string("/Users/2024oliverbindewald/Documents/Code/AOC/2016/Day4/Input.txt").expect("failed to read file");
    let lines: Vec<&str> = file_contents.lines().collect();
    let mut valid_codes = vec![];
    for i in lines{
        let ind = i.find('[').unwrap();
        let key = &i[ind+1..ind+6];
        let mut actual_key = String::new();
        let mut alaphabet_counts = [0; 26];
        for j in i[0..i.len()-11].chars(){
            let uni = (j as i32)-97;
            if uni >= 0{
                alaphabet_counts[uni as usize] += 1;
            }
        }
        let mut max = 0;
        let mut max_ind = 0;
        let mut used = vec![];
        for _j in 0..5{
            for k in 0..alaphabet_counts.len(){
                if alaphabet_counts[k] > max && !used.contains(&k){
                    max = alaphabet_counts[k];
                    max_ind = k;
                }
            }
            used.push(max_ind);
            let to_ut = vec![(max_ind+97) as u8];
            let to_add = String::from_utf8(to_ut).unwrap();
            actual_key = actual_key+&to_add;
            max = 0;
        }
        if key == actual_key{
            valid_codes.push(&i[0..ind]); 
        }
    }
    for i in valid_codes{
        let key = &i[i.len()-3..i.len()].parse::<i32>().unwrap();
        let mut new_code = String::new();
        for j in i[0..i.len()-4].chars(){
            if j == '-'{
                new_code = new_code + " ";
            } else {
                let shifted_character = vec![((((j as i32) - 97 + key) % 26)+97) as u8];
                //println!("{}", String::from_utf8(shifted_character).unwrap());
                new_code = new_code + String::from_utf8(shifted_character).unwrap().as_str();
            }
        }
        if new_code == "northpole object storage"{
            println!("{}", key);
        }
    }
}
fn main() {
    part_one();
    part_two();
}