fn main()
{
    let starting_position = [1,1];
    //let target_pos = [7,4];
    //let favorite_number = 1352;
    //println!("{}", valid_space([1,1], favorite_number));
    println!("{:?}", bredth_first_search(starting_position, [31,39], vec![], 0));
}
fn bredth_first_search(position: [i32; 2], target: [i32;2], invalid_spaces: Vec<[i32;2]>, moves_made: i32) -> Option<i32>
{
    if position == target
    {
        return Some(moves_made);
    }
    else
    {
        let offsets: [[i32;2];4] = [[0,1],[0,-1], [1,0],[-1,0]];
        let mut valid_moves: Vec<[i32;2]> = Vec::new();
        let mut possible: Vec<i32> = Vec::new();
        let mut inval = invalid_spaces;
        inval.push(position);
        for i in offsets.into_iter()
        {
            let next_position: [i32;2] = [i[0]+position[0], i[1]+position[1]];
            if valid_space(next_position, 1352) && !inval.contains(&next_position) && next_position[0]>=0 && next_position[1]>=0{
                valid_moves.push(next_position);
            }
            else
            {
                inval.push(next_position);
            }
        }
        for i in valid_moves.into_iter()
        {
            let recurs = bredth_first_search(i, target, inval.clone(), moves_made+1);
            if recurs != None {
                possible.push(recurs.unwrap());
            }
        }
        if possible.len() == 0
        {
            return None;
        }
        let mut min = 1000;
        for i in possible.into_iter()
        {
            if i<min
            {
                min = i;
            }
        }
        return Some(min);
    }
}
fn count_set_bits(x: i32) -> i32
{
    let mut n = x;
    let mut count = 0;
    while n !=  0
    {
        n = n & (n-1);
        count += 1;
    }
    count
}
fn valid_space(checking_position: [i32;2], fav_number: i32) -> bool
{
    let step_one = checking_position[0]*checking_position[0] + 3*checking_position[0] + 2*checking_position[0]*checking_position[1] + checking_position[1] + checking_position[1]*checking_position[1]; 
    let step_two = step_one + fav_number;
    let step_three = count_set_bits(step_two)%2;
    if step_three == 0
    {
        return true;
    }
    false
} 