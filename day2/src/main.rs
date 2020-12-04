use std::fs::File;
use std::io::BufReader;
use std::io::BufRead;

fn main() {
    let passwordfile = File::open("passwords.dat").expect("Unable to open file.");
    let reader = BufReader::new(passwordfile);

    let passwords: Vec<String> = reader.lines().map(|line| line.unwrap().parse::<String>().unwrap()).collect();
    
    let mut correct_passwords = 0;

    for password in passwords.iter() {
        if check_password_pt1(&password) {
            correct_passwords += 1;
        }
    }
    println!("Correct Passwords (Part 1): {}", correct_passwords);

    correct_passwords = 0;

    for password in passwords.iter() {
        if check_password_pt2(&password) {
            correct_passwords += 1;
        }
    }
    println!("Correct Passwords (Part 2): {}", correct_passwords);
}

fn check_password_pt1(password_line: &String) -> bool {
    // Split line on whitespace.
    // This way we end up with
    // 0: number-number
    // 1: letter:
    // 2: password
    let split: Vec<&str> = password_line.split(" ").collect();

    let bounds: Vec<&str> = split[0].trim().split("-").collect();
    let minimum: u64 = bounds[0].parse::<u64>().unwrap();
    let maximum: u64 = bounds[1].parse::<u64>().unwrap();

    let limited_character = String::from(split[1].trim().replace(":", ""));
    let password = String::from(split[2].trim());

    let mut occurrences: u64 = 0;

    for character in password.chars() {
        if String::from(character) == limited_character {
            occurrences += 1;
        }
    }
    
    if occurrences >= minimum && occurrences <= maximum {
        return true;
    }
    return false;
}

fn check_password_pt2(password_line: &String) -> bool {
    // Split line on whitespace.
    // This way we end up with
    // 0: number-number
    // 1: letter:
    // 2: password
    let split: Vec<&str> = password_line.split(" ").collect();

    let positions: Vec<&str> = split[0].trim().split("-").collect();
    let p1: usize = positions[0].parse::<usize>().unwrap();
    let p2: usize = positions[1].parse::<usize>().unwrap();

    let limited_character = String::from(split[1].trim().replace(":", ""));
    let password = String::from(split[2].trim());

    let mut occurrences: u64 = 0;

    for (char_index, character) in password.char_indices() {
        if char_index+1 == p1 || char_index+1 == p2 {
            if String::from(character) == limited_character {
                occurrences += 1;
            }
        }
    }
    if occurrences == 1 {
        return true;
    }
    return false;
}
