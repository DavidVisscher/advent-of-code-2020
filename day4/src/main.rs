use std::fs::File;
use std::io::BufReader;
use std::io::BufRead;
use std::collections::HashMap;

fn main() {
    let passportfile = File::open("passports.dat").expect("Unable to open file.");
    let reader = BufReader::new(passportfile);

    let passportlines: Vec<String> = reader
        .lines()
        .map(|line|
             line.unwrap()
                 .trim()
                 .parse::<String>()
                 .unwrap())
        .collect();

    let raw_passports = split_raw_passports(&passportlines);

    let mut passports: Vec<HashMap<String, String>> = Vec::new();

    for raw_passport in raw_passports {
        passports.push(parse_passport(raw_passport.trim().to_string()));
    }
    
    let mut valid_passports: u64 = 0;

    for passport in passports {
        println!("Passport:");
        for (key, value) in &passport {
            println!(" - {} : {}", key, value);
        }
        let valid = verify_passport(&passport);
        println!(" - VALID: {}", &valid);
        if valid { valid_passports += 1; }
    }

    println!("\n\nValid Passports: {}", valid_passports);
}

fn verify_passport(passport: &HashMap<String, String>) -> bool {
    // Checks if a passport has all required fields.

    let required_fields = vec![
        String::from("byr"), 
        String::from("iyr"),
        String::from("eyr"),
        String::from("hgt"),
        String::from("hcl"), 
        String::from("ecl"),
        String::from("pid") ]; // cid is optional

    for field in required_fields {
        if ! passport.contains_key(&field.to_string()) {
            return false;
        }
    }
    return true;
}

fn parse_passport(raw_passport: String) -> HashMap<String, String> {
    // Parses a single passport entry into a HashMap.
    let mut passport: HashMap<String, String> = HashMap::new();
    let pairs: Vec<&str> = raw_passport.split(" ").collect();
    for pair in pairs {
        let kvpair: Vec<&str> = pair.split(":").collect();
        passport.insert(String::from(kvpair[0].trim()), String::from(kvpair[1].trim()));
    }
    return passport;
}

fn split_raw_passports(passportlines: &Vec<String>) -> Vec<String> {
    // Splits the passports at each empty line.
    let mut raw_passports: Vec<String> = Vec::new();

    let mut current_passport = String::from("");
    for line in passportlines {
        let linestring = String::from(line).replace("\n", " ").replace("\r", "");
        if linestring == "" {
            raw_passports.push(current_passport.clone());
            current_passport = String::from("");
        }
        else {
            current_passport.push_str(" ");
            current_passport.push_str(linestring.as_str());
        }
    }

    return raw_passports;
}
