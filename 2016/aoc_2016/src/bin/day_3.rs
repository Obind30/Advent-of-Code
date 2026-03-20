fn part_one(){
    let file_contents = std::fs::read_to_string("/Users/2024oliverbindewald/Documents/Code/AOC/2016/Day3/Input.txt").expect("failed to read file");
    let lines: Vec<Vec<i32>> = file_contents.lines()
        .map(|x| x.split_whitespace().map(|y| y.parse::<i32>().unwrap()).collect())
        .collect();
    let mut sum = 0;
    for i in lines{
        if i[0]+i[1] > i[2] && i[1]+i[2] > i[0] && i[2]+i[0] > i[1]{
            sum += 1;
        }
    }
    println!("{sum}");
}
fn part_two(){
    let file_contents = std::fs::read_to_string("/Users/2024oliverbindewald/Documents/Code/AOC/2016/Day3/Input.txt").expect("failed to read file");
    let lines: Vec<Vec<i32>> = file_contents.lines()
        .map(|x| x.split_whitespace().map(|y| y.parse::<i32>().unwrap()).collect())
        .collect();
    let mut sum = 0;
    for i in 0..(lines.len())/3{
        for j in 0..lines[i].len(){
            if lines[i*3][j]+lines[i*3+1][j] > lines[i*3+2][j] && lines[i*3+1][j]+lines[i*3+2][j] > lines[i*3][j] && lines[i*3+2][j]+lines[i*3][j] > lines[i*3+1][j]{
                sum += 1;
            }
        }
    }
    println!("{sum}");
}
fn main() {  
    part_one();  
    part_two();
}
