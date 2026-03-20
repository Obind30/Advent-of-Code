fn main() {
    let file_contents = &std::fs::read_to_string("/Users/2024oliverbindewald/Documents/Code/AOC/2016/aoc_2016/src/bin/day_25.txt").expect("Could not read");
    let lines: Vec<&str> = file_contents.lines().collect();
    let mut k = 0;
    while true {
        let mut registers: [i32;4] = [k,0,0,0];
        let mut i = 0;
        let mut o = 0;
        let mut out: Vec<i32> = Vec::new();
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
            } else if line[0] == "jnz" {
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
                } else if line[0] == "out" {
                        o += 1;
                        out.push(registers[0]);
                        if registers[0] == 0 {println!("{:?}", k);}
                        i += 1;
                        if o == 1 {i = lines.len()}
                }
        }
        //println!("{:?}    {:?}", k, out);
        k += 1;
    }
}
