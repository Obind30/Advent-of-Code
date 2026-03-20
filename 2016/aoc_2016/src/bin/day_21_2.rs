use std::fs;

fn main(){
    let now = std::time::Instant::now();

    let mut string: Vec<char> = "fbgdceah".chars().collect();
    let raw_dawggin = fs::read_to_string("/Users/2024oliverbindewald/Documents/2016/aoc_2016/src/bin/day_21.txt").expect("no");
    let raw_dawggin: Vec<&str> = raw_dawggin.lines().collect();
    let mut instructions: Vec<Vec<&str>> = Vec::new();
    for i in raw_dawggin {
        instructions.push(i.split_whitespace().collect::<Vec<&str>>());
    }
    for i in instructions.iter().rev() {
        if i[1] == "position" && i[0] == "swap" {
            let index1 = i[2].parse::<usize>().unwrap();
            let index2 = i[5].parse::<usize>().unwrap();
            let temp: char = string[index1];
            string[index1] = string[index2];
            string[index2] = temp;
        } else if i[1] == "letter"{
            let index1 = string.iter().position(|&x| x == i[2].parse::<char>().unwrap()).unwrap();
            let index2 = string.iter().position(|&x| x == i[5].parse::<char>().unwrap()).unwrap();
            let temp: char = string[index1];
            string[index1] = string[index2];
            string[index2] = temp;
        } else if i[1] == "left" || i[1] == "right" {
            let steps = i[2].parse::<usize>().unwrap();
            let mut new = Vec::new();
            if i[1] == "left"{
                for j in 0..string.len() {
                    new.push(string[(((string.len())*((steps/string.len())+1))-steps+j)%string.len()]);
                }
            } else {
                for j in 0..string.len() {
                    new.push(string[(((string.len())*((steps/string.len())+1))+steps+j)%string.len()]);
                }
            }
            string = new;
        } else if i[1] == "based" {//********
            let p = string.iter().position(|&x| x == i[6].parse::<char>().unwrap()).unwrap();
             let steps;
            if p%2 == 1 || p == 0{
                steps = (p/2)+1;
            } else {
                steps = (p/2)+5;
            }
            let mut new = Vec::new();
            for j in 0..string.len() {
                new.push(string[(((string.len())*((steps/string.len())+1))+steps+j)%string.len()]);
            }
            string = new;
        } else if i[0] == "reverse" {
            let copy = string.clone();
            let low = i[2].parse::<usize>().unwrap();
            let high = i[4].parse::<usize>().unwrap();
            let mut k = high+1;
            for j in low..high+1 {
                k -= 1;
                string[j] = copy[k];
            }
        } else if i[0] == "move" {
            let moveind = i[5].parse::<usize>().unwrap();
            let moveto = i[2].parse::<usize>().unwrap();
            let moved = string[moveind];
            let mut copy = string.clone();
            copy.remove(moveind);
            let mut state = false;
            for i in 0 .. string.len(){
                if i == moveto {
                    state = true;
                    string[i] = moved;
                } else {
                    if state == false {
                        string[i] = copy[i];
                    } else {
                        string[i] = copy[i-1];
                    } 
                } 
            }
        }
    }
    println!("{:?}", string.iter().collect::<String>());
    
    println!("Runtime: {:?}", now.elapsed());
}