fn main() {
    let now = std::time::Instant::now();

    println!("{}", bfs([0,0], String::new(), [3,3], "mmsxrhfx".to_string()).len());

    let elapsed_time = now.elapsed();
    println!("Runtime: {:?}", elapsed_time);
}
fn bfs(current_pos: [i8;2], moves_made: String, target: [i8;2], base_string: String) -> String {
    let offsets:[[i8;2];4] = [[0,-1],[0,1],[-1,0],[1,0]];
    let moves: [char;4] = ['U','D','L','R'];
    let hash: String = format!("{:X}", md5::compute(format!("{}{}", base_string, moves_made)));
    let mut possible: Vec<String> = Vec::new();
    if current_pos == target {
        return moves_made
    }
    for i in 0..4 {
        let hash_index: u32 = hash.chars().nth(i).unwrap() as u32;
        let next_pos: [i8;2] = [current_pos[0]+offsets[i][0], current_pos[1]+offsets[i][1]];
        if hash_index > 65 && hash_index < 71 && next_pos[0] > -1 && next_pos[0] < 4 && next_pos[1] > -1 && next_pos[1] < 4{
            let result = bfs(next_pos, format!("{}{}",moves_made, moves[i]), target, base_string.clone());
            if result != String::new(){
                possible.push(result);
            }
        }
    }
    let mut max = 0;
    let mut out = String::new();
    for i in possible{
        let length = i.len();
        if length>max{
            out = i;
            max = length;
        }
    }
    out
}