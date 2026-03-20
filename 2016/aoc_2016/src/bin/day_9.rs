fn version_one(){
    let file_chars: Vec<char> = std::fs::read_to_string("/Users/2024oliverbindewald/Documents/Code/AOC/2016/Day9/Input.txt").expect("CAnnot read file").chars().collect();
    let mut i = 0;
    let mut decompressed_string: Vec<char> = vec![];
    while i < file_chars.len(){
        if (file_chars[i] as u8) > 64 && (file_chars[i] as u8) < 91{
            decompressed_string.push(file_chars[i]);
        } else if file_chars[i] == '('{
            let mut j = i;
            while file_chars[j] != ')'{
                j = j + 1;
            }
            let dim = file_chars[i+1..j].iter().collect::<String>();
            let dim = dim.split('x').collect::<Vec<&str>>();
            let repeting_str: &str = &file_chars.iter().collect::<String>()[(j+1)..(1+j+dim[0].parse::<usize>().expect("Could not parse"))];
            for _p in 0..dim[1].parse::<usize>().expect("Could not parse"){
                for k in repeting_str.chars(){
                    decompressed_string.push(k);
                }
            }
            i = j+dim[0].parse::<usize>().expect("Could not parse");
            //println!("{:?}", repeting_str.chars().collect::<Vec<char>>());
        }
        i += 1;
    }
    println!("{:?}", decompressed_string.iter().collect::<String>().len());
}
fn version_two(inp: &str) -> u64{
    let file_chars: Vec<char> = inp.chars().collect();
    let mut i = 0;
    let mut decompressed_string: u64 = 0;
    while i < inp.len(){
        if (file_chars[i as usize]) as u8 >= 65 && (file_chars[i as usize]) as u8 <= 90{
            decompressed_string += 1;
            i += 1;
        } else if file_chars[i as usize] == '('{
            let mut j = i;
            while file_chars[j] != ')'{
                j += 1;
            }
            let par_contents = &file_chars[(i+1)..(j)].iter().collect::<String>();
            let par_contents = par_contents.split('x').collect::<Vec<&str>>();
            let repeting_str_len = version_two(&file_chars.iter().collect::<String>()[(j+1)..(1+j+par_contents[0].parse::<usize>().expect("Could not parse"))]);
            decompressed_string += (repeting_str_len as u64)*(par_contents[1].parse::<u64>().expect("Could not parse"));
            i = 1+j+par_contents[0].parse::<usize>().expect("Could not parse");
        }
    }
    decompressed_string
}
fn main() {
    let file_chars: &str = &std::fs::read_to_string("/Users/2024oliverbindewald/Documents/Code/AOC/2016/Day9/Input.txt").expect("CAnnot read file");
    version_one();
    println!("{:?}",version_two(file_chars));
}
    