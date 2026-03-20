fn part_one(){
    let file_contents = std::fs::read_to_string("/Users/2024oliverbindewald/Documents/Code/AOC/2016/Day6/Input.txt").expect("failed to read file");
    let lines: Vec<&str> = file_contents.lines().collect();
    let mut alphabet_counts = [[0;26];8];
    for i in 0..lines.len(){
        let chrs: Vec<char> = lines[i].chars().collect();
        for j in 0..chrs.len(){
            alphabet_counts[j][((chrs[j] as u8)-97) as usize] += 1;
        }
    }
    let mut code = String::new();
    for i in alphabet_counts{
        let mut max = 0;
        let mut max_ind = 0;
        for j in 0..i.len(){
            if i[j] > max{
                max = i[j];
                max_ind = j;
            }
        }
        let next_letter = String::from_utf8(vec![(max_ind+97) as u8]).unwrap();
        code = code + &next_letter;
    }
    println!("{:?}", code);
}
fn part_two(){
    let file_contents = std::fs::read_to_string("/Users/2024oliverbindewald/Documents/Code/AOC/2016/Day6/Input.txt").expect("failed to read file");
    let lines: Vec<&str> = file_contents.lines().collect();
    let mut alphabet_counts = [[0;26];8];
    for i in 0..lines.len(){
        let chrs: Vec<char> = lines[i].chars().collect();
        for j in 0..chrs.len(){
            alphabet_counts[j][((chrs[j] as u8)-97) as usize] += 1;
        }
    }
    let mut code = String::new();
    for i in alphabet_counts{
        let mut min = lines.len();
        let mut min_ind = 0;
        for j in 0..i.len(){
            if i[j] < min{
                min = i[j];
                min_ind = j;
            }
        }
        let next_letter = String::from_utf8(vec![(min_ind+97) as u8]).unwrap();
        code = code + &next_letter;
    }
    println!("{:?}", code); 
}
fn main() {
    part_one();
    part_two();
}
