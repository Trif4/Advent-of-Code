use itertools::enumerate;
use std::collections::HashSet;
use std::str::FromStr;

advent_of_code::solution!(4);

struct Card {
    winning: HashSet<u32>,
    have: HashSet<u32>,
}

impl Card {
    fn win_count(&self) -> usize {
        self.winning.intersection(&self.have).count()
    }
}

fn parse_card_numbers(numbers: &str) -> HashSet<u32> {
    numbers
        .split_whitespace()
        .map(|n| n.parse().unwrap())
        .collect()
}

impl FromStr for Card {
    type Err = ();

    fn from_str(s: &str) -> Result<Self, ()> {
        let (_, body) = s.split_once(':').ok_or(())?;
        let (winning, have) = body.split_once('|').ok_or(())?;
        Ok(Card {
            winning: parse_card_numbers(winning),
            have: parse_card_numbers(have),
        })
    }
}

pub fn part_one(input: &str) -> Option<u32> {
    let cards: Vec<Card> = input.lines().map(|line| line.parse().unwrap()).collect();
    Some(
        cards
            .into_iter()
            .map(|card| u32::pow(2, card.win_count() as u32) / 2)
            .sum(),
    )
}

pub fn part_two(input: &str) -> Option<u32> {
    let cards: Vec<Card> = input.lines().map(|line| line.parse().unwrap()).collect();
    let mut counts = vec![1; cards.len()];
    for (i, card) in enumerate(cards) {
        let count = counts[i];
        for j in 1..=card.win_count() {
            counts[i + j] += count;
        }
    }
    Some(counts.iter().sum())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(13));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(30));
    }
}
