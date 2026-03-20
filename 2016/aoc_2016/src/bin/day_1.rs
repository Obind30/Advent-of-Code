fn part_one() {
    use std::fs;
    let input = fs::read_to_string("/Users/2024oliverbindewald/Documents/Code/AOC/2016/Day1/Input.txt")
        .expect("LogRocket: Should have been able to read the file");
    let input = input.split(", ");
    let mut direction_instrictions = Vec::new();
    let mut instruction_length = Vec::new();
    for i in input {
        let first_char = i.chars().next().unwrap();
        let ints = &i[1..];
        let ints: i32 = ints.parse().unwrap();
        instruction_length.push(ints);
        direction_instrictions.push(first_char);
    }
    let directions = [[0,1],[1,0],[0,-1],[-1,0]];
    let mut current_direction: i32 = 0;
    let mut position = [0,0];
    for i in 0..direction_instrictions.len(){
        if direction_instrictions[i] == 'R'{
            current_direction += 1;
        }
        else if direction_instrictions[i] == 'L'{
            current_direction -= 1;
        }
        if current_direction > 3{
            current_direction = 0;
        }
        if current_direction < 0{
            current_direction = 3;
        }
        let current_direction: usize = current_direction.try_into().unwrap(); 
        position[0] = directions[current_direction][0]*instruction_length[i]+position[0];
        position[1] = directions[current_direction][1]*instruction_length[i]+position[1];
    }
    println!("{}",position[0]+position[1])
}
fn part_two() -> [i32; 2]{
    use std::fs;
    let input = fs::read_to_string("/Users/2024oliverbindewald/Documents/Code/AOC/2016/Day1/Input.txt")
        .expect("LogRocket: Should have been able to read the file");
    let input = input.split(", ");
    let mut direction_instrictions = Vec::new();
    let mut instruction_length = Vec::new();
    for i in input {
        let first_char = i.chars().next().unwrap();
        let ints = &i[1..];
        let ints: i32 = ints.parse().unwrap();
        instruction_length.push(ints);
        direction_instrictions.push(first_char);
    }
    let directions = [[0,1],[1,0],[0,-1],[-1,0]];
    let mut visited = Vec::new();
    let mut current_direction: i32 = 0;
    let mut position = [0,0];
    for i in 0..direction_instrictions.len(){
        if direction_instrictions[i] == 'R'{
            current_direction += 1;
        }
        else if direction_instrictions[i] == 'L'{
            current_direction -= 1;
        }
        if current_direction > 3{
            current_direction = 0;
        }
        if current_direction < 0{
            current_direction = 3;
        }
        let current_direction: usize = current_direction.try_into().unwrap(); 
        for _j in 0..instruction_length[i]{
            position[0] = directions[current_direction][0]+position[0];
            position[1] = directions[current_direction][1]+position[1];
            if visited.contains(&position){
                return position;
            }
            visited.push(position);
        }
    }
    //for i in visited{
    //    println!("{:?}",i);
    //}
    position
}
fn main() {
    //part_one();
    println!("{:?}", part_two());
}