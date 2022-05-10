fn print_word(s: &str) {
    print!("{}", s);
    print!("{}", s);

}

fn main() {
    let s: &str = "Dog";
    print_word(s);
}