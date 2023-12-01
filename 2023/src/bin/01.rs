use regex::Regex;

advent_of_code::solution!(1);

pub fn part_one(input: &str) -> Option<u32> {
    Some(
        input
            .lines()
            .map(|l| {
                format!(
                    "{}{}",
                    l.chars().find(|&c: &char| c.is_ascii_digit()).unwrap(),
                    l.chars().rfind(|&c: &char| c.is_ascii_digit()).unwrap()
                )
                .parse::<u32>()
                .unwrap()
            })
            .sum(),
    )
}

fn parse_elvish_number(s: &str) -> &str {
    match s {
        "one" => "1",
        "two" => "2",
        "three" => "3",
        "four" => "4",
        "five" => "5",
        "six" => "6",
        "seven" => "7",
        "eight" => "8",
        "nine" => "9",
        d => d,
    }
}

pub fn part_two(input: &str) -> Option<u32> {
    let re_first = Regex::new(r"(\d|one|two|three|four|five|six|seven|eight|nine)").unwrap();
    let re_last = Regex::new(r".*(\d|one|two|three|four|five|six|seven|eight|nine)").unwrap();
    Some(
        input
            .lines()
            .map(|l| {
                format!(
                    "{}{}",
                    parse_elvish_number(re_first.find(l).unwrap().as_str()),
                    parse_elvish_number(&re_last.captures(l).unwrap()[1]),
                )
                .parse::<u32>()
                .unwrap()
            })
            .sum(),
    )
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(142));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(281));
    }
}
