use nom::branch::alt;
use nom::bytes::complete::tag;
use nom::character::complete::{char, u32 as nom_u32};
use nom::multi::separated_list1;
use nom::sequence::{delimited, separated_pair, Tuple};
use nom::IResult;
use nom::Parser;
use std::cmp::max;

advent_of_code::solution!(2);

enum Colour {
    Red,
    Green,
    Blue,
}

struct Cubes {
    count: u32,
    colour: Colour,
}

struct Set {
    groups: Vec<Cubes>,
}

struct Game {
    id: u32,
    sets: Vec<Set>,
}

fn game_id(input: &str) -> IResult<&str, u32> {
    delimited(tag("Game "), nom_u32, tag(": "))(input)
}

// Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
fn parse_game(line: &str) -> Game {
    let red = tag("red").map(|_| Colour::Red);
    let green = tag("green").map(|_| Colour::Green);
    let blue = tag("blue").map(|_| Colour::Blue);
    let colour = alt((red, green, blue));
    let cubes =
        separated_pair(nom_u32, char(' '), colour).map(|(count, colour)| Cubes { count, colour });
    let set = separated_list1(tag(", "), cubes).map(|groups| Set { groups });
    let sets = separated_list1(tag("; "), set);
    let (_, (id, sets)) = (game_id, sets).parse(line).unwrap();
    Game { id, sets }
}

pub fn part_one(input: &str) -> Option<u32> {
    Some(
        input
            .lines()
            .map(parse_game)
            .filter(|game| {
                game.sets.iter().all(|set| {
                    set.groups.iter().all(|cubes| match cubes.colour {
                        Colour::Red => cubes.count <= 12,
                        Colour::Green => cubes.count <= 13,
                        Colour::Blue => cubes.count <= 14,
                    })
                })
            })
            .map(|game| game.id)
            .sum(),
    )
}

pub fn part_two(input: &str) -> Option<u32> {
    Some(
        input
            .lines()
            .map(parse_game)
            .map(|game| {
                let mut red = 0;
                let mut green = 0;
                let mut blue = 0;
                for set in game.sets {
                    for cubes in set.groups {
                        match cubes.colour {
                            Colour::Red => red = max(red, cubes.count),
                            Colour::Green => green = max(green, cubes.count),
                            Colour::Blue => blue = max(blue, cubes.count),
                        }
                    }
                }
                red * green * blue
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
        assert_eq!(result, Some(8));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(2286));
    }
}
