use std::fs;

fn main(){
    let now = std::time::Instant::now();

    let raw_dawggin = fs::read_to_string("/Users/2024oliverbindewald/Documents/2016/aoc_2016/src/bin/day_20.txt").expect("no");
    let raw_dawggin: Vec<&str> = raw_dawggin.lines().collect();
    let mut a: Vec<u32> = Vec::new();
    let mut b: Vec<u32> = Vec::new();
    for i in raw_dawggin {
        let ind = i.find('-').unwrap();
        a.push(i[0..ind].parse().unwrap());
        b.push(i[ind+1..i.len()].parse().unwrap());
    }
    let mut combined = merge_sort([a, b]);
    let mut i = 1;
    let mut max = combined[1][0];
    let mut sum = 0;
    while i < combined[0].len() {
        if (combined[0][i]-1 <= max) && (combined[1][i] > max) {
            max = combined[1][i];
        } else if combined[0][i]-1 > max{
            sum += combined[0][i]-max-1;
            max = combined[1][i];
        }
        i += 1;
    }
    if max != 4294967295{
        sum += 4294967295 - max - 1;
    }
    println!("{}", sum);

    println!("Runtime: {:?}", now.elapsed());
}
fn merge_sort(arr: [Vec<u32>;2]) -> [Vec<u32>; 2] {
    let arrlen = arr[0].len();
    if arrlen>1{
        let mut out: [Vec<u32>;2] = [Vec::new(),Vec::new()];
        
        let mid = arrlen/2;
        let left = merge_sort([arr[0][0..mid].to_vec(), arr[1][0..mid].to_vec()]);
        let right = merge_sort([arr[0][mid..arrlen].to_vec(), arr[1][mid..arrlen].to_vec()]);
        let llen = left[0].len();
        let rlen = right[0].len();
        
        let mut i = 0;
        let mut j = 0;

        while (i < llen) && (j < rlen) {
            if left[0][i] <= right[0][j] {
                out[0].push(left[0][i]);
                out[1].push(left[1][i]);
                i += 1;
            } else {
                out[0].push(right[0][j]);
                out[1].push(right[1][j]);
                j += 1;
            }
        }
        while i < llen {
            out[0].push(left[0][i]);
            out[1].push(left[1][i]);
            i += 1;
        }
        while j < rlen {
            out[0].push(right[0][j]);
            out[1].push(right[1][j]);
            j += 1;
        }
        return out
    } else {
        return arr
    }
}