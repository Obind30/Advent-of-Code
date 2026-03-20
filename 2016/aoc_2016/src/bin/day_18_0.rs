use std::fs;
fn main(){
    let now = std::time::Instant::now();

    let rows = 400000;
    
    let mut current_row: Vec<char> = fs::read_to_string("/Users/2024oliverbindewald/Documents/2016/aoc_2016/src/bin/day_18.txt").expect("no")
    .chars().collect();
    let row_width = current_row.len();
    let mut new_row: Vec<char> = Vec::new();
    let mut safe: u32 = 0;
    for i in &current_row{
        if i == &'.' {
            safe += 1;
        }
    }
    for i in 0..(rows-1) {
        for i in 0..row_width {
            if i == 0 {
                if current_row[i+1] == '^'{
                    new_row.push('^');
                } else {
                    new_row.push('.');
                    safe += 1;
                }
            } else if i == row_width-1 {
                if current_row[i-1] == '^'{
                    new_row.push('^');
                } else {
                    new_row.push('.');
                    safe += 1;
                }
            }
            else{
                if current_row[i-1] != current_row[i+1] {
                    new_row.push('^');
                } else {
                    new_row.push('.');
                    safe += 1;
                }
            }
        }
        current_row = new_row;
        new_row = Vec::new();
    }
    
    println!("{}", safe);

    let elapsed_time = now.elapsed();
    println!("Runtime: {:?}", elapsed_time);
}