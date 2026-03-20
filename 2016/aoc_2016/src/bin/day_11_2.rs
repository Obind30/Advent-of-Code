extern crate queues;
use queues::*;

const N: usize = 7;
//const N: usize = 2;

fn main () {
    let overall:[i32;2*N+1] = [1,1,2,2,2,2,1,1,1,3,3,3,3,1,1];
    //let overall:[i32;2*N+1] = [1,2,3,1,1];
    println!("{:?}", bfs(overall, [4;2*N+1]));
    //println!("{:?}", generate_next_positions(overall, -1, [0,0,0,0,0]));
}
fn bfs(initial_position: [i32;2*N+1], goal_pos: [i32;2*N+1]) -> i32 {
    let mut q: Queue<[i32;2*N+1]> = queue![];
    let mut visited: Vec<[i32;2*N+1]> = Vec::new();
    q.add(initial_position);
    visited.push(initial_position);

    let mut in_queue = 1;
    let mut next_q = 0;
    let mut total_moves = 0;

    while q.size() > 0 {
        let node = q.remove().unwrap();
        if node == goal_pos {return total_moves}
        in_queue -= 1;
        let mut pushing = Vec::new();
        if node[0] > 1 { pushing.append(&mut generate_next_positions(node.clone(), -1)); }
        if node[0] < 4 { pushing.append(&mut generate_next_positions(node.clone(), 1)); }
        for i in 0..pushing.len() {
            if !any_equ(visited.clone(), pushing[i]) {
                q.add(pushing[i]);
                next_q += 1;
                visited.push(pushing[i]);
            }
        }
        if in_queue == 0 {total_moves += 1; in_queue = next_q; next_q = 0;}
     }
     -1
}
fn generate_next_positions(initial: [i32;2*N+1], direction: i32) -> Vec<[i32;2*N+1]> {
    //ones
    let mut moves: Vec<[i32;2*N+1]> = Vec::new();
    for i in 1..2*N+1 {
        if initial[i] == initial[0] {
            let mut toop = initial.clone();
            toop[i] += direction;
            toop[0] += direction;
            moves.push(toop);
        }
    }
    //twos
    for i in 1..(2*N) {
        if initial[i] == initial[0] {
            for j in i+1..2*N+1 {
                if initial[j] == initial[0] {
                    let mut toop = initial.clone();
                    toop[i] += direction;
                    toop[j] += direction;
                    toop[0] += direction;
                    moves.push(toop);
                }
            }
        }
    }
    //parse down options no exploding microchips
    for i in (0..moves.len()).rev() {
        'pop: for j in N+1..N*2+1 {
            if moves[i][j] != moves[i][j-N] {
                for k in 1..N+1 {
                    if moves[i][k] == moves[i][j] {
                        moves.remove(i);
                        break 'pop;
                    }
                }
            }
        }
    }
    for i in (1..moves.len()).rev() {
        'pop: for j in 0..i {
            if is_equavilant(moves[i], moves[j]) {
                moves.remove(i);
                break 'pop;
            }
        }
    }
    moves
}
fn is_equavilant(a: [i32;2*N+1], b: [i32;2*N+1]) -> bool {
    if a[0] != b[0] {return false}
    let mut used_indicies: Vec<usize> = Vec::new();
    'wam: for i in 1..N+1 {
        for j in 1..N+1 {
            if !used_indicies.contains(&j) && a[i] == b[j] && a[i+N] == b[j+N] {
                used_indicies.push(j);
                continue 'wam
            }
        }
        return false
    }
    true
}
fn any_equ(lis: Vec<[i32;2*N+1]>, look: [i32;2*N+1]) -> bool {
    for i in lis {
        if is_equavilant(look, i) {return true}
    }
    false
}