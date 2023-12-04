use std::collections::HashMap;

advent_of_code::solution!(3);

fn padded_input(input: &str) -> Vec<Vec<char>> {
    let mut grid: Vec<Vec<char>> = input.lines().map(|l| l.chars().collect()).collect();
    let width = grid[0].len();
    grid.insert(0, vec!['.'; width]);
    grid.push(vec!['.'; width]);
    for row in grid.iter_mut() {
        row.insert(0, '.');
        row.push('.');
    }
    grid
}

pub fn part_one(input: &str) -> Option<u32> {
    let grid = padded_input(input);
    let mut part_numbers: Vec<u32> = vec![];
    for (y, row) in grid.iter().enumerate() {
        let mut current_number = String::new();
        let mut is_part_number = false;
        for (x, c) in row.iter().enumerate() {
            if c.is_ascii_digit() {
                current_number.push(*c);
                for (nx, ny) in [
                    (x - 1, y - 1),
                    (x, y - 1),
                    (x + 1, y - 1),
                    (x - 1, y),
                    (x + 1, y),
                    (x - 1, y + 1),
                    (x, y + 1),
                    (x + 1, y + 1),
                ] {
                    let neighbour = grid[ny][nx];
                    if neighbour != '.' && !neighbour.is_ascii_digit() {
                        is_part_number = true;
                    }
                }
            } else if !current_number.is_empty() {
                if is_part_number {
                    part_numbers.push(current_number.parse().unwrap());
                }
                current_number.clear();
                is_part_number = false;
            }
        }
    }
    Some(part_numbers.into_iter().sum())
}

pub fn part_two(input: &str) -> Option<u32> {
    let grid = padded_input(input);
    let mut asterisks_parts = HashMap::new();
    for (y, row) in grid.iter().enumerate() {
        let mut current_number = String::new();
        let mut asterisk_pos = None;
        for (x, c) in row.iter().enumerate() {
            if c.is_ascii_digit() {
                current_number.push(*c);
                for (nx, ny) in [
                    (x - 1, y - 1),
                    (x, y - 1),
                    (x + 1, y - 1),
                    (x - 1, y),
                    (x + 1, y),
                    (x - 1, y + 1),
                    (x, y + 1),
                    (x + 1, y + 1),
                ] {
                    let neighbour = grid[ny][nx];
                    if neighbour == '*' {
                        asterisk_pos = Some((nx, ny));
                    }
                }
            } else if !current_number.is_empty() {
                if let Some(pos) = asterisk_pos {
                    let part_number = current_number.parse().unwrap();
                    asterisks_parts
                        .entry(pos)
                        .or_insert(Vec::<u32>::new())
                        .push(part_number);
                }
                current_number.clear();
                asterisk_pos = None;
            }
        }
    }
    Some(
        asterisks_parts
            .values()
            .filter(|part_numbers| part_numbers.len() == 2)
            .map(|part_numbers| part_numbers.iter().product::<u32>())
            .sum(),
    )
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(4361));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(467835));
    }
}
