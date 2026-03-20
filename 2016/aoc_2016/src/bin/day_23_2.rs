fn main() {
    let file_contents = &std::fs::read_to_string("/Users/2024oliverbindewald/Documents/2016/aoc_2016/src/bin/day_23.txt").expect("Could not read");
    let lines: Vec<&str> = file_contents.lines().collect();
    let length = lines.len();
    let mut edit_values: [&str; 26] = ["";26];
    let mut registers: [i32;4] = [12,0,0,0];
    let mut i = 0;
    while i < length{
        let mut line: Vec<&str> = lines[i].split(' ').collect();
        if edit_values[i] != "" {
            line[0] = edit_values[i];
        }
        if i == 4 && registers[3] != 0{
            registers[0] += (registers[1]*registers[3]);
            registers[2] = 0;
            registers[3] = 0;
            i = 10;
        } else if i == 13 && registers[3] != 0{
            registers[2] += registers[3];
            registers[3] = 0;
            i = 16;
        } else if i == 20 && edit_values[20] == "cpy" && edit_values[24] == "dec" && registers[2] != 0{
            registers[0] += (71*registers[2]);
            registers[3] = 0;
            registers[2] = 0;
            i = 27;
        } else {
            println!("{} --- {:?} ----- {:?} ----- {:?}", i, line, registers, edit_values);
            if line[0] == "cpy"{
                if (line[1].chars().nth(0).unwrap() as u8) >= 97{
                    registers[((line[2].chars().nth(0).unwrap() as u8) - 97) as usize] = registers[((line[1].chars().nth(0).unwrap() as u8) - 97) as usize]
                }
                else{
                    registers[((line[2].chars().nth(0).unwrap() as u8) - 97) as usize] = line[1].parse::<i32>().unwrap();
                }
                i += 1;
            } else if line[0] == "inc" {
                registers[((line[1].chars().nth(0).unwrap() as u8) - 97) as usize] += 1;
                i += 1;
            } else if line[0] == "dec" {
                registers[((line[1].chars().nth(0).unwrap() as u8) - 97) as usize] -= 1;
                i += 1;
            } else if line[0] == "jnz" {
                let add: i32;
                if (line[1].chars().nth(0).unwrap() as u8) >= 97 && registers[((line[1].chars().nth(0).unwrap() as u8) - 97) as usize] == 0 || 97 >= (line[1].chars().nth(0).unwrap() as u8)  && line[1].parse::<i32>().unwrap() == 0{
                    add = 1;
                } else {
                    if (line[2].chars().nth(0).unwrap() as u8) >= 97 {
                        add = registers[((line[2].chars().nth(0).unwrap() as u8) - 97) as usize];
                    } else {
                        add = line[2].parse::<i32>().unwrap();
                    }
                }
                let new_i = (i as i32 + add) as usize;
                i = new_i;
            } else if line[0] == "tgl" {
                let toggling_index: i32;
                let mut toggling_line: Vec<&str>;
                if (line[1].chars().nth(0).unwrap() as u8) >= 97{ 
                    toggling_index = registers[((line[1].chars().nth(0).unwrap() as u8) - 97) as usize];
                } else {
                    toggling_index = line[1].parse::<i32>().unwrap();
                }
                if i+(toggling_index as usize) < length{
                    let prefix: &str;
                    let editing_line = lines[i+toggling_index as usize];
                    toggling_line = editing_line.split(' ').collect();
                    if edit_values[i+toggling_index as usize-1] != "" {
                        toggling_line[0] = edit_values[i+toggling_index as usize];
                    }
                        if toggling_line.len() == 2 {
                            if toggling_line[0] == "inc" {prefix = "dec"; i += 1;}
                            else {prefix = "inc"; i += 1}
                        } else {
                            if toggling_line[0] == "jnz" {prefix = "cpy"; i += 1;}
                            else {prefix = "jnz"; i += 1;}
                        }
                        edit_values[i+toggling_index as usize-1] = prefix;
                } else {
                    i += 1;
                }
            }
        }
        }
        
        
    println!("{:?}", registers[0]);
}
