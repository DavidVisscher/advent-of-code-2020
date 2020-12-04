use std::fs::File;
use std::io::BufReader;
use std::io::BufRead;


fn main() {
    let numberfile = File::open("numbers.dat").expect("Unable to open file.");
    let reader = BufReader::new(numberfile);

    let numbers: Vec<u64> = reader
        .lines()
        .map(|line| line.unwrap().parse::<u64>().unwrap())
        .collect();

    for x in numbers.iter() {
        for y in numbers.iter() {
            if x + y == 2020 {
                println!("{} {} = 2020, {} * {} = {}", x, y, x, y, x*y);
            }
        }
    }
}
