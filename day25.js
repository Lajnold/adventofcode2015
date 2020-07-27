#!node

code_1_1 = 20151125
required_row = 2981
required_column = 3075

function part1() {
    function find() {
        let code = code_1_1;
        for (let row = 1; ; row++) {
            let r = row;
            let c = 1;

            while (r > 0) {
                if (r === required_row && c === required_column) {
                    return code;
                }

                r--;
                c++;
                code = code * 252533 % 33554393;
            }
        }
    }

    console.log(`Part 1: ${find()}`);
}

part1()
