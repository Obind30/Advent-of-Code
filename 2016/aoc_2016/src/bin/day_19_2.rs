fn main() {
    let now = std::time::Instant::now();

    let elve_count: i32 = 3014387;
    let log3 = 3_i32.pow(elve_count.ilog(3));
    if elve_count == log3{
        println!("{}", elve_count);
    } else if elve_count-log3 <= log3{
        println!("{}", elve_count-log3);
    } else {
        println!("{}",log3+(2*(elve_count-2*log3)));
    }
    

    /*for j in 1..82{           //Naieve solution to find better solution
        let elve_count = j;
        let mut elves: Vec<i32> = (1..elve_count+1).collect();
        let mut len = elve_count;
        let mut index = 0;
        for _i in 0..(elve_count-1) {
            let rem = elves[(((len/2)+(index))%len) as usize];
            //println!("{:?}---{}---{}",elves, rem, index);
            elves.remove((((len/2)+(index))%len) as usize);
            if rem < elves[(index%(len-1)) as usize] {
                index -= 1;
            }
            len -= 1;
            index += 1; 
            index = index%(len+1);
        }
        println!("{}", elves[0]);
    }*/
    
    
    println!("Runtime: {:?}", now.elapsed());
}