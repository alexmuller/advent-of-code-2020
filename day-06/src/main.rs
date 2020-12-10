use std::env;
use std::fs;

// I've never written any Rust before :/

fn part_1() {
    let input_file = env::args().nth(1).expect("No input file given");
    let input_data = fs::read_to_string(input_file).expect("Error reading input file");
    let customs_declarations = input_data.split("\n\n");

    let mut unique_answer_count = 0;

    for group in customs_declarations {
        let mut chars: Vec<char> = group.chars().collect();
        chars.sort_by(|a, b| a.cmp(b));
        chars.dedup();
        chars.retain(|&x| x != '\n');

        unique_answer_count += chars.len();
    }

    println!("Part 1: {}", unique_answer_count);
}

fn part_2() {
    let input_file = env::args().nth(1).expect("No input file given");
    let input_data = fs::read_to_string(input_file).expect("Error reading input file");
    let customs_declarations = input_data.split("\n\n");

    let questions = (b'a'..=b'z')
        .map(|c| c as char)
        .filter(|c| c.is_alphabetic())
        .collect::<Vec<_>>();

    let mut all_group_participants_yes = 0;

    for group in customs_declarations {
        let mut group_participants: Vec<&str> = group.split("\n").collect();
        group_participants.retain(|&x| x != "");
        let group_size = group_participants.len();

        let mut answers: Vec<char> = group.chars().collect();
        answers.sort_by(|a, b| a.cmp(b));
        answers.retain(|&x| x != '\n');

        for question in &questions {
            let mut question_answers = answers.clone();
            question_answers.retain(|x| x == question);
            if question_answers.len() == group_size {
                all_group_participants_yes += 1;
            }
        }
    }

    println!("Part 2: {}", all_group_participants_yes);
}

fn main() {
    part_1();
    part_2();
}
