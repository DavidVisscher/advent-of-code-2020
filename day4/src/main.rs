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
        println!("Passport: {}", &passport.get(&"pid".to_string()).get_or_insert(&"XXX".to_string()));
        for (key, value) in &passport {
            //println!(" - {} : {}", key, value);
        }
        let valid = verify_passport(&passport);
        println!(" - VALID: {}\n\n", &valid);
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
            println!(" - Invalid: Missing fields. ");
            return false;
        }
    }
    
    if ! verify_year(&passport, "byr".to_string(), 1920, 2002){
        println!(" - Invalid byr: {}", &passport.get(&"byr".to_string()).unwrap());
        return false 
    };
    if ! verify_year(&passport, "iyr".to_string(), 2010, 2020){ 
        println!(" - Invalid iyr: {}", &passport.get(&"iyr".to_string()).unwrap());
        return false 
    };
    if ! verify_year(&passport, "eyr".to_string(), 2020, 2030){ 
        println!(" - Invalid eyr: {}", &passport.get(&"eyr".to_string()).unwrap());
        return false 
    };
    if ! verify_height(&passport){ 
        println!(" - Invalid hgt: {}", &passport.get(&"hgt".to_string()).unwrap());
        return false };
    if ! verify_hair_color(&passport){ 
        println!(" - Invalid hcl: {}", &passport.get(&"hcl".to_string()).unwrap());
        return false };
    if ! verify_eye_color(&passport){ 
        println!(" - Invalid ecl: {}", &passport.get(&"ecl".to_string()).unwrap());
        return false };
    if ! verify_pid(&passport){ 
        println!(" - Invalid pid: {}", &passport.get(&"pid".to_string()).unwrap());
        return false };

    return true;
}

fn verify_year(passport: &HashMap<String,String> , field:String, minimum:u64, maximum:u64) -> bool {
    // Must be an int between 1920 and 2002.
    let value: u64 = passport.get(&field)
        .unwrap()
        .as_str()
        .parse::<u64>()
        .unwrap();

    if value >= minimum && value <= maximum {
        return true;
    }
    return false;
}

fn verify_height(passport: &HashMap<String,String>) -> bool {
    // Verify if height is within limits.
    
    let height: String = passport.get(&"hgt".to_string()).unwrap().clone();
    
    let value: u64 = height.clone()
        .replace("cm", "")
        .replace("in", "")
        .as_str()
        .parse::<u64>()
        .unwrap();

    if height.as_str().contains("in") && value >= 59 && value <= 76 {
        return true;
    }
    if height.as_str().contains("cm") && value >= 150 && value <= 193 {
        return true;
    }
    return false;
}

fn verify_hair_color(passport: &HashMap<String, String>) -> bool {
    // Verify the format of the hair color field.
    let valid_digits = vec!['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                            'a', 'b', 'c', 'd', 'e', 'f'];

    let mut value: String = passport.get(&"hcl".to_string()).unwrap().clone();
    
    if ! value.len() == 7 { return false; }

    for _ in 0..6 {
        let character_opt = value.pop();
        if character_opt.is_none() { return false; }
        let character = character_opt.unwrap();
        if ! valid_digits.contains(&character) { return false; }
    }
    let last_character_opt = value.pop();
    if last_character_opt.is_none() { return false; }
    let last_character = last_character_opt.unwrap();
    if last_character != '#' { return false; }

    return true;
}

fn verify_eye_color(passport: &HashMap<String, String>) -> bool {
    // Verify that the eye color is one of the valid options.
    let valid_options = vec![
        "amb".to_string(), 
        "blu".to_string(), 
        "brn".to_string(), 
        "gry".to_string(), 
        "grn".to_string(), 
        "hzl".to_string(), 
        "oth".to_string()
    ];
    
    let value: String = passport.get(&"ecl".to_string()).unwrap().clone();
    
    if value.len() != 3 { return false; };

    if valid_options.contains(&value) { return true; }
    return false;
}

fn verify_pid(passport: &HashMap<String, String>) -> bool {
    // Verify the format of the pid field.
    let valid_digits = vec!['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'];

    let mut value: String = passport.get(&"pid".to_string()).unwrap().clone();
    
    if ! value.len() == 9 { return false; }

    for _ in 0..9 {
        let character_opt = value.pop();
        if character_opt.is_none() { return false; }
        let character = character_opt.unwrap();
        if ! valid_digits.contains(&character) { return false; }
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
