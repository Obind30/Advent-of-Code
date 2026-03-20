fn main() {
    let file_contents = std::fs::read_to_string("/Users/2024oliverbindewald/Documents/Code/AOC/2016/Day8/Input.txt").expect("no loser");
    let mut light_array = [['.';50];6];
    for i in file_contents.lines(){
        let line: Vec<&str> = i.split(|x| x == ' ' || x == '='|| x == 'x').collect();
        match line[0]{
            "rect" => {
                for j in 0..line[2].parse::<usize>().expect("Could not parse"){
                    for k in  0..line[1].parse::<usize>().expect("Could not parse"){
                        light_array[j][k] = '#'
                    }
                }
            }
            "rotate" => {
                if line[1] == "row"{
                    let row = light_array[line[3].parse::<usize>().expect("Could not parse")];
                    for j in 0..50{
                        light_array[line[3].parse::<usize>().expect("Could not parse")]
                        [j as usize] 
                        = row[((j-(line[5].parse::<i32>().expect("Could not parse"))+50)%50) as usize];
                    }
                }else if line[1] == "column"{
                    let mut collumn = vec![];
                    for j in 0..6{
                        collumn.push(light_array[j][line[4].parse::<usize>().expect("Could not parse")]);
                    }
                    for j in 0..6{
                        light_array[j as usize][line[4].parse::<usize>().expect("Could not parse")] = collumn[(((j - line[6].parse::<i32>().expect("Could not parse"))+6)%6) as usize];
                    }
                }
            }
            _ => println!("no match found"),
        } 
    }
    let mut light_on = 0;
    for i in light_array{
        for j in i{
            if j == '#'{
                light_on += 1;
            }
        }
        println!("{:?}", i.iter().collect::<String>());
    }
    println!("{:?}", light_on);
}
