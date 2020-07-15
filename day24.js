#!node

const fs = require('fs');

function sum(arr) {
    return arr.reduce((a, b) => a + b, 0);
}

function entanglement(weights) {
    return weights.reduce((a, b) => a * b, 1);
}

async function loadWeights() {
    const fileContent = await fs.promises.readFile('day24-input.txt', 'ascii');
    const weights = fileContent.split('\n').map(Number);
    return weights;
}

async function part1() {
    const weights = await loadWeights();
    const compartment = findBestFirstGroup(weights, 3);
    console.log(`Part 1: ${entanglement(compartment)}`);
}

async function part2() {
    const weights = await loadWeights();
    const compartment = findBestFirstGroup(weights, 4);
    console.log(`Part 2: ${entanglement(compartment)}`);
}

function findBestFirstGroup(weights, numGroups) {
    const totalWeight = sum(weights);
    const targetWeight = totalWeight / numGroups;

    function existsValidConfiguration(depth, usedWeights) {
        if (depth == numGroups) {
            return true;
        }

        return findLegalGroups(weights, usedWeights, targetWeight)
            .some(g => existsValidConfiguration(depth + 1, usedWeights.concat(g)));
    }

    let bestFirstGroup = null;
    for (const firstGroup of findLegalGroups(weights, [], targetWeight)) {
        const isSmaller =
            bestFirstGroup == null
            || firstGroup.length < bestFirstGroup.length
            || (firstGroup.length === bestFirstGroup.length
                && entanglement(firstGroup) < entanglement(bestFirstGroup));

        if (isSmaller && existsValidConfiguration(1, firstGroup)) {
            bestFirstGroup = firstGroup;
        }
    }

    return bestFirstGroup;
}

function findLegalGroups(weights, usedWeights, targetWeight) {
    const builder = [];
    function* inner(startIndex) {
        for (let i = startIndex; i < weights.length; i++) {
            if (!usedWeights.includes(weights[i])) {
                builder.push(weights[i])

                const builderSum = sum(builder);
                if (builderSum == targetWeight) {
                    yield [...builder];
                } else if (builderSum < targetWeight) {
                    yield* inner(i + 1);
                }

                builder.pop();
            }
        }
    }

    return Array.from(inner(0));
}

part1().then(part2);
