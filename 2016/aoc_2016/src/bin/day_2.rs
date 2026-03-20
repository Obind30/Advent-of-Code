fn read_line_by_line()->Vec<String>{
    use std::fs::File;
    use std::io::BufReader;
    use std::io::prelude::*;
    let mut lines = Vec::new();
    let file = File::open("/Users/2024oliverbindewald/Documents/Code/AOC/2016/Day2/Input.txt")
        .expect("file not found!");
    let  buf_reader = BufReader::new(file);
    for line in buf_reader.lines() {
        lines.push(line.unwrap());
    }
    lines
}
fn manhattan_distance(coord_one: [i32; 2], coord_two: [i32; 2]) -> i32{
    let one = coord_two[0]-coord_one[0];
    let two = coord_two[1]-coord_one[1]; 
    one.abs()+two.abs()
}
fn part_one(){
    let inp = read_line_by_line();
    let mut result = String::new();
    let mut position = [1,1];
    for i in inp{
        for j in i.chars(){
            match j{
                'U' => position[0] -= 1,
                'D' => position[0] += 1,
                'R' => position[1] += 1,
                'L' => position[1] -= 1,
                _ => todo!(),
            }
            if position[0] < 0{
                position[0] = 0;
            } else if position[0]>2{
                position[0] = 2;
            }
            if position[1] < 0{
                position[1] = 0;
            } else if position[1]>2{
                position[1] = 2;
            }
        }
    result = result + format!("{}",position[0]*3+position[1]+1).as_str();
    }
    println!("{}",result);
}
fn part_two(){
    let inp = read_line_by_line();
    let mut result = String::new();
    let keypad = [['n','n','1','n','n'],['n','2','3','4','n'],['5','6','7','8','9'],['n','A','B','C','n'],['n','n','D','n','n']];
    let mut position = [2,0];
    for i in inp{
        for j in i.chars(){
            let mut proposed_pos = position;
            match j{
                'U' => proposed_pos[0] -= 1,
                'D' => proposed_pos[0] += 1,
                'R' => proposed_pos[1] += 1,
                'L' => proposed_pos[1] -= 1,
                _ => todo!(),
            }
            if manhattan_distance(proposed_pos, [2,2])>2{
                proposed_pos = position;
            }
            position = proposed_pos;
        }
    result += format!("{}",(keypad[position[0] as usize][position[1] as usize]).to_string()).as_str();
    }
    println!("{}",result);
}
fn main(){
    part_one();
    part_two();
}