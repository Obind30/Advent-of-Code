fn main() {
    let file_contents = &std::fs::read_to_string("/Users/2024oliverbindewald/Documents/Code/AOC/2016/Day12/Input.txt").expect("Could not read");
    let lines: Vec<&str> = file_contents.lines().collect();
    let mut registers: [i32;4] = [0,0,1,0];
    let mut i = 0;
    while i < lines.len(){
        let line: Vec<&str> = lines[i].split(' ').collect();
        if line[0] == "cpy"{
            if (line[1].chars().nth(0).unwrap() as u8) >= 97{
                registers[((line[2].chars().nth(0).unwrap() as u8) - 97) as usize] = registers[((line[1].chars().nth(0).unwrap() as u8) - 97) as usize]
            }
            else{
                registers[((line[2].chars().nth(0).unwrap() as u8) - 97) as usize] = line[1].parse::<i32>().unwrap();
            }
            i += 1;
        }else if line[0] == "inc" {
            registers[((line[1].chars().nth(0).unwrap() as u8) - 97) as usize] += 1;
            i += 1;
        }else if line[0] == "dec" {
            registers[((line[1].chars().nth(0).unwrap() as u8) - 97) as usize] -= 1;
            i += 1;
        }
       else if line[0] == "jnz" {
            let add: i32;
            if (line[1].chars().nth(0).unwrap() as u8) >= 97{
                if registers[((line[1].chars().nth(0).unwrap() as u8) - 97) as usize] != 0{
                    add = line[2].parse::<i32>().unwrap();
                }
                else{
                    add = 1;
                }
            }
            else{
                if line[1].parse::<i32>().unwrap() != 0{
                    add = line[2].parse::<i32>().unwrap();
                }
                else{
                    add = 1;
                }
            }
            let mut new_i = (i as i32 + add) as usize;
            i = new_i;
       }
    }
    println!("{:?}", registers[0]);
}
