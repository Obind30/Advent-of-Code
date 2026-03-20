fn part_one(){
    let file_contents: &str = &std::fs::read_to_string("/Users/2024oliverbindewald/Documents/Code/AOC/2016/Day10/Input.txt").expect("CAnnot read file");
    let lines: Vec<&str> = file_contents.lines().collect();
    let mut bot_inventories = [[0;2];210];
    let mut i = 0;
    let mut run = false;
    loop{
        let line: Vec<&str> = lines[i].split(' ').collect();
        if line[0] == "value" && !run{
            if bot_inventories[line[5].parse::<usize>().unwrap()][0] == 0{
                bot_inventories[line[5].parse::<usize>().unwrap()][0] = line[1].parse::<i32>().unwrap();
            } else if bot_inventories[line[5].parse::<usize>().unwrap()][1] == 0{
                bot_inventories[line[5].parse::<usize>().unwrap()][1] = line[1].parse::<i32>().unwrap();
            }
        } else if line[0] == "bot"{
            let bot_id = line[1].parse::<usize>().unwrap();
            if bot_inventories[bot_id].iter().position(|x| *x == 0) == None{
                if bot_inventories[bot_id] == [17,61] || bot_inventories[bot_id] == [61,17]{//if bot_inventories[bot_id] == [5,2] || bot_inventories[bot_id] == [2,5]{
                    println!("{:?}", bot_id);
                    break;
                }
                if bot_inventories[bot_id][0] < bot_inventories[bot_id][1]{
                    let low_go = bot_inventories[line[6].parse::<usize>().unwrap()].iter().position(|x| *x==0);
                    let high_go = bot_inventories[line[11].parse::<usize>().unwrap()].iter().position(|x| *x==0);
                    if low_go != None && line[5] != "output"{
                        bot_inventories[line[6].parse::<usize>().unwrap()][low_go.unwrap()] = bot_inventories[bot_id][0];
                    }
                    if high_go != None && line[10] != "output"{
                        bot_inventories[line[11].parse::<usize>().unwrap()][high_go.unwrap()] = bot_inventories[bot_id][1];
                    }
                    bot_inventories[bot_id] = [0,0];
                } else{
                    let low_go = bot_inventories[line[6].parse::<usize>().unwrap()].iter().position(|x| *x==0);
                    let high_go = bot_inventories[line[11].parse::<usize>().unwrap()].iter().position(|x| *x==0);
                    if low_go != None && line[5] != "output"{
                        bot_inventories[line[6].parse::<usize>().unwrap()][low_go.unwrap()] = bot_inventories[bot_id][1];
                    }
                    if high_go != None && line[10] != "output"{
                        bot_inventories[line[11].parse::<usize>().unwrap()][high_go.unwrap()] = bot_inventories[bot_id][0];
                    }
                    bot_inventories[bot_id] = [0,0];
                }
            } 
        }
        i = (i+1)%(lines.len());
        if i == 0{
            run = true;
        }
    }
}
fn part_two(){
    let file_contents: &str = &std::fs::read_to_string("/Users/2024oliverbindewald/Documents/Code/AOC/2016/Day10/Input.txt").expect("CAnnot read file");
    let lines: Vec<&str> = file_contents.lines().collect();
    let mut bot_inventories = [[0;2];210];//[[0;2];5];//
    let mut i = 0;
    let mut run = false;
    let mut lines_run = 0;
    let mut outputs = [0,0,0];
    loop{
        let line: Vec<&str> = lines[i].split(' ').collect();
        if line[0] == "value" && !run{
            if bot_inventories[line[5].parse::<usize>().unwrap()][0] == 0{
                bot_inventories[line[5].parse::<usize>().unwrap()][0] = line[1].parse::<i32>().unwrap();
            } else if bot_inventories[line[5].parse::<usize>().unwrap()][1] == 0{
                bot_inventories[line[5].parse::<usize>().unwrap()][1] = line[1].parse::<i32>().unwrap();
            }
            lines_run += 1;
        } else if line[0] == "bot"{
            let bot_id = line[1].parse::<usize>().unwrap();
            if bot_inventories[bot_id].iter().position(|x| *x == 0) == None{
                if bot_inventories[bot_id][0] < bot_inventories[bot_id][1]{
                    let low_go = bot_inventories[line[6].parse::<usize>().unwrap()].iter().position(|x| *x==0);
                    let high_go = bot_inventories[line[11].parse::<usize>().unwrap()].iter().position(|x| *x==0);
                    if line[5] != "output"{
                        bot_inventories[line[6].parse::<usize>().unwrap()][low_go.unwrap()] = bot_inventories[bot_id][0];
                    } else if line[6].parse::<i32>().unwrap() <= 2{
                        outputs[line[6].parse::<usize>().unwrap()] = bot_inventories[bot_id][0];
                    }
                    if line[10] != "output"{
                        bot_inventories[line[11].parse::<usize>().unwrap()][high_go.unwrap()] = bot_inventories[bot_id][1];
                    } else if line[11].parse::<i32>().unwrap() <= 2{
                        outputs[line[11].parse::<usize>().unwrap()] = bot_inventories[bot_id][1];
                    }
                    bot_inventories[bot_id] = [0,0];
                    lines_run += 1;
                } else{
                    let low_go = bot_inventories[line[6].parse::<usize>().unwrap()].iter().position(|x| *x==0);
                    let high_go = bot_inventories[line[11].parse::<usize>().unwrap()].iter().position(|x| *x==0);
                    if line[5] != "output"{
                        bot_inventories[line[6].parse::<usize>().unwrap()][low_go.unwrap()] = bot_inventories[bot_id][1];
                    }else if line[6].parse::<i32>().unwrap() <= 2{
                        outputs[line[6].parse::<usize>().unwrap()] = bot_inventories[bot_id][1];
                    }
                    if line[10] != "output"{
                        bot_inventories[line[11].parse::<usize>().unwrap()][high_go.unwrap()] = bot_inventories[bot_id][0];
                    } else if line[11].parse::<i32>().unwrap() <= 2{
                        outputs[line[11].parse::<usize>().unwrap()] = bot_inventories[bot_id][0];
                    }
                    bot_inventories[bot_id] = [0,0];
                    lines_run += 1;
                }
            } 
        }
        i = (i+1)%(lines.len());
        if lines_run == lines.len(){
            break;
        }
        if i == 0{
            run = true;
        }
    }
    println!("{:?}", outputs[0]*outputs[1]*outputs[2]);
}
fn main() {
    part_one();
    part_two();
}