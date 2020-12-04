use std::fs::File;
use std::io::BufReader;
use std::io::BufRead;

fn main() {
    let passwordfile = File::open("passwords.dat").expect("Unable to open file.");
    let reader = BufReader::new(passwordfile);

    let passwords: Vec<String> = reader.lines().map(|line| line.unwrap().parse::<String>().unwrap()).collect();
    
    let mut correct_passwords = 0;

    for password in passwords.iter() {
        if check_password(&password) {
            correct_passwords += 1;
        }
    }

    println!("Correct Passwords: {}", correct_passwords)
}

fn check_password(password_line: &String) -> bool {
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
