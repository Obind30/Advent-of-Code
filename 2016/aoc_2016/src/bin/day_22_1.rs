use std::fs;

fn main() {
    let now = std::time::Instant::now();
    let raw_dawggin = fs::read_to_string("/Users/2024oliverbindewald/Documents/2016/aoc_2016/src/bin/day_22.txt").expect("no");
    let mut raw_dawggin: Vec<&str> = raw_dawggin.lines().collect();
    raw_dawggin.remove(0);
    raw_dawggin.remove(0);
    let mut used: Vec<u32> = Vec::new();
    let mut available: Vec<u32> = Vec::new();
    for i in raw_dawggin {
        let split = i.split_whitespace().collect::<Vec<&str>>();
        used.push(split[2][0..split[2].len()-1].to_string().parse::<u32>().unwrap());
        available.push(split[3][0..split[3].len()-1].to_string().parse::<u32>().unwrap());
    }

    let mut count = 0;
    for i in 0..used.len() {
        for j in 0..available.len() {
            if used[i] <= available[j] && used[i] != 0 && i != j {
                count += 1;
            }
        }
    }
    println!("{}", count);
    

    println!("Runtime: {:?}", now.elapsed());
}