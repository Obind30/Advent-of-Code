use std::fs;
extern crate queues;
use queues::*;

fn main() {
    let now = std::time::Instant::now();
    let raw_dawggin = fs::read_to_string("/Users/2024oliverbindewald/Documents/2016/aoc_2016/src/bin/day_22.txt").expect("no");
    let mut raw_dawggin: Vec<&str> = raw_dawggin.lines().collect();
    const grid_size: usize = 925; //925
    raw_dawggin.remove(0);
    raw_dawggin.remove(0);

    let mut nodes: [[i32;3];grid_size] = [[-1;3];grid_size];
    for i in 0..grid_size {
        let split = raw_dawggin[i].split_whitespace().collect::<Vec<&str>>();
        for j in 1..4 {
            nodes[i][j-1] = split[j][0..split[j].len()-1].to_string().parse::<i32>().unwrap();
        }
        //println!("{:?}", nodes[i]);
    }

    let mut empty: i32 = -1;
    let mut st: i32 = -1;

    for i in 0..grid_size {
        if i%25 == 0{
            print!("\n");
        }
        if nodes[i][1] == 0 {
            empty = i as i32;
            print!(" - ");
        } else if i == 900 {
            st = i as i32;
            print!(" G ");
        } else if i == 0 {
            print!("(.)");
        } else if nodes[i][0] < 150 {
            print!(" . ");
        } else {
            print!(" # ");
        }
    }
    print!("\n");

    fn solve(s: i32, nodes:[[i32;3];grid_size], avoid: i32) -> [i32;grid_size] {
        let mut q: Queue<i32> = queue![];
        q.add(s);

        let mut visited: [bool; grid_size] = [false; grid_size];
        visited[s as usize] = true;
        for i in 0..grid_size {
            if nodes[i][0] >= 150 { visited[i] = true; }
        }

        let mut prev: [i32;grid_size] = [-1;grid_size];
        while q.size() > 0 {
            let node = q.remove().unwrap(); 

            let mut neighbors: [i32;4] = [-1;4];

            let x = node/25;
            let y = node%25;
            if x<36 { neighbors[0] = (x+1)*25 + y; }
            if x>0 { neighbors[1] = (x-1)*25 + y; }
            if y<24 { neighbors[2] = x*25 + y+1; }
            if y>0 {neighbors[3] = x*25 + y-1; }
            for next in neighbors {
                if next != -1 && next != avoid && !visited[next as usize]  {
                    q.add(next);
                    visited[next as usize] = true;
                    prev[next as usize] = node;
                }
            }
        }
        prev
    }
    fn reconstruct_path (s: i32, e: i32, prev: [i32; grid_size]) -> Vec<i32> {
        let mut path: Vec<i32> = Vec::new();
        let mut at = e;
        while at != -1 {
            path.push(at);
            at = prev[at as usize];
        }
        path.reverse();
        if path[0] == s {
            return path
        }
        Vec::<i32>::new()
    }
    fn bfs(s: i32, e: i32, nodes:[[i32;3];grid_size], avoid: i32) -> Vec<i32> {
        reconstruct_path(s,e,solve(s, nodes, avoid))
    }

    let path = bfs(900,0,nodes, -1);
    let mut total_distance = 0;
    for i in 1..path.len() {
        total_distance += bfs(empty, path[i], nodes, st).len();
        println!("{:?}", bfs(empty, path[i], nodes, st).len());
        empty = st;
        st = path[i]; 
    }
    println!("{:?}", total_distance);

    println!("Runtime: {:?}", now.elapsed());
}