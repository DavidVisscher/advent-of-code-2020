use std::fs::File;
use std::io::BufReader;
use std::io::BufRead;

fn main() {
    let landscapefile = File::open("landscape.dat").expect("Unable to open file.");
    let reader = BufReader::new(landscapefile);
    
    let landscapedata: Vec<String> = reader
        .lines()
        .map(|line| 
            line.unwrap()
                .trim()
                .parse::<String>()
                .unwrap())
        .collect();

    let mut map = build_map(&landscapedata);

    let r1d1: u64 =  sled_down(0, 0, &mut map, 1, 1);
    println!("R1D1 Trees encountered: {}", &r1d1);
    let r3d1: u64 =  sled_down(0, 0, &mut map, 3, 1);
    println!("R3D1 Trees encountered: {}", &r3d1);
    let r5d1: u64 =  sled_down(0, 0, &mut map, 5, 1);
    println!("R5D1 Trees encountered: {}", &r5d1);
    let r7d1: u64 =  sled_down(0, 0, &mut map, 7, 1);
    println!("R7D1 Trees encountered: {}", &r7d1);
    let r1d2: u64 =  sled_down(0, 0, &mut map, 1, 2);
    println!("R1D2 Trees encountered: {}", &r1d2);
    println!("Combined Product      : {}", r1d1 * r3d1 * r5d1 * r7d1 * r1d2 )
}

fn build_map(landscapedata: &Vec<String>) -> Vec<Vec<String>> {
    // turns the lines read from the file into a 2d Vec
    let mut map: Vec<Vec<String>> = Vec::new();

    for line in landscapedata.iter() {
        let mut row: Vec<String> = Vec::new();
        for character in line.chars() {
            row.push(String::from(character));
        }
        map.push(row);
    }

    return map;
}

fn sled_down(start_x: usize, start_y: usize, map: &mut Vec<Vec<String>>, move_x: usize, move_y: usize) -> u64 {
    // Moves the tobogan across the map and returns the amount of trees encountered.
    let mut current_x = start_x.clone();
    let mut current_y = start_y.clone();
    
    let mut trees: u64 = 0;
    let map_width = map[0].len();
    
    while current_y < map.len() {
        //println!("At [{}, {}] : {} - Trees: {}", &current_x, &current_y, &map[current_y][current_x], &trees);
        if map[current_y][current_x] == "#" {
            trees += 1;
        }

        current_x += move_x;
        current_x = current_x % map_width;

        current_y += move_y;
    }


    return trees;
}