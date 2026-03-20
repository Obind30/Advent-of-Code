extern crate queues;
use queues::*;

fn main() {
    let file_contents = &std::fs::read_to_string("/Users/2024oliverbindewald/Documents/2016/aoc_2016/src/bin/day_24.txt").expect("Could not read");
    let map: Vec<Vec<char>> = file_contents.lines().map(|x| x.chars().collect()).collect();
    const N: usize = 8;

    let mut locations: [[i32;2];N] = [[-1;2];N];
    for i in 0..map.len(){ 
        for j in 0..map[0].len() { 
            if map[i][j] as u8 > 47 { locations[(map[i][j] as u8 - 48) as usize] = [i as i32,j as i32]; }
        }
    }

    let mut adjacency_matrix: [[i32;N];N] = [[-1;N];N];
    for i in 0..N {
        for j in 0..N {
            adjacency_matrix[i][j] = bfs(locations[i],locations[j],map.clone());
        }
    }
    let combos = generate_combinations(Vec::new(), Vec::from_iter(1..N as i32));
    let mut min = 1000;
    for i in combos {
        let mut last: usize = 0;
        let mut sum = 0;
        for j in 0..N-1 {
            sum += adjacency_matrix[last][i[j] as usize];
            last = i[j] as usize;
        }
        sum += adjacency_matrix[last][0];
        if min > sum { min = sum; }
    }
    println!("{}", min);
}
fn bfs(s: [i32; 2], e: [i32;2], map: Vec<Vec<char>>) -> i32{
    const WIDTH: usize = 179;
    const HEIGHT: usize = 39;
    let mut q: Queue<[i32; 2]> = queue![];
    q.add(s);
    let neighbors = [[-1,0], [1,0], [0,-1], [0,1]];

    let mut visited: [[bool; WIDTH]; HEIGHT] = [[false; WIDTH];HEIGHT];
    visited[s[0] as usize][s[1] as usize] = true;

    for i in 0..HEIGHT {
        for j in 0..WIDTH { if map[i][j] == '#' { visited[i][j] = true; } }
    }
    
    let mut in_queue = 1;
    let mut next_q = 0;
    let mut total_moves = 0;

    while q.size() > 0 {
        let node = q.remove().unwrap();
        if node == e {return total_moves}
        in_queue -= 1;
        for i in 0..4 {
            let neighbor = [node[0]+neighbors[i][0], node[1]+neighbors[i][1]];
            if visited[neighbor[0] as usize][neighbor[1] as usize] == false {
                q.add(neighbor);
                next_q += 1;
                visited[neighbor[0] as usize][neighbor[1] as usize] = true;
            }
        }
        if in_queue == 0 {total_moves += 1; in_queue = next_q; next_q = 0;}
    }
    -1
}
fn generate_combinations(hist: Vec<i32>, data: Vec<i32>) -> Vec<Vec<i32>> {
    if hist.len() == data.len() {
        return vec![hist]
    }
    let mut out: Vec<Vec<i32>> = vec![vec![]];
    for i in 0..data.len() {
        if !hist.contains(&data[i]) {
            let mut next = hist.clone();
            next.push(data[i]);
            out.append(&mut generate_combinations(next, data.clone()))
        }
    }
    out.remove(0);
    out
}