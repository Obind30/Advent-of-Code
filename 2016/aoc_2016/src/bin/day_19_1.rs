fn main(){
    let now = std::time::Instant::now();

    let elve_count: i32 = 3014387;
    println!("{}", (elve_count as u32 -(2_u32.pow(elve_count.ilog2())))*2+1);
    
    println!("Runtime: {:?}", now.elapsed());
}