extern crate termion;

// fn main() {
//     print!("{}{}Stuff", termion::clear::All, termion::cursor::Goto(1, 1));
//     print!("{}{}Things", termion::clear::All, termion::cursor::Goto(1, 1));
// }

// fn main() {
//     let mut stdout = stdout();

//     for i in 0..=100 {
//         print!("\rProcessing {}%...", i);
//         // or
//         // stdout.write(format!("\rProcessing {}%...", i).as_bytes()).unwrap();
//         stdout.flush().unwrap();
//         sleep(Duration::from_millis(20));
//     }
//     println!();
// }

use std::{thread::sleep, time::Duration};

fn game_loop() {
    let mut arr: [[i8; 10]; 10] = [[0; 10]; 10];
    let mut i: i16 = 0;
    while i < 1000 {
        for a in arr {
            println!("{:?}", a);
        };
        let mut b: usize= (i%10) as usize;
        let mut a: usize= ((i/10)%10) as usize;
        arr[a][b] += 1;
        i+=1;
        sleep(Duration::from_millis(100));
        print!("{}{}", termion::clear::All, termion::cursor::Goto(1, 1));
    }

    // arr[0][1] = 4;
    // for a in arr {
    //     println!("{:?}", a)
    // }
    // sleep(Duration::from_millis(100));
}

fn main() {
    game_loop();
}